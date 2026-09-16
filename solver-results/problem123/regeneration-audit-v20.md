# problem123 regeneration audit v20

## Corrected local verdict for the exact probability candidate

Exact statement blob `c6d8a37df48d6f937fb39ab0440d685c1d21cada` received the intended single GPT-5.5 Medium run in `solver-results/problem123/c6d8a37df48d.json`.

Correct difficulty verdict: `TRUE_STUMP`.

Route audit:

- **COMMON ENTRY:** Bernoulli de Finetti representation and conversion to a linear-fractional moment problem.
- **COMMON REDUCTION:** the solver guessed a three-atom support family, derived a one-parameter ratio, differentiated it, and recovered the correct numerical optimum `E≈0.508704693012965`.
- **FIRST DECISIVE RECOGNITION:** the optimizer should lie on a structured finite-support moment law and can be parameterized algebraically.
- **LOAD-BEARING NODES RECOVERED:** de Finetti, moment constraints, a candidate support family, a stationary parameter equation, and algebraic elimination machinery.
- **MISSING LOAD-BEARING NODE:** a proof that the chosen support family is globally optimal among all admissible mixing laws. The response simply states that the extremal problem reduces to two interior atoms plus the endpoint `1`; it does not derive this and gives no global moment-dual certificate.
- **RECOVERY PATH:** structural. The missing step requires constructing the ratio-dependent cubic dual polynomial, proving its slack is nonnegative on `[0,1]`, and using complementary contact to certify the global upper bound.
- **REPAIR RADIUS:** `STRUCTURAL`.
- **FINAL-ALGEBRA NOTE:** the displayed final polynomial is also wrong by a local scale substitution: it is `16 Q(T/2)` rather than the correct `Q(T)`. This local error is not the reason for the stump classification; the missing global certificate is.
- **CANONICAL COLLAPSE:** no.

## Strong-model adversarial audit

Verdict: `STRONG_AUDIT_PASS`.

1. **Earliest natural entry:** de Finetti is standard and immediate, but it only converts the problem to an extremal ratio over probability measures with three fixed moments.
2. **No theorem-collapse:** generic finite-moment extremal results bound support size but do not identify the exact support `{a,b,1}`, determine its parameter, or prove this support globally maximizes the nonlinear ratio.
3. **Substantial dependencies after the gateway:** construct a feasible three-atom family; compute the primal ratio; build a ratio-dependent cubic majorant; force contact/degree cancellation; prove slack positivity; match primal and dual values; eliminate the support parameter; prove irreducibility.
4. **The local miss is structural rather than execution noise:** its unsupported sentence asserting the extremal support is exactly the point that the dual certificate is needed to justify.
5. **Difficulty is not concealment:** the conditional probability naturally creates a linear-fractional moment problem. The dual certificate arises from the optimization structure, not from hidden notation or tuned constants.
6. **Gate D:** passes. Direction discovery, certificate construction, interaction of primal and dual objects, serial dependence, and global closure all remain after the de Finetti gateway.

## Candidate quality

- The exchangeable Bernoulli model and posterior predictive target are standard probabilistic objects.
- The conditioning denominator is intrinsic.
- The primal support parameterization follows from the prescribed first three moments.
- The dual slack is forced by contact and degree constraints.
- Global optimality is certified analytically, not by numerical sampling.
- The subresultant chain is exact cleanup after the main structural certificate.
- No `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER` issue is present.

Quality verdict: `PASS`.

## Taxonomy

Snapshot date: `2026-09-16`.

- Domain: `Probability and Statistics`
- Sub-domain: `Probability foundations`
- Status: open in the current snapshot.
- Problem Type: `Optimization`
- Answer Type: `Polynomial or rational function`

## Exact promotion pair

- `problem.md` blob: `c6d8a37df48d6f937fb39ab0440d685c1d21cada`
- `solution.md` blob: `81d3db26fd53207dc7078e23e786ac46ffae8d5d`

The exact pair previously passed the prompt, answer, solution-length, concepts, structure, and classification gates. The statement has qualifying local `TRUE_STUMP` evidence and `STRONG_AUDIT_PASS`, with no contrary matching external evaluator evidence in the current conversation.

The later Bifurcation-theory draft was created only after the local result was initially over-classified as a conceptual solve. It was never exposed through `candidate-ready.json` and has no solver evidence. Abandon that draft and restore this exact measured pair for promotion.
