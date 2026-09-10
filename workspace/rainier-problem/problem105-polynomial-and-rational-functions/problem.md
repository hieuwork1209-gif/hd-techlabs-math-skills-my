# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
V=\mathbb F_2^6\oplus\mathbb F_2^6
$$
and define the quadratic form
$$
q(x,y)=x^Ty.
$$
Call a $6$-dimensional subspace of $V$ a generator if $q$ vanishes identically on it. A partial spread is a set of generators in which every two distinct members intersect only in $\{0\}$.

Let
$$
X=\mathbb F_2^6\oplus0,
\qquad
Y=0\oplus\mathbb F_2^6,
$$
and let $G$ be the subgroup of linear isometries of $(V,q)$ that fixes $X$ and $Y$ individually.

Determine the exact number of $G$-orbits on the $5$-element partial spreads that contain both $X$ and $Y$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Discrete Mathematics and Combinatorics |
| **Sub-domain** | Design theory and finite geometry |
| **Problem Type** | Exhaustive enumeration |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for an isometry classification of partial spreads in the hyperbolic orthogonal space $Q^+(11,2)$. Generators complementary to the two fixed coordinate generators correspond to nondegenerate alternating forms, while the stabilizer of $X$ and $Y$ acts by congruence. The count therefore requires a genuine orbit classification of compatible triples rather than only a labeled clique count.
