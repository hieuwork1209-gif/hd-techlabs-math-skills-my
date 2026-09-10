# Normalized Math Problem

## LaTeX (Normalized)

An orientation of a finite graph is called Eulerian if every vertex has equal indegree and outdegree.

Let $\operatorname{Aut}(K_{6,6})$ act on orientations of $K_{6,6}$ by transporting edge directions along graph automorphisms.

Among all Eulerian orientations of $K_{6,6}$, determine the multiset of orbit sizes under this action, listed in increasing order.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Discrete Mathematics and Combinatorics |
| **Sub-domain** | Graph theory |
| **Problem Type** | Exhaustive enumeration |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem counts balanced orientations of a complete bipartite graph modulo its natural automorphism group. Encoding an Eulerian orientation by a regular binary matrix turns part-preserving automorphisms into row and column permutations, while automorphisms exchanging the two parts induce a complement-transpose symmetry; the final count requires classifying the resulting incidence structures and applying orbit-stabilizer.
