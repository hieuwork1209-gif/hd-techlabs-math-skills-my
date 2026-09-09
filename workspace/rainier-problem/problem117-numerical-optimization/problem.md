# Normalized Math Problem

## LaTeX (Normalized)

For each $\lambda\in[1,9]$, let
$$
f_\lambda(x)=\frac{\lambda}{2}x^2.
$$
Choose constant heavy-ball parameters $\alpha>0$ and $\beta\ge0$. Starting from $x_{-1}=x_0\ne0$, perform two iterations
$$
x_{k+1}=x_k-\alpha f_\lambda'(x_k)+\beta(x_k-x_{k-1}),
\qquad k=0,1.
$$
Define the worst-case two-step contraction factor
$$
R(\alpha,\beta)
=\max_{\lambda\in[1,9]}\left|\frac{x_2}{x_0}\right|,
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

This problem asks for robust tuning of the heavy-ball method over a natural interval of quadratic curvatures. Two iterations produce a degree-two residual polynomial, and the optimal parameters are characterized by a sharp minimax argument on the spectral interval, making the problem a numerical optimization problem with an exact convergence-factor calculation.
