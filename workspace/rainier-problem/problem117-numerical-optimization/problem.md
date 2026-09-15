# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A=\begin{bmatrix}
2&1&1\\
1&2&1\\
1&1&3
\end{bmatrix},
\qquad
f(x)=\frac12x^TAx.
$$
For a permutation $\pi=(\pi_1,\pi_2,\pi_3)$ of $\{1,2,3\}$, perform one exact Gauss-Seidel sweep in that order: starting from $x^{(0)}=x$, for $k=1,2,3$ replace coordinate $\pi_k$ by the value that minimizes $f$ while the other two coordinates are held fixed. Let the resulting vector be $x^\pi$.

Choose the permutation randomly according to an arbitrary probability distribution $q=(q_\pi)_{\pi\in S_3}$, and define
$$
\rho(q)=\sup_{x\ne0}
\frac{\mathbb E_q[f(x^\pi)]}{f(x)}.
$$
Determine exactly
$$
\rho_*:=\min_{q_\pi\geq0,\ \sum_{\pi\in S_3}q_\pi=1}\rho(q).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the optimal randomization of a complete exact-coordinate Gauss-Seidel epoch on a symmetric positive-definite quadratic. The objective is the worst-case expected energy contraction over all initial vectors, so the task is a numerical-optimization problem involving sweep operators, spectral minimax optimization, symmetry reduction, and a sharp global semidefinite lower bound.
