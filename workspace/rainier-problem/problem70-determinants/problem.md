# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$ and real $a>0$, define
$$
T_r(n,a)=\sum_{q=1}^3 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}
\qquad(1\le r\le5),
$$
$$
\Delta_n(a)=\det\!\left[(i+j)!\,T_{i+j+1}(n,a)\right]_{i,j=0}^{2},
$$
$$
\Lambda_n(a)=2T_1T_3-T_2^2,
\qquad
\Omega_n(a)=-6T_1^2T_4+6T_1T_2T_3-2T_2^3,
$$
where the $T_r$ in $\Lambda_n,\Omega_n$ are evaluated at $(n,a)$.

For all sufficiently large $n$, let $a_n>0$ be the larger of the two solutions satisfying
$$
\left|a_n\log n-1\right|<\frac1{\log n}
$$
of
$$
54\Delta_n(a_n)-1188(\log n)^4T_1\Lambda_n
+189(\log n)^3\Omega_n
+1594(\log n)^6T_1^3=0,
$$
where $T_1,\Lambda_n,\Omega_n$ are evaluated at $(n,a_n)$.
Determine
$$
\lim_{n\to\infty}(\log n)^{3/2}\bigl(a_n\log n-1\bigr).
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

The Hankel determinant and its derivative invariants are tuned so the normalized limiting equation has a degenerate root. Resolving the larger nearby branch requires combining the determinant identity with the next asymptotic perturbation.
