# Regeneration audit v11 — problem123

## Why regeneration was required

The exact moment-extremal blob `49e74f606d8911252fed6ae4e278f4f96106385c` was solved correctly by GPT-5.5 Medium in one intended run. Its earliest robust shortcut is the classical cubic Hermite / Gaussian-Radau quadrature route: fixed moments make cubic expectations invariant, while `h_t^{(4)}>0` gives the two sharp one-sided interpolation certificates. A proposal-level quality preflight rejected same-blueprint changes such as adding another moment, excluding current nodes, or replacing the resolvent by another 4-convex function because they preserve the same quadrature skeleton and mainly add degree or bookkeeping. The moment-extremal blueprint is therefore retired after v1.

## Blueprint triage

At least three structurally different candidates were compared before authoring.

1. **Analysis -> Calculus of variations — zero-mean symmetric clamped-beam mode.** Natural object: the least bending-energy Rayleigh quotient among even clamped functions with zero average. Gateway: the variational quotient forces a fourth-order Euler-Lagrange equation with one constant Lagrange multiplier. Post-gateway work remains substantial: derive the secular determinant, identify the first positive root rather than an arbitrary stationary root, prove its exact interval and uniqueness, and construct the attaining eigenfunction. **Selected.**
2. **Linear Algebra -> Tensor and multilinear algebra — Frobenius-normalized discriminant of a real `2x2` matrix pencil.** Quality-safe and natural, but after orthogonalizing the two slices the determinant quadratic form becomes a compression of a signature `(2,2)` involution, making the sharp `1/4` bound too short for the target solver. **Survived preflight but not selected.**
3. **Analysis -> Fourier analysis — one-step Toeplitz moment completion.** Quality-safe, but the feasible disk for the next Fourier coefficient falls out of a single Schur-complement calculation once the Toeplitz PSD condition is written. **Survived preflight but not selected.**
4. **Number Theory -> Diophantine equations — simultaneous Pell-type compatibility.** Rejected because a clean exact formulation either reduces to standard unit-group recognition or requires long recurrence/congruence casework; the latter would be computation depth rather than conceptual depth.

At least two quality-safe alternatives survived; the clamped-beam problem was selected because its closure genuinely requires reasoning after the Euler-Lagrange gateway.

## Exact selected pair

- **Problem path:** `workspace/rainier-problem/problem123-calculus-of-variations/problem.md`
- **Problem blob:** `9b4756f099e1785ad1c189f1d9a2ba0e8f6e1147`
- **Solution path:** `workspace/rainier-problem/problem123-calculus-of-variations/solution.md`
- **Solution blob:** `b9fadfe780f0d6bcabeeb4eb96be9199e2708293`
- **Domain/Sub-domain:** Analysis -> Calculus of variations.
- **Current slot evidence:** the 2026-09-11 taxonomy snapshot lists Calculus of variations with 1 remaining slot and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** `kappa^4`, where `3*pi/2 < kappa < 2*pi` and `kappa(cot kappa + coth kappa)=2`.
- **Standalone answer length:** 91 stripped characters including `\displaystyle`; below the 100-character gate.

## Difficulty architecture

Natural object: the first zero-average symmetric vibration mode of a clamped beam, expressed as the sharp bending-energy Rayleigh quotient.

Serial reasoning nodes:

1. prove the constrained Rayleigh infimum is attained rather than assuming an eigenfunction exists;
2. derive the Euler-Lagrange equation and show the zero-mean constraint produces exactly one constant forcing term;
3. solve the even fourth-order ODE and combine the two clamped conditions with the integral constraint into a `3x3` secular determinant;
4. reduce the determinant to `k(cot k+coth k)=2` without losing the `sin k=0` cases;
5. prove there is no positive root below `3*pi/2`, then prove existence and uniqueness of the first root in `(3*pi/2,2*pi)`;
6. construct the corresponding smooth extremizer and use the zero-mean condition to close the Rayleigh quotient exactly at `kappa^4`.

The Euler-Lagrange equation is only the entry point. A solver that merely writes the fourth-order ODE has not identified the correct spectral branch or proved that its root is globally first.

## Forward-provenance / anti-reverse-engineering preflight

- **Rayleigh quotient / Euler-Lagrange equation: CANONICAL.** It is forced directly by the requested infimum.
- **Constant forcing term: FORCED_BY_EQUATIONS.** The only additional linear constraint is `integral f=0`, so the annihilator of the admissible variation space is exactly the span of that integral functional.
- **Hyperbolic/trigonometric basis: STANDARD_NATURAL_REPRESENTATION.** It is the canonical solution basis of `f''''=k^4 f + constant`; no coordinate disguise is introduced.
- **Secular determinant: FORCED_BY_EQUATIONS.** Its three rows are exactly `f(1)=0`, `f'(1)=0`, and `integral_0^1 f=0`.
- **Function `F(k)=k(cot k+coth k)-2`: FORCED_BY_EQUATIONS.** It is the determinant equation after division by nonzero factors, with the excluded `sin k=0` cases checked separately.
- **Euler-product identity in the root audit: STANDARD_NATURAL_REPRESENTATION.** It is used only to prove that the secular equation has no root in `(0,pi)`; the product is stated explicitly and logarithmically differentiated, not invoked as a black-box cancellation device.
- **Extremizer `f_kappa`: FORCED_BY_EQUATIONS.** Its coefficients are obtained from the nullspace of the boundary/mean system; they are not fit to the final answer.

No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

Compression test: stating the secular equation directly would delete the variational derivation and the boundary/mean compatibility, but it would not make the remaining problem routine because the first-root location and attainment still require proof. In the actual statement, however, the secular equation is not hidden behind custom notation; it is derived canonically from the visible variational constraints.

Reviewer-quote simulation: there are no special correction terms, custom invariant combinations, or tuned coefficients. The root equation is visibly the compatibility condition of the Euler-Lagrange ODE, and the solution explains its provenance before using it.

## Ground-truth / reviewer completeness audit

- **Well-defined class:** in one dimension `H^2` functions have absolutely continuous representatives for `f` and `f'`, so the clamped traces are meaningful.
- **Existence:** the solution derives uniform bounds/equicontinuity from the clamped integral formulas, passes to uniform limits of `f,f'` and a weak `L^2` limit of `f''`, and uses lower semicontinuity.
- **Euler-Lagrange:** the quotient derivative is written explicitly on the zero-mean tangent space, and the codimension-one annihilator argument derives the constant multiplier.
- **ODE form:** `lambda>0` is justified; `lambda=k^4`; all even solutions are displayed.
- **Secular determinant:** the exact `3x3` system is displayed and expanded; `k=j*pi` is checked separately.
- **No early root:** on `(0,pi)` the stated Euler products combine to `sin k sinh k/k^2`, whose logarithmic derivative gives a strictly negative series. On `(pi,3*pi/2)` positivity is immediate.
- **First-root uniqueness:** on `(3*pi/2,2*pi)`, endpoint signs are explicit and derivative estimates show strict decrease.
- **Attainment:** the explicit `f_kappa` is checked against evenness, all clamped boundary data, and the mean condition; two integrations by parts then give the exact quotient.
- **Numerical sanity only (not proof):** `kappa ~= 5.2676575303368146`, hence `Lambda ~= 769.9634832419018`; direct numerical integration of the displayed extremizer agrees with `kappa^4`.

## Promotion gates pre-solver

- **Gate A — honest taxonomy:** PASS. The primary request is a constrained variational minimum; the boundary-value spectrum is generated by the Euler-Lagrange condition.
- **Gate B — natural statement:** PASS. The zero-average even clamped mode is an independently meaningful sharp beam-energy problem; every condition has a direct geometric/variational role.
- **Gate C — forward provenance:** PASS as detailed above.
- **Gate D — difficulty architecture:** PASS. Direction discovery, multiplier derivation, compatibility determinant, nontrivial first-root proof, and attainment are serial and load-bearing.
- **Gate E — ground truth:** PASS. Existence, positivity, root localization/uniqueness, and equality construction cover the full stated class.
- **Gate F — reviewer completeness:** PASS. No load-bearing determinant, limiting, boundary, or root-order claim is left as a bare direct calculation.
- **Gate G — solver evidence:** PENDING. This exact statement blob is fresh and must receive exactly one GPT-5.5 Medium cold solve.
- **Gate H — portal format:** PASS. Five consecutive Steps, three Solution Concepts, exact Final Answer line, matching metadata, and a 91-character standalone answer.
- **Gate I — originality:** PASS. Repository searches for `clamped beam best constant mean zero H^2`, `Poincare inequality fourth derivative clamped boundary moment constraint`, `clamped zero mean cot coth`, and `Rayleigh quotient f'' even H2 zero mean` found no matching corpus item on `main`. The mechanism registry contains only an unrelated hidden cyclic basepoint-orbit skeleton.

## State

The exact normalized pair is quality-safe and ready for one cold solver measurement. Publish `candidate-ready.json` only after this audit, using the exact two blob SHAs above.
