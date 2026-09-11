# Regeneration audit v13 — problem123

## Why regeneration was required

The exact convex-optimization blob `72cfb8ab7be6514f6347e0f62305123f3e9a0330` was solved correctly by GPT-5.5 Medium in one intended run. Its earliest robust shortcut was shorter than the reference: the affine Rayleigh test gives the sharp upper bound and forces `w_i proportional i(n-i)`; then the centered pairwise-difference identity plus Cauchy yields exactly the weighted discrete Poincare inequality needed to prove optimality, so the full orthogonal-polynomial spectrum is unnecessary. Same-blueprint proposals based on edge caps, nonuniform costs, or secondary spectral outputs were rejected because clean exact versions either preserve the same affine-certificate skeleton or introduce constraints mainly to break the successful shortcut. The weighted-path blueprint is retired.

## Blueprint triage

At least three structurally different fresh directions were compared before authoring.

1. **Number Theory -> Elementary number theory — gcd of the even-index binomial coefficients in row `2p`.** Natural object: exact common divisibility of a canonical parity-restricted subset of one Pascal row. Gateway: prime-by-prime reduction from `C(2p,2)=p(2p-1)`. Post-gateway work: prove the `p`-part, analyze a general prime `q | 2p-1` through base-`q` digit compatibility, construct the escaping even index `q^a+1` when the cofactor is nontrivial, characterize why no such even digitwise subnumber exists precisely for a prime power, and prove the surviving `q` occurs to exponent exactly one. **Selected.**
2. **Analysis -> Complex analysis — three-node Schur/Pick derivative interpolation.** Quality-safe: the Pick matrix is canonical and PSD closure gives an extremal finite Blaschke map, but the resulting determinant reduction was judged too close to a standard one-shot interpolation recipe. **Survived preflight but not selected.**
3. **Abstract Algebra -> Field theory — intersection degree of finite-field cyclotomic extensions.** Quality-safe and natural, but uniqueness of finite subfields reduces the answer almost immediately to a gcd of multiplicative orders. **Survived preflight but not selected.**
4. **Number Theory -> Elementary number theory — gcd of all odd-index coefficients in row `n`.** Rejected before solver exposure: after invoking Lucas' theorem the three cases are routine, so it failed the Difficulty Architecture gate as theorem-recognition plus short casework.

At least two quality-safe alternatives survived; the restricted row-`2p` gcd was selected because it retains a nontrivial parity/digit classification and an exact valuation closure after Lucas' theorem is discovered.

## Exact selected pair

- **Problem path:** `workspace/rainier-problem/problem123-elementary-number-theory/problem.md`
- **Problem blob:** `09d7ddd800b614981c6ac4315ac585fd19341ae0`
- **Solution path:** `workspace/rainier-problem/problem123-elementary-number-theory/solution.md`
- **Solution blob:** `3db982255d60986d27f8865a4eeee6e4fae1f6ed`
- **Domain/Sub-domain:** Number Theory -> Elementary number theory.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists Elementary number theory with 1 remaining slot and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** `H_p = pq` if `2p-1=q^a` is a prime power, and `H_p=p` otherwise.
- **Standalone answer length:** 79 stripped characters; below the 100-character gate.

## Difficulty architecture

Serial reasoning nodes:

1. use `C(2p,2)=p(2p-1)` to limit possible primes;
2. prove `p` divides every allowed coefficient because the only interior multiple of `p` is the excluded odd index `p`, and prove its gcd exponent is exactly one;
3. for `q^a || 2p-1`, translate `q`-nondivisibility into digitwise containment via Lucas;
4. if `(2p-1)/q^a>1`, build the canonical escaping even index `q^a+1` and show its digits are contained in those of `2p`;
5. if `2p-1=q^a`, prove the only digitwise subnumbers are `0,1,q^a,q^a+1`, so parity excludes every interior even candidate;
6. use `k=q^(a-1)+1` plus a second Lucas calculation to prove the surviving `q` has exact valuation one.

The hard step is not merely recognizing Lucas' theorem: one must characterize the parity-restricted digitwise subnumbers and then separately close the exact valuation.

## Forward provenance / anti-reverse-engineering preflight

- **Prime-by-prime split:** CANONICAL, forced by the gcd and by the visible coefficient `C(2p,2)`.
- **Lucas theorem/base-`q` digits:** STANDARD_NATURAL_REPRESENTATION for binomial divisibility modulo a prime.
- **Index `q^a+1`:** FORCED_BY_EQUATIONS. The valuation `q^a || 2p-1` makes the low base-`q` digits of `2p` equal to `1,0,...,0` with a nonzero digit in position `a`; adding the units digit to `q^a` is the smallest even digitwise-contained index and is available exactly when the cofactor exceeds one.
- **Index `q^(a-1)+1`:** FORCED_BY_EQUATIONS as the nearest even index that reduces the prime-power case to the canonical coefficient `C(q^a,q^(a-1))`, whose valuation can be closed exactly.

No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

Compression test: explicitly naming Lucas' theorem in the statement would not remove the central work of classifying even digitwise subnumbers and proving the exact surviving exponent. The difficulty therefore survives a cleaner representation.

Reviewer-quote simulation: there are no custom coefficients, corrections, encoded standard structures, or cancellation-tuned relations. The family `2p` and the even-index subset are intrinsic to the divisibility question; their interaction excludes the central index `p` and creates the two-prime local analysis.

## Promotion gates pre-solver

- **Gate A — honest taxonomy:** PASS.
- **Gate B — natural statement:** PASS. A parity-restricted gcd of one Pascal row is independently meaningful and uses only intrinsic parameters.
- **Gate C — forward provenance:** PASS as above.
- **Gate D — difficulty architecture:** PASS. Lucas is only the gateway; witness construction, parity classification, necessity/sufficiency, and exact valuation remain serial and load-bearing.
- **Gate E — ground truth:** PASS. The proof covers every odd prime `p`, every prime divisor `q` of `2p-1`, prime and higher prime-power cases, and exact exponents.
- **Gate F — reviewer completeness:** PASS. Lucas' theorem is stated in the exact digit form used; every witness index is shown admissible; exact valuations are derived explicitly.
- **Gate G — solver evidence:** PENDING for this fresh exact blob.
- **Gate H — portal format:** PASS. Five consecutive Steps, three Solution Concepts, matching metadata, exact Final Answer, answer under 100 stripped characters.
- **Gate I — originality:** PASS. Repository searches for the restricted `2p` even-index binomial gcd and its Lucas/prime-power skeleton found no matching item on `main`.

## Sanity checks

Direct exact computation of the gcd for odd primes below 100 matches the stated formula. The simpler all-odd-index draft was rejected before any ready marker, so no solver budget was spent on that discarded statement.

## State

The exact normalized pair is quality-safe and ready for exactly one GPT-5.5 Medium cold solve. Publish `candidate-ready.json` only after this audit and only with the exact two blob SHAs above.
