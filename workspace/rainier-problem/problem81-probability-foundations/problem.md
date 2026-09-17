# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be a random variable supported on $[0,1]$ such that
$$
\mathbb E[X^k]=\frac1{k+1}
\qquad(k=1,2,\ldots,8),
$$
and
$$
\mathbb E[X^9]=\frac{35281}{352800}.
$$
Among all probability laws on $[0,1]$ satisfying these nine moment constraints, determine exactly
$$
M=\max \mathbb E\!\left[\frac1{2-X}\right].
$$
Also determine whether the maximizing law is unique.

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Probability and Statistics |
| Sub-domain | Probability foundations |
| Problem Type | Optimization |
| Answer Type | Exact scalar |

---

## Domain Explanation

The problem is an extremal question over probability laws subject to a truncated sequence of moments on a compact interval. The ninth moment is a deliberate perturbation of the uniform moment sequence, so the extremizer is no longer the standard Radau representation from the eight-moment problem; one must derive a sharp degree-$9$ polynomial majorant, construct the corresponding positive six-node quadrature, and prove uniqueness from the equality set. Thus Probability and Statistics -> Probability foundations is primary, with polynomial and quadrature arguments serving as subordinate tools.
