# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
X=\mathbb F_2^8/\langle\mathbf1\rangle,
$$
where $\mathbf1=(1,\ldots,1)$. Thus a point of $X$ is an antipodal pair
$$
[x]=\{x,x+\mathbf1\}
$$
of vertices of the $8$-dimensional Hamming cube. Define
$$
d([x],[y])=\min\{\operatorname{wt}(x-y),\ 8-\operatorname{wt}(x-y)\},
$$
where $\operatorname{wt}$ denotes Hamming weight.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_u)_{u\in X}$ with $\sum_uc_u=0$ satisfies
$$
\sum_{u,v\in X}c_uc_v\,d(u,v)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^X:\sum_uc_u=0,\ \sum_{u,v}c_uc_v\,d(u,v)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of the antipodal quotient of the $8$-cube with its quotient Hamming metric, together with the dimension of the boundary equality space. The key structure is the Fourier decomposition of the quotient, whose characters are indexed by even-weight binary vectors.
