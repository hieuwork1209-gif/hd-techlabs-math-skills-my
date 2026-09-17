# Normalized Math Problem

## LaTeX (Normalized)

Let $N\geq3$ be an integer and let $0<p<1$, $0<\rho<1$. Define
$$
r=\left\lfloor (N-1)p(1-\rho)\right\rfloor.
$$
Let $(X_1,\ldots,X_N)$ be an exchangeable Bernoulli vector satisfying
$$
\mathbb{P}(X_1=1)=p
$$
and
$$
\operatorname{Corr}(X_1,X_2)=\rho.
$$
Determine the largest possible value of
$$
\mathbb{P}(X_1=X_2=\cdots=X_N=1).
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

This problem is primarily Probability and Statistics and Probability foundations: finite exchangeability reduces the joint law to the distribution of the total number of successes, while the marginal probability and pairwise correlation fix its first two factorial moments. The sharp extremum then depends on the integer-lattice geometry of those moment constraints.
