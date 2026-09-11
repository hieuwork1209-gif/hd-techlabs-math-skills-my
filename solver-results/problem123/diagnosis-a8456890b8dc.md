# Difficulty diagnosis — problem123 / a8456890b8dc

- **COMMON ENTRY:** recognize the semiconjugacy `x=z+z^{-1}`, so `f^{\circ m}(x)` becomes `z^{2^m}+z^{-2^m}`.
- **COMMON REDUCTION:** rewrite the forward target as `\ell^{2^q}+\ell^{-2^q}` and read the roots as a radical times `2^n`-th roots of unity.
- **FIRST DECISIVE RECOGNITION:** the forward depth merely cancels `min(n,q)` layers of the Kummer tower, leaving radical depth `d=max(n-q,0)` while the full cyclotomic layer remains.
- **RECOVERY PATH:** identify the splitting field as `Q(\ell^{1/2^d},\zeta_{2^n})`, separate radical and cyclotomic parts by ramification, then read the faithful affine action on the roots.
- **EARLIEST ROBUST SHORTCUT:** once the semiconjugacy is recognized, the revised `q`-dependence is visible immediately as a change of radical exponent; the rest is a standard Kummer-cyclotomic semidirect-product calculation.

**Decision:** `DIFFICULTY_FAIL`. This was the one permitted structural revision of the Galois blueprint and it was solved correctly on its first cold measurement. Retire the blueprint; do not add another orbit depth, prime, or cyclotomic layer.
