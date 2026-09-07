# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge5$, real $a>0$, and $r\in\{1,2,3\}$, define
$$
S_r(N,a)=\sum_{k=0}^{N}\frac{(-1)^k\binom Nk}{(k+a)^r},\qquad
T_r(n,a)=\sum_{q=1}^3e^{q-1}S_r(n^q,a).
$$
Put $L=\log n$, $t=n^{-1/2}$, $m_j=\lfloor jn^{5/2}\rfloor$, and
$$
b_1=\frac{27-5t}{19},\qquad b_2=\frac{-9+10t}{19},\qquad b_3=\frac{1-5t}{19}.
$$
Define
$$
U_r(n,a)=S_r(n,a)+eS_r(n^2,a)+e^2\sum_{j=1}^3b_jS_r(n^3+m_j,a),
\qquad W_r=T_r-U_r,
$$
$$
H_n(a)=\frac1L\left(\frac{T_2}{T_1}-\frac{W_2}{W_1}\right),
$$
$$
K_n(a)=\frac1{L^2}\left(\frac{2W_3}{W_1}-\frac{W_2^2}{W_1^2}
-\frac{2T_3}{T_1}+\frac{T_2^2}{T_1^2}\right),
$$
where all $T_r,U_r,W_r$ are evaluated at $(n,a)$.

For all sufficiently large $n$, let $a_n>0$ be the unique solution with
$$
|a_nL-1|<\frac1{10}
$$
of
$$
K_n(a_n)+\frac{66}{125}H_n(a_n)^2+\frac65H_n(a_n)+\frac53=0.
$$
Determine
$$
\lim_{n\to\infty}(nL)^{1/3}(a_nL-1).
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

$H_n$ is the normalized $2\times2$ determinant ratio for the two columns $T$ and $U$, while $K_n$ is its scale derivative. The tuned combination forces a cubic degeneracy of the limiting determinant equation, so the root is selected by a finite-size cusp balance rather than ordinary linearization.
