# Rainier Authoring, Submission, and Local Check Workflow

This is the human-facing source of truth for moving a Rainier problem from repository draft to official portal submission.

The workflow now has **two separate commands with different responsibilities**:

```text
/rainier-next problemNN
/rainier-next-check problemNN
```

Do not merge their contracts.

## 1. Command responsibilities

### `/rainier-next`

Use `/rainier-next` for the normal Rainier authoring/reviewer pipeline:

- create/resolve the problem;
- solve or repair a stale solution;
- normalize problem/solution;
- repair reviewer feedback;
- validate taxonomy, answer type, formatting, and portal fields;
- produce a clean portal-ready version.

`/rainier-next` may work on the portal-submission version and keeps its existing behavior. The local Codex adversary branch is **not** part of this command.

### `/rainier-next-check`

Use `/rainier-next-check` for the separate local adversarial difficulty preflight:

- ensure `adversary/problemNN` exists;
- keep all difficulty hardening on that branch;
- use one cold GPT-5.4 High solve per `problem.md` blob;
- stop each solve after 20 minutes by default;
- review returned answers mathematically;
- harden again only when the solver is correct;
- promote the exact candidate pair to `main` when the solver is wrong or times out;
- never promote on a runner/infrastructure error.

Detailed state machine: `docs/codex-adversary-loop.md`.

## 2. Recommended end-to-end sequence

For an existing problem:

```text
/rainier-next problem89
        |
        v
problem + solution clean on main
        |
        v
/rainier-next-check problem89
        |
        +--> create/reuse adversary/problem89
        |
        v
local watcher: GPT-5.4 High x1 per candidate, <=20m
        |
        v
user: next
        |
   +----+----------------+
   |                     |
solver correct       wrong / timeout
   |                     |
   v                     v
harden adversary       promote exact pair
and test again           to main
   |                     |
   +---------------------+
                         v
                 ./scripts/adv submit problem89
                         |
                         v
                    Rainier portal
```

If the user does not want the local check, `/rainier-next` may still prepare a problem directly for portal testing. `/rainier-next-check` is an additional adversarial preflight, not a replacement.

## 3. User boundaries

The assistant owns all safe repository-side work that can be executed with available tools.
The user owns:

- running the local watcher process on their machine;
- sending `next` after a watcher attempt completes;
- running `./scripts/adv submit problemNN` when `main` is ready;
- running the official Rainier portal checks;
- bringing back portal feedback, score summaries, JSON, or full traces when needed.

The web chat cannot wake itself solely because GitHub changed. During `/rainier-next-check`, `next` is the one-message handoff.

## 4. Current portal calibration

Observed Rainier evidence from 2026-08-23/24 used:

- `@openai/gpt-5.4`;
- `@bedrock/anthropic.claude-opus-4-8`;
- 8 attempts per model;
- difficulty accepted when at least one model had success rate `<=75%`.

Portal behavior may change. A newer user-provided export overrides this calibration.

Do not aim exactly at the threshold when redesigning. Prefer conceptual failures with a meaningful buffer rather than arithmetic noise.

## 5. Evidence priority

For Rainier difficulty/reviewer analysis, prefer:

1. full trace HTML;
2. full attempt-level JSON;
3. raw model attempts;
4. score summary only.

Different answer strings do not imply different mathematical outcomes when Rainier marks them equivalent.
`No Response` is not reliable stump evidence unless the portal explicitly scores it that way.

Never fabricate repeated independent attempts from one ChatGPT-web reasoning run.

## 6. Core status model

Do not use one generic `PASS`.

```text
VALIDITY PASS
CORRECTNESS PASS
SOLUTION QUALITY PASS
SUBMISSION GATES PASS
LOCAL_STUMPED / LOCAL_NOT_STUMPED / UNMEASURED
RAINIER DIFFICULTY PASS / FAIL / BORDERLINE / UNTESTED
RAINIER ACCEPTED
```

Local Codex evidence is preflight only. No local status may be called `RAINIER DIFFICULTY PASS`.

## 7. Submission-gate preflight

Before declaring `PORTAL READY`, `MAIN_READY_FOR_RAINIER`, or `SUBMISSION GATES PASS`, validate the fields mapped by `./scripts/adv submit problemNN`.

Required checks include:

- Math Problem prompt is nonempty and at most `2000` characters.
- Answer is nonempty and at most `102` characters.
- Standalone Answer contains no `\\boxed`.
- `## Steps` splits into consecutive `Step 1:`, `Step 2:`, ... blocks.
- The final non-whitespace line of the final step is exactly a `Final Answer: $\\boxed{...}$` line.
- There is no period, prose, display equation, or other content after that final-answer line.
- Solution Concepts contains `1` to `5` entries.
- Each concept is under `100` characters.
- Domain, Sub-domain, Domain Explanation, Problem Type, and Answer Type are present and portal-compatible.
- Problem Type and Answer Type agree between `problem.md` and `solution.md`.
- LaTeX remains portal-safe after normalization.

Mathematical correctness alone is not enough. A format failure is a `SUBMISSION GATES FAIL` and must be repaired before portal handoff.

## 8. `/rainier-next` normal loop

`/rainier-next` remains the normal authoring/repair orchestrator.

Typical transitions:

```text
problem missing
  -> math-clone
  -> math-solve
  -> normalize-all
  -> PORTAL READY

solution missing/stale
  -> math-solve
  -> normalize-all
  -> PORTAL READY

solution-quality feedback
  -> repair with math-solve / format-solution / normalize-all
  -> PORTAL READY

Rainier difficulty FAIL + strong trace/JSON
  -> evaluate-responses when needed
  -> math-harder
  -> math-solve
  -> normalize-all
  -> PORTAL READY
```

This command should not silently create or manage `adversary/problemNN`. Use `/rainier-next-check` when the user asks for the local adversary/Codex loop.

## 9. `/rainier-next-check` local loop

`/rainier-next-check` assumes the problem already exists and has a current problem/solution pair on `main`.

Branch roles:

```text
main                 = portal submission / frozen accepted version
adversary/problemNN  = active local difficulty design branch
```

First invocation:

1. resolve exact `problemNN-*` on `main`;
2. ensure `adversary/problemNN` exists;
3. create it from current `main` only if absent;
4. never reset an existing adversary branch silently;
5. inspect current candidate/result state;
6. if the current blob is untested, stop at `WAIT_CODEX`.

Local watcher command:

```bash
python scripts/codex-adversary-watch.py problemNN --watch
```

Watcher defaults:

```text
gpt-5.4 / high
1 run per problem.md blob
1200s timeout
45s poll interval
```

After a completed attempt, the user sends:

```text
next
```

Then ChatGPT reads `solver-results/problemNN/latest.json` and the full result when needed.

Decision:

```text
solver mathematically correct
  -> LOCAL_NOT_STUMPED
  -> diagnose actual shortcut
  -> harden structurally on adversary
  -> solution.md first
  -> problem.md second
  -> watcher tests new blob once

solver wrong/materially incomplete
  -> LOCAL_STUMPED
  -> submission gates
  -> promote exact pair to main

20-minute timeout
  -> LOCAL_STUMPED_BY_TIMEOUT
  -> submission gates
  -> promote exact pair to main

runner/infrastructure error
  -> BLOCKED_RUNNER
  -> no promotion
```

## 10. Structural hardening policy

When difficulty evidence shows a solver shortcut, identify:

```text
COMMON ENTRY:
COMMON REDUCTION:
COMMON SCALING/REPRESENTATION:
FIRST DECISIVE RECOGNITION:
RECOVERY PATH:
EARLIEST ROBUST SHORTCUT:
```

Harden the earliest robust shortcut.

Prefer:

- hidden representation or invariant discovery;
- coupled implicit conditions;
- competing regimes whose dominance must be derived;
- leading-order degeneracy forcing a structural next step;
- a tempting standard route that fails mathematically;
- a necessary lemma/certificate before a short finish;
- answer-sensitive asymmetric/secondary contributions.

Do not count these as meaningful hardening by themselves:

- more Taylor orders;
- bigger determinants or matrices only for arithmetic volume;
- longer coefficient/case/partition tables;
- longer recurrences or brute-force searches;
- extra parameters without a new dependency;
- uglier constants or longer symbolic simplification.

## 11. Promotion discipline

During `/rainier-next-check`, ordinary hardening must not modify `main`.

At the local stopping point:

1. repair any submission-format issues on the adversary branch;
2. capture the exact candidate pair;
3. update `main` `solution.md` first;
4. update `main` `problem.md` second;
5. re-fetch and verify both match the selected adversary candidate;
6. then report `MAIN_READY_FOR_RAINIER`.

Do not copy `solver-results/` to `main` unless explicitly requested.

## 12. Rainier portal loop

After the exact `main` version is tested:

### Difficulty PASS

Freeze the exact statement. Do not harden it further.

### Difficulty FAIL or borderline

Use the strongest available portal trace/JSON as new evidence.
When using `/rainier-next-check`, continue design work on the existing adversary branch while leaving the failed submitted version on `main` for version traceability.

### Solution / format / taxonomy FAIL

Repair the narrowest issue. Preserve the difficulty-producing statement structure whenever possible.

Any statement change invalidates all older difficulty percentages.

## 13. Version discipline

Never transfer percentages between changed statements.

```text
v1 portal: GPT 8/8, Claude 8/8 -> TOO EASY
v2: statement hardened
v1 scores are now stale
v2 portal: fresh official measurement required
```

Solution-only formatting changes do not change the tested statement blob, but the final package must still pass all submission gates.

## 14. Parallel problems

The `/rainier-next-check` workflow may run for several problem numbers in parallel because each problem uses separate branches and result/state paths.

Use one watcher per problem. Do not run two watchers for the same problem.

## 15. Usage

Normal preparation:

```text
/rainier-next problem98
```

Then optional local adversarial preflight:

```text
/rainier-next-check problem98
```

After each completed local attempt:

```text
next
```

When `main` is promoted and gate-clean:

```bash
./scripts/adv submit problem98
```

With new official feedback, provide the problem number and the strongest available Rainier evidence to the appropriate command. If context already uniquely identifies the active problem, the number may be omitted only when there is no ambiguity.