# Rainier Pass Gates

Run these as rejection gates. Do not average them into a score: one serious failure blocks promotion.

## Gate A — Honest taxonomy

Pass only if:

- the selected Domain/Sub-domain describes the primary requested object;
- auxiliary methods do not dominate the true mathematics;
- the classification would remain the same after removing cosmetic vocabulary;
- the Domain Explanation is affirmative and specific, not defensive taxonomy camouflage.

Reject when the natural reviewer reaction is “this is really a problem about X, not the chosen sub-domain.”

## Gate B — Natural statement

Pass only if the mathematical object/question is worth asking independently of the target constant.

Every definition, parameter, and index must have an intrinsic role. Prefer standard notation and a small number of definitions.

Reject when difficulty mainly comes from:

- constants tuned so several terms vanish;
- alternating/finite-difference devices inserted to move the first nonzero coefficient;
- nested helper symbols hiding a custom integrand or matrix;
- many special cases/indices that only increase bookkeeping;
- large determinants/matrices or high-degree expressions used only as computational burden;
- long mechanical expansions after the key idea is already obvious;
- a verbose custom presentation of a standard object whose main purpose is to conceal the standard structure;
- families of relations or coefficients that are natural only because the intended solution later makes them cancel.

Diagnostic questions:

1. Can the object and question be described naturally in one sentence?
2. Would the problem still look interesting if the answer were unknown?
3. Does each parameter have a conceptual role?
4. Is the difficulty a new idea or just more work?
5. Could a simpler formulation preserve the same conceptual obstacle?
6. If the decisive hidden structure were stated directly, would meaningful difficulty remain?

Several unfavorable answers -> redesign.

## Gate C — Forward provenance / anti-reverse-engineering

Pass only if every decisive non-obvious object introduced in the solution has a forward discovery path from the visible problem. Apply `quality-redesign-preflight.md`.

For each correction, substitution, invariant, auxiliary matrix/function, coefficient choice, or normal form, the solution must make clear:

- what visible obstruction/equation/symmetry triggers the search for it;
- how it is derived rather than guessed;
- why the choice is canonical, forced, extremal, universal, or otherwise intrinsic;
- what later reasoning node genuinely depends on it.

Automatic rejection signals:

- `GUESSED_TO_CANCEL`;
- `FIT_TO_TARGET`;
- `COEFFICIENT_TUNED`;
- `BACKSOLVED_FROM_FINAL_ANSWER`;
- a custom generators-and-relations encoding used mainly to hide a standard algebra or representation;
- defining several special invariant combinations first and only afterwards checking that all brackets/terms cancel;
- a hardening move whose main effect is to make the same successful representation harder to recognize.

Use the compression test: rewrite the problem using the decisive structure found in the solution. If the statement becomes dramatically shorter and the remaining mathematics becomes routine, reject the encoded version.

A hidden representation may pass only when it is forced by an intrinsic obstruction and at least two load-bearing reasoning nodes remain after discovery.

## Gate D — Difficulty architecture

A strong candidate should force all of:

- **direction discovery:** the statement does not name the decisive representation/invariant/certificate;
- **tool construction:** the solver must build a problem-specific lemma, reduction, certificate, recursion, coupling, or normal form;
- **idea interaction:** at least two ideas are load-bearing and neither alone finishes the problem;
- **serial dependence:** later steps genuinely require earlier discoveries;
- **closure:** the last stage proves uniqueness/exhaustiveness/attainment/inverse consistency rather than stopping at a plausible candidate.

Reject recognize-theorem-apply-simplify problems even if the final algebra is lengthy.

## Gate E — Ground-truth correctness

Pass only if the solution independently establishes:

- all objects are well-defined over the full stated parameter range;
- existence where needed;
- uniqueness/exhaustiveness where needed;
- no missing sign/branch/parity/boundary cases;
- the final expression exactly matches the requested answer type;
- every statement edit has a matching fresh solution audit.

For asymptotics/limits, check uniformity or continuity hypotheses whenever they are load-bearing.

## Gate F — Reviewer completeness

Use a hostile standard: if a reviewer can reasonably write “asserted without derivation,” strengthen the proof before promotion.

### Named theorem/identity usage

When a named result is load-bearing:

1. state the exact form being used;
2. identify all instantiated objects and dimensions/hypotheses;
3. show the substitution/reduction that produces the displayed conclusion.

Example pattern for matrix identities: state the determinant identity, define the actual `P,U,V` (or analogous objects), and show conformability/invertibility when required.

### Taylor/endpoint/asymptotic expansions

Do not merely assert coefficients that control the argument. Show enough derivatives/algebra to produce the first relevant coefficients and justify the remainder order.

### Repeated Rolle / zero accumulation / multiplicity arguments

If several derivatives are claimed to vanish from accumulating zeros, explicitly give the repeated Rolle/Taylor mechanism. Do not compress the entire implication into one sentence when it is load-bearing.

### Quadratic/Gaussian/matrix block derivations

If a posterior precision, Hessian, covariance, or block matrix is central, expand the quadratic form and collect the blocks explicitly. Do not jump directly to the final block matrix.

### “Direct calculation”

This phrase is acceptable only for low-risk arithmetic. If the calculation determines a determinant factor, key coefficient, sign, rank, invariant, or final constant, show reproducible intermediate work.

### Limit/interchange/continuity steps

State why inversion, determinant, log, sum/integral interchange, differentiation, expectation, or limiting operations are valid in the required neighborhood/range.

## Gate G — Solver evidence integrity

Pass local difficulty only if the exact statement blob was measured once with the intended solver settings and the result is one of:

- mathematically wrong;
- materially incomplete in a way that misses a necessary dependency;
- valid timeout with the expected timeout metadata.

Do not count:

- infrastructure failures;
- malformed output;
- a result from an older statement blob;
- repeated attempts on the same blob;
- a custom easier solver configuration unless the user explicitly chose it and the deviation is reported.

## Gate H — Portal format

Before promotion ensure at least:

- problem prompt is nonempty and within the current Rainier prompt limit;
- standalone answer is nonempty, within the current answer limit, and does not contain `\\boxed` if the portal requires a plain standalone answer;
- solution steps are consecutive `Step 1:`, `Step 2:`, ...;
- the last required line follows the current exact Final Answer format;
- Solution Concepts count/length obey current portal rules;
- Domain, Sub-domain, Problem Type, Answer Type, and Domain Explanation are present;
- Problem Type and Answer Type agree between problem and solution/package;
- no stale metadata remains after redesign.

Use current repository/portal limits when they differ from historical values.

## Gate I — Originality and corpus distance

The problem may reuse a mathematical theme, but not the distinctive statement skeleton, constants, notation, or solution sequence of an existing corpus item.

Prefer reusing **successful difficulty principles**, not copying accepted problems.

Reject a candidate that is essentially an existing problem with renamed variables, changed constants, larger dimension, or one extra constraint.

## Final promotion question

Before promotion ask internally:

> If GPT-5.5 had not been stumped, would I still defend this as a clean, self-contained, naturally motivated expert problem with an honest taxonomy label?

If the answer is no, redesign instead of promoting.
