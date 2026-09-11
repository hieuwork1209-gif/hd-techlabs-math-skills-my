# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
k=\frac1{\sqrt2},
\qquad
K(k)=\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-k^2\sin^2\phi}},
$$
and let $\operatorname{sn}(t,k)$ be the Jacobi elliptic sine. For $0<h<5$, consider the Lamé equation
$$
y''(t)+\left(h-3\operatorname{sn}^2(t,k)\right)y(t)=0.
$$
The coefficient has period $T=2K(k)$. Let $M_h$ be the monodromy matrix over one period $T$.

Determine all $h\in(0,5)$ for which both Floquet multipliers of $M_h$ have modulus $1$.

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

This is a Floquet spectral-stability problem for a classical periodic second-order differential equation. The parameter $h$ determines whether solutions lie in a stability band or an instability gap of the periodic coefficient.
