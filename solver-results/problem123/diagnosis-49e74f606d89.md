# Solver diagnosis — problem123 — 49e74f606d89

The exact ready blob `49e74f606d8911252fed6ae4e278f4f96106385c` was solved correctly by GPT-5.5 Medium in one intended run. The solver's final formula is algebraically identical to the reference formula.

- **COMMON ENTRY:** Recognize the fixed first three moments as making expectations of all cubic polynomials invariant across admissible laws.
- **COMMON REDUCTION:** Replace the moment optimization by one-sided cubic interpolation bounds for `h_t(x)=1/(1+t x)`.
- **FIRST DECISIVE RECOGNITION:** Use the sign of `h_t^{(4)}` and Hermite remainder formulas to identify the two-double-interior-node lower certificate and the endpoint/double-midpoint upper certificate.
- **RECOVERY PATH:** Recover the two discrete extremal laws from the moment equations, evaluate the resolvent on them, and subtract.
- **EARLIEST ROBUST SHORTCUT:** Classical Gaussian/Radau quadrature logic for a 4-convex function immediately supplies the same extremal support patterns; direct Hermite interpolation then proves sharpness with little additional search.

## Hardening decision

A same-blueprint revision was considered and rejected before editing. Natural-looking changes such as excluding the current contact nodes, adding another moment, or asking for another completely monotone/4-convex test function preserve the same quadrature skeleton and merely add degree/bookkeeping. Nonlinear functionals such as a variance or ratio would change the mathematical problem substantially but do not currently admit a compact, independently audited exact formula without introducing tuned side conditions. Therefore no quality-safe hardening-by-depth proposal is being used. This blueprint is retired after v1 and the workflow regenerates a structurally different candidate.
