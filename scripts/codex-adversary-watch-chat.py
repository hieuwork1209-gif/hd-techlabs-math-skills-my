#!/usr/bin/env python3
"""Strict ChatGPT-linked wrapper for codex-adversary-watch.py.

The base watcher remains responsible for solving and publishing solver results.
This wrapper adds three guarantees:

1. Default solver settings are GPT-5.5 / medium / 2100 seconds.
2. Before every desktop notification, refresh
   solver-results/<problem>/chat-binding.json from origin/adversary/<problem>.
3. A clickable PowerShell toast targets only the bound ChatGPT conversation;
   GitHub result URLs are never used as a notification fallback.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "codex-adversary-watch.py"


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


def main() -> int:
    route = parse_route_args(sys.argv)
    inject_defaults(sys.argv)
    base = load_base()
    binding_path = f"solver-results/{route.problem}/chat-binding.json"
    explicit_chat = valid_chat_url(route.chat_url)

    def remote_chat_url() -> str | None:
        try:
            base.fetch_branch(route.branch)
            raw = base.git("show", f"origin/{route.branch}:{binding_path}", check=False)
        except Exception:
            return None
        return url_from_binding(raw)

    original_chat_url_for = base.chat_url_for

    def chat_url_for(problem: str, cli_url: str | None = None) -> str | None:
        # Explicit CLI binding is strongest. Otherwise prefer the GitHub relay
        # over stale local state so a running watcher can follow the web chat.
        explicit = valid_chat_url(cli_url) or explicit_chat
        if explicit:
            return explicit
        return remote_chat_url() or valid_chat_url(original_chat_url_for(problem, None))

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
            body = 'Toast is linked to this ChatGPT conversation; "next" is copied.'
        else:
            title = f"Rainier {problem} - runner error"
            body = "Codex runner errored. Open this chat to inspect it; do not promote yet."

        if base.is_wsl() and shutil.which("powershell.exe"):
            return base.windows_toast(title, body, target, None)
        ok, detail = base.linux_notify(title, body)
        if ok:
            return ok, detail
        if shutil.which("powershell.exe"):
            return base.windows_toast(title, body, target, None)
        return False, detail

    base.chat_url_for = chat_url_for
    base.send_desktop_notification = strict_notification
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
