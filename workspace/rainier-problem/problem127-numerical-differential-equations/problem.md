# Normalized Math Problem

## LaTeX (Normalized)

Let $a,d>0$. Consider the two-stage diagonally implicit Runge-Kutta method
$$
A=
\begin{pmatrix}
a&0\\
1-a-d&d
\end{pmatrix},
\qquad
b^T=\left(\frac12,\frac12\right),
\qquad
c=A\mathbf1.
$$
Its stability function is
$$
R(z)=1+z\,b^T(I-zA)^{-1}\mathbf1.
$$
Call the method L-stable if
$$
|R(z)|\leq1
$$
for every $z$ with $\operatorname{Re}z\leq0$ and, in addition,
$$
\lim_{x\to+\infty}R(-x)=0.
$$
Determine all pairs $(a,d)\in(0,\infty)^2$ for which the method is L-stable.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Numerical differential equations |
| **Problem Type** | Parameter identification |
| **Answer Type** | Set or multiset of objects |

---

## Domain Explanation

This problem is primarily Differential Equations and Dynamical Systems and Numerical differential equations: it asks for the complete L-stability region of a two-parameter family of diagonally implicit Runge-Kutta schemes. The classification couples the asymptotic decay condition of the rational stability function with a global boundedness certificate on the left half-plane.
