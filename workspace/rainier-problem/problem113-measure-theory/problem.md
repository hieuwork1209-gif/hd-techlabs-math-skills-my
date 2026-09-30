# Normalized Math Problem

## LaTeX (Normalized)

Let $\mu$ be a Borel probability measure on $[0,1]$ such that
$$
\int_0^1 x\,d\mu(x)=\frac{1}{3},
\qquad
\int_0^1 x^2\,d\mu(x)=\frac{1}{5},
\qquad
\int_0^1 x^3\,d\mu(x)=\frac{1}{7}.
$$

Determine the maximum possible value of
$$
\mu\left(\left[\frac{1}{2},1\right]\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Measure theory |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for a sharp extremal value over Borel probability measures subject to finitely many moment constraints. The decisive work is to build a polynomial majorant for an indicator function, match it to an atomic extremal measure, and use equality in the integral bound to close the extremal case. Therefore Analysis / Measure theory is the primary classification. Finite-dimensional optimization appears in the moment equations, but the requested object is an extremum over measures.
