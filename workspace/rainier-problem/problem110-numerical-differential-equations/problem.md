# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$, consider the one-step family applied to the decaying test equation $y'=-\kappa y$, where $\kappa>0$. With $s=h\kappa\geq0$, define
$$
R_{a,b}(s)=1-s+as^{2}+bs^{3},
\qquad
u_{m+1}=R_{a,b}(s)u_m\qquad(m\geq0).
$$
For each $(a,b)$, let
$$
\rho(a,b)=\sup\left\{L\geq0:\text{ for every }s\in[0,L]\text{ and every }u_0\in\mathbb R,\ (u_m)_{m\geq0}\text{ is bounded}\right\}.
$$
Let
$$
\rho_* = \sup_{(a,b)\in\mathbb R^2}\rho(a,b).
$$
Show that the supremum is attained by a unique pair $(a_*,b_*)$, and determine the ordered triple $(\rho_*,a_*,b_*)$. Any extremal polynomial inequality used in the proof must be established directly rather than quoted as a black box.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Numerical differential equations |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem asks for the sharp real-axis stability radius of a parameterized one-step discretization and for the unique coefficients attaining it. Amplification polynomials and bounded discrete dynamics are central topics in numerical differential equations. The extremal-polynomial argument supplies the sharp optimization certificate.
