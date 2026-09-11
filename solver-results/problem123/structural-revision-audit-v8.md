# Structural revision audit v8 — problem123

## Revision status

This is the **single allowed same-blueprint structural revision** after GPT-5.5 Medium solved blob `701fb1d717bd7975481997c0f9d8d28a500a4878` correctly. If this revised clean statement is also solved correctly, the reinforced-urn blueprint must be retired rather than hardened again.

The original shortcut fails because the revised problem introduces this new natural mathematical dependency:

> the next-level hitting-time spacing must be analyzed conditionally on the random macroscopic clock `tau_m`, and that local hazard law must be coupled with the global `m^2/tau_m` limit to obtain the joint transform.

This changes the dependency graph. It is not a tuned constant, extra color, extra state index, cancellation device, or longer version of the old calculation.

## Selection

- **Domain/Sub-domain:** Probability and Statistics -> Stochastic processes.
- **Current slot evidence:** the 2026-09-11 taxonomy snapshot lists Stochastic processes with 6 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Natural object:** the joint asymptotic law of a first hitting time and the relative spacing to the next level in a triangular reinforced urn.
- **Hidden gateway:** first identify the global `sqrt(n)` red-count limit, then realize that the next waiting time must be rescaled by the random clock `tau_m` and analyzed through its conditional product hazard.
- **Serial nodes:** (1) scalar red-count transition; (2) martingale normalization and almost-sure `sqrt(n)` limit; (3) rising-factorial moments and half-normal identification; (4) inversion at `tau_m`; (5) conditional product-hazard asymptotic for `tau_{m+1}-tau_m`; (6) uniform clock-window control giving asymptotic independence and the joint Laplace transform.
- **Closure certificate:** positivity of the global limit guarantees all levels are hit; uniform conditional spacing convergence on compact clock windows plus tightness of `tau_m/m^2` upgrades the local limit to the required joint expectation limit.
- **Final answer:** `\frac1{(1+2u)\sqrt{1+4t}}`.
- **Portal stripped Final Answer length including `\displaystyle`:** 41 characters.

## Difficulty architecture

The old one-dimensional shortcut `factorial moments -> weak limit -> monotone inverse event` still determines the marginal `m^2/tau_m`, but it does not determine the new spacing term. The solver must additionally derive the exact conditional survival product

`prod_j (1 - m/(2(n+j)+2))`

at the random time `tau_m=n`, find the non-obvious scale `m(tau_{m+1}/tau_m-1)`, prove its conditional exponential limit uniformly when `n` is of order `m^2`, and then couple this with the global limit. The cancellation of the random clock in the local limit is structural and produces asymptotic independence; it is not encoded in the statement.

Technique skeleton:

`urn martingale -> factorial-moment law -> hitting-time inversion -> random-clock hazard -> uniform conditional limit -> joint transform`.

Repository searches on `main` for `tau_{m+1} hitting time urn` and `successive hitting times reinforced urn` returned no matching problem.

## Triviality Probe

- **P1 State-space count:** no finite enumeration; both hitting levels and the random clock diverge. -> **PASS**
- **P2 Decoration-deletion:** initial composition, both replacement rules, first hitting times, `m^2/tau_m`, relative successive spacing, and the two Laplace variables all affect the limiting law. -> **PASS**
- **P3 Answer-triviality:** the result is a nonconstant two-parameter transform, not a zero/identity/degenerate object. -> **PASS**
- **P4 Core-reduces-to:** no single named theorem produces both the half-normal global limit and the conditional random-clock spacing law. -> **PASS**
- **P5 Answer-recoverability:** finite simulation at fixed `(t,u)` cannot certify the exact two-parameter formula or the asymptotic independence mechanism. -> **PASS**
- **P6 Route-Concession:** the statement does not name the martingale, rising-factorial identity, conditional product hazard, exponential spacing law, or independence conclusion. -> **PASS**
- **P7 Depth-vs-Breadth:** six serial nodes; the new node is genuinely downstream of `tau_m ~ m^2/W^2` and cannot be replaced by more bookkeeping. -> **PASS**
- **P8 Terminology-density:** no bespoke terminology; only the urn, red count, and hitting times are primary objects. -> **PASS**

## Reviewer completeness / correctness

- The total population and one-step red transition are derived explicitly.
- The martingale normalization is displayed and its gamma-product asymptotic is justified by the stated fixed-shift gamma ratio.
- Rising-factorial moments are derived from the exact one-step identity and iterated; conversion to ordinary moments and uniform integrability are justified.
- The half-normal moment match uses the displayed gamma duplication identity; moment uniqueness is verified through the explicit Carleman series.
- Positivity of the almost-sure scaling limit proves every integer level is hit, and the random-subsequence inversion gives `m^2/tau_m -> W^2` almost surely.
- Conditional on `tau_m=n`, the survival probability of the next-level waiting time is written exactly as a product. The proof controls both the first-order hazard sum and the quadratic log-error uniformly for `n/m^2` in a compact interval.
- Uniform conditional survival convergence is converted to uniform Laplace convergence with the exact tail-integral identity; the exponentially weighted tail is controlled before sending the compact cutoff to infinity.
- Tightness of `tau_m/m^2` away from zero and infinity follows from its almost-sure convergence to `1/W^2`; this transfers the conditional limit from deterministic clock windows to the random clock.
- Boundedness of the conditional Laplace transforms upgrades convergence in probability to `L^1`, justifying the factorization step in the joint expectation.
- The final Gaussian square transform is `1/sqrt(1+4t)`, while the local spacing transform is `1/(1+2u)`, giving the exact product.

## Sanity check

A non-proof numerical check of the exact conditional waiting-time product at `n=m^2`, `u=0.7` gave conditional Laplace values `0.40237`, `0.41093`, `0.41379` for `m=20,50,100`, respectively, converging toward the predicted `1/(1+2u)=0.41667`.

## Promotion state

The revised statement must receive exactly one fresh GPT-5.5 Medium cold solve. The previous result for blob `701fb1d...` is stale for difficulty evaluation of this revised blob. No further same-blueprint revision is allowed if the revised blob is solved correctly.
