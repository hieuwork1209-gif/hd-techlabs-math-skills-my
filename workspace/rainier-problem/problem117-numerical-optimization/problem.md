# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
f(x)=\frac12\left(x_1^2+3x_2^2+5x_3^2+7x_4^2\right),
\qquad x\in\mathbb R^4.
$$
For step sizes $0<\alpha_0,\alpha_1,\alpha_2\leq\frac12$, start from $x_0\in\mathbb R^4$ and apply
$$
x_{k+1}=x_k-\alpha_{k\bmod 3}\nabla f(x_k).
$$
For the first cycle define the weighted transient contraction
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\sup_{x_0\neq0}
\frac{\max\left\{\frac5{14}\|x_1\|_2,\frac57\|x_2\|_2,\|x_3\|_2\right\}}
{\|x_0\|_2},
$$
and let
$$
R_*=\min_{0<\alpha_0,\alpha_1,\alpha_2\leq1/2}
R(\alpha_0,\alpha_1,\alpha_2).
$$
Determine the ordered pair $(R_*,\alpha_*)$, where $\alpha_*=(\alpha_0,\alpha_1,\alpha_2)$ is an optimizing ordered triple.

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

The task is to tune a periodic gradient-descent schedule for a strongly convex quadratic under a transient-sensitive minimax convergence criterion. The decisive structure couples one-, two-, and three-step convergence factors, so the problem is fundamentally Numerical optimization; prefix polynomials and interpolation identities provide optimality certificates for that algorithmic tuning problem.
