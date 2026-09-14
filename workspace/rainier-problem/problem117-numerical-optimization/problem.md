# Normalized Math Problem

## LaTeX (Normalized)

For $\alpha>0$ and $\lambda>0$, define the reflected-proximal spectral factor
$$
\phi_\alpha(\lambda)=\frac{1-\alpha\lambda}{1+\alpha\lambda}.
$$
For three positive parameters $\alpha_1,\alpha_2,\alpha_3$, define the worst-case contraction over the spectral interval $[1,9]$ by
$$
\rho(\alpha_1,\alpha_2,\alpha_3)
=\max_{1\leq\lambda\leq9}
\left|
\phi_{\alpha_1}(\lambda)
\phi_{\alpha_2}(\lambda)
\phi_{\alpha_3}(\lambda)
\right|,
$$
and let
$$
\rho_*=\inf_{\alpha_1,\alpha_2,\alpha_3>0}
\rho(\alpha_1,\alpha_2,\alpha_3).
$$

For a real polynomial $p(t)$ and an interval $I$ containing exactly one real zero of $p$, write
$$
\operatorname{Root}(p(t);I)
$$
for that zero. Determine $\rho_*$ exactly in this notation.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The quantity $\rho_*$ is the optimal robust contraction of a three-stage reflected-proximal, or Cayley, iteration on a prescribed eigenvalue interval. The task is a parameter-optimization problem for a rational spectral filter and requires a global minimax certificate rather than pointwise tuning.
