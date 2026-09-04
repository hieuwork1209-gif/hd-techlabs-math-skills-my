# Reusable Chat Web + Codex Adversary Loop

This runbook is the source of truth for the **optional local difficulty preflight** driven by `/rainier-next-check`.
It is deliberately separate from `/rainier-next`.

## Command split

```text
/rainier-next problemNN
    -> normal Rainier authoring / solving / normalization / reviewer repair
    -> works on the portal-submission version

/rainier-next-check problemNN
    -> local adversary branch + Codex GPT-5.4 High preflight
    -> hardens only on adversary/problemNN
    -> promotes to main only at the local stopping point
```

Do not retrofit the adversary loop into `/rainier-next`.

## Design goal

```text
main contains a current problem + solution
        |
        v
/rainier-next-check problemNN
        |
        +--> ensure adversary/problemNN exists
        |       create from current main only if absent
        |
        v
local watcher sees current adversary problem.md blob
        |
        v
Codex GPT-5.4 High solves exactly once, cold, <=20m
        |
        v
result + latest.json pushed to adversary/problemNN
        |
        +--> desktop notification on supported systems
        |       WSL2 -> native Windows toast
        |
        v
user sends: next
        |
        v
ChatGPT web reviews result
   +----+-------------------+
   |                        |
correct                wrong / timeout
   |                        |
   v                        v
harden structurally      promotion gates
on adversary                |
solution first               v
problem second            promote exact pair
   |                     to main
   v                        |
new blob -> watcher          v
                         Rainier portal
```

The Rainier portal remains the only official difficulty authority.

## 1. Naming and state

For `problem103`:

```text
main
adversary/problem103
workspace/rainier-problem/problem103-*/problem.md
workspace/rainier-problem/problem103-*/solution.md
solver-results/problem103/<problem-blob-prefix>.json
solver-results/problem103/latest.json
.tmp/codex-adversary/problem103.json
.tmp/codex-adversary/chat-urls.json
```

The `.tmp/` files are local-only and gitignored. In particular, ChatGPT conversation URLs are never written to `solver-results/` and never pushed to GitHub.

## 2. Starting a new local check

First make sure the problem exists on `main`, normally via `/rainier-next`.
Then invoke:

```text
/rainier-next-check problem103
```

The skill must:

1. resolve the exact problem on `main`;
2. verify a matching `problem.md` and `solution.md` exist;
3. check for `adversary/problem103`;
4. create that branch from current `main` only if it does not exist;
5. reuse an existing adversary branch without silently resetting it;
6. inspect whether the current adversary `problem.md` blob already has a matching local result.

If the current blob has no result, stop at `WAIT_CODEX`.

## 3. Local working-tree rule

**Do not checkout every adversary branch in the main watcher clone.** A normal Git working tree can only have one checked-out branch at a time.

Keep the main local clone on `main`:

```bash
git switch main
git pull --ff-only origin main
```

The watcher explicitly reads `origin/adversary/problemNN`; the currently checked-out branch is not used as the solver input.
When publishing a result it creates its own temporary detached Git worktree.

Therefore multiple problem watchers can run from the same local repo while that repo stays on `main`:

```bash
python scripts/codex-adversary-watch.py problem103 --watch
python scripts/codex-adversary-watch.py problem104 --watch
python scripts/codex-adversary-watch.py problem105 --watch
```

Use one terminal/tmux pane/process per problem. Do not run two watchers for the same problem.

If a watcher was already started while the clone happened to be checked out on `adversary/problemNN`, that measured run is still valid. Let it finish; switch the clone back to `main` afterward rather than restarting the same blob.

## 4. Local watcher defaults

```bash
python scripts/codex-adversary-watch.py problem103 --watch
```

Defaults:

```text
branch             adversary/problem103
model              gpt-5.4
reasoning effort   high
runs per blob      1
timeout             1200 seconds / 20 minutes
poll interval       45 seconds
desktop notify     enabled when a supported backend exists
```

Do not use `--force` in the normal protocol.

## 5. WSL2 desktop notifications

The watcher prefers native Windows notifications when it detects WSL and `powershell.exe`.
No PowerShell module is required.

For each completed attempt it:

1. pushes the result JSON to the adversary branch;
2. copies the literal text `next` to the Windows clipboard;
3. shows a Windows toast;
4. makes a configured ChatGPT conversation the default click target;
5. exposes `Open Chat` and `Open Result` actions when those URLs are available.

### Register a problem's ChatGPT conversation

Copy the exact URL of that problem's ChatGPT conversation from the browser, then run once:

```bash
python scripts/codex-adversary-watch.py problem103 \
  --chat-url 'https://chatgpt.com/c/...' \
  --notify-test
```

This does **not** run Codex. It saves the mapping locally in:

```text
.tmp/codex-adversary/chat-urls.json
```

and sends a test toast.

After that, normal watcher starts do not need `--chat-url` again:

```bash
python scripts/codex-adversary-watch.py problem103 --watch
```

The configured URL may also be supplied through `RAINIER_CHAT_PROBLEM103` or the generic `RAINIER_CHAT_URL` environment variable.

### Toast behavior

With a chat URL configured:

```text
click toast  -> open exact problem ChatGPT conversation
Open Chat    -> same exact conversation
Open Result  -> immutable solver result JSON on GitHub
clipboard    -> next
```

Without a chat URL, the toast still appears when possible and opens the GitHub result instead.

Use `--no-notify` to disable desktop notifications.

A watcher process already running before the notification-capable script was loaded will not hot-reload the new code; let that run finish normally and use notifications on subsequent runs.

## 6. Isolation contract

For each unseen `problem.md` blob, the watcher:

1. fetches `origin/adversary/problemNN`;
2. extracts only the normalized mathematical statement;
3. removes taxonomy/domain explanation from solver input;
4. creates a fresh temp directory outside the Rainier repo;
5. runs one ephemeral `gpt-5.4` solve at `high` effort, read-only;
6. instructs the solver not to use memory, prior conversations, GitHub, web, connected apps, or external files;
7. waits at most 20 minutes;
8. kills the Codex process group on timeout;
9. publishes the result to the same adversary branch;
10. emits a desktop notification when enabled and available.

## 7. Result files

Each completed attempt produces:

```text
solver-results/problem103/<blob-prefix>.json
solver-results/problem103/latest.json
```

The blob-specific file is the immutable run record.
`latest.json` is the compact handoff for ChatGPT web.

Important fields:

```text
problem_blob_sha
source_commit_sha
status
local_verdict
recommended_action
promotion_ready
requested_model
requested_reasoning_effort
runs
timeout_seconds
result_file
```

Never reuse a verdict whose `problem_blob_sha` does not equal the current adversary candidate blob.

## 8. User handoff

The web chat cannot wake itself when GitHub changes.
After a watcher attempt completes, the only user message needed is:

```text
next
```

The WSL2 toast copies this text to the clipboard for convenience.
A bare `next` in an active `/rainier-next-check` conversation means: read `latest.json`, follow `result_file` if needed, compare against the exact current solution, and continue the state machine.

## 9. Solver returned before timeout

Watcher metadata:

```text
status = success
local_verdict = SOLVER_ANSWER_RETURNED
recommended_action = REVIEW_SOLVER_ANSWER
promotion_ready = false
```

`status=success` means only that Codex returned text. It is **not** a mathematical verdict.

If the solver is mathematically correct, treat this as `LOCAL_NOT_STUMPED`, diagnose the earliest robust shortcut, and harden again on `adversary/problemNN`.
For every new candidate:

1. re-derive validity, uniqueness, and answer;
2. ensure the solution is self-contained and reasoning-dominant;
3. preserve submission gates;
4. update `solution.md` first;
5. update `problem.md` second;
6. do not change `main`;
7. let the watcher test the new blob once.

If the solver is wrong or materially incomplete, treat the exact candidate as locally stumped. Do not harden further. Run promotion gates and promote the pair to `main`.

## 10. Timeout

On timeout the watcher records:

```text
status = timeout
local_verdict = LOCAL_STUMPED_BY_TIMEOUT
recommended_action = PROMOTE_TO_MAIN_FOR_RAINIER
promotion_ready = true
timeout_seconds = 1200
```

A timeout is the local stopping rule, not an official Rainier pass.

## 11. Runner error

For infrastructure errors:

```text
local_verdict = SOLVER_ERROR
recommended_action = INSPECT_RUNNER
promotion_ready = false
```

Do not promote. Fix/inspect the harness first.

## 12. Promotion gates

Before copying anything to `main`, check the current `./scripts/adv submit problemNN` contract, including at least:

- Math Problem prompt: nonempty, <=2000 characters;
- Answer: nonempty, <=102 characters, no `\\boxed`;
- steps begin consecutively with `Step 1:`, `Step 2:`, ...;
- the final non-whitespace line of the last step is exactly `Final Answer: $\\boxed{...}$`, with no period/prose afterward;
- Solution Concepts: 1–5 entries, each under 100 characters;
- Domain, Sub-domain, Domain Explanation, Problem Type, Answer Type present and valid;
- Problem Type and Answer Type agree between `problem.md` and `solution.md`.

If only solution formatting is wrong, repair it on the adversary branch first. A solution-only edit does not trigger another solver attempt because the statement blob is unchanged.

## 13. Promotion to `main`

Promotion happens only at the local stopping point.

1. capture the exact selected adversary `solution.md` and `problem.md`;
2. update `main` `solution.md` first;
3. update `main` `problem.md` second;
4. re-fetch both from `main` and verify they match the selected candidate;
5. do not copy `solver-results/` to `main` unless separately requested;
6. report `MAIN_READY_FOR_RAINIER`.

The user can then run:

```bash
./scripts/adv submit problemNN
```

and the official Rainier portal checks.

## 14. Rainier feedback

- `RAINIER DIFFICULTY PASS` -> freeze the exact `main` statement.
- Difficulty FAIL/borderline -> keep the failed submitted version on `main`, continue design work on the existing adversary branch, and use the new Rainier trace/JSON as stronger evidence.
- Solution/format/taxonomy feedback -> repair the narrow issue while preserving the difficulty-producing structure whenever possible.
- Any statement edit invalidates all older portal difficulty percentages.

## 15. Compact state outputs

`/rainier-next-check` should end with one of:

```text
RAINIER CHECK: WAIT_CODEX
RAINIER CHECK: HARDENED_WAIT_CODEX
RAINIER CHECK: MAIN_READY_FOR_RAINIER
RAINIER CHECK: BLOCKED_RUNNER
```

Include only the problem number, adversary branch, candidate blob prefix, one-line status, and the next real user action.
