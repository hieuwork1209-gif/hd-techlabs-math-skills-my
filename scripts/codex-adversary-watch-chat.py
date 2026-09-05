#!/usr/bin/env python3
"""Strict ChatGPT-linked wrapper for codex-adversary-watch.py.

The base watcher remains responsible for solving and publishing solver results.
This wrapper adds five guarantees:

1. Default solver settings are GPT-5.5 / medium / 2100 seconds.
2. Before every desktop notification, refresh
   solver-results/<problem>/chat-binding.json from origin/adversary/<problem>.
3. On WSL2, a clickable PowerShell toast routes through the locally bound
   Chrome HWND for this problem; it never guesses another browser/account.
4. GitHub result URLs are never used as a notification fallback.
5. A matching solver-results/<problem>/terminal.json with state
   MAIN_READY_FOR_RAINIER stops the watcher cleanly instead of repeating
   "already tested" forever.
"""
from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "codex-adversary-watch.py"
TERMINAL_STATE = "MAIN_READY_FOR_RAINIER"


def load_base():
    if not BASE_PATH.exists():
        raise SystemExit(f"error: base watcher not found: {BASE_PATH}")
    spec = importlib.util.spec_from_file_location("rainier_codex_adversary_watch", BASE_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"error: could not load base watcher: {BASE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_route_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("problem")
    ap.add_argument("--branch")
    ap.add_argument("--chat-url")
    ns, _ = ap.parse_known_args(argv[1:])
    ns.branch = ns.branch or f"adversary/{ns.problem}"
    return ns


def has_option(argv: list[str], name: str) -> bool:
    return name in argv or any(arg.startswith(name + "=") for arg in argv)


def inject_defaults(argv: list[str]) -> None:
    if not has_option(argv, "--model"):
        argv.extend(["--model", "gpt-5.5"])
    if not has_option(argv, "--effort"):
        argv.extend(["--effort", "medium"])
    if not has_option(argv, "--timeout"):
        argv.extend(["--timeout", "2100"])


def valid_chat_url(value: str | None) -> str | None:
    if not value:
        return None
    try:
        parsed = urlparse(value.strip())
    except ValueError:
        return None
    if parsed.scheme != "https" or parsed.hostname not in {"chatgpt.com", "chat.openai.com"}:
        return None
    if "/c/" not in parsed.path:
        return None
    return value.strip()


def url_from_binding(raw: str) -> str | None:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    direct = valid_chat_url(str(data.get("chat_url") or ""))
    if direct:
        return direct
    conversation_id = str(data.get("conversation_id") or "").strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{8,200}", conversation_id):
        return f"https://chatgpt.com/c/{conversation_id}"
    return None


def protocol_url(problem: str, chat_url: str) -> str:
    payload = base64.urlsafe_b64encode(chat_url.encode("utf-8")).decode("ascii").rstrip("=")
    return f"rainier-chat://{problem}/{payload}"


def main() -> int:
    route = parse_route_args(sys.argv)
    inject_defaults(sys.argv)
    base = load_base()
    binding_path = f"solver-results/{route.problem}/chat-binding.json"
    terminal_path = f"solver-results/{route.problem}/terminal.json"
    window_binding_path = base.ROOT / ".tmp" / "codex-adversary" / f"{route.problem}-window.json"
    explicit_chat = valid_chat_url(route.chat_url)

    def remote_chat_url() -> str | None:
        try:
            base.fetch_branch(route.branch)
            raw = base.git("show", f"origin/{route.branch}:{binding_path}", check=False)
        except Exception:
            return None
        return url_from_binding(raw)

    def local_window_binding_ready() -> bool:
        try:
            data = json.loads(window_binding_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return False
        if not isinstance(data, dict):
            return False
        if str(data.get("problem") or "") != route.problem:
            return False
        if str(data.get("process_name") or "").lower() != "chrome":
            return False
        try:
            return int(data.get("hwnd") or 0) > 0 and int(data.get("pid") or 0) > 0
        except (TypeError, ValueError):
            return False

    def matching_terminal_state() -> dict | None:
        """Return the terminal marker only when it matches the current problem blob."""
        try:
            base.fetch_branch(route.branch)
            ref = f"origin/{route.branch}"
            problem_path = base.resolve_problem_path(route.problem, route.branch)
            current_blob = base.git("rev-parse", f"{ref}:{problem_path}")
            raw = base.git("show", f"{ref}:{terminal_path}", check=False)
            if not raw:
                return None
            data = json.loads(raw)
        except Exception:
            return None
        if not isinstance(data, dict):
            return None
        if str(data.get("problem") or "") != route.problem:
            return None
        if str(data.get("state") or "") != TERMINAL_STATE:
            return None
        if str(data.get("problem_blob_sha") or "") != current_blob:
            return None
        return data

    original_chat_url_for = base.chat_url_for
    original_solve_once = base.solve_once

    def chat_url_for(problem: str, cli_url: str | None = None) -> str | None:
        # Explicit CLI binding is strongest. Otherwise prefer the GitHub relay
        # over stale local state so a running watcher can follow the web chat.
        explicit = valid_chat_url(cli_url) or explicit_chat
        if explicit:
            return explicit
        return remote_chat_url() or valid_chat_url(original_chat_url_for(problem, None))

    def solve_once(*args, **kwargs):
        terminal = matching_terminal_state()
        if terminal:
            blob = str(terminal["problem_blob_sha"])
            print(
                f"[codex-adversary] {route.problem}: {blob[:12]} "
                f"{TERMINAL_STATE}; stopping watcher",
                flush=True,
            )
            # SystemExit is deliberately used instead of Exception so the base
            # watch loop's retry handler does not swallow the terminal signal.
            raise SystemExit(0)
        return original_solve_once(*args, **kwargs)

    def strict_notification(
        problem: str,
        status: str,
        timeout: int,
        chat_url: str | None,
        result_url: str | None,
    ) -> tuple[bool, str]:
        # Refresh at notification time. The result_url argument is deliberately
        # ignored: GitHub must never become the click target.
        target = explicit_chat or remote_chat_url() or valid_chat_url(chat_url)
        if not target:
            return False, (
                f"missing ChatGPT binding at {binding_path}; "
                "notification has no GitHub fallback"
            )

        if status == "timeout":
            minutes = max(1, round(timeout / 60))
            title = f"Rainier {problem} - {minutes}m timeout"
            body = "GPT-5.5 Medium timed out. Open this chat and send next for review."
        elif status == "success":
            title = f"Rainier {problem} - Codex finished"
            body = 'Codex returned an answer. Open this chat and send "next" for review.'
        elif status == "test":
            title = f"Rainier {problem} - notification test"
            body = 'Toast is linked to this problem\'s bound Chrome window; "next" is copied.'
        else:
            title = f"Rainier {problem} - runner error"
            body = "Codex runner errored. Open this chat to inspect it; do not promote yet."

        if base.is_wsl() and shutil.which("powershell.exe"):
            if not local_window_binding_ready():
                return False, (
                    f"missing local Chrome window binding at "
                    f"{window_binding_path.relative_to(base.ROOT)}; run "
                    f"python scripts/rainier-bind-window.py {route.problem}"
                )
            return base.windows_toast(title, body, protocol_url(problem, target), None)

        ok, detail = base.linux_notify(title, body)
        if ok:
            return ok, detail
        if shutil.which("powershell.exe"):
            # Outside WSL we cannot prove a Chrome HWND binding. Do not route a
            # click into an arbitrary signed-in browser window.
            return False, "PowerShell notification routing requires the WSL2 window binder"
        return False, detail

    base.chat_url_for = chat_url_for
    base.solve_once = solve_once
    base.send_desktop_notification = strict_notification
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
