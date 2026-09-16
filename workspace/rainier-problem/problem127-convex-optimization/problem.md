# Normalized Math Problem

## LaTeX (Normalized)

Let $0\le m<1$. Among all measurable functions
$$
f:[-1,1]\to[0,\infty)
$$
with $f\in L^2([-1,1])$ and
$$
\int_{-1}^1 f(x)\,dx=1,
\qquad
\int_{-1}^1 x f(x)\,dx=m,
$$
determine the minimum possible value of
$$
\int_{-1}^1 f(x)^2\,dx.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Convex optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Optimization and Numerical Mathematics and Convex optimization: it minimizes a strictly convex quadratic functional over nonnegative $L^2$ functions subject to affine mass and first-moment constraints. The nonnegativity constraint becomes active beyond a sharp parameter threshold, so determining the optimum requires identifying and certifying both regimes.
