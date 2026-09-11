# Promotion audit — problem123 de66d9047bf7

## Exact pair

- Problem blob: `de66d9047bf7904f317e5b0055ae59ad7ee43b7b`
- Solution blob: `1e277cccfb8a04c3ad1a6d2b068d9b768dc913ef`
- Branch measured: `adversary/problem123`
- Solver evidence: GPT-5.5 / Medium / one run / 2100 seconds
- Local difficulty verdict: `LOCAL_STUMPED` because the solver asserted the collision-field equality and degree collapse without deriving the common radical or proving field equality.

## Gates

- A Honest taxonomy: PASS — Topology and Geometry -> Algebraic geometry; current snapshot has 2 open slots.
- B Natural statement: PASS — genus change under collision of branch points is an intrinsic algebraic-geometry question.
- C Forward provenance: PASS — generic Kummer structure comes directly from the equations; the collision radical is derived canonically from `lcm(m,n)` and Bezout coefficients.
- D Difficulty architecture: PASS — generic degree/inertia, collision degree collapse, special inertia, and genus comparison are serially dependent; the solver missed the collision reconstruction dependency.
- E Ground truth: PASS — generic and collision degrees, all branch/inertia orders, parity case through `h=gcd(ell,2)`, and both Riemann-Hurwitz computations are established over the full stated range.
- F Reviewer completeness: PASS — local valuation arguments, the Bezout reconstruction, field equality, degree `ell`, and ramification contributions are explicitly derived.
- G Solver evidence: PASS — exact blob, intended model/settings, one run; materially incomplete on a load-bearing dependency.
- H Portal format: PASS — consecutive steps, 3 concepts, symbolic/exact metadata consistent, standalone answer under 100 stripped characters.
- I Originality: PASS — main-branch corpus search found no matching genus-drop/Kummer-collision skeleton before promotion.

Final promotion question: PASS. The exact problem remains clean and mathematically motivated independently of the solver outcome.

## Main verification

Promoted solution first and problem second. Re-fetched `main` blobs match the exact adversary pair byte-for-byte:

- `main:workspace/rainier-problem/problem123-algebraic-geometry/solution.md` -> `1e277cccfb8a04c3ad1a6d2b068d9b768dc913ef`
- `main:workspace/rainier-problem/problem123-algebraic-geometry/problem.md` -> `de66d9047bf7904f317e5b0055ae59ad7ee43b7b`
