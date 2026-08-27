# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$, consider a two-step discretization of the decaying test equation $y'=-\kappa y$, where $\kappa>0$. With $s=h\kappa$, set
$$
B_s=as+bs(1-s)
$$
and define
$$
u_{m+2}=\bigl(1+B_s-s(1-s)\bigr)u_{m+1}-B_s u_m\qquad(m\geq 0).
$$
Call $(a,b)$ interval-stable if, for every $s\in[0,1]$ and every real starting pair $(u_0,u_1)$, the resulting sequence $(u_m)_{m\geq 0}$ is bounded. Determine the set of all interval-stable pairs $(a,b)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Numerical differential equations |
| **Problem Type** | Exhaustive enumeration |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

This problem involves stability of a two-step discretization over a full interval of step parameters, which is part of Differential Equations and Dynamical Systems and Numerical differential equations.
The problem also involves quadratic characteristic roots and exact parameter envelopes, which are part of Algebra.
However, the algebraic tools support the stability classification and are not the main subject.
