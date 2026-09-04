#!/usr/bin/env python3
"""Blind-solve each new adversary problem.md once with Codex GPT-5.4 High.

The watcher never runs Codex inside the Rainier repo. It extracts only the
normalized statement into a temporary directory, runs one ephemeral Codex exec,
and writes the result back under solver-results/<problem>/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_ROOT = ROOT / ".tmp" / "codex-adversary"
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
    p = subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True, timeout=timeout)
    if check and p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or f"exit {p.returncode}").strip())
    return p


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


def solve_once(problem: str, branch: str, model: str, effort: str, timeout: int, force: bool) -> bool:
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
            result.update(status="timeout", exit_code=None, stderr=f"timeout after {timeout}s", final_answer="")

    result["completed_at"] = now()
    attempted[blob] = {"at": result["completed_at"], "status": result["status"], "source_commit_sha": commit}
    save_state(problem, state)

    rel = Path("solver-results") / problem / f"{blob[:12]}.json"
    for attempt in range(2):
        fetch_branch(branch)
        with tempfile.TemporaryDirectory(prefix="rainier-publish-") as td:
            wt = Path(td) / "wt"
            git("worktree", "add", "--detach", "-q", str(wt), f"origin/{branch}")
            try:
                target = wt / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                git("add", "--", str(rel).replace(os.sep, "/"), cwd=wt)
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
    print(f"[codex-adversary] {problem}: {result['status']} -> {rel}", flush=True)
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
    args = ap.parse_args()
    args.branch = args.branch or f"adversary/{args.problem}"

    if not shutil.which("git"):
        print("error: git not found on PATH", file=sys.stderr)
        return 2
    if not shutil.which("codex"):
        print("error: codex not found on PATH", file=sys.stderr)
        return 2

    if not args.watch:
        solve_once(args.problem, args.branch, args.model, args.effort, args.timeout, args.force)
        return 0

    print(f"[codex-adversary] watching origin/{args.branch}; one {args.model}/{args.effort} run per new problem.md")
    while True:
        try:
            solve_once(args.problem, args.branch, args.model, args.effort, args.timeout, args.force)
            time.sleep(max(args.interval, 10))
        except KeyboardInterrupt:
            return 0
        except Exception as exc:
            print(f"[codex-adversary] {exc}", file=sys.stderr, flush=True)
            time.sleep(max(args.interval, 10))


if __name__ == "__main__":
    raise SystemExit(main())
