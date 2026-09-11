# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$. For each delay $\tau>0$, consider the scalar delay differential equation
$$
\dot x(t)=-x(t)-a\,x(t-\tau)-b\,x(t-2\tau),\qquad t\ge0,
$$
with arbitrary continuous initial history on $[-2\tau,0]$.
Determine all pairs $(a,b)$ for which, for every $\tau>0$, the zero solution is globally asymptotically stable in the history sup norm; that is, it is Lyapunov stable and every solution exists for all $t\ge0$ and satisfies $x(t)\to0$ as $t\to\infty$.

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

This is a delay-independent stability problem for a scalar linear equation with two commensurate delays. The exact gain region is obtained by excluding imaginary characteristic roots for every delay, reducing the phase condition to positivity of a quadratic trigonometric polynomial on an open interval.
