# Normalized Math Problem

## LaTeX (Normalized)

For real parameters $a,b$, a perturbation parameter $c>0$, and $s\geq0$, define
$$
R_{a,b}(s)=1-s+as^2+bs^3,
\qquad
S^{(c)}_{a,b}(s)=R_{a,b}(s)+cs^2R_{a,b}''(s),
$$
and
$$
M^{(c)}_{a,b}(s)=
\begin{pmatrix}
R_{a,b}(s)&s\bigl(R_{a,b}(s)-S^{(c)}_{a,b}(s)\bigr)\\
0&S^{(c)}_{a,b}(s)
\end{pmatrix}.
$$
For each fixed $s$ and $v_0\in\mathbb R^2$, consider
$$
v_{m+1}=M^{(c)}_{a,b}(s)v_m\qquad(m\geq0).
$$
Set
$$
\rho_c(a,b)=\sup\left\{L\geq0:\text{ for every }s\in[0,L]\text{ and every }v_0\in\mathbb R^2,\ (v_m)_{m\geq0}\text{ is bounded}\right\},
$$
and
$$
\rho_*(c)=\sup_{(a,b)\in\mathbb R^2}\rho_c(a,b).
$$
Determine exactly the right-hand sensitivity
$$
\kappa_*=\lim_{h\downarrow0}\frac{\rho_*(\tfrac14+h)-\rho_*(\tfrac14)}{h}.
$$
Your determination must also establish that this limit exists. You may use $\operatorname{Root}_I(P)$ to denote the unique real root of a polynomial $P$ in an interval $I$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem studies the sensitivity of the optimal power-bounded stability interval of a parameter-dependent discrete linear dynamical system under a perturbation of its curvature-coupled mode, which fits Differential Equations and Dynamical Systems and Stability theory. Polynomial minimax duality and algebraic elimination from Optimization and Algebra are tools for determining how the stability threshold changes.