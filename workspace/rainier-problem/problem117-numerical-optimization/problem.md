# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
Q=\begin{bmatrix}1&0\\0&4\end{bmatrix},
\qquad
R=\begin{bmatrix}\frac{5}{2}&-\frac{3}{2}\\-\frac{3}{2}&\frac{5}{2}\end{bmatrix},
$$
and define
$$
f(x)=\frac{1}{2}x^TQx,
\qquad
g(x)=\frac{1}{2}x^TRx
\qquad(x\in\mathbb{R}^2).
$$
For $\rho>0$, define the proximal maps
$$
P_{f,\rho}(v)=\operatorname*{argmin}_{x\in\mathbb{R}^2}
\left(f(x)+\frac{\rho}{2}\|x-v\|_2^2\right),
$$
$$
P_{g,\rho}(v)=\operatorname*{argmin}_{x\in\mathbb{R}^2}
\left(g(x)+\frac{\rho}{2}\|x-v\|_2^2\right).
$$
For a relaxation parameter $0<\theta<2$, one relaxed Douglas-Rachford step is
$$
y=P_{f,\rho}(z),
\qquad
w=P_{g,\rho}(2y-z),
\qquad
z^+=z+\theta(w-y).
$$
Since the unique minimizer of $f+g$ is $0$, define the worst-case one-step Euclidean contraction
$$
C(\rho,\theta)=\sup_{z\ne0}\frac{\|z^+\|_2}{\|z\|_2}.
$$
Determine exactly
$$
C_*:=\min_{\rho>0,\ 0<\theta<2}C(\rho,\theta),
$$
and determine the unique minimizing pair $(\rho_*,\theta_*)$. Give the final answer as
$$
(\rho_*,\theta_*,C_*).
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

This problem tunes the penalty and relaxation parameters of relaxed Douglas-Rachford splitting for a strongly convex quadratic optimization problem by minimizing its worst-case one-step contraction, which is part of Optimization and Numerical Mathematics and Numerical optimization. Linear Algebra, especially singular values and matrix norms, supplies the convergence certificate, but it is subordinate because those tools are used to optimize the parameters of the splitting algorithm rather than being the requested object themselves.
