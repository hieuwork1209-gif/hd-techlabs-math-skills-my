# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$, real $a>0$, and $r\in\{1,2\}$, define
$$
S_r(N,a)=\sum_{k=0}^{N}\frac{(-1)^k\binom Nk}{(k+a)^r},
\qquad
T_r(n,a)=\sum_{q=1}^3 e^{q-1}S_r(n^q,a).
$$
Let
$$
m_n=\left\lfloor\frac{n^2}{3}\right\rfloor,
$$
and define
$$
U_r(n,a)=S_r(n,a)+eS_r(n^2,a)
+e^2\left(\frac34S_r(n^3+m_n,a)+\frac14S_r(n^3+n^2,a)\right).
$$
For all sufficiently large $n$, let $a_n>0$ be the unique solution satisfying
$$
\left|a_n\log n-1\right|<\frac1{10}
$$
of
$$
\det\!\begin{pmatrix}
T_1(n,a_n)&U_1(n,a_n)\\
T_2(n,a_n)&U_2(n,a_n)
\end{pmatrix}=0.
$$
Determine
$$
\lim_{n\to\infty}n(\log n)^2\bigl(a_n\log n-1\bigr).
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

The determinant compares a base Beta-moment column with a two-cutoff mesoscopic mixture. The first finite-size cancellation depends on a hidden ratio of shift moments rather than on a single effective cutoff, while the root is still selected by the next logarithmic correction.
