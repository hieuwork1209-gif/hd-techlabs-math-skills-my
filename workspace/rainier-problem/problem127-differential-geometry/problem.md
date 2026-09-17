# Normalized Math Problem

## LaTeX (Normalized)

Let $-1<\lambda<\infty$ with $\lambda\neq0$. Let $R>0$, and let $f:[0,R]\to[0,1]$ be smooth with
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

For each $0<c<1$, let a unit-speed geodesic enter the boundary $r=R$ with inward tangent making angle $\arcsin c$ with the inward radial direction and pointing toward increasing $\theta$. Let $2\Phi(c)$ be the total increase of a continuous lift of $\theta$ between its two boundary intersections. Suppose
$$
\Phi(c)=\arccos c+\lambda c\sqrt{1-c^2}
$$
for every $0<c<1$.

Determine all pairs $(\lambda,H)$ for which this metric can be realized as the induced metric of a smooth surface of revolution
$$
X(r,\theta)=\bigl(f(r)\cos\theta,f(r)\sin\theta,z(r)\bigr)\subset\mathbb{R}^3,
$$
where $r$ is meridian arclength, $z(0)=0$, $z'(r)\geq0$, and $H=z(R)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Topology and Geometry |
| **Sub-domain** | Differential geometry |
| **Problem Type** | Parameter identification |
| **Answer Type** | Set or multiset of objects |

---

## Domain Explanation

This problem is primarily Topology and Geometry and Differential geometry: geodesic scattering data first determines the intrinsic rotational metric, after which isometric realization as a surface of revolution imposes an independent extrinsic compatibility condition. The requested parameter-height pairs require both inverse metric reconstruction and the meridian-arclength embedding constraint.
