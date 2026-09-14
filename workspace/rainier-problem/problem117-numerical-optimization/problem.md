# Normalized Math Problem

## LaTeX (Normalized)

For each integer $m\geq 4$ and $k=0,1,2$, let
$$
R_k=
\begin{bmatrix}
\cos(k\pi/3)&-\sin(k\pi/3)\\
\sin(k\pi/3)&\cos(k\pi/3)
\end{bmatrix},
\qquad
P_k^{(m)}=R_k
\begin{bmatrix}1&0\\0&m\end{bmatrix}
R_k^T.
$$
Consider
$$
f(x)=\frac{1}{2}\|x\|_2^2.
$$
Choose a single constant step size
$$
0<\alpha\leq\frac{2}{m},
$$
and use it at every stage of one cyclic preconditioned-gradient sweep:
$$
x_{k+1}=x_k-\alpha P_k^{(m)}\nabla f(x_k),
\qquad k=0,1,2.
$$
Define
$$
R_m(\alpha)=\sup_{x_0\ne0}\frac{\|x_3\|_2}{\|x_0\|_2},
\qquad
R_m^*=\min_{0<\alpha\leq 2/m}R_m(\alpha),
$$
and let $\alpha_m$ be the smallest step size attaining $R_m^*$.

There are constants $A,B,C,D$ such that
$$
\alpha_m=\frac{A}{m}+\frac{B}{m^2}+o\left(m^{-2}\right),
\qquad
R_m^*=C+\frac{D}{m}+o\left(m^{-1}\right)
$$
as $m\to\infty$. Determine the exact ordered quadruple
$$
(A,B,C,D).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem studies the optimal constant step size for a cyclic preconditioned-gradient method as the anisotropy, hence the condition number of each preconditioner, tends to infinity. The task requires both spectral-norm optimization of the noncommuting three-stage update and a sharp asymptotic analysis of the minimizing step and optimal contraction.
