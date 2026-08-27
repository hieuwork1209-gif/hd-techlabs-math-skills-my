## Steps

Step 1: Convert boundedness into three stability constraints

For fixed $z$,
$$
u_m=R_{a,b}(z)^m u_0,
$$
so boundedness for every $u_0$ is equivalent to $|R_{a,b}(z)|\leq1$.

Let $L>0$ be admissible and set
$$
A=aL^2,\qquad B=bL^3.
$$
On the imaginary ray,
$$
|R_{a,b}(iy)|^2-1
=(1-2a)y^2+(a^2+2b)y^4+b^2y^6.
$$
Hence stability for all sufficiently small $y>0$ forces
$$
a\geq\frac12,\qquad A\geq A_0:=\frac{L^2}{2}. \tag{1}
$$
At $y=L/2$,
$$
(B+4L)^2\leq4A(8-A),
$$
so $0\leq A\leq8$ and
$$
B\leq U(A,L):=-4L+2\sqrt{A(8-A)}. \tag{2}
$$

Now put $q=e^{i\pi/3}$. Since $q^2=-\frac12+\frac{\sqrt3}{2}i$ and $q^3=-1$,
$$
|R_{a,b}(qL)|^2
=\left(1-\frac{A+L}{2}-B\right)^2+\frac34(A-L)^2.
$$
Thus
$$
D:=4-3(A-L)^2\geq0
$$
and
$$
B\geq V(A,L):=\frac{2-A-L-\sqrt D}{2}. \tag{3}
$$
The intervals in (2) and (3) must overlap, so
$$
K(A,L):=4\sqrt{A(8-A)}+\sqrt{4-3(A-L)^2}+A-7L-2\geq0. \tag{4}
$$

Step 2: Show that the local imaginary constraint becomes active at the optimum

If $L<8/3$, it is already below the sharp value found below. Assume $L\geq8/3$.

On the feasible range, $A\geq A_0>L$. Differentiating (4) with respect to $A$ gives
$$
K_A
=
1+\frac{4(4-A)}{\sqrt{A(8-A)}}
-\frac{3(A-L)}{\sqrt{4-3(A-L)^2}}.
$$
The second and third terms are decreasing functions of $A$. At $A=A_0$ their sum also decreases as $L$ increases. Therefore
$$
K_A
\leq
1+\frac1{\sqrt5}-\frac{12}{\sqrt{33}}<0, \tag{5}
$$
where the right side is the value at $L=8/3$, $A_0=32/9$. Hence $K(A,L)$ is strictly decreasing in $A$, and (1),(4) imply
$$
0\leq K(A,L)\leq H(L):=K(A_0,L),
$$
where
$$
H(L)=2L\sqrt{16-L^2}
+\sqrt{4-\frac34L^2(L-2)^2}
+\frac{L^2}{2}-7L-2. \tag{6}
$$
If the second radical in (6) is not real, then (3) is already impossible for every $A\geq A_0$.

Where (6) is real and $L\geq8/3$,
$$
H'(L)
=
\frac{4(8-L^2)}{\sqrt{16-L^2}}
-\frac{3L(L-2)(L-1)}
{2\sqrt{4-\frac34L^2(L-2)^2}}
+L-7<0. \tag{7}
$$
Indeed, on $[8/3,\sqrt8]$ the first term is less than $16/9$ while $L-7<-4$, and for $L\geq\sqrt8$ the first term is nonpositive.

Also
$$
H(8/3)=\frac{64\sqrt5+2\sqrt{33}-154}{9}>0,
$$
while
$$
H(11/4)=\frac{132\sqrt{15}+\sqrt{829}-559}{32}<0.
$$
Thus there is a unique
$$
r\in(8/3,11/4)
$$
such that $H(r)=0$, and every admissible $L$ satisfies $L\leq r$.

Step 3: Identify the exact algebraic value of the sharp bound

Put
$$
s=\sqrt{16-r^2}.
$$
At $A=A_0=r^2/2$, equality $H(r)=0$ means that the upper endpoint from (2) equals the lower endpoint from (3). The common value is
$$
B_*=-4r+rs.
$$
Substituting $A=r^2/2$ and $B=B_*$ into the oblique endpoint equality gives
$$
3r^3+10r^2-114r-28+(-2r^2+28r+8)s=0. \tag{8}
$$
On $(8/3,11/4)$ the coefficient of $s$ is positive and the remaining cubic expression is negative, so squaring (8) introduces no sign ambiguity. Using $s^2=16-r^2$ gives
$$
P(r)=0,
$$
where
$$
P(x)=13x^6-52x^5+104x^4-208x^3+468x^2-784x-240. \tag{9}
$$
Conversely, any root of $P$ in $(8/3,11/4)$ satisfies (8), hence $H=0$. By Step 2 this root is unique. Therefore
$$
r=\operatorname{Root}_{(8/3,11/4)}(P).
$$

Step 4: Construct the candidate and verify the real and imaginary rays

Define
$$
a_*=rac12,\qquad
b_*=-\frac{1}{4+s}.
$$
Since $r^2=(4-s)(4+s)$,
$$
b_*r^2=s-4,\qquad b_*r^3=B_*.
$$
Thus both complex endpoint constraints used above are equalities.

For the imaginary ray,
$$
|R_{a_*,b_*}(iy)|^2-1
=
y^4\left(\frac14+2b_*+b_*^2y^2\right).
$$
The bracket is affine increasing in $y^2$ and vanishes at $y=r/2$. Also $r>8/3>\sqrt7$ gives $s<3$, so $b_*<-1/7$ and the bracket is negative at $0$. Hence
$$
|R_{a_*,b_*}(iy)|\leq1\qquad(0\leq y\leq r/2). \tag{10}
$$

On the real ray,
$$
R_{a_*,b_*}'(x)=-1+x+3b_*x^2.
$$
Its discriminant is $1+12b_*<1-12/7<0$, so $R_{a_*,b_*}'(x)<0$ for every real $x$. Moreover
$$
R_{a_*,b_*}(r)+1
=
J(r):=
2-5r+\frac{r^2}{2}+r\sqrt{16-r^2}.
$$
Moreover
$$
J'(L)=-5+L+\frac{16-2L^2}{\sqrt{16-L^2}}
<-\frac94+\frac{64}{99}<0
\qquad(8/3<L<11/4),
$$
so $J$ is decreasing there, and
$$
J(11/4)=\frac{66\sqrt{15}-255}{32}>0.
$$
Therefore $-1<R_{a_*,b_*}(r)<1$, and monotonicity gives
$$
|R_{a_*,b_*}(x)|\leq1\qquad(0\leq x\leq r). \tag{11}
$$

Step 5: Verify the oblique ray and prove uniqueness

Let $u=3-r$, so $1/4<u<1/3$. Using (8), a direct expansion for $0\leq t\leq1$ gives
$$
|R_{a_*,b_*}(rtq)|^2-1
=
\frac{rt(t-1)}{4(14r+4-r^2)}\,Q_r(t), \tag{12}
$$
where $Q_r$ has the degree-$4$ Bernstein expansion
$$
Q_r(t)=\sum_{k=0}^{4}c_k\binom4k t^k(1-t)^{4-k},
$$
with
$$
\begin{aligned}
c_0&=4(14r+4-r^2),\\
c_1&=\frac{(10-r)(14r+4-r^2)}2,\\
c_2&=\frac{435-u^4-22u^2-28u}{3},\\
c_3&=\frac{-u^5+u^4+18u^3-158u^2+215u+565}{4},\\
c_4&=-5u^5+55u^4-264u^3+620u^2-795u+725.
\end{aligned}
$$
All five coefficients are positive for $1/4<u<1/3$: the first two are immediate, while
$$
c_2>\frac{384}{3},\qquad
c_3>\frac{406}{4},\qquad
c_4>725-265-\frac{264}{27}-\frac5{243}>0.
$$
Hence $Q_r(t)>0$ on $[0,1]$. Since $t(t-1)\leq0$, (12) proves
$$
|R_{a_*,b_*}(z)|\leq1
\qquad\left(z\in e^{i\pi/3}[0,r]\right). \tag{13}
$$
Together with (10),(11), this shows $\rho(a_*,b_*)\geq r$. Step 2 gives the reverse inequality, so $\rho_*=r$.

Finally, if another pair attained $r$, then (1) gives $A\geq r^2/2$, while (4) and the strict decrease in (5) give
$$
0\leq K(A,r)\leq K(r^2/2,r)=H(r)=0.
$$
Thus $A=r^2/2$, so $a=1/2$. The two endpoint intervals (2),(3) then touch at a single value $B=B_*$, forcing $b=b_*$. Hence the maximizing pair is unique.

Final Answer: $\boxed{\operatorname{Root}_{(8/3,11/4)}(13x^6-52x^5+104x^4-208x^3+468x^2-784x-240)}$

## Answer

$\operatorname{Root}_{(8/3,11/4)}(13x^6-52x^5+104x^4-208x^3+468x^2-784x-240)$

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

## Solution Concepts

- coupled stability on multiple spectral rays
- endpoint interval overlap
- leading-order degeneracy
- Bernstein positivity certificate
- equality-case rigidity

## Black-Box Audit

The upper bound is obtained from explicit endpoint inequalities and monotonicity. The oblique-ray verification uses a displayed Bernstein-basis identity with coefficient signs proved on the isolating interval. No numerical optimizer or external extremal theorem is used.
