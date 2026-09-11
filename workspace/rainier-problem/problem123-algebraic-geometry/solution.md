## Steps

Step 1: Prove the covering has degree $mn$

Let
$$
F=\mathbb C(x),
$$
and let
$$
K=F(y,z),
\qquad
y^m=x(x-1),
\qquad
z^n=x(x-\lambda),
$$
where $m,n\ge2$ and $\lambda\in\mathbb C\setminus\{0,1\}$. Let $C$ be the smooth projective curve with function field $K$.

First consider $F(y)/F$. At the $x=0$ valuation $v_0$,
$$
v_0(x(x-1))=1.
$$
If $P$ is a place above $v_0$ with ramification index $e_P$, then
$$
m\,v_P(y)=v_P(x(x-1))=e_P.
$$
Hence $m\mid e_P$. Since always
$$
e_P\le [F(y):F]\le m,
$$
we get
$$
[F(y):F]=m.
\tag{1}
$$

At $x=\lambda$, the equation for $y$ has a nonzero unit on the right-hand side. Because the residue field is $\mathbb C$ and the characteristic is $0$, the $y$-cover is unramified there. Thus at every place $Q$ of $F(y)$ over $x=\lambda$,
$$
v_Q(x(x-\lambda))=1.
$$
For a place $R$ of $K$ above such a $Q$, the equation $z^n=x(x-\lambda)$ gives
$$
n\,v_R(z)=e(R/Q).
$$
Therefore $n\mid e(R/Q)$, and hence
$$
[K:F(y)]=n.
\tag{2}
$$
Combining (1)-(2),
$$
[K:F]=mn.
\tag{3}
$$
Moreover the automorphisms
$$
y\mapsto \zeta_m^a y,
\qquad
z\mapsto \zeta_n^b z
$$
for $a\in\mathbb Z/m\mathbb Z$ and $b\in\mathbb Z/n\mathbb Z$ give $mn$ distinct $F$-automorphisms. Hence the map
$$
x:C\longrightarrow\mathbb P^1
$$
is Galois with group
$$
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
\tag{4}
$$

Step 2: Compute the finite inertia groups

For a Kummer equation $u^r=h(x)$ in characteristic $0$, a small loop around a point where $h$ has valuation $s$ acts by
$$
u\mapsto \zeta_r^s u.
$$
Thus for the two simultaneous equations, the local inertia generator is determined by the pair of valuations of the two right-hand sides.

At $x=0$, both valuations equal $1$, so the inertia generator is
$$
(1,1)\in \mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
$$
Its order is
$$
e_0=\operatorname{lcm}(m,n)=\frac{mn}{d},
\qquad d:=\gcd(m,n).
\tag{5}
$$
At $x=1$, only the first cover ramifies, so
$$
e_1=m.
\tag{6}
$$
At $x=\lambda$, only the second cover ramifies, so
$$
e_\lambda=n.
\tag{7}
$$
No other finite point ramifies, because away from $0,1,\lambda$ both right-hand sides are units and hence have local $m$-th and $n$-th roots after passing to the completed local field.

Step 3: Compute the inertia at infinity and expose the parity transition

Put $t=1/x$. Then near $t=0$,
$$
x(x-1)=t^{-2}(1-t),
$$
$$
x(x-\lambda)=t^{-2}(1-\lambda t).
$$
Therefore the inertia generator at infinity is
$$
(-2,-2),
$$
whose order is
$$
e_\infty
=\operatorname{lcm}\left(\frac{m}{\gcd(m,2)},\frac{n}{\gcd(n,2)}\right).
\tag{8}
$$
If $mn$ is odd, then both $m,n$ are odd, so
$$
e_\infty=\operatorname{lcm}(m,n)=\frac{mn}{d}.
\tag{9}
$$
If $mn$ is even, removing the common factor $2$ from the relevant even moduli lowers the least common multiple by exactly a factor $2$, giving
$$
e_\infty=\frac{mn}{2d}.
\tag{10}
$$
Equivalently, the number of points of $C$ above infinity is
$$
\frac{mn}{e_\infty}
=
\begin{cases}
d,&mn\text{ odd},\\
2d,&mn\text{ even}.
\end{cases}
\tag{11}
$$

Step 4: Apply Riemann-Hurwitz with the exact inertia data

For a Galois cover of degree $D$ over $\mathbb P^1$, a branch point with inertia order $e$ contributes
$$
\frac{D}{e}(e-1)=D-\frac De
$$
to the ramification sum. Here $D=mn$.

From (5)-(7), the three finite contributions are
$$
mn-d,
\qquad
mn-n,
\qquad
mn-m.
\tag{12}
$$
At infinity, by (11), the contribution is
$$
\begin{cases}
mn-d,&mn\text{ odd},\\
mn-2d,&mn\text{ even}.
\end{cases}
\tag{13}
$$
Riemann-Hurwitz therefore gives
$$
2g(C)-2
=-2mn+\sum_P\left(mn-\frac{mn}{e_P}\right).
\tag{14}
$$
If $mn$ is odd, (12)-(14) yield
$$
2g(C)-2
=2mn-m-n-2d,
$$
so
$$
g(C)=1+mn-\frac{m+n+2d}{2}.
\tag{15}
$$
If $mn$ is even, they yield
$$
2g(C)-2
=2mn-m-n-3d,
$$
so
$$
g(C)=1+mn-\frac{m+n+3d}{2}.
\tag{16}
$$

Step 5: Combine the two regimes

Let $\mathbf 1_{2\mid mn}$ be $1$ when $mn$ is even and $0$ otherwise. Since $d=\gcd(m,n)$, equations (15)-(16) combine as
$$
g(C)
=1+mn-
\frac{m+n+\bigl(2+\mathbf 1_{2\mid mn}\bigr)\gcd(m,n)}{2}.
$$
The parameter $\lambda$ affects the locations of the distinct finite branch points but not their inertia orders, so the genus is independent of $\lambda$ as long as $\lambda\ne0,1$.

## Solution Concepts

- Kummer covers and exact extension degree from local valuations.
- Simultaneous inertia in a fiber product, including the parity change at infinity.
- Riemann-Hurwitz with Galois ramification contributions.

Final Answer: $\displaystyle 1+mn-\frac{m+n+(2+\mathbf1_{2\mid mn})\gcd(m,n)}2$.
