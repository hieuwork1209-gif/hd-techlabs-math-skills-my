# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$, real $a>0$, and $r\in\{1,2\}$, define
$$
T_r(n,a)=\sum_{q=1}^3 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r},
$$
and
$$
U_r(n,a)=\sum_{q=1}^2 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}
+e^2\sum_{k=0}^{n^3+1}
\frac{(-1)^k\binom{n^3+1}{k}}{(k+a)^r}.
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
\lim_{n\to\infty}n\log n\,\bigl(a_n\log n-1\bigr).
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

The determinant compares two nearly identical Beta-moment columns. Their continuum asymptotics are tangent at the limiting root, so the parameter shift is determined only by the first finite-$n$ correction rather than by any fixed-order expansion in $1/\log n$.
