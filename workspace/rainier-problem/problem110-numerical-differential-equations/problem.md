# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$, define
$$
R_{a,b}(z)=1-z+az^2+bz^3.
$$
For $L\geq0$, let
$$
\Gamma_L=[0,L]\cup i[0,L/2]\cup e^{i\pi/3}[0,L].
$$
For each fixed $z\in\Gamma_L$ and $u_0\in\mathbb C$, consider
$$
u_{m+1}=R_{a,b}(z)u_m\qquad(m\geq0).
$$
Set
$$
\rho(a,b)=\sup\left\{L\geq0:\text{ for every }z\in\Gamma_L\text{ and every }u_0\in\mathbb C,\ (u_m)_{m\geq0}\text{ is bounded}\right\},
$$
and
$$
\rho_*=\sup_{(a,b)\in\mathbb R^2}\rho(a,b).
$$
Show that $\rho_*$ is attained by a unique pair $(a_*,b_*)$, and determine $\rho_*$ exactly. You may use $\operatorname{Root}_I(P)$ to denote the unique real root of a polynomial $P$ in an interval $I$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Numerical differential equations |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the largest simultaneous stability scale of a cubic amplification polynomial on three coupled spectral rays. The imaginary ray imposes a local order constraint, while the oblique ray creates a competing nonlocal stability regime.
