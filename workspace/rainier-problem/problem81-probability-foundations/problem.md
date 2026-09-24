# Normalized Math Problem

## LaTeX (Normalized)

Consider the discrete-time random walk on an unknown connected tree with vertex set $\{1,2,3,4\}$. Each edge $\{i,j\}$ has a positive conductance $c_{ij}=c_{ji}$, and from vertex $i$ the walk moves to a neighbor $j$ with probability
$$
P(i,j)=\frac{c_{ij}}{\sum_{k\sim i}c_{ik}}.
$$

For $i\neq j$, let
$$
T_j=\inf\{n\geq0:X_n=j\}
$$
and define the commute time
$$
C_{ij}=\mathbb E_iT_j+\mathbb E_jT_i.
$$

Suppose
$$
C_{12}=4,
\qquad
C_{23}=6,
\qquad
C_{34}=12,
$$
$$
C_{13}=10,
\qquad
C_{24}=18.
$$

For a walk started at $X_0=2$, let
$$
\tau_{\rm cov}
=
\inf\{n\geq0:\{X_0,X_1,\ldots,X_n\}=\{1,2,3,4\}\}.
$$

Determine exactly
$$
\left(C_{14},\mathbb E_2\tau_{\rm cov},\operatorname{Var}_2(\tau_{\rm cov})\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Exact computation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem is an inverse question for a reversible random walk on a weighted tree. The commute data determine the hidden tree metric and conductance ratios, after which endpoint-first decomposition and strong-Markov moment calculations determine the mean and variance of the cover time. Thus Probability and Statistics -> Probability foundations is primary.
