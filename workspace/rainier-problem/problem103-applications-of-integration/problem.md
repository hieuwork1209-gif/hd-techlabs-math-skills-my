# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Let
$$
T=\{(x,y,z)\in\mathbb R^3:x,y,z\ge0,\ x+y+z\le1\}.
$$
For $n\ge1$, define
$$
I_n=\iiint_T
\exp\left(-nxyz(1-x-y-z)\right)\,dx\,dy\,dz.
$$
Also let
$$
\gamma=\lim_{m\to\infty}\left(\sum_{k=1}^m\frac1k-\log m\right)
$$
be Euler's constant. Evaluate
$$
\lim_{n\to\infty}
\left(
nI_n-2(\log n)^2-4\gamma\log n
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

The factor $xyz(1-x-y-z)$ is the product of the four barycentric coordinates of the standard tetrahedron. It vanishes on all four faces, and the intersections of those faces create a repeated Mellin singularity that produces the quadratic logarithmic asymptotics. This is a natural asymptotic-integration problem in Calculus -> Applications of integration.
