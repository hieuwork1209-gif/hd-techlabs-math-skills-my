# Regeneration audit v8 — problem123

## Why regeneration was required

The revised stochastic-processes blob `d823bbed230f5a45a87bd91cfecb6e47aec10259` was solved correctly by GPT-5.5 Medium in one intended run. Its earliest robust shortcut was: once `tau_m` is known to be order `m^2`, conditioning on `tau_m=k` turns the successive spacing into a first-order hazard product and immediately gives an `Exp(1/2)` limit. That was the one permitted same-blueprint revision, so the reinforced-urn blueprint is retired.

## Blueprint triage

Three genuinely different families were considered before authoring:

1. **Topology and Geometry -> Algebraic geometry:** normalization defect of the two-characteristic-exponent plane branch `x=t^m`, `y=t^n+t^p`. Hidden gateway: the first common leading valuation forces the approximate root `y^(m/d)-x^(n/d)`. Post-gateway dependencies: valuation-adapted module basis, residue separation, exact value set, and gap-count closure. **Selected.**
2. **Linear Algebra -> Tensor and multilinear algebra:** kernel/Jordan data for the derivation induced by a single nilpotent Jordan block on an exterior power. This is natural and quality-safe, but the visible Jordan chain gives an unusually strong standard `sl_2` entry point, making the likely solver shortcut too direct. **Not selected.**
3. **Probability and Statistics -> Probability foundations:** a compact-support moment extremal problem closed by a dual polynomial certificate. Natural and quality-safe, but low-degree moment duality gives a short canonical majorant route and is weaker than the selected branch problem. **Not selected.**

At least two choices survive the quality screen; the algebraic-geometry candidate was selected on difficulty architecture rather than taxonomy capacity.

## Exact candidate

- **Problem path:** `workspace/rainier-problem/problem123-algebraic-geometry/problem.md`
- **Problem blob:** `8a7dcbf3f64bc3965d1a57990de8c280b5cc3abe`
- **Solution path:** `workspace/rainier-problem/problem123-algebraic-geometry/solution.md`
- **Solution blob:** `1ede2060913e6edcac63efea479158e4b111f2fa`
- **Domain/Sub-domain:** Topology and Geometry -> Algebraic geometry.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists Algebraic geometry with 2 remaining slots and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference answer:** `\frac{(m-d)n+(d-1)p-m+1}{2}`.
- **Stripped Final Answer length including `\displaystyle`:** 40 characters.

## Proposal-level anti-reverse-engineering preflight

- **Visible mathematical object:** the completed local ring of a parametrized irreducible plane-curve germ and its normalization defect; independently standard and meaningful.
- **Parameter provenance:** `d=gcd(m,n)>1` selects the genuine two-stage characteristic-exponent regime; `gcd(d,p)=1` is exactly the primitiveness condition that makes the normalization field `C((t))` and the defect finite. No parameter is chosen to cancel a target term.
- **Decisive auxiliary object:** `g=y^(m/d)-x^(n/d)`.
  - **Trigger:** `ord_t(x)=m` and `ord_t(y)=n` visibly have first common positive multiple `(m/d)n=(n/d)m`.
  - **Derivation:** subtract the two monomials whose leading orders first coincide.
  - **Canonicity:** the exponents are the least positive solution of `alpha n=beta m`; the leading coefficients are both 1, so the subtraction coefficient is forced.
  - **Classification:** `FORCED_BY_EQUATIONS`.
  - **Load-bearing role:** its new order `beta=(m/d-1)n+p` separates the residual `d` valuation classes and builds the final Apéry-type basis.
- **Valuation-adapted basis:** `y^i g^j` is derived from the canonical relation `y^(m/d)=x^(n/d)+g` and the unique decomposition of exponents modulo `m/d`; classification `CANONICAL`.
- **Value set / gap filtration:** standard natural invariants of a one-branch normalization problem; classification `STANDARD_NATURAL_REPRESENTATION`.
- No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

### Compression test

Naming the approximate root in the statement would remove one discovery step but would not make the rest routine: the solver would still need to prove the free module basis, establish pairwise residue separation, identify the exact value set, and convert it to normalization length. The difficulty therefore survives a cleaner representation and is not concealment-only.

### Reviewer-quote simulation

- “The correction was chosen exactly to cancel leading terms.” **Defeated:** the solution first derives the least positive valuation equality and only then defines the forced difference.
- “The invariant is introduced after the fact.” **Defeated:** valuation order is the intrinsic filtration governing the requested normalization quotient.
- “Once the hidden representation is recognized, the rest is routine.” **Not applicable:** three load-bearing proof nodes remain after the approximate root is found.
- “The statement appears engineered from the answer.” **No:** it is the simplest two-term Puiseux parametrization with a nontrivial gcd drop.

## Pass gates

- **Gate A — Honest taxonomy:** PASS. The requested invariant is the normalization defect/delta invariant of a plane branch; module and numerical-semigroup calculations are auxiliary.
- **Gate B — Natural statement:** PASS. One standard local ring, one intrinsic gcd regime, one standard normalization length.
- **Gate C — Forward provenance:** PASS as detailed above.
- **Gate D — Difficulty architecture:** PASS. Serial chain: field/normalization rank -> forced approximate root -> basis change -> residue separation/value set -> gap-count closure.
- **Gate E — Ground truth:** PASS. The solution proves primitiveness, rank `m`, finite normalization quotient, exact value set, and exact gap count over the full stated parameter range.
- **Gate F — Reviewer completeness:** PASS. The Weierstrass-division form is stated and instantiated; the associated-graded filtration for the length/gap equality is written explicitly; no load-bearing `direct calculation` is hidden.
- **Gate G — Solver evidence:** not yet applicable. This regenerated problem blob is unseen and must receive exactly one cold GPT-5.5 Medium run.
- **Gate H — Portal format:** PASS. Consecutive Steps, three Solution Concepts, exact Final Answer line, classification metadata present, standalone answer under the answer-length limit.
- **Gate I — Originality/corpus distance:** PASS. Main-branch searches for the parametrized branch, delta/normalization wording, and Apéry/valuation-semigroup skeleton returned no matching corpus item; mechanism registry has no matching skeleton.

## Independent sanity checks

Truncated exact linear-span computations for the image of `C[[x,y]]` in `C[[t]]` matched the formula for representative valid tuples including `(4,6,7)`, `(6,9,10)`, `(6,15,16)`, `(8,12,13)`, `(9,12,14)`, and `(10,15,17)` once truncation exceeded the conductor range.

## Promotion state

Quality-safe regenerated candidate. Publish `candidate-ready.json` only after re-reading the exact pair and using the blob SHAs above; then wait for exactly one GPT-5.5 Medium cold solve.