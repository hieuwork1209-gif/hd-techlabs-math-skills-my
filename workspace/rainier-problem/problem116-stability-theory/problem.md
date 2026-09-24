# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b\geq0$ and consider the nonlinear system
$$
x'=y,
\qquad
y'=-x-(a+bx^2)y.
$$
Determine all pairs $(a,b)$ for which the origin is globally exponentially stable in the Euclidean norm. That is, determine all $(a,b)$ for which there exist constants $M,\gamma>0$ such that every solution satisfies
$$
\|(x(t),y(t))\|_2
\leq
M e^{-\gamma t}
\|(x(0),y(0))\|_2
$$
for all $t\geq0$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Exhaustive enumeration |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

The problem asks for the complete parameter region giving global exponential stability of an equilibrium in a nonlinear second-order system. The main distinction is between local damping near the origin and the large-state decay rate required for a global exponential estimate.
