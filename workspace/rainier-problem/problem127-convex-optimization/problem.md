# Normalized Math Problem

## LaTeX (Normalized)

Let $0\le m\le\frac12$. Among all measurable functions
$$
f:[-1,1]\to[0,1]
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

This problem is primarily Optimization and Numerical Mathematics and Convex optimization: it minimizes a strictly convex quadratic functional over an $L^2$ box subject to affine mass and first-moment constraints. As the prescribed mean increases, the unconstrained affine projection hits both faces of the box, creating a genuine active-set transition whose sharp value requires reconstructing and certifying the clipped optimizer.
