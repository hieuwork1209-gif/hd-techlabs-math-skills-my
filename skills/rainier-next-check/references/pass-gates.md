# Rainier Pass Gates

Run these as rejection gates. Do not average them into a score: one serious failure blocks promotion.

## Gate A — Honest taxonomy

Pass only if:

- selected Domain/Sub-domain describes the primary requested object;
- auxiliary methods do not dominate the true mathematics;
- classification would remain the same after removing cosmetic vocabulary;
- Domain Explanation is affirmative and specific.

Reject when the natural reaction is “this is really a problem about X, not the chosen sub-domain.”

## Gate B — Natural statement

Pass only if the object/question is worth asking independently of the target constant.

Reject when difficulty mainly comes from tuned constants, cancellation devices, nested helper notation, mechanical casework, giant calculations, verbose encodings of standard structures, or relations that are natural only because the intended solution later makes them cancel.

Diagnostic questions:

1. Can the problem be described naturally in one sentence?
2. Would it still look interesting if the answer were unknown?
3. Does every parameter have a conceptual role?
4. Is the difficulty a new idea or merely more work?
5. Could a cleaner formulation preserve the same conceptual obstacle?
6. If the decisive structure were stated directly, would meaningful difficulty remain?

Several unfavorable answers -> redesign.

## Gate C — Forward provenance / anti-reverse-engineering

Pass only if every decisive non-obvious object has a forward discovery path from visible mathematics.

For each correction, substitution, invariant, auxiliary object, coefficient choice, or normal form, require:

- visible trigger;
- derivation rather than guess;
- canonicity/forcedness/intrinsic motivation;
- a later load-bearing role.

Automatic rejection signals:

- `GUESSED_TO_CANCEL`;
- `FIT_TO_TARGET`;
- `COEFFICIENT_TUNED`;
- `BACKSOLVED_FROM_FINAL_ANSWER`;
- a custom encoding mainly hiding a standard algebra/representation;
- special combinations introduced only because they later cancel;
- hardening whose main effect is making the same successful representation harder to recognize.

Compression test: if naming the decisive structure makes the statement dramatically shorter and the remainder routine, reject the encoded version.

A hidden representation may pass only when it is intrinsically triggered and at least two substantial reasoning nodes remain after discovery.

## Gate D — Difficulty architecture

Require all of:

- **direction discovery** — the decisive representation/invariant/certificate is not handed to the solver;
- **tool construction** — a problem-specific lemma, reduction, certificate, recursion, coupling, or normal form must be built;
- **idea interaction** — at least two ideas are load-bearing and neither alone finishes the problem;
- **serial dependence** — later steps genuinely require earlier discoveries;
- **closure** — uniqueness/exhaustiveness/attainment/inverse consistency is proved.

Reject recognize-theorem-apply-simplify problems even if the algebra is long.

Also reject a candidate when a strong audit can summarize the solve as one standard gateway followed by routine one-variable optimization, routine diagonalization, routine coefficient extraction, or similarly canonical cleanup.

## Gate E — Ground-truth correctness

Pass only if the solution independently establishes:

- well-definedness over the full stated range;
- existence where needed;
- uniqueness/exhaustiveness where needed;
- all sign/branch/parity/boundary cases;
- exact answer type;
- consistency after every statement edit.

For asymptotics/limits, check uniformity/continuity/interchange hypotheses whenever load-bearing.

## Gate F — Reviewer completeness

Use a hostile standard: if a reviewer can reasonably write “asserted without derivation,” strengthen the proof before promotion.

### Load-bearing theorem/identity usage

State the exact form, instantiate all objects/hypotheses, and show the substitution/reduction that produces the claimed conclusion.

### Expansions and finite calculations

Do not hide determinant factors, signs, ranks, traces, coefficients, minors, or allowed cases behind “direct calculation.” Show reproducible intermediate work or a general formula.

### Limit/interchange/continuity steps

State why inversion, determinant, log, sum/integral interchange, differentiation, expectation, continuation, or limiting operations are valid where used.

## Gate G — Local solver evidence integrity

Read `difficulty-evidence.md` before assigning a verdict.

The exact statement blob must be measured once with intended GPT-5.5 Medium settings unless explicitly waived.

A completed response must be graded by **reasoning route**, not final-answer equality.

Qualifying classifications:

- `EXACT_SOLVE` -> difficulty FAIL;
- `CONCEPTUAL_SOLVE_EXECUTION_ERROR` -> difficulty FAIL;
- `MATERIAL_PARTIAL` -> not promotion-ready; requires strong audit;
- `TRUE_STUMP` -> first-line difficulty evidence only;
- qualifying timeout -> first-line evidence only;
- infrastructure failure -> no evidence.

### Conceptual-solve rule

If the solver recovers the common entry, decisive reduction, and all load-bearing nodes, and the wrong answer can be fixed by a local arithmetic/sign/transcription/simplification correction to its own displayed work, classify `CONCEPTUAL_SOLVE_EXECUTION_ERROR`.

Do **not** count it as mathematically wrong for difficulty purposes.

A wrong scalar after an otherwise complete proof architecture is not a stump.

### True-stump rule

Use `TRUE_STUMP` only when completion requires a genuinely new load-bearing dependency absent from the response (`REPAIR_RADIUS=STRUCTURAL`).

Do not count:

- local execution mistakes;
- infrastructure failures;
- malformed/unjudgeable output;
- stale/mismatched blob evidence;
- repeated attempts on the same blob;
- easier custom solver configurations unless explicitly chosen and reported.

## Gate H — Strong-model adversarial audit

A local GPT-5.5 stump/timeout is insufficient by itself.

Before promotion, run the strong audit from `difficulty-evidence.md` with the strongest reviewer reasoning available in the authoring environment on the exact statement/solution pair.

Pass only with `STRONG_AUDIT_PASS`.

Block promotion on:

- `STRONG_AUDIT_CONCEPTUAL_SOLVE`;
- `STRONG_AUDIT_CANONICAL_COLLAPSE`;
- `STRONG_AUDIT_UNCERTAIN`.

The strong audit must explicitly test whether:

- a standard gateway collapses the problem;
- the GPT-5.5 miss was merely execution noise;
- fewer than two meaningful nodes remain after the gateway;
- the route is canonical enough that a stronger solver/reviewer is likely to recover it directly.

### External evaluator evidence

When the user supplies matching HTML/report from stronger independent evaluators, grade each attempt conceptually.

Any exact or conceptual solve on the exact statement is contrary evidence and blocks promotion until a new statement is measured.

If two or more independent strong evaluators converge on the same canonical shortcut, mark `BLUEPRINT_TRANSPARENT` and prefer regeneration over adding concealment.

Official portal evidence outranks these preflight evaluators.

## Gate I — Portal format / repository submission compatibility

Mirror the deterministic repository checks, not remembered portal rules. Read `skills/_shared/hard_gates.md` and current constants in `scripts/adv`.

Before candidate-ready and again before promotion require at least:

- apply `skills/format-solution/SKILL.md` to the exact Rainier solution path;
- Math Problem is nonempty and within current prompt limit;
- `## Answer` is nonempty and contains no `\\boxed`;
- Answer is within current raw repository limit and under 100 characters after stripping `$` plus whitespace;
- Answer is exactly one mathematical object using prompt-defined notation except locally bound dummy indices;
- final boxed object matches `## Answer` character-for-character;
- `## Steps` is under current solution-length cap;
- Solution Concepts count/length pass;
- steps are consecutive;
- Domain, Sub-domain, Problem Type, Answer Type, Domain Explanation are present and consistent;
- no stale metadata remains.

A solution-only formatting repair preserves statement evidence only when `problem.md` is byte-identical, but requires a refreshed solution SHA/ready marker.

If fitting the answer requires changing the prompt or Answer Type, treat that as a statement change requiring fresh evidence.

## Gate J — Originality and corpus distance

Reuse mathematical themes, not distinctive statement skeletons, constants, notation, or solution sequences.

Reject a candidate that is essentially an existing problem with renamed variables, changed constants, larger dimension, or one extra constraint.

## Gate K — Human-verifiable answer shape

Pass only if the requested final object can be checked from the proof with modest arithmetic.

Reject opaque many-digit scalars when a natural factorized/product/certificate form would expose the derivation more safely.

The answer must not depend on solution-local undefined notation.

## Final promotion question

Before promotion ask internally:

> If GPT-5.5 had not produced a wrong final answer, would I still defend this as a clean, self-contained, naturally motivated expert problem whose difficulty survives a stronger reviewer and whose package passes deterministic submission checks?

If the answer is no, redesign rather than promote.

## Promotion evidence bundle

Without an explicit user waiver, promotion requires all of:

1. exact-blob local verdict is `TRUE_STUMP` or qualifying timeout;
2. `STRONG_AUDIT_PASS`;
3. no matching strong-evaluator exact/conceptual solve;
4. Gates A-F and I-K all pass;
5. exact ready marker still matches both blobs.

A wrong final answer alone never satisfies this bundle.
