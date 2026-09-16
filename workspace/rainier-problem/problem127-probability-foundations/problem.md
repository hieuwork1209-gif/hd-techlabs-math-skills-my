# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be a random variable supported on $[0,1]$ such that
$$
\mathbb E[X]=\frac12,\qquad
\mathbb E[X^{2}]=\frac13,\qquad
\mathbb E[X^{3}]=\frac14,\qquad
\mathbb E[X^{4}]=\frac15.
$$
Determine the maximum possible Pearson correlation coefficient
$$
\operatorname{Corr}(X^{2},X^{3})
=\frac{\mathbb E[X^{5}]-\mathbb E[X^{2}]\mathbb E[X^{3}]}
{\sqrt{\operatorname{Var}(X^{2})\operatorname{Var}(X^{3})}}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem is a truncated moment extremal problem for probability measures on a compact interval. Its primary content is Probability and Statistics and Probability foundations: the correlation objective couples the unknown fifth and sixth moments, and sharp bounds follow from positivity of weighted polynomial squares, least-squares projection in the moment inner product, and construction of an extremal atomic distribution. The polynomial algebra is subordinate to the probabilistic moment constraints.
