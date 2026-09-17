## Steps

Step 1: Convert the geodesic scattering data into an integral transform
Let a unit-speed geodesic be written as $(r(s),\theta(s))$. For the rotational metric
$$
ds^2=dr^2+f(r)^2d\theta^2,
$$
rotational symmetry gives the conserved quantity
$$
J=f(r)^2\dot\theta.
$$
At the boundary $r=R$, one has $f(R)=1$. If the inward unit tangent makes angle $\arcsin c$ with the inward radial direction and points toward increasing $\theta$, then its tangential speed is $c$, so $J=c$.

Unit speed gives
$$
\dot r^2+f(r)^2\dot\theta^2=1,
$$
hence
$$
\dot r^2=1-\frac{c^2}{f(r)^2}.
$$
Because $f$ is strictly increasing from $0$ to $1$, the geodesic has a unique turning radius $r_c$ satisfying
$$
f(r_c)=c.
$$
The two halves of the geodesic are symmetric about the turning point. Therefore, if $\Phi(c)$ is half of the total lifted angular change between the two boundary intersections,
$$
\Phi(c)
=\int_{r_c}^{R}\frac{c}{f(r)\sqrt{f(r)^2-c^2}}\,dr.
$$

Step 2: Express the prescribed scattering law through the inverse radial profile
Since $f$ is strictly increasing, let
$$
g(x)=(f^{-1})'(x),
\qquad 0\leq x\leq1.
$$
Changing variables $x=f(r)$ in the integral from Step 1 gives
$$
\Phi(c)
=\int_c^1\frac{c\,g(x)}{x\sqrt{x^2-c^2}}\,dx.
$$
The two elementary integrals
$$
\int_c^1\frac{c}{x\sqrt{x^2-c^2}}\,dx=\arccos c
$$
and
$$
\int_c^1\frac{cx}{\sqrt{x^2-c^2}}\,dx=c\sqrt{1-c^2}
$$
show that the prescribed law
$$
\Phi(c)=\arccos c+\lambda c\sqrt{1-c^2}
$$
is exactly the transform of
$$
g_0(x)=1+\lambda x^2.
$$
Thus, with
$$
h(x)=g(x)-1-\lambda x^2,
$$
we have
$$
\int_c^1\frac{c\,h(x)}{x\sqrt{x^2-c^2}}\,dx=0
$$
for every $0<c<1$.

Step 3: Prove injectivity of the transform by a second integration
Fix $0<y<1$. Integrate the zero identity from Step 2 against $1/\sqrt{c^2-y^2}$ for $y<c<1$. Since $h$ is continuous and the endpoint singularities are integrable, Fubini's theorem applies and gives
$$
0
=\int_y^1\frac{h(x)}{x}
\left(
\int_y^x\frac{c\,dc}{\sqrt{x^2-c^2}\sqrt{c^2-y^2}}
\right)dx.
$$
In the inner integral set
$$
c^2=y^2+(x^2-y^2)t.
$$
Then
$$
c\,dc=\frac{x^2-y^2}{2}\,dt
$$
and
$$
\sqrt{x^2-c^2}\sqrt{c^2-y^2}
=(x^2-y^2)\sqrt{t(1-t)}.
$$
Hence
$$
\int_y^x\frac{c\,dc}{\sqrt{x^2-c^2}\sqrt{c^2-y^2}}
=\frac12\int_0^1\frac{dt}{\sqrt{t(1-t)}}
=\frac{\pi}{2}.
$$
Therefore
$$
\int_y^1\frac{h(x)}{x}\,dx=0
$$
for every $0<y<1$. Differentiating with respect to $y$ yields
$$
\frac{h(y)}{y}=0,
$$
so
$$
g(x)=1+\lambda x^2
$$
throughout $[0,1]$.

Step 4: Reconstruct the metric profile and verify uniqueness and existence
Because $f^{-1}(0)=0$,
$$
f^{-1}(x)
=\int_0^x g(t)\,dt
=x+\frac{\lambda x^3}{3}.
$$
In particular,
$$
R=f^{-1}(1)=1+\frac{\lambda}{3}.
$$

Conversely, define
$$
F(x)=x+\frac{\lambda x^3}{3}
$$
on $[0,1]$ and let $f=F^{-1}$. Since
$$
F'(x)=1+\lambda x^2>0,
$$
this gives a smooth increasing profile with $f(0)=0$, $f'(0)=1$, and $f(R)=1$. Substituting $(f^{-1})'(x)=1+\lambda x^2$ into the scattering integral reproduces exactly
$$
\Phi(c)=\arccos c+\lambda c\sqrt{1-c^2}.
$$
Thus the recovered pair is both attainable and unique.

Final Answer: $\boxed{\left(1+\frac{\lambda}{3},x\mapsto x+\frac{\lambda x^3}{3}\right)}$

---

## Answer

$\left(1+\frac{\lambda}{3},x\mapsto x+\frac{\lambda x^3}{3}\right)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- geodesic conservation law
- rotationally symmetric metrics
- inverse scattering transform
- Abel-type integral inversion
- inverse profile reconstruction
