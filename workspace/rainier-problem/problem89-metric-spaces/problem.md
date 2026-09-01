# Normalized Math Problem

## LaTeX (Normalized)

Let $G$ be the weighted graph with vertex set
$$
Y=\{\ast,0,1,\ldots,12\}.
$$
For indices modulo $13$, join $i$ to $i+1$ by an edge of length $4$. In addition, join $\ast$ to
$$
0,1,2,5,10
$$
by edges of lengths
$$
7,7,7,13,15,
$$
respectively. Let $d$ be the shortest-path metric on $Y$.

For $p>0$, say that $(Y,d)$ has $p$-negative type if, for every family of real numbers $(c_z)_{z\in Y}$ with $\sum_{z\in Y}c_z=0$,
$$
\sum_{z,w\in Y}c_zc_w\,d(z,w)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(Y,d)\text{ has }p\text{-negative type}\}.
$$

At $p=1$, let $(a_z)_{z\in Y}$ be the unique nonzero zero-sum family normalized by $a_\ast=2$ and satisfying
$$
\sum_{z,w\in Y}a_za_w\,d(z,w)=0.
$$
Define
$$
\tau=\frac14\left.\frac{d}{dp}\right|_{p=1}
\sum_{z,w\in Y}a_za_w\,d(z,w)^p.
$$
Determine the ordered pair $(\wp,\tau)$.

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

The task asks for a supremal negative-type exponent and the first-order transversality of its unique boundary equality direction. Both are controlled by conditional negative definiteness of powers of a finite shortest-path metric.