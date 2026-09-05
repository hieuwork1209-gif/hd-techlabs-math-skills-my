# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge4$. Let $\Gamma_n$ be the incidence graph of the complete graph $K_n$: its vertex set is
$$
[n]\sqcup\binom{[n]}2,
$$
and $i\in[n]$ is adjacent to $e\in\binom{[n]}2$ exactly when $i\in e$. Let $d$ be the shortest-path metric on $\Gamma_n$.

For $p>0$, say that $(\Gamma_n,d)$ has $p$-negative type if every real family $(c_x)$ with $\sum_xc_x=0$ satisfies
$$
\sum_{x,y}c_xc_y\,d(x,y)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(\Gamma_n,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c:\sum_xc_x=0,\ \sum_{x,y}c_xc_y\,d(x,y)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a natural finite incidence-graph metric and the dimension of its boundary equality space. The decisive structure is a hidden squared-Euclidean representation of graph distance by the vectors attached to vertices and edges of $K_n$.
