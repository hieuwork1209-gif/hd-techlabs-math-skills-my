## Steps

Step 1: Reduce right-half-plane roots to a boundary modulus problem
For a fixed delay $\tau\geq0$, write
$$
P(\lambda)=\lambda^2+a\lambda+1,
\qquad
Q(\lambda)=b+c\lambda.
$$
The characteristic equation is
$$
P(\lambda)+Q(\lambda)e^{-\lambda\tau}=0.
$$
Because $a>0$, the two zeros of $P$ have negative real part. Therefore
$$
H(\lambda)=\frac{Q(\lambda)}{P(\lambda)}
$$
is analytic on the open right half-plane and continuous on its boundary. Also $H(\lambda)\to0$ as $|\lambda|\to\infty$ in that half-plane.

If $\lambda$ is a characteristic root with $\operatorname{Re}\lambda\geq0$, then
$$
H(\lambda)=-e^{\lambda\tau},
$$
so
$$
|H(\lambda)|=e^{\tau\operatorname{Re}\lambda}\geq1.
$$
Therefore a delay-independent exclusion of right-half-plane roots is controlled by the maximum of $|H|$ on the imaginary axis. On large right half-disks, the maximum modulus principle applies to $H$; letting the radius tend to infinity shows that if $|H(i\omega)|\leq1$ for all real $\omega$, then $|H(\lambda)|<1$ whenever $\operatorname{Re}\lambda>0$.

Step 2: Compute the imaginary-axis modulus gap
For real $\omega$,
$$
|P(i\omega)|^2
=
(1-\omega^2)^2+a^2\omega^2,
$$
while
$$
|Q(i\omega)|^2
=
b^2+c^2\omega^2.
$$
Set
$$
u=\omega^2\geq0.
$$
Then
$$
D(u)
:=
|P(i\omega)|^2-|Q(i\omega)|^2
=
u^2+(a^2-c^2-2)u+1-b^2.
$$
$|H(i\omega)|<1$ is therefore equivalent to $D(u)>0$.

Step 3: Characterize when the gap stays positive
First suppose $0\leq b<1$. Then
$$
B:=1-b^2>0.
$$
Write
$$
A:=a^2-c^2-2,
$$
so
$$
D(u)=u^2+Au+B.
$$
If $A\geq0$, the minimum of $D$ on $u\geq0$ is $D(0)=B>0$. If $A<0$, the minimum occurs at $u=-A/2>0$ and equals
$$
B-\frac{A^2}{4}.
$$
This gives
$
D(u)>0\quad\text{for all }u\geq0
$
exactly when
$$
A>-2\sqrt{B},
$$
or
$$
a^2>c^2+2-2\sqrt{1-b^2}.
$$

Now suppose $b=1$. Then
$$
D(u)=u(u+A).
$$
For every $u>0$ this is positive exactly when
$$
A\geq0,
$$
that is,
$$
a^2\geq c^2+2.
$$
At $u=0$ equality gives $|H(0)|=1$, but $\lambda=0$ is not a characteristic root because
$$
P(0)+Q(0)=1+b=2.
$$

Step 4: Establish sufficiency of the two parameter regimes
Assume first that
$$
0\leq b<1,
\qquad
a^2>c^2+2-2\sqrt{1-b^2}.
$$
Step 3 gives $D(u)>0$ for every $u\geq0$, so
$$
|H(i\omega)|<1
$$
for every real $\omega$. Step 1 then gives $|H(\lambda)|<1$ throughout the open right half-plane. A characteristic root there would require $|H(\lambda)|\geq1$, which is impossible. No imaginary-axis root exists either because the boundary inequality is strict.

Next assume
$$
b=1,
\qquad
a^2\geq c^2+2.
$$
Then Step 3 gives
$$
|H(i\omega)|<1
$$
for every $\omega\neq0$, while $|H(0)|=1$. The maximum modulus argument still gives $|H(\lambda)|<1$ in the open right half-plane, since $H$ is nonconstant and tends to $0$ at infinity. The only boundary point where equality in modulus occurs is $\lambda=0$, and that point is not a characteristic root. Every characteristic root therefore has negative real part for every $\tau\geq0$.

Step 5: Establish necessity by constructing a critical delay
If $b>1$, then
$$
D(0)=1-b^2<0,
$$
while $D(u)\to\infty$ as $u\to\infty$, so $D$ has a positive zero.

If $0\leq b<1$ but
$$
a^2\leq c^2+2-2\sqrt{1-b^2},
$$
then the quadratic from Step 3 has a zero at some $u>0$. If $b=1$ and $a^2<c^2+2$, then
$$
D(u)=u(u+A)
$$
has the positive zero $u=-A$.

In every excluded case there is therefore some $\omega>0$ for which
$$
|P(i\omega)|=|Q(i\omega)|.
$$
The value $Q(i\omega)$ cannot vanish at such a point, because then $P(i\omega)$ would also vanish, contradicting $a>0$. Hence
$$
-\frac{P(i\omega)}{Q(i\omega)}
$$
lies on the unit circle. Choose $\tau\geq0$ so that
$$
e^{-i\omega\tau}
=
-\frac{P(i\omega)}{Q(i\omega)}.
$$
Then $\lambda=i\omega$ is a characteristic root, so the required strict left-half-plane property fails. Combining this with Step 4 gives the complete parameter region.
Final Answer: $\boxed{\{(a,b,c):b<1,\ a^2>c^2+2-2\sqrt{1-b^2}\}\cup\{(a,1,c):a^2\geq c^2+2\}}$

---

## Answer

$\{(a,b,c):b<1,\ a^2>c^2+2-2\sqrt{1-b^2}\}\cup\{(a,1,c):a^2\geq c^2+2\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Interval or region description

---

## Solution Concepts

- delay-independent stability
- characteristic quasipolynomials
- maximum modulus principle
- frequency-domain inequalities
- quadratic minimization

---

## Black-Box Audit — no issues found
