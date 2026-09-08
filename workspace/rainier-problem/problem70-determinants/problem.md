# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge5$ and real $a>0$, define
$$
A_N(a)=\sum_{k=0}^{N}\frac{(-1)^k\binom Nk}{k+a}.
$$
For $b\in\mathbb R$, put
$$
T_n(a,b)=A_n(a)+n^bA_{n^2}(a)+n^{2b}A_{n^3}(a),
$$
$$
D_n(a,b)=n^b\bigl(A_{n^2}(a)-A_{n^2+n}(a)\bigr),
\qquad
R_n(a,b)=\frac{D_n(a,b)}{a\,T_n(a,b)}.
$$
All derivatives below are with respect to $a$, with $n$ and $b$ fixed.

For all sufficiently large $n$, let $(a_n,b_n)$ be the unique pair satisfying
$$
\left|a_n-\frac14\right|<\frac18,
\qquad
\left|b_n-\frac14\right|<\frac18,
\qquad b_n<a_n,
$$
and
$$
\frac{\partial}{\partial a}\log R_n(a_n,b_n)=0,
\qquad
\frac{\partial^3}{\partial a^3}\log R_n(a_n,b_n)=0.
$$
Determine
$$
\lim_{n\to\infty}n(\log n)(a_n-b_n).
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

The first odd log-derivative is the normalized $2\times2$ determinant condition for the two Beta-moment columns $T_n$ and $D_n/a$. Requiring the first and third odd derivatives to vanish forces a rank-deficient local-symmetry condition whose finite-size splitting selects the parameters.