## Steps

Step 1: Parametrize the image and its boundary
Let
$$
D_c=\{z\in\mathbb C:|z-c|<1\},\qquad 1<c<2,
$$
and let $S_c=\{z^2:z\in D_c\}$. Since $\operatorname{Re}z>c-1>0$ on $D_c$, the squaring map is injective on $\overline{D_c}$: if $z_1^2=z_2^2$, then $z_1=\pm z_2$, and the second possibility cannot occur because both points have positive real part. Hence $S_c$ is a Jordan domain whose boundary is
$$
\gamma(t)=(c+e^{it})^2=x(t)+iy(t),\qquad -\pi\leq t\leq\pi,
$$
with
$$
x(t)=c^2+2c\cos t+\cos 2t,
\qquad
y(t)=2c\sin t+\sin 2t.
$$

Step 2: Find the supporting chord that cuts off the nonconvex indentation
Write $u=\cos t$. Then
$$
x(t)=2u^2+2cu+c^2-1.
$$
Because $1<c<2$, the minimum over $-1\leq u\leq 1$ occurs at $u=-c/2$. Put
$$
t_0=\arccos\left(-\frac c2\right)=\pi-\arccos\left(\frac c2\right)
$$
and
$$
x_0=x(t_0)=\frac{c^2}{2}-1.
$$
Indeed,
$$
x(t)-x_0=2\left(\cos t+\frac c2\right)^2\geq 0,
$$
with equality only at $t=\pm t_0$. Thus the vertical line $x=x_0$ is a supporting line of $S_c$. At the two contact points,
$$
y(\pm t_0)=\pm y_0,
\qquad
y_0=\frac c2\sqrt{4-c^2}.
$$
So the supporting chord joins $\gamma(-t_0)$ to $\gamma(t_0)$.

To verify that replacing the boundary arc through $t=\pm\pi$ by this chord gives the entire convex hull, differentiate
$$
\gamma'(t)=2ie^{it}(c+e^{it}).
$$
If $\psi(t)$ is a continuous tangent angle along the arc $-t_0\leq t\leq t_0$, then
$$
\psi'(t)=\operatorname{Im}\frac{\gamma''(t)}{\gamma'(t)}
=\frac{c^2+2+3c\cos t}{c^2+1+2c\cos t}.
$$
On this arc, $\cos t\geq-c/2$, so
$$
c^2+2+3c\cos t\geq 2-\frac{c^2}{2}>0.
$$
Hence the tangent angle is strictly increasing. Also $\gamma'(\pm t_0)=-2i$, so this arc together with the downward vertical chord has a nondecreasing tangent angle making one full turn. Therefore it is the boundary of a convex set. Since $x>x_0$ throughout the interior of $S_c$ and every other boundary point also has $x>x_0$, the chord lies outside $S_c$ and replacing the indented arc by the chord adds exactly the missing pocket. Thus this convex set is $\operatorname{conv}(S_c)$.

Step 3: Express the area gain as the pocket between the chord and the omitted arc
By symmetry about the real axis, half of the added area lies between the upper half of the omitted arc, $t_0\leq t\leq\pi$, and the line $x=x_0$. Along this arc, $y'(t)<0$, so
$$
\frac{\operatorname{Area}(\operatorname{conv}(S_c))-\operatorname{Area}(S_c)}{2}
=-\int_{t_0}^{\pi}(x(t)-x_0)y'(t)\,dt.
$$
Now
$$
x(t)-x_0=\frac{(c+2\cos t)^2}{2}
$$
and
$$
y'(t)=2(c\cos t+\cos 2t),
$$
so
$$
(x(t)-x_0)y'(t)
=(c+2\cos t)^2(c\cos t+2\cos^2t-1).
$$
An antiderivative is
$$
J(t)=c^3\sin t+2c^2t+\frac{3c^2}{2}\sin 2t+5c\sin t+c\sin 3t+t+\sin 2t+\frac14\sin 4t.
$$
Therefore the half-deficit equals $J(t_0)-J(\pi)$.

Step 4: Evaluate the endpoint terms
Let
$$
d=\sqrt{4-c^2}.
$$
Since $\cos t_0=-c/2$ and $\sin t_0=d/2$,
$$
\sin 2t_0=-\frac{cd}{2},
\qquad
\sin 3t_0=\frac{d(c^2-1)}{2},
\qquad
\sin 4t_0=-\frac{cd(c^2-2)}{2}.
$$
Substituting these into $J$ gives
$$
J(t_0)=(2c^2+1)t_0+\frac{cd(c^2+14)}{8},
$$
while
$$
J(\pi)=(2c^2+1)\pi.
$$
Using $t_0-\pi=-\arccos(c/2)$ and doubling the half-deficit,
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
