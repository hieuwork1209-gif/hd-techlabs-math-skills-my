# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$ and real $a>0$, define
$$
T_r(n,a)=\sum_{q=1}^3 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}\qquad(1\le r\le5),
$$
$$
\Delta_n=\det\!\left[(i+j)!T_{i+j+1}\right]_{i,j=0}^2,
\quad \Lambda_n=2T_1T_3-T_2^2,
$$
$$
\Omega_n=-6T_1^2T_4+6T_1T_2T_3-2T_2^3,
$$
$$
\Psi_n=24T_1^3T_5-24T_1^2T_2T_4-12T_1^2T_3^2
+24T_1T_2^2T_3-6T_2^4,
$$
where all $T_r$ are evaluated at $(n,a)$.

For all sufficiently large $n$, let $a_n>0$ be the unique solution with
$$
|a_n\log n-1|<(\log n)^{-3/2}
$$
of
$$
81T_1\Delta_n+2238(\log n)^4T_1^2\Lambda_n
-324(\log n)^3T_1\Omega_n-135(\log n)^2\Psi_n
-1206(\log n)^2\Lambda_n^2-1454(\log n)^6T_1^4=0.
$$
Determine
$$
\lim_{n\to\infty}(\log n)^2(a_n\log n-1).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Determinants |
| **Problem Type** | Parameter identification |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The Hankel determinant, its log-derivative invariants, and a quadratic minor term are tuned to a stationary triple degeneracy. The nearby root is then selected by a mixed displacement--Gamma correction rather than by the leading cubic alone.
