# Normalized Math Problem

## LaTeX (Normalized)

Let $q\ge5$ be a prime power with $q\equiv1\pmod4$. Let $P(q)$ be the Paley graph on $\mathbb F_q$: distinct vertices $x,y$ are adjacent exactly when $x-y$ is a nonzero square in $\mathbb F_q$. Let $d$ be its shortest-path metric.

For $p>0$, say that $(\mathbb F_q,d)$ has $p$-negative type if every real family $(c_x)_{x\in\mathbb F_q}$ with $\sum_xc_x=0$ satisfies
$$
\sum_{x,y\in\mathbb F_q}c_xc_y\,d(x,y)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(\mathbb F_q,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^{\mathbb F_q}:\sum_xc_x=0,\ \sum_{x,y}c_xc_y\,d(x,y)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a finite graph metric and the dimension of its boundary equality space. The Paley graph's strong regularity makes the threshold a spectral property of the powered distance matrix.
