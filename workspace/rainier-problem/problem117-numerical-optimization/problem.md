# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
U=\frac{1}{\sqrt{2}}\begin{bmatrix}1&-1\\1&1\end{bmatrix}.
$$
Assume the determinant of the Hessian is fixed while its anisotropy is uncertain. For $\mu\in[1,4]$, define
$$
Q_{\mu}=\begin{bmatrix}\mu&0\\0&\frac{4}{\mu}\end{bmatrix},
\qquad
R_{\mu}=UQ_{\mu}U^T,
$$
and
$$
f_{\mu}(x)=\frac{1}{2}x^TQ_{\mu}x,
\qquad
g_{\mu}(x)=\frac{1}{2}x^TR_{\mu}x
\qquad(x\in\mathbb{R}^2).
$$
Thus $\det Q_{\mu}=\det R_{\mu}=4$ for every $\mu$, while the two principal curvatures vary reciprocally between $1$ and $4$.

For $\rho>0$, define
$$
P_{h,\rho}(v)=\operatorname*{argmin}_{x\in\mathbb{R}^2}
\left(h(x)+\frac{\rho}{2}\|x-v\|_2^2\right).
$$
Using one common parameter pair $(\rho,\theta)$ for every $\mu\in[1,4]$, with $0<\theta\leq2$, perform one relaxed Douglas-Rachford step
$$
y=P_{f_{\mu},\rho}(z),
\qquad
w=P_{g_{\mu},\rho}(2y-z),
\qquad
z^+=z+\theta(w-y).
$$
Define the robust worst-case one-step Euclidean contraction
$$
\mathcal C(\rho,\theta)
=\sup_{\mu\in[1,4]}\sup_{z\ne0}
\frac{\|z^+\|_2}{\|z\|_2}.
$$
Determine exactly
$$
\mathcal C_*:=\min_{\rho>0,\ 0<\theta\leq2}\mathcal C(\rho,\theta),
$$
and determine the unique minimizing pair $(\rho_*,\theta_*)$. Give the final answer as
$$
(\rho_*,\theta_*,\mathcal C_*).
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

This problem asks for robust tuning of the penalty and relaxation parameters of Douglas-Rachford splitting for a fixed-determinant family of anisotropic quadratic objectives. The requested object is the parameter pair minimizing the worst-case contraction across the full anisotropy interval, which is part of Optimization and Numerical Mathematics and Numerical optimization. Linear Algebra, especially proximal reflections and matrix norms, is used only to certify the contraction bounds and is therefore subordinate to the numerical-optimization task.
