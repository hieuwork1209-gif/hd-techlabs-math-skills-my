# Solver diagnosis — problem123 — 8838ee73f40f

## COMMON ENTRY
Recognize the beta laws of the two uniform order statistics and the conditional beta scaling relations between them.

## COMMON REDUCTION
Turn the nonlinear-correlation supremum into the operator norm of conditional expectation from the centered L2 space of U_(r) to that of U_(s).

## FIRST DECISIVE RECOGNITION
The conditional beta formulas preserve polynomial degree in both directions, so monic orthogonal polynomials are immediately mapped degree-by-degree and become singular functions.

## RECOVERY PATH
Read off the forward and reverse leading coefficients from beta moments, multiply them to obtain the full T*T spectrum, then use its strict monotonicity to identify the centered top singular value.

## EARLIEST ROBUST SHORTCUT
Once the solver notices the invariant polynomial flags, the whole problem collapses to a standard Jacobi/orthogonal-polynomial singular-spectrum computation; the degree-one mode is then visibly dominant. The intended nonlinear extremal closure does not add a genuinely separate obstacle.

## QUALITY DECISION
Do not spend the optional same-blueprint revision on artificial constraints such as forbidding affine functions or asking for a later singular mode. Those would only suppress the solver's successful mode rather than add a natural mathematical dependency. Retire this blueprint after its first clean solve and regenerate.