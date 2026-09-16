# Unified Rainier Next Check Workflow

## State model

For `problem123` use:

- submission branch: `main`;
- design branch: `adversary/problem123`;
- candidate pair: `workspace/rainier-problem/problem123-*/solution.md` then `problem.md`;
- ready handshake: `solver-results/problem123/candidate-ready.json`;
- immutable local run: `solver-results/problem123/<problem-blob-prefix>.json`;
- latest local handoff: `solver-results/problem123/latest.json`;
- author-chat binding: `solver-results/problem123/chat-binding.json` on the adversary branch only.

The ready marker is the transaction boundary. No exact marker, no solver run.

## Quality-preserving authoring invariant

Before writing a new statement or statement-changing hardening, run `quality-redesign-preflight.md` on the proposal itself.

Distinguish:

- **hardening by depth** — add a natural mathematical dependency that creates new reasoning after the common entry point;
- **hardening by concealment** — make the same successful representation/invariant/substitution harder to recognize through notation, coordinates, dimensions, cases, or tuned cancellation.

Only depth is allowed. Rerun the preflight on the exact normalized pair before readiness.

## First invocation and mode detection

Invocation:

`/rainier-next-check problemNN https://chatgpt.com/c/<conversation-id>`

Legacy `/rainier-new-problem problemNN ...` follows the same state machine.

1. Validate the supplied conversation URL and extract its conversation id when possible.
2. Inspect `main` for `workspace/rainier-problem/problemNN-*/problem.md`.
   - Exactly one -> `mode=existing`.
   - None -> `mode=new`.
   - More than one -> stop and resolve; never guess.
3. Ensure `adversary/problemNN` exists; create it from current `main` only when absent.
4. Upsert `solver-results/problemNN/chat-binding.json` on the adversary branch only.
5. Continue with the mode-specific authoring stage.

## Runner bootstrap

Before exposing a local candidate, inspect the repository watcher. It must implement the exact candidate-ready handshake and GPT-5.5 / Medium / 2100-second defaults.

If the repository runner is older than the bundled/expected protocol, sync it before readiness. A running Python watcher must be restarted after a runner-script update because it does not hot-reload.

## Repository submission-format bridge

Before every `candidate-ready.json` and again before every promotion:

1. Apply `skills/format-solution/SKILL.md` to the exact `workspace/rainier-problem/problemNN-*/solution.md` path.
2. Apply `skills/_shared/hard_gates.md` and current constants in `scripts/adv`.
3. Require a nonempty prompt, nonempty standalone Answer, correct answer type, required sections, consecutive steps, valid concept count/length, and matching boxed final answer.
4. Require Answer to use prompt-defined notation except locally bound dummy indices.
5. Require Answer to satisfy both repository raw length and stripped-under-100 portal constraints.

A solution-only formatting edit with byte-identical `problem.md` preserves statement-level difficulty evidence but changes the solution blob SHA; re-audit and refresh the marker.

Any `problem.md` edit invalidates prior exact-blob difficulty evidence.

## Candidate-ready handshake

The watcher may solve only when `solver-results/problemNN/candidate-ready.json` exists on `origin/adversary/problemNN` and matches the exact current pair.

Payload:

```json
{
  "problem": "problem123",
  "mode": "new",
  "ready": true,
  "problem_path": "workspace/rainier-problem/problem123-subdomain/problem.md",
  "problem_blob_sha": "<full git blob sha>",
  "solution_path": "workspace/rainier-problem/problem123-subdomain/solution.md",
  "solution_blob_sha": "<full git blob sha>"
}
```

### Authoring transaction

For every statement-changing cycle:

1. Run proposal-level quality preflight before editing.
2. Treat the candidate as draft and invalidate/remove the ready marker.
3. Complete derivation and write/repair `solution.md` first.
4. Write/update `problem.md` second.
5. Normalize and execute repository formatting.
6. Re-read the exact pair and verify problem/solution agreement.
7. Run `pass-gates.md`; for new/redesigned candidates also run `design-patterns.md`; rerun quality preflight on the exact pair.
8. Resolve final problem and solution blob SHAs.
9. Publish `candidate-ready.json` last.
10. Stop at `*_WAIT_CODEX`.

Any later edit to either candidate file invalidates the marker.

### Watcher eligibility

Before every local solve, verify:

- exactly one current problem path resolves;
- matching sibling solution exists;
- marker parses and has valid `problem`, `mode`, and `ready`;
- marker paths equal the current pair;
- marker problem and solution SHAs equal the current blobs.

If any check fails, wait without invoking the solver.

One unseen exact problem blob receives one intended cold solve. Never rerun it to fish for failure.

## Existing mode authoring stage

1. Read the exact adversary pair.
2. Read official feedback, `latest.json`, matching immutable result, and any evaluator report supplied in the current conversation.
3. If the current statement already has matching accepted evidence, continue from it; do not rerun.
4. If no matching local evidence exists, audit the pair, publish the marker last, and stop at `WAIT_CODEX`.
5. A proof-only/format-only repair with byte-identical `problem.md` preserves difficulty evidence; refresh only the solution SHA/marker after re-audit.
6. A statement change requires fresh exact-blob evidence.

Do not pre-harden an unmeasured candidate unless official/external evidence already identifies a concrete shortcut.

## New mode authoring stage

### Blueprint selection

Silently generate at least three blueprints. Each must specify:

1. honest open Domain/Sub-domain fit;
2. natural object/question;
3. main gateway, if any;
4. visible trigger making the gateway forward-discoverable;
5. 3-6 load-bearing reasoning nodes, including at least two after the gateway;
6. closure certificate;
7. compact human-verifiable answer shape;
8. likely solver shortcut and why it should fail;
9. provenance of every nonstandard coefficient/relation/helper object.

Reject blueprints whose difficulty is mainly theorem recognition, tuned constants, cancellation stacks, hidden encodings of standard objects, giant computation, repeated bookkeeping, excessive notation, or concealment of the main gateway.

Require at least two quality-safe survivors before selecting one.

### Ground truth before statement

1. Derive complete ground truth privately.
2. Resolve the final answer object and proof dependencies before writing the prompt.
3. Write/repair `solution.md` first.
4. Audit every load-bearing claim for reviewer completeness.
5. Write `problem.md` second.
6. Normalize and format.
7. Re-read the exact pair and rerun correctness, taxonomy, answer, naturalness, provenance, compression, reviewer-simulation, and field gates.
8. Publish the ready marker last.
9. Stop at `RAINIER CHECK: WAIT_CODEX`.

## Result state machine

Read `difficulty-evidence.md` before grading any completed solver response.

### No exact local result

Stop at `WAIT_CODEX`.

### Local result mismatch

Treat the current candidate as unmeasured. Never reuse an older verdict.

### `status=success`

1. Open `latest.json.result_file`.
2. Fetch the exact solution named by the ready marker.
3. Confirm intended model/effort settings; otherwise report the deviation explicitly.
4. Compare the solver reasoning to the exact reference solution.
5. Run the required route audit from `difficulty-evidence.md` **before comparing final answers for difficulty classification**.
6. Assign exactly one conceptual verdict.

#### `EXACT_SOLVE`

The model establishes the decisive route and correct answer.

- Difficulty fails.
- Record shortcut diagnostics.
- Propose one depth-based hardening sentence and run proposal preflight before editing.

#### `CONCEPTUAL_SOLVE_EXECUTION_ERROR`

The final answer is wrong, but the response already contains the load-bearing route and only a local arithmetic/sign/transcription/simplification repair remains.

- Treat exactly like `EXACT_SOLVE` for difficulty.
- **Never** label `LOCAL_STUMPED`.
- Record `REPAIR_RADIUS=LOCAL` and the earliest robust shortcut.
- Harden/regenerate using the same rules as a correct solve.

#### `MATERIAL_PARTIAL`

The response makes substantive progress but misses at least one necessary load-bearing node.

- Do not promote yet.
- Run the strong-model adversarial audit on the exact pair.
- If the strong audit finds the standard/canonical completion, treat as solver success and harden/regenerate.
- Only if the missing dependency is structural and the strong audit passes may this be considered along with other difficulty evidence.

#### `TRUE_STUMP`

Use only when a genuinely new load-bearing dependency is missing and `REPAIR_RADIUS=STRUCTURAL`.

- This is first-line evidence, not promotion authorization.
- Run every correctness/quality/reviewer/format gate.
- Run the mandatory strong-model adversarial audit before promotion.
- Promote only if the strong audit is `STRONG_AUDIT_PASS` and no contrary exact-blob strong-evaluator evidence exists.

### Strong-model adversarial audit

For every candidate that would otherwise promote due to `TRUE_STUMP` or timeout:

1. Re-read the exact statement and solution without relying on the GPT-5.5 final-answer verdict.
2. Use the strongest reviewer reasoning available in the authoring environment.
3. Answer the six audit questions in `difficulty-evidence.md`.
4. Assign one of:
   - `STRONG_AUDIT_PASS`;
   - `STRONG_AUDIT_CONCEPTUAL_SOLVE`;
   - `STRONG_AUDIT_CANONICAL_COLLAPSE`;
   - `STRONG_AUDIT_UNCERTAIN`.
5. Only `STRONG_AUDIT_PASS` permits promotion on difficulty grounds.

This audit is intentionally separate from GPT-5.5. Its job is to detect false stumps caused by execution noise or a solver-specific miss.

### User-provided strong evaluator reports

When the user supplies an HTML/report from independent stronger models:

1. Verify the embedded statement matches the exact current candidate text/blob.
2. Grade each attempt with the same conceptual verdict taxonomy.
3. Any exact or conceptual solve blocks promotion and triggers hardening/regeneration.
4. If two or more independent strong evaluators converge on the same canonical shortcut, mark `BLUEPRINT_TRANSPARENT` and prefer blueprint retirement/regeneration over concealment hardening.
5. If the report is for a different statement, use it only as design feedback.

### Hardening/regeneration rule

When local or strong evaluation conceptually solves the candidate:

- diagnose `COMMON ENTRY`, `COMMON REDUCTION`, `FIRST DECISIVE RECOGNITION`, `RECOVERY PATH`, `EARLIEST ROBUST SHORTCUT`;
- propose one sentence naming a new intrinsic dependency that defeats the shortcut;
- require at least one new reasoning node after the original common entry point;
- run proposal-level quality preflight before editing;
- reject proposals based on concealment, extra notation, tuned coefficients, bigger dimensions, more cases, or repeated computation.

For `mode=new`, allow at most one same-blueprint structural revision. If the revised clean blob is also conceptually solved, retire the blueprint and regenerate.

When multiple independent strong evaluators already expose the same canonical route, default to regeneration unless a clearly natural depth hardening exists.

After any statement revision: solution first, problem second, formatter, full audits, new blob SHAs, ready marker last, then `HARDENED_WAIT_CODEX` or `REGENERATED_WAIT_CODEX`.

### `status=timeout`

Accept timeout as first-line evidence only when metadata confirms the expected runner contract, including GPT-5.5, Medium, and the intended timeout.

A timeout **still requires the strong-model adversarial audit**. Do not promote merely because the clock expired.

### `SOLVER_ERROR`

Do not promote. Infrastructure failure is not difficulty evidence. Preserve the candidate and report `BLOCKED_RUNNER` with one concrete recovery action.

## Official and automated feedback

Official portal evidence outranks all local/external preflight evidence.

- Difficulty PASS -> freeze the exact statement unless another official gate requires repair.
- Difficulty FAIL/borderline -> treat the trace as stronger shortcut evidence; revise structurally.
- `contrived`, `over-engineered`, `synthetic`, `overly layered`, `awkward construction`, or cancellation-tuning -> `QUALITY_REDESIGN`.
- `unjustified`, `unsupported`, `not self-contained` -> repair proof architecture when feasible; statement changes require fresh evidence.
- Domain/Sub-domain mismatch -> fix taxonomy or redesign emphasis honestly.
- Submission-format failure -> repair deterministically; prompt/Answer-Type changes require fresh statement evidence.
- Any statement edit invalidates old portal percentages and exact-blob solver verdicts.

## Promotion preflight

Before touching `main`:

1. Run `pass-gates.md` on the exact selected pair.
2. Run the repository submission-format bridge again.
3. Confirm the local exact-blob verdict is qualifying (`TRUE_STUMP` or qualifying timeout), unless explicitly waived.
4. Confirm the strong-model audit is `STRONG_AUDIT_PASS`, unless explicitly waived.
5. Confirm no matching user-provided strong-evaluator evidence contains an exact or conceptual solve.
6. Confirm taxonomy freshness and all correctness/reviewer/naturalness gates.
7. Confirm the ready marker still matches both exact blobs.

If a solution-only format repair is needed, edit adversary, re-audit, and refresh the solution SHA/marker. If `problem.md` changes, stop promotion and obtain fresh evidence.

Only after all gates are green: update `main` solution first and problem second, then re-fetch both and verify exact equality. Do not copy solver-control/evidence files or chat binding to `main`.

Report `RAINIER CHECK: MAIN_READY_FOR_RAINIER` only when the exact promoted pair passes deterministic submission checks and difficulty evidence policy.

## Chat binding and notification routing

The binding always points to the author/reviewer chat. Use it only for local notification routing. Never use a GitHub result URL as a click fallback.

## Compact statuses

Use concise states:

- `RAINIER CHECK: WAIT_CODEX`
- `RAINIER CHECK: HARDENED_WAIT_CODEX`
- `RAINIER CHECK: REGENERATED_WAIT_CODEX`
- `RAINIER CHECK: MAIN_READY_FOR_RAINIER`
- `RAINIER CHECK: BLOCKED_RUNNER`
- `RAINIER CHECK: TAXONOMY_STALE`

When useful, include a one-line evidence note such as `CONCEPTUAL_SOLVE_EXECUTION_ERROR`, `TRUE_STUMP`, `STRONG_AUDIT_CANONICAL_COLLAPSE`, or `BLUEPRINT_TRANSPARENT`.
