# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge5$, real $a>0$, and $r\in\{1,2\}$, define
$$
S_r(N,a)=\sum_{k=0}^{N}\frac{(-1)^k\binom Nk}{(k+a)^r},
\qquad T_r(n,a)=\sum_{q=1}^3e^{q-1}S_r(n^q,a).
$$
Put $L=\log n$, $t_n=n^{-1/2}$, and
$$
m_{j,n}=\lfloor jn^{5/2}\rfloor\qquad(j=1,2,3),
$$
$$
b_{1,n}=\frac{27-5t_n}{19},\qquad
b_{2,n}=\frac{-9+10t_n}{19},\qquad
b_{3,n}=\frac{1-5t_n}{19}.
$$
Define
$$
U_r(n,a)=S_r(n,a)+eS_r(n^2,a)
+e^2\sum_{j=1}^3b_{j,n}S_r(n^3+m_{j,n},a).
$$
For all sufficiently large $n$, let $a_n>0$ be the unique solution satisfying
$$
|a_nL-1|<\frac1{10}
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
\lim_{n\to\infty}n^{3/2}L\,(a_nL-1).
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

The determinant compares a base Beta-moment column with a signed three-cutoff stencil. Its coefficients cancel the leading second shift moment, so the root is selected by a coupled second/third-moment correction at a new mesoscopic scale.
