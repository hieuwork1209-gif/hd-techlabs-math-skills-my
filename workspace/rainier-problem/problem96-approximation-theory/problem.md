# Normalized Math Problem

## LaTeX (Normalized)

For each real number $\varepsilon$, let $\mathcal M_\varepsilon$ be the set of all monic polynomials $P\in\mathbb R[x]$ of degree $6$ whose $x^3$-coefficient is $\varepsilon$. Define
$$
\Lambda(\varepsilon)=\min_{P\in\mathcal M_\varepsilon}\max_{-1\le x\le1}\frac{|P(x)|}{\sqrt{1+120x^2}}.
$$
Determine exactly
$$
\lim_{\varepsilon\to0}\frac{\Lambda(\varepsilon)-\Lambda(0)}{|\varepsilon|}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Approximation theory |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the first-order sensitivity of a weighted minimax problem under a coefficient constraint. Its main structure is weighted polynomial approximation, with an extremal certificate and a perturbation analysis around the unconstrained symmetric minimizer.
