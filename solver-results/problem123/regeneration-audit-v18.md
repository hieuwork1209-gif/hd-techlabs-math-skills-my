# problem123 regeneration audit v18

## Trigger

Exact candidate blob `1316e591da799f8a2b7ad519b57ef4d8ccd61fa4` received the intended single GPT-5.5 Medium run and was solved exactly.

Difficulty verdict: `EXACT_SOLVE`.

Route audit:

- **COMMON ENTRY:** formulate the nonlinear rational approximation error and impose three alternating minimax contacts.
- **COMMON REDUCTION:** scale the two interior critical points by `sqrt(B)` and reduce stationarity/equal-error conditions to symmetric equations in their product and sum.
- **FIRST DECISIVE RECOGNITION:** the scale-free stationary system determines `2R^2+3R-1=0`, after which endpoint matching and elimination determine the exact error polynomial.
- **LOAD-BEARING NODES RECOVERED:** alternating contact geometry, stationary-point reduction, endpoint condition, elimination to the exact quartic, global sign-change certificate, and irreducibility.
- **MISSING LOAD-BEARING NODE:** none.
- **RECOVERY PATH:** none needed; the solver returned the exact requested polynomial.
- **REPAIR RADIUS:** `LOCAL` vacuously because no repair was needed.
- **EARLIEST ROBUST SHORTCUT:** standard rational minimax contact equations followed by scale-free symmetrization.
- **CANONICAL COLLAPSE:** yes for this revised approximation-theory blueprint.

The preceding polynomial-minimax blob in the same blueprint was also solved exactly. The rational-minimax candidate was the single permitted structural revision. Under the one-revision rule, the entire Approximation theory blueprint is now retired rather than hardened again.

## Retired blueprint

`Optimization and Numerical Mathematics -> Approximation theory`

Do not add degrees, poles, extra contacts, or tuned coefficients to disguise the same minimax gateway.

## New blueprint search

1. **Probability foundations — exchangeable Bernoulli truncated-moment extremum (selected).** Infinite exchangeability gives a latent Bernoulli parameter, but de Finetti is only the gateway. The target sixth-degree Bernstein expectation then requires a matched primal/dual truncated-moment certificate, support recurrence, branch/sign analysis, and exact evaluation.
2. **Bifurcation theory — generalized Hopf in planar biochemical/neural models.** Rejected at preflight because the clean two-dimensional examples reduced the first Lyapunov coefficient to a short standard formula or low-degree equation, leaving too little depth after the Hopf gateway.
3. **Differential topology — cosine level sets on a torus.** Rejected because the natural regular-level examples compressed to a standard Morse-skeleton calculation with a short homology formula, making the blueprint too canonical for the difficulty target.

## New candidate provenance

The new statement fixes the first three joint-success probabilities of an infinite exchangeable Bernoulli sequence at the natural values `1/2, 1/3, 1/4` and asks for the largest probability of exactly two successes in six trials.

After de Finetti, the moment vector is fixed at the first three moments of the uniform distribution on `[0,1]`; this is intrinsic probabilistic data, not a coefficient fit. The objective is the natural Bernstein polynomial `15x^2(1-x)^4` for exactly two successes.

The decisive dual slack is derived from moment duality. A cubic majorant must cancel the degree-six, degree-five, and degree-four terms of the Bernstein polynomial. A matched primal-dual certificate with one endpoint contact and two double interior contacts has slack

`-15 x (x-a)^2 (x-b)^2 (x-r)`.

Degree cancellation forces relations among `S=a+b`, `P=ab`, and `r`; independently, the moment recurrence on the matching three-point support forces `P=2S/3-1/2`. Their compatibility gives `9S^2-28S+21=0`, and the nonnegative-slack branch selects `S=(14-sqrt(7))/9`. Thus the algebraic constants arise from visible dual and moment equations rather than target fitting.

## Quality-redesign preflight

- The visible object is a standard and independently meaningful exchangeability extremum.
- De Finetti is a natural representation, not hidden encoding.
- At least three load-bearing dependencies remain after de Finetti: dual degree cancellation, primal moment recurrence/positivity, and global certificate/evaluation.
- The contact polynomial is forced by complementary slackness and polynomial degree; it is not inserted solely to cancel later terms.
- The support points and weights are proved feasible and positive.
- Global optimality follows from an explicit cubic majorant whose slack has a displayed nonnegative factorization.
- Exact symbolic verification confirms the moment constraints, cubic cancellation, slack sign, and final value.
- No `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER` step remains.

Preflight verdict: `PASS`.

## Domain change

`Optimization and Numerical Mathematics -> Approximation theory` => `Probability and Statistics -> Probability foundations`.

The taxonomy snapshot dated `2026-09-16` lists `Probability foundations` as open.

## Exact candidate pair

- `problem.md` blob: `cded7bc73a9d6e602322306452285046da7f9423`
- `solution.md` blob: `0b1c164a1f0d91c674ff1304bad1145257263dbb`

Submission-shape review:

- prompt is nonempty and well below the 2000-character cap;
- standalone Answer is a single exact scalar and well below both answer-length caps;
- four consecutive substantial steps;
- five plain-text solution concepts, each below 100 characters;
- boxed final object matches the standalone Answer exactly;
- Problem Type and Answer Type agree between problem and solution;
- the `## Steps` payload is well below the 10000-character cap.

This statement has no valid difficulty evidence yet. All previous local solver evidence belongs to retired statement blobs and does not transfer.
