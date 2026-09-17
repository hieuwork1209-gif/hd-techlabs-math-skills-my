# Normalized Math Problem

## LaTeX (Normalized)

Let $u:[0,1]\to[-1,1]$ be Lebesgue measurable and define the chained states
$$
x_u(t)=\int_0^t u(s)\,ds,\qquad
y_u(t)=\int_0^t x_u(s)\,ds,\qquad
z_u(t)=\int_0^t y_u(s)\,ds.
$$
Assume
$$
x_u(1)=y_u(1)=z_u(1)=0.
$$
Determine
$$
\max_u\int_0^1x_u(t)^3\,dt
$$
exactly. A complete proof must also classify all optimal controls, up to equality almost everywhere.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Dynamic programming and optimal control |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The variable $u$ is a bounded measurable control for a chain of integrator states, with simultaneous terminal constraints on the first three states and a nonlinear running payoff. Solving the problem requires a sharp global compatibility argument between the terminal moment constraints and the geometry of optimal state excursions, so Optimization and Numerical Mathematics and Dynamic programming and optimal control are the direct classification.