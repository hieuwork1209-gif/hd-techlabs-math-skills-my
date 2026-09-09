# Normalized Math Problem

## LaTeX (Normalized)

Let $A$ be a real symmetric positive-definite matrix whose spectrum is contained in
$$
[1,4]\cup[6,9].
$$
For
$$
f(x)=\frac12 x^TAx,
$$
choose constant heavy-ball parameters $\alpha>0$ and $\beta\ge0$. Starting from any $x_0\ne0$, set $x_{-1}=x_0$ and perform two iterations
$$
x_{k+1}=x_k-\alpha\nabla f(x_k)+\beta(x_k-x_{k-1}),
\qquad k=0,1.
$$
Define the worst-case two-step contraction factor
$$
R(\alpha,\beta)
=\sup_{A:\,\sigma(A)\subset[1,4]\cup[6,9]}
\sup_{x_0\ne0}
\frac{\|x_2\|_2}{\|x_0\|_2},
$$
and let
$$
R_*=\min_{\alpha>0,\,\beta\ge0}R(\alpha,\beta).
$$
Determine the ordered pair
$$
\bigl(R_*,(\alpha_*,\beta_*)\bigr),
$$
where $(\alpha_*,\beta_*)$ is the optimizing parameter pair.

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

This problem asks for robust heavy-ball tuning when the Hessian spectrum has two separated clusters. Two iterations produce a quadratic residual polynomial, but the spectral gap changes the minimax geometry because the residual may attain a deeper extremum inside the missing interval without affecting the worst-case contraction. The proof therefore combines spectral reduction with a sharp interpolation certificate adapted to the disconnected spectral set.
