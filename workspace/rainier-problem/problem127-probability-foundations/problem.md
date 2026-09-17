# Normalized Math Problem

## LaTeX (Normalized)

Let $0<p<1$, $0<\rho<1$, and let $n\geq3$ be an integer. Let $(X_k)_{k\geq1}$ be an infinite exchangeable sequence of Bernoulli random variables satisfying
$$
\mathbb{P}(X_1=1)=p
$$
and
$$
\operatorname{Corr}(X_1,X_2)=\rho.
$$
Determine the largest possible value of
$$
\mathbb{P}(X_1=X_2=\cdots=X_n=1).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Probability and Statistics and Probability foundations: infinite exchangeability converts the joint Bernoulli law into a latent mixing distribution, while the prescribed marginal probability and pairwise correlation fix its first two moments. The requested extremal joint success probability is then determined by a sharp moment bound and its equality case.
