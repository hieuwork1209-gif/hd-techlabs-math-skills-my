# Normalized Math Problem

## LaTeX (Normalized)

Let $H$ be a real symmetric positive definite matrix whose spectrum is contained in
$$
E=[1,2]\cup[4,5].
$$
Consider nonstationary gradient descent on the quadratic $f(x)=\frac12x^THx$:
$$
x_{k+1}=(I-\eta_{k+1}H)x_k,
$$
where the five step sizes $\eta_1,\dots,\eta_5$ are positive and chosen in advance.

Define
$$
\rho_5=\inf_{\eta_1,\dots,\eta_5>0}
\max_{\lambda\in E}
\left|\prod_{j=1}^{5}(1-\eta_j\lambda)\right|.
$$
Also define the stepwise-stable optimum
$$
\widehat\rho_5=
\inf_{\substack{\eta_1,\dots,\eta_5>0\\
\max_{\lambda\in E}|1-\eta_j\lambda|\leq1\ (j=1,\dots,5)}}
\max_{\lambda\in E}
\left|\prod_{j=1}^{5}(1-\eta_j\lambda)\right|.
$$
Determine the ordered pair $(\rho_5,\widehat\rho_5)$ exactly.

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

The problem asks for exact worst-case convergence factors of a five-step nonstationary gradient method on a quadratic objective whose spectrum lies in two separated intervals. The unrestricted and per-step-stable schedules are both step-size design problems for an iterative optimization method, so Numerical optimization is the primary sub-domain.
