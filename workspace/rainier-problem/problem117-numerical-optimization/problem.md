# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
Q=\begin{bmatrix}1&0\\0&4\end{bmatrix},
\qquad
R=\begin{bmatrix}\frac{5}{2}&-\frac{3}{2}\\-\frac{3}{2}&\frac{5}{2}\end{bmatrix}.
$$
The common curvature scale is uncertain and is known only to lie between the two eigenvalues of $Q$. Thus, for $\mu\in[1,4]$, define
$$
f_{\mu}(x)=\frac{\mu}{2}x^TQx,
\qquad
g_{\mu}(x)=\frac{\mu}{2}x^TRx
\qquad(x\in\mathbb{R}^2).
$$
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

This problem asks for robust tuning of the penalty and relaxation parameters of Douglas-Rachford splitting when the quadratic objective has an uncertain common curvature scale. The requested object is the parameter pair minimizing the worst-case contraction across the entire uncertainty interval, which is part of Optimization and Numerical Mathematics and Numerical optimization. Linear Algebra, especially singular values and matrix norms, is used only to certify the contraction bounds and is therefore subordinate to the numerical-optimization task.
