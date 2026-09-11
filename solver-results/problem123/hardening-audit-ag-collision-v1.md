# Hardening audit — AG collision revision

## Trigger

The first Algebraic Geometry blob `bfcaebb18d58b0a6d87e443639a5a1463545b0b1` was solved correctly by GPT-5.5 Medium. The solver's earliest robust shortcut was the standard Kummer-compositum reduction followed by four inertia orders and Riemann-Hurwitz.

## Structural revision

The revised problem keeps the same natural one-parameter family but asks for the genus drop when the two nonzero branch points collide at `lambda=1`.

The original shortcut no longer finishes the problem because the collision changes the compositum itself: the generic degree is `mn`, whereas the normalized collision field must be reconstructed as the single Kummer extension of degree `lcm(m,n)`. This dependency is intrinsic to the degeneration and forces a second normalization/Riemann-Hurwitz computation before the genus comparison.

## Exact pair

- problem path: `workspace/rainier-problem/problem123-algebraic-geometry/problem.md`
- problem blob: `de66d9047bf7904f317e5b0055ae59ad7ee43b7b`
- solution path: `workspace/rainier-problem/problem123-algebraic-geometry/solution.md`
- solution blob: `1e277cccfb8a04c3ad1a6d2b068d9b768dc913ef`
- taxonomy: `Topology and Geometry -> Algebraic geometry`
- final answer: `1+mn-(m+n+d(1+h)+ell-h)/2` in the notation of the statement

## Pass gates

- **A Honest taxonomy: PASS.** The requested invariant is the genus change of a degenerating family of algebraic curves; Algebraic geometry is primary.
- **B Natural statement: PASS.** Collision of branch points and genus drop are intrinsic questions about the displayed family. No tuned constants or auxiliary relations were inserted.
- **C Forward provenance: PASS.** `d`, `ell`, and `h` are canonical arithmetic invariants. Generic Kummer inertia is forced by the branch valuations. At `lambda=1`, the common radical is derived from `gcd(ell/m,ell/n)=1` via Bezout; it is not guessed to cancel terms.
- **D Difficulty architecture: PASS.** The chain is generic degree/inertia -> generic genus -> detect degree collapse at collision -> reconstruct the common radical -> special inertia/genus -> subtract. Multiple load-bearing nodes remain after the Kummer gateway.
- **E Ground truth: PASS.** Generic and collision degrees, all inertia orders, both Riemann-Hurwitz calculations, and the subtraction were checked for all parity/gcd regimes.
- **F Reviewer completeness: PASS.** The generic degree `mn` is justified by explicit valuation divisibility; the collision degree `ell` is proved by Bezout reconstruction and a valuation; ramification contributions are instantiated explicitly.
- **G Solver evidence: PENDING.** This revised statement blob is intentionally unmeasured until the ready marker is published.
- **H Portal format: PASS.** Consecutive Steps, three Solution Concepts, matching Symbolic derivation / Exact symbolic expression metadata, and standalone answer below the 100-character gate.
- **I Originality: PASS.** Repository searches on `main` found no matching Kummer genus-drop / branch-collision skeleton.

## Final quality-redesign preflight

- visible object has independent interest: PASS;
- decisive helpers have forward provenance: PASS;
- no guessed/tuned/backsolved object: PASS;
- compression test: PASS;
- at least two reasoning nodes remain after the main representation is recognized: PASS;
- hardening adds degeneration/normalization depth rather than concealment: PASS;
- reviewer-quote simulation: no unanswered reverse-engineering concern.

Verdict: solver-eligible as the one allowed same-blueprint structural revision.
