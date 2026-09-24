# Normalized Math Problem

## LaTeX (Normalized)

Let $r\geq3$ be an integer and let
$$
0<\rho<\frac{1}{2\cos(\pi/(r+1))}.
$$
Define
$$
D_0=D_1=1,
\qquad
D_j=D_{j-1}-\rho^2D_{j-2}
\quad(j\geq2).
$$

Let $\mu$ range over all Borel probability measures on the unit circle $|z|=1$ satisfying
$$
\int z\,d\mu(z)=\rho
$$
and
$$
\int z^j\,d\mu(z)=0
\qquad
(2\leq j\leq r-1).
$$

Determine the ordered triple consisting of

1. the maximum possible value of
$$
\operatorname{Re}\int z^r\,d\mu(z);
$$
2. the number of points in the support of every maximizing measure;
3. the number of maximizing measures.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Harmonic analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem is a finite trigonometric moment extremization on the unit circle. The solution uses positivity of Toeplitz moment matrices to obtain the sharp bound, then reconstructs and classifies the extremizing measure through the associated unitary moment representation.
