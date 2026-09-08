## Steps

Step 1: Reduce the heavy-ball cycle to scalar residual recurrences
The Hessian is
$$
A=\operatorname{diag}(1,3,7).
$$
With $x_{-1}=x_0$ and momentum $\beta=1/3$, each eigencoordinate with eigenvalue $\lambda\in\{1,3,7\}$ is multiplied by scalar residuals
$$
q_0(\lambda)=1,
\qquad q_1(\lambda)=1-\alpha_0\lambda,
$$
$$
q_2(\lambda)=\left(\frac43-\alpha_1\lambda\right)q_1(\lambda)-\frac13,
$$
$$
q_3(\lambda)=\left(\frac43-\alpha_2\lambda\right)q_2(\lambda)-\frac13q_1(\lambda).
$$
Therefore
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\max_{\lambda\in\{1,3,7\}}
\max\left\{\frac14|q_1(\lambda)|,\frac12|q_2(\lambda)|,|q_3(\lambda)|\right\}.
$$

Step 2: Define the candidate algebraic optimizer
Let $t$ be the unique real root of
$$
P(z)=1463z^3-1438z^2+471z-48.
$$
The discriminant of $P$ is $-671179008<0$, so there is exactly one real root. Moreover
$$
P\!\left(\frac{19}{100}\right)<0,
\qquad
P\!\left(\frac15\right)>0,
$$
so
$$
\frac{19}{100}<t<\frac15.
$$
Define
$$
r_*:=\frac{1-t}{4},
\qquad
a_*:=t,
$$
$$
b_*:=\frac{5t-3}{6(t-1)}=\frac{3-5t}{6(1-t)},
$$
$$
c_*:=\frac{2(29t^2-19t+2)}{3(105t^2-67t+8)}.
$$
The above interval for $t$ gives $0<a_*,b_*,c_*<1/2$. Numerically,
$$
t\approx0.1948313835,
\quad b_*\approx0.4193413738,
\quad c_*\approx0.3751492009,
\quad r_*\approx0.2012921541.
$$

Step 3: The first two prefixes force a narrow feasible strip
Write
$$
a=\alpha_0,\qquad b=\alpha_1,\qquad c=\alpha_2,
$$
and suppose $R\le r_*$. From the one-step constraint at $\lambda=1$,
$$
\frac14(1-a)\le r_*,
$$
so $a\ge t$. Since $t>1/7$, the one-step constraint at $\lambda=7$ gives
$$
7a-1\le1-t,
\qquad\text{hence}\qquad
 a\le\frac{2-t}{7}. \tag{1}
$$
On this range $q_2(1)>0$, hence $q_2(1)\le2r_*$ yields
$$
b\ge L(a):=\frac43-\frac{5-3t}{6(1-a)}. \tag{2}
$$
Also $q_2(7)$ is increasing in $b$. At $b=L(a)$,
$$
q_2(7)=\frac{-112a^2+49at+47a-7t-5}{2(1-a)}>0.
$$
Indeed the numerator is concave in $a$, and at the two endpoints of (1) it equals
$$
-63t^2+40t-5>0,
\qquad
-\frac{65t^2-66t+5}{7}>0.
$$
Thus the constraint $q_2(7)\le2r_*$ gives
$$
b\le U(a):=\frac17\left(\frac43+\frac{5-3t}{6(7a-1)}\right). \tag{3}
$$
Feasibility requires $L(a)\le U(a)$. Since
$$
L(a)-U(a)
=\frac{56a^2-24at-24a+3t+3}{7(a-1)(7a-1)},
$$
and the denominator is negative, we must have
$$
N(a,t):=56a^2-24at-24a+3t+3\ge0. \tag{4}
$$
Now $N$ is convex in $a$, while
$$
N\!\left(\frac{11}{50},t\right)
=-\frac{1425t-269}{625}<0
$$
and, using the upper endpoint from (1),
$$
N\!\left(\frac{2-t}{7},t\right)
=\frac{32t^2-35t+5}{7}<0.
$$
Hence (4) rules out $a\ge11/50$. Therefore
$$
t\le a<\frac{11}{50}. \tag{5}
$$
Since $L$ decreases in $a$ and increases in $t$, (2), (5), and $t>19/100$ imply
$$
b>L\!\left(\frac{11}{50};\frac{19}{100}\right)
=\frac{181}{468}>\frac{19}{50}. \tag{6}
$$
Thus every schedule with $R\le r_*$ lies in the rectangle
$$
\frac{19}{100}<a<\frac{11}{50},
\qquad
\frac{19}{50}<b\le\frac12. \tag{7}
$$

Step 4: Eliminate the third step by a momentum certificate
For $\lambda=3,7$, set
$$
S:=-3q_2(3)>0,
\qquad
T:=7q_2(7)>0,
$$
which follows directly from (7). Also put
$$
V_3:=\frac43q_2(3)-\frac13q_1(3),
\qquad
V_7:=\frac43q_2(7)-\frac13q_1(7).
$$
Then
$$
q_3(3)=V_3+Sc,
\qquad
q_3(7)=V_7-Tc.
$$
The linear combination
$$
Tq_3(3)+Sq_3(7)=TV_3+SV_7
$$
is independent of $c$. Hence for every $c$,
$$
\max\{|q_3(3)|,|q_3(7)|\}
\ge h(a,b):=-\frac{TV_3+SV_7}{T+S}. \tag{8}
$$
A simplification gives
$$
h(a,b)=-\frac{5292a^2b^2-2730a^2b+364a^2-2520ab^2+1068ab-120a+252b^2-90b+9}
{3(237ab-40a-30b+3)}.
$$
On the rectangle (7), the denominator factor
$$
D_0:=237ab-40a-30b+3
$$
is positive. Differentiating,
$$
\frac{\partial h}{\partial b}
=-\frac{7E(a,b)}{D_0^2},
$$
where
$$
E=36(3a-1)(7a-1)(79a-10)b^2
-24(3a-1)(7a-1)(40a-3)b
+a(1092a^2-550a+51).
$$
Furthermore
$$
\frac{\partial E}{\partial b}
=24(3a-1)(7a-1)D_0<0.
$$
Thus $E(a,b)\le E(a,19/50)$. Here
$$
E\!\left(a,\frac{19}{50}\right)
=\frac{1284591a^3-953650a^2+214446a-15390}{625}<0
$$
throughout $19/100\le a\le11/50$: its derivative is a convex quadratic that is negative at both endpoints, and the cubic itself is already negative at $a=19/100$. Consequently
$$
\frac{\partial h}{\partial b}>0. \tag{9}
$$
By (2) and (9), $h(a,b)\ge h(a,L(a))$. Using $P(t)=0$, direct reduction yields
$$
h(a,L(a))-r_*
=\frac{(a-t)Q(a,t)}
{12(a-1)D_1(a,t)}, \tag{10}
$$
where
$$
D_1=-184a^2+79at+77a-10t-8
$$
and
$$
\begin{aligned}
Q={}&16352a^3+624a^2t-15328a^2+4389at^2-3830at+5353a\\
&-1463t^2+1240t-681.
\end{aligned}
$$
On $19/100\le a\le11/50$ and $19/100\le t\le1/5$,
$$
\partial_aD_1=-368a+79t+77>0,
\qquad
\partial_tD_1=79a-10>0,
$$
so
$$
D_1\ge D_1\!\left(\frac{19}{100},\frac{19}{100}\right)=\frac{1879}{2000}>0.
$$
Also $Q_a$ and $Q_t$ decrease as either variable increases on this rectangle, and
$$
Q_a\!\left(\frac{11}{50},\frac15\right)=\frac{279664}{625}>0,
\qquad
Q_t\!\left(\frac{11}{50},\frac15\right)=\frac{142896}{625}>0.
$$
Thus $Q$ increases in both variables, while
$$
Q\!\left(\frac{11}{50},\frac15\right)
=-\frac{85556}{15625}<0.
$$
Hence $Q<0$ throughout the rectangle. Since $a\ge t$, $a-1<0$, and $D_1>0$, equation (10) gives
$$
h(a,L(a))\ge r_*,
$$
with equality only when $a=t$. Combining this with (8) proves $R\ge r_*$. Moreover, equality forces successively
$$
a=t,
\qquad
b=L(t)=\frac{5t-3}{6(t-1)}.
$$

Step 5: Attain the bound and prove uniqueness of the third step
At $a=t$ and $b=b_*$, solving
$$
q_3(3)=q_3(7)
$$
gives exactly
$$
c=c_*=
\frac{2(29t^2-19t+2)}{3(105t^2-67t+8)}.
$$
Moreover
$$
q_3(3)+r_*=q_3(7)+r_*
=\frac{(3t-1)P(t)}{12(t-1)(105t^2-67t+8)}=0,
$$
so
$$
q_3(3)=q_3(7)=-r_*.
$$
For the other active prefixes,
$$
q_1(1)=1-t=4r_*;
\qquad
q_2(1)=\frac{1-t}{2}=2r_*.
$$
The remaining modes are strict. Indeed
$$
|q_1(3)|<1-t,
\qquad |q_1(7)|<1-t,
$$
while
$$
q_2(3)=\frac{7t^2-4t+1}{2(t-1)},
\qquad
q_2(7)=\frac{63t^2-40t+5}{2(t-1)},
$$
and $19/100<t<1/5$ gives $|q_2(3)|,|q_2(7)|<2r_*$. Finally
$$
q_3(1)=\frac{2(1-t)(38t^2-24t+3)}{3(105t^2-67t+8)},
$$
and both quadratic factors in the ratio are negative on this interval; the inequality $q_3(1)<r_*$ reduces to
$$
8(38t^2-24t+3)>3(105t^2-67t+8),
$$
which is just $t(9-11t)>0$.
Therefore $R(a_*,b_*,c_*)=r_*$. Equality in the certificate (8) with both third-step residuals bounded by $r_*$ forces $q_3(3)=q_3(7)=-r_*$, so the displayed $c_*$ is also unique.

Thus, with $t$ the unique real root of $1463t^3-1438t^2+471t-48=0$,
Final Answer: $\boxed{\left(\frac{1-t}{4},\left(t,\frac{5t-3}{6(t-1)},\frac{2(29t^2-19t+2)}{3(105t^2-67t+8)}\right)\right)}$

---

## Answer

Approximately $(0.2012921541,(0.1948313835,0.4193413738,0.3751492009))$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- heavy-ball momentum
- spectral residual recurrence
- transient minimax optimization
- affine elimination certificate
- algebraic optimality certificate

---

## Black-Box Audit — no issues found
