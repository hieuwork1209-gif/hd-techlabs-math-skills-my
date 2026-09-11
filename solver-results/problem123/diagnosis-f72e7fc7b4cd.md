# Difficulty diagnosis — problem123 blob f72e7fc7b4cd

- **COMMON ENTRY:** Pass to the conjugates of the parametrization under the canonical action `t -> zeta t`, `zeta^m=1`.
- **COMMON REDUCTION:** Write the discriminant as the squared product of pairwise conjugate differences and split pairs according to whether their `n`th powers agree.
- **FIRST DECISIVE RECOGNITION:** The map `mu_m -> mu_{m/d}`, `zeta -> zeta^n`, has fibers of size `d`; this forces exactly two leading contact orders, `n` across distinct fibers and `p` inside a fiber.
- **RECOVERY PATH:** Count both pair strata, evaluate the corresponding root-of-unity/Vandermonde products, track the phase/sign, then convert the total `t`-order to the `X=t^m` exponent.
- **EARLIEST ROBUST SHORTCUT:** Once the conjugates are written down, the entire problem becomes a direct root-of-unity stratification of the discriminant; the exact leading unit follows from standard cyclotomic product identities. The added discriminant target therefore did not create enough post-gateway difficulty.

The solver's coefficient `(-1)^S d^m q^{md}` with `q=m/d` is mathematically equivalent to the reference coefficient `(-1)^{m(m-1)/2+(m+1)D}((m/d)^d d)^m`; the sign exponents agree modulo `2` under the stated hypotheses.

**Verdict:** `DIFFICULTY_FAIL`. This was the one permitted structural revision of the Algebraic Geometry blueprint, so the blueprint is retired and must not be hardened again.
