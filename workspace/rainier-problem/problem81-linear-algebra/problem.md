# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge1$, let $a,b>0$, and let
$$
0<\lambda<\mu<1.
$$
Put
$$
w(x)=x^{a-1}(1-x)^{b-1}
\qquad(0<x<1).
$$
Define the two $n\times n$ Hankel determinants
$$
D_n
=
\det\left[
\int_0^1 x^{i+j}w(x)\,dx
\right]_{i,j=0}^{n-1},
$$
$$
D_n(\lambda,\mu)
=
\det\left[
\int_0^1 x^{i+j}w(x)(1-\lambda x)^2(1-\mu x)^2\,dx
\right]_{i,j=0}^{n-1}.
$$

For $m\ge0$, let $P_m^{(b-1,a-1)}$ denote the Jacobi polynomial in the standard normalization, and define the monic shifted Jacobi polynomial
$$
\pi_m(x)
=
\frac{P_m^{(b-1,a-1)}(2x-1)}{c_m},
$$
where
$$
c_m
=
\frac{\Gamma(2m+a+b-1)}{\Gamma(m+1)\Gamma(m+a+b-1)}.
$$
Thus $\pi_m$ is monic and orthogonal on $[0,1]$ for the weight $w$.

Determine exactly the normalized determinant
$$
\frac{D_n(\lambda,\mu)}{D_n}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Linear Algebra |
| Sub-domain | Determinants |
| Problem Type | Exact computation |
| Answer Type | Exact symbolic expression |

---

## Domain Explanation

The quantity to be determined is an exact Hankel determinant ratio. Its structure is controlled by determinant identities for moment matrices; orthogonal-polynomial and integral representations are the subordinate tools used to evaluate the determinant. Thus Linear Algebra -> Determinants is primary.
