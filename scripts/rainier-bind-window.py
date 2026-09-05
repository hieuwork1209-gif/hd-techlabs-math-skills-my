#!/usr/bin/env python3
r"""Bind a Rainier problem to the currently selected Chrome window on Windows.

Run this from WSL2 after /rainier-next-check has stored the problem's ChatGPT
conversation URL on origin/adversary/problemNN. The binding is local-only:

- WSL mirror: .tmp/codex-adversary/problemNN-window.json
- Windows runtime copy: %LOCALAPPDATA%\Rainier\window-bindings\problemNN.json

No account email, Chrome profile, or browser credentials are read or stored.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
STATE_ROOT = ROOT / ".tmp" / "codex-adversary"
HANDLER_SOURCE = Path(__file__).with_name("rainier-window-handler.ps1")
PROBLEM_RE = re.compile(r"^problem[0-9]+$")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run(cmd: list[str], *, cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(
        cmd,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if check and p.returncode != 0:
        detail = (p.stderr or p.stdout or f"exit {p.returncode}").strip()
        raise RuntimeError(detail)
    return p


def git(*args: str, check: bool = True) -> str:
    return run(["git", *args], check=check).stdout.strip()


def powershell(script: str, *, check: bool = True) -> subprocess.CompletedProcess[str]:
    encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
    return run(
        [
            "powershell.exe",
            "-NoProfile",
            "-NonInteractive",
            "-EncodedCommand",
            encoded,
        ],
        check=check,
    )


def valid_chat_url(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    try:
        parsed = urlparse(value)
    except ValueError:
        return None
    if parsed.scheme != "https" or parsed.hostname not in {"chatgpt.com", "chat.openai.com"}:
        return None
    if "/c/" not in parsed.path:
        return None
    return value


def remote_chat_url(problem: str, branch: str) -> str:
    git("fetch", "-q", "origin", f"+refs/heads/{branch}:refs/remotes/origin/{branch}")
    binding_path = f"solver-results/{problem}/chat-binding.json"
    raw = git("show", f"origin/{branch}:{binding_path}", check=False)
    if not raw:
        raise RuntimeError(
            f"missing {binding_path} on {branch}; run /rainier-next-check with the chat URL first"
        )
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid JSON in {binding_path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"invalid binding object in {binding_path}")
    direct = valid_chat_url(str(data.get("chat_url") or ""))
    if direct:
        return direct
    conversation_id = str(data.get("conversation_id") or "").strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{8,200}", conversation_id):
        return f"https://chatgpt.com/c/{conversation_id}"
    raise RuntimeError(f"{binding_path} does not contain a valid ChatGPT conversation URL")


def capture_chrome_window() -> dict:
    script = r'''
$ErrorActionPreference = 'Stop'
Add-Type @"
using System;
using System.Runtime.InteropServices;
public static class RainierCapture {
    [DllImport("user32.dll")]
    public static extern IntPtr GetForegroundWindow();

    [DllImport("user32.dll")]
    public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);
}
"@

while ($true) {
    Start-Sleep -Milliseconds 250
    $hwnd = [RainierCapture]::GetForegroundWindow()
    if ($hwnd -eq [IntPtr]::Zero) { continue }

    [uint32]$targetProcessId = 0
    [RainierCapture]::GetWindowThreadProcessId($hwnd, [ref]$targetProcessId) | Out-Null
    if ($targetProcessId -eq 0) { continue }

    try {
        $proc = Get-Process -Id ([int]$targetProcessId) -ErrorAction Stop
    } catch {
        continue
    }

    if ($proc.ProcessName -ne 'chrome') { continue }

    $record = [ordered]@{
        hwnd = [int64]$hwnd.ToInt64()
        pid = [int]$targetProcessId
        process_name = $proc.ProcessName
        title = $proc.MainWindowTitle
    }
    Write-Output ('RAINIER_BIND_JSON=' + ($record | ConvertTo-Json -Compress))
    break
}
'''
    p = powershell(script)
    marker = "RAINIER_BIND_JSON="
    for line in p.stdout.splitlines():
        if line.startswith(marker):
            try:
                data = json.loads(line[len(marker):])
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"could not parse captured Chrome window: {exc}") from exc
            if not isinstance(data, dict):
                break
            return data
    detail = (p.stderr or p.stdout).strip()
    raise RuntimeError(f"PowerShell did not return a Chrome window binding: {detail}")


def install_windows_runtime(problem: str, binding: dict) -> str:
    if not HANDLER_SOURCE.exists():
        raise RuntimeError(f"missing protocol handler source: {HANDLER_SOURCE}")

    handler_b64 = base64.b64encode(HANDLER_SOURCE.read_bytes()).decode("ascii")
    binding_bytes = (json.dumps(binding, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    binding_b64 = base64.b64encode(binding_bytes).decode("ascii")

    script = rf'''
$ErrorActionPreference = 'Stop'
$root = Join-Path $env:LOCALAPPDATA 'Rainier'
$bindingDir = Join-Path $root 'window-bindings'
New-Item -ItemType Directory -Force -Path $bindingDir | Out-Null

$handlerPath = Join-Path $root 'rainier-window-handler.ps1'
$handlerBytes = [Convert]::FromBase64String('{handler_b64}')
[IO.File]::WriteAllBytes($handlerPath, $handlerBytes)

$bindingPath = Join-Path $bindingDir '{problem}.json'
$bindingBytes = [Convert]::FromBase64String('{binding_b64}')
[IO.File]::WriteAllBytes($bindingPath, $bindingBytes)

$protocolRoot = 'HKCU:\Software\Classes\rainier-chat'
$commandKey = Join-Path $protocolRoot 'shell\open\command'
New-Item -Force -Path $commandKey | Out-Null
Set-Item -Path $protocolRoot -Value 'URL:Rainier Chat Window'
New-ItemProperty -Path $protocolRoot -Name 'URL Protocol' -Value '' -PropertyType String -Force | Out-Null

$psExe = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
$command = '"' + $psExe + '" -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "' + $handlerPath + '" "%1"'
Set-Item -Path $commandKey -Value $command

Write-Output ('RAINIER_WINDOWS_BINDING=' + $bindingPath)
'''
    p = powershell(script)
    marker = "RAINIER_WINDOWS_BINDING="
    for line in p.stdout.splitlines():
        if line.startswith(marker):
            return line[len(marker):].strip()
    detail = (p.stderr or p.stdout).strip()
    raise RuntimeError(f"could not install Windows Rainier protocol handler: {detail}")


def load_local_binding(problem: str) -> tuple[Path, dict]:
    local_path = STATE_ROOT / f"{problem}-window.json"
    try:
        data = json.loads(local_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeError(f"missing local binding: {local_path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid local binding JSON: {exc}") from exc

    if not isinstance(data, dict) or str(data.get("problem") or "") != problem:
        raise RuntimeError(f"local binding does not belong to {problem}")
    if str(data.get("process_name") or "").lower() != "chrome":
        raise RuntimeError("local binding does not point to Chrome")
    try:
        if int(data.get("hwnd") or 0) <= 0 or int(data.get("pid") or 0) <= 0:
            raise ValueError
    except (TypeError, ValueError) as exc:
        raise RuntimeError("local binding has an invalid HWND/PID") from exc
    return local_path, data


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Bind problemNN to the Chrome window you select on Windows."
    )
    ap.add_argument("problem", help="e.g. problem81")
    ap.add_argument("--branch", help="default: adversary/<problem>")
    ap.add_argument(
        "--refresh-runtime",
        action="store_true",
        help="reinstall the Windows handler from the current repo without recapturing HWND",
    )
    args = ap.parse_args()

    if not PROBLEM_RE.fullmatch(args.problem):
        print("error: problem must look like problem81", file=sys.stderr)
        return 2
    branch = args.branch or f"adversary/{args.problem}"

    if not os.environ.get("WSL_DISTRO_NAME") and "microsoft" not in os.uname().release.lower():
        print("error: this binder is intended to run inside WSL2", file=sys.stderr)
        return 2
    if not shutil.which("git"):
        print("error: git not found on PATH", file=sys.stderr)
        return 2
    if not shutil.which("powershell.exe"):
        print("error: powershell.exe not found; Windows interop is unavailable", file=sys.stderr)
        return 2

    if args.refresh_runtime:
        try:
            local_path, binding = load_local_binding(args.problem)
            windows_path = install_windows_runtime(args.problem, binding)
        except Exception as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        print("[rainier-window] REFRESHED")
        print(f"[rainier-window] HWND : {binding['hwnd']}")
        print(f"[rainier-window] PID  : {binding['pid']}")
        print(f"[rainier-window] local: {local_path.relative_to(ROOT)}")
        print(f"[rainier-window] win  : {windows_path}")
        print(
            f"[rainier-window] test: python scripts/codex-adversary-watch-chat.py "
            f"{args.problem} --notify-test"
        )
        return 0

    try:
        chat_url = remote_chat_url(args.problem, branch)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(f"[rainier-window] {args.problem}")
    print(f"[rainier-window] chat: {chat_url}")
    print("[rainier-window] click the Chrome window/account that owns this chat...")
    print("[rainier-window] waiting until that Chrome window becomes foreground", flush=True)

    try:
        captured = capture_chrome_window()
        binding = {
            "problem": args.problem,
            "hwnd": int(captured["hwnd"]),
            "pid": int(captured["pid"]),
            "process_name": str(captured.get("process_name") or "chrome"),
            "title": str(captured.get("title") or ""),
            "bound_at": now(),
        }
        STATE_ROOT.mkdir(parents=True, exist_ok=True)
        local_path = STATE_ROOT / f"{args.problem}-window.json"
        local_path.write_text(
            json.dumps(binding, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        windows_path = install_windows_runtime(args.problem, binding)
    except KeyboardInterrupt:
        print("\n[rainier-window] cancelled", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print("[rainier-window] BOUND")
    print(f"[rainier-window] HWND : {binding['hwnd']}")
    print(f"[rainier-window] PID  : {binding['pid']}")
    print(f"[rainier-window] TITLE: {binding['title']}")
    print(f"[rainier-window] local: {local_path.relative_to(ROOT)}")
    print(f"[rainier-window] win  : {windows_path}")
    print(
        f"[rainier-window] test: python scripts/codex-adversary-watch-chat.py "
        f"{args.problem} --notify-test"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
