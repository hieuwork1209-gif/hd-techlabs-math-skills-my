# Solver diagnosis — problem123 blob 72cfb8ab7be6

- **Verdict:** DIFFICULTY_FAIL (solver correct).
- **COMMON ENTRY:** Use the centered affine coordinate on the path as a Rayleigh test vector; its edge differences are all 1, so the unit edge-budget makes the numerator fixed.
- **COMMON REDUCTION:** The universal bound is `M=12/[n(n^2-1)]`; equality forces the affine vector to be a Fiedler eigenvector and hence forces `w_i=(M/2)i(n-i)` uniquely.
- **FIRST DECISIVE RECOGNITION:** For the forced quadratic profile, the remaining lower bound can be proved directly by a weighted discrete Poincare inequality rather than by computing the full spectrum.
- **RECOVERY PATH:** Express centered variance as the average of all pairwise squared differences, write each pairwise difference as a sum of edge increments, apply Cauchy, and evaluate the crossing-pair weight `sum_{a<=k<b}(b-a)=n k(n-k)/2`.
- **EARLIEST ROBUST SHORTCUT:** Once the affine certificate forces `i(n-i)`, the pairwise-difference identity produces exactly the needed `k(n-k)` Poincare weights and closes optimality in one inequality; the reference's orthogonal-polynomial spectral closure is unnecessary.

## Blueprint decision

The first clean weighted-path blob was solved correctly. Candidate revisions based on extra edge costs, caps, or secondary spectral outputs were rejected by proposal-level quality preflight: the clean exact versions either preserve the same affine-certificate skeleton or require coefficients/constraints chosen mainly to defeat the successful inequality. The convex weighted-path blueprint is therefore retired rather than hardened by concealment.
