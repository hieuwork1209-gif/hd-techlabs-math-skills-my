# Normalized Math Problem

## LaTeX (Normalized)

Let $m\ge3$. Form a graph $B_m$ from two disjoint copies of $K_m$ by choosing one distinguished vertex in each copy and joining those two distinguished vertices by a single edge. Let $d$ be the shortest-path metric on $B_m$.

For $p>0$, say that $(B_m,d)$ has $p$-negative type if every real family $(c_x)_{x\in B_m}$ with $\sum_xc_x=0$ satisfies
$$
\sum_{x,y\in B_m}c_xc_y\,d(x,y)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(B_m,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^{B_m}:\sum_xc_x=0,\ \sum_{x,y}c_xc_y\,d(x,y)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of the natural barbell-graph metric and the dimension of its boundary equality space. The graph has two vertex orbits inside each clique, so the decisive step is a symmetry decomposition of the powered-distance quadratic form into competing even and odd modes.
