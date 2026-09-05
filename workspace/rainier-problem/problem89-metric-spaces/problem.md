# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be the set of perfect matchings of the complete graph $K_8$ on vertex set $[8]$. Form a graph $G$ on $X$ by joining two perfect matchings when one is obtained from the other by choosing two matched edges and replacing them by one of the other two perfect matchings on the same four endpoints. Let $d$ be the shortest-path metric on $G$.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_M)_{M\in X}$ with $\sum_Mc_M=0$ satisfies
$$
\sum_{M,N\in X}c_Mc_N\,d(M,N)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^X:\sum_Mc_M=0,\ \sum_{M,N}c_Mc_N\,d(M,N)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a natural flip metric on perfect matchings and the dimension of its boundary equality space. The key structure is the alternating-cycle decomposition of two matchings together with the five symmetry types under the stabilizer of one matching.
