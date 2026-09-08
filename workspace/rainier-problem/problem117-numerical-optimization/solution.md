## Steps

Step 1: Reduce the heavy-ball cycle to scalar residual recurrences
The Hessian is
$$
A=\operatorname{diag}(1,3,7).
$$
With $x_{-1}=x_0$ and momentum $\beta=1/3$, each eigencoordinate with eigenvalue $\lambda\in\{1,3,7\}$ is multiplied by residuals
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
This gives
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\max_{\lambda\in\{1,3,7\}}
\max\left\{\frac14|q_1(\lambda)|,\frac12|q_2(\lambda)|,|q_3(\lambda)|\right\}.
$$

Step 2: Define the candidate algebraic minimizer
Let $t$ be the unique real root of
$$
P(z)=1463z^3-1438z^2+471z-48.
$$
The discriminant of $P$ is $-671179008<0$, so $P$ has exactly one real root. Also,
$$
P\!\left(\frac{19}{100}\right)<0,
\qquad
P\!\left(\frac15\right)>0,
$$
which places that root in
$$
\frac{19}{100}<t<\frac15.
$$
Set
$$
r_*:=\frac{1-t}{4},
\qquad a_*:=t,
$$
$$
b_*:=\frac{5t-3}{6(t-1)}=\frac{3-5t}{6(1-t)},
$$
$$
c_*:=\frac{2(29t^2-19t+2)}{3(105t^2-67t+8)}.
$$
The interval for $t$ gives $0<a_*,b_*,c_*<1/2$. Numerically,
$$
t\approx0.1948313835,
\quad b_*\approx0.4193413738,
\quad c_*\approx0.3751492009,
\quad r_*\approx0.2012921541.
$$

Step 3: Restrict the first two step sizes to a narrow feasible strip
Write
$$
a=\alpha_0,\qquad b=\alpha_1,\qquad c=\alpha_2,
$$
and suppose $R\leq r_*$. The one-step constraint at $\lambda=1$ gives
$$
\frac14(1-a)\leq r_*,
$$
so $a\geq t$. Since $t>1/7$, the one-step constraint at $\lambda=7$ gives
$$
7a-1\leq1-t,
\qquad
 a\leq\frac{2-t}{7}.
$$
Because $b\leq1/2$ and $a\leq(2-t)/7<2/7$,
$$
q_2(1)=\left(\frac43-b\right)(1-a)-\frac13
>\frac56\cdot\frac57-\frac13=\frac{11}{42}>0.
$$
The bound $q_2(1)\leq2r_*$ therefore gives
$$
b\geq L(a):=\frac43-\frac{5-3t}{6(1-a)}.
$$
The quantity $q_2(7)$ is increasing in $b$. At $b=L(a)$,
$$
q_2(7)=\frac{-112a^2+49at+47a-7t-5}{2(1-a)}>0.
$$
The numerator is concave in $a$, and at $a=t$ and $a=(2-t)/7$ it equals
$$
-63t^2+40t-5>0,
\qquad
-\frac{65t^2-66t+5}{7}>0.
$$
The constraint $q_2(7)\leq2r_*$ then gives
$$
b\leq U(a):=\frac17\left(\frac43+\frac{5-3t}{6(7a-1)}\right).
$$
Feasibility requires $L(a)\leq U(a)$. Since
$$
L(a)-U(a)
=\frac{56a^2-24at-24a+3t+3}{7(a-1)(7a-1)},
$$
and $a<1$ while $7a-1>0$, the denominator is negative. Therefore
$$
N(a,t):=56a^2-24at-24a+3t+3\geq0.
$$
For fixed $t$, the function $N$ is convex in $a$. At the endpoints of the interval $[11/50,(2-t)/7]$,
$$
N\!\left(\frac{11}{50},t\right)
=-\frac{1425t-269}{625}<0,
$$
$$
N\!\left(\frac{2-t}{7},t\right)
=\frac{32t^2-35t+5}{7}<0.
$$
Convexity makes $N<0$ throughout that interval, which is incompatible with $N(a,t)\geq0$. So
$$
t\leq a<\frac{11}{50}.
$$
Since
$$
\frac{\partial L}{\partial a}=-\frac{5-3t}{6(1-a)^2}<0,
\qquad
\frac{\partial L}{\partial t}=\frac{1}{2(1-a)}>0,
$$
the bounds $b\geq L(a)$, $a<11/50$, and $t>19/100$ imply
$$
b>L\!\left(\frac{11}{50};\frac{19}{100}\right)
=\frac{181}{468}>\frac{19}{50}.
$$
Every schedule with $R\leq r_*$ therefore lies in
$$
\frac{19}{100}<a<\frac{11}{50},
\qquad
\frac{19}{50}<b\leq\frac12.
$$

Step 4: Eliminate the third step size with a momentum certificate
On the rectangle from Step 3, define
$$
S:=-3q_2(3),
\qquad
T:=7q_2(7).
$$
For $\lambda=3$, $q_2(3)$ decreases with $b$ because $1-3a>0$. At $b=19/50$, the factor $4/3-3b$ is positive, so the same expression also decreases with $a$. Therefore
$$
q_2(3)
\leq\left(\frac43-3\cdot\frac{19}{50}\right)
\left(1-3\cdot\frac{19}{100}\right)-\frac13
=-\frac{1251}{5000}<0.
$$
For $\lambda=7$, both factors $4/3-7b$ and $1-7a$ are negative, and $q_2(7)$ increases with each of $a$ and $b$. Therefore
$$
q_2(7)
\geq\left(\frac43-7\cdot\frac{19}{50}\right)
\left(1-7\cdot\frac{19}{100}\right)-\frac13
=\frac{1567}{15000}>0.
$$
So $S,T>0$. Put
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
The combination
$$
Tq_3(3)+Sq_3(7)=TV_3+SV_7
$$
does not depend on $c$. Since $S,T>0$,
$$
\max\{|q_3(3)|,|q_3(7)|\}
\geq h(a,b):=-\frac{TV_3+SV_7}{T+S}.
$$
Expanding gives
$$
h(a,b)=-\frac{5292a^2b^2-2730a^2b+364a^2-2520ab^2+1068ab-120a+252b^2-90b+9}
{3(237ab-40a-30b+3)}.
$$
Write
$$
D_0:=237ab-40a-30b+3.
$$
On the Step 3 rectangle, both partial derivatives of $D_0$ are positive, and
$$
D_0\!\left(\frac{19}{100},\frac{19}{50}\right)=\frac{5557}{5000}>0.
$$
So $D_0>0$. Differentiation gives
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
Also,
$$
\frac{\partial E}{\partial b}
=24(3a-1)(7a-1)D_0<0.
$$
So $E(a,b)\leq E(a,19/50)$. Let
$$
F(a):=1284591a^3-953650a^2+214446a-15390.
$$
Then
$$
E\!\left(a,\frac{19}{50}\right)=\frac{F(a)}{625}.
$$
The derivative
$$
F'(a)=3853773a^2-1907300a+214446
$$
is convex and is negative at both $a=19/100$ and $a=11/50$. So $F'$ is negative on the whole interval. Since $F(19/100)<0$, we get $F(a)<0$, so $E(a,b)<0$ and
$$
\frac{\partial h}{\partial b}>0.
$$
Step 3 gives $b\geq L(a)$, so
$$
h(a,b)\geq h(a,L(a)).
$$
Expanding the rational expression and replacing each $t^3$ by the relation from $P(t)=0$ gives
$$
h(a,L(a))-r_*
=\frac{(a-t)Q(a,t)}{12(a-1)D_1(a,t)},
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
On $19/100\leq a\leq11/50$ and $19/100\leq t\leq1/5$,
$$
\frac{\partial D_1}{\partial a}=-368a+79t+77>0,
\qquad
\frac{\partial D_1}{\partial t}=79a-10>0,
$$
so
$$
D_1\geq D_1\!\left(\frac{19}{100},\frac{19}{100}\right)=\frac{1879}{2000}>0.
$$
For $Q$,
$$
Q_{aa}=98112a+1248t-30656<0,
$$
$$
Q_{at}=1248a+8778t-3830<0,
\qquad
Q_{tt}=8778a-2926<0
$$
throughout the same rectangle. So $Q_a$ and $Q_t$ decrease as either variable increases. At the upper corner,
$$
Q_a\!\left(\frac{11}{50},\frac15\right)=\frac{279664}{625}>0,
\qquad
Q_t\!\left(\frac{11}{50},\frac15\right)=\frac{142896}{625}>0.
$$
So $Q$ increases in both variables. Its maximum is therefore at the upper corner, where
$$
Q\!\left(\frac{11}{50},\frac15\right)
=-\frac{85556}{15625}<0.
$$
So $Q<0$ on the rectangle. Since $a\geq t$, $a-1<0$, and $D_1>0$, the factorization for $h(a,L(a))-r_*$ gives
$$
h(a,L(a))\geq r_*,
$$
with equality only at $a=t$. The lower bound for $\max\{|q_3(3)|,|q_3(7)|\}$ then proves $R\geq r_*$. Equality forces
$$
a=t,
\qquad
b=L(t)=\frac{5t-3}{6(t-1)}.
$$

Step 5: Attain the bound and identify the unique third step size
At $a=t$ and $b=b_*$, solving
$$
q_3(3)=q_3(7)
$$
gives
$$
c=c_*=
\frac{2(29t^2-19t+2)}{3(105t^2-67t+8)}.
$$
Also,
$$
q_3(3)+r_*=q_3(7)+r_*
=\frac{(3t-1)P(t)}{12(t-1)(105t^2-67t+8)}=0,
$$
so
$$
q_3(3)=q_3(7)=-r_*.
$$
For the other prefixes,
$$
q_1(1)=1-t=4r_*,
\qquad
q_2(1)=\frac{1-t}{2}=2r_*.
$$
The remaining modes are strict:
$$
|q_1(3)|<1-t,
\qquad |q_1(7)|<1-t,
$$
$$
q_2(3)=\frac{7t^2-4t+1}{2(t-1)},
\qquad
q_2(7)=\frac{63t^2-40t+5}{2(t-1)},
$$
For $q_2(3)<0$, the inequality $|q_2(3)|<2r_*=(1-t)/2$ reduces to
$$
2t(3t-1)<0,
$$
which holds because $0<t<1/5$. For $q_2(7)>0$, the inequality $|q_2(7)|<2r_*$ reduces to
$$
64t^2-42t+6>0.
$$
This quadratic is decreasing for $t<1/5$ and equals $4/25$ at $t=1/5$, so it is positive on the required interval. For the last mode,
$$
q_3(1)=\frac{2(1-t)(38t^2-24t+3)}{3(105t^2-67t+8)}.
$$
Both quadratic factors in this ratio are negative on $19/100<t<1/5$. The inequality $q_3(1)<r_*$ is equivalent to
$$
8(38t^2-24t+3)>3(105t^2-67t+8),
$$
which reduces to $t(9-11t)>0$. So $R(a_*,b_*,c_*)=r_*$. Equality in the Step 4 certificate with both third-step residuals bounded by $r_*$ forces $q_3(3)=q_3(7)=-r_*$, so $c_*$ is unique.

For the final answer, the third component can be shortened without changing its value. Since $P(t)=0$,
$$
\frac{2(29t^2-19t+2)}{3(105t^2-67t+8)}
-\frac{41t-13}{147t-42}
=\frac{P(t)}{-21(7t-2)(105t^2-67t+8)}=0.
$$
Step 2 shows that the cubic condition in the final expression selects one real value of $t$.
Final Answer: $\boxed{(\frac{-t+1}{4},(t,\frac{5t-3}{6t-6},\frac{41t-13}{147t-42}))|_{1463t^3-1438t^2+471t-48=0,0<t<1}}$

---

## Answer

$(\frac{-t+1}{4},(t,\frac{5t-3}{6t-6},\frac{41t-13}{147t-42}))|_{1463t^3-1438t^2+471t-48=0,0<t<1}$

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
- algebraic minimax certificate

---

## Black-Box Audit — no issues found
