# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
F(x,y,z)=\frac{1}{1-x^2-y^2-z^2-xyz},
$$
and define
$$
a_n=[x^ny^nz^n]F(x,y,z).
$$
Let $q>1$ be the unique real root of
$$
q^3-3q-1=0.
$$

Determine exactly
$$
\lim_{n\to\infty}\frac{na_n}{q^{3n}}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Discrete Mathematics and Combinatorics |
| **Sub-domain** | Generating functions |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem asks for the sharp diagonal asymptotic constant of a symmetric rational multivariate generating function. Exact coefficient extraction produces a parity-restricted sum, and the asymptotic evaluation requires both its saddle and the spacing of the admissible lattice. Therefore Discrete Mathematics and Combinatorics / Generating functions is the primary classification. Algebra, Functions, and Trigonometry / Polynomial and rational functions is secondary because the rational function is the source of the coefficient sequence rather than the final algebraic object being studied.
