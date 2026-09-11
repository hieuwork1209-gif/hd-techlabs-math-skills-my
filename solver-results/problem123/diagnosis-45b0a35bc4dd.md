# Difficulty diagnosis — blob 45b0a35bc4dd

- **COMMON ENTRY:** Compress each categorical sample to its multinomial count vector and regard the visible coarsenings as regular Bayesian multinomial experiments.
- **COMMON REDUCTION:** Apply the standard asymptotic mutual-information/Laplace formula separately to the X experiment, the Y experiment, and their joint experiment, then combine them by conditional independence.
- **FIRST DECISIVE RECOGNITION:** The X and Y marginals are 2-dimensional Dirichlet-aggregated multinomial models while the joint experiment is 3-dimensional, so the whole limit can be recovered from prior entropies and Fisher-information determinants without discovering the intended shared-mass/residual-composition split.
- **RECOVERY PATH:** Aggregate the Dirichlet law for each marginal, compute the two marginal Fisher determinants and the joint Fisher determinant, substitute the corresponding entropy/log-determinant expectations, and simplify digamma constants.
- **EARLIEST ROBUST SHORTCUT:** A generic regular Bayesian experiment expansion sees through the layered construction immediately; it bypasses the bespoke Dirichlet reparameterization and residual-dependence limit entirely.

**Verdict:** `DIFFICULTY_FAIL`. This was the single allowed structural revision of the blueprint and it was also solved correctly on its first cold measurement. Retire this blueprint; do not add another layer, extra category, tuned coefficient, or further notation.
