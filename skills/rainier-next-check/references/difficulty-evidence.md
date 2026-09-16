# Difficulty Evidence and Conceptual-Solve Grading

Use this reference whenever a solver/evaluator result is graded and again before promotion.

## Governing rule

Difficulty is about missing reasoning, not merely a wrong final scalar.

A solver has **conceptually solved** a statement when its own response contains the load-bearing route needed to finish the exact problem, even if the final answer is wrong because of a local arithmetic, sign, transcription, simplification, or substitution error.

Never classify `final_answer != ground_truth` as a stump without first grading the reasoning route.

## Required route audit

For every completed solver response, record internally:

- **COMMON ENTRY** — first correct representation/reduction that an expert would naturally use.
- **COMMON REDUCTION** — main structural simplification reached by the solver.
- **FIRST DECISIVE RECOGNITION** — point after which the intended proof architecture is essentially determined.
- **LOAD-BEARING NODES RECOVERED** — which necessary reasoning nodes from the reference solution the solver actually established.
- **MISSING LOAD-BEARING NODE** — the earliest necessary node not established, if any.
- **RECOVERY PATH** — whether the solver could finish by repairing its own displayed work or would need a genuinely new idea.
- **REPAIR RADIUS** — `LOCAL` or `STRUCTURAL`.
- **EARLIEST ROBUST SHORTCUT** — shortest reliable route that made the candidate easy.
- **CANONICAL COLLAPSE** — whether the statement reduces to a standard theorem/representation plus routine computation once the common entry is found.

`REPAIR_RADIUS=LOCAL` means no new mathematical idea is required: examples include arithmetic correction, sign correction, a missed factor, evaluating an already-derived formula correctly, a transcription error, or checking an endpoint already identified.

`REPAIR_RADIUS=STRUCTURAL` means completion requires a genuinely new lemma, representation, compatibility condition, invariant, obstruction, uniqueness argument, or other load-bearing dependency not contained in the response.

## Verdict taxonomy

### `EXACT_SOLVE`

The response reaches the correct answer and establishes the decisive route. Difficulty fails for this blob.

### `CONCEPTUAL_SOLVE_EXECUTION_ERROR`

The final answer is wrong or malformed, but:

- the common entry and decisive reduction are correct;
- every load-bearing node needed for the intended solution is present, or only routine closure remains;
- the error has `REPAIR_RADIUS=LOCAL`.

Treat this exactly like a correct solve for difficulty. Diagnose the shortcut and harden/regenerate. It is **not** stump evidence.

### `MATERIAL_PARTIAL`

The response makes meaningful progress but misses at least one load-bearing node. Do not promote automatically. Run the strong-model audit below to determine whether the missing node represents real depth or whether the candidate still collapses canonically.

### `TRUE_STUMP`

Use only when the response is wrong/materially incomplete because it misses a necessary load-bearing dependency and `REPAIR_RADIUS=STRUCTURAL`.

A `TRUE_STUMP` is only first-line difficulty evidence. It does not by itself authorize promotion; the strong-model audit and all quality gates must still pass.

### `TIMEOUT_STUMP`

Use only for a valid timeout that satisfies the runner metadata contract. A timeout still requires the strong-model audit before promotion.

### `INFRA_FAILURE`

UI/runner/tool/infrastructure failure is never difficulty evidence.

## Strong-model adversarial audit

GPT-5.5 Medium is a calibration solver, not a binary oracle. Before promotion of any `TRUE_STUMP` or `TIMEOUT_STUMP` candidate, run a separate adversarial audit with the strongest reviewer model available in the authoring environment on the exact statement/solution pair.

The strong audit must answer:

1. What is the earliest natural entry point?
2. Does a standard representation/theorem/symmetry reduce the problem to routine work?
3. After the main gateway, how many genuinely load-bearing reasoning nodes remain?
4. Can the candidate be solved by a short canonical chain that the GPT-5.5 run nearly found?
5. Is the apparent hardness caused by a local execution error, notation, bookkeeping, or concealment rather than missing mathematics?
6. Does the problem still satisfy Gate D (direction discovery, tool construction, idea interaction, serial dependence, closure)?

Strong-audit verdicts:

- `STRONG_AUDIT_PASS` — no canonical collapse is found and at least one substantial dependency remains beyond standard entry points.
- `STRONG_AUDIT_CONCEPTUAL_SOLVE` — reviewer can recover the decisive route; harden/regenerate.
- `STRONG_AUDIT_CANONICAL_COLLAPSE` — once a standard gateway is recognized, the remainder is routine; redesign/harden by depth.
- `STRONG_AUDIT_UNCERTAIN` — insufficient confidence; do not promote on local stump alone.

## User-provided external evaluator evidence

When the user supplies an HTML/report from stronger external evaluators (for example GPT-5.x High, Claude/Opus-class models, or another independent reviewer), treat it as explicit difficulty evidence if the embedded statement matches the exact candidate statement.

For each evaluator attempt, grade the reasoning using the same verdict taxonomy above; do not reduce it to correct/incorrect final answer.

Rules:

- Any `EXACT_SOLVE` or `CONCEPTUAL_SOLVE_EXECUTION_ERROR` on the exact statement is contrary evidence to promotion and triggers hardening/regeneration.
- If two or more independent strong evaluators converge on the same canonical shortcut, classify `BLUEPRINT_TRANSPARENT`. Prefer retiring/regenerating the blueprint instead of stacking concealment machinery.
- If the report is for a different statement blob/text, use it only as design feedback, not exact-blob evidence.
- Official portal feedback still outranks local/external preflight evidence.

## Regression example: arithmetic false stump

A solver may derive the correct Gram-matrix reduction, symmetry averaging, circulant spectrum, feasible interval, and correct critical point, then mis-evaluate the determinant by a constant factor and return the wrong final answer. This is `CONCEPTUAL_SOLVE_EXECUTION_ERROR`, because correcting the already-derived expression needs no new mathematical idea.

The candidate must be treated as solved for difficulty purposes.

## Promotion requirement

Without an explicit user waiver, promotion requires all of:

- exact-blob local evidence is `TRUE_STUMP` or qualifying `TIMEOUT_STUMP`;
- strong-model audit is `STRONG_AUDIT_PASS`;
- no matching user-provided strong-evaluator report contains an `EXACT_SOLVE` or conceptual solve;
- every non-difficulty quality/format/taxonomy gate passes.

A wrong final answer alone is never sufficient promotion evidence.
