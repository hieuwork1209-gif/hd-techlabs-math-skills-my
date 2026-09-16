# problem123 regeneration audit v17

## Trigger

Exact candidate blob `cfbc976d729eaba18fabff7fe45b6249a60c1119` received the intended single GPT-5.5 Medium run and was solved exactly.

Difficulty verdict: `EXACT_SOLVE`.

Route audit:

- **COMMON ENTRY:** recognize the task as best uniform approximation of `-x^4-x^3` by quadratics.
- **COMMON REDUCTION:** use four alternating contacts and the two interior critical-point equations.
- **FIRST DECISIVE RECOGNITION:** the scalar polynomial equioscillation/contact system determines the extremal quartic.
- **LOAD-BEARING NODES RECOVERED:** contact pattern, critical-point elimination, exact optimal error, and irreducibility of its minimal polynomial.
- **MISSING LOAD-BEARING NODE:** none.
- **RECOVERY PATH:** none needed.
- **REPAIR RADIUS:** `LOCAL` vacuously because no repair was needed.
- **EARLIEST ROBUST SHORTCUT:** standard polynomial minimax structure followed by direct elimination.
- **CANONICAL COLLAPSE:** yes for the scalar polynomial candidate.

The previous statement therefore fails the difficulty gate and is not promotable.

## Same-blueprint structural revision

The revised problem stays in Approximation theory but moves from a linear polynomial approximation space to the nonlinear rational family

`R_{A,B}(x)=A x^2/(x^2+B)`, `A,B>0`.

Hardening sentence:

> The solver's original shortcut fails because the revised problem introduces the natural denominator-scale dependency of rational minimax approximation; after identifying an alternating contact pattern, the solver must prove a sign-change certificate for a nonlinear rational family, solve two coupled stationary contacts in scale-free variables, and close the endpoint and denominator-feasibility conditions before algebraic elimination.

This is the one permitted clean same-blueprint structural revision. If the exact revised blob is conceptually solved by GPT-5.5 Medium, retire the Approximation theory blueprint rather than adding degree, coefficients, or concealment.

## Quality-redesign preflight

- The visible object is a standard two-parameter rational approximating family with a positive denominator on the whole interval.
- The target function `x` and interval `[0,1]` are intrinsic and require no tuned constants.
- The denominator scale `B` is a genuine nonlinear approximation parameter, not notation hiding the previous polynomial problem.
- The global certificate is derived directly: two positive zeros would be forced in the difference of two competing approximants, while that difference has a numerator affine in `x^2` and therefore at most one positive zero.
- The scale-free variables arise canonically from `y=sqrt(B)` in the stationary equation.
- The algebraic relation `2q^2+3q-1=0` is forced by equal stationary values and a common numerator scale; it is not fitted to the final answer.
- The endpoint scale is forced by the third alternating contact and factors explicitly.
- The full sup-norm bound is proved from the monotonicity of `H(t)=(1+t^2)^2/(2t)`; it is not inferred from sampled points.
- The final polynomial is obtained by displayed elimination from two quadratic relations, and irreducibility is proved modulo `3`.
- No `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER` step is present.

Preflight verdict: `PASS`.

## Taxonomy

Snapshot date: `2026-09-16`.

- Domain: `Optimization and Numerical Mathematics`
- Sub-domain: `Approximation theory`
- Status: open in the current snapshot.
- Problem Type: `Exact computation`
- Answer Type: `Polynomial or rational function`

No domain change in this revision.

## Exact candidate pair

- `problem.md` blob: `1316e591da799f8a2b7ad519b57ef4d8ccd61fa4`
- `solution.md` blob: `eaa87def95a59366a50af6dc1807bf86e65181f8`

Submission-shape checks:

- prompt is nonempty and comfortably below the 2000-character cap;
- `## Steps` is comfortably below the 10000-character cap;
- standalone Answer is a single polynomial and comfortably below both answer-length caps;
- 5 solution concepts, each below 100 characters;
- consecutive Steps 1-5;
- boxed final answer matches the standalone Answer exactly;
- classification matches between problem and solution.

This revised statement has no valid difficulty evidence yet. Evidence for `cfbc976d729e...` does not transfer across the statement change.
