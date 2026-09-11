# Regeneration audit v10 — problem123

## Why regeneration was required

The fresh order-statistics maximal-correlation blob `8838ee73f40f737e5a257efcab7cbc1ed30c70b7` was solved correctly by GPT-5.5 Medium in its single intended run. The solver used the same decisive route as the reference: conditional Beta laws, invariant polynomial flags, orthogonal-polynomial singular functions, and the decreasing singular spectrum. A same-blueprint revision would naturally amount to suppressing the degree-one mode or asking for a later spectral coefficient, which adds bookkeeping rather than a new mathematical dependency. That hardening proposal fails the depth-vs-concealment quality test, so the blueprint is retired without spending the optional revision.

## Blueprint triage

1. **Random variables and distributions — width of a resolvent expectation under three fixed moments.** Natural object: quantify the exact remaining uncertainty in `E[1/(1+tX)]` when the first three moments of a bounded law are known. Gateway: because moments through degree three are fixed, sharp bounds must come from cubic dual certificates. Visible trigger: multiplying the residual by `1+tx` turns it into a quartic whose sign and contact multiplicities can be controlled exactly. Post-gateway nodes: derive the two-point lower principal representation from the moment equations, prove the lower quartic sign certificate, derive the endpoint three-point upper representation, prove the upper sign certificate, and close by subtracting the attained extrema. **Selected.**
2. **Calculus of variations — symmetric clamped-beam obstacle with a free contact interval.** The free boundary and matching conditions are natural and quality-safe, but once symmetry reveals the contact pattern the remaining Euler-Lagrange calculation is comparatively standard. **Survived preflight but not selected.**
3. **Modular arithmetic and congruences — singular quadratic congruence count over powers of two.** Rejected because the intended difficulty was dominated by valuation casework rather than a serial conceptual unlock.
4. **Linear transformations — kernel growth of a structured nilpotent operator on symmetric matrices.** Rejected because the cleanest solution is largely recognition of a standard `sl_2` decomposition, making theorem recognition too dominant.

At least two quality-safe families survived; the moment-extremal problem was selected because its two sharp dual certificates and attainment closure remain nontrivial after the gateway is found.

## Exact selected pair

- **Problem path:** `workspace/rainier-problem/problem123-random-variables-and-distributions/problem.md`
- **Problem blob:** `49e74f606d8911252fed6ae4e278f4f96106385c`
- **Solution path:** `workspace/rainier-problem/problem123-random-variables-and-distributions/solution.md`
- **Solution blob:** `40cfa3bb4106aafff511a04b54d3ba4374a2d84b`
- **Domain/Sub-domain:** Probability and Statistics -> Random variables and distributions.
- **Current slot evidence:** the 2026-09-11 taxonomy snapshot lists this sub-domain with 19 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** `a t^4/[2(2a+1)(t+1)(t+2)(a t^2+4at+4a+2t+2)]`.
- **Standalone answer length:** 61 stripped characters including `\displaystyle`, below the 100-character gate.

## Ground-truth checks

The two candidate extremal laws were checked directly against all three prescribed moments. Symbolic simplification gives

- lower extremum
  `L_a(t)=(2a+1)(t+2)/(a t^2+4at+4a+2t+2)`;
- upper extremum
  `U_a(t)=(8at+8a+t^2+4t+4)/(2(2a+1)(t+1)(t+2))`;
- exact difference
  `U_a(t)-L_a(t)=a t^4/[2(2a+1)(t+1)(t+2)(a t^2+4at+4a+2t+2)]`.

For the lower certificate, `N_q=1-(1+tx)q` is a positive constant times the square of the forced quadratic whose roots are the two support points. For the upper certificate, it is a positive constant times `x(x-1)(x-1/2)^2`, which has the required opposite sign on `[0,1]`. Thus both bounds are global and attained.

## Forward provenance / anti-reverse-engineering preflight

- **Cubic dual certificate: FORCED_BY_EQUATIONS.** Moments through degree three are exactly the quantities fixed across all admissible laws, so cubic expectations are the canonical dual functionals.
- **Quartic residual `N_q`: FORCED_BY_EQUATIONS.** It comes directly from clearing the positive denominator of the visible resolvent `1/(1+tx)`; no coefficient is introduced by fitting.
- **Lower support quadratic: CANONICAL.** It is the unique monic quadratic orthogonal to `1,x` under the given moment functional; its roots and the equal weights are solved from the moment equations.
- **Upper support `{0,1/2,1}`: FORCED_BY_EQUATIONS.** For the endpoint-plus-one-interior contact pattern required by a nonpositive quartic, the vanishing cubic together with the prescribed moments forces the interior point to be `1/2`, after which the weights are uniquely determined.
- **Hermite-contact cubics: CANONICAL.** Their four interpolation conditions are exactly the multiplicities required by the quartic sign certificates; uniqueness follows from four zeros counted with multiplicity.

No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

Compression test: saying “use principal moment representations” would shorten the proof language but would not make the answer routine. One must still derive both representations from the moments, build and sign two different quartic residuals, prove global optimality, and subtract the exact attained values.

Reviewer-quote simulation: the solution derives every support node and every contact pattern before using it; nothing is introduced merely because a later cancellation works.

## Promotion gates pre-solver

- **Gate A — honest taxonomy:** PASS. The variable law and its moment-constrained distribution family are the primary objects.
- **Gate B — natural statement:** PASS. Exact uncertainty of an expectation from finitely many moments is independently meaningful; both parameters `a,t` have intrinsic roles.
- **Gate C — forward provenance:** PASS as above.
- **Gate D — difficulty architecture:** PASS. Direction discovery, dual construction, two distinct extremal certificates, and attainment are serial and load-bearing.
- **Gate E — ground truth:** PASS for all `a>0,t>0`; all support points lie in `[0,1]`, all masses are positive, and both extrema are explicitly attained.
- **Gate F — reviewer completeness:** PASS. Moment equations, support derivations, certificate signs, and algebraic simplifications are shown explicitly; no compactness theorem is needed.
- **Gate G — solver evidence:** PENDING. This exact blob has not been measured.
- **Gate H — portal format:** PASS. Four consecutive Steps, three Solution Concepts, matching metadata, exact Final Answer line, answer length under the gate.
- **Gate I — originality:** PASS. Repository searches for the resolvent/moment-extremal skeleton and quartic-contact formulation returned no matching corpus item on `main`.

## State

The exact normalized pair is quality-safe and ready for exactly one GPT-5.5 Medium cold solve. Publish `candidate-ready.json` only after this audit and after re-verifying the exact pair SHAs.