## Steps

Step 1: Pass to polar coordinates and rescale time
Set
$$
P=a(x^2+y^2)^2+x^4-6x^2y^2+y^4,
\qquad
Q=b(x^2+y^2)^2+x^4-y^4.
$$
The system is
$$
\dot x=-Px-Qy,
\qquad
\dot y=-Py+Qx.
$$
For a nonzero trajectory write $x=r\cos\theta$, $y=r\sin\theta$. Since
$$
x\dot x+y\dot y=-Pr^2,
\qquad
x\dot y-y\dot x=Qr^2,
$$
and
$$
P=r^4(a+\cos4\theta),
\qquad
Q=r^4(b+\cos2\theta),
$$
we obtain
$$
\dot r=-r^5A(\theta),
\qquad
\dot\theta=r^4B(\theta),
$$
where
$$
A(\theta)=a+\cos4\theta,
\qquad
B(\theta)=b+\cos2\theta.
$$
Introduce the increasing time variable $\tau$ by $d\tau/dt=r^4$. Then
$$
\frac{d\theta}{d\tau}=B(\theta),
\qquad
\frac{d}{d\tau}\log r=-A(\theta).
$$
Thus the angular equation is autonomous, while the logarithmic radial change is obtained by integrating $-A$ along the angular motion.

Step 2: Analyze the regime $|b|\leq1$
Now $B$ has zeros, namely the angles satisfying
$$
\cos2\theta=-b.
$$
Each such angle is an invariant ray. On every one of these rays,
$$
A(\theta)=a+\cos4\theta
=a+2\cos^2 2\theta-1
=a+2b^2-1.
$$
Hence a necessary condition for global asymptotic stability is
$$
a+2b^2-1>0.
$$
Indeed, equality makes every nonzero point of each such ray an equilibrium, while a negative value makes $r$ increase along that ray.

Assume now that
$$
a+2b^2-1>0.
$$
All zeros of $B$ then lie in a neighborhood on which $A$ is uniformly positive. On each component between consecutive zeros of $B$, the scalar equation $d\theta/d\tau=B(\theta)$ is monotone and approaches an endpoint zero; an orbit starting at a zero remains there. Therefore any part of the angular motion on which $A<0$ is traversed only for a uniformly bounded amount of $\tau$-time, whereas eventually $A$ is bounded below by a positive constant. Consequently there is a constant $C=C(a,b)$ such that
$$
r(\tau)\leq C r(0)
$$
for all $\tau\geq0$, and moreover $r(\tau)\to0$ as $\tau\to\infty$.

Since $dt/d\tau=r^{-4}$, the relation $r(\tau)\to0$ forces $t(\tau)\to\infty$. Thus every forward solution is global and converges to the origin. The bound $r(\tau)\leq Cr(0)$ gives Lyapunov stability. Hence for $|b|\leq1$ the exact condition is
$$
a>1-2b^2.
$$

Step 3: Analyze the rotating regime $|b|>1$
Here $B$ never vanishes and has the constant sign of $b$, so every nonzero trajectory rotates forever in the $\tau$-time. During one full revolution the change in $\log r$ is
$$
-K,
\qquad
K:=\int_0^{2\pi}\frac{A(\theta)}{|B(\theta)|}\,d\theta.
$$
If $K>0$, each revolution multiplies $r$ by $e^{-K}<1$. Because $A/B$ is continuous, the radial variation within a single revolution is uniformly bounded, so $r(\tau)\leq Cr(0)$ and $r(\tau)\to0$. This again gives global existence, convergence, and Lyapunov stability.

If $K=0$, the radius returns to its starting value after every full turn, producing a nonzero periodic orbit. If $K<0$, the radius is multiplied by a factor larger than $1$ each turn, so arbitrarily small initial data eventually leave any fixed neighborhood of the origin. Therefore global asymptotic stability is equivalent to $K>0$.

Let $\sigma=\operatorname{sgn}(b)$ and $s=\sqrt{b^2-1}$. With $\phi=2\theta$,
$$
K=\sigma\int_0^{2\pi}\frac{a+\cos2\phi}{b+\cos\phi}\,d\phi.
$$
Use
$$
\frac{\cos2\phi}{b+\cos\phi}
=2\cos\phi-2b+\frac{2b^2-1}{b+\cos\phi}.
$$
Also, the tangent-half-angle substitution $u=\tan(\phi/2)$ gives, for $|b|>1$,
$$
\int_0^{2\pi}\frac{d\phi}{b+\cos\phi}
=\frac{2\pi\sigma}{\sqrt{b^2-1}}
=\frac{2\pi\sigma}{s}.
$$
Hence
$$
K
=\frac{2\pi}{s}\left(a+2b^2-1-2|b|s\right).
$$
Thus $K>0$ exactly when
$$
a>1-2b^2+2|b|\sqrt{b^2-1}.
$$

Step 4: Combine the two regimes
For $|b|\leq1$ the threshold is $1-2b^2$, while for $|b|>1$ it is $1-2b^2+2|b|\sqrt{b^2-1}$. These combine as
$$
a>1-2b^2+2|b|\sqrt{\max\{b^2-1,0\}}.
$$
The inequality is strict in every case: equality yields either nonzero equilibria on invariant rays or nonzero periodic orbits.
Final Answer: $\boxed{\{(a,b):a>1-2b^2+2|b|\sqrt{\max\{b^2-1,0\}}\}}$

---

## Answer

$\{(a,b):a>1-2b^2+2|b|\sqrt{\max\{b^2-1,0\}}\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- global asymptotic stability
- polar coordinates
- homogeneous polynomial systems
- invariant rays and periodic orbits
- time rescaling

---

## Black-Box Audit — no issues found
