# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
0<a<b,
\qquad
0<c<1,
\qquad
\tau>0.
$$
Consider the neutral delay differential equation
$$
x'(t)+a x(t)+c x'(t-\tau)+b x(t-\tau)=0.
$$
Its characteristic roots are the complex numbers $\lambda$ satisfying
$$
\lambda+a+(c\lambda+b)e^{-\lambda\tau}=0.
$$
Determine all delays $\tau>0$ for which every characteristic root satisfies
$$
\operatorname{Re}\lambda<0.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Parameter identification |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

This problem is primarily Differential Equations and Dynamical Systems and Stability theory: it asks for the exact delay range for spectral stability of a neutral delay equation. The solution must locate all imaginary-axis characteristic roots, determine their crossing direction, and rule out both an earlier instability and any later restabilization.
