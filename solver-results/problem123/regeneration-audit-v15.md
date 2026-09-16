# problem123 regeneration audit v15

## Trigger

The exact candidate with problem blob `94d265e193a58a850dd2a8a4a092e4415ca8c0d3` received one GPT-5.5 Medium cold solve. The immutable result is `solver-results/problem123/94d265e193a5.json`.

Difficulty verdict: `EXACT_SOLVE`.

Route audit:

- **COMMON ENTRY:** rewrite the information matrix as a Hankel moment matrix and use canonical moments on `[0,1]`.
- **COMMON REDUCTION:** factor the Hankel determinant into independent canonical-moment factors.
- **FIRST DECISIVE RECOGNITION:** the canonical-moment determinant factorization with `p_1=1/3`.
- **LOAD-BEARING NODES RECOVERED:** all nodes needed for the exact optimum, including admissibility and exact simplification.
- **MISSING LOAD-BEARING NODE:** none.
- **RECOVERY PATH:** none needed; the solver returned the exact value.
- **REPAIR RADIUS:** `LOCAL` vacuously because no repair was needed.
- **EARLIEST ROBUST SHORTCUT:** canonical moments make the remaining optimization factor-by-factor.
- **CANONICAL COLLAPSE:** yes.

The previous blob therefore fails the difficulty gate and is not promotable.

## Structural hardening

The revised problem keeps the experimental-design setting but changes from an arbitrary Borel design measure to an **exact five-point, equally weighted design** with prescribed centroid. This is a natural exact-design restriction rather than notation or concealment.

Hardening sentence:

> The solver's original shortcut fails because the revised problem introduces the natural dependency that all five design weights are fixed and the centroid constraint therefore couples the support locations; this arises from exact experimental-design allocation and forces a constrained Vandermonde/KKT problem, a differential equation for the support polynomial, and a global concavity certificate.

This is the first clean same-domain structural revision after the regenerated approximate-design candidate.

## Quality-redesign preflight

- The visible object is a standard exact D-optimal polynomial-regression design.
- Equal weights arise intrinsically from an exact five-run design; they are not fitted to the answer.
- The centroid `1/3` is an explicit balance constraint, not a cancellation coefficient.
- The support quartic is not guessed: it is forced by the KKT equations and the root identity `p''(r)/p'(r)=2\sum_{s\ne r}(r-s)^{-1}`.
- Global optimality is certified by strict concavity and the full first-order inequality, not by checking a guessed configuration.
- The final discriminant is obtained from displayed Euclidean divisions and the resultant identity; no hidden computer algebra is required.
- After the Vandermonde gateway, multiple load-bearing nodes remain: KKT coupling, ODE reconstruction, feasibility/root placement, global concavity certification, and exact discriminant evaluation.
- No `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER` step is present.

Preflight verdict: `PASS`.

## Taxonomy

Snapshot date: `2026-09-16`.

- Domain: `Probability and Statistics`
- Sub-domain: `Experimental design and causal inference`
- Status: open, 4 remaining in the snapshot.
- Problem Type: `Optimization`
- Answer Type: `Exact scalar`

No domain change in this revision.

## Exact candidate pair

- `problem.md` blob: `9694f2373be8c85b62682157987236692e3fe585`
- `solution.md` blob: `6b601d2fa77bffd4f3fc7794e34a17e4fe1f5da4`

Independent symbolic verification confirms the KKT ODE, all three displayed Euclidean divisions, the root intervals, `disc(q)=5^3/(2^10 3^8)`, `disc(xq)=5^5/(2^20 3^14)`, and final value `1/(2^20 3^14)`.

Submission-shape checks on the exact text:

- prompt payload: 304 characters, below 2000;
- `## Steps` payload: below 5000 characters, below 10000;
- standalone Answer: 22 raw characters and 20 after stripping `$`/whitespace;
- 5 solution concepts, each below 100 characters;
- consecutive Steps 1-4;
- boxed final answer matches the standalone Answer exactly;
- classification matches between problem and solution.

This new statement has no valid difficulty evidence yet. Old solver/evaluator evidence does not transfer across the statement change.
