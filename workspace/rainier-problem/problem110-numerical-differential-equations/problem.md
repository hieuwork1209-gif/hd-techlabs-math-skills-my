# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$, define the cubic stability polynomial
$$
R_{a,b}(z)=1-z+az^2+bz^3.
$$
For $L\geq0$, let
$$
\Sigma_L=[0,L]\cup i[0,L/2].
$$
For each fixed $z\in\Sigma_L$ and $u_0\in\mathbb C$, consider
$$
u_{m+1}=R_{a,b}(z)u_m\qquad(m\geq0).
$$
Set
$$
\rho(a,b)=\sup\left\{L\geq0:\text{ for every }z\in\Sigma_L\text{ and every }u_0\in\mathbb C,\ (u_m)_{m\geq0}\text{ is bounded}\right\},
$$
and
$$
\rho_*=\sup_{(a,b)\in\mathbb R^2}\rho(a,b).
$$
Show that $\rho_*$ is attained by a unique pair $(a_*,b_*)$, and determine the ordered triple $(\rho_*,a_*,b_*)$ exactly.

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

This problem asks for the sharp stability window of a cubic one-step amplification polynomial on coupled dissipative and oscillatory spectral segments. The real- and imaginary-axis constraints interact through the same method coefficients, making it a numerical stability optimization problem.
