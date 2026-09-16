# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
U=\frac{1}{\sqrt{2}}\begin{bmatrix}1&-1\\1&1\end{bmatrix}.
$$
There are two independent uncertainties: an overall curvature scale $\lambda\in[\frac{1}{2},2]$ and an anisotropy parameter $\mu\in[1,4]$. Define
$$
Q_{\lambda,\mu}
=\lambda\begin{bmatrix}\mu&0\\0&\frac{4}{\mu}\end{bmatrix},
\qquad
R_{\lambda,\mu}=UQ_{\lambda,\mu}U^T,
$$
and
$$
f_{\lambda,\mu}(x)=\frac{1}{2}x^TQ_{\lambda,\mu}x,
\qquad
g_{\lambda,\mu}(x)=\frac{1}{2}x^TR_{\lambda,\mu}x
\qquad(x\in\mathbb{R}^2).
$$
Thus $\lambda$ changes the common scale while $\mu$ changes the reciprocal principal curvatures.

For $\rho>0$, define
$$
P_{h,\rho}(v)=\operatorname*{argmin}_{x\in\mathbb{R}^2}
\left(h(x)+\frac{\rho}{2}\|x-v\|_2^2\right).
$$
Using one common parameter pair $(\rho,\theta)$ for every $(\lambda,\mu)\in[\frac{1}{2},2]\times[1,4]$, with $0<\theta\leq2$, perform one relaxed Douglas-Rachford step
$$
y=P_{f_{\lambda,\mu},\rho}(z),
\qquad
w=P_{g_{\lambda,\mu},\rho}(2y-z),
\qquad
z^+=z+\theta(w-y).
$$
For fixed $(\lambda,\mu)$ define
$$
\kappa_{\lambda,\mu}(\rho,\theta)
=\sup_{z\ne0}\frac{\|z^+\|_2}{\|z\|_2},
$$
and define the robust worst-case contraction
$$
\mathcal C(\rho,\theta)
=\sup_{(\lambda,\mu)\in[\frac{1}{2},2]\times[1,4]}
\kappa_{\lambda,\mu}(\rho,\theta).
$$
Also define the worst-case uncertainty set
$$
\mathcal W(\rho,\theta)
=\left\{(\lambda,\mu)\in[\frac{1}{2},2]\times[1,4]:
\kappa_{\lambda,\mu}(\rho,\theta)=\mathcal C(\rho,\theta)\right\}.
$$
Determine exactly
$$
\mathcal C_*:=\min_{\rho>0,\ 0<\theta\leq2}\mathcal C(\rho,\theta),
$$
determine the unique minimizing pair $(\rho_*,\theta_*)$, and determine the complete set
$$
\mathcal W_*:=\mathcal W(\rho_*,\theta_*).
$$
Give the final answer as
$$
(\rho_*,\theta_*,\mathcal C_*,\mathcal W_*).
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

This problem asks for robust parameter tuning of relaxed Douglas-Rachford splitting under simultaneous scale and anisotropy uncertainty, together with identification of all uncertainty realizations attaining the optimal worst-case contraction. The primary task is therefore a minimax tuning and extremal-set problem in Optimization and Numerical Mathematics and Numerical optimization. Linear Algebra, especially proximal reflections and operator norms, supplies the certificates for the robust bounds and is subordinate to the numerical-optimization objective.
