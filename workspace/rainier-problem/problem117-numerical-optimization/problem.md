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
\rho_*:=\min_{q_\pi\geq0,\ \sum_{\pi\in S_3}q_\pi=1}\rho(q),
$$
prove that the minimizing distribution is unique, and determine that distribution. Give the final answer as the ordered pair
$$
\left(\rho_*,q_{123}\right),
$$
where $q_{123}$ is the probability assigned to the sweep order $(1,2,3)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem optimizes the randomization law of a complete exact-coordinate Gauss-Seidel epoch for a symmetric positive-definite quadratic, with objective the worst-case expected energy contraction and with the equality case used to reconstruct the unique optimizer, which is part of Optimization and Numerical Mathematics and Numerical optimization. The problem also uses eigenvalues, invariant subspaces, and positive-semidefinite matrix inequalities from Linear Algebra, but those are subordinate tools for certifying the optimization objective rather than the primary requested task.
