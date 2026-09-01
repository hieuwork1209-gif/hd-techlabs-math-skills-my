# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$, $a>0$, and $b\in\mathbb R$, define
$$
T_r(n,a,b)=\sum_{q=1}^3e^{b(q-1)}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}\qquad(1\le r\le5),
$$
$$
\Delta=\det\!\left[(i+j)!T_{i+j+1}\right]_{i,j=0}^2,
\qquad \Lambda=2T_1T_3-T_2^2,
$$
and
$$
\Omega=-6T_1^2T_4+6T_1T_2T_3-2T_2^3,
$$
where all $T_r$ in $\Delta,\Lambda,\Omega$ are evaluated at $(n,a,b)$.

For all sufficiently large $n$, let $(a_n,b_n)$ be the unique pair satisfying
$$
|a_n\log n-1|<\frac1{100},\qquad |b_n-1|<\frac1{100},\qquad a_n\log n>b_n,
$$
and
$$
3\Lambda=5(\log n)^2T_1^2,
$$
$$
27\Delta-108(\log n)^3\Omega=598(\log n)^6T_1^3.
$$
Determine
$$
\lim_{n\to\infty}(\log n)\bigl(a_n\log n-b_n\bigr).
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

The problem couples two scale-free Hankel determinant invariants. Their leading Jacobian is singular in the relative-scale direction, so the selected branch is determined only after a quadratic splitting of the determinant constraints.