# Normalized Math Problem

## LaTeX (Normalized)

For $A,B>0$, let
$$
R_{A,B}(x)=\frac{Ax^2}{x^2+B},
$$
and define
$$
E=\inf_{A,B>0}\max_{0\leq x\leq1}\left|x-R_{A,B}(x)\right|.
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

This problem asks for the exact algebraic invariant of a nonlinear best uniform rational approximation problem. The approximating family has a free numerator scale and a free positive denominator scale, so the optimal error must be determined together with the rational contact geometry rather than by linear polynomial equioscillation alone. The primary subject is therefore Optimization and Numerical Mathematics and Approximation theory; algebraic elimination and finite-field irreducibility are secondary tools used after the minimax structure is established.
