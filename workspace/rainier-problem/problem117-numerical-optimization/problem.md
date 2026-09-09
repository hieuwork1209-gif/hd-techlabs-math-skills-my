# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A=\operatorname{diag}(1,2,3,4,5,6,7),
\qquad
f(x)=\frac12x^TAx.
$$
Choose step sizes $\alpha_0,\alpha_1,\alpha_2>0$. Starting from a random point $x_0$ chosen uniformly from the unit sphere in $\mathbb R^7$, perform three gradient steps
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
R_*=\min_{\alpha_0,\alpha_1,\alpha_2>0}
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

The problem asks for optimal nonstationary gradient-step tuning on a quadratic with a simple evenly spaced spectrum under an isotropic average-case criterion. Three steps generate a cubic residual polynomial, while the spherical average converts the optimization into a discrete least-squares problem over the seven eigenvalues. A sharp solution uses a discrete evaluation certificate rather than endpoint minimax interpolation, placing the problem in numerical optimization.
