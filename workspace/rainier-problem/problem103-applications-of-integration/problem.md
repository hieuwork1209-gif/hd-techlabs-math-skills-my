# Normalized Math Problem

## LaTeX (Normalized)

For $n\ge1$, define
$$
I_n=\iiint_{\mathbb R^3}
\exp\left(-n\left((xy-z^2)^2+(x^2+y^2+2z^2)^3\right)\right)
\,dx\,dy\,dz.
$$
Also let
$$
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt
\qquad(s>0).
$$
Evaluate
$$
\lim_{n\to\infty}n^{3/4}
\left(I_n-\frac{\pi^{3/2}\Gamma(1/6)}{3n^{2/3}}\right).
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

The phase is built from two natural invariants of the real symmetric matrix $\begin{pmatrix}x&z\\z&y\end{pmatrix}$: the squared determinant and the cube of its Frobenius norm squared. Its degenerate minimum lies on the determinant-zero cone. The leading term comes from that cone away from its apex, while the next term is a nonuniform apex correction, making this a natural degenerate Laplace-asymptotic integration problem.
