## Steps

Step 1: Reduce delay-independent stability to imaginary-axis crossings
Fix a delay $\tau>0$ and consider
$$
\dot x(t)=-x(t)-a\,x(t-\tau)-b\,x(t-2\tau),
\qquad a,b>0.
$$
An exponential mode $x(t)=e^{\lambda t}$ gives the characteristic equation
$$
\Delta_\tau(\lambda):=\lambda+1+a e^{-\tau\lambda}+b e^{-2\tau\lambda}=0.
$$
For a retarded linear equation, the zero solution is exponentially asymptotically stable exactly when every characteristic root has negative real part. Because the equation is linear, this is equivalent to global asymptotic stability in the history sup norm.

Any characteristic root with $\operatorname{Re}\lambda\ge0$ satisfies
$$
|\lambda+1|
=|a e^{-\tau\lambda}+b e^{-2\tau\lambda}|
\le a+b.
$$
Thus all roots in the closed right half-plane lie in a fixed compact disk, uniformly in $\tau$. For sufficiently small positive $\tau$, $\Delta_\tau$ converges uniformly on this disk to
$$
\lambda+1+a+b,
$$
which has no zero in the closed right half-plane. Hence the equation is stable for all sufficiently small $\tau>0$. As $\tau$ varies, the number of roots in the open right half-plane can therefore change only through a root on the imaginary axis.

Step 2: Eliminate the delay from the imaginary-axis equations
A zero root never occurs because
$$
\Delta_\tau(0)=1+a+b>0.
$$
Let $\lambda=i\omega$ with $\omega>0$, and set
$$
\theta=\tau\omega,
\qquad
c=\cos\theta,
\qquad
s=\sin\theta.
$$
Separating real and imaginary parts gives
$$
1+a c+b\cos2\theta=0,
$$
$$
\omega=a s+b\sin2\theta.
$$
Using $\cos2\theta=2c^2-1$ and $\sin2\theta=2sc$, define
$$
h(c):=2bc^2+ac+1-b.
$$
Every nonzero imaginary-axis root therefore gives
$$
h(c)=0
\qquad\text{for some }c\in(-1,1),
$$
because $s=0$ would force $\omega=0$.

Conversely, suppose $h(c)=0$ for some $c\in(-1,1)$. Put
$$
k=a+2bc.
$$
If $k\ne0$, choose $\theta\in(0,2\pi)$ with $\cos\theta=c$ and with $\sin\theta$ having the same sign as $k$. Then
$$
\omega=\sin\theta\,k>0,
\qquad
\tau=\frac{\theta}{\omega}>0,
$$
and the two imaginary-axis equations are satisfied. If $k=0$, then substituting $c=-a/(2b)$ into $h(c)=0$ gives $b=1$. But then $h(0)=0$, and at $c=0$ we have $a+2bc=a>0$, reducing to the previous case. Thus an interior zero of $h$ always produces a nonzero imaginary characteristic root for some positive delay.

Since $h(1)=1+a+b>0$, the equation is stable for every $\tau>0$ exactly when
$$
h(c)>0
\qquad\text{for all }-1<c<1.
$$
Indeed, under this condition there is no imaginary-axis crossing for any $\tau$, while right-half-plane roots cannot enter from infinity; hence the small-delay stability persists for every positive delay.

Step 3: Minimize the quadratic on the open interval
Because $b>0$, the quadratic
$$
h(c)=2bc^2+ac+1-b
$$
is strictly convex, with vertex
$$
c_*=-\frac{a}{4b}.
$$

If $a\ge4b$, then $c_*\le-1$, so $h$ is increasing on $(-1,1)$. Its infimum there is the endpoint value
$$
h(-1)=1-a+b.
$$
The endpoint itself is not part of the interval, so $h(c)>0$ for every $-1<c<1$ exactly when
$$
1-a+b\ge0,
$$
i.e.
$$
a\le1+b.
$$
Equality is allowed: when $h(-1)=0$, the only zero at the left endpoint would correspond to $\sin\theta=0$ and hence cannot give a nonzero imaginary characteristic root.

If $0<a<4b$, then $c_*\in(-1,0)$ and the minimum is attained inside the interval. We need
$$
h(c_*)
=1-b-\frac{a^2}{8b}>0,
$$
which is equivalent to
$$
a^2<8b(1-b).
$$

Step 4: State the robust stability region
Combining the two cases, the zero solution is globally asymptotically stable for every delay $\tau>0$ exactly for
$$
\{(a,b):a,b>0,\ a\ge4b,\ a\le1+b\}
\cup
\{(a,b):a,b>0,\ a<4b,\ a^2<8b(1-b)\}.
$$
Final Answer: $\boxed{\{(a,b):a,b>0,a\ge4b,a\le1+b\}\cup\{(a,b):a,b>0,a<4b,a^2<8b(1-b)\}}$

---

## Answer

$\{(a,b):a,b>0,a\ge4b,a\le1+b\}\cup\{(a,b):a,b>0,a<4b,a^2<8b(1-b)\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- delay differential equations
- delay-independent stability
- characteristic roots
- imaginary-axis crossings
- constrained quadratic positivity

---

## Black-Box Audit — no issues found
