# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge3$. Let $B_n$ be the graph whose vertices are the signed permutations
$$
w=(w_1,\ldots,w_n),
$$
where $|w_1|,\ldots,|w_n|$ are distinct and form $\{1,\ldots,n\}$. Two vertices are adjacent exactly when one is obtained from the other by either

- swapping two adjacent entries, or
- replacing $w_1$ by $-w_1$.

Let $d$ be the shortest-path metric on $B_n$.

For $p>0$, say that $(B_n,d)$ has $p$-negative type if every real family $(c_w)$ with $\sum_wc_w=0$ satisfies
$$
\sum_{u,v}c_uc_v\,d(u,v)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(B_n,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^{B_n}:\sum_wc_w=0,\ \sum_{u,v}c_uc_v\,d(u,v)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of the standard signed-permutation Cayley graph and the dimension of its boundary equality space. The decisive structure is its realization as the chamber graph of the type $B_n$ reflection arrangement, which gives a hidden Hamming representation by separating hyperplanes.
