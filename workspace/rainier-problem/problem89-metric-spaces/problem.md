# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be the set of $3$-dimensional subspaces of $\mathbb F_2^6$. Let $G$ be the graph on $X$ in which distinct subspaces $U,W$ are adjacent exactly when
$$
\dim(U\cap W)=2.
$$
Let $d$ be the shortest-path metric on $G$.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_U)_{U\in X}$ with $\sum_Uc_U=0$ satisfies
$$
\sum_{U,W\in X}c_Uc_W\,d(U,W)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^X:\sum_Uc_U=0,\ \sum_{U,W}c_Uc_W\,d(U,W)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of the Grassmann graph metric on $3$-subspaces of $\mathbb F_2^6$ and the dimension of its boundary equality space. The key structure is the graph's distance-regular recurrence, which diagonalizes the powered distance matrix into competing spectral modes.
