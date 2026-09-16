# Normalized Math Problem

## LaTeX (Normalized)

Let $u:[0,1]\to[-1,1]$ be Lebesgue measurable, and define its state by
$$
x_u(t)=\int_0^t u(s)\,ds.
$$
Assume the terminal and integral state constraints
$$
x_u(1)=0,\qquad \int_0^1x_u(t)\,dt=0.
$$
Determine exactly
$$
\max_u\int_0^1x_u(t)^3\,dt.
$$
A complete proof must also classify all optimal controls up to equality almost everywhere.

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

The decision variable is a bounded measurable control, its state is determined by the control system $x_u'=u$, and the problem imposes terminal and integral state constraints while maximizing a running cubic payoff. The main task is to certify global optimality and reconstruct every optimal control, so Optimization and Numerical Mathematics and Dynamic programming and optimal control are the direct classification. Real-variable integral estimates are used only to solve this particular control problem.
