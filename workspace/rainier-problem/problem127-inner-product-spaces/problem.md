# Normalized Math Problem

## LaTeX (Normalized)

Let $v_1,\dots,v_5$ be unit vectors in $\mathbb{R}^{5}$, with indices read modulo $5$, such that
$$
\langle v_i,v_{i+1}\rangle=\frac12\qquad(i=1,\dots,5).
$$
Determine the maximum possible value of
$$
\left|\det[v_1\ v_2\ v_3\ v_4\ v_5]\right|.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Inner product spaces |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the largest volume of a parallelotope formed by unit vectors subject to cyclic inner-product constraints. Its primary content is Linear Algebra and Inner product spaces: the volume is a Gram determinant, the feasible Gram matrices are positive semidefinite, cyclic averaging reduces the completion by concavity of log determinant, and the remaining extremum is determined from the spectrum of a circulant Gram matrix. The cyclic combinatorics are subordinate to the inner-product geometry.
