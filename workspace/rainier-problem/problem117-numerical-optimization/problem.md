# Normalized Math Problem

## LaTeX (Normalized)

Let $A$ be a real symmetric positive-definite matrix whose spectrum is contained in
$$
[1,9],
$$
and let
$$
f(x)=\frac12x^TAx.
$$
Choose ordered step sizes
$$
0<\alpha_0\le\alpha_1\le\alpha_2\le\frac29.
$$
Starting from any $x_0\ne0$, perform three gradient steps
$$
x_{k+1}=x_k-\alpha_k\nabla f(x_k),
\qquad k=0,1,2.
$$
The bound $\alpha_k\le2/9$ makes every individual gradient step nonexpansive for every eigenvalue in $[1,9]$.

Define the worst-case three-step contraction factor
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\sup_{A:\,\sigma(A)\subset[1,9]}
\sup_{x_0\ne0}
\frac{\|x_3\|_2}{\|x_0\|_2},
$$
and let
$$
R_*=\min_{0<\alpha_0\le\alpha_1\le\alpha_2\le2/9}
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

The problem asks for optimal nonstationary gradient-step tuning on a quadratic when every individual step must remain spectrally nonexpansive. The three-step method produces a cubic residual polynomial, but the root locations are constrained by the stability bound. Determining the sharp worst-case contraction therefore becomes a constrained polynomial-design problem arising directly from numerical optimization.
