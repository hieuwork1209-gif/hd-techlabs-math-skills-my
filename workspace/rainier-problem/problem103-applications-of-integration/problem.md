# Normalized Math Problem

## LaTeX (Normalized)

For $x=(x_1,x_2,x_3,x_4)\in\mathbb R^4$, put
$$
\Delta(x)=\prod_{1\le i<j\le4}(x_i-x_j).
$$
For $n\ge1$, define
$$
I_n=\int_{\mathbb R^4}|\Delta(x)|
\exp\left(-n\left((x_1x_2x_3x_4)^2+
(x_1^2+x_2^2+x_3^2+x_4^2)^5\right)\right)\,dx.
$$
Also let
$$
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt
\qquad(s>0).
$$
Evaluate
$$
\lim_{n\to\infty}n^{23/20}
\left(
I_n-
\frac{3\pi^{3/2}\Gamma(3/5)}{5\sqrt2\,n^{11/10}}
\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Real number |

---

## Domain Explanation

The factor $|\Delta(x)|$ is the eigenvalue Jacobian for real symmetric $4\times4$ matrices. The determinant-zero set $x_1x_2x_3x_4=0$ is stratified by the number of vanishing eigenvalues. The leading Laplace contribution comes from the four rank-three hyperplanes, while the next term comes from their six rank-two intersections through a nonuniform finite-part correction. This is a natural degenerate asymptotic-integration problem in Calculus -> Applications of integration.
