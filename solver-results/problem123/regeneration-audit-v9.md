# Regeneration audit v9 — problem123

## Previous blueprint retirement

The Algebraic Geometry statement blob `8a7dcbf3f64b...` and its one permitted structural revision `f72e7fc7b4cd...` were both solved correctly by GPT-5.5 Medium. The revised discriminant problem was solved through the exact conjugate/root-of-unity stratification intended by the reference. The Algebraic Geometry blueprint is therefore retired and is not being hardened again.

## Blueprint triage

Fresh mechanisms were compared before authoring.

1. **Joint distributions and dependence — nonlinear correlation of two order statistics.** Natural object: the strongest possible correlation after arbitrary square-integrable transforms. Gateway: the variational definition canonically becomes a conditional-expectation operator norm. Visible trigger after that gateway: the two conditional order-statistic laws are affine Beta scalings, forcing invariant polynomial flags. Post-gateway work: derive the two conditional laws, build the adjoint pair, orthogonalize the invariant flags, compute the complete singular spectrum, prove its strict monotonicity, and close attainment. **Selected.**
2. **Eigenvalues and eigenvectors — periodic Jacobi matrix with a boundary defect.** Natural and quality-safe, with Floquet reduction followed by a bound-state matching condition and regime closure, but the decisive route is closer to a standard transfer-matrix recipe and was judged easier for the target solver. **Survived preflight but not selected.**
3. **Module theory — Jordan structure of multiplication by a linear form in a truncated complete intersection.** Rejected because the strongest route is essentially recognition of the standard Lefschetz/`sl_2` structure; too much of the difficulty would be theorem recognition.
4. **Riemannian geometry — first conjugate time on a homogeneous three-manifold.** Rejected because a clean self-contained version either exposes the standard Jacobi-field reduction or becomes coordinate-heavy; the latter would add computation rather than reasoning depth.

At least two quality-safe choices survived; the order-statistics problem was selected for its stronger closure requirement.

## Exact selected pair

- **Problem path:** `workspace/rainier-problem/problem123-joint-distributions-and-dependence/problem.md`
- **Problem blob:** `8838ee73f40f737e5a257efcab7cbc1ed30c70b7`
- **Solution path:** `workspace/rainier-problem/problem123-joint-distributions-and-dependence/solution.md`
- **Solution blob:** `46556e96d39c2a8771978aeecd0bc0160267413e`
- **Domain/Sub-domain:** Probability and Statistics -> Joint distributions and dependence.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists this sub-domain with 6 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** `sqrt(r(n+1-s)/(s(n+1-r)))`.
- **Standalone answer length:** 45 stripped characters including `\displaystyle`; below the 100-character gate.

## Difficulty architecture

Natural object: for two order statistics `X=U_(r)` and `Y=U_(s)`, determine the strongest dependence detectable by arbitrary centered unit-variance transforms.

Serial reasoning nodes:

1. derive the exact joint density and the two conditional Beta scaling laws;
2. convert the bilinear supremum into the norm of `T f=E[f(X)|Y]` on centered `L^2`;
3. observe from the affine Beta conditionals that `T` and `T*` preserve every polynomial-degree flag;
4. derive the canonical monic orthogonal bases and prove `T p_k=a_k q_k`, `T* q_k=b_k p_k`;
5. use completeness to diagonalize `T*T` on all of `L^2`, not merely on low-degree test functions;
6. prove the full eigenvalue sequence is strictly decreasing and close the supremum/attainment at degree one.

The obvious shortcut of computing the ordinary Pearson correlation only supplies a lower bound: it does not rule out nonlinear transforms with larger correlation. The load-bearing closure is the complete singular-spectrum argument proving that no nonlinear transform beats degree one.

## Forward-provenance / anti-reverse-engineering preflight

- **Conditional-expectation operator `T`: CANONICAL.** Triggered directly by the bilinear supremum `E[f(X)g(Y)]`; the adjoint formula follows from the tower property.
- **Polynomial flags: FORCED_BY_EQUATIONS.** Equations `X=YB` conditionally on `Y` and `Y=X+(1-X)C` conditionally on `X` show immediately that both conditional operators preserve polynomial degree.
- **Orthogonal polynomials `p_k,q_k`: CANONICAL.** Once the invariant flags and the self-adjoint operator `T*T` are visible, Gram-Schmidt gives the unique monic basis adapted to both the flag and each marginal inner product. They are not guessed to cancel terms.
- **Coefficients `a_k,b_k`: FORCED_BY_EQUATIONS.** They are the leading coefficients of the conditional images and equal explicit Beta moments; no coefficient is tuned.
- **Spectrum `lambda_k=a_k b_k`: FORCED_BY_EQUATIONS.** It follows from the two adjoint intertwining identities.

No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

Compression test: naming Jacobi polynomials explicitly would shorten some notation but would not remove the main mathematics. One must still derive both conditional operators, prove the intertwining coefficients, establish completeness, compare the entire nonconstant spectrum, and prove attainment. Difficulty therefore survives the clean representation.

Reviewer-quote simulation: the solution explicitly states why polynomial flags arise before introducing the orthogonal basis. There are no special corrections, custom relations, tuned constants, or hidden encodings.

## Promotion gates pre-solver

- **Gate A — honest taxonomy:** PASS. The requested object is a nonlinear dependence coefficient of a joint distribution; operator methods are auxiliary.
- **Gate B — natural statement:** PASS. Maximal nonlinear correlation of order statistics is independently meaningful; `n,r,s` all have intrinsic roles.
- **Gate C — forward provenance:** PASS as detailed above.
- **Gate D — difficulty architecture:** PASS. Direction discovery, tool construction, multiple serial ideas, and a global no-better-nonlinear-function certificate are all load-bearing.
- **Gate E — ground truth:** PASS. All Beta parameters are positive for `1<=r<s<=n`; conditional laws, operator spectrum, monotonicity, and attainment cover the full parameter range.
- **Gate F — reviewer completeness:** PASS. The joint density, Beta moments, conditional Jensen contraction, adjoint relation, invariant polynomial flags, completeness argument, diagonal expansion, and monotonicity ratio are all displayed explicitly.
- **Gate G — solver evidence:** PENDING. This exact problem blob is fresh and must receive exactly one GPT-5.5 Medium cold solve.
- **Gate H — portal format:** PASS. Five consecutive Steps, three Solution Concepts, exact Final Answer line, matching metadata, compact standalone answer.
- **Gate I — originality:** PASS. Repository searches for `maximal correlation order statistics Uniform` and `order statistic Beta conditional orthogonal polynomial correlation` found no matching corpus item on `main`.

## State

The exact normalized pair is quality-safe and ready for one cold solver measurement. Publish `candidate-ready.json` only after this audit, using the exact two blob SHAs above.
