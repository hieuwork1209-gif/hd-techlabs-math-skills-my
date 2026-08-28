# Normalized Math Problem

## LaTeX (Normalized)

Fix an odd prime $p$. For a real number $X\ge 2$, let $T_p(X)$ count the triples of integers $(a,b,c)$ satisfying
$$
1\le a<b<c\le X,
\qquad
a+c=2b,
\qquad
ac\ \text{is a perfect square},
\qquad
\gcd(abc,p)=1.
$$
There is a constant $C_p>0$, depending only on $p$, with
$$
T_p(X)\sim C_p\,X\log X
\qquad(X\to\infty).
$$
Determine $C_p$ in closed form.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Analytic number theory |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem involves an asymptotic count of integer arithmetic progressions subject to a perfect-square condition and a coprimality restriction at a fixed prime, and asks for the exact leading constant. These are central topics of Number Theory, specifically Analytic number theory, because the solution depends on primitive parametrization, local arithmetic densities, an Euler product, and partial summation. The problem also uses parity casework and elementary lattice-point counting, which have a combinatorial aspect. However, those are supporting devices; the main task is to derive an arithmetic asymptotic constant from prime-by-prime density information, so Analytic number theory is the more appropriate classification.
