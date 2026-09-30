# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
F(x,y,z)=\frac{1}{1-x-y-z-xyz},
$$
and define
$$
a_n=[x^ny^nz^n]F(x,y,z).
$$
Let $q>3$ be the unique real root of
$$
q^3-3q^2-1=0.
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

This problem asks for the sharp diagonal asymptotic constant of a rational multivariate generating function. The main work starts from exact diagonal coefficient extraction and then analyzes the resulting coefficient sum to obtain its saddle and Gaussian prefactor, so Discrete Mathematics and Combinatorics / Generating functions is the primary classification. Algebra, Functions, and Trigonometry / Polynomial and rational functions is a close secondary fit because the source is rational, but the requested object is a diagonal coefficient asymptotic rather than an algebraic property of the rational function itself.
