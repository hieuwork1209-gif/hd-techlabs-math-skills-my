## Steps

Step 1: Reduce the homogeneous flow to angular and radial equations
Set
$$
P=a(x^2+y^2)^3+(x^2+y^2)(x^4-6x^2y^2+y^4),
$$
$$
Q=b(x^2+y^2)^3+x^6-15x^4y^2+15x^2y^4-y^6.
$$
For a nonzero trajectory write $x=r\cos\theta$, $y=r\sin\theta$. Since
$$
x\dot x+y\dot y=-Pr^2,
\qquad
x\dot y-y\dot x=Qr^2,
$$
and
$$
P=r^6(a+\cos4\theta),
\qquad
Q=r^6(b+\cos6\theta),
$$
we obtain
$$
\dot r=-r^7A(\theta),
\qquad
\dot\theta=r^6B(\theta),
$$
where
$$
A(\theta)=a+\cos4\theta,
\qquad
B(\theta)=b+\cos6\theta.
$$
Introduce the increasing time variable $\tau$ by $d\tau/dt=r^6$. Then
$$
\frac{d\theta}{d\tau}=B(\theta),
\qquad
\frac{d}{d\tau}\log r=-A(\theta).
$$
Thus global stability is determined by the angular flow and the accumulated radial drift along it.

Step 2: Analyze the regime $|b|\leq1$
Now $B$ has zeros, so every angle satisfying
$$
\cos6\theta=-b
$$
defines an invariant ray. Global asymptotic stability requires
$$
A(\theta)=a+\cos4\theta>0
$$
at every such ray. If equality holds at one of them, every nonzero point of that ray is an equilibrium; if the value is negative, the radius grows along that ray.

Let
$$
c=\cos4\theta.
$$
At a zero of $B$,
$$
\cos12\theta=2\cos^2 6\theta-1=2b^2-1.
$$
But also
$$
\cos12\theta=4c^3-3c.
$$
Hence the possible values of $c$ are precisely the three roots of
$$
4c^3-3c=2b^2-1.
$$
Put
$$
\gamma=\arccos(2b^2-1),
\qquad 0\leq\gamma\leq\pi.
$$
The three roots are
$$
\cos\frac\gamma3,
\qquad
\cos\left(\frac\gamma3+\frac{2\pi}{3}\right),
\qquad
\cos\left(\frac\gamma3+\frac{4\pi}{3}\right).
$$
Since $0\leq\gamma/3\leq\pi/3$, the smallest is
$$
\cos\left(\frac\gamma3+\frac{2\pi}{3}\right).
$$
Therefore $A>0$ at every invariant ray exactly when
$$
a> -\cos\left(\frac\gamma3+\frac{2\pi}{3}\right)
 =\cos\left(\frac\pi3-\frac\gamma3\right).
$$
Equivalently,
$$
a>\cos\left(\frac{\pi-\arccos(2b^2-1)}{3}\right).
$$

This condition is also sufficient. The scalar angular equation is monotone on every component between consecutive zeros of $B$ and every angular orbit either starts at a zero or approaches one as $\tau\to\infty$. Because $A$ is strictly positive at all finitely many zeros, it is uniformly positive in neighborhoods of them. Any portion of an orbit where $A<0$ is therefore traversed in a bounded amount of $\tau$-time. Hence there is a constant $C=C(a,b)$ such that
$$
r(\tau)\leq Cr(0)
$$
for all $\tau\geq0$, while eventually $A(\theta(\tau))$ is bounded below by a positive constant, so $r(\tau)\to0$. Since $dt/d\tau=r^{-6}$, this also forces $t\to\infty$. Thus the origin is globally asymptotically stable in this regime exactly under the displayed inequality.

Step 3: Analyze the rotating regime $|b|>1$
Here $B$ never vanishes and has the constant sign of $b$, so every nonzero trajectory rotates forever in $\tau$. The logarithmic radial change over one full revolution is
$$
-K,
\qquad
K=\int_0^{2\pi}\frac{a+\cos4\theta}{|b+\cos6\theta|}\,d\theta.
$$
The denominator is invariant under $\theta\mapsto\theta+\pi/3$. Therefore, writing
$$
J=\int_0^{2\pi}\frac{\cos4\theta}{|b+\cos6\theta|}\,d\theta,
$$
we may average $J$ over the three shifts $0,\pi/3,2\pi/3$ to obtain
$$
3J=\int_0^{2\pi}
\frac{\cos4\theta+\cos(4\theta+4\pi/3)+\cos(4\theta+8\pi/3)}{|b+\cos6\theta|}\,d\theta=0.
$$
Thus
$$
K=a\int_0^{2\pi}\frac{d\theta}{|b+\cos6\theta|}.
$$
The integral is strictly positive, so $K>0$ exactly when
$$
a>0.
$$
If $a>0$, every revolution contracts the radius by the same factor $e^{-K}<1$, and the radial variation during one turn is uniformly bounded; this gives Lyapunov stability, global existence, and convergence to the origin. If $a=0$, the radius returns to its initial value after every revolution, producing nonzero periodic orbits. If $a<0$, the radius expands from turn to turn, so the origin is not Lyapunov stable.

Step 4: Combine the two regimes
For $|b|\leq1$ the exact threshold is
$$
a>\cos\left(\frac{\pi-\arccos(2b^2-1)}{3}\right),
$$
whereas for $|b|>1$ it is simply $a>0$. Therefore the required region is
$$
\{(a,b):|b|>1,\ a>0\}
\cup
\left\{(a,b):|b|\leq1,\ a>\cos\left(\frac{\pi-\arccos(2b^2-1)}{3}\right)\right\}.
$$
Final Answer: $\boxed{\{(a,b):|b|>1,\ a>0\}\cup\{(a,b):|b|\le1,\ a>\cos((\pi-\arccos(2b^2-1))/3)\}}$

---

## Answer

$\{(a,b):|b|>1,\ a>0\}\cup\{(a,b):|b|\le1,\ a>\cos((\pi-\arccos(2b^2-1))/3)\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- global asymptotic stability
- homogeneous polynomial systems
- polar coordinates and time rescaling
- invariant rays and periodic orbits
- Chebyshev polynomial identities

---

## Black-Box Audit — no issues found
