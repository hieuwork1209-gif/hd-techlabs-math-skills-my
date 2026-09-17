# Normalized Math Problem

## LaTeX (Normalized)

For $0<c\leq\frac12$, let $u:[0,1]\to[-1,1]$ be Lebesgue measurable and define
$$
x_u(t)=\int_0^t u(s)\,ds.
$$
Assume
$$
x_u(1)=0,\qquad \int_0^1x_u(t)\,dt=0,\qquad x_u(t)\leq c\quad(0\leq t\leq1).
$$
Define
$$
M(c)=\max_u\int_0^1x_u(t)^3\,dt.
$$
Determine $M(c)$ exactly for every $0<c\leq\frac12$. A complete proof must also classify all optimal controls, up to equality almost everywhere, for every $c$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Dynamic programming and optimal control |
| **Problem Type** | Optimization |
| **Answer Type** | Function or mapping |

---

## Domain Explanation

The decision variable is a bounded measurable control, its state satisfies $x_u'=u$, and the optimization includes terminal, integral, and pointwise state constraints. The state ceiling creates an active-constraint regime and an inactive-constraint regime, while the task also requires reconstruction of every optimal control. Thus Optimization and Numerical Mathematics and Dynamic programming and optimal control remain the direct classification; the real-variable inequalities are tools for proving the sharp control result.
