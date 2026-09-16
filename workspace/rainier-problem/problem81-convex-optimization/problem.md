# Normalized Math Problem

## LaTeX (Normalized)

For real $a,b$, let $C(a,b)$ be the symmetric circulant $6\times6$ matrix whose first row is
$$
\left(1,\frac12,a,b,a,\frac12\right).
$$
Let $\mathcal F$ be the set of all real symmetric positive semidefinite matrices $G=(g_{ij})_{1\le i,j\le6}$ satisfying
$$
g_{ii}=1\quad(1\le i\le6),
$$
$$
g_{12}=g_{23}=g_{34}=g_{45}=g_{56}=g_{61}=\frac12.
$$
Determine the ordered triple $(D,a,b)$ such that $D$ is the largest possible value of $\det G$ over $G\in\mathcal F$ and $C(a,b)$ is the unique maximizing matrix.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Convex optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem is a maximum-determinant positive-semidefinite matrix completion problem with affine correlation constraints. The key task is to identify the unique optimizer using concavity and first-order optimality, then evaluate its determinant exactly. Thus Optimization and Numerical Mathematics -> Convex optimization is the direct classification.
