## Steps

Step 1: Recover the scattering transform from rotational symmetry
Let a unit-speed geodesic be written as $(r(s),\theta(s))$. For the rotational metric
$$
ds^2=dr^2+f(r)^2d\theta^2,
$$
rotational symmetry gives the conserved quantity
$$
J=f(r)^2\dot\theta.
$$
At $r=R$ one has $f(R)=1$. If the inward unit tangent makes angle $\arcsin c$ with the inward radial direction and points toward increasing $\theta$, then its tangential speed is $c$, so $J=c$.

Unit speed gives
$$
\dot r^2+f(r)^2\dot\theta^2=1,
$$
hence
$$
\dot r^2=1-\frac{c^2}{f(r)^2}.
$$
Because $f$ is strictly increasing, the geodesic has a unique turning radius $r_c$ with $f(r_c)=c$. The two halves are symmetric about the turning point, so
$$
\Phi(c)
=\int_{r_c}^{R}\frac{c}{f(r)\sqrt{f(r)^2-c^2}}\,dr.
$$

Step 2: Invert the transform and reconstruct the intrinsic metric
Let
$$
g(x)=(f^{-1})'(x),
\qquad 0\leq x\leq1.
$$
Changing variables $x=f(r)$ gives
$$
\Phi(c)=\int_c^1\frac{c\,g(x)}{x\sqrt{x^2-c^2}}\,dx.
$$
The identities
$$
\int_c^1\frac{c}{x\sqrt{x^2-c^2}}\,dx=\arccos c
$$
and
$$
\int_c^1\frac{cx}{\sqrt{x^2-c^2}}\,dx=c\sqrt{1-c^2}
$$
show that the prescribed scattering law is produced by
$$
g_0(x)=1+\lambda x^2.
$$
To prove uniqueness, put $h=g-g_0$. Then
$$
\int_c^1\frac{c\,h(x)}{x\sqrt{x^2-c^2}}\,dx=0
$$
for every $0<c<1$. Fix $0<y<1$ and integrate this identity against $1/\sqrt{c^2-y^2}$ for $y<c<1$. The endpoint singularities are integrable, so Fubini's theorem gives
$$
0=\int_y^1\frac{h(x)}{x}
\left(\int_y^x\frac{c\,dc}{\sqrt{x^2-c^2}\sqrt{c^2-y^2}}\right)dx.
$$
With $c^2=y^2+(x^2-y^2)t$, the inner integral equals
$$
\frac12\int_0^1\frac{dt}{\sqrt{t(1-t)}}=\frac{\pi}{2}.
$$
Hence
$$
\int_y^1\frac{h(x)}{x}\,dx=0
$$
for every $y$, and differentiation gives $h(y)=0$. Therefore
$$
(f^{-1})'(x)=1+\lambda x^2,
$$
so
$$
f^{-1}(x)=x+\frac{\lambda x^3}{3},
\qquad
R=1+\frac{\lambda}{3}.
$$
For $-1<\lambda<\infty$, the derivative $1+\lambda x^2$ is positive on $[0,1]$. Thus this intrinsic metric exists uniquely. Since $f^{-1}$ extends to a smooth odd function with derivative $1$ at the origin, its inverse is smooth and odd near $0$, so the pole condition is satisfied.

Step 3: Determine exactly when an isometric surface of revolution exists
Suppose the metric is induced by
$$
X(r,\theta)=\bigl(f(r)\cos\theta,f(r)\sin\theta,z(r)\bigr),
$$
with $z(0)=0$ and $r$ equal to meridian arclength. Then the induced metric is
$$
\bigl(f'(r)^2+z'(r)^2\bigr)dr^2+f(r)^2d\theta^2.
$$
Therefore one must have
$$
f'(r)^2+z'(r)^2=1.
$$
Writing $x=f(r)$ and using $(f^{-1})'(x)=1+\lambda x^2$ gives
$$
f'(r)=\frac{1}{1+\lambda x^2}.
$$
If $-1<\lambda<0$, then $1+\lambda x^2<1$ for every $x>0$, so $f'(r)>1$ away from the pole. The equation $f'^2+z'^2=1$ is then impossible. Thus no such surface of revolution exists for negative $\lambda$.

If $\lambda>0$, then $0<f'(r)\leq1$, so one may choose
$$
z'(r)=\sqrt{1-f'(r)^2}.
$$
This gives a smooth surface of revolution. Indeed, as $x\to0$,
$$
z_x=x\sqrt{2\lambda+\lambda^2x^2},
$$
so $z$ is a smooth even function of the Euclidean radial coordinate $x$ near the pole.

Step 4: Compute the boundary height
For $\lambda>0$, the boundary height is
$$
H=z(R)-z(0)=\int_0^R\sqrt{1-f'(r)^2}\,dr.
$$
Set $x=f(r)$. Since $dr=(1+\lambda x^2)dx$,
$$
H
=\int_0^1\sqrt{(1+\lambda x^2)^2-1}\,dx
=\int_0^1x\sqrt{2\lambda+\lambda^2x^2}\,dx.
$$
Therefore
$$
H
=\frac{[\lambda(\lambda+2)]^{3/2}-(2\lambda)^{3/2}}{3\lambda^2}
=\frac{(\lambda+2)^{3/2}-2\sqrt2}{3\sqrt\lambda}.
$$
Thus the admissible parameter-height pairs are exactly those with $\lambda>0$ and this value of $H$.

Final Answer: $\boxed{\{(\lambda,\frac{(\lambda+2)^{3/2}-2\sqrt2}{3\sqrt\lambda}):\lambda>0\}}$

---

## Answer

$\{(\lambda,\frac{(\lambda+2)^{3/2}-2\sqrt2}{3\sqrt\lambda}):\lambda>0\}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- geodesic conservation law
- inverse scattering transform
- Abel-type integral inversion
- isometric surface of revolution
- metric reconstruction
