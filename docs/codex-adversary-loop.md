# Reusable Chat Web + Codex Adversary Loop

This runbook describes the reusable local difficulty loop used for Rainier problems.
It is intended to work for any `problemNN` under `workspace/rainier-problem/`.

The design goal is:

```text
ChatGPT web hardens the problem
        -> pushes candidate to adversary/problemNN
local watcher sees the new problem.md blob
        -> Codex GPT-5.4 High solves exactly once, cold
        -> result + latest.json are pushed to the adversary branch
user sends `next` in the same ChatGPT web thread
        -> ChatGPT reads latest.json and decides what happens next
```

The official Rainier portal remains the final authority. Local Codex results are only preflight evidence.

## 1. Naming convention

For a problem such as `problem103`:

```text
main
adversary/problem103
workspace/rainier-problem/problem103-*/problem.md
workspace/rainier-problem/problem103-*/solution.md
solver-results/problem103/
```

The watcher resolves exactly one `problem103-*/problem.md` under `workspace/rainier-problem/`.
If zero or multiple matching files exist, it stops with an error rather than guessing.

## 2. One-time setup for a new problem

Start from the current `main`:

```bash
git switch main
git pull --ff-only origin main
git switch -c adversary/problem103
git push -u origin adversary/problem103
```

If the adversary branch already exists:

```bash
git fetch origin
git switch adversary/problem103
git pull --ff-only origin adversary/problem103
```

The generic watcher lives on `main` at:

```text
scripts/codex-adversary-watch.py
```

It accepts the problem number as an argument, so no code change is required per problem.

## 3. Start the local watcher

From the repository root:

```bash
python scripts/codex-adversary-watch.py problem103 --watch
```

Normal defaults are:

```text
branch             adversary/problem103
model              gpt-5.4
reasoning effort   high
runs per blob      1
timeout             1200 seconds / 20 minutes
poll interval       45 seconds
```

Expected startup output:

```text
[codex-adversary] watching origin/adversary/problem103; one gpt-5.4/high run per new problem.md; timeout=1200s
```

Keep this terminal running while ChatGPT web performs the hardening loop.

## 4. ChatGPT web hardening contract

The web hardener works only on `adversary/problemNN` until the candidate is ready for Rainier.

For each new candidate, ChatGPT must:

1. Inspect the current problem, solution, previous solver result, and reviewer/difficulty evidence.
2. Diagnose the earliest robust shortcut used by the solver.
3. Harden structurally, not by adding blind arithmetic or bookkeeping.
4. Re-derive and verify the new ground truth.
5. Update `solution.md` first.
6. Update `problem.md` second.
7. Do not change `main` during ordinary hardening iterations.

Updating `solution.md` first prevents a transient state where a new problem statement exists without its matching reference solution.

The watcher keys attempts by the Git blob SHA of `problem.md` only.
Changing `solution.md`, scripts, docs, or solver-result files does not trigger another solve.

## 5. What the watcher sends to Codex

For each previously unseen `problem.md` blob, the watcher:

1. Fetches `origin/adversary/problemNN`.
2. Extracts only the normalized mathematical statement.
3. Removes domain/taxonomy explanation from the cold-solve input.
4. Creates a clean temporary directory outside the Rainier repository.
5. Runs exactly one ephemeral Codex solve:

```text
model: gpt-5.4
reasoning effort: high
sandbox: read-only
```

6. Instructs the solver not to use memory, prior conversations, GitHub, web search, browsing, connected apps, or external files.
7. Waits at most 20 minutes.
8. Publishes the result back to the adversary branch.

Do not use `--force` in the normal workflow. One candidate blob gets one measured solve.

## 6. Result files

Each attempt produces:

```text
solver-results/problem103/<problem-blob-prefix>.json
solver-results/problem103/latest.json
```

The blob-specific JSON is the immutable run record.
`latest.json` is the compact handoff file for the next ChatGPT web turn.

Important fields include:

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

## 7. Verdict semantics

### A. Solver returned an answer before 20 minutes

The watcher records:

```text
status = success
local_verdict = SOLVER_ANSWER_RETURNED
recommended_action = REVIEW_SOLVER_ANSWER
promotion_ready = false
```

`status=success` means only that Codex completed and returned text.
It does NOT mean the mathematical answer is correct.

The user sends:

```text
next
```

ChatGPT web then reads `latest.json` and the full result file, compares the solver answer against the reference solution, and decides:

```text
solver answer correct
    -> diagnose the shortcut
    -> harden again on adversary/problemNN
    -> push solution.md, then problem.md
    -> watcher automatically tests the new blob

solver answer wrong / materially incomplete
    -> local stump
    -> stop hardening
    -> promote the exact candidate to main for Rainier testing
```

### B. Solver exceeds 20 minutes

The watcher terminates the Codex process group and records:

```text
status = timeout
local_verdict = LOCAL_STUMPED_BY_TIMEOUT
recommended_action = PROMOTE_TO_MAIN_FOR_RAINIER
promotion_ready = true
```

Expected terminal output:

```text
[codex-adversary] problem103: timeout after 1200s -> ...; LOCAL_STUMPED_BY_TIMEOUT; candidate ready for main/Rainier
```

The user sends:

```text
next
```

ChatGPT web reads `latest.json`, sees `promotion_ready=true`, stops local hardening, and promotes the exact matching `problem.md` and `solution.md` from `adversary/problem103` to `main`.

A local timeout is not an official Rainier difficulty pass. It is only the local stopping rule for this workflow.

### C. Runner error

The watcher records:

```text
local_verdict = SOLVER_ERROR
recommended_action = INSPECT_RUNNER
promotion_ready = false
```

Do not promote on an infrastructure error. Fix or inspect the runner first.

## 8. The only user message needed between local rounds

After the watcher prints `success`, `timeout`, or another completed verdict, the user only needs to send:

```text
next
```

ChatGPT web owns the rest of the decision logic.

The web chat cannot currently wake itself solely because GitHub changed, so this one user message is the handoff trigger.

## 9. Promotion to main

Promotion happens only when the local loop decides to stop and the user wants to test the candidate on Rainier.

Promote the exact candidate pair:

```text
adversary/problemNN: problem.md  -> main: problem.md
adversary/problemNN: solution.md -> main: solution.md
```

The problem and solution must correspond to the same hardened candidate.
Never promote only one of them.

Before telling the user to submit, verify on `main` that the resulting blob/content SHAs match the chosen candidate.

Do not copy `solver-results/` into `main` unless there is a separate reason to archive local evidence there.

## 10. Rainier decision loop

After promotion, the user runs the official Rainier checks.

```text
RAINIER DIFFICULTY PASS
    -> freeze that exact main version
    -> do not harden further

RAINIER DIFFICULTY FAIL
    -> bring the new Rainier trace/JSON/feedback back to ChatGPT
    -> continue hardening on adversary/problemNN
    -> old success percentages are stale as soon as problem.md changes

SOLUTION / FORMAT / TAXONOMY FAIL
    -> repair the narrow issue
    -> preserve the difficulty-producing structure whenever possible
```

The portal result for the exact unchanged statement is the only thing that may be called `RAINIER DIFFICULTY PASS`.

## 11. Full reusable state machine

```text
START problemNN
    |
    v
create/use adversary/problemNN
    |
    v
ChatGPT hardens + verifies solution
    |
    +--> push solution.md
    +--> push problem.md
              |
              v
watcher detects new problem.md blob
              |
              v
Codex GPT-5.4 High x1, cold, <= 20m
              |
        +-----+---------------------+
        |                           |
        v                           v
answer returned                 timeout
        |                           |
        v                           v
user: next                  latest.json says
        |                    promotion_ready=true
        v                           |
ChatGPT checks correctness           v
        |                       user: next
   +----+----+                      |
   |         |                      v
 correct    wrong              promote candidate
   |         |                   to main
   v         v                      |
harden     promote                  v
again      to main              Rainier test
   |         |                      |
   +---------+----------------------+
                                |
                        +-------+-------+
                        |               |
                      PASS             FAIL
                        |               |
                      FREEZE       adversary loop
```

## 12. Example: reuse for another problem

For `problem112`:

```bash
git switch main
git pull --ff-only origin main
git switch -c adversary/problem112
git push -u origin adversary/problem112
python scripts/codex-adversary-watch.py problem112 --watch
```

Then in ChatGPT web:

```text
/rainier-next problem112
```

After each completed local attempt:

```text
next
```

After Rainier returns official feedback, paste that feedback into the same problem conversation and continue from the exact submitted version.

## 13. Operational rules

- Exactly one GPT-5.4 High run per new `problem.md` blob.
- Default local timeout is 20 minutes.
- Do not repeatedly retry the same blob because the first result was inconvenient.
- Do not call a CLI `success` a solver success until the mathematical answer is reviewed.
- Do not call a local timeout an official Rainier pass.
- Keep hardening work on `adversary/problemNN`.
- Update `solution.md` before `problem.md` for each candidate.
- Promote both files together to `main` only at the local stopping point.
- Any statement change invalidates all older Rainier difficulty percentages for that problem.
- `main` is the version intended for portal submission; `adversary/problemNN` is the active design/test branch.
