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
Determine the maximum possible value of
$$
\left|\det[v_1\ v_2\ v_3\ v_4]\right|.
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

This problem is primarily Linear Algebra and Inner product spaces: the basis and its Euclidean dual are encoded by a positive definite Gram matrix $G$ and its inverse $G^{-1}$, while the unit-norm conditions prescribe their diagonals. The volume is $\sqrt{\det G}$, so the extremal problem couples the spectrum of a Gram matrix with the compatibility of simultaneous diagonal constraints on $G$ and $G^{-1}$. Scalar optimization is subordinate to this inner-product and dual-basis structure.
