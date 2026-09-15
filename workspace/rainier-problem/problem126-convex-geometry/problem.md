# Normalized Math Problem

## LaTeX (Normalized)

For $1\leq h\leq2$, let
$$
K_h=\left\{x\in\mathbb{R}^4:
|x_i|\leq1\ (1\leq i\leq4),\quad
|x_1+x_2+x_3+x_4|\leq h,\quad
\left|\frac{x_1+x_2+x_3}{3}-x_4\right|\leq h
\right\}.
$$
For each $h$, let $E_h$ be the centered ellipsoid of maximum volume contained in $K_h$.

Call one of the following four facet families tangent at $h$ if $E_h$ meets a facet in that family:

- $C_{123}$: the three pairs $|x_i|=1$ for $1\leq i\leq3$;
- $C_4$: the pair $|x_4|=1$;
- $S_+$: the pair $|x_1+x_2+x_3+x_4|=h$;
- $S_-$: the pair $\left|\frac{x_1+x_2+x_3}{3}-x_4\right|=h$.

Let $\mathcal T(h)$ be the set of tangent facet families. Determine all $h\in(1,2)$ at which $\mathcal T(h)$ is not locally constant.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Topology and Geometry |
| **Sub-domain** | Convex geometry |
| **Problem Type** | Parameter identification |
| **Answer Type** | Set or multiset of objects |

---

## Domain Explanation

This problem studies how the John ellipsoid of a one-parameter family of centrally symmetric convex bodies changes its facet-contact pattern. Determining the transition parameters requires convex-geometric containment, symmetry reduction, and active-set analysis of the maximal-volume ellipsoid, so the primary classification is Topology and Geometry and Convex geometry. Linear-algebraic determinant calculations are auxiliary to that geometric optimization.
