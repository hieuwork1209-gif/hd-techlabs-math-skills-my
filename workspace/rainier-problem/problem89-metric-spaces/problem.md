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

For $p>0$, say that $(Y,d)$ has $p$-negative type if, for every family of real numbers $(a_z)_{z\in Y}$ with $\sum_{z\in Y}a_z=0$,
$$
\sum_{z,w\in Y}a_za_w\,d(z,w)^p\le0.
$$
Determine
$$
\wp=\sup\{p>0:(Y,d)\text{ has }p\text{-negative type}\}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Metric spaces |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The quantity $\wp$ is a metric-space invariant defined by conditional negative definiteness of powers of the shortest-path metric. The weighted graph is only a compact presentation of the finite metric; the central work is metric negative type, Gram matrices, and convexity rather than graph-theoretic classification.