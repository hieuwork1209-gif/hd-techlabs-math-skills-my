# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
K=\left\{x\in\mathbb{R}^4:
|x_i|\leq1\ (1\leq i\leq4),\quad
|x_1+x_2+x_3+x_4|\leq1,\quad
\left|\frac{x_1+x_2+x_3}{3}-x_4\right|\leq1
\right\}.
$$
Let $B_4=\{x\in\mathbb{R}^4:\|x\|_2\leq1\}$.

Among all ellipsoids $E\subset K$, determine the exact maximum value of
$$
\left(\frac{\operatorname{vol}(E)}{\operatorname{vol}(B_4)}\right)^2.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Topology and Geometry |
| **Sub-domain** | Convex geometry |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the maximal-volume ellipsoid contained in a centrally symmetric convex body and for its exact volume ratio, which is a standard extremal question in Topology and Geometry and Convex geometry. The solution uses symmetry averaging, support functions, positive definite shape matrices, and determinant optimization; these linear-algebraic tools are subordinate to the convex-geometric containment and volume problem.
