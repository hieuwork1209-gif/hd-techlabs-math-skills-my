#!/usr/bin/env python3
"""Blind-solve each new adversary problem.md once with Codex GPT-5.4 High.

The watcher never runs Codex inside the Rainier repo. It extracts only the
normalized statement into a temporary directory, runs one ephemeral Codex exec,
and writes the result back under solver-results/<problem>/.

Each completed attempt also updates solver-results/<problem>/latest.json so a
later ChatGPT web turn can immediately see the latest local verdict. A timeout
is recorded explicitly as LOCAL_STUMPED_BY_TIMEOUT and marks the candidate as
ready to promote to main for official Rainier testing.

On WSL2, completed attempts can raise a native Windows toast through
powershell.exe. The toast copies ``next`` to the Windows clipboard and, when a
ChatGPT conversation URL is configured for the problem, clicking the toast or
Open Chat opens that exact conversation. Chat URLs are local-only state under
.tmp/codex-adversary/ and are never written to solver-results or pushed.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import os
import platform
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_ROOT = ROOT / ".tmp" / "codex-adversary"
CHAT_URLS_FILE = STATE_ROOT / "chat-urls.json"
PROBLEM_ROOT = "workspace/rainier-problem"

STATEMENT_HEAD = re.compile(r"^##\s*LaTeX\s*\(Normalized\)\s*$", re.M | re.I)
NEXT_HEAD = re.compile(r"^##\s+", re.M)
LEAKY_HEAD = re.compile(r"^##\s*(Domain Classification|Domain Explanation)\s*$", re.M | re.I)
LEAKY_BOLD = re.compile(r"^\*\*(Domain|Sub-?domain|Domain Explanation|Problem Type|Answer Type|Difficulty)\b", re.M | re.I)

PROMPT_HEAD = """You are being measured on whether you can solve this problem cold.
Use only your own mathematical reasoning and the statement below.
Do not use memory, other conversations, GitHub, connected apps, web search,
browsing, external files, or external sources. If outside material about this
problem appears, ignore it and solve from scratch.
Give a complete self-contained solution and finish with a clearly stated final
answer in exactly the form requested.

--- PROBLEM ---
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run(cmd: list[str], cwd: Path = ROOT, check: bool = True, timeout: int | None = None):
    """Run a command and kill its whole process group if the timeout expires."""
    p = subprocess.Popen(
        cmd,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
    )
    try:
        stdout, stderr = p.communicate(timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        try:
            os.killpg(p.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            stdout, stderr = p.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(p.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = p.communicate()
        raise subprocess.TimeoutExpired(
            cmd,
            timeout,
            output=stdout,
            stderr=stderr,
        ) from exc

    completed = subprocess.CompletedProcess(cmd, p.returncode, stdout, stderr)
    if check and completed.returncode != 0:
        raise RuntimeError((completed.stderr or completed.stdout or f"exit {completed.returncode}").strip())
    return completed


def git(*args: str, check: bool = True, cwd: Path = ROOT) -> str:
    return run(["git", *args], cwd=cwd, check=check).stdout.strip()


def statement_only(text: str) -> str:
    m = STATEMENT_HEAD.search(text)
    if m:
        rest = text[m.end():]
        nxt = NEXT_HEAD.search(rest)
        body = rest[:nxt.start()] if nxt else rest
        return body.strip().strip("-").strip() + "\n"
    cuts = [m.start() for m in (LEAKY_HEAD.search(text), LEAKY_BOLD.search(text)) if m]
    return (text[:min(cuts)] if cuts else text).strip() + "\n"


def fetch_branch(branch: str) -> None:
    git("fetch", "-q", "origin", f"+refs/heads/{branch}:refs/remotes/origin/{branch}")


def resolve_problem_path(problem: str, branch: str) -> str:
    ref = f"origin/{branch}"
    names = git("ls-tree", "-r", "--name-only", ref, PROBLEM_ROOT).splitlines()
    prefix = f"{PROBLEM_ROOT}/{problem}-"
    hits = [x for x in names if x.startswith(prefix) and x.endswith("/problem.md")]
    if len(hits) != 1:
        raise RuntimeError(f"expected one {problem}-*/problem.md on {branch}; found {hits}")
    return hits[0]


def state_file(problem: str) -> Path:
    return STATE_ROOT / f"{problem}.json"


def load_state(problem: str) -> dict:
    p = state_file(problem)
    if not p.exists():
        return {"attempted_blobs": {}}
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(problem: str, state: dict) -> None:
    STATE_ROOT.mkdir(parents=True, exist_ok=True)
    state_file(problem).write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_chat_urls() -> dict[str, str]:
    if not CHAT_URLS_FILE.exists():
        return {}
    try:
        data = json.loads(CHAT_URLS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {str(k): str(v) for k, v in data.items()} if isinstance(data, dict) else {}


def save_chat_url(problem: str, url: str) -> None:
    if not re.match(r"^https?://", url, re.I):
        raise ValueError("--chat-url must be an http(s) URL")
    STATE_ROOT.mkdir(parents=True, exist_ok=True)
    data = load_chat_urls()
    data[problem] = url
    tmp = CHAT_URLS_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(CHAT_URLS_FILE)


def chat_url_for(problem: str, cli_url: str | None = None) -> str | None:
    if cli_url:
        return cli_url
    env_specific = os.environ.get(f"RAINIER_CHAT_{problem.upper()}")
    if env_specific:
        return env_specific
    if os.environ.get("RAINIER_CHAT_URL"):
        return os.environ["RAINIER_CHAT_URL"]
    return load_chat_urls().get(problem)


def repo_slug() -> str | None:
    remote = git("remote", "get-url", "origin", check=False)
    m = re.search(r"github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$", remote)
    return m.group(1) if m else None


def github_file_url(branch: str, rel: Path | str) -> str | None:
    slug = repo_slug()
    if not slug:
        return None
    path = str(rel).replace(os.sep, "/")
    return f"https://github.com/{slug}/blob/{branch}/{path}"


def is_wsl() -> bool:
    if os.environ.get("WSL_DISTRO_NAME") or os.environ.get("WSL_INTEROP"):
        return True
    return "microsoft" in platform.release().lower()


def run_powershell(script: str, timeout: int = 15) -> subprocess.CompletedProcess:
    encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
    return subprocess.run(
        ["powershell.exe", "-NoProfile", "-NonInteractive", "-EncodedCommand", encoded],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )


def windows_toast(title: str, body: str, chat_url: str | None, result_url: str | None) -> tuple[bool, str]:
    """Send a native Windows toast from WSL without requiring extra modules."""
    if not shutil.which("powershell.exe"):
        return False, "powershell.exe not found"

    primary = chat_url or result_url or "https://chatgpt.com/"
    title_xml = html.escape(title, quote=True)
    body_xml = html.escape(body, quote=True)
    primary_xml = html.escape(primary, quote=True)
    chat_xml = html.escape(chat_url, quote=True) if chat_url else ""
    result_xml = html.escape(result_url, quote=True) if result_url else ""

    actions = []
    if chat_url:
        actions.append(
            f'<action content="Open Chat" activationType="protocol" arguments="{chat_xml}"/>'
        )
    if result_url:
        actions.append(
            f'<action content="Open Result" activationType="protocol" arguments="{result_xml}"/>'
        )
    action_xml = "<actions>" + "".join(actions) + "</actions>" if actions else ""

    toast_xml = (
        f'<toast activationType="protocol" launch="{primary_xml}">'
        '<visual><binding template="ToastGeneric">'
        f'<text>{title_xml}</text>'
        f'<text>{body_xml}</text>'
        '<text placement="attribution">next copied to clipboard</text>'
        '</binding></visual>'
        f'{action_xml}'
        '</toast>'
    )

    # Single-quoted here-string avoids PowerShell interpolation inside the XML.
    ps = f"""
$ErrorActionPreference = 'Stop'
Set-Clipboard -Value 'next'
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] > $null
$xmlText = @'
{toast_xml}
'@
$doc = New-Object Windows.Data.Xml.Dom.XmlDocument
$doc.LoadXml($xmlText)
$toast = [Windows.UI.Notifications.ToastNotification]::new($doc)
$app = Get-StartApps | Where-Object {{ $_.Name -match '^Windows Terminal$' }} | Select-Object -First 1
if (-not $app) {{ $app = Get-StartApps | Where-Object {{ $_.Name -match 'PowerShell' }} | Select-Object -First 1 }}
if (-not $app) {{ $app = Get-StartApps | Where-Object {{ $_.Name -match 'Terminal' }} | Select-Object -First 1 }}
if (-not $app) {{ throw 'Could not find a Start-menu AppID for Windows Terminal or PowerShell' }}
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($app.AppID).Show($toast)
"""
    try:
        p = run_powershell(ps)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    if p.returncode == 0:
        return True, "Windows toast via powershell.exe"
    err = (p.stderr or p.stdout or b"").decode("utf-8", "replace").strip()
    return False, err[-800:] or f"powershell.exe exit {p.returncode}"


def linux_notify(title: str, body: str) -> tuple[bool, str]:
    if not shutil.which("notify-send"):
        return False, "notify-send not found"
    try:
        p = subprocess.run(
            ["notify-send", title, body],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=8,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    if p.returncode == 0:
        return True, "notify-send"
    err = (p.stderr or p.stdout or b"").decode("utf-8", "replace").strip()
    return False, err[-800:] or f"notify-send exit {p.returncode}"


def send_desktop_notification(
    problem: str,
    status: str,
    timeout: int,
    chat_url: str | None,
    result_url: str | None,
) -> tuple[bool, str]:
    if status == "timeout":
        minutes = max(1, round(timeout / 60))
        title = f"Rainier {problem} - {minutes}m timeout"
        body = "GPT-5.4 High timed out. Candidate is ready for promotion review."
    elif status == "success":
        title = f"Rainier {problem} - Codex finished"
        body = 'Codex returned an answer. Open Chat and send "next" for review.'
    elif status == "test":
        title = f"Rainier {problem} - notification test"
        body = 'Toast is working. Click Open Chat; "next" is already copied.'
    else:
        title = f"Rainier {problem} - runner error"
        body = 'Codex runner returned an error. Inspect the result; do not promote yet.'

    if is_wsl() and shutil.which("powershell.exe"):
        ok, detail = windows_toast(title, body, chat_url, result_url)
        if ok:
            return ok, detail
        fallback_ok, fallback_detail = linux_notify(title, body)
        return (fallback_ok, fallback_detail) if fallback_ok else (False, f"{detail}; {fallback_detail}")

    ok, detail = linux_notify(title, body)
    if ok:
        return ok, detail
    if shutil.which("powershell.exe"):
        return windows_toast(title, body, chat_url, result_url)
    return False, detail


def annotate_result(result: dict, timeout: int) -> None:
    status = result.get("status")
    result["timeout_seconds"] = timeout
    if status == "timeout":
        result["local_verdict"] = "LOCAL_STUMPED_BY_TIMEOUT"
        result["recommended_action"] = "PROMOTE_TO_MAIN_FOR_RAINIER"
        result["promotion_ready"] = True
    elif status == "success":
        result["local_verdict"] = "SOLVER_ANSWER_RETURNED"
        result["recommended_action"] = "REVIEW_SOLVER_ANSWER"
        result["promotion_ready"] = False
    else:
        result["local_verdict"] = "SOLVER_ERROR"
        result["recommended_action"] = "INSPECT_RUNNER"
        result["promotion_ready"] = False


def solve_once(
    problem: str,
    branch: str,
    model: str,
    effort: str,
    timeout: int,
    force: bool,
    notifications: bool = True,
    chat_url: str | None = None,
) -> bool:
    fetch_branch(branch)
    ref = f"origin/{branch}"
    problem_path = resolve_problem_path(problem, branch)
    blob = git("rev-parse", f"{ref}:{problem_path}")
    commit = git("rev-parse", ref)
    state = load_state(problem)
    attempted = state.setdefault("attempted_blobs", {})
    if blob in attempted and not force:
        print(f"[codex-adversary] {problem}: {blob[:12]} already tested")
        return False

    raw = git("show", f"{ref}:{problem_path}")
    statement = statement_only(raw)
    prompt = PROMPT_HEAD + statement
    result = {
        "problem": problem,
        "branch": branch,
        "problem_path": problem_path,
        "source_commit_sha": commit,
        "problem_blob_sha": blob,
        "statement_sha256": hashlib.sha256(statement.encode()).hexdigest(),
        "requested_model": model,
        "requested_reasoning_effort": effort,
        "runs": 1,
        "started_at": now(),
    }

    print(f"[codex-adversary] {problem}: {blob[:12]} -> {model}/{effort} x1", flush=True)
    with tempfile.TemporaryDirectory(prefix=f"rainier-{problem}-") as td:
        wd = Path(td)
        (wd / "problem.md").write_text(statement, encoding="utf-8")
        final = wd / "final.txt"
        cmd = [
            "codex", "exec",
            "--ephemeral",
            "--skip-git-repo-check",
            "--json",
            "--output-last-message", str(final),
            "--model", model,
            "--config", f'model_reasoning_effort="{effort}"',
            "--sandbox", "read-only",
            "--cd", str(wd),
            prompt,
        ]
        try:
            p = run(cmd, cwd=wd, check=False, timeout=timeout)
            result["exit_code"] = p.returncode
            result["stderr"] = p.stderr.strip()[-4000:]
            result["final_answer"] = final.read_text(encoding="utf-8", errors="replace").strip() if final.exists() else ""
            result["status"] = "success" if p.returncode == 0 and result["final_answer"] else "error"
        except subprocess.TimeoutExpired:
            result.update(
                status="timeout",
                exit_code=None,
                stderr=f"timeout after {timeout}s; Codex process group terminated",
                final_answer="",
            )

    result["completed_at"] = now()
    annotate_result(result, timeout)
    attempted[blob] = {
        "at": result["completed_at"],
        "status": result["status"],
        "local_verdict": result["local_verdict"],
        "source_commit_sha": commit,
    }
    save_state(problem, state)

    result_dir = Path("solver-results") / problem
    rel = result_dir / f"{blob[:12]}.json"
    latest_rel = result_dir / "latest.json"
    result["result_file"] = str(rel).replace(os.sep, "/")

    latest = {
        "problem": problem,
        "branch": branch,
        "problem_path": problem_path,
        "problem_blob_sha": blob,
        "source_commit_sha": commit,
        "status": result["status"],
        "local_verdict": result["local_verdict"],
        "recommended_action": result["recommended_action"],
        "promotion_ready": result["promotion_ready"],
        "requested_model": model,
        "requested_reasoning_effort": effort,
        "runs": 1,
        "timeout_seconds": timeout,
        "completed_at": result["completed_at"],
        "result_file": result["result_file"],
    }

    for attempt in range(2):
        fetch_branch(branch)
        with tempfile.TemporaryDirectory(prefix="rainier-publish-") as td:
            wt = Path(td) / "wt"
            git("worktree", "add", "--detach", "-q", str(wt), f"origin/{branch}")
            try:
                target = wt / rel
                latest_target = wt / latest_rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                latest_target.write_text(json.dumps(latest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                git(
                    "add",
                    "--",
                    str(rel).replace(os.sep, "/"),
                    str(latest_rel).replace(os.sep, "/"),
                    cwd=wt,
                )
                diff = run(["git", "diff", "--cached", "--quiet"], cwd=wt, check=False)
                if diff.returncode == 0:
                    break
                git("commit", "-q", "-m", f"Record {model} {effort} solve for {problem} {blob[:12]}", cwd=wt)
                push = run(["git", "push", "-q", "origin", f"HEAD:refs/heads/{branch}"], cwd=wt, check=False)
                if push.returncode == 0:
                    break
                if attempt == 1:
                    raise RuntimeError((push.stderr or push.stdout).strip())
            finally:
                git("worktree", "remove", "--force", str(wt), check=False)

    if result["status"] == "timeout":
        print(
            f"[codex-adversary] {problem}: timeout after {timeout}s -> {rel}; "
            "LOCAL_STUMPED_BY_TIMEOUT; candidate ready for main/Rainier",
            flush=True,
        )
    else:
        print(
            f"[codex-adversary] {problem}: {result['status']} -> {rel}; "
            f"{result['local_verdict']}",
            flush=True,
        )

    if notifications:
        result_link = github_file_url(branch, rel)
        ok, detail = send_desktop_notification(problem, result["status"], timeout, chat_url, result_link)
        if ok:
            print(f"[codex-adversary] {problem}: desktop notification sent via {detail}", flush=True)
        else:
            print(f"[codex-adversary] {problem}: desktop notification unavailable: {detail}", file=sys.stderr, flush=True)
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("problem", help="e.g. problem81")
    ap.add_argument("--branch", help="default: adversary/<problem>")
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--interval", type=int, default=45)
    ap.add_argument("--model", default="gpt-5.4")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--force", action="store_true")
    ap.add_argument(
        "--chat-url",
        help="ChatGPT conversation URL for this problem; saved locally under .tmp/codex-adversary/",
    )
    ap.add_argument(
        "--notify-test",
        action="store_true",
        help="send a desktop test notification and exit without running Codex",
    )
    ap.add_argument("--no-notify", action="store_true", help="disable desktop notifications")
    args = ap.parse_args()
    args.branch = args.branch or f"adversary/{args.problem}"

    if not shutil.which("git"):
        print("error: git not found on PATH", file=sys.stderr)
        return 2

    if args.chat_url:
        try:
            save_chat_url(args.problem, args.chat_url)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        print(
            f"[codex-adversary] {args.problem}: saved local ChatGPT URL in "
            f"{CHAT_URLS_FILE.relative_to(ROOT)}",
            flush=True,
        )
    chat_url = chat_url_for(args.problem, args.chat_url)

    if args.notify_test:
        if args.no_notify:
            print("error: --notify-test cannot be combined with --no-notify", file=sys.stderr)
            return 2
        result_link = github_file_url(
            args.branch,
            Path("solver-results") / args.problem / "latest.json",
        )
        ok, detail = send_desktop_notification(args.problem, "test", args.timeout, chat_url, result_link)
        if ok:
            print(f"[codex-adversary] {args.problem}: test notification sent via {detail}")
            if chat_url:
                print(f"[codex-adversary] {args.problem}: click toast/Open Chat to open the configured conversation")
            else:
                print(
                    f"[codex-adversary] {args.problem}: no ChatGPT URL configured; "
                    "toast opens the GitHub result instead"
                )
            return 0
        print(f"error: desktop notification failed: {detail}", file=sys.stderr)
        return 2

    if not shutil.which("codex"):
        print("error: codex not found on PATH", file=sys.stderr)
        return 2

    if not args.watch:
        solve_once(
            args.problem,
            args.branch,
            args.model,
            args.effort,
            args.timeout,
            args.force,
            notifications=not args.no_notify,
            chat_url=chat_url,
        )
        return 0

    notify_state = "off" if args.no_notify else ("chat-linked" if chat_url else "result-only")
    print(
        f"[codex-adversary] watching origin/{args.branch}; one {args.model}/{args.effort} "
        f"run per new problem.md; timeout={args.timeout}s; notifications={notify_state}"
    )
    while True:
        try:
            solve_once(
                args.problem,
                args.branch,
                args.model,
                args.effort,
                args.timeout,
                args.force,
                notifications=not args.no_notify,
                chat_url=chat_url,
            )
            time.sleep(max(args.interval, 10))
        except KeyboardInterrupt:
            return 0
        except Exception as exc:
            print(f"[codex-adversary] {exc}", file=sys.stderr, flush=True)
            time.sleep(max(args.interval, 10))


if __name__ == "__main__":
    raise SystemExit(main())
