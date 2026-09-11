# Regeneration audit v7 — problem123

## Selection

- **Domain/Sub-domain:** Probability and Statistics -> Stochastic processes.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists Stochastic processes with 6 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Natural object:** the inverse scaling law for first hitting times in a two-color reinforced urn whose red population is sublinear.
- **Hidden gateway:** normalize the red count by the exact multiplicative drift and then discover that rising factorials diagonalize all conditional moment recurrences.
- **Serial nodes:** (1) deterministic total and one-dimensional transition; (2) nonnegative martingale normalization and a.s. `sqrt(n)` limit; (3) exact rising-factorial moments; (4) identify the limit as `|N(0,2)|` with moment uniqueness; (5) invert the deterministic-time asymptotic along `tau_m`; (6) evaluate the Laplace transform of the squared limit.
- **Closure certificate:** the identified limit is strictly positive a.s., forcing every level to be hit; the random-subsequence argument then proves the inverse hitting-time limit, and bounded convergence closes the expectation limit.
- **Final answer:** `\frac1{\sqrt{1+4t}}`; stripped Final Answer length including `\displaystyle` = 32 characters.

## Blueprint triage

Three fresh mechanism families were compared before authoring: a free-boundary calculus-of-variations problem, a homological-algebra Poincare-series problem, and this reinforced-urn inverse-hitting problem. The first two were rejected at blueprint stage because their decisive cores were too close to recognizable Euler-Lagrange/obstacle or fiber-product/resolution recipes. The selected urn blueprint keeps a single natural process and forces a bespoke bridge from multiplicative drift to moment identification to inverse stopping-time asymptotics.

## Shortcut analysis

A standard Polya-urn Beta-limit heuristic is false here because the replacement is triangular rather than diagonal: the red proportion tends to zero and the relevant scale is `sqrt(n)`. Solving only the mean recursion does not identify the random limit or the hitting-time law. Direct recurrences for `tau_m` create an unbounded state problem; the intended route instead discovers the deterministic-time martingale limit first and then inverts it.

Technique skeleton: `multiplicative-drift martingale -> rising-factorial moments -> moment-law identification -> inverse hitting-time limit`.
Workspace mechanism registry has no matching skeleton, and repository searches for `Polya urn`, `triangular urn hitting time`, and `urn martingale hitting time rising factorial` returned no matching problem on main.

## Triviality Probe

- **P1 State-space count:** no finite enumeration; the requested object is an `m -> infinity` hitting-time limit and the proof derives a symbolic process law valid for all levels. -> **PASS**
- **P2 Decoration-deletion:** initial red/blue counts -> Yes; red replacement rule -> Yes; blue replacement rule -> Yes; first hitting time -> Yes; `m^2` scaling -> Yes; free Laplace parameter `t` -> Yes. -> **PASS**
- **P3 Answer-triviality:** literal answer `1/sqrt(1+4t)` is a nonconstant symbolic function, not a zero/identity/empty/nonexistent object. -> **PASS**
- **P4 Core-reduces-to:** "Find the exact multiplicative martingale and the rising-factorial identity that identifies its random limit, then invert that limit at hitting times."; skeleton=`urn-martingale -> factorial-moments -> inverse-hitting`; workspace reuse=0. No single named recipe supplies the full chain. -> **PASS**
- **P5 Answer-recoverability:** finite simulation can approximate isolated values for chosen `t`, but cannot recover or certify the exact function for arbitrary real `t >= 0`, the `m^2` scaling, or the a.s. inversion. No finite search or numeric-recognition side channel determines the requested symbolic law. small-input/small-answer flag: free unbounded level `m` and free continuous parameter `t`; clear. -> **PASS**
- **P6 Route-Concession:** 6a no hidden auxiliary object is constructed in the statement; 6b the longest step (factorial-moment identification) is not conceded; 6c no compaction-forced helper definition. -> **PASS**
- **P7 Depth-vs-Breadth:** 7a six serial nodes; 7b at most two simultaneous process objects (`R_n`, then `tau_m` after the limit law is known); 7c deleting any of the six nodes breaks the route. -> **PASS**
- **P8 Terminology-density:** N=0 bespoke terms; max simultaneous primary definitions=2 (`R_n`, `tau_m`); all terminology (urn, hitting time, expectation) is standard stochastic-process vocabulary. -> **PASS**

## Reviewer completeness / correctness

- The deterministic total `2n+2` and exact transition law for `R_n` are derived directly from the replacement rules.
- The normalization `a_n` is shown explicitly to make `R_n/a_n` a nonnegative martingale; the gamma-product formula and the exact fixed-shift gamma-ratio asymptotic are displayed.
- For every integer moment, the conditional rising-factorial recurrence is expanded line by line and iterated exactly.
- Ordinary moment convergence is justified from the polynomial difference between rising factorials and powers; uniform integrability is obtained from the next moment.
- The half-normal moments are evaluated by an explicit integral and matched using the displayed gamma duplication identity.
- Moment uniqueness is not asserted vaguely: the exact Carleman condition is stated and verified using `m_{2j}=(2j)!/j!`.
- Positivity of the identified limit proves that every integer red level is reached a.s.; because red increments are only `0` or `1`, `R_{tau_m}=m` exactly.
- The deterministic-time a.s. limit is evaluated along the random subsequence `tau_m -> infinity`, yielding `m^2/tau_m -> W^2` a.s.; bounded convergence is applicable because the exponential is in `[0,1]`.
- The final Gaussian integral gives `1/sqrt(1+4t)` for every `t >= 0`.

## Promotion state

Fresh statement blob must receive exactly one GPT-5.5 Medium cold solve. No prior solver result applies to this regenerated statement.
