# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be a random variable supported on $[0,1]$ such that
$$
\mathbb E[X^k]=\frac1{k+1}
\qquad(k=1,2,\ldots,8).
$$
Among all probability laws on $[0,1]$ satisfying these eight moment constraints, determine exactly
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

The problem is an extremal question over probability laws subject to finitely many moment constraints on a compact interval. Its core is a truncated moment problem: one must construct a sharp polynomial majorant for the target expectation and prove attainability and uniqueness of the extremal distribution. Thus Probability and Statistics -> Probability foundations is primary, with polynomial and quadrature arguments serving as subordinate tools.
