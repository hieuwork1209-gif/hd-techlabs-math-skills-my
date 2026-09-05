# Normalized Math Problem

## LaTeX (Normalized)

For $|s|<\frac12$, let $G_s$ be the weighted graph with vertex set
$$
Y=\{\ast,0,1,\ldots,12\}.
$$
For indices modulo $13$, join $i$ to $i+1$ by an edge of length $4$. Put
$$
h(s)=\frac{29s^2+7s|s|}{104}.
$$
Join $\ast$ to $0,1,2,5,10$ by edges of lengths
$$
7+h(s),\ 7+h(s),\ 7+h(s),\ 13+h(s),\ 15+h(s),
$$
respectively. Finally add chords $\{0,7\}$ and $\{3,8\}$ of lengths $24+s$ and $20-s$, respectively. Let $d_s$ be the shortest-path metric on $Y$.

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
\tau=\frac14\left.\frac{d}{dp}\right|_{p=1}\sum_{z,w\in Y}a_za_w\,d_0(z,w)^p,
$$
$$
\beta_-=\tau\,\wp'''(0^-),\qquad \beta_+=\tau\,\wp'''(0^+),
$$
where the third derivatives are taken one-sided. Determine the ordered triple $(\wp(0),\beta_-,\beta_+)$.

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

The problem studies the supremal negative-type exponent of a finite shortest-path metric across two different one-sided geodesic regimes, with a coupled spoke perturbation that cancels the quadratic eigenvalue splitting. The key objects are conditional negative definiteness and third-order one-sided perturbation of a simple boundary eigenvalue.
