# Normalized Math Problem

## LaTeX (Normalized)

Let $a>0$ and $b,c\geq0$. For each delay $\tau\geq0$, consider
$$
x''(t)+a x'(t)+x(t)+b x(t-\tau)+c x'(t-\tau)=0.
$$
Its characteristic quasipolynomial is
$$
\Delta_{\tau}(\lambda)
=
\lambda^2+a\lambda+1+(b+c\lambda)e^{-\lambda\tau}.
$$
Determine all triples $(a,b,c)$ such that, for every $\tau\geq0$, every zero $\lambda\in\mathbb{C}$ of $\Delta_{\tau}$ satisfies
$$
\operatorname{Re}\lambda<0.
$$

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

The problem asks for the complete delay-independent spectral stability region of a second-order retarded differential equation. The decisive issue is whether the characteristic roots can reach the imaginary axis for some delay.
