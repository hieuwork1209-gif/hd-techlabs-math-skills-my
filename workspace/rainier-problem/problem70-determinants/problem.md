# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge5$, real $a>0$, $b\in\mathbb R$, and $r\in\{1,2,3\}$, define
$$
S_r(N,a)=\sum_{k=0}^{N}\frac{(-1)^k\binom Nk}{(k+a)^r},
\qquad
T_r(n,a,b)=\sum_{q=1}^3e^{b(q-1)}S_r(n^q,a).
$$
Put $L=\log n$, $t=n^{-1/2}$, $m_j=\lfloor jn^{5/2}\rfloor$, and
$$
b_1=\frac{27-5t}{19},\qquad b_2=\frac{-9+10t}{19},\qquad b_3=\frac{1-5t}{19}.
$$
Define
$$
U_r(n,a,b)=S_r(n,a)+e^bS_r(n^2,a)+e^{2b}\sum_{j=1}^3b_jS_r(n^3+m_j,a),
\qquad W_r=T_r-U_r,
$$
$$
H_n(a,b)=\frac1L\left(\frac{T_2}{T_1}-\frac{W_2}{W_1}\right),
$$
$$
K_n(a,b)=\frac1{L^2}\left(\frac{2W_3}{W_1}-\frac{W_2^2}{W_1^2}
-\frac{2T_3}{T_1}+\frac{T_2^2}{T_1^2}\right),
$$
where all $T_r,U_r,W_r$ are evaluated at $(n,a,b)$.

For all sufficiently large $n$, let $(a_n,b_n)$ be the unique pair satisfying
$$
|a_nL-1|<\frac1{10},\qquad |b_n-1|<\frac1{10},\qquad a_nL<b_n,
$$
and
$$
H_n(a_n,b_n)=0,
$$
$$
K_n(a_n,b_n)+\frac53-\frac45(b_n-1)+\frac{21}{125}(b_n-1)^2=0.
$$
Determine
$$
\lim_{n\to\infty}(nL)^{1/3}(b_n-a_nL).
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

The first normalized determinant ratio selects a stationary curve in two coupled scale parameters. Along that curve the curvature condition has a singular Jacobian and loses both its linear and quadratic relative-scale terms, so the selected branch is determined by a finite-size cubic splitting.