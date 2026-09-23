# Normalized Math Problem

## LaTeX (Normalized)

Let $H$ be a real symmetric positive definite matrix whose spectrum is contained in
$$
E=[1,2]\cup[7,8].
$$
Consider nonstationary gradient descent on the quadratic $f(x)=\frac12x^THx$:
$$
x_{k+1}=(I-\eta_{k+1}H)x_k,
$$
where the six step sizes $\eta_1,\dots,\eta_6$ are positive and may be chosen in advance.

Define the optimal six-step worst-case contraction factor
$$
\rho_6=\inf_{\eta_1,\dots,\eta_6>0}
\max_{\lambda\in E}
\left|\prod_{j=1}^{6}(1-\eta_j\lambda)\right|.
$$
Determine $\rho_6$ exactly.

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

The problem asks for the optimal fixed six-step schedule for gradient descent on a class of quadratic objectives with a prescribed disconnected spectral set. Its core task is a minimax design of the gradient-descent error polynomial over that spectrum, which is a numerical optimization problem rather than a generic polynomial approximation problem.
