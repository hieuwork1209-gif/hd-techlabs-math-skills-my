# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A=\operatorname{diag}(1,2,4),
\qquad
f(x)=\frac12x^TAx.
$$
Choose step sizes satisfying the standard stability restriction
$$
0<\alpha_k\le\frac{2}{\lambda_{\max}(A)}=\frac12,
\qquad k=0,1,2.
$$
Starting from a random point $x_0$ chosen uniformly from the unit sphere in $\mathbb R^3$, perform three gradient steps
$$
x_{k+1}=x_k-\alpha_k\nabla f(x_k),
\qquad k=0,1,2.
$$
Define the average squared contraction factor
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\mathbb E\,\|x_3\|_2^2,
$$
where the expectation is over $x_0$, and let
$$
R_*=\min_{0<\alpha_0,\alpha_1,\alpha_2\le1/2}
R(\alpha_0,\alpha_1,\alpha_2).
$$
Determine $R_*$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Number |

---

## Domain Explanation

This problem asks for optimal nonstationary gradient-step tuning on a quadratic under the usual per-step stability bound. The isotropic average converts the objective into three residual values, while the stability restriction imposes a nonnegative-coefficient structure after a spectral shift. Exploiting that structure yields a sharp finite-step contraction bound, so the problem belongs to numerical optimization.
