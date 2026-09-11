#!/usr/bin/env python3
"""Gate Rainier cold solves on an exact finalized candidate pair.

This launcher leaves codex-adversary-watch-chat.py unchanged. It polls the
adversary branch and invokes that existing runner only when
solver-results/<problem>/candidate-ready.json matches the exact current
problem.md and sibling solution.md Git blobs.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
CHAT_RUNNER = ROOT / "scripts" / "codex-adversary-watch-chat.py"
PROBLEM_ROOT = "workspace/rainier-problem"
TERMINAL_STATE = "MAIN_READY_FOR_RAINIER"


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(
        cmd,
        cwd=str(ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or f"exit {p.returncode}").strip())
    return p


def git(*args: str, check: bool = True) -> str:
    return run(["git", *args], check=check).stdout.strip()


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


def show_json(ref: str, path: str) -> dict | None:
    raw = git("show", f"{ref}:{path}", check=False)
    if not raw:
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def terminal_matches(problem: str, branch: str, problem_blob: str) -> bool:
    ref = f"origin/{branch}"
    path = f"solver-results/{problem}/terminal.json"
    data = show_json(ref, path)
    return bool(
        data
        and data.get("problem") == problem
        and data.get("state") == TERMINAL_STATE
        and data.get("problem_blob_sha") == problem_blob
    )


def ready_state(problem: str, branch: str) -> tuple[bool, str, str | None]:
    fetch_branch(branch)
    ref = f"origin/{branch}"
    try:
        problem_path = resolve_problem_path(problem, branch)
    except Exception as exc:
        return False, f"candidate incomplete: {exc}", None

    solution_path = str(PurePosixPath(problem_path).with_name("solution.md"))
    problem_blob = git("rev-parse", f"{ref}:{problem_path}", check=False)
    solution_blob = git("rev-parse", f"{ref}:{solution_path}", check=False)
    if not problem_blob:
        return False, f"candidate incomplete: missing {problem_path}", None
    if not solution_blob:
        return False, f"candidate incomplete: missing {solution_path}", problem_blob

    if terminal_matches(problem, branch, problem_blob):
        return False, TERMINAL_STATE, problem_blob

    marker_path = f"solver-results/{problem}/candidate-ready.json"
    marker = show_json(ref, marker_path)
    if marker is None:
        return False, f"waiting for {marker_path}", problem_blob

    mode = marker.get("mode")
    checks = (
        (marker.get("problem") == problem, "problem id mismatch"),
        (marker.get("ready") is True, "ready flag is not true"),
        (mode in {"new", "existing"}, "mode must be new or existing"),
        (marker.get("problem_path") == problem_path, "problem path mismatch"),
        (marker.get("solution_path") == solution_path, "solution path mismatch"),
        (marker.get("problem_blob_sha") == problem_blob, "problem blob mismatch"),
        (marker.get("solution_blob_sha") == solution_blob, "solution blob mismatch"),
    )
    failures = [reason for ok, reason in checks if not ok]
    if failures:
        return False, "stale candidate-ready marker: " + "; ".join(failures), problem_blob

    result_path = f"solver-results/{problem}/{problem_blob[:12]}.json"
    if git("show", f"{ref}:{result_path}", check=False):
        return False, f"{problem_blob[:12]} already has published solver result", problem_blob

    return (
        True,
        f"candidate-ready gate passed mode={mode} problem={problem_blob[:12]} solution={solution_blob[:12]}",
        problem_blob,
    )


def invoke_runner(problem: str, branch: str, args: argparse.Namespace) -> int:
    cmd = [sys.executable, str(CHAT_RUNNER), problem, "--branch", branch]
    if args.chat_url:
        cmd.extend(["--chat-url", args.chat_url])
    if args.no_notify:
        cmd.append("--no-notify")
    if args.model:
        cmd.extend(["--model", args.model])
    if args.effort:
        cmd.extend(["--effort", args.effort])
    if args.timeout is not None:
        cmd.extend(["--timeout", str(args.timeout)])
    p = subprocess.run(cmd, cwd=str(ROOT), check=False)
    return p.returncode


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("problem", help="e.g. problem123")
    ap.add_argument("--branch", help="default: adversary/<problem>")
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--interval", type=int, default=45)
    ap.add_argument("--chat-url")
    ap.add_argument("--no-notify", action="store_true")
    ap.add_argument("--model")
    ap.add_argument("--effort")
    ap.add_argument("--timeout", type=int)
    args = ap.parse_args()
    branch = args.branch or f"adversary/{args.problem}"

    if not CHAT_RUNNER.exists():
        print(f"error: missing existing runner: {CHAT_RUNNER}", file=sys.stderr)
        return 2

    last_detail: str | None = None
    while True:
        try:
            eligible, detail, blob = ready_state(args.problem, branch)
            if detail != last_detail:
                suffix = "" if eligible else "; not solving"
                print(f"[codex-adversary] {args.problem}: {detail}{suffix}", flush=True)
                last_detail = detail

            if detail == TERMINAL_STATE:
                return 0

            if eligible:
                rc = invoke_runner(args.problem, branch, args)
                if rc != 0:
                    return rc

            if not args.watch:
                return 0
            time.sleep(max(args.interval, 10))
        except KeyboardInterrupt:
            return 0
        except Exception as exc:
            print(f"[codex-adversary] {args.problem}: gate error: {exc}", file=sys.stderr, flush=True)
            if not args.watch:
                return 2
            time.sleep(max(args.interval, 10))


if __name__ == "__main__":
    raise SystemExit(main())
