## Steps

Step 1: Reduce the alternating BDF5 recurrence to a two-phase Floquet determinant

For one phase, scale the current step to length $1$ and write the other step ratio as $\rho>0$. The five backward distances are
$$
H(\rho)=(1,1+\rho,2+\rho,2+2\rho,3+2\rho).
$$
After translating the current time to $0$, the derivative weights are
$$
w_0(\rho)=\sum_{m=1}^{5}\frac{1}{H_m},
$$
and, for $1\leq j\leq5$,
$$
w_j(\rho)=-\frac{\prod_{\substack{1\leq m\leq5\\m\ne j}}H_m}{H_j\prod_{\substack{1\leq m\leq5\\m\ne j}}(H_m-H_j)}.
$$
For $y'=0$,
$$
\sum_{j=0}^{5}w_j(\rho)y_{n-j}=0.
$$
Since the weights annihilate constants, $\sum_{j=0}^{5}w_j(\rho)=0$. Thus for $d_n=y_n-y_{n-1}$,
$$
d_n=\sum_{k=1}^{4}\beta_k(\rho)d_{n-k},
\qquad
\beta_k(\rho)=\frac{\sum_{j=k+1}^{5}w_j(\rho)}{w_0(\rho)}.
$$

The two alternating phases are $\rho=r$ and $\rho=1/r$. For a two-step Floquet multiplier $z$, write
$$
d_{2m}=az^m,\qquad d_{2m+1}=bz^m.
$$
Substitution into the two phase recurrences gives
$$
\begin{pmatrix}
z^2-\beta_2(r)z-\beta_4(r) & -\beta_1(r)z-\beta_3(r)\\
-\beta_1(1/r)z^2-\beta_3(1/r)z & z^2-\beta_2(1/r)z-\beta_4(1/r)
\end{pmatrix}
\binom{a}{b}=0.
$$
Hence the first-difference period multipliers are the zeros of this determinant.

Step 2: Derive the determinant coefficients and the Cayley polynomial explicitly

Set
$$
N(\rho)=4\rho^3+30\rho^2+63\rho+40.
$$
Substituting the five distances from Step 1 into the weight formula and simplifying gives
$$
w_0(\rho)=\frac{N(\rho)}{2(\rho+1)(\rho+2)(2\rho+3)},
$$
$$
w_1(\rho)=-\frac{(\rho+2)(2\rho+3)}{\rho(2\rho+1)},\qquad
w_2(\rho)=\frac{2(2\rho+3)}{\rho(\rho+1)},
$$
$$
w_3(\rho)=-\frac{2(2\rho+3)}{\rho(\rho+2)},\qquad
w_4(\rho)=\frac{(\rho+2)(2\rho+3)}{2\rho(\rho+1)(2\rho+1)},\qquad
w_5(\rho)=-\frac{1}{2\rho+3}.
$$
Therefore the four coefficients of the first-difference recurrence are
$$
\beta_1(\rho)=\frac{46\rho^3+171\rho^2+200\rho+72}{\rho(2\rho+1)N(\rho)},
$$
$$
\beta_2(\rho)=-\frac{32\rho^3+130\rho^2+173\rho+76}{(2\rho+1)N(\rho)},
$$
$$
\beta_3(\rho)=\frac{(\rho+2)(14\rho^2+31\rho+18)}{\rho(2\rho+1)N(\rho)},
\qquad
\beta_4(\rho)=-\frac{2(\rho+1)(\rho+2)}{N(\rho)}.
$$

Write $\widehat\beta_k=\beta_k(1/r)$. Expanding the determinant from Step 1 gives
$$
\Delta_r(z)=z^4+c_3z^3+c_2z^2+c_1z+c_0,
$$
where
$$
c_3=-\beta_2(r)-\widehat\beta_2-\beta_1(r)\widehat\beta_1,
$$
$$
c_2=\beta_2(r)\widehat\beta_2-\beta_4(r)-\widehat\beta_4-\beta_1(r)\widehat\beta_3-\beta_3(r)\widehat\beta_1,
$$
$$
c_1=\beta_2(r)\widehat\beta_4+\beta_4(r)\widehat\beta_2-\beta_3(r)\widehat\beta_3,
\qquad
c_0=\beta_4(r)\widehat\beta_4.
$$
Put
$
u=r+\frac{1}{r},\qquad s=u+2.
$
Let
$
L=N(r)N(1/r).
$
Substituting the displayed $\beta_k$ into $c_3,c_2,c_1,c_0$, putting every term over the common denominator $L$, and pairing reciprocal powers gives
$
L=160\left(r^3+r^{-3}\right)+1452\left(r^2+r^{-2}\right)+4530\left(r+r^{-1}\right)+6485,
$
$
Lc_3=304\left(r^3+r^{-3}\right)+1348\left(r^2+r^{-2}\right)+2442\left(r+r^{-1}\right)+2781,
$
$
Lc_2=16\left(r^3+r^{-3}\right)+108\left(r^2+r^{-2}\right)+362\left(r+r^{-1}\right)+547,
$
$
Lc_1=-36\left(r^2+r^{-2}\right)-170\left(r+r^{-1}\right)-269,
$
$
Lc_0=8\left(r^2+r^{-2}\right)+36\left(r+r^{-1}\right)+56.
$
Now
$
r^2+r^{-2}=u^2-2,\qquad r^3+r^{-3}=u^3-3u,
$
so, after replacing $u$ by $s-2$,
$
L=160s^3+492s^2+162s+9>0.
$
Consequently
$
L\Delta_r(z)=P_s(z)=p_4z^4+p_3z^3+p_2z^2+p_1z+p_0,
$
where
$
p_4=160s^3+492s^2+162s+9,
$
$
p_3=304s^3-476s^2-214s-15,
$
$
p_2=16s^3+12s^2+74s+7,
$
$
p_1=-(36s^2+26s+1),\qquad p_0=4s(2s+1).
$

Now set
$$
z=\frac{1+x}{1-x},\qquad q_s(x)=\frac{(1-x)^4}{8}P_s\left(\frac{1+x}{1-x}\right).
$$
Thus
$$
q_s(x)=\frac{1}{8}\left[p_4(1+x)^4+p_3(1+x)^3(1-x)+p_2(1+x)^2(1-x)^2+p_1(1+x)(1-x)^3+p_0(1-x)^4\right].
$$
Collecting powers of $x$ gives
$$
q_s(x)=4D(s)x^4+2C(s)x^3+B(s)x^2+A(s)x+60s^3,
$$
where
$$
D(s)=-4s^3+32s^2+15s+1,
$$
$$
C(s)=2s^3+176s^2+63s+4,
$$
$$
B(s)=116s^3+372s^2+106s+5,
$$
$$
A(s)=156s^3+132s^2+32s+1.
$$
Indeed the five coefficients are respectively
$$
\frac{p_4-p_3+p_2-p_1+p_0}{8}=4D,
$$
$$
\frac{4p_4-2p_3+2p_1-4p_0}{8}=2C,
$$
$$
\frac{6p_4-2p_2+6p_0}{8}=B,
$$
$$
\frac{4p_4+2p_3-2p_1-4p_0}{8}=A,
\qquad
\frac{p_4+p_3+p_2+p_1+p_0}{8}=60s^3.
$$

Since $s=u+2$ for $u=r+1/r$,
$$
D(s)=-(4u^3-8u^2-95u-127).
$$
Let
$$
F(u)=4u^3-8u^2-95u-127.
$$
Then
$$
F(6)=-121,\qquad F\left(\frac{13}{2}\right)=16.
$$
Also $F'(u)=12u^2-16u-95$ has exactly one positive zero, smaller than $6$. Therefore $F$ decreases and then increases on $u\geq2$, so it has a unique zero $u_*$ in $(6,13/2)$, and $D(s)>0$ exactly for $2\leq u<u_*$.

Step 3: Prove Hurwitz stability below the threshold

Assume $2\leq u<u_*$. Then $4\leq s<17/2$, and $A,B,C,D$ are positive. Four inequalities control the quartic Routh-Hurwitz determinants.

First,
$$
C-10D=42s^3-144s^2-87s-6.
$$
Its value at $s=4$ is $30$. Its derivative is $126s^2-288s-87$, whose derivative is positive for $s\geq4$ and whose value at $4$ is positive. Hence $C>10D$.

Second,
$$
10B-9A=s^2(2532-244s)+772s+41>0
$$
because $s<17/2$. Hence $B>\frac{9}{10}A$, and therefore
$$
CB>9DA>8DA.
$$

Third,
$$
A-3C=150s^3-396s^2-157s-11.
$$
Its value at $s=4$ is $2625$. Its derivative is $450s^2-792s-157$, whose derivative is positive for $s\geq4$ and whose value at $4$ is positive. Hence $A>3C$.

Finally,
$$
B-160s^3=s^2(372-44s)+106s+5.
$$
Since $s<17/2$, the right-hand side is larger than $-2s^2+106s+5$, which is positive on $4\leq s<17/2$. Thus
$$
AB>480Cs^3.
$$

For
$$
q_s(x)=a_4x^4+a_3x^3+a_2x^2+a_1x+a_0,
$$
the coefficients are
$$
(a_4,a_3,a_2,a_1,a_0)=(4D,2C,B,A,60s^3).
$$
The quartic Routh-Hurwitz conditions reduce to
$$
a_3a_2-a_4a_1=2CB-4DA>0
$$
and
$$
a_3a_2a_1-a_4a_1^2-a_3^2a_0=2\left(CBA-2DA^2-120C^2s^3\right).
$$
From $CB>8DA$,
$$
2DA^2<\frac{1}{4} CBA,
$$
and from $AB>480Cs^3$,
$$
120C^2s^3<\frac{1}{4} CBA.
$$
Hence the second Hurwitz determinant is positive. All roots of $q_s$ satisfy $\operatorname{Re}x<0$. The Cayley map from Step 2 then gives $|z|<1$, so every first-difference period multiplier is strictly inside the unit disk for $2\leq u<u_*$.

Step 4: Include the boundary and exclude larger step ratios

At $u=u_*$, $D=0$, so the $x^4$ coefficient of $q_s$ vanishes while its $x^3$ coefficient is $2C>0$. This degree drop corresponds to a simple multiplier at $z=-1$ as follows. With $P_s$ from Step 2, define
$$
Q_s(x)=(1-x)^4P_s\left(\frac{1+x}{1-x}\right)=8q_s(x).
$$
The coefficient of $x^4$ in $Q_s$ is $P_s(-1)$. If $P_s(-1)=0$, factor $P_s(z)=(z+1)R_s(z)$; since $z+1=2/(1-x)$,
$$
Q_s(x)=2(1-x)^3R_s\left(\frac{1+x}{1-x}\right),
$$
so the coefficient of $x^3$ is $-2R_s(-1)=-2P_s'(-1)$. Therefore
$$
P_s(-1)=32D(s)=0,
\qquad
P_s'(-1)=-8C(s)\ne0,
$$
and $z=-1$ is a simple period multiplier.

The remaining three roots are strictly stable. The cubic Routh-Hurwitz condition is
$$
BA>(2C)(60s^3)=120Cs^3,
$$
which follows from $AB>480Cs^3$ in Step 3. Thus the endpoint is zero-stable.

For $u>u_*$, $D<0$. Also
$$
q_s(1)=2L(s)>0,
$$
while the leading coefficient $4D$ is negative, so $q_s(x)\to-\infty$ as $x\to+\infty$. Hence $q_s$ has a real zero $x_0>1$. The Cayley map gives
$$
z_0=\frac{1+x_0}{1-x_0}<-1,
$$
so zero-stability fails.

Finally, the full two-step state can be written as one base value together with four consecutive first differences. Its period matrix is block upper triangular with diagonal blocks $[1]$ and the first-difference monodromy. Since $q_s(0)=60s^3>0$, $z=1$ is not a first-difference multiplier, while the boundary multiplier $z=-1$ is simple. Hence every unit-modulus multiplier is semisimple.

Step 5: Recover the lower endpoint and the requested scalar

For $r>0$,
$$
u=r+\frac{1}{r}\geq2.
$$
Steps 3 and 4 give zero-stability exactly when
$$
2\leq u\leq u_*.
$$
Equivalently,
$$
r_-\leq r\leq r_+,
\qquad
r_{\pm}=\frac{u_*\pm\sqrt{u_*^2-4}}{2},
\qquad
r_-r_+=1.
$$
Thus $r_-<1$ is the lower endpoint appearing in the prompt, and $u_*=r_-+1/r_-$. Since Step 2 shows that $u_*$ is the unique zero of $F$ in $(6,13/2)$, it is also the unique zero in $(6,7)$. Therefore
$$
u_*=\operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127).
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
- floquet multipliers
- cayley transform
- routh-hurwitz stability criterion
- reciprocal step-ratio symmetry
