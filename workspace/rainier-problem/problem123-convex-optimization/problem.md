# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge2$. For numbers
$$
w_1,\dots,w_{n-1}\ge0,
\qquad
\sum_{i=1}^{n-1}w_i=1,
$$
let $L_w$ be the weighted Laplacian of the path on vertices $1,\dots,n$, defined by
$$
(L_wx)_1=w_1(x_1-x_2),
$$
$$
(L_wx)_i=w_{i-1}(x_i-x_{i-1})+w_i(x_i-x_{i+1})
\qquad(2\le i\le n-1),
$$
$$
(L_wx)_n=w_{n-1}(x_n-x_{n-1}).
$$
Write $\lambda_2(L_w)$ for the second-smallest eigenvalue of $L_w$.

Determine exactly
$$
M_n=\max_{\substack{w_i\ge0\\\sum_{i=1}^{n-1}w_i=1}}\lambda_2(L_w),
$$
and determine all weight vectors attaining the maximum.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Convex optimization |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem optimizes the algebraic connectivity of a weighted network over a simplex of edge resources. Since the second Laplacian eigenvalue is a concave function of the edge weights through its Rayleigh characterization, the primary task is a convex-optimization problem; spectral and orthogonal-polynomial arguments provide the sharp certificate and uniqueness of the optimizer.
