# Natural Difficulty Design Patterns

Use these as mechanism families, not templates to copy literally.

## Preferred structural levers

### Hidden representation

The visible formulation is awkward until the solver discovers a more natural representation: quotient, dual object, generating object, spectral coordinates, invariant factor, martingale, normal form, or certificate.

Good difficulty: discovering why the representation is necessary.
Bad difficulty: hiding an obvious substitution behind notation.

### Local-global compatibility

Local pieces are individually easy, but the requested object exists or is unique only when they satisfy a global compatibility constraint. The hard step is constructing/proving the compatibility condition.

### Competing regimes

Two natural mechanisms control different parameter ranges or structural cases, and the solver must identify where the transition occurs and prove closure across it.

Avoid arbitrary case splits; the regimes should arise from the mathematics.

### Leading-order degeneracy

A standard first-order route naturally loses information because of symmetry/degeneracy, forcing a second genuine idea. The degeneracy must be intrinsic, not engineered by tuned cancellation coefficients.

### Inverse reconstruction

A forward object is easy to compute, but the requested answer requires reconstructing hidden data and proving the reconstruction is unique.

### Extremal certificate

Finding a candidate is not enough. The solver must build a sharp certificate: dual witness, equality characterization, obstruction, gap argument, exchange argument, or attainment proof.

### Coupled invariants

One invariant narrows possibilities but does not determine the answer. A second invariant interacts with it in a nontrivial way. Avoid merely listing many independent congruences/conditions.

## Good source families by broad area

These are prompts for invention, not prescriptions.

- Algebra/number theory: local-to-global obstruction, valuation interaction, module/ideal normal form, congruence plus uniqueness certificate.
- Analysis: extremal function plus equality case, implicit parameter plus monotonicity/compactness, singular/regular regime interaction.
- Probability: conditioning changes a natural decomposition, stopping/coupling certificate, dependence functional requiring latent-variable reconstruction.
- Combinatorics: invariant plus reconstruction, generating object with non-obvious coefficient constraint, extremal structure plus exchange proof.
- Geometry/topology: incidence/duality obstruction, configuration invariant, local data constrained by global topology.
- Linear algebra: spectral/invariant-subspace structure where the matrix computation is a consequence, not the main source of difficulty.

## Blueprint anti-patterns

Retire the blueprint instead of hardening further when you see:

- “increase `n`, degree, dimension, or matrix size” as the main difficulty move;
- three or more nested helper definitions whose only purpose is to hide the same calculation;
- specially chosen constants justified only because they cancel earlier terms;
- a target coefficient pushed farther out by finite-difference/alternating sums;
- a giant determinant whose conceptual reduction is obvious once recognized;
- a named theorem directly matching the statement;
- many parallel cases instead of a serial unlock chain;
- a short final answer that can be guessed from symmetry or a tiny set of possibilities;
- a proof whose hard part is primarily arithmetic expansion.

## One-revision rule

If GPT-5.5 Medium solves the first clean blob, allow one same-blueprint revision only when the revision can be summarized as:

> “The original shortcut fails because the revised problem introduces this new natural mathematical dependency: ___.”

If that blank cannot be filled without talking about extra notation, coefficients, indices, or cancellation, regenerate a different blueprint.

If GPT-5.5 solves the revised blob too, retire the blueprint. Repeated solver success is evidence that the conceptual skeleton is too transparent, not a request to keep piling machinery onto it.
