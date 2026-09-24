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

Determine exactly
$$
\left(C_{14},\mathbb E_1T_4,\operatorname{Var}_1(T_4)\right).
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

The problem is an inverse question for a reversible random walk on a weighted tree. The commute data determine the hidden tree metric and conductance ratios, after which first- and second-moment hitting-time recursions determine the requested mean and variance. Thus Probability and Statistics -> Probability foundations is primary.
