# Normalized Math Problem

## LaTeX (Normalized)

Let $\lambda>0$. Let $R>0$, and let $f:[0,R]\to[0,1]$ be smooth with
$$
f(0)=0,
\qquad
f'(0)=1,
\qquad
f'(r)>0,
\qquad
f(R)=1.
$$
Assume the rotational metric
$$
ds^2=dr^2+f(r)^2d\theta^2
$$
extends smoothly across $r=0$.

For each $0<c<1$, let a unit-speed geodesic enter the boundary $r=R$ with inward tangent making angle $\arcsin c$ with the inward radial direction and pointing toward increasing $\theta$. Let $2\Phi(c)$ be the total increase of a continuous lift of $\theta$ between its two boundary intersections.

Suppose
$$
\Phi(c)=\arccos c+\lambda c\sqrt{1-c^2}
$$
for every $0<c<1$.

Determine the ordered pair $(R,f^{-1})$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Topology and Geometry |
| **Sub-domain** | Differential geometry |
| **Problem Type** | Parameter identification |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem is primarily Topology and Geometry and Differential geometry: it asks for inverse reconstruction of a rotationally symmetric Riemannian metric from its geodesic scattering data. Rotational symmetry yields a conserved geodesic quantity, while the full angular scattering law determines the inverse radial profile through an injective integral transform.
