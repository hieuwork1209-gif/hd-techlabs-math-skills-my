# Normalized Math Problem

## LaTeX (Normalized)

Let $k\ge2$ and $n\ge3k-1$. Let $KG(n,k)$ be the Kneser graph whose vertices are the $k$-subsets of $[n]=\{1,\ldots,n\}$, with two vertices adjacent exactly when they are disjoint. Let $d$ be its shortest-path metric.

For $p>0$, say that the vertex set has $p$-negative type if every real family $(c_S)$ with $\sum_S c_S=0$ satisfies
$$
\sum_{S,T}c_Sc_T\,d(S,T)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:KG(n,k)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define
$$
E=\left\{c:\sum_Sc_S=0,\ \sum_{S,T}c_Sc_T\,d(S,T)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a finite graph metric and the dimension of its boundary equality space. The decisive structure is the natural inclusion filtration of functions on the Kneser graph, which reveals the least adjacency eigenspace and hence the powered-distance threshold.
