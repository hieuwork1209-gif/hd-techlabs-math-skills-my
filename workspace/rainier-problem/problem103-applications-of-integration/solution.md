## Steps

Step 1: Locate the zero set and identify the relevant scales

Let
$$
z=1-x-y,
\qquad
P=xyz,
\qquad
D=(x-y)(y-z)(z-x),
$$
so the phase is
$$
\Phi=P^2+D^2.
$$
Since $\Phi\ge0$, its zeros satisfy $P=D=0$. On the barycentric triangle this gives exactly six points: the three vertices
$$
(1,0,0),\ (0,1,0),\ (0,0,1)
$$
and the three edge midpoints
$$
\left(\frac12,\frac12,0\right),\quad
\left(\frac12,0,\frac12\right),\quad
\left(0,\frac12,\frac12\right).
$$
Away from fixed small neighborhoods of these points, $\Phi$ is bounded below by a positive constant, so the contribution is exponentially small.

At a vertex the tangential scale is $n^{-1/4}$ and the transverse scale is $n^{-1/2}$, producing the leading order $n^{-3/4}$. At an edge midpoint both local directions have scale $n^{-1/2}$, so those points first contribute at order $n^{-1}$.

Step 2: Compute the leading contribution from one vertex

Consider the vertex $(x,y,z)=(1,0,0)$. Put
$$
y=t+d,
\qquad
z=t-d,
\qquad
x=1-2t.
$$
Then $dy\,dz=2\,dt\,dd$ and the local domain is $t\ge0$, $|d|\le t$. Moreover
$$
P=(1-2t)(t^2-d^2),
$$
$$
D=-2d\left((1-3t)^2-d^2\right).
$$
Let
$$
\varepsilon=n^{-1/4},
\qquad
t=\varepsilon T,
\qquad
d=\varepsilon^2U.
$$
Then
$$
n\Phi=T^4+4U^2-arepsilon\left(4T^5+48TU^2\right)+O(\varepsilon^2)
$$
on bounded scaled sets, while the scaled domain is
$$
T\ge0,
\qquad
|U|\le \frac{T}{\varepsilon}.
$$
Hence the leading contribution of this vertex is
$$
2\varepsilon^3
\int_0^\infty e^{-T^4}\,dT
\int_{-\infty}^\infty e^{-4U^2}\,dU
=
\frac{\sqrt\pi\,\Gamma(1/4)}4\,n^{-3/4}.
$$
The three vertices therefore give
$$
\frac{3\sqrt\pi\,\Gamma(1/4)}4\,n^{-3/4}.
$$

Step 3: Compute the order $n^{-1}$ correction from the vertices

There are two contributions at the next order.

First, expanding the exponential using Step 2 gives the bulk correction at one vertex
$$
2\int_0^\infty\int_{-\infty}^\infty
\left(4T^5+48TU^2\right)e^{-T^4-4U^2}\,dU\,dT.
$$
Using
$$
\int_0^\infty T^5e^{-T^4}\,dT=\frac{\sqrt\pi}{8},
\qquad
\int_0^\infty Te^{-T^4}\,dT=\frac{\sqrt\pi}{4},
$$
$$
\int_{-\infty}^\infty e^{-4U^2}\,dU=\frac{\sqrt\pi}{2},
\qquad
\int_{-\infty}^\infty U^2e^{-4U^2}\,dU=\frac{\sqrt\pi}{16},
$$
this equals
$$
2\left(\frac\pi4+\frac{3\pi}{4}\right)=2\pi.
$$

Second, the exact condition $|U|\le T/\varepsilon$ cannot be replaced by the whole line at this order. Its correction is concentrated where $T=O(\varepsilon)$. Setting $T=\varepsilon S$ gives
$$
2\int_0^\infty
\left[
\int_{|U|\le S}e^{-4U^2}\,dU
-
\int_{-\infty}^\infty e^{-4U^2}\,dU
\right]dS.
$$
Reversing the order of integration,
$$
-2\int_{-\infty}^\infty |U|e^{-4U^2}\,dU=-\frac12.
$$
Thus one vertex contributes
$$
\left(2\pi-\frac12\right)n^{-1}
$$
at the next order, and all three vertices contribute
$$
\left(6\pi-\frac32\right)n^{-1}.
$$

Step 4: Compute the edge-midpoint contribution

Consider $(x,y,z)=(1/2,1/2,0)$. Put
$$
z=s,
\qquad
x=\frac{1-s}{2}+u,
\qquad
y=\frac{1-s}{2}-u.
$$
The Jacobian is $1$, and
$$
P=s\left(\frac{(1-s)^2}{4}-u^2\right),
$$
$$
D=-2u\left(\frac{(1-3s)^2}{4}-u^2\right).
$$
With
$$
s=n^{-1/2}S,
\qquad
u=n^{-1/2}U,
$$
one has
$$
n\Phi\longrightarrow \frac{S^2}{16}+\frac{U^2}{4}.
$$
Therefore one midpoint contributes
$$
n^{-1}
\int_0^\infty e^{-S^2/16}\,dS
\int_{-\infty}^\infty e^{-U^2/4}\,dU
=4\pi\,n^{-1}.
$$
There are three edge midpoints, so their total contribution is
$$
12\pi\,n^{-1}.
$$

Step 5: Combine the local contributions

Adding Steps 2--4 gives
$$
I_n=
\frac{3\sqrt\pi\,\Gamma(1/4)}4\,n^{-3/4}
+\left(18\pi-\frac32\right)n^{-1}
+o(n^{-1}).
$$
Hence
$$
\lim_{n\to\infty}
n\left(
I_n-\frac{3\sqrt\pi\,\Gamma(1/4)}{4n^{3/4}}
\right)
=18\pi-\frac32.
$$
Final Answer: $\boxed{18\pi-\frac32}$

---

## Answer

$18\pi-\frac32$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- barycentric symmetric invariants
- anisotropic vertex scaling
- boundary-layer matching
- edge-midpoint Gaussian scaling
- degenerate Laplace asymptotics
