# Normalized Math Problem

## LaTeX (Normalized)

Let $\Gamma$ be the Cayley graph on $A_5$ in which two vertices $\sigma,\tau$ are adjacent exactly when $\sigma^{-1}\tau$ is a $3$-cycle. Let $d$ be the shortest-path metric on $\Gamma$.

For $p>0$, say that $(A_5,d)$ has $p$-negative type if every real family $(c_\sigma)_{\sigma\in A_5}$ with $\sum_\sigma c_\sigma=0$ satisfies
$$
\sum_{\sigma,\tau\in A_5}c_\sigma c_\tau\,d(\sigma,\tau)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(A_5,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^{A_5}:\sum_\sigma c_\sigma=0,\ \sum_{\sigma,\tau}c_\sigma c_\tau\,d(\sigma,\tau)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a natural finite Cayley graph metric and the dimension of its boundary equality space. The key invariant is the spectrum of the normal Cayley adjacency operator, obtained from the representation theory of $A_5$.
