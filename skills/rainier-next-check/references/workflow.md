# Unified Rainier Next Check Workflow

## State model

For `problem123` use:

- submission branch: `main`
- design branch: `adversary/problem123`
- candidate pair: `workspace/rainier-problem/problem123-*/solution.md` then `problem.md`
- ready handshake: `solver-results/problem123/candidate-ready.json`
- immutable run record: `solver-results/problem123/<problem-blob-prefix>.json`
- latest handoff: `solver-results/problem123/latest.json`
- chat binding: `solver-results/problem123/chat-binding.json` on the adversary branch only

The ready handshake is the transaction boundary between ChatGPT authoring and the local watcher. **No matching marker, no Codex run.**

## First invocation and mode detection

Invocation form:

`/rainier-next-check problemNN https://chatgpt.com/c/<conversation-id>`

A legacy `/rainier-new-problem problemNN ...` request follows this same flow.

1. Validate the supplied ChatGPT conversation URL and extract `/c/<id>` when possible.
2. Inspect `main` for `workspace/rainier-problem/problemNN-*/problem.md`.
   - Exactly one match -> `mode=existing`.
   - No match -> `mode=new`.
   - More than one match -> stop and resolve the repository ambiguity; never guess.
3. Ensure `adversary/problemNN` exists.
   - If absent, create it from current `main`.
   - If present, reuse it exactly; never force-reset it.
4. Immediately upsert `solver-results/problemNN/chat-binding.json` on the adversary branch. Store `problem`, `chat_url`, and `conversation_id` when extractable. Never put this file on `main`.
5. Continue through the mode-specific authoring stage below.

## Runner bootstrap

Before exposing any candidate to Codex, inspect the repository `scripts/codex-adversary-watch-chat.py`. It must implement the bundled candidate-ready handshake and GPT-5.5/Medium/2100 defaults. If the repository copy is older, sync the bundled wrapper before publishing a ready marker or reporting `WAIT_CODEX`. A watcher process that was already running must be stopped and restarted after the script changes; editing the file cannot change code already loaded by that Python process.

## Candidate-ready handshake

The watcher must not infer readiness from the existence or modification of `problem.md`. It may solve only when `solver-results/problemNN/candidate-ready.json` exists on `origin/adversary/problemNN` and matches the exact current pair.

Use this payload shape:

```json
{
  "problem": "problem123",
  "mode": "new",
  "ready": true,
  "problem_path": "workspace/rainier-problem/problem123-stochastic-processes/problem.md",
  "problem_blob_sha": "<full git blob sha>",
  "solution_path": "workspace/rainier-problem/problem123-stochastic-processes/solution.md",
  "solution_blob_sha": "<full git blob sha>"
}
```

`mode` must be `new` or `existing`.

### Authoring transaction

For every statement-changing cycle:

1. Treat the candidate as draft. Delete the old ready marker first when practical; a stale marker is also invalid because the watcher verifies both blob SHAs.
2. Complete mathematical derivation and repair `solution.md` **first**.
3. Write or update `problem.md` **second**.
4. Run normalization/formatting/submission preparation on the adversary branch.
5. Re-read the normalized `solution.md` and `problem.md`; confirm they describe the same exact problem and answer.
6. Run `references/pass-gates.md`. For new candidates and quality redesigns, also run `references/design-patterns.md` while selecting the design.
7. Resolve the final Git blob SHA of both files after all edits.
8. Upsert `candidate-ready.json` **last**, with those exact paths and SHAs.
9. Only now report a `*_WAIT_CODEX` status.

Any later edit to either candidate file invalidates the marker, even if the mathematical answer did not change. Refresh the marker only after a new final audit.

### Watcher eligibility

Before every attempted solve, the wrapper must fetch `origin/adversary/problemNN` and verify all of:

- exactly one current `problemNN-*/problem.md` resolves;
- matching sibling `solution.md` exists;
- `candidate-ready.json` parses as JSON;
- `problem`, `ready`, and `mode` are valid;
- marker `problem_path` equals the resolved current path;
- marker `solution_path` equals the sibling solution path;
- marker problem SHA equals the current Git blob SHA;
- marker solution SHA equals the current Git blob SHA.

If any check fails, the watcher waits without invoking Codex. Intermediate commits, half-written pairs, normalization commits, folder renames, and regenerated drafts are therefore harmless.

The repository base watcher still enforces one solve per unseen problem blob. The wrapper additionally avoids repeatedly delegating the same ready pair within one watch process.

## Existing mode authoring stage

Use this when `main` already contains exactly one `problemNN-*` pair.

1. Read the exact pair from `adversary/problemNN` if present; otherwise the branch starts from `main`.
2. Read any relevant official Rainier feedback and `latest.json`.
3. If the current statement already has matching solver evidence, continue from that evidence; do not rerun it.
4. If the current candidate has no matching solver evidence, audit it and publish the matching ready marker. Stop at `WAIT_CODEX`.
5. If official feedback requires a proof-only/format-only repair and `problem.md` remains byte-identical, repair `solution.md`, re-audit, and refresh the ready marker. Do not rerun Codex merely for exposition changes to the same statement blob.
6. If official feedback changes the statement or requests quality redesign, invalidate old solver evidence for difficulty, finish the new pair, refresh the marker, and cold-solve the new statement once.

Do not pre-harden an unmeasured candidate unless official trace/feedback already provides a concrete shortcut that must be repaired.

## New mode authoring stage

Use this when `main` has no `problemNN-*`.

### Blueprint selection

Silently create at least three blueprints. Each must specify:

1. honest Domain/Sub-domain fit;
2. natural object/question in one sentence;
3. hidden gateway the solver must discover;
4. 3-6 load-bearing reasoning nodes after the gateway;
5. closure certificate for existence/uniqueness/exhaustiveness/correctness;
6. compact final answer shape;
7. likely solver shortcut and why it should fail.

Filter with `references/pass-gates.md` and `references/design-patterns.md`. Reject blueprints whose difficulty is mainly tuned constants, cancellation stacks, giant calculations, long casework, excessive notation, obscure facts, or theorem-recognition.

### Ground truth before statement

For the selected blueprint:

1. Derive the complete ground truth privately enough to verify validity and gradeability.
2. Create/repair `solution.md` first.
3. Audit every load-bearing claim under the Reviewer Completeness Gate.
4. Create `problem.md` second with only the information needed for a self-contained problem.
5. Normalize and apply portal formatting on the adversary branch.
6. Re-read the normalized exact pair and re-check correctness, taxonomy, answer type, and naturalness.
7. Publish `candidate-ready.json` last.
8. Stop at `RAINIER CHECK: WAIT_CODEX`.

Do not start Codex while blueprints, derivation, solution, statement, normalization, or reviewer audit are still in progress.

## Result state machine

### No result for the exact ready problem blob

Stop at `WAIT_CODEX`. The watcher may stay running; the matching ready marker is what makes the candidate eligible.

### Latest result does not match the current ready blob

Treat the current candidate as unmeasured. Never reuse the old verdict. Stop at `WAIT_CODEX`.

### `status=success`

1. Open `latest.json.result_file`.
2. Fetch the exact candidate `solution.md` named by the ready marker.
3. Confirm `requested_model=gpt-5.5` and `requested_reasoning_effort=medium`; otherwise report the custom run and do not silently treat it as default evidence.
4. Judge mathematical correctness, not CLI exit status or wording similarity.

If the solver is wrong or materially incomplete:

- label the exact candidate `LOCAL_STUMPED`;
- do not harden further;
- run every correctness/quality/reviewer/format gate;
- if all gates pass, promote the exact pair to `main`.

If the solver is correct:

- record `COMMON ENTRY`, `COMMON REDUCTION`, `FIRST DECISIVE RECOGNITION`, `RECOVERY PATH`, and `EARLIEST ROBUST SHORTCUT`;
- run the Naturalness/Problem-Quality Gate before editing;
- invalidate the ready marker before the new authoring cycle;
- add only a genuinely load-bearing mathematical dependency.

For `mode=existing`, continue structural hardening only while the statement stays natural and reviewer-clean. Redesign rather than stack machinery.

For `mode=new`, allow at most **one same-blueprint structural revision**. If that revised clean blob is also solved correctly, retire the blueprint and regenerate a fresh blueprint. Regeneration is preferred to over-hardening.

After any statement revision: derive ground truth again, update `solution.md` first, `problem.md` second, normalize, re-audit, and publish a new ready marker last. Then stop at `HARDENED_WAIT_CODEX` or `REGENERATED_WAIT_CODEX`.

### `status=timeout`

Accept local timeout evidence only when metadata confirms:

- `local_verdict=LOCAL_STUMPED_BY_TIMEOUT`;
- `recommended_action=PROMOTE_TO_MAIN_FOR_RAINIER`;
- `promotion_ready=true`;
- `requested_model=gpt-5.5`;
- `requested_reasoning_effort=medium`;
- `timeout_seconds=2100`, unless the user explicitly selected another timeout.

Then run all promotion gates on the exact ready pair. A timeout is local evidence, never an official Rainier pass.

### `SOLVER_ERROR`

Do not promote. Infrastructure failure is not stump evidence. Preserve the candidate and report `BLOCKED_RUNNER` with the one concrete recovery action.

## Official feedback

Official portal evidence outranks the local verdict.

- Difficulty PASS: freeze the exact statement unless another official gate requires repair.
- Difficulty FAIL/borderline: use the trace as stronger shortcut evidence; revise structurally subject to the quality gate.
- `contrived`, `over-engineered`, `synthetic`, `overly layered`, `awkward construction`, or cancellation-tuning criticism: classify `QUALITY_REDESIGN`; simplify/redesign rather than harden the same machinery.
- `unjustified`, `unsupported`, `not self-contained`: repair proof architecture; statement changes require fresh solver evidence, solution-only exposition changes do not.
- Domain/Sub-domain mismatch: fix the taxonomy or redesign the mathematical emphasis honestly.
- Any statement edit invalidates old portal percentages and prior local difficulty verdicts for the old blob.

## Promotion preflight

Run `references/pass-gates.md` on the exact ready pair. Also ensure the ready marker still matches both current blob SHAs immediately before promotion.

Capture exact adversary contents, update `main` `solution.md` first and `problem.md` second, then re-fetch both from `main` and verify they match the selected candidate. Do not copy `candidate-ready.json`, solver result files, or `chat-binding.json` to `main`.

## Chat binding and notification routing

Use GitHub only as a relay for the chat binding.

- Binding path: `solver-results/problemNN/chat-binding.json` on `adversary/problemNN` only.
- Prefer `{problem, conversation_id, chat_url}` when the URL contains `/c/<id>`.
- Never fabricate an ID.
- On later `next` turns, reuse the stored binding unless the user explicitly rebinds the problem.
- The wrapper refreshes the binding from the remote adversary branch at notification time.
- Toast click/Open Chat must target the bound ChatGPT conversation. Never fall back to a GitHub result URL.

## Compact statuses

Use one of:

- `RAINIER CHECK: WAIT_CODEX`
- `RAINIER CHECK: HARDENED_WAIT_CODEX`
- `RAINIER CHECK: REGENERATED_WAIT_CODEX`
- `RAINIER CHECK: MAIN_READY_FOR_RAINIER`
- `RAINIER CHECK: BLOCKED_RUNNER`

Include the problem number, mode, adversary branch, current problem blob prefix, Domain/Sub-domain, and only the next real user action.
