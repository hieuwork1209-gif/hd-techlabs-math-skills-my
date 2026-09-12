## Steps

Step 1: Parametrize the squared disk
Let
$$
D_c=\{z\in\mathbb C:|z-c|<1\},\qquad 1<c<2,
$$
and let $S_c=\{z^2:z\in D_c\}$. Since $\operatorname{Re}z\geq c-1>0$ on $\overline{D_c}$, the squaring map is injective there: if $z_1^2=z_2^2$, then $z_1=\pm z_2$, and the second possibility cannot occur for two points with positive real part. Thus $\overline{S_c}$ is a Jordan domain with boundary
$$
\gamma(t)=(c+e^{it})^2=x(t)+iy(t),\qquad -\pi\leq t\leq\pi,
$$
where
$$
x(t)=c^2+2c\cos t+\cos 2t,
\qquad
y(t)=2c\sin t+\sin 2t.
$$
Taking closures does not change either area in the requested difference, so the convex-hull analysis may be done for this closed Jordan domain.

Step 2: Determine the boundary of the convex hull
Write $u=\cos t$. Then
$$
x(t)=2u^2+2cu+c^2-1.
$$
Because $1<c<2$, the minimum for $-1\leq u\leq1$ occurs at $u=-c/2$. Put
$$
\beta=\arccos\left(\frac c2\right),
\qquad
t_0=\pi-\beta,
\qquad
x_0=\frac{c^2}{2}-1.
$$
Then
$$
x(t)-x_0=2\left(\cos t+\frac c2\right)^2\geq0,
$$
with equality only for $t=\pm t_0$. Hence $x=x_0$ is a supporting line, meeting the curve at two points whose imaginary parts are
$$
y(\pm t_0)=\pm y_0,
\qquad
y_0=\frac c2\sqrt{4-c^2}.
$$

It remains to show that the arc $-t_0\leq t\leq t_0$ together with the vertical chord between these contact points is exactly the convex-hull boundary. Since
$$
\gamma'(t)=2ie^{it}(c+e^{it}),
$$
a continuous tangent angle on that arc is
$$
\psi(t)=\frac\pi2+t+\arg(c+e^{it}),
$$
where the argument is continuous because $\operatorname{Re}(c+e^{it})\geq c-1>0$. Differentiating gives
$$
\psi'(t)=\frac{c^2+2+3c\cos t}{c^2+1+2c\cos t}.
$$
For $|t|\leq t_0$, $\cos t\geq-c/2$, so
$$
\psi'(t)\geq\frac{2-c^2/2}{c^2+1+2c\cos t}>0.
$$
Also
$$
\arg(c+e^{it_0})=\beta,
\qquad
\arg(c+e^{-it_0})=-\beta,
$$
so
$$
\psi(t_0)-\psi(-t_0)=2t_0+2\beta=2\pi.
$$
Moreover $\gamma'(\pm t_0)=-2i$, exactly the direction of the downward vertical chord. Therefore the arc plus chord is a simple closed $C^1$ curve whose tangent angle is nondecreasing through one full turn; by the plane-curve convexity criterion, it bounds a convex set $C$.

Every point of the omitted arc $t_0<t<2\pi-t_0$ has $x(t)>x_0$, while the chord lies on $x=x_0$. Since the original boundary is a Jordan curve, replacing that indented arc by the exterior supporting chord enlarges the Jordan domain, so $\overline{S_c}\subset C$. Conversely, the curved part of $\partial C$ lies in $\overline{S_c}$ and the chord is the segment joining two points of $\overline{S_c}$, hence $\partial C\subset\operatorname{conv}(\overline{S_c})$. Because $C$ is convex, this gives
$$
C=\operatorname{conv}(\overline{S_c}).
$$
Thus the requested area difference is exactly the area of the pocket between the supporting chord and the omitted arc.

Step 3: Convert the pocket area to an explicit integral
By symmetry about the real axis, half of the pocket lies between the arc $t_0\leq t\leq\pi$ and the line $x=x_0$. On this interval $u=\cos t$ runs from $-c/2$ to $-1$, and
$$
\frac{y'(t)}2=2u^2+cu-1<0,
$$
because its derivative with respect to $u$ is $4u+c\leq-c<0$ and its value at $u=-1$ is $1-c<0$. Therefore
$$
\frac{\operatorname{Area}(\operatorname{conv}(S_c))-\operatorname{Area}(S_c)}{2}
=-\int_{t_0}^{\pi}(x(t)-x_0)y'(t)\,dt.
$$
Using
$$
x(t)-x_0=\frac{(c+2\cos t)^2}{2},
\qquad
y'(t)=2(c\cos t+\cos 2t),
$$
the integrand expands to
$$
(x(t)-x_0)y'(t)
=(2c^2+1)+(c^3+5c)\cos t+(3c^2+2)\cos 2t+3c\cos 3t+\cos 4t.
$$
Hence an explicit antiderivative is
$$
J(t)=(2c^2+1)t+(c^3+5c)\sin t+\frac{3c^2+2}{2}\sin 2t+c\sin 3t+\frac14\sin 4t.
$$
The half-deficit is therefore $J(t_0)-J(\pi)$.

Step 4: Evaluate the endpoint terms
Let
$$
d=\sqrt{4-c^2}.
$$
From $\cos t_0=-c/2$ and $\sin t_0=d/2$,
$$
\sin 2t_0=-\frac{cd}{2},
\qquad
\sin 3t_0=\frac{d(c^2-1)}{2},
\qquad
\sin 4t_0=-\frac{cd(c^2-2)}{2}.
$$
Substitution into $J$ gives
$$
J(t_0)=(2c^2+1)t_0+\frac{cd(c^2+14)}{8},
$$
while
$$
J(\pi)=(2c^2+1)\pi.
$$
Since $t_0-\pi=-\arccos(c/2)$, doubling the half-deficit yields
$$
\operatorname{Area}(\operatorname{conv}(S_c))-\operatorname{Area}(S_c)
=\frac{c(c^2+14)\sqrt{4-c^2}}{4}-2(2c^2+1)\arccos\left(\frac c2\right).
$$

Final Answer: $\boxed{\frac{c(c^2+14)\sqrt{4-c^2}}{4}-2(2c^2+1)\arccos\left(\frac c2\right)}$

---

## Answer

$\frac{c(c^2+14)\sqrt{4-c^2}}{4}-2(2c^2+1)\arccos\left(\frac c2\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- convex hulls
- supporting lines
- turning angle criterion
- Jordan curves
- Green's theorem
