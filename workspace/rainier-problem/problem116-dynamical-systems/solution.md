## Steps

Step 1: Convert the characteristic equation to a two-channel transfer bound
For fixed delays $\tau,\sigma\geq0$, write
$$
P(\lambda)=\lambda^2+a\lambda+1,
\qquad
H_1(\lambda)=\frac{b}{P(\lambda)},
\qquad
H_2(\lambda)=\frac{c\lambda}{P(\lambda)}.
$$
Because $a>0$, both zeros of $P$ have negative real part, so $H_1$ and $H_2$ are analytic on the open right half-plane and continuous on its boundary. They also tend to $0$ as $|\lambda|\to\infty$ there.

A characteristic root satisfies
$$
1+H_1(\lambda)e^{-\lambda\tau}
+H_2(\lambda)e^{-\lambda\sigma}=0.
$$
If $\operatorname{Re}\lambda\geq0$, then
$$
1
\leq
|H_1(\lambda)|e^{-\tau\operatorname{Re}\lambda}
+
|H_2(\lambda)|e^{-\sigma\operatorname{Re}\lambda}
\leq
|H_1(\lambda)|+|H_2(\lambda)|.
$$
The function
$$
S(\lambda)=|H_1(\lambda)|+|H_2(\lambda)|
$$
is subharmonic as a sum of moduli of analytic functions. The maximum principle for subharmonic functions says that on each bounded right half-disk, the maximum of $S$ is attained on the boundary. Since $S\to0$ on the large semicircle, a bound
$$
S(i\omega)<1
$$
for every real $\omega$, with a uniform gap from $1$, rules out every characteristic root in the closed right half-plane.

Step 2: Identify the phase geometry on the imaginary axis
Let $\omega>0$. Write
$$
R(\omega)=|P(i\omega)|
=
\sqrt{(1-\omega^2)^2+a^2\omega^2}.
$$
For $\lambda=i\omega$, the two delayed feedback terms have magnitudes $b$ and $c\omega$. Since $\tau$ and $\sigma$ are independent, the phases
$$
e^{-i\omega\tau},
\qquad
i e^{-i\omega\sigma}
$$
can be chosen independently anywhere on the unit circle. Therefore the possible magnitudes of their sum fill exactly the interval
$$
[|b-c\omega|,\ b+c\omega].
$$
Indeed, if the relative angle is $\theta$, the squared magnitude is
$$
b^2+c^2\omega^2+2bc\omega\cos\theta,
$$
which runs continuously from $(b-c\omega)^2$ to $(b+c\omega)^2$.

It follows that an imaginary root $i\omega$ can be produced by some pair of delays exactly when
$$
|b-c\omega|
\leq
R(\omega)
\leq
b+c\omega.
$$

Step 3: Reduce the regime $0\leq b<1$ to one frequency margin
Assume $0\leq b<1$. At $\omega=0$,
$$
R(0)=1>b.
$$
Thus the root locus can reach the annulus from Step 2 only after $R$ first meets its upper boundary $b+c\omega$. Consequently, no imaginary root can occur for any delays exactly when
$$
R(\omega)>b+c\omega
$$
for every $\omega>0$.

Squaring gives
$$
\omega^4+(a^2-c^2-2)\omega^2-2bc\omega+1-b^2>0.
$$
After division by $\omega^2$,
$$
a^2
>
c^2+2+
\frac{2bc}{\omega}
-
\frac{1-b^2}{\omega^2}
-
\omega^2.
$$
The function
$$
g_{b,c}(r)
=
\frac{2bc}{r}
-
\frac{1-b^2}{r^2}
-
r^2,
\qquad r>0,
$$
tends to $-\infty$ as $r\to0^+$ and as $r\to\infty$, so it attains a finite maximum. Hence the required condition for $0\leq b<1$ is
$$
a^2
>
c^2+2+
\max_{r>0}
\left(
\frac{2bc}{r}
-
\frac{1-b^2}{r^2}
-
r^2
\right).
$$

Under this strict inequality, the continuous function
$$
\frac{b+c|\omega|}{|P(i\omega)|}
$$
is below $1$ for all real $\omega$ and tends to $0$ as $|\omega|\to\infty$. Its maximum is therefore some $\rho<1$. Step 1 then gives $S(\lambda)\leq\rho<1$ in the open right half-plane, so no characteristic root there is possible. The strict boundary inequality also excludes imaginary roots.

Step 4: Handle the boundary and excluded parameter regimes
Suppose first that $b=1$ and $c=0$. Then
$$
R(\omega)^2-1
=
\omega^2(\omega^2+a^2-2).
$$
Therefore $R(\omega)>1$ for every $\omega>0$ exactly when
$$
a^2\geq2.
$$
For $a^2\geq2$, Step 1 applies to the single analytic function $H_1=1/P$. On the imaginary axis $|H_1|\leq1$, with equality only at $\omega=0$. The strong maximum principle gives $|H_1(\lambda)|<1$ in the open right half-plane. Also
$$
\Delta_{\tau,\sigma}(0)=2,
$$
so the boundary equality at $0$ is harmless.

Now let $b=1$ and $c>0$. Since
$$
R(\omega)=1+O(\omega^2)
$$
as $\omega\to0^+$, while
$$
|1-c\omega|=1-c\omega,
\qquad
1+c\omega=1+c\omega
$$
for sufficiently small $\omega$, one has
$$
|1-c\omega|<R(\omega)<1+c\omega
$$
for all sufficiently small positive $\omega$. Step 2 then produces an imaginary root.

Finally let $b>1$. At $\omega=0$,
$$
R(0)=1<|b-c\omega|\big|_{\omega=0}=b,
$$
whereas $R(\omega)\sim\omega^2$ and $|b-c\omega|=O(\omega)$ as $\omega\to\infty$. By continuity there is some $\omega>0$ with
$$
R(\omega)=|b-c\omega|,
$$
and Step 2 again produces an imaginary root.

Step 5: Prove necessity in the remaining $b<1$ cases and state the region
Assume $0\leq b<1$ but
$$
a^2
\leq
c^2+2+
\max_{r>0}
\left(
\frac{2bc}{r}
-
\frac{1-b^2}{r^2}
-
r^2
\right).
$$
Then the inequality from Step 3 fails at some positive frequency. Since
$$
R(0)>b
$$
and both sides are continuous, there is a first $\omega_*>0$ such that
$$
R(\omega_*)=b+c\omega_*.
$$
This is the upper endpoint of the annulus in Step 2. Choose the two delayed feedback vectors to be aligned with each other and opposite to $P(i\omega_*)$. Their two phases can be realized independently by suitable nonnegative delays $\tau$ and $\sigma$. Then
$$
\Delta_{\tau,\sigma}(i\omega_*)=0,
$$
so the closed right half-plane is reached.

Combining this construction with Steps 3 and 4 gives the complete parameter region.
Final Answer: $\boxed{\{(a,b,c):b<1,\ a^2>c^2+2+\max_{r>0}(\frac{2bc}{r}-\frac{1-b^2}{r^2}-r^2)\}\cup\{(a,1,0):a^2\geq2\}}$

---

## Answer

$\{(a,b,c):b<1,\ a^2>c^2+2+\max_{r>0}(\frac{2bc}{r}-\frac{1-b^2}{r^2}-r^2)\}\cup\{(a,1,0):a^2\geq2\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Interval or region description

---

## Solution Concepts

- delay root loci
- subharmonic maximum principle
- phase annulus geometry
- frequency-domain inequalities
- extremal frequency margin

---

## Black-Box Audit — no issues found
