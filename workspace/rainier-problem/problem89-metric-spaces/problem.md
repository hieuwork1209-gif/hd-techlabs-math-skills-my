# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge4$. Let $\Pi_n$ be the graph whose vertices are the permutations in $S_n$, written in one-line notation, with two permutations adjacent exactly when one is obtained from the other by swapping two adjacent entries. Let $d$ be the shortest-path metric on $\Pi_n$.

For $p>0$, say that $(S_n,d)$ has $p$-negative type if every real family $(c_\sigma)_{\sigma\in S_n}$ with $\sum_\sigma c_\sigma=0$ satisfies
$$
\sum_{\sigma,\tau\in S_n}c_\sigma c_\tau\,d(\sigma,\tau)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(S_n,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^{S_n}:\sum_\sigma c_\sigma=0,\ \sum_{\sigma,\tau}c_\sigma c_\tau\,d(\sigma,\tau)^{\wp}=0\right\}.
$$
Determine the ordered pair $(\wp,\dim E)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Metric spaces |
| **Problem Type** | Exact computation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the maximal negative-type exponent of the permutahedron graph metric and the dimension of its boundary equality space. The decisive structure is a hidden Hamming representation by pairwise inversion indicators.
