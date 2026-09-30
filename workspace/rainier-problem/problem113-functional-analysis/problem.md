# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
V=
\left\{
u\in H_0^1(0,1):
\int_0^1xu(x)\,dx=0,
\quad
\int_0^1x^3u(x)\,dx=0
\right\}.
$$

Determine the sharp constant $C$ such that
$$
\left|u\left(\frac{1}{2}\right)\right|^2
\leq
C
\int_0^1u'(x)^2\,dx
$$
for every $u\in V$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Functional analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the exact norm of a point-evaluation functional on a closed codimension-two subspace of the Dirichlet energy space. The decisive structure is the interaction between Riesz representation, orthogonal projection, and the two moment constraints, so Analysis / Functional analysis is the primary classification. Calculus / Integration is secondary because the required moment and Green-kernel integrals are explicit once the Hilbert-space reduction is found.
