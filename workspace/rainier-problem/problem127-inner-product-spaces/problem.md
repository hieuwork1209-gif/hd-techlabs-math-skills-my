# Normalized Math Problem

## LaTeX (Normalized)

Let $v_1,\dots,v_4$ be a basis of $\mathbb R^4$ such that
$$
\|v_i\|=1\qquad(i=1,\dots,4).
$$
Let $w_1,\dots,w_4$ be the dual basis with respect to the Euclidean inner product, so
$$
\langle v_i,w_j\rangle=\delta_{ij}.
$$
Suppose also that
$$
\|w_i\|=\sqrt2\qquad(i=1,\dots,4).
$$
Fix two sign vectors
$$
\varepsilon=(\varepsilon_1,\dots,\varepsilon_4),
\qquad
\eta=(\eta_1,\dots,\eta_4)\in\{-1,1\}^4
$$
satisfying
$$
\sum_{i=1}^4\varepsilon_i\eta_i=0.
$$
Determine the maximum possible value of
$$
\left\|\sum_{i=1}^4\varepsilon_i v_i\right\|
\left\|\sum_{i=1}^4\eta_i v_i\right\|.
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

This problem is primarily Linear Algebra and Inner product spaces: the basis and Euclidean dual basis are encoded by a positive definite Gram matrix $G$ and its inverse, while the prescribed norms fix the diagonals of both matrices. The two orthogonal sign vectors select a two-dimensional subspace on which the quadratic form of $G$ must be optimized, so the problem couples dual-basis geometry with a sharp two-dimensional spectral bound. Scalar inequalities enter only after this inner-product-space reduction.
