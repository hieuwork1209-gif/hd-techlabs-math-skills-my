## Steps

Step 1: Encode the fixed moments

Let
$$
m_0=1,\qquad m_1=\frac12,
$$
$$
m_2=\frac{a+1}{2(2a+1)},\qquad
m_3=\frac{a+2}{4(2a+1)}.
\tag{1}
$$
For any admissible random variable $X$ and every cubic polynomial
$$
q(x)=c_0+c_1x+c_2x^2+c_3x^3,
$$
its expectation is fixed:
$$
E q(X)=c_0m_0+c_1m_1+c_2m_2+c_3m_3.
\tag{2}
$$
Thus a cubic minorant or majorant of
$$
h_t(x):=\frac1{1+tx},\qquad 0\le x\le1,
\tag{3}
$$
gives a universal lower or upper bound for $E h_t(X)$.

The special form (3) makes such certificates exact. For every cubic $q$ define
$$
N_q(x):=1-(1+tx)q(x).
\tag{4}
$$
Then $N_q$ has degree at most $4$ and
$$
h_t(x)-q(x)=\frac{N_q(x)}{1+tx}.
\tag{5}
$$
Since $1+tx>0$ on $[0,1]$, the sign of $h_t-q$ is exactly the sign of the quartic $N_q$. This is why contact patterns of total multiplicity four are the natural sharp certificates for the three prescribed moments.

Step 2: Construct the sharp lower certificate

A nonnegative quartic with two interior contact points must have even multiplicity at each contact, so the natural sharp pattern is two double roots. The corresponding two support points are forced by the moment equations.

Let
$$
r(x)=x^2+ux+v
$$
be the monic quadratic orthogonal, with respect to the moment functional (1), to both $1$ and $x$. Thus
$$
m_2+u m_1+v=0,
$$
$$
m_3+u m_2+v m_1=0.
$$
Substituting (1) gives
$$
u=-1,
\qquad
v=\frac{a}{2(2a+1)}.
\tag{6}
$$
Hence
$$
r(x)=x^2-x+\frac{a}{2(2a+1)}
=(x-c_-)(x-c_+),
$$
where
$$
c_\pm=\frac12\left(1\pm\frac1{\sqrt{2a+1}}\right).
\tag{7}
$$
Because $a>0$, both points lie in $(0,1)$.

Let $\nu_-$ be the probability measure assigning mass $1/2$ to each of $c_-$ and $c_+$. Since $c_-+c_+=1$, its mean is $1/2$. Also $r(c_\pm)=0$ gives
$$
c_\pm^2=c_\pm-v,
$$
so
$$
E_{\nu_-}X^2=\frac12-v
=\frac{a+1}{2(2a+1)}=m_2.
$$
Multiplying $x^2=x-v$ by $x$ gives
$$
x^3=(1-v)x-v
$$
on the two support points, hence
$$
E_{\nu_-}X^3
=\frac{1-v}{2}-v
=\frac{a+2}{4(2a+1)}=m_3.
$$
Thus $\nu_-$ is admissible.

Now let $q_-$ be the unique cubic satisfying the four Hermite contact conditions
$$
q_-(c_\pm)=h_t(c_\pm),
\qquad
q_-'(c_\pm)=h_t'(c_\pm).
\tag{8}
$$
Uniqueness holds because the difference of two such cubics would have the two distinct roots $c_-,c_+$ each with multiplicity at least two, hence would be the zero polynomial.

By (4) and (8), $N_{q_-}$ is a quartic having $c_-$ and $c_+$ as double roots, so
$$
N_{q_-}(x)=C_-r(x)^2
\tag{9}
$$
for some constant $C_-$. Evaluate (9) at $x=-1/t$. Since
$$
N_{q_-}(-1/t)=1,
$$
we get
$$
C_-\,r(-1/t)^2=1,
$$
so $C_->0$. Therefore (5) and (9) give
$$
q_-(x)\le h_t(x)
\qquad(0\le x\le1).
\tag{10}
$$
For every admissible $X$, equations (2) and (10) imply
$$
E h_t(X)\ge E q_-(X).
$$
The right side depends only on the moments, so it equals its value under $\nu_-$. By the contact conditions (8),
$$
E q_-(X)=E_{\nu_-}q_-=E_{\nu_-}h_t.
$$
Hence $\nu_-$ attains the infimum.

Using (7),
$$
\begin{aligned}
L_a(t)
&:=\inf E h_t(X)\\
&=\frac12\left(\frac1{1+tc_-}+\frac1{1+tc_+}\right).
\end{aligned}
$$
Since
$$
c_-+c_+=1,
\qquad
c_-c_+=\frac{a}{2(2a+1)},
$$
this simplifies to
$$
L_a(t)=
\frac{(2a+1)(t+2)}{a t^2+4at+4a+2t+2}.
\tag{11}
$$

Step 3: Construct the sharp upper certificate

For an upper certificate, $N_q$ must be nonpositive on $[0,1]$. A sharp quartic may therefore have simple zeros at the two endpoints and one double zero in the interior. The moment equations force the corresponding three-point support.

Suppose the support is $\{0,c,1\}$. Its vanishing cubic is
$$
s_c(x)=x(x-1)(x-c)
=x^3-(1+c)x^2+cx.
$$
For any probability measure on these three points matching the moments, necessarily
$$
E s_c(X)=0.
$$
Using (1), this condition is
$$
m_3-(1+c)m_2+c m_1=0.
$$
Because
$$
m_2-m_3=\frac{a}{4(2a+1)},
\qquad
m_1-m_2=\frac{a}{2(2a+1)},
$$
we obtain
$$
c=\frac{m_2-m_3}{m_1-m_2}=\frac12.
\tag{12}
$$
Thus the interior support point is forced to be $1/2$.

Let the masses at $0$ and $1$ both be $\eta$ and the mass at $1/2$ be $1-2\eta$. The mean is automatically $1/2$. Matching the second moment gives
$$
\eta+\frac{1-2\eta}{4}=m_2,
$$
so
$$
\eta=\frac1{2(2a+1)}.
\tag{13}
$$
Then
$$
1-2\eta=\frac{2a}{2a+1}>0,
$$
and the third moment is
$$
\eta+\frac{1-2\eta}{8}
=\frac{a+2}{4(2a+1)}=m_3.
$$
Hence the probability measure
$$
\nu_+
=\frac1{2(2a+1)}\delta_0
+\frac{2a}{2a+1}\delta_{1/2}
+\frac1{2(2a+1)}\delta_1
\tag{14}
$$
is admissible.

Let $q_+$ be the unique cubic satisfying
$$
q_+(0)=h_t(0),
\qquad
q_+(1)=h_t(1),
$$
$$
q_+(1/2)=h_t(1/2),
\qquad
q_+'(1/2)=h_t'(1/2).
\tag{15}
$$
Again uniqueness follows because a difference polynomial would have zeros at $0$ and $1$ and a double zero at $1/2$, four zeros counted with multiplicity.

The quartic $N_{q_+}$ therefore has the same contact multiplicities, so
$$
N_{q_+}(x)
=C_+x(x-1)(x-1/2)^2.
\tag{16}
$$
At $x=-1/t$, the product on the right of (16) is positive and $N_{q_+}(-1/t)=1$, hence $C_+>0$. For $0\le x\le1$,
$$
x(x-1)(x-1/2)^2\le0,
$$
so (5) and (16) give
$$
h_t(x)\le q_+(x).
\tag{17}
$$
As in Step 2, for every admissible $X$,
$$
E h_t(X)\le E q_+(X)
=E_{\nu_+}q_+
=E_{\nu_+}h_t.
$$
Thus $\nu_+$ attains the supremum.

From (14),
$$
\begin{aligned}
U_a(t)
&:=\sup E h_t(X)\\
&=\frac1{2(2a+1)}
+\frac{2a}{2a+1}\frac1{1+t/2}
+\frac1{2(2a+1)}\frac1{1+t}\\
&=\frac{8at+8a+t^2+4t+4}
{2(2a+1)(t+1)(t+2)}.
\end{aligned}
\tag{18}
$$

Step 4: Subtract the two sharp bounds

By (11) and (18),
$$
\Delta_a(t)=U_a(t)-L_a(t).
$$
Putting the two terms over a common denominator and simplifying gives
$$
\Delta_a(t)
=
\frac{a t^4}
{2(2a+1)(t+1)(t+2)(a t^2+4at+4a+2t+2)}.
\tag{19}
$$
Both extrema are attained by the explicit admissible measures $\nu_+$ and $\nu_-$, so no compactness or limiting argument is needed.

## Solution Concepts

- Cubic moment duality for expectations under three fixed moments.
- Canonical two-point and endpoint three-point extremal measures forced by quartic contact patterns.
- Exact polynomial sign certificates for the resolvent $1/(1+tX)$.

Final Answer: $\displaystyle \frac{a t^4}{2(2a+1)(t+1)(t+2)(a t^2+4at+4a+2t+2)}$.
