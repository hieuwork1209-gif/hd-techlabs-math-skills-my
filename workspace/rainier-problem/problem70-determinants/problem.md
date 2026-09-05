# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge5$, real $a>0$, and $r\in\{1,2\}$, define
$$
S_r(N,a)=\sum_{k=0}^{N}\frac{(-1)^k\binom Nk}{(k+a)^r},
\qquad
T_r(n,a)=\sum_{q=1}^3 e^{q-1}S_r(n^q,a).
$$
Put $L=\log n$ and
$$
p_n=\frac34-\frac{9}{8L},\qquad
m_n=\left\lfloor\frac{n^2}{3}\right\rfloor.
$$
Define
$$
U_r(n,a)=S_r(n,a)+eS_r(n^2,a)
+e^2\left(p_nS_r(n^3+m_n,a)+(1-p_n)S_r(n^3+n^2,a)\right).
$$
For all sufficiently large $n$, let $a_n>0$ be the unique solution satisfying
$$
\left|a_nL-1\right|<\frac1{10}
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
\lim_{n\to\infty}nL^3\bigl(a_nL-1\bigr).
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

The determinant compares a base Beta-moment column with a logarithmically varying two-cutoff mixture. The mixture is tuned so two finite-size corrections cancel, forcing the root to be selected by the variation of a hidden shift-moment ratio at the next asymptotic scale.
