# Regeneration audit v5 — problem123

## Candidate identity

- **Branch:** `adversary/problem123`
- **Problem path:** `workspace/rainier-problem/problem123-galois-theory/problem.md`
- **Problem blob:** `45793123e76381c7f0ed9a977c2001e0ddd78e62`
- **Solution blob:** `c08a39c8a23ee95b5364637e9953d7bec7796cca`
- **Domain/Sub-domain:** Abstract Algebra -> Galois theory.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists Galois theory with 1 remaining slot and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Final answer:** `C_{2^n}\rtimes(\mathbb Z/2^n\mathbb Z)^\times` with the natural multiplication action.
- **Stripped final-answer length:** 43 characters.

## Difficulty architecture

- **Natural object:** the Galois group of the splitting fields of the iterated preimage polynomial for the classical map $x^2-2$.
- **Hidden gateway:** discover the multiplicative coordinate $x=z+z^{-1}$ in which the iteration becomes $z\mapsto z^2$.
- **Serial nodes:** (1) prove the semiconjugacy and lift the roots; (2) prove the $2^n$ lifted trace-roots are distinct; (3) prove their splitting field is the full radical-cyclotomic compositum by faithfulness of its action on the roots; (4) prove the radical field is totally ramified at the odd prime $\ell$ while the cyclotomic field is unramified there; (5) conclude the two fields intersect trivially and are linearly disjoint; (6) build the split exact sequence and identify the multiplication action giving the semidirect product.
- **Closure certificate:** a trivial kernel for the action proves no smaller splitting field is possible, and trivial field intersection proves all radical and cyclotomic automorphisms occur independently.
- **Decisive skeleton:** `hidden-multiplicative-coordinate -> faithful-root-action -> ramification-separation -> semidirect-Galois-group`.
- **Workspace reuse:** 0 in the current mechanism registry; repository searches for the distinctive iterate/splitting-field and semidirect-product formulation returned no match on `main`.

## Triviality Probe

- **P1 State-space count:** no finite enumeration; the problem asks for the Galois group for arbitrary unbounded `n`, with group order growing as `2^(2n-1)` -> PASS.
- **P2 Decoration-deletion:** odd-prime hypothesis on `ell` -> Yes (it supplies Eisenstein irreducibility and ramification disjoint from the power-of-two cyclotomic field; `ell=2` changes the intersection); iterate depth `n` -> Yes; map `x^2-2` -> Yes; target `(ell^2+1)/ell` -> Yes; splitting-field/Galois-group request -> Yes -> PASS.
- **P3 Answer-triviality:** `C_{2^n} rtimes (Z/2^n Z)^times`; a nonabelian parameter-dependent family for `n>=2`, not a degenerate object -> PASS.
- **P4 Core-reduces-to:** the first gateway is the recognizable Chebyshev-type semiconjugacy `x=z+z^{-1}` (SOFT WARNING), but it is not the entire decisive content: field equality, ramification separation, linear disjointness, and the semidirect action remain load-bearing. Skeleton reuse=0 -> WARN, not hard reject.
- **P5 Answer-recoverability:** small `n` cases can be computed, but no finite computation determines the isomorphism type for all unbounded `n`; the general semidirect action and disjointness must be established symbolically -> PASS. Small-input/small-answer flag: clear.
- **P6 Route-Concession:** 6a multiplicative coordinate, radical-cyclotomic field, and ramification obstruction are all CONSTRUCT and absent from the statement; 6b longest step conceded? No; 6c compaction-forced definition? No -> PASS.
- **P7 Depth-vs-Breadth:** 7a six serial dependencies; 7b at most three fields (`E,C,M`) are active in the intersection stage and the root-action stage uses only `(beta,zeta)`; 7c every node is load-bearing -> PASS.
- **P8 Terminology-density:** N=0 bespoke terms; `iterate`, `splitting field`, and `Galois group` are standard terms. Max simultaneous primary definitions=2 (`f,K_n`); no renamed standard concept -> PASS.

## Reviewer completeness / correctness

- The identity `f(z+z^{-1})=z^2+z^{-2}` is derived explicitly and iterated by induction.
- The lifted equation is factored exactly and all `2^n` roots are written down; pairwise distinctness is proved rather than assumed.
- For any automorphism of the radical-cyclotomic compositum, its affine action `k -> a+bk` on root indices is derived. Triviality of the kernel proves the compositum equals the original splitting field.
- `X^{2^n}-ell` is Eisenstein at `ell`, giving the radical degree. Total ramification is proved by the principal-ideal identity `(ell)=(beta)^{2^n}` together with `Norm(beta)=ell`.
- On the cyclotomic side, for `n>=2`, `Phi_{2^n}(X)=X^{2^{n-1}}+1` has polynomial discriminant a power of 2; the exact order/field-discriminant index relation is stated, so the odd prime `ell` is unramified. The `n=1` case is handled separately by `C=Q`.
- Ramification therefore forces `Q(beta) intersect Q(zeta)=Q`; since the cyclotomic extension is Galois, this gives linear disjointness.
- The cyclic radical subgroup and the cyclotomic unit subgroup are explicitly defined, and conjugation is computed as `tau_a -> tau_{ba}`, fixing the semidirect action.
- Sanity checks: `n=1` gives `C_2`; for `n=2` an exact Galois-group computation for the specialized odd prime `ell=3` gives order 8 with a 4-cycle and an involution, matching `C_4 rtimes (Z/4Z)^times`.

## Promotion state

Fresh statement blob `45793123e763...` must receive exactly one GPT-5.5 Medium cold solve. No previous solver result applies to this Galois-theory blueprint.
