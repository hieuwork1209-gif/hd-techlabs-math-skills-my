# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\mathcal P=\left\{x^4+x^3+ax^2+bx+c:a,b,c\in\mathbb R\right\},
$$
and define
$$
E=\inf_{p\in\mathcal P}\max_{-1\leq x\leq1}|p(x)|.
$$
Determine the primitive irreducible polynomial $P(T)\in\mathbb Z[T]$ with positive leading coefficient such that
$$
P(E)=0.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Approximation theory |
| **Problem Type** | Exact computation |
| **Answer Type** | Polynomial or rational function |

---

## Domain Explanation

This problem asks for the exact algebraic invariant of a constrained best uniform approximation problem: the leading quartic coefficients are fixed, the remaining coefficients are optimized in the sup norm on an interval, and the optimal error is then identified algebraically. The primary subject is therefore Optimization and Numerical Mathematics and Approximation theory. Polynomial elimination and finite-field irreducibility are secondary tools used after the minimax structure determines the extremal error.
