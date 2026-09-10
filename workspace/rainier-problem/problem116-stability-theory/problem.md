# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b\in\mathbb{R}$. Consider the planar polynomial system
$$
\dot x=-4x^3-3a x^2y-2bxy^2-a y^3,
$$
$$
\dot y=-a x^3-2b x^2y-3axy^2-4y^3.
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

This problem concerns global asymptotic stability for a homogeneous polynomial gradient flow. The stability region is equivalent to positive definiteness of a symmetric binary quartic, whose reciprocal structure reduces the parameter analysis to a quadratic on the disconnected set $(-\infty,-2]\cup[2,\infty)$.
