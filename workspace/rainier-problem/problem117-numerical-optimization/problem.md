# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
f(x)=\frac12\left(x_1^2+3x_2^2+7x_3^2\right),
\qquad x\in\mathbb R^3.
$$
Choose step sizes $0<\alpha_0,\alpha_1,\alpha_2\le\frac12$. Starting from any $x_0\in\mathbb R^3$, set $x_{-1}=x_0$ and apply the heavy-ball iteration
$$
x_{k+1}=x_k-\alpha_{k\bmod3}\nabla f(x_k)+\frac13(x_k-x_{k-1}),
\qquad k\ge0.
$$
For the first cycle define
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\sup_{x_0\ne0}
\frac{\max\left\{\frac14\|x_1\|_2,\frac12\|x_2\|_2,\|x_3\|_2\right\}}
{\|x_0\|_2},
$$
and let
$$
R_*=\min_{0<\alpha_0,\alpha_1,\alpha_2\le1/2}R(\alpha_0,\alpha_1,\alpha_2).
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

The task tunes a periodic heavy-ball schedule on a strongly convex quadratic under a transient-sensitive minimax criterion. Momentum couples successive spectral residuals through a second-order recurrence, so the optimizer cannot be obtained from independent gradient-descent prefix products. The proof requires a spectral recurrence, coupled feasibility constraints, and an affine elimination certificate for the third step, placing the problem squarely in numerical optimization.
