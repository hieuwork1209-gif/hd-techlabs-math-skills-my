# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$ and $s\geq0$, set
$$
R_{a,b}(s)=1-s+as^2+bs^3,\qquad c=\frac3{25},
$$
and define
$$
A_s=\begin{pmatrix}1&cs\\0&R_{a,b}(s)\end{pmatrix},
\qquad
B_s=\begin{pmatrix}R_{a,b}(s)&0\\-cs&1\end{pmatrix}.
$$
For each fixed $s$ and $v_0\in\mathbb R^2$, define
$$
v_{m+1}=
\begin{cases}
A_s v_m,&m\ \text{even},\\
B_s v_m,&m\ \text{odd}.
\end{cases}
$$
Set
$$
\rho(a,b)=\sup\left\{L\geq0:\text{ for every }s\in[0,L]\text{ and every }v_0\in\mathbb R^2,\ (v_m)_{m\geq0}\text{ is bounded}\right\},
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

This problem asks for the sharp stability interval of a periodically alternating two-stage amplification scheme. Power boundedness is controlled by the two-step monodromy matrix, whose unit-disk root conditions interact with the cubic scalar amplification polynomial.
