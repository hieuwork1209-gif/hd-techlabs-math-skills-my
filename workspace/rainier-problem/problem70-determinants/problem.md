# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$ and real $a>0$, define
$$
T_r(n,a)=\sum_{q=1}^3 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}
\qquad(1\le r\le5)
$$
and
$$
\Delta_n(a)=\det\!\left[(i+j)!\,T_{i+j+1}(n,a)\right]_{i,j=0}^{2}.
$$
For all sufficiently large $n$, let $a_n>0$ be the unique solution with
$$
\left|a_n\log n-1\right|<\frac1{10}
$$
of
$$
27\,\Delta_n(a_n)=382\,(\log n)^6\,T_1(n,a_n)^3.
$$
Determine
$$
\lim_{n\to\infty}(\log n)^2\bigl(a_n\log n-1\bigr).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Determinants |
| **Problem Type** | Parameter identification |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem is governed by a scale-free Hankel determinant ratio. The normalization by $T_1^3$ makes the first boundary displacement invisible by translation invariance, so the parameter is selected only by the second-order deformation of the moment determinant.