## Steps

Step 1: Reduce the transport network to a boundary recurrence
Consider
$$
u_t+u_x=0,\qquad 0<x<1,
$$
$$
v_t+v_x=0,\qquad 0<x<3,
$$
with boundary coupling
$$
u(t,0)=a u(t,1)+v(t,3),\qquad v(t,0)=-b u(t,1),
$$
where $a,b>0$.
Let
$$p(t)=u(t,0).$$
By propagation along characteristics,
$$
u(t,1)=p(t-1),$$
and
$$
v(t,3)=v(t-3,0)=-b u(t-3,1)=-b p(t-4).$$
Hence the boundary trace satisfies
$$
p(t)=a p(t-1)-b p(t-4).
$$
For each $s\in[0,1)$, the sequence $p_n(s)=p(s+n)$ obeys the same fourth-order recurrence
$$
p_n=a p_{n-1}-b p_{n-4},
$$
with characteristic polynomial
$$
P(z)=z^4-a z^3+b.
$$
Thus all boundary traces decay exponentially, uniformly in the phase $s$, exactly when every zero of $P$ lies in the open unit disk. Since every interior value of $u$ or $v$ is a time translate of a boundary trace along a characteristic, this is equivalent to exponential stability of the transport semigroup in $L^2(0,1)\times L^2(0,3)$.

Step 2: Apply the first Schur reduction
For a real polynomial
$$
R(z)=z^n+c_1z^{n-1}+\cdots+c_n
$$
with $|c_n|<1$, Schur reduction says that all zeros of $R$ lie in $|z|<1$ exactly when all zeros of
$$
\frac{R(z)-c_n z^nR(1/z)}{z}
$$
lie in $|z|<1$.
Applying this to
$$P(z)=z^4-a z^3+b$$
first requires
$$0<b<1.$$
Moreover,
$$
P(z)-b z^4P(1/z)
=(1-b^2)z^4-a z^3+abz.
$$
After dividing by $z(1-b^2)$, the reduced cubic is
$$
Q(z)=z^3-Az^2+B,
$$
where
$$
A=\frac{a}{1-b^2},\qquad B=\frac{ab}{1-b^2}.
$$

Step 3: Reduce the cubic to a quadratic
For $Q$ to be Schur stable we need $0<B<1$, and a second Schur reduction gives
$$
(1-B^2)z^2-Az+AB.
$$
A real quadratic $\alpha z^2+\beta z+\gamma$ with $\alpha>0$ is Schur stable exactly when
$$
|\gamma|<\alpha,\qquad \alpha+\beta+\gamma>0,\qquad \alpha-\beta+\gamma>0.
$$
Here the last inequality is automatic. The condition
$$
AB<1-B^2
$$
becomes
$$
a^2b(1+b)<(1-b^2)^2,
$$
that is,
$$
a<(1-b)\sqrt{\frac{1+b}{b}}.
$$
The condition
$$
1-B^2-A+AB>0
$$
becomes, after multiplying by $(1-b^2)^2$,
$$
(1-b)b\left(a-(1+b)\right)
\left(a-\frac{1-b^2}{b}\right)>0.
$$
Also $B<1$ is
$$
a<\frac{1-b^2}{b}.
$$
Under this last inequality, the factored condition above is equivalent to
$$
a<1+b
$$
whenever it is active. Since
$$
(1-b)\sqrt{\frac{1+b}{b}}<\frac{1-b^2}{b},
$$
the $B<1$ bound is redundant once the quadratic Schur bound is imposed.

Step 4: State the exact stability region
Combining the conditions gives
$$
0<b<1,
\qquad
0<a<1+b,
\qquad
0<a<(1-b)\sqrt{\frac{1+b}{b}}.
$$
Therefore the transport network is exponentially stable exactly for
$$
0<b<1,
\qquad
0<a<\min\left\{1+b,(1-b)\sqrt{\frac{1+b}{b}}\right\}.
$$
Final Answer: $\boxed{\{(a,b):0<b<1,0<a<\min\{1+b,(1-b)\sqrt{(1+b)/b}\}\}}$

---

## Answer

$\{(a,b):0<b<1,0<a<\min\{1+b,(1-b)\sqrt{(1+b)/b}\}\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- transport semigroups
- boundary feedback systems
- method of characteristics
- Schur stability
- Schur-Cohn reduction

---

## Black-Box Audit — no issues found
