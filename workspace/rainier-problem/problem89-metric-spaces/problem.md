# Normalized Math Problem

## LaTeX (Normalized)

Let $T$ be the complete rooted binary tree of height $3$: its vertices are the binary words of lengths $0,1,2,3$, and a word is joined to each one-letter extension. Let $d$ be the shortest-path metric on the $15$ vertices of $T$.

For $p>0$, say that $(T,d)$ has $p$-negative type if every real family $(c_x)_{x\in T}$ with $\sum_xc_x=0$ satisfies
$$
\sum_{x,y\in T}c_xc_y\,d(x,y)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(T,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^T:\sum_xc_x=0,\ \sum_{x,y\in T}c_xc_y\,d(x,y)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a canonical finite tree metric and the dimension of its boundary equality space. The decisive structure is the hierarchical decomposition induced by the independent child-swaps of the rooted binary tree.
