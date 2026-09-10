# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b\in\mathbb{R}$. Consider the planar polynomial system
$$
\dot x=y,
$$
$$
\dot y=-x^5-a x^3-b x^2-x-(1+x^2)y.
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

This is a polynomial damped-oscillator system. Global asymptotic stability is controlled by a mechanical-energy Lyapunov function, but determining the exact parameter region requires characterizing when the quartic restoring factor $x^4+a x^2+b x+1$ is strictly positive on the whole real line.
