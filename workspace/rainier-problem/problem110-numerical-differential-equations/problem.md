# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$ and $s\geq0$, define
$$
R_{a,b}(s)=1-s+as^2+bs^3,
\qquad
S_{a,b}(s)=R_{a,b}(s)+\frac{s^2}{4}R_{a,b}''(s),
$$
and
$$
M_{a,b}(s)=
\begin{pmatrix}
R_{a,b}(s)&s\bigl(R_{a,b}(s)-S_{a,b}(s)\bigr)\\
0&S_{a,b}(s)
\end{pmatrix}.
$$
For each fixed $s$ and $v_0\in\mathbb R^2$, consider
$$
v_{m+1}=M_{a,b}(s)v_m\qquad(m\geq0).
$$
Set
$$
\rho(a,b)=\sup\left\{L\geq0:\text{ for every }s\in[0,L]\text{ and every }v_0\in\mathbb R^2,\ (v_m)_{m\geq0}\text{ is bounded}\right\},
$$
and
$$
\rho_*=\sup_{(a,b)\in\mathbb R^2}\rho(a,b).
$$
Show that $\rho_*$ is attained by a unique pair $(a_*,b_*)$, and determine the ordered triple $(\rho_*,a_*,b_*)$ exactly. You may use $\operatorname{Root}_I(P)$ to denote the unique real root of a polynomial $P$ in an interval $I$.

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

This problem asks for the sharp simultaneous stability interval of a cubic amplification mode and a curvature-corrected companion mode. Their competing unit-disk constraints force an interior tangency together with two opposed endpoint contacts.
