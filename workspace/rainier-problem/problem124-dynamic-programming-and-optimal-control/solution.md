## Steps

Step 1: Prove the two sharp cubic estimates for nonnegative Lipschitz pieces
Let $v$ be nonnegative and $1$-Lipschitz on a positivity component $I$, with value $0$ at the two endpoints of $I$. Write
$$
B=\int_I v(x)\,dx,\qquad Q=\int_I v(x)^3\,dx,
$$
and let $H=\max_I v$. For $0\leq y<H$, put
$$
m(y)=|\{x\in I:v(x)>y\}|.
$$
If $0\leq y<z<H$, the $(z-y)$-neighborhood of $\{v>z\}$ lies in $\{v>y\}$ by the Lipschitz condition. In one dimension this enlarges a nonempty bounded set by at least $2(z-y)$, so
$$
m(y)\geq m(z)+2(z-y).
$$
Hence
$$
e(y):=m(y)-2(H-y)
$$
is nonincreasing, and letting $z\uparrow H$ in the preceding inequality shows $e(y)\geq0$. By Fubini,
$$
B=\int_0^H m(y)\,dy,\qquad Q=\int_0^H3y^2m(y)\,dy.
$$
Substituting $m(y)=2(H-y)+e(y)$ gives
$$
B=H^2+\int_0^H e(y)\,dy
$$
and
$$
Q=\frac{H^4}{2}+\int_0^H3y^2e(y)\,dy.
$$
Because $y^2$ is increasing and $e$ is nonincreasing,
$$
\int_0^H\int_0^H(y^2-z^2)(e(y)-e(z))\,dz\,dy\leq0.
$$
Expanding this double integral yields
$$
\int_0^H3y^2e(y)\,dy\leq H^2\int_0^He(y)\,dy.
$$
Therefore
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2},
$$
since $B\geq H^2$. Equality forces $B=H^2$ and $e=0$, hence the component has length $2H$ and $v$ is the full symmetric tent of height $H$. Applying this estimate to all positivity components and using
$$
\sum_i B_i^2\leq\left(\sum_iB_i\right)^2
$$
shows that
$$
\int v^3\leq\frac12\left(\int v\right)^2,
$$
with equality only for one full symmetric tent.

We also need the opposite sharp estimate. Let $w$ be nonnegative and $1$-Lipschitz on $[0,L]$, with $w(0)=w(L)=0$ and
$$
\int_0^Lw(x)\,dx=B,\qquad 0<B\leq\frac{L^2}{4}.
$$
Let $h\in(0,L/2]$ be the smaller root of
$$
B=hL-h^2,
$$
and define
$$
v_h(x)=\min\{x,L-x,h\}.
$$
Then $\int_0^Lv_h=B$. Since $w(x)\leq d(x):=\min\{x,L-x\}$, consider
$$
\phi(s)=s^3-3h^2s.
$$
On the central region $d(x)\geq h$,
$$
\phi(w(x))-\phi(h)=(w(x)-h)^2(w(x)+2h)\geq0.
$$
On the boundary region $d(x)<h$, one has $0\leq w(x)\leq d(x)=v_h(x)<h$, while $\phi$ is decreasing on $[0,h]$, so again $\phi(w(x))\geq\phi(v_h(x))$. Integrating and using $\int w=\int v_h$ gives
$$
\int_0^Lw(x)^3\,dx\geq\int_0^Lv_h(x)^3\,dx
=h^3L-\frac32h^4.
$$
Equality holds only for $w=v_h$. If a nonnegative function has several positive components, enumerate and concatenate those components. Their endpoints are all $0$. Across a join, values at distances $r$ and $s$ from the join are at most $r$ and $s$, so their difference is at most $r+s$; hence the concatenation is still $1$-Lipschitz and preserves area and cubic integral. The same lower bound applies after appending a zero interval to any larger available length. Equality with positive area forces one component and no appended zero interval.

Step 2: Reduce the control problem to one scalar compatibility parameter
For an admissible control $u$, let
$$
x(t)=\int_0^t u(s)\,ds.
$$
Then $x$ is absolutely continuous, $x(0)=x(1)=0$, $|x'(t)|\leq1$ almost everywhere, and $\int_0^1x(t)\,dt=0$. Write
$$
x_+(t)=\max(x(t),0),\qquad x_-(t)=\max(-x(t),0).
$$
The integral state constraint gives a common area
$$
A:=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt.
$$
Put $A=a^2$ with $a\geq0$. The case $a=0$ gives $x=0$, so assume $a>0$.

If the positive components have lengths $\ell_i$, the tent envelope on each component gives area at most $\ell_i^2/4$. Thus, with
$$
P=|\{t\in[0,1]:x(t)>0\}|,
$$
we have
$$
a^2\leq\frac14\sum_i\ell_i^2\leq\frac{P^2}{4},
$$
so $P\geq2a$. The negative components therefore occupy total length at most $1-2a$. Concatenate all negative components and append a zero interval if necessary to obtain a nonnegative $1$-Lipschitz function on
$$
[0,L],\qquad L=1-2a,
$$
with endpoint values $0$, area $a^2$, and cubic integral equal to $\int_0^1x_-(t)^3\,dt$. Feasibility gives
$$
a^2\leq\frac{L^2}{4},
$$
so $0<a\leq1/4$.

Let $h$ be the smaller root of
$$
a^2=h(1-2a)-h^2.
$$
The upper estimate from Step 1 gives
$$
\int_0^1x_+(t)^3\,dt\leq\frac{a^4}{2},
$$
while the lower estimate from Step 1 gives
$$
\int_0^1x_-(t)^3\,dt\geq h^3(1-2a)-\frac32h^4.
$$
Consequently
$$
\int_0^1x(t)^3\,dt
\leq\frac{a^4}{2}-h^3(1-2a)+\frac32h^4.
$$

Step 3: Optimize the compatibility relation exactly
Set
$$
z=\frac{h}{a}.
$$
Because $L=1-2a\geq2a$ and $h$ is the smaller root of $h(L-h)=a^2$, one has $0<z\leq1$. Dividing
$$
a^2=h(1-2a-h)
$$
by $a$ and substituting $h=za$ gives
$$
a=\frac{z}{(1+z)^2},\qquad
h=\frac{z^2}{(1+z)^2},\qquad
1-2a=\frac{1+z^2}{(1+z)^2}.
$$
Substitution into the bound from Step 2 simplifies it to
$$
\int_0^1x(t)^3\,dt
\leq F(z):=\frac{z^4(1-z)^2}{2(1+z)^6}.
$$
For $0<z<1$,
$$
\frac{F'(z)}{F(z)}
=\frac4z-\frac2{1-z}-\frac6{1+z}
=\frac{4(1-2z)}{z(1-z^2)}.
$$
Thus $F$ increases up to $z=1/2$ and decreases afterwards. Since its endpoint limits are $0$, its unique maximum occurs at
$$
z=\frac12.
$$
At that point
$$
a=\frac29,\qquad h=\frac19,
$$
and
$$
F\left(\frac12\right)=\frac1{1458}.
$$

Step 4: Reconstruct all optimal controls
Equality requires equality at every sharp estimate used in Steps 1 and 2. The positive part of the state must therefore be one full symmetric tent. Since $a=2/9$, it has area $4/81$, height $2/9$, and support length $4/9$. The negative part must be one minimizing trapezoid. Since $h=1/9$ and its available length is $1-2a=5/9$, it has support length $5/9$, height $1/9$, and a flat portion of length $1/3$. Equality in the support bound leaves no zero interval between the two sign components.

Hence the positive and negative supports tile $[0,1]$ in one of two orders. If the positive tent comes first, the state is
$$
x_1(t)=
\begin{cases}
t,&0\leq t\leq\frac29,\\
\frac49-t,&\frac29\leq t\leq\frac59,\\
-\frac19,&\frac59\leq t\leq\frac89,\\
t-1,&\frac89\leq t\leq1.
\end{cases}
$$
If the negative trapezoid comes first, the state is
$$
x_2(t)=
\begin{cases}
-t,&0\leq t\leq\frac19,\\
-\frac19,&\frac19\leq t\leq\frac49,\\
t-\frac59,&\frac49\leq t\leq\frac79,\\
1-t,&\frac79\leq t\leq1.
\end{cases}
$$
Both states satisfy the terminal and integral constraints because their positive and negative areas are each $4/81$. Their positive cubic contribution is
$$
\frac12\left(\frac{4}{81}\right)^2=\frac{16}{13122},
$$
and their negative cubic contribution in absolute value is
$$
\left(\frac19\right)^3\frac59-\frac32\left(\frac19\right)^4
=\frac7{13122}.
$$
Thus each gives $9/13122=1/1458$. Differentiating the two states almost everywhere shows that the optimal controls are exactly
$$
u_1(t)=
\begin{cases}
1,&0<t<\frac29,\\
-1,&\frac29<t<\frac59,\\
0,&\frac59<t<\frac89,\\
1,&\frac89<t<1,
\end{cases}
$$
and
$$
u_2(t)=
\begin{cases}
-1,&0<t<\frac19,\\
0,&\frac19<t<\frac49,\\
1,&\frac49<t<\frac79,\\
-1,&\frac79<t<1.
\end{cases}
$$
up to equality almost everywhere. Values at the finitely many switching times are irrelevant. The equality conditions in the two sharp estimates force these state shapes and the no-gap tiling, so there are no other optimal controls.

Final Answer: $\boxed{\frac{1}{1458}}$

---

## Answer

$\frac{1}{1458}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- layer-cake representation
- Lipschitz extremal geometry
- optimal control with state constraints
- convex integral minimization
- equality classification
