# Normalized Math Problem

## LaTeX (Normalized)

For $k=0,1,2$, let
$$
R_k=
\begin{bmatrix}
\cos(k\pi/3)&-\sin(k\pi/3)\\
\sin(k\pi/3)&\cos(k\pi/3)
\end{bmatrix},
\qquad
P_k=R_k
\begin{bmatrix}1&0\\0&4\end{bmatrix}
R_k^T.
$$
Consider
$$
f(x)=\frac12\|x\|_2^2.
$$
Choose step sizes
$$
0<\alpha_k\le\frac12,
\qquad k=0,1,2,
$$
and perform one cyclic preconditioned-gradient sweep
$$
x_{k+1}=x_k-\alpha_kP_k\nabla f(x_k),
\qquad k=0,1,2.
$$
Define
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\sup_{x_0\ne0}\frac{\|x_3\|_2}{\|x_0\|_2},
$$
and let
$$
R_*=
\min_{0<\alpha_0,\alpha_1,\alpha_2\le1/2}
R(\alpha_0,\alpha_1,\alpha_2).
$$
Determine
$$
\bigl(R_*,(\alpha_0^*,\alpha_1^*,\alpha_2^*)\bigr).
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

This problem asks for optimal tuning of a cyclic preconditioned-gradient method with three symmetric positive-definite preconditioners whose eigendirections rotate between stages. Because the update matrices do not commute, the cycle cannot be reduced to a scalar residual polynomial. The sharp solution instead depends on rank loss and geometric alignment of successive eigenspaces, which are natural finite-step phenomena in numerical optimization.
