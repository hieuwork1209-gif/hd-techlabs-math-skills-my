# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b\in\mathbb{R}$. Consider the planar polynomial system
$$
\dot x=-x^3+3x^2y^2-3xy^4+y^6-2y^4+2y^3+(a-2b)y^2-2xy-ax-y,
$$
$$
\dot y=-x-y^3+y^2-by.
$$
Determine all pairs $(a,b)$ for which the equilibrium $(0,0)$ is globally asymptotically stable; that is, it is Lyapunov stable and every solution with initial data in $\mathbb{R}^2$ exists for all $t\geq0$ and converges to $(0,0)$ as $t\to\infty$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Solve for unknowns |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

This problem asks for the exact global-stability region of a planar polynomial system. A nonlinear polynomial coordinate exposes a coupled gradient flow, and the answer depends on a positive-semidefinite quadratic form together with quartic coercivity, including a nonhyperbolic boundary case.
