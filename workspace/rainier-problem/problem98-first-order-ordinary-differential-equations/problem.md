# Normalized Math Problem

## LaTeX (Normalized)

Fix $p\in(0,2)$. For $\lambda>0$ and $u\in[-\frac12,\frac12]$, define
$$
F_{\lambda,p}(u)=(u^2-\lambda)^2+\lambda^3(1-pu).
$$
For each positive integer $n$, let $\lambda_{n,p}$ be the least positive value of $\lambda$ for which there is a strictly increasing function $y_{n,p}:[0,1]\to[0,1]$ satisfying
$$
y_{n,p}'(x)=
\frac{
nF_{\lambda,p}(u)
\left(1-4u^3+2(1-2u)x+36(1-2u)x^2\right)
}{
1-4u^3+nF_{\lambda,p}(u)
\left(12u^2x+2x^2+24x^3\right)
},
\qquad
u=y_{n,p}(x)-\frac12,
\qquad
y_{n,p}(0)=0,
\qquad
y_{n,p}(1)=1.
$$
Let $\xi_{n,p}\in(0,1)$ be determined by $y_{n,p}(\xi_{n,p})=\frac12$.

Determine the unique ordered pair $(c_p,K_p)$ such that
$$
\xi_{n,p}=c_p+K_pn^{-1/4}+o(n^{-1/4})
$$
as $n\to\infty$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | First-order ordinary differential equations |
| **Problem Type** | Parameter identification |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem involves a parameter-dependent nonlinear first-order differential equation and a terminal condition that selects the smallest admissible parameter, which are part of Differential Equations and Dynamical Systems and First-order ordinary differential equations. The problem also involves singular asymptotic analysis of two coalescing slow regions and an implicit transition location, which are part of Calculus. However, those asymptotic tools are used to analyze the trajectory selected by the differential equation rather than defining the primary subject.
