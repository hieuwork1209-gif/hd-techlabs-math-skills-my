# Normalized Math Problem

## LaTeX (Normalized)

For $|s|<\frac12$, let $G_s$ be the weighted graph with vertex set
$$
Y=\{\ast,0,1,\ldots,12\}.
$$
For indices modulo $13$, join $i$ to $i+1$ by an edge of length $4$. Join $\ast$ to $0,1,2,5,10$ by edges of lengths
$$
7,\ 7,\ 7,\ 13,\ 15,
$$
respectively. Finally add chords $\{7,9\}$ and $\{3,8\}$ of lengths $8+s$ and $20-s$, respectively. Let $d_s$ be the shortest-path metric on $Y$.

For $p>0$, say that $(Y,d_s)$ has $p$-negative type if every real family $(c_z)_{z\in Y}$ with $\sum_zc_z=0$ satisfies
$$
\sum_{z,w\in Y}c_zc_w\,d_s(z,w)^p\leq0.
$$
Let
$$
\wp(s)=\sup\{p>0:(Y,d_s)\text{ has }p\text{-negative type}\}.
$$

At $s=0$ and $p=1$, let $(a_z)_{z\in Y}$ be the unique nonzero zero-sum family normalized by $a_\ast=2$ and satisfying
$$
\sum_{z,w\in Y}a_za_w\,d_0(z,w)=0.
$$
Define
$$
\tau=\frac14\left.\frac{d}{dp}\right|_{p=1}
\sum_{z,w\in Y}a_za_w\,d_0(z,w)^p,
$$
$$
\alpha_-=\tau\,\wp''(0^-),
\qquad
\alpha_+=\tau\,\wp''(0^+),
$$
where the second derivatives are taken one-sided. Determine the ordered quadruple $(\wp(0),\tau,\alpha_-,\alpha_+)$.

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

The problem studies the supremal negative-type exponent of a finite shortest-path metric at a point where two tied geodesics split into different one-sided regimes. The key objects are conditional negative definiteness, shortest-path regime changes, and one-sided perturbation of a simple boundary eigenvalue.
