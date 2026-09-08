# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
T=\{(x,y)\in\mathbb R^2:x\ge0,\ y\ge0,\ x+y\le1\},
$$
and for $(x,y)\in T$ put
$$
z=1-x-y,
\qquad
P=xyz,
\qquad
D=(x-y)(y-z)(z-x).
$$
For $n\ge1$, define
$$
I_n=\iint_T e^{-n(P^2+D^2)}\,dx\,dy.
$$
Also let
$$
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt
\qquad(s>0).
$$
Evaluate
$$
\lim_{n\to\infty}
n\left(
I_n-
\frac{3\sqrt\pi\,\Gamma(1/4)}{4n^{3/4}}
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

The functions $P$ and $D$ are the basic product and Vandermonde invariants of the three barycentric coordinates $x,y,z$. Their common zero set consists of the three vertices and the three edge midpoints of the simplex. The vertices have an anisotropic degenerate scale, while the edge midpoints contribute at the next Gaussian scale, so the requested coefficient requires matching two distinct local geometries. This is a natural degenerate asymptotic-integration problem in Calculus -> Applications of integration.
