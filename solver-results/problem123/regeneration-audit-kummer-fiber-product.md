# Regeneration audit — Kummer fiber product — problem123

## Why regeneration was required

The exact Elementary Number Theory revision blob `4f68bc3891d858d8ed8f91d9d61190a03d68ca54` was solved correctly by GPT-5.5 Medium in the single permitted revised run. The solver compressed the reference classification to the equivalent condition `2m=q^a+q^b` and closed exact exponents with a one-carry Kummer witness. Because this was already the one allowed same-blueprint structural revision in new mode, that blueprint is retired rather than hardened again.

## Fresh blueprint triage

1. **Topology and Geometry -> Algebraic geometry — fiber product of two Kummer covers.** Natural object: the genus of the smooth projective normalization of two cyclic covers of `P^1` sharing one finite branch point and infinity. Gateway: view the function field as a Galois Kummer cover over `C(x)`. Post-gateway work: prove the full degree `mn`, compute simultaneous inertia at `0`, separate inertia at `1` and `lambda`, derive the parity-sensitive inertia at infinity, then close with Riemann-Hurwitz. **Selected.**
2. **Abstract Algebra -> Galois theory — compositum of maximal real cyclotomic fields.** Quality-safe local-global sign compatibility through CRT, but once translated to congruences `a=+-1 mod m_i` the degree is controlled by a short sign-counting argument. **Survived preflight but not selected.**
3. **Analysis -> Calculus of variations — one-dimensional obstacle-energy minimization with a mass constraint.** Natural free-boundary problem with a genuine active/inactive regime, but the one-dimensional Euler-Lagrange/free-boundary computation is shorter and more standard for the target solver. **Survived preflight but not selected.**
4. **Linear Algebra -> Tensor and multilinear algebra — invariant extremum for a binary cubic tensor.** Rejected because a clean Bombieri-norm formulation exposes an orthogonal harmonic decomposition that makes the remaining optimization too close to a standard invariant calculation.

At least two quality-safe alternatives survived; the Kummer fiber-product problem was selected for its stronger simultaneous-local-ramification closure.

## Exact selected pair

- **Problem path:** `workspace/rainier-problem/problem123-algebraic-geometry/problem.md`
- **Problem blob:** `bfcaebb18d58b0a6d87e443639a5a1463545b0b1`
- **Solution path:** `workspace/rainier-problem/problem123-algebraic-geometry/solution.md`
- **Solution blob:** `c3adc5306512f865470b5576f0be6e7c457c2b40`
- **Domain/Sub-domain:** Topology and Geometry -> Algebraic geometry.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists Algebraic geometry with 2 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** `1+mn-(m+n+(2+1_{2|mn})gcd(m,n))/2` in the displayed indicator notation.
- **Standalone answer length:** 63 stripped characters; below the 100-character gate.

## Difficulty architecture

Serial reasoning nodes:

1. use the valuation at `x=0` to force `[C(x,y):C(x)]=m`;
2. use the unramified place over `x=lambda` to force the second extension degree `n`, hence total degree `mn` and Galois group `C_m x C_n`;
3. translate visible valuations into simultaneous inertia generators, with the shared branch at `0` giving order `lcm(m,n)`;
4. analyze infinity separately from valuations `(-2,-2)`, producing a genuine parity transition when at least one of `m,n` is even;
5. convert each inertia order into the full ramification contribution and apply Riemann-Hurwitz;
6. simplify the two parity regimes to one compact exact expression and close independence of `lambda`.

Knowing Riemann-Hurwitz alone does not solve the problem: the load-bearing work is the exact normalization degree and the inertia orders in the fiber product, especially at the two common branch locations.

## Forward provenance / anti-reverse-engineering preflight

- **Kummer-cover viewpoint: STANDARD_NATURAL_REPRESENTATION.** It is the literal function-field presentation given in the statement.
- **Valuations at `0`, `1`, `lambda`, and infinity: FORCED_BY_EQUATIONS.** These are exactly the zeros and poles of the two displayed radicands.
- **Inertia generators `(1,1)` and `(-2,-2)`: FORCED_BY_EQUATIONS.** Their coordinates are the two local valuations, not tuned coefficients.
- **`d=gcd(m,n)`: CANONICAL.** It appears as the reciprocal index of the diagonal inertia generator through `lcm(m,n)=mn/d`.
- **Parity split at infinity: FORCED_BY_EQUATIONS.** It comes from the pole order `2` in both radicands and the order of `-2` in the two cyclic factors.
- **Riemann-Hurwitz: STANDARD_NATURAL_REPRESENTATION.** Once the exact cover and inertia data are established, genus is canonically determined by the ramification divisor.

No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

Compression test: writing the curve as a Galois Kummer cover does not make the problem routine. The degree proof, simultaneous inertia at shared branch points, parity-sensitive infinity analysis, and complete ramification count remain load-bearing.

Reviewer-quote simulation: there are no special correction terms, hidden generator relations, or invariant combinations inserted after the fact. Every non-obvious quantity appears only after the visible divisor data force it.

## Promotion gates pre-solver

- **Gate A — honest taxonomy:** PASS. The requested object is the genus of an algebraic curve obtained by normalization of a fiber product.
- **Gate B — natural statement:** PASS. Two cyclic covers with partially overlapping branch loci form a standard independently meaningful algebraic curve.
- **Gate C — forward provenance:** PASS as detailed above.
- **Gate D — difficulty architecture:** PASS. Degree, local inertia, parity interaction, and global Riemann-Hurwitz closure are serial and load-bearing.
- **Gate E — ground truth:** PASS. The proof covers all `m,n>=2`, both parity regimes, all common divisors, and all `lambda` distinct from `0,1`.
- **Gate F — reviewer completeness:** PASS. Extension degree, local inertia, absence of additional branch points, infinity lcm reduction, and each Riemann-Hurwitz contribution are derived explicitly.
- **Gate G — solver evidence:** PENDING. This exact problem blob is fresh and must receive exactly one GPT-5.5 Medium cold solve.
- **Gate H — portal format:** PASS. Five consecutive Steps, three Solution Concepts, exact Final Answer line, matching metadata, compact standalone answer.
- **Gate I — originality:** PASS. Repository searches for the displayed Kummer-fiber-product equations and simultaneous-inertia/Riemann-Hurwitz skeleton found no matching corpus item on `main`.

## State

The exact normalized pair is quality-safe and ready for one cold solver measurement. The ready marker must be updated last using the exact blob SHAs above.
