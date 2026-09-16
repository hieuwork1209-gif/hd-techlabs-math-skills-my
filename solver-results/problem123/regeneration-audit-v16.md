# problem123 regeneration audit v16

## Trigger

Exact candidate blob `9694f2373be8c85b62682157987236692e3fe585` received the intended single GPT-5.5 Medium run and was solved exactly.

Difficulty verdict: `EXACT_SOLVE`.

Route audit:

- **COMMON ENTRY:** factor the information determinant as a squared Vandermonde product.
- **COMMON REDUCTION:** impose the centroid-constrained Lagrange equations on the ordered support points.
- **FIRST DECISIVE RECOGNITION:** encode the interior critical points as roots of the derivative polynomial and recover the quartic candidate by coefficient comparison.
- **LOAD-BEARING NODES RECOVERED:** boundary reduction, quartic construction, feasibility, discriminant evaluation, and the exact optimum.
- **MISSING LOAD-BEARING NODE:** none.
- **RECOVERY PATH:** none needed.
- **REPAIR RADIUS:** `LOCAL` vacuously because no repair was needed.
- **EARLIEST ROBUST SHORTCUT:** Vandermonde plus KKT on the equal-weight support points.
- **CANONICAL COLLAPSE:** yes for this revised experimental-design blueprint.

The previous clean blob in the same blueprint was also solved exactly, via canonical moments. The equal-weight/centroid version was the one permitted same-blueprint structural revision. Under the one-revision rule, the experimental-design blueprint is now retired rather than hardened again.

## Retired blueprint

`Probability and Statistics -> Experimental design and causal inference`

Do not add more moment constraints, support points, dimensions, or tuned coefficients to hide the same determinant gateway.

## New blueprint search

1. **Approximation theory — constrained minimax polynomial (selected).** Fix the two leading coefficients of a quartic, minimize its uniform norm on `[-1,1]`, and ask for the primitive irreducible polynomial of the optimum. Natural serial dependencies are an alternation/sign-change certificate, critical-point reconstruction, and algebraic elimination/irreducibility.
2. **Quadratic residues — coupled character constraint.** Rejected because clean exact instances tended either to collapse to CRT/character sums or to require opaque finite enumeration.
3. **Optimal control — state-coupled bang-bang problem.** Rejected because a nontrivial exact switching structure introduced more case bookkeeping than genuine reasoning.

The selected blueprint passes the anti-reverse-engineering preflight. The fixed leading coefficients define the approximation class directly; alternation is intrinsic to minimax approximation; the critical points are forced by contact equalities; and algebraic elimination is required by the requested minimal polynomial rather than fitted to a target answer.

## Domain change

`Probability and Statistics -> Experimental design and causal inference` => `Optimization and Numerical Mathematics -> Approximation theory`.

The 2026-09-16 taxonomy snapshot lists `Approximation theory` as open.

## Exact new candidate

- problem path: `workspace/rainier-problem/problem123-approximation-theory/problem.md`
- problem blob: `cfbc976d729eaba18fabff7fe45b6249a60c1119`
- solution path: `workspace/rainier-problem/problem123-approximation-theory/solution.md`
- solution blob: `c0d80f65ff958a5f6ff21e30926ff6ccdbfdfe19`

Final hostile audit:

- the four-contact lower bound is proved directly by a sign-change argument, not invoked as a black-box alternation theorem;
- the critical-point equations are derived from the two equal-contact integrals;
- the feasible root branch and the bound `3/5<v<2/3` are explicitly certified;
- the algebraic elimination displays its subresultant remainders;
- irreducibility is proved modulo `5` without an opaque CAS factorization;
- prompt, answer, concepts, step structure, and solution length are within repository hard gates;
- the answer uses only the prompt-defined variable `T` and the boxed answer matches exactly.

Pre-ready verdict: `PASS` on Gates A-F and I-K. Difficulty is unmeasured for this new statement blob.
