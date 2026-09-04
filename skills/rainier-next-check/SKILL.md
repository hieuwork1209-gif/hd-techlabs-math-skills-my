---
name: rainier-next-check
description: Run the Rainier local adversarial difficulty loop for an existing problem. Use for `/rainier-next-check problemNN`, for requests to create or continue `adversary/problemNN`, and for `next` follow-ups in a conversation already running this loop. Keep hardening off `main`, use one cold GPT-5.4 High solve per problem blob with a 20-minute timeout, review returned answers against the matching reference solution, harden again only when the solver is correct, and promote the exact problem/solution pair to `main` when the solver is wrong or times out.
user-invocable: true
disable-model-invocation: false
argument-hint: problemNN or folder path, optionally Rainier feedback/JSON/trace; bare `next` continues the active check loop
---

# Rainier Next Check — Adversary/Codex Preflight

## Contract

- **Do not replace or modify `/rainier-next`.** `/rainier-next` remains the normal Rainier authoring, normalization, reviewer-repair, and portal-package orchestrator.
- **Task:** run the separate local adversarial difficulty loop for an already-existing Rainier problem.
- **Branch discipline:** `main` is the portal-submission/frozen branch. All local difficulty hardening happens on `adversary/problemNN`.
- **First invocation:** resolve the exact `problemNN-*` on `main`, verify a matching `problem.md` + `solution.md` exist, then ensure `adversary/problemNN` exists. Create it from current `main` only if absent. Never silently reset an existing adversary branch.
- **Independent solver:** use the result format produced by `scripts/codex-adversary-watch.py`, which runs exactly one cold `gpt-5.4` / `high` solve per unseen `problem.md` blob with a default timeout of 1200 seconds.
- **One blob, one measured solve.** Do not use `--force` in the normal loop.
- **Success is not correctness.** `status=success` only means Codex returned text; compare the returned mathematics against the exact matching candidate solution.
- **Correct solver answer:** diagnose the actual earliest robust shortcut, harden structurally, verify the new ground truth, then update `solution.md` first and `problem.md` second on the adversary branch. Do not touch `main`.
- **Wrong/materially incomplete solver answer:** treat the candidate as locally stumped, stop hardening, run promotion gates, and promote the exact pair to `main`.
- **Timeout:** when `latest.json` records `LOCAL_STUMPED_BY_TIMEOUT` and `promotion_ready=true`, stop hardening, run promotion gates, and promote the exact pair to `main`.
- **Runner error:** never promote on `SOLVER_ERROR` or another infrastructure failure.
- A local stump/timeout is only preflight evidence. Only the official portal may be called `RAINIER DIFFICULTY PASS`.

## Authoritative references

Read these before acting:

- `docs/codex-adversary-loop.md`
- `docs/rainier-hardening-workflow.md`
- `skills/_shared/harden_loop.md`
- current portal/reviewer evidence for this exact problem, when supplied

A newer user-provided Rainier trace/JSON overrides older local evidence.

## State resolution

For `problem103`, use:

```text
main
adversary/problem103
workspace/rainier-problem/problem103-*/problem.md
workspace/rainier-problem/problem103-*/solution.md
solver-results/problem103/<blob-prefix>.json
solver-results/problem103/latest.json
```

Resolve exactly one matching problem folder. Never infer another problem number from ordering.

### First use / no result for the current blob

1. Resolve the current `main` problem and solution.
2. Ensure `adversary/problemNN` exists; create it from current `main` if absent.
3. Read the candidate pair from the adversary branch.
4. Check `solver-results/problemNN/latest.json` if present.
5. If there is no result whose `problem_blob_sha` equals the current adversary `problem.md` blob, do **not** reuse an older verdict and do not harden blindly unless current Rainier trace/feedback already exposes a concrete shortcut.
6. Stop at `WAIT_CODEX` and give the exact local command:

```bash
python scripts/codex-adversary-watch.py problemNN --watch
```

The first measured candidate may be identical to `main`.

### `next` follow-up

In a conversation already running this skill, interpret a bare `next` as:

1. read `solver-results/problemNN/latest.json` from `adversary/problemNN`;
2. verify its `problem_blob_sha` equals the current adversary candidate blob;
3. follow `result_file` when needed;
4. compare the solver result with the exact current candidate solution;
5. continue the state machine below without asking the user to restate the problem.

The web chat cannot wake itself when GitHub changes. `next` is the single user handoff between completed local rounds.

## Result state machine

### A — Current blob has no matching result

Return `RAINIER CHECK: WAIT_CODEX`. Do not mutate the statement.

### B — `status=success`

Fetch the full run record and current adversary solution.

If the solver is mathematically correct:

1. Extract the route actually used, including when possible:

```text
COMMON ENTRY:
COMMON REDUCTION:
COMMON SCALING/REPRESENTATION:
FIRST DECISIVE RECOGNITION:
RECOVERY PATH:
EARLIEST ROBUST SHORTCUT:
```

2. Harden the earliest robust shortcut structurally. Prefer hidden representation/invariant, coupled conditions, competing regimes, leading-order degeneracy, a standard route that fails for a mathematical reason, or a necessary certificate.
3. Do not manufacture difficulty with longer expansions, bigger matrices, larger case tables, ugly constants, brute force, or extra parameters without a new dependency.
4. Re-derive validity, uniqueness, and the intended answer.
5. Ensure the reference solution is self-contained and reasoning-dominant.
6. Preserve submission gates.
7. Write `solution.md` first.
8. Write `problem.md` second.
9. Verify the new `problem.md` blob changed and stop at `RAINIER CHECK: HARDENED_WAIT_CODEX`.

If the solver is wrong or materially incomplete:

1. Record the local judgment as `LOCAL_STUMPED`.
2. Do not harden again.
3. Run promotion preflight.
4. Promote the exact adversary pair to `main`.

### C — `status=timeout`

Require the run metadata to support the timeout verdict, normally:

```text
local_verdict = LOCAL_STUMPED_BY_TIMEOUT
recommended_action = PROMOTE_TO_MAIN_FOR_RAINIER
promotion_ready = true
timeout_seconds = 1200
```

Unless the user explicitly chose a different timeout for that run, 1200 seconds is the stopping rule. Then run promotion preflight and promote the exact pair to `main`.

### D — runner/infrastructure error

If the latest run is `SOLVER_ERROR`, malformed, missing its matching candidate, or otherwise infrastructure-failed, return `RAINIER CHECK: BLOCKED_RUNNER`. Do not promote and do not count it as stump evidence.

## Promotion preflight

Before writing to `main`, check the current repository submission contract, including at least:

- prompt nonempty and at most 2000 characters;
- standalone Answer nonempty, at most 102 characters, and containing no `\\boxed`;
- consecutive `Step 1:`, `Step 2:`, ... blocks;
- the final non-whitespace line of the last step is exactly a `Final Answer: $\\boxed{...}$` line, with no punctuation/prose afterward;
- Solution Concepts has 1–5 entries, each under 100 characters;
- Domain, Sub-domain, Domain Explanation, Problem Type, and Answer Type are present and portal-compatible;
- Problem Type and Answer Type agree between problem and solution.

If only solution formatting needs repair, fix it on the adversary branch first. A solution-only repair does not require another Codex solve because the measured statement blob is unchanged.

## Promote to `main`

1. Capture the exact selected adversary `solution.md` and `problem.md`.
2. Update `main` `solution.md` first.
3. Update `main` `problem.md` second.
4. Re-fetch both from `main` and verify they match the selected candidate.
5. Do not copy `solver-results/` to `main` unless explicitly requested.
6. Return `RAINIER CHECK: MAIN_READY_FOR_RAINIER` and tell the user to run `./scripts/adv submit problemNN` / the official portal checks.

## After official Rainier feedback

- Difficulty PASS: freeze the exact `main` statement.
- Difficulty FAIL/borderline: keep the failed submitted version on `main`, continue design work on the existing adversary branch, and use the new Rainier trace/JSON as stronger hardening evidence.
- Statement edits invalidate all previous portal difficulty percentages.

## Output

Use one compact state:

```text
RAINIER CHECK: <WAIT_CODEX | HARDENED_WAIT_CODEX | MAIN_READY_FOR_RAINIER | BLOCKED_RUNNER>
PROBLEM: problemNN
BRANCH: adversary/problemNN
CANDIDATE: <problem blob prefix>
STATUS: <one line>
YOUR ACTION: <only the next real user action>
```

Do not narrate every internal GitHub operation.