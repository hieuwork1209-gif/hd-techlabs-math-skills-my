# Structural revision audit — problem123 — Algebraic geometry v2

## Why revision is allowed

The first Algebraic-geometry statement blob `8a7dcbf3f64bc3965d1a57990de8c280b5cc3abe` was solved correctly by GPT-5.5 Medium in one run. The robust shortcut was:

`first characteristic cancellation -> three-generator value semigroup -> rectangular Apéry set -> genus formula`.

This file audits the one and only same-blueprint structural revision permitted after that result.

## Revision mechanism

The parametrized branch itself is unchanged. The target is now the first nonzero term of the discriminant of the finite projection `x=t^m`.

The solver's original shortcut fails because the revised problem introduces the natural dependency **exact leading-unit data of the branch discriminant**, which arises from the canonical conjugate branches of the finite map and forces the additional reasoning step **classify conjugate differences by root-of-unity stabilizer, evaluate the resulting products, and track the global discriminant sign**. Value-semigroup/gap data can recover the discriminant valuation but not this exact leading coefficient.

## Forward-provenance audit

- Conjugates `t -> alpha t`, `alpha^m=1`: `STANDARD_NATURAL_REPRESENTATION`, forced by the visible finite projection `x=t^m`.
- Roots `y_alpha=alpha^n t^n+alpha^p t^p`: `FORCED_BY_EQUATIONS`, obtained by applying those automorphisms to the visible parametrization.
- The two strata `xi^n != 1` and `xi^n=1`: `FORCED_BY_EQUATIONS`, obtained directly from the first nonzero term of `y_alpha-y_{alpha xi}`.
- Products over `mu_m` and `mu_d`: `CANONICAL`, since they are exactly the leading coefficients in the derivative product for the discriminant.
- No correction term, coefficient, relation, or auxiliary object is guessed to cancel or fitted to the final answer.

No `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER` ingredient occurs.

## Compression / reviewer-quote simulation

Writing the minimal polynomial explicitly would make the statement longer, not conceptually cleaner. The parametrization plus its monic minimal polynomial is the standard geometric description of the finite branch projection. Revealing the conjugate roots in the statement would concede the main derivation, but even after the conjugates are found the solver must still classify stabilizers, compute two nontrivial root-of-unity products, multiply all conjugates, and track the discriminant sign. Thus the difficulty survives the gateway and is not concealment.

The reviewer objections "specific corrections were chosen to cancel", "invariants were introduced only after the fact", and "statement engineered from the intended cancellation" do not apply: every decisive object is generated canonically by the projection and the discriminant identity.

## Pass gates

- **A Honest taxonomy:** PASS. The object is the discriminant of a finite projection of an irreducible plane-curve germ; Algebraic geometry is primary.
- **B Natural statement:** PASS. Leading discriminant term is a standard invariant of a ramified finite map; `m,n,p,d` all affect ramification strata or coefficient.
- **C Forward provenance:** PASS as recorded above.
- **D Difficulty architecture:** PASS. Serial nodes are: prove degree/exhaustive conjugates; instantiate discriminant derivative product; stratify conjugate differences; evaluate root products; assemble sign and convert from `t` to `X`.
- **E Ground truth:** PASS. The solution proves irreducibility/degree, all conjugates, nonzero leading products, exact exponent, exact coefficient, and sign over the full stated range.
- **F Reviewer completeness:** PASS. The discriminant identity is derived from pair factors; kernel/image sizes are identified; both root-of-unity products are evaluated explicitly; the `t^m=X` conversion and next-order claim are justified.
- **G Solver evidence:** PENDING for revised blob. Previous evidence applies only to `8a7dcbf3...` and is not reused.
- **H Portal format:** PASS. Symbolic derivation / exact symbolic expression; four consecutive steps; three Solution Concepts; standalone answer stripped of `$`/whitespace has 69 characters.
- **I Originality:** PASS. Repository searches for `discriminant plane branch t^m t^n+t^p` and `root-of-unity discriminant minimal polynomial parametrized branch` returned no matching main-corpus problem.

## Independent checks

Direct resultant/discriminant computations on sample triples `(2,4,5)`, `(4,6,7)`, and `(6,9,10)` agree with the derived exponent, magnitude, and sign.

## Revision budget

This is the single structural revision for the Algebraic-geometry plane-branch blueprint. If GPT-5.5 Medium solves the revised exact statement correctly, retire this blueprint and regenerate; do not harden it again.
