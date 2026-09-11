# Regeneration audit v12 — problem123

## Why regeneration was required

The exact Calculus-of-Variations blob `9b4756f099e1785ad1c189f1d9a2ba0e8f6e1147` was solved correctly by GPT-5.5 Medium in one intended run. The solver followed the full intended route: direct-method attainment, constant Lagrange multiplier, the fourth-order clamped-beam ODE, the scalar `cot/coth` secular equation, localization of its first positive root, and construction of the attaining eigenfunction. The earliest robust shortcut is that the zero-mean constraint contributes only a constant forcing term, leaving a standard one-parameter beam spectrum. Candidate hardenings based on another moment, point spring, or extra boundary/interface condition were rejected because they mainly lengthen the secular determinant or make the standalone answer difficult to grade. The variational blueprint is therefore retired after v1.

## Blueprint triage

At least three structurally different candidates were compared before authoring.

1. **Optimization and Numerical Mathematics -> Convex optimization — maximize algebraic connectivity of a weighted path under a unit edge-resource budget.** The affine coordinate of the path gives a universal Rayleigh upper certificate; equality then forces the only possible quadratic edge-weight profile. Substantial work remains after that gateway: prove the forced profile actually attains the bound by deriving its exact spectrum, and close uniqueness of all optimizers. **Selected.**
2. **Number Theory -> Modular arithmetic and congruences — count zeros of the Eisenstein norm form modulo prime powers.** Natural and quality-safe, with split/inert/ramified local regimes, but each regime collapses quickly after factoring the quadratic algebra and was judged too close to a standard local-counting exercise. **Survived preflight but not selected.**
3. **Topology and Geometry -> Convex geometry — John ellipsoid of a centrally symmetric cube cut by a diagonal slab.** Natural and quality-safe, but the permutation symmetry reduces the problem to two semiaxes and one short determinant/volume optimization, leaving too little reasoning after symmetry reduction. **Survived preflight but not selected.**
4. **Abstract Algebra -> Field theory — degree of a radical/cyclotomic compositum with parameterized intersections.** Rejected because a clean exact version is dominated by recognition of standard Kummer-intersection facts, while a self-contained version becomes case-heavy rather than conceptually deeper.

At least two alternatives survived the proposal-level quality screen. The weighted-path design was selected because equality forcing and spectral closure are independent load-bearing steps.

## Exact selected pair

- **Problem path:** `workspace/rainier-problem/problem123-convex-optimization/problem.md`
- **Problem blob:** `72cfb8ab7be6514f6347e0f62305123f3e9a0330`
- **Solution path:** `workspace/rainier-problem/problem123-convex-optimization/solution.md`
- **Solution blob:** `6ccfe5c95ea654ea919f07fbb50cf540e571c61f`
- **Domain/Sub-domain:** Optimization and Numerical Mathematics -> Convex optimization.
- **Current slot evidence:** the 2026-09-11 taxonomy snapshot lists Convex optimization with 18 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** `M_n=12/(n(n^2-1)), w_i^*=6i(n-i)/(n(n^2-1))`.
- **Standalone answer length:** 72 stripped characters including `\displaystyle`; below the 100-character gate.

## Difficulty architecture

Natural object: allocate a fixed total edge weight on a path to maximize its algebraic connectivity, and identify every optimal allocation.

Serial reasoning nodes:

1. use the Rayleigh characterization of `lambda_2`;
2. discover the affine path coordinate whose edge increments are all equal, making the unit edge budget a universal upper certificate;
3. enforce equality in that certificate to derive the optimizer recurrence and force `w_i` proportional to `i(n-i)`;
4. recognize from the quadratic coefficients and first-difference operator that polynomial degree is an invariant flag;
5. orthogonalize the flag and derive the complete spectrum `k(k+1)` of the unnormalized forced Laplacian;
6. scale back to obtain the sharp value and use the equality recurrence to prove uniqueness of the optimizer.

The upper bound alone does not prove attainability. The forced weight profile alone does not prove that its affine eigenvector is the second mode. The full spectrum is therefore a genuinely separate closure step.

## Forward-provenance / anti-reverse-engineering preflight

- **Affine coordinate `v_i=i-(n+1)/2`: CANONICAL.** The path comes with a natural vertex coordinate; centering it makes it orthogonal to constants, and its unit edge increments interact directly with the fixed total edge budget.
- **Quadratic weights `i(n-i)`: FORCED_BY_EQUATIONS.** They are obtained by requiring equality in the universal Rayleigh certificate, which forces the affine vector to satisfy the eigenvalue equation. Solving that recurrence uniquely produces the quadratic profile.
- **Polynomial-degree flag: STANDARD_NATURAL_REPRESENTATION.** Once the forced edge coefficients are quadratic while the Laplacian uses first differences, polynomial degree is visibly preserved. The solution states this trigger before introducing the orthogonal basis.
- **Orthogonal polynomials: CANONICAL.** Gram-Schmidt on the invariant degree flag is the unique monic basis adapted to the uniform inner product; it is not chosen to cancel terms.
- **Eigenvalues `k(k+1)`: FORCED_BY_EQUATIONS.** They are the leading coefficients obtained by applying the forced Laplacian to monic degree-`k` polynomials.

No decisive object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

Compression test: stating the quadratic weights in advance would remove the optimization/equality-forcing half of the problem, but the solver would still have to prove that the affine mode is truly the spectral gap by deriving or otherwise certifying the spectrum. The current statement is already the natural network-design formulation, not an encoding of a hidden standard object.

Reviewer-quote simulation: there are no tuned constants, custom relations, or auxiliary combinations introduced only because they cancel. Every special object is either visible from the path geometry or forced by equality in the variational bound.

## Promotion gates pre-solver

- **Gate A — honest taxonomy:** PASS. The primary task is optimizing a concave spectral objective over the edge-weight simplex; linear algebra supplies the certificate.
- **Gate B — natural statement:** PASS. Optimizing algebraic connectivity under a resource budget is an independently meaningful network-design problem; `n` and all edge weights have intrinsic roles.
- **Gate C — forward provenance:** PASS as detailed above.
- **Gate D — difficulty architecture:** PASS. Direction discovery, equality forcing, exact spectral verification, and uniqueness form a serial chain.
- **Gate E — ground truth:** PASS. The derivation covers every `n>=2`, including `n=2`, and the proposed weights are positive and normalized.
- **Gate F — reviewer completeness:** PASS. The Rayleigh form, equality recurrence, normalization, invariant polynomial flag, leading-coefficient calculation, complete spectrum, and uniqueness implication are explicit.
- **Gate G — solver evidence:** PENDING. This exact problem blob is fresh and must receive exactly one GPT-5.5 Medium cold solve.
- **Gate H — portal format:** PASS. Four consecutive Steps, three Solution Concepts, exact Final Answer line, matching metadata, and a compact standalone answer.
- **Gate I — originality:** PASS. Repository searches for weighted-path algebraic-connectivity optimization and the `i(n-i)` weighted-Laplacian spectrum found no matching corpus item on `main`.

## Independent sanity checks

For `n=2,...,8`, direct numerical diagonalization of the forced weights gives total edge weight `1` and exact spectral pattern, to floating precision,
`6 k(k+1)/(n(n^2-1))`, so the second eigenvalue equals `12/(n(n^2-1))`. These checks are only error detection; the submitted proof is symbolic.

## State

The exact normalized pair is quality-safe and ready for one cold GPT-5.5 Medium measurement. Publish `candidate-ready.json` only after this audit, using the exact two blob SHAs above.
