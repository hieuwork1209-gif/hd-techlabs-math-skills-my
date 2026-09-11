# Hardening audit — problem123 — elementary number theory revision

## Trigger and solver diagnosis

The exact v1 statement blob `09d7ddd800b614981c6ac4315ac585fd19341ae0` was solved correctly by GPT-5.5 Medium in one intended run. The solver's robust route was:

- reduce the gcd to the prime `p` and primes dividing `2p-1`;
- dispatch the `p`-part immediately;
- use Lucas digit compatibility to prove that a divisor `q | (2p-1)` survives exactly in the prime-power case;
- use Kummer to show the surviving exponent is one.

The v1 difficulty therefore failed.

## Structural revision

The revision replaces the special assumption “`p` is prime” by the natural ambient hypothesis “`m` is odd”. The same parity-restricted gcd is now determined for every odd row `2m`.

Proposal sentence required by the quality preflight:

> The solver's original shortcut fails because the revised problem introduces the natural dependency that every prime divisor `q | m` has its own base-`q` digit geometry, which arises directly from Lucas' criterion for even admissible indices and forces the additional reasoning step of classifying all proper even digitwise subnumbers before the separate `q | (2m-1)` family and exact Kummer exponents can be closed.

This is hardening by depth, not concealment: no notation layer, tuned constant, extra relation, or artificial exclusion was added. The hypothesis was relaxed.

## Exact revised pair

- **Problem path:** `workspace/rainier-problem/problem123-elementary-number-theory/problem.md`
- **Problem blob:** `4f68bc3891d858d8ed8f91d9d61190a03d68ca54`
- **Solution path:** `workspace/rainier-problem/problem123-elementary-number-theory/solution.md`
- **Solution blob:** `1da7f4bd3aa672551fafa060c08306dcbee7c1e4`
- **Domain/Sub-domain:** Number Theory -> Elementary number theory.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Reference:** product of precisely the primes `q` for which `2m=2q^a`, or `2m=q^a+q^b` with `a>b>=1`, or `2m-1=q^a`.
- **Standalone answer length:** 98 stripped characters; within the 100-character gate.

## Ground-truth architecture

1. `C(2m,2)=m(2m-1)` restricts possible primes to two coprime intrinsic families.
2. For `q | m`, Lucas converts common divisibility into the nonexistence of an even proper digitwise subnumber of `2m`.
3. Since `q` is odd, parity equals base-`q` digit-sum parity. Such an even proper subnumber is absent exactly when the digit sum of `2m` is two, equivalently `2m=2q^a` or `q^a+q^b`.
4. Kummer gives a forced one-carry witness in each surviving `q | m` regime, proving exponent exactly one.
5. For `q | (2m-1)`, the forced Lucas witness `q^{v_q(2m-1)}+1` removes `q` unless `2m-1` is a pure prime power.
6. In that prime-power case, parity excludes all digitwise interior subnumbers and a one-carry Kummer witness again gives exponent one.
7. The two coprime prime families combine exhaustively.

## Forward provenance

- Prime-family split: **FORCED_BY_EQUATIONS** from the index-2 coefficient.
- Lucas digit criterion: **STANDARD_NATURAL_REPRESENTATION** for prime divisibility of binomial coefficients.
- Digit-sum-two condition: **FORCED_BY_EQUATIONS** by classifying even proper digitwise subnumbers; it is derived, not placed in the statement.
- Witness indices `2q^{a-1}` and `q^{a-1}+1`: **FORCED_BY_EQUATIONS** as the nearest indices producing exactly one carry in the already-derived surviving digit patterns.
- Kummer carry count: **STANDARD_NATURAL_REPRESENTATION** for exact binomial valuations.

No object is `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, or `BACKSOLVED_FROM_FINAL_ANSWER`.

## Pass gates

- **A — Honest taxonomy:** PASS. The target is an exact divisibility classification; Elementary number theory is primary.
- **B — Natural statement:** PASS. It asks the same intrinsic restricted-binomial gcd for all odd `m`, with fewer special assumptions than v1.
- **C — Forward provenance:** PASS as above.
- **D — Difficulty architecture:** PASS. Lucas is only the gateway; local digit classification, two prime families, exact valuations, and exhaustive closure remain serially load-bearing.
- **E — Ground truth:** PASS. Direct brute-force checks for every odd `m <= 201` matched the formula, and the proof covers all odd `m >= 3`.
- **F — Reviewer completeness:** PASS. Lucas and Kummer are stated in exact forms, the digit classification is proved both ways, and every exact exponent has an explicit one-carry witness.
- **G — Solver evidence:** PENDING for the revised blob. The old v1 solver result is not reused.
- **H — Portal format:** PASS. Consecutive Steps, three Solution Concepts, exact Final Answer line, matching metadata, answer within limit.
- **I — Originality:** PASS. Repository searches on `main` for restricted/even-index binomial gcd and Lucas/Kummer variants returned no matching corpus item.

## Quality-redesign preflight

Compression does not expose a shorter hidden standard object; the statement is already the natural gcd question. Reviewer-quote simulation has no reverse-engineering red flag. The revision adds intrinsic local classification after the same visible gateway rather than making Lucas harder to recognize.

The revised exact pair is solver-eligible after the matching ready marker is published last.
