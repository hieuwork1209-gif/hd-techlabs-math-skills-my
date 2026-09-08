# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\mathbb D=\{(x,y)\in\mathbb R^2:x^2+y^2\le1\}.
$$
For each integer $n\ge1$, define
$$
I_n=\iint_{\mathbb D}
\cos\left(2\pi n(x^3-3xy^2)\right)\,dx\,dy.
$$
Also let
$$
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt
\qquad(s>0).
$$
Evaluate
$$
\lim_{n\to\infty}n^{3/2}
\left(
I_n-
\frac{\pi^{1/3}\Gamma(1/3)}{3\Gamma(2/3)n^{2/3}}
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

The phase $x^3-3xy^2$ is the real part of $(x+iy)^3$, a natural cubic harmonic on the unit disk. The leading oscillatory contribution comes from its degenerate stationary point at the origin, while the requested correction comes from stationary points on the boundary. Determining the limit therefore requires matching two distinct oscillatory mechanisms, making this a natural asymptotic-integration problem in Calculus -> Applications of integration.
