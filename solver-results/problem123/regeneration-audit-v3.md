# Regeneration audit v3 — problem123

## Selection

- **Domain/Sub-domain:** Abstract Algebra -> Commutative algebra.
- **Current slot evidence:** 2026-09-11 taxonomy snapshot lists Commutative algebra with 1 remaining slot and status open.
- **Problem Type:** Symbolic derivation.
- **Answer Type:** Exact symbolic expression.
- **Natural object:** the conductor of a sparse standard-graded monomial subalgebra inside the full degree-n Veronese algebra.
- **Hidden gateway:** encode degree-d monomials by the d-fold exponent sumset and discover that it is a union of equally spaced integer intervals indexed by the number of summands taken from the upper exponent block.
- **Serial nodes:** (1) graded exponent-sumset encoding; (2) exact interval decomposition; (3) saturation threshold where A_d=B_d; (4) upper conductor inclusion from saturation; (5) lower-degree exclusion by shifting a nonzero term into the next graded gap; (6) identify the homogeneous tail as a power of A_+.
- **Closure certificate:** the gap-shift argument excludes every nonzero homogeneous conductor element below the threshold, while homogeneity of the conductor reduces arbitrary elements to homogeneous components.
- **Final answer shape:** `A_+^{ceil((n-1)/r)-2}`; stripped answer length = 27 characters.

## Shortcut analysis

A generic normalization/conductor recipe does not determine the exponent. The decisive work is the problem-specific two-parameter description of every graded exponent set and the construction, for an arbitrary lower-degree nonzero polynomial, of a degree-one Veronese monomial that sends one of its terms into a genuine gap without allowing cancellation. No single named theorem supplies both directions.

Technique skeleton: `graded-exponent-sumset -> interval-saturation -> gap-shift-conductor`.
Workspace mechanism registry contains no matching skeleton; repository searches for the distinctive conductor/Veronese formulation returned no match on main.

## Mandatory triviality probes

- **P1 PASS:** the problem asks for a general law for unbounded integers n,r. The intended solution does not enumerate a finite state space; it proves a symbolic description of all d-fold sumsets.
- **P2 PASS:** every visible structural component is load-bearing. The lower exponent block, upper exponent block, full Veronese overring B, nontrivial-gap condition n>=2r+2, and standard grading all change either the saturation threshold or the conductor power if removed/trivialized.
- **P3 PASS:** the answer is the nondegenerate parameter-dependent ideal `A_+^{ceil((n-1)/r)-2}`; the exponent is at least 1 under n>=2r+2.
- **P4 PASS:** the decisive skeleton has no single retrievable theorem/algorithm that finishes the task after recognition; workspace reuse = 0.
- **P5 PASS:** fixed small instances can be checked computationally, but no finite/numerical side channel recovers the exact law for arbitrary unbounded n,r. Small-instance enumeration was used only as a sanity check and matched the proof.
- **P6 PASS:** the statement does not reveal the exponent sumset, interval decomposition, saturation threshold, or gap-shift obstruction.
- **P7 PASS:** the proof has 6 serial load-bearing nodes and at most two active structural objects at a time (current exponent intervals and the next-degree gap); difficulty is depth rather than parallel case breadth.
- **P8 PASS:** the statement introduces only the two primary algebras A and B; `A_+`, standard grading, and conductor are standard commutative-algebra terminology, with no renamed standard concept or helper-definition stack.

## Reviewer completeness / correctness

- The degree-d exponent set is derived explicitly by conditioning on the number h of upper-block summands and proving every integer from 0 to dr is attainable.
- The exact adjacency condition for consecutive integer intervals is shown as `dr >= n-r-1`, giving the minimal threshold `q=ceil((n-1)/r)-1`.
- Homogeneity of the conductor is proved from the grading rather than asserted.
- For every nonzero homogeneous element below degree q-1, the proof constructs an explicit `k` with `0<=k<=n` whose degree-one B monomial moves a chosen support exponent to the first point of a nonempty next-degree gap; distinct exponents rule out cancellation.
- Standard gradedness is used explicitly to identify the homogeneous tail with `A_+^{q-1}`.
- Exhaustive small checks over many nontrivial pairs `(n,r)` verified the sumset formula, saturation threshold, and monomial conductor criterion; the reference proof itself is symbolic and characteristic-free.

## Promotion state

Fresh statement blob must receive exactly one GPT-5.5 Medium cold solve. No prior solver result applies to this regenerated statement.
