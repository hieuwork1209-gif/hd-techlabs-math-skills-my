## Steps

Step 1: Derive the two phase transfer matrices for first differences

At a step $n$, let
$$
H_j=t_n-t_{n-j},\qquad j=1,\ldots,5.
$$
After translating $t_n$ to $0$, the BDF5 derivative weights are
$$
w_0=\sum_{m=1}^5\frac1{H_m},
$$
and, for $1\leq j\leq5$,
$$
w_j=
-\frac{\prod_{\substack{1\leq m\leq5\\m\ne j}}H_m}
{H_j\prod_{\substack{1\leq m\leq5\\m\ne j}}(H_m-H_j)}.
$$
For the test equation $y'=0$,
$$
\sum_{j=0}^5w_jy_{n-j}=0.
$$
Since $\sum_{j=0}^5w_j=0$, putting $d_n=y_n-y_{n-1}$ gives
$$
d_n=\beta_1d_{n-1}+\beta_2d_{n-2}+\beta_3d_{n-3}+\beta_4d_{n-4},
$$
where
$$
\beta_k=\frac{\sum_{j=k+1}^5w_j}{w_0}.
$$

Scale $h=1$. In the phase whose current step has length $1$,
$$
(H_1,\ldots,H_5)
=
(1,1+r,2+r,2+2r,3+2r).
$$
If
$$
D=r(2r+1)(4r^3+30r^2+63r+40),
$$
substitution in the weight formula gives
$$
\beta_1=\frac{46r^3+171r^2+200r+72}{D},
$$
$$
\beta_2=-\frac{r(32r^3+130r^2+173r+76)}{D},
$$
$$
\beta_3=\frac{(r+2)(14r^2+31r+18)}{D},
$$
$$
\beta_4=-\frac{2r(2r+1)(r+1)(r+2)}{D}.
$$
Let $T(r)$ be the companion matrix with first row $(\beta_1,\beta_2,\beta_3,\beta_4)$. In the other phase the cumulative distances, after division by the current step length $r$, are exactly the preceding distances with $r$ replaced by $1/r$. The two-step monodromy for first differences is therefore
$$
M(r)=T(1/r)T(r).
$$

Step 2: Reduce the monodromy polynomial by the reciprocal step-ratio symmetry

Put
$$
u=r+\frac1r.
$$
The matrices $M(r)$ and $M(1/r)$ are cyclic products of the same two factors, so they have the same nonzero eigenvalues. The characteristic polynomial therefore depends on $r$ only through the reciprocal invariant $u$.

Multiplying the two companion matrices from Step 1 gives the characteristic coefficients in the usual principal-minor form: the $z^3$ coefficient is $-\operatorname{tr}M$, the $z^2$ coefficient is the sum of the $2\times2$ principal minors, the $z$ coefficient is minus the sum of the $3\times3$ principal minors, and the constant term is $\det M$. For example,
$$
\det M=\beta_4(r)\beta_4(1/r)=\frac{4(u+2)(2u+5)}{160u^3+1452u^2+4050u+3581}.
$$
Substituting the four displayed $\beta_k$ into those coefficient formulas and collecting reciprocal pairs $r^j+r^{-j}$ gives
$$
\det(zI-M(r))=\frac{P_u(z)}{A_4(u)},
$$
where
$$
P_u(z)=A_4z^4+A_3z^3+A_2z^2+A_1z+A_0
$$
and
$$
A_4=160u^3+1452u^2+4050u+3581,
$$
$$
A_3=304u^3+1348u^2+1530u+85,
$$
$$
A_2=16u^3+108u^2+314u+331,
$$
$$
A_1=-36u^2-170u-197,
\qquad
A_0=4(u+2)(2u+5).
$$
The denominator $A_4$ is positive for $u\geq2$.

Step 3: Exclude every nonreal unit-circle crossing

Let $z=e^{i\theta}$ be a zero of $P_u$ with $0<\theta<\pi$, and put $c=\cos\theta$. Dividing by $z^2$, the imaginary part is
$$
(A_4-A_0)\sin 2\theta+(A_3-A_1)\sin\theta=0.
$$
Because $\sin\theta\ne0$,
$$
c=-\frac{A_3-A_1}{2(A_4-A_0)}.
$$
Here
$$
A_4-A_0=160u^3+1444u^2+4014u+3541>0.
$$
Set
$$
D=A_4-A_0,\qquad B=A_3-A_1,\qquad C=A_3+A_1,\qquad E=A_4+A_0.
$$
Then $c=-B/(2D)$, so the real part becomes
$$
E(2c^2-1)+Cc+A_2
=
\frac{EB^2-CBD+2(A_2-E)D^2}{2D^2}.
$$
Equivalently,
$$
E(2c^2-1)+Cc+A_2
=
-\frac{16H(u)}{D^2},
$$
where the numerator identity
$$
32H(u)=2(E-A_2)D^2+CBD-EB^2
$$
expands to
$$
\begin{aligned}
H(u)={}&230400u^9+6166272u^8+72776096u^7+494393008u^6\\
&+2124814096u^5+5986899964u^4+11062602954u^3\\
&+12938115410u^2+8700086037u+2565772676.
\end{aligned}
$$
Every coefficient of $H$ is positive, so this real part cannot vanish for $u\geq2$. A parasitic multiplier can therefore meet the unit circle only at $z=1$ or $z=-1$.

At those two points,
$$
P_u(1)=480(u+2)^3>0,
$$
while
$$
P_u(-1)=-32F(u),
\qquad
F(u)=4u^3-8u^2-95u-127.
$$

Step 4: Locate the stability boundary and include the endpoint

At $u=2$, corresponding to constant steps, the Cayley substitution
$$
z=\frac{1+x}{1-x}
$$
transforms $P_2$ into
$$
10144x^4+51200x^3+110440x^2+97800x+30720.
$$
For a quartic $a_4x^4+a_3x^3+a_2x^2+a_1x+a_0$, the Routh-Hurwitz test requires positive coefficients together with
$$
a_3a_2-a_4a_1>0
$$
and
$$
a_3a_2a_1-a_4a_1^2-a_3^2a_0>0.
$$
Here these two determinants are
$$
4662444800
$$
and
$$
375456464640000,
$$
so all four roots of $P_2$ lie strictly inside the unit disk.

The coefficients of $P_u$ vary continuously with $u$, and Step 3 shows that roots cannot leave the disk except through $z=-1$. Now
$$
F(6)=-121<0,
\qquad
F(7)=188>0.
$$
Also
$$
F'(u)=12u^2-16u-95
$$
has only one positive zero before $6$, so $F$ is strictly increasing on $[6,\infty)$. There is therefore a unique
$$
u_*\in(6,7)
$$
with $F(u_*)=0$.

For $2\leq u<u_*$, no unit-circle crossing occurs, so all parasitic multipliers stay strictly inside the disk. At $u=u_*$, $z=-1$ is a simple root because
$$
\frac{\partial P_u}{\partial z}(-1)
=
24(10u^3-84u^2-517u-622),
$$
which is negative throughout $6<u<7$. The remaining roots stay inside the disk.

For $u>u_*$, $P_u(-1)<0$, while the leading coefficient $A_4$ is positive and $P_u(z)\to+\infty$ as $z\to-\infty$. It follows that $P_u$ has a real root less than $-1$, and zero-stability fails.

Use state coordinates consisting of one base value together with four consecutive first differences. Over one two-step period, the state matrix is block upper triangular with diagonal blocks $[1]$ and $M(r)$. Since $P_u(1)>0$, the consistency multiplier $1$ is not an eigenvalue of $M(r)$. At the boundary the only parasitic unit multiplier is the simple value $-1$, so every unit-modulus multiplier of the full recurrence is semisimple and every homogeneous solution remains bounded.

Step 5: Recover the step-ratio interval and the requested exact scalar

Since
$$
u=r+\frac1r,
$$
the condition $2\leq u\leq u_*$ is equivalent to
$$
r_-\leq r\leq r_+,
$$
where
$$
r_\pm=
\frac{u_*\pm\sqrt{u_*^2-4}}{2},
\qquad
r_-r_+=1.
$$
Numerically,
$$
u_*\approx6.4474256391,
\qquad
r_-\approx0.1590228935,
\qquad
r_+\approx6.2884027456.
$$
By definition of the root notation in the problem,
$$
u_*=
\operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127).
$$

Final Answer: $\boxed{\operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127)}$

---

## Answer

$\operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- variable-step backward differentiation formulas
- first-difference transfer matrices
- Floquet monodromy
- unit-circle root exclusion
- Routh-Hurwitz stability criterion
