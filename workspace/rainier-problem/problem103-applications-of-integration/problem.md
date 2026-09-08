# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
T=\{(x,y)\in\mathbb{R}^2:x\geq0,\ y\geq0,\ x+y\leq1\},
\qquad z=1-x-y,
$$
and define
$$
\Delta=(x-y)(y-z)(z-x).
$$
For each integer $n\geq1$, put
$$
I_n=
\iint_T
\frac{\Delta^2 e^{-nxyz}}
{\sqrt{xyz}(x+y)(y+z)(z+x)}\,dx\,dy.
$$
Let Euler's constant be
$$
\gamma=\lim_{m\to\infty}
\left(\sum_{k=1}^m\frac{1}{k}-\log m\right).
$$
Evaluate
$$
\lim_{n\to\infty}
\left(
n^{3/2}I_n-\sqrt{\pi}\,n+6\pi\sqrt{n}-9\sqrt{\pi}\log n
\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

Up to normalization, the factor
$\Delta^2/[\sqrt{xyz}(x+y)(y+z)(z+x)]$
is the three-eigenvalue Bures spectral weight on the standard simplex. The determinant $xyz$ vanishes on nested boundary strata, and the Bures denominator couples those strata so that the Mellin transform develops both simple poles and a double pole. Determining the renormalized determinant-Laplace asymptotic is a natural exact integration problem in Calculus -> Applications of integration.
