# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
f(x)=\frac12\left(x_1^2+3x_2^2+5x_3^2+7x_4^2\right),
\qquad x\in\mathbb R^4.
$$
For step sizes $0<\alpha_0,\alpha_1,\alpha_2\leq\frac12$, apply the $3$-periodic gradient descent iteration
$$
x_{k+1}=x_k-\alpha_{k\bmod 3}\nabla f(x_k).
$$
Define its worst-case three-step state contraction by
$$
\rho(\alpha_0,\alpha_1,\alpha_2)
=\sup_{x_0\neq0}\frac{\|x_3\|_2}{\|x_0\|_2},
$$
and let
$$
\rho_*=\min_{0<\alpha_0,\alpha_1,\alpha_2\leq1/2}
\rho(\alpha_0,\alpha_1,\alpha_2).
$$
Determine the ordered pair $(\rho_*,S_*)$, where $S_*$ is the unordered multiset of the three step sizes of an optimizing triple.

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

The central task is to tune a constrained periodic gradient-descent schedule and determine its exact worst-case convergence factor on a strongly convex quadratic, so the problem is fundamentally Numerical optimization. The degree-$3$ convergence polynomial and interpolation identity are certificates for the algorithmic convergence optimization; unlike Approximation theory, there is no function-approximation target or best approximant being sought.
