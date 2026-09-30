## Steps

Step 1: Build a cubic majorant for the tail indicator
Let
$$
I(z)=
\begin{cases}
0,&0\leq z<\frac{1}{2},\\
1,&\frac{1}{2}\leq z\leq1.
\end{cases}
$$
Only the first three moments are prescribed, so a cubic polynomial can be integrated exactly from the given data. For
$$
0\leq r<\frac{1}{2},
$$
write
$$
q_r(z)=(z-r)^2(Az+B).
$$
The two remaining contact conditions
$$
q_r\left(\frac{1}{2}\right)=q_r(1)=1
$$
become
$$
A+B=\frac{1}{(1-r)^2},
\qquad
\frac{A}{2}+B=\frac{4}{(1-2r)^2}.
$$
Therefore
$$
A=
\frac{2}{(1-r)^2}
-
\frac{8}{(1-2r)^2},
\qquad
B=
\frac{8}{(1-2r)^2}
-
\frac{1}{(1-r)^2}.
$$
Substitution and collection of the linear factor give
$$
q_r(z)
=
\frac{(z-r)^2\left(4r^2+8rz-12r-6z+7\right)}
{(1-r)^2(1-2r)^2}.
$$

The linear factor in the numerator has coefficient
$$
8r-6<0
$$
in $z$, so its minimum on $[0,1]$ occurs at $z=1$, where it equals
$$
(1-2r)^2>0.
$$
Therefore
$$
q_r(z)\geq0
$$
for $0\leq z\leq1$, with equality only at $z=r$.

Also,
$$
q_r(z)-1
=
\frac{(z-1)(2z-1)\left(-6r^2+4rz+6r-3z-1\right)}
{(1-r)^2(1-2r)^2}.
$$
For $z\in[\frac{1}{2},1]$, the first two factors have product at most $0$. The last factor decreases with $z$, because
$$
4r-3<0,
$$
and at $z=\frac{1}{2}$ it is
$$
-6r^2+8r-\frac{5}{2}
=
-\frac{1}{2}(12r^2-16r+5)
\leq0
$$
for $0\leq r<\frac{1}{2}$. The inequality is strict there because the two roots of
$$
12r^2-16r+5=0
$$
are $1/2$ and $5/6$. Therefore the last factor is strictly negative on $[\frac{1}{2},1]$. It follows that
$$
q_r(z)\geq1
$$
throughout $[\frac{1}{2},1]$, with equality only at $z=1/2$ and $z=1$.

Every $q_r$ is therefore a valid cubic majorant:
$$
I(z)\leq q_r(z)
$$
on $[0,1]$.

Step 2: Determine the contact point forced by the moments
If a bound coming from $q_r$ is attained, the measure must be supported where the majorant meets the indicator. For $0\leq r<\frac{1}{2}$, those contact points are
$$
r,
\qquad
\frac{1}{2},
\qquad
1.
$$
Seek a probability measure
$$
\nu
=
a\delta_r+b\delta_{1/2}+c\delta_1
$$
with the required moments. The equations for total mass and the first two moments are
$$
a+b+c=1,
$$
$$
ar+\frac{b}{2}+c=\frac{1}{3},
$$
$$
ar^2+\frac{b}{4}+c=\frac{1}{5}.
$$
Subtracting the second equation from the first and the third from the second gives
$$
a(1-r)+\frac{b}{2}=\frac{2}{3},
$$
$$
ar(1-r)+\frac{b}{4}=\frac{2}{15}.
$$
Set
$$
A=a(1-r).
$$
Then
$$
A+\frac{b}{2}=\frac{2}{3},
\qquad
rA+\frac{b}{4}=\frac{2}{15}.
$$
Eliminating $b$ yields
$$
A=\frac{2}{5(1-2r)},
$$
and then
$$
a=\frac{2}{5(1-r)(1-2r)},
\qquad
b=\frac{8(1-5r)}{15(1-2r)}.
$$

The third moment condition is
$$
ar^3+\frac{b}{8}+c=\frac{1}{7}.
$$
Subtract it from the second-moment equation to obtain
$$
ar^2(1-r)+\frac{b}{8}
=
\frac{2}{35}.
$$
Substituting the formulas for $A=a(1-r)$ and $b$ gives
$$
\frac{6r^2-5r+1}{15(1-2r)}
=
\frac{2}{35}.
$$
After clearing denominators,
$$
42r^2-23r+1=0,
$$
or
$$
(21r-1)(2r-1)=0.
$$
Since $r<1/2$,
$$
r=\frac{1}{21}.
$$

The corresponding weights are
$$
a=\frac{441}{950},
\qquad
b=\frac{128}{285},
\qquad
c=\frac{13}{150}.
$$
They are positive and sum to $1$. Therefore
$$
\nu_*=
\frac{441}{950}\delta_{1/21}
+
\frac{128}{285}\delta_{1/2}
+
\frac{13}{150}\delta_1
$$
is an admissible probability measure.

Step 3: Use the sharp certificate to obtain the maximum
Substituting
$$
r=\frac{1}{21}
$$
into the cubic from Step 1 gives
$$
q_*(z)
=
\frac{(21z-1)^2(2839-2478z)}{144400}.
$$
The factorization
$$
q_*(z)-1
=
-\frac{1323}{144400}
(z-1)(2z-1)(413z+107)
$$
shows that the equality set of
$$
I(z)\leq q_*(z)
$$
is exactly
$$
\left\{
\frac{1}{21},
\frac{1}{2},
1
\right\}.
$$

Let $\nu$ be any admissible probability measure. Since $q_*$ has degree at most $3$, its integral depends only on the prescribed moments. Therefore
$$
\int_0^1q_*(z)\,d\nu(z)
=
\int_0^1q_*(z)\,d\nu_*(z).
$$
The measure $\nu_*$ is supported on contact points, so
$$
q_*(z)=I(z)
$$
at every point of its support. Therefore,
$$
\begin{aligned}
\nu\left(\left[\frac{1}{2},1\right]\right)
&=
\int_0^1I(z)\,d\nu(z)\\
&\leq
\int_0^1q_*(z)\,d\nu(z)\\
&=
\int_0^1q_*(z)\,d\nu_*(z)\\
&=
\nu_*\left(\left[\frac{1}{2},1\right]\right)\\
&=
\frac{128}{285}+\frac{13}{150}\\
&=
\frac{509}{950}.
\end{aligned}
$$
The upper bound is attained by $\nu_*$.

Step 4: Close the equality case
If an admissible measure $\nu$ attains the value $509/950$, then
$$
\int_0^1\left(q_*(z)-I(z)\right)\,d\nu(z)=0.
$$
The integrand is nonnegative on $[0,1]$ and vanishes only at
$$
\frac{1}{21},
\qquad
\frac{1}{2},
\qquad
1.
$$
Therefore $\nu$ must be supported on these three points. The moment equations solved in Step 2 then force the weights to be
$$
\frac{441}{950},
\qquad
\frac{128}{285},
\qquad
\frac{13}{150}.
$$
Therefore the extremizer is unique, and the maximum tail mass is
$$
\frac{509}{950}.
$$
Final Answer: $\boxed{\frac{509}{950}}$

---

## Answer

$\frac{509}{950}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- truncated moment problems
- polynomial majorants
- atomic extremal measures
- moment matching
- equality-case analysis
