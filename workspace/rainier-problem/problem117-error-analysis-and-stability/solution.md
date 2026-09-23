## Steps

Step 1: Reduce the real-axis boundary condition to one free coefficient

Write
$$
P(z)=1+z+\frac{z^2}{2}+az^3+bz^4.
$$
The condition $P(-3)=1$ gives
$$
1-3+\frac92-27a+81b=1,
$$
hence
$$
a=3b+\frac1{18}.
$$
So every admissible polynomial is determined by the single real parameter $b$.

Step 2: Express imaginary-axis stability by a quadratic inequality

For real $y$,
$$
P(iy)=1-\frac{y^2}{2}+by^4+i(y-ay^3).
$$
Put $q=y^2$. Expanding the squared modulus gives
$$
|P(iy)|^2-1
=y^4H_b(q),
$$
where
$$
H_b(q)=b^2q^2+(a^2-b)q+\frac14-2a+2b.
$$
Using the relation from Step 1,
$$
324H_b(q)
=324q(q+9)b^2-216(q+6)b+q+45.
$$
Therefore a polynomial is stable on $i[-R,R]$ exactly when
$$
H_b(q)\leq0\qquad(0\leq q\leq R^2).
$$

Step 3: Derive a global upper bound by eliminating the coefficient

Fix $q>0$. The expression $324H_b(q)$ is a quadratic in $b$ with positive leading coefficient. It can be nonpositive for some real $b$ only if its discriminant is nonnegative. That discriminant equals
$$
\begin{aligned}
\Delta(q)
&=216^2(q+6)^2
-4\cdot324q(q+9)(q+45)\\
&=-1296C(q),
\end{aligned}
$$
where
$$
C(q)=q^3+18q^2-27q-1296.
$$
Hence any admissible imaginary radius must satisfy
$$
C(R^2)\leq0.
$$

Now
$$
C'(q)=3(q^2+12q-9).
$$
This derivative has exactly one positive zero,
$$
q_0=-6+3\sqrt5.
$$
The polynomial decreases on $(0,q_0)$, so $C(q_0)<C(0)<0$, and then increases strictly to infinity. Thus $C$ has a unique positive zero, denoted $q_*$. Also
$$
C\left(\frac{15}{2}\right)=-\frac{513}{8}<0,
\qquad
C\left(\frac{31}{4}\right)=\frac{2647}{64}>0,
$$
so
$$
\frac{15}{2}<q_*<\frac{31}{4}.
$$
It follows that every admissible polynomial satisfies
$$
R^2\leq q_*.
$$

Step 4: Construct the unique polynomial attaining the bound

At $q=q_*$, equality in the discriminant bound forces the quadratic in $b$ from Step 3 to have a double root. Hence the only possible maximizing coefficient is
$$
b_*=\frac{q_*+6}{3q_*(q_*+9)},
\qquad
a_*=3b_*+\frac1{18}.
$$
The function
$$
b(q)=\frac{q+6}{3q(q+9)}
$$
is strictly decreasing for $q>0$. Using the bounds from Step 3,
$$
\frac{220}{6231}<b_*<\frac2{55}.
$$
In particular,
$$
\frac5{144}<b_*<\frac1{20}.
$$

For the imaginary axis, the discriminant equality gives
$$
H_{b_*}(q_*)=0,
$$
while
$$
H_{b_*}(0)=\frac5{36}-4b_*<0.
$$
Since $H_{b_*}$ is an upward-opening quadratic in $q$ and its constant term is negative, its two real roots have opposite signs. Therefore
$$
H_{b_*}(q)\leq0\qquad(0\leq q\leq q_*).
$$

It remains to verify the required real interval. For $0\leq t\leq3$,
$$
P_*(-t)-1
=\frac{t(t-3)}{18}\left(18b_*t^2-t+6\right).
$$
The quadratic factor is positive for every real $t$ because
$$
1-432b_*<0.
$$
Thus $P_*(-t)\leq1$ on $[0,3]$.

For the lower bound, set $u=t/3$. In the degree-four Bernstein basis on $[0,1]$,
$$
\begin{aligned}
P_*(-3u)
={}&1(1-u)^4
+\frac14\,4u(1-u)^3
+\frac14\,6u^2(1-u)^2\\
&+\left(\frac58-\frac{81b_*}{4}\right)4u^3(1-u)
+u^4.
\end{aligned}
$$
All Bernstein basis functions are nonnegative and sum to $1$. Since $b_*<1/20$,
$$
\frac58-\frac{81b_*}{4}>
-\frac{31}{80}>-1.
$$
Every Bernstein coefficient is therefore greater than $-1$, so
$$
P_*(-t)>-1\qquad(0\leq t\leq3).
$$
Hence $P_*$ is admissible and attains $R_*=\sqrt{q_*}$. The double-root condition also shows that the maximizing pair $(a_*,b_*)$ is unique.

Step 5: Write the positive cubic root in closed form

Set
$$
q=u-6.
$$
Then $C(q)=0$ becomes
$$
u^3-135u-702=0.
$$
Let
$$
c=\sqrt[3]{13+2\sqrt{11}}.
$$
Because
$$
(13+2\sqrt{11})(13-2\sqrt{11})=125,
$$
the number
$$
u=3c+\frac{15}{c}
$$
satisfies
$$
u^3-135u
=27c^3+\frac{3375}{c^3}
=702.
$$
By the uniqueness of the positive root from Step 3,
$$
q_*=-6+3\sqrt[3]{13+2\sqrt{11}}
+\frac{15}{\sqrt[3]{13+2\sqrt{11}}}.
$$
Therefore
$$
R_*=
\sqrt{-6+3\sqrt[3]{13+2\sqrt{11}}
+\frac{15}{\sqrt[3]{13+2\sqrt{11}}}}.
$$
Numerically, $R_*\approx2.76648049$.

Final Answer: $\boxed{\sqrt{-6+3\sqrt[3]{13+2\sqrt{11}}+\frac{15}{\sqrt[3]{13+2\sqrt{11}}}}}$

---

## Answer

$\sqrt{-6+3\sqrt[3]{13+2\sqrt{11}}+\frac{15}{\sqrt[3]{13+2\sqrt{11}}}}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- stability-polynomial optimization
- imaginary-axis stability
- discriminant certificate
- Bernstein basis bounds
- Cardano formula
