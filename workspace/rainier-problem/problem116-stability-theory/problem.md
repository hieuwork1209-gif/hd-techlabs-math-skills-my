# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$. Consider the transport system
$$
u_t+u_x=0,\qquad 0<x<1,
$$
$$
v_t+v_x=0,\qquad 0<x<3,
$$
with boundary coupling
$$
u(t,0)=a u(t,1)+v(t,3),
\qquad
v(t,0)=-b u(t,1).
$$
Determine all pairs $(a,b)$ for which the zero solution is exponentially stable in
$$
L^2(0,1)\times L^2(0,3).
$$
That is, determine all $(a,b)$ for which there exist constants $M,\gamma>0$ such that every solution satisfies
$$
\|u(t,\cdot)\|_{L^2(0,1)}+\|v(t,\cdot)\|_{L^2(0,3)}
\le M e^{-\gamma t}
\left(\|u(0,\cdot)\|_{L^2(0,1)}+\|v(0,\cdot)\|_{L^2(0,3)}\right)
$$
for all $t\ge0$.

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

This is an exponential-stability problem for a transport network with static boundary feedback and unequal propagation lengths. The feedback parameters determine whether repeated boundary returns decay or amplify as signals circulate through the two transport channels.
