# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b\in\mathbb{R}$ and define
$$
P=a(x^2+y^2)^2+x^4-6x^2y^2+y^4,
\qquad
Q=b(x^2+y^2)^2+x^4-y^4.
$$
Consider the planar polynomial system
$$
\dot x=-Px-Qy,
\qquad
\dot y=-Py+Qx.
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

This problem studies global asymptotic stability in a homogeneous polynomial planar flow. In polar coordinates the radial and angular dynamics separate after a natural time rescaling, and the parameter region is determined by invariant angular rays in one regime and the net radial drift over a full rotation in the other.
