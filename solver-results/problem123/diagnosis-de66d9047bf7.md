# Solver diagnosis — problem123 de66d9047bf7

- Exact problem blob: `de66d9047bf7904f317e5b0055ae59ad7ee43b7b`
- Exact solution blob: `1e277cccfb8a04c3ad1a6d2b068d9b768dc913ef`
- Solver: GPT-5.5, Medium, one run, 2100-second timeout budget
- Result status: success
- Local verdict: `LOCAL_STUMPED`

## Mathematical comparison

The solver obtained the same final genus-drop formula as the reference and correctly computed the generic-fiber ramification. However, in the collision fiber it asserted

`C(x)(y,z)=C(x)(u), u^ell=x(x-1)`

without constructing `u` or proving the field equality / degree collapse from `mn` to `ell`. This is the load-bearing dependency introduced by the structural revision, not a cosmetic proof detail. The exact reference solution derives it by setting `a=ell/m`, `b=ell/n`, choosing Bezout coefficients `r,s` with `ar+bs=1`, taking `u=y^r z^s`, proving `u^ell=x(x-1)`, and then proving conversely that `y/u^a` and `z/u^b` are constant roots of unity. It then establishes `[C(x)(u):C(x)]=ell` by valuation.

Therefore the solver answer is materially incomplete despite the correct final expression.

## Shortcut diagnosis

- COMMON ENTRY: Treat both equations as Kummer covers and use Riemann-Hurwitz.
- COMMON REDUCTION: Read ramification from valuation vectors at `0,1,lambda,infinity`.
- FIRST DECISIVE RECOGNITION: At `lambda=1` the two radicals share the same radicand, so the generic degree-`mn` argument no longer applies.
- RECOVERY PATH: Construct the common `ell`-th radical via Bezout, prove the exact collision field and degree, compute special-fiber inertia, then subtract genera.
- EARLIEST ROBUST SHORTCUT: The solver could state the expected single Kummer cover at the collision without proving the field reconstruction; that skipped the revised problem's decisive dependency.

No further hardening is permitted or needed. Promotion gates are evaluated on the exact reference pair, not on the incomplete solver exposition.
