# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
V=\mathbb{F}_2^3\setminus\{0\}.
$$
Form the bipartite graph with point-vertices $P_v$ and line-vertices $L_u$, indexed by $u,v\in V$, where
$$
P_v\sim L_u\iff u\cdot v=0.
$$
Let $X$ be its $14$-vertex set and give $X$ the shortest-path metric $d$.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_x)_{x\in X}$ with $\sum_xc_x=0$ satisfies
$$
\sum_{x,y\in X}c_xc_y d(x,y)^p\leq0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\},
$$
and define
$$
E=\left\{c\in\mathbb{R}^{X}:\sum_xc_x=0,\ 
\sum_{x,y\in X}c_xc_y d(x,y)^{\wp}=0\right\}.
$$

For a subspace $L\leq E$, write
$$
\operatorname{supp}(L)=\{x\in X:\text{some }c\in L\text{ has }c_x\neq0\}.
$$
For $1\leq r\leq\dim E$, define
$$
d_r=\min_{\substack{L\leq E\\ \dim L=r}}|\operatorname{supp}(L)|.
$$

Determine
$$
\left(\wp,\dim E,(d_1,\ldots,d_{\dim E})\right).
$$

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

The primary object is the shortest-path metric on the Heawood graph, and the problem asks for its supremal negative type together with the generalized support hierarchy of the critical equality space, so Analysis / Metric spaces is the natural primary classification. Spectral graph methods identify the equality space, while the decisive support bounds come from the self-dual incidence geometry of the Fano plane.
