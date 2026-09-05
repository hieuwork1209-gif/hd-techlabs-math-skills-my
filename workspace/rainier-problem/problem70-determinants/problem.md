# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$, real $a>0$, and $r\in\{1,2\}$, define
$$
T_r(n,a)=\sum_{q=1}^3 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}.
$$
Let
$$
m_n=\left\lfloor\frac{2n^2}{3}\right\rfloor,
$$
and define
$$
U_r(n,a)=\sum_{q=1}^2 e^{q-1}\sum_{k=0}^{n^q}
\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r}
+e^2\sum_{k=0}^{n^3+m_n}
\frac{(-1)^k\binom{n^3+m_n}{k}}{(k+a)^r}.
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

The determinant compares a base Beta-moment column with a mesoscopically shifted cutoff column. The shift $m_n\asymp n^2$ is tuned so its first finite-size effect cancels the $q=1$ Beta bias, forcing the root to be selected by a smaller competing asymptotic scale.