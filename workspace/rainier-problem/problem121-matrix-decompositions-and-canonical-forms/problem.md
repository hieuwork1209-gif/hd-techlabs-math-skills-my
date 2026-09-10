# Normalized Math Problem

## LaTeX (Normalized)

Let $n\geq5$ be odd and let $m=\binom{n}{2}$. Let $B_n\in M_{n\times m}(\mathbb{Z})$ be the matrix whose columns are indexed by the unordered pairs $\{i,j\}\subset\{1,\ldots,n\}$, with the column indexed by $\{i,j\}$ equal to $e_i+e_j$, where $e_1,\ldots,e_n$ is the standard basis of $\mathbb{Z}^n$.

Define
$$
M_n=2(n-1)I_m-B_n^TB_n.
$$

Determine the Smith normal form of $M_n$ over $\mathbb{Z}$, with the diagonal invariant factors written in divisibility order.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Matrix decompositions and canonical forms |
| **Problem Type** | Canonicalization or normalization |
| **Answer Type** | Canonical form |

---

## Domain Explanation

The requested object is the Smith normal form of an explicit integer matrix, so the problem is fundamentally about canonical matrix decompositions. The pair-indexed columns give the matrix a combinatorial symmetry, but no graph is an input or an output; the task is to determine integer invariant factors, making Linear Algebra -> Matrix decompositions and canonical forms a better fit than a combinatorics classification.
