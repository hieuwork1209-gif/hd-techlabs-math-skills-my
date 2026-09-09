# Normalized Math Problem

## LaTeX (Normalized)

Let $A$ be a real symmetric positive-definite matrix whose spectrum is contained in
$$
[1,4]\cup[6,9].
$$
For
$$
f(x)=\frac12x^TAx,
$$
choose step sizes
$$
0<\alpha_0\le\alpha_1\le\alpha_2.
$$
Starting from any $x_0\ne0$, perform three gradient steps
$$
x_{k+1}=x_k-\alpha_k\nabla f(x_k),
\qquad k=0,1,2.
$$
Define the worst-case three-step contraction factor
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\sup_{A:\,\sigma(A)\subset[1,4]\cup[6,9]}
\sup_{x_0\ne0}
\frac{\|x_3\|_2}{\|x_0\|_2},
$$
and let
$$
R_*=\min_{0<\alpha_0\le\alpha_1\le\alpha_2}
R(\alpha_0,\alpha_1,\alpha_2).
$$
Determine the ordered pair
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

The task tunes a three-step nonstationary gradient method for a quadratic whose Hessian spectrum lies in two separated clusters. The iteration generates a degree-three residual polynomial, and the optimal schedule is obtained from a minimax polynomial on the disconnected spectral set. The spectral gap is load-bearing: it changes the extremal polynomial and therefore the best finite-step contraction factor.
