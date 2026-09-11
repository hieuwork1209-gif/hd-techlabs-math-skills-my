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

## Quality-preserving authoring invariant

Before writing any **new** statement or any **statement-changing hardening**, run `quality-redesign-preflight.md` on the proposal itself. Do not edit the candidate until the proposed difficulty mechanism passes.

The workflow must distinguish **hardening by depth** from **hardening by concealment**:

- hardening by depth adds a natural mathematical dependency that creates new reasoning after the solver's common entry point;
- hardening by concealment makes the same standard structure, invariant, or substitution harder to recognize through extra notation, coordinates, relation layers, or tuned cancellation.

Only the first is allowed. If the proposal fails provenance/reviewer simulation, reject it before Codex and select a different blueprint. Run the same preflight again on the exact normalized pair before publishing `candidate-ready.json`.

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

## Repository submission-format bridge

The adversarial workflow uses `workspace/rainier-problem/...`, while the repository formatter was originally written around the frontier workspace. Do not skip it because of that path difference.

Before **every** `candidate-ready.json` and again immediately before **every** promotion:

1. Read and apply `skills/format-solution/SKILL.md` to the exact candidate `solution.md`, explicitly overriding its folder-resolution default with the current `workspace/rainier-problem/problemNN-*/solution.md` path.
2. Read and apply `skills/_shared/hard_gates.md` to the exact mapped portal fields.
3. Mirror the current field constants in `scripts/adv`. Current known values are `PROMPT_MAX=2000`, `ANSWER_MAX=102`, `CONCEPT_MAX=100`, `CONCEPT_LIMIT=5`; if the script changes, the script wins.
4. Run both Answer gates: raw mapped Answer length must be at most the current `ANSWER_MAX`, and after stripping `$` plus all whitespace it must be under 100 characters.
5. Reject solution-only aliases in the Answer field. The answer may use prompt-defined notation and bound dummy indices introduced locally inside the answer expression, but may not rely on `Z_0`, `A`, `C`, or similar aliases defined only inside the solution.
6. Check the exact boxed final answer against `## Answer`, prompt length, `## Steps` length, concept count/length, classification agreement, and required sections.

If a mathematically equivalent compact answer can be written using prompt-defined notation, that is a formatting repair. If the answer cannot fit honestly without changing `problem.md` or Answer Type, block the candidate **before Codex** when possible and redesign the statement/Answer Type. Do not spend a cold solve on a candidate that deterministic submission checks would reject.

A solution-only formatting edit with byte-identical `problem.md` does not require another cold solve. It does change the solution blob SHA, so re-run the final pair audit and refresh `candidate-ready.json`. Any `problem.md` edit invalidates prior solver evidence for difficulty and requires a fresh solve of the new statement blob.

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

For every statement-changing cycle, first complete the proposal-level `quality-redesign-preflight.md`. If it fails, do not edit the current candidate and do not expose anything to Codex.

After the proposal passes:

1. Treat the candidate as draft. Delete the old ready marker first when practical; a stale marker is also invalid because the watcher verifies both blob SHAs.
2. Complete mathematical derivation and repair `solution.md` **first**.
3. Write or update `problem.md` **second**.
4. Normalize the pair on the adversary branch.
5. Run the **Repository submission-format bridge** above. Apply any legal solution-only formatting repair before continuing.
6. Re-read the normalized/formatted `solution.md` and `problem.md`; confirm they describe the same exact problem and answer.
7. Run `references/pass-gates.md`. For new candidates and quality redesigns, also run `references/design-patterns.md` while selecting the design. Run `references/quality-redesign-preflight.md` again against the exact normalized pair; any unanswered reverse-engineering red flag or submission-format failure blocks readiness.
8. Resolve the final Git blob SHA of both files after all edits.
9. Upsert `candidate-ready.json` **last**, with those exact paths and SHAs.
10. Only now report a `*_WAIT_CODEX` status.

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
4. If the current candidate has no matching solver evidence, run the full pair audit **including the Repository submission-format bridge**, publish the matching ready marker only after it passes, and stop at `WAIT_CODEX`.
5. If official feedback requires a proof-only/format-only repair and `problem.md` remains byte-identical, repair `solution.md`, run the formatter/submission gates again, re-audit, and refresh the ready marker. Do not rerun Codex merely for exposition or Answer-field formatting changes to the same statement blob.
6. If official feedback changes the statement or requests quality redesign, invalidate old solver evidence for difficulty, finish the new pair, run all formatting/quality gates, refresh the marker, and cold-solve the new statement once.

Do not pre-harden an unmeasured candidate unless official trace/feedback already provides a concrete shortcut that must be repaired.

## New mode authoring stage

Use this when `main` has no `problemNN-*`.

### Blueprint selection

Silently create at least three blueprints. Each must specify:

1. honest Domain/Sub-domain fit;
2. natural object/question in one sentence;
3. hidden gateway the solver must discover;
4. the visible trigger that makes that gateway forward-discoverable;
5. 3-6 load-bearing reasoning nodes, including at least two after the gateway;
6. closure certificate for existence/uniqueness/exhaustiveness/correctness;
7. **compact final answer shape that can clear the repository Answer gates without solution-only aliases**;
8. likely solver shortcut and why it should fail;
9. provenance of every nonstandard coefficient/relation/helper object used to construct the statement.

Filter each blueprint with `references/pass-gates.md`, `references/design-patterns.md`, and proposal-level `references/quality-redesign-preflight.md` **before deriving/writing the candidate**. Reject blueprints whose difficulty is mainly tuned constants, cancellation stacks, hidden encodings of standard objects, giant calculations, long casework, excessive notation, obscure facts, theorem-recognition, concealment of the main gateway, or a final answer that cannot fit the submission field honestly. If fewer than two of the initial blueprints survive, silently generate replacements until there are at least two quality-safe choices, then select the stronger one.

### Ground truth before statement

For the selected blueprint:

1. Derive the complete ground truth privately enough to verify validity and gradeability.
2. Create/repair `solution.md` first.
3. Audit every load-bearing claim under the Reviewer Completeness Gate.
4. Create `problem.md` second with only the information needed for a self-contained problem.
5. Normalize and apply the repository `format-solution` rules on the adversary branch.
6. Map the exact portal fields and run `skills/_shared/hard_gates.md` plus current `scripts/adv` caps.
7. Re-read the exact pair and re-check correctness, taxonomy, answer type, naturalness, forward provenance, compression test, reviewer-quote simulation, Answer self-containedness, and all field lengths.
8. Publish `candidate-ready.json` last only if every quality and submission-format gate is green.
9. Stop at `RAINIER CHECK: WAIT_CODEX`.

Do not start Codex while blueprints, derivation, solution, statement, normalization, formatting, field validation, or reviewer audit are still in progress.

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
- run every correctness/quality/reviewer gate and the **Repository submission-format bridge**;
- if a solution-only formatting repair is needed, apply it, refresh the solution SHA/ready marker, and preserve the existing solver verdict because the problem blob is unchanged;
- if all gates pass, promote the exact pair to `main`.

If the solver is correct:

- record `COMMON ENTRY`, `COMMON REDUCTION`, `FIRST DECISIVE RECOGNITION`, `RECOVERY PATH`, and `EARLIEST ROBUST SHORTCUT`;
- propose the hardening in one sentence and run proposal-level `quality-redesign-preflight.md` **before editing**;
- require the proposal to add a genuinely load-bearing natural dependency after the common entry point, not merely make that entry point harder to recognize;
- if the proposal fails, retire/redesign the blueprint immediately rather than stacking machinery;
- only after a proposal passes, run the Naturalness/Problem-Quality Gate, invalidate the ready marker, and begin the authoring cycle.

For `mode=existing`, continue structural hardening only while the statement stays natural, forward-motivated, reviewer-clean, and passes the anti-reverse-engineering preflight. If the only available move is concealment hardening, redesign before producing another candidate.

For `mode=new`, allow at most **one same-blueprint structural revision**. If that revised clean blob is also solved correctly, retire the blueprint and regenerate a fresh blueprint. Regeneration is preferred to over-hardening.

After any statement revision: derive ground truth again, update `solution.md` first, `problem.md` second, normalize, run the repository formatter/submission gates, re-audit, and publish a new ready marker last. Then stop at `HARDENED_WAIT_CODEX` or `REGENERATED_WAIT_CODEX`.

### `status=timeout`

Accept local timeout evidence only when metadata confirms:

- `local_verdict=LOCAL_STUMPED_BY_TIMEOUT`;
- `recommended_action=PROMOTE_TO_MAIN_FOR_RAINIER`;
- `promotion_ready=true`;
- `requested_model=gpt-5.5`;
- `requested_reasoning_effort=medium`;
- `timeout_seconds=2100`, unless the user explicitly selected another timeout.

Then run all promotion gates, including the Repository submission-format bridge, on the exact ready pair. A timeout is local evidence, never an official Rainier pass.

### `SOLVER_ERROR`

Do not promote. Infrastructure failure is not stump evidence. Preserve the candidate and report `BLOCKED_RUNNER` with the one concrete recovery action.

## Official feedback

Official portal evidence outranks the local verdict.

- Difficulty PASS: freeze the exact statement unless another official gate requires repair.
- Difficulty FAIL/borderline: use the trace as stronger shortcut evidence; revise structurally subject to the quality gate.
- `contrived`, `over-engineered`, `synthetic`, `overly layered`, `awkward construction`, or cancellation-tuning criticism: classify `QUALITY_REDESIGN`; simplify/redesign rather than harden the same machinery.
- `unjustified`, `unsupported`, `not self-contained`: repair proof architecture; statement changes require fresh solver evidence, solution-only exposition changes do not.
- Domain/Sub-domain mismatch: fix the taxonomy or redesign the mathematical emphasis honestly.
- Submission field failure: repair through `format-solution`/compact equivalent notation when `problem.md` can remain byte-identical; if the prompt or Answer Type must change, treat it as a statement change and obtain fresh solver evidence.
- Any statement edit invalidates old portal percentages and prior local difficulty verdicts for the old blob.

## Promotion preflight

Run `references/pass-gates.md` on the exact ready pair. Run the **Repository submission-format bridge** again even if it passed before Codex. Ensure the exact portal-mapped fields satisfy the current `scripts/adv` limits and `skills/_shared/hard_gates.md` before touching `main`.

If a format-only `solution.md` edit is required, make it on `adversary/problemNN`, re-audit, refresh `candidate-ready.json` with the new solution SHA, and keep the existing solver evidence only because the problem blob is byte-identical. If `problem.md` must change, stop promotion and require a fresh cold solve.

Only after all gates are green: capture exact adversary contents, update `main` `solution.md` first and `problem.md` second, then re-fetch both from `main` and verify they match the selected candidate. Do not copy `candidate-ready.json`, solver result files, or `chat-binding.json` to `main`.

`RAINIER CHECK: MAIN_READY_FOR_RAINIER` is forbidden unless the exact promoted pair would pass the deterministic field checks mirrored by `./scripts/adv submit problemNN`.

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
