# Normalized Math Problem

## LaTeX (Normalized)

For $|s|<1$, let $G_s$ be the weighted graph with vertex set
$$
Y=\{\ast,0,1,\ldots,12\}.
$$
For indices modulo $13$, join $i$ to $i+1$ by an edge of length $4$. In addition, join $\ast$ to $0,1,2,5,10$ by edges of lengths
$$
7,\ 7,\ 7-s,\ 13,\ 15+s,
$$
respectively. Let $d_s$ be the shortest-path metric on $Y$.

For $p>0$, say that $(Y,d_s)$ has $p$-negative type if every real family $(c_z)_{z\in Y}$ with $\sum_z c_z=0$ satisfies
$$
\sum_{z,w\in Y}c_zc_w\,d_s(z,w)^p\le0.
$$
Let
$$
\wp(s)=\sup\{p>0:(Y,d_s)\text{ has }p\text{-negative type}\}.
$$

At $s=0$ and $p=1$, let $(a_z)$ be the unique nonzero zero-sum family normalized by $a_\ast=2$ and satisfying
$$
\sum_{z,w\in Y}a_za_w\,d_0(z,w)=0.
$$
Define
$$
\tau=\frac14\left.\frac{d}{dp}\right|_{p=1}
\sum_{z,w\in Y}a_za_w\,d_0(z,w)^p,
\qquad
\kappa=\tau\,\wp''(0).
$$
Determine the ordered triple $(\wp(0),\tau,\kappa)$.

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

The problem concerns the supremal negative-type exponent of a finite metric and its second-order response under a coupled perturbation of the shortest-path metric. The key objects are conditional negative definiteness and the perturbation of the unique critical equality direction.