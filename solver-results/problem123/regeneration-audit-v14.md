# problem123 regeneration audit v14

## Trigger

The prior moment-curve simplex statement is retired. The supplied independent evaluator report solved the matching statement repeatedly by the same route: move vertices to the curve, use a Vandermonde determinant, force the endpoints, then finish by symmetry/log-concavity or the equivalent Fekete/Gauss-Lobatto calculation. The local GPT-5.5 trace also recovered that full architecture and only made a local arithmetic simplification error. Verdict on the retired blob: `BLUEPRINT_TRANSPARENT` and `CONCEPTUAL_SOLVE_EXECUTION_ERROR`.

## Taxonomy freshness

Snapshot checked: 2026-09-16. `Topology and Geometry -> Convex geometry` is no longer listed as open. `Probability and Statistics -> Experimental design and causal inference` is open.

DOMAIN CHANGE: Topology and Geometry -> Convex geometry  =>  Probability and Statistics -> Experimental design and causal inference

## Blueprint triage

Three structurally different directions were preflighted.

1. **Selected — constrained D-optimal polynomial design.** Natural object: a polynomial-regression information matrix for a probability design with a prescribed mean. Gateway: log-determinant duality. Post-gateway nodes: saturated KKT equations, node-polynomial divisibility, exact feasibility from a logarithmic derivative, sensitivity contact multiplicities, and a global affine majorant certificate. Closure: the certificate applies to all Borel probability measures, not merely finite designs, and the exact determinant is recovered from the cubic discriminant and Vandermonde factorization.
2. **Harmonic-analysis survivor — constrained Toeplitz determinant from a circle measure.** Natural and potentially deep through positive trigonometric polynomials and spectral factorization, but more likely to collapse to a named OPUC/Fejer-Riesz theorem for a strong solver, so it was not selected.
3. **Optimal-control survivor — fixed-budget terminal determinant with bang-bang control.** Natural and serial, but the exact answer required more switching-case bookkeeping and had a higher risk of becoming a long mechanical verification, so it was not selected.

The selected design was preferred because its statement is shorter and more standard than either alternative while still leaving multiple load-bearing nodes after the initial convexity gateway.

## Quality-redesign preflight on the exact candidate

- **Independent interest:** PASS. Maximizing determinant of a regression information matrix under an allocation-moment constraint is a standard exact optimal-design question.
- **Compression test:** PASS. Naming the object as D-optimal design does not remove the hard part; the constrained support, weights, and global certificate still have to be constructed.
- **Forward provenance:** PASS. The reciprocal-affine weights come from weight KKT equations; the node polynomial comes from the node KKT equations; its coefficients come from explicit divisibility/remainder equations; the sensitivity polynomial is the intrinsic derivative of log determinant; contact multiplicities come from complementary stationarity.
- **No tuned cancellation:** PASS. No coefficient is inserted in the prompt to force a later cancellation. The only numerical datum, the mean $1/3$, is the experimental allocation constraint; all polynomial coefficients in the solution are derived from stationarity.
- **Post-gateway depth:** PASS. After log-det concavity, the solve still requires candidate construction, exact feasibility, global sensitivity majorization, and determinant evaluation.
- **Reviewer-quote simulation:** PASS after strengthening Step 2. The exact KKT remainder equations and the elimination factor selecting the admissible branch are displayed before the cubic is introduced.

## Pass gates A-F and I-K pre-ready audit

- **A Honest taxonomy:** PASS. Primary object is an experimental-design information matrix. Convex optimization is explicitly secondary.
- **B Natural statement:** PASS. One probability measure, one moment constraint, one standard information matrix, one determinant objective.
- **C Forward provenance:** PASS as recorded above.
- **D Difficulty architecture:** PASS pre-solver. Direction discovery, problem-specific KKT construction, interaction of determinant geometry with a dual polynomial, serial dependence, and global closure are all present.
- **E Ground truth:** PASS. Feasibility, positivity, root location, global optimality over all Borel measures, and exact determinant are established.
- **F Reviewer completeness:** PASS. The global certificate is derived from Lagrange cardinal polynomials and contact multiplicities rather than asserted from a named equivalence theorem.
- **I Portal/repository shape:** PASS by manual exact-pair audit against current hard-gate constants: concise prompt, exact scalar answer, five consecutive steps, five concepts, matching boxed/standalone answer, and no solution-local alias in the answer.
- **J Originality/corpus distance:** PASS. Repository search found no matching information-matrix/Borel-measure statement, and this is not a dimension/constant variant of the retired moment-curve problem.
- **K Human-verifiable answer:** PASS after changing the final object to the factorized form $2^4/(3^5 5^5 7^7)$.

## Difficulty status

Fresh statement: unmeasured. Prior solver/evaluator evidence does not transfer across this statement change. Publish an exact candidate-ready marker only after resolving current problem/solution blob SHAs, then stop at `REGENERATED_WAIT_CODEX` for the one allowed GPT-5.5 Medium cold solve.
