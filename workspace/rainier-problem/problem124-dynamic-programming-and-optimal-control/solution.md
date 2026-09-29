## Steps

Step 1: Convert the terminal constraints to moments and prove sharp excursion bounds
Write $x=x_u$. From $y_u(1)=z_u(1)=0$,
$$
\int_0^1x(t)\,dt=0,\qquad \int_0^1(1-t)x(t)\,dt=0,
$$
so also $\int_0^1t x(t)\,dt=0$. Hence $x_+$ and $x_-$ have the same area and the same barycenter.

Let $v\geq0$ be $1$-Lipschitz on an interval of length $L$, vanish at its endpoints, and write
$$
B=\int v,\qquad Q=\int v^3,\qquad H=\max v.
$$
For $0\leq a<H$, put $m(a)=|\{v>a\}|$. If $a<b<H$, the $(b-a)$-neighborhood of $\{v>b\}$ lies in $\{v>a\}$, so
$$
m(a)\geq m(b)+2(b-a).
$$
So $e(a)=m(a)-2(H-a)$ is nonnegative and nonincreasing. Layer cake gives
$$
B=H^2+\int_0^He(a)\,da,
$$
$$
Q=\frac{H^4}{2}+\int_0^H3a^2e(a)\,da.
$$
Since $a^2$ is increasing and $e$ is nonincreasing,
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2}.
$$
Equality holds exactly for the triangular tent of height $\sqrt{B}$ and length $2\sqrt{B}$.

For the reverse cubic bound at fixed $B,L$, let $b$ be the smaller root of $B=bL-b^2$ and set $v_b(t)=\min\{t,L-t,b\}$. With $\phi(s)=s^3-3b^2s$, one has $\phi(v)\geq\phi(v_b)$ pointwise: where $v_b<b$, the endpoint Lipschitz bounds give $v\leq v_b\leq b$ and $\phi$ is decreasing, while where $v_b=b$,
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0.
$$
Therefore
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2},
$$
with equality exactly for the capped tent $v_b$. Also $\Phi_L<0$, so for fixed area extra available length can only decrease the least possible cubic cost.

Step 2: Keep the packet barycenters and derive a moment-safe two-sided bound
Let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt A.
$$
If $A=0$, then $x=0$, so assume $A>0$.

We first record the barycenter margin that will replace the invalid assumption that a symmetric extremizer has the same intrinsic barycenter as an arbitrary packet. If $v\ge0$ is $1$-Lipschitz on an interval of length $S$, vanishes at both endpoints, has area $B>0$, and has barycenter
$$
\beta=\frac1B\int_0^S t,v(t)\,dt,
$$
then
$$
\sqrt B\le \beta\le S-\sqrt B. \tag{1}
$$
Indeed, decompose $v$ into zero-ended excursions and move them left without changing their shapes or their order. For an excursion of area $B_j$, the shortest possible support is $2\sqrt{B_j}$ and its smallest possible barycenter relative to its left endpoint is $\sqrt{B_j}$; both equalities are attained only by the triangular tent. Placing the excursions consecutively from the left therefore minimizes the packet barycenter. If $a_j=\sqrt{B_j}$, that leftmost packing has first moment
$$
\sum_j a_j^2\left(2\sum_{i<j}a_i+a_j\right)
\ge \left(\sum_j a_j^2\right)^{3/2}=B^{3/2},
$$
where the last inequality follows by expanding the square and applying $2a_i a_j\ge0$. Hence $\beta\ge\sqrt B$; reflection gives the other inequality. Equality in either side of (1) forces one triangular excursion.

Now form one positive packet $P$ by concatenating all positive excursions in their original internal order, and regard each negative excursion as a separate packet. No extremal replacement has yet been made, so every packet keeps its true intrinsic first moment. Reordering adjacent packets changes the signed first moment by
$$
m_F\ell_E-m_E\ell_F,
$$
and moving a zero gap of length $q$ past a prefix of signed area $M$ changes it by $-qM$. Sweeping the negative excursions across $P$, exactly as in the packet-sweep argument, gives a split into a left negative packet and a right negative packet together with a placement of all zero time for which the signed first moment is still zero. Denote their areas by
$$
B_L,qquad B_R,qquad B_L+B_R=A.
$$

Let $c$ be the barycenter of $P$. By (1), $P$ contains the interval $[c-h,c+h]$ inside its packet span. We may therefore replace only the positive packet by the centered triangular tent of area $A$ on that interval. This preserves its area and its barycenter exactly, does not cross either negative packet, and can only increase the positive cubic to $A^2/2$. Put
$$
L=c-h,qquad R=1-c-h,
$$
so that
$$
L+R=1-2h.
$$
All left negative mass lies in $[0,L]$ and all right negative mass lies in $[L+2h,1]$. Including any zero gaps in these two outer intervals and applying Step 1 gives
$$
\int_0^1x_-^3\,dt
\ge \Phi(B_L,L)+\Phi(B_R,R). \tag{2}
$$
Thus
$$
\int_0^1x^3\,dt
\le \frac{h^4}{2}-\Phi(B_L,L)-\Phi(B_R,R). \tag{3}
$$

Write
$$
p=\sqrt{B_L},\qquad q=\sqrt{B_R},
$$
so $p^2+q^2=h^2$. Let $c_L,c_R$ be the barycenters of the two negative packets. Applying (1) on the two outer intervals yields
$$
p\le c_L\le L-p,
$$
$$
L+2h+q\le c_R\le1-q.
$$
Since the positive and negative barycenters agree and the positive triangle is centered at $c=L+h$,
$$
p^2(c-c_L)=q^2(c_R-c)=:T. \tag{4}
$$
Hence
$$
T\ge p^2(h+p),\qquad T\ge q^2(h+q), \tag{5}
$$
while
$$
\frac{T}{p^2}+\frac{T}{q^2}=c_R-c_L\le1-p-q. \tag{6}
$$
These inequalities are the missing moment information; no symmetric replacement of a negative packet has been used.

Assume $p\le q$. Combining the second inequality in (5) with (6) gives
$$
p^2(1-p-q)\ge h^2(h+q). \tag{7}
$$
The same statement with $p,q$ exchanged holds when $q\le p$. In particular, (7) is possible only if
$$
h\le\frac1{2(1+\sqrt2)}. \tag{8}
$$
For such $h$, let $b_0$ be the smaller positive root of
$$
2b+\frac{h^2}{b}=1-2h. \tag{9}
$$
A direct monotonicity check in (7), using $q=\sqrt{h^2-p^2}$ on $0<p\le h/\sqrt2$, shows that every feasible split satisfies
$$
p\ge b_0,qquad q\ge b_0. \tag{10}
$$
For completeness, the left side minus the right side in (7) is
$$
G_h(p)=p^2\bigl(1-p-\sqrt{h^2-p^2}\bigr)
-h^2\bigl(h+\sqrt{h^2-p^2}\bigr);
$$
$G_h$ is strictly increasing on $(0,h/\sqrt2]$, and substitution of (9) gives $G_h(b_0)\le0$, proving (10).

Step 3: Minimize the negative cubic and optimize one scalar
For fixed $B$, write $b(B,S)$ for the smaller root of
$$
B=b(S-b).
$$
From Step 1,
$$
\Phi(B,S)=Bb^2-\frac{b^4}{2},
$$
and differentiation at fixed $B$ gives
$$
\frac{\partial\Phi}{\partial S}=-2b^3.
$$
Therefore $S\mapsto\Phi(B,S)$ is strictly convex.

For fixed $h,p,q$ with $p^2+q^2=h^2$, minimize
$$
\Phi(p^2,L)+\Phi(q^2,R)
$$
subject to $L+R=1-2h$. The interior critical point equalizes the two cap depths. By (10), the common value $b_0$ from (9) is admissible for both sides, so strict convexity gives the global minimum at
$$
L=b_0+\frac{p^2}{b_0},\qquad
R=b_0+\frac{q^2}{b_0}.
$$
Consequently
$$
\Phi(B_L,L)+\Phi(B_R,R)
\ge h^2b_0^2-b_0^4.
$$
Combining with (3),
$$
\int_0^1x^3\,dt
\le \frac{h^4}{2}-h^2b_0^2+b_0^4. \tag{11}
$$

Put $z=b_0/h$. Equation (9) becomes
$$
h=\frac{z}{1+2z+2z^2}.
$$
Also (10) and $p^2+q^2=h^2$ imply $2b_0^2\le h^2$, hence
$$
0<z\le\frac1{\sqrt2}.
$$
Thus the right side of (11) is
$$
J(z)=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}{(2z^2+2z+1)^5}.
$$
Therefore $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so
$$
z=\frac12,qquad h=\frac15,qquad b_0=\frac1{10},
$$
and
$$
J_{\max}=\frac1{2000}.
$$

At equality, (7) and its reflected counterpart must both be tight; hence $p=q=h/\sqrt2$, so $B_L=B_R=h^2/2$. Equality in the positive bound and in (1) makes the positive packet the centered triangle, while equality in (2) makes the two negative packets the congruent capped tents. Equation (9) then gives
$$
L=R=\frac3{10}.
$$

Step 4: Recover the unique optimal control
For $h=1/5$ and $b=1/10$, each negative block has length $3/10$ and flat part of length $1/10$. The equality profile is
$$
x(t)=
\begin{cases}
-t,&0\leq t\leq\frac{1}{10},\\
-\frac{1}{10},&\frac{1}{10}\leq t\leq\frac{1}{5},\\
t-\frac{3}{10},&\frac{1}{5}\leq t\leq\frac{1}{2},\\
\frac{7}{10}-t,&\frac{1}{2}\leq t\leq\frac{4}{5},\\
-\frac{1}{10},&\frac{4}{5}\leq t\leq\frac{9}{10},\\
t-1,&\frac{9}{10}\leq t\leq1.
\end{cases}
$$
Its positive area is $1/25$ and its two negative areas are $1/50$ each. Symmetry about $1/2$ gives both moment constraints. Differentiating yields, up to equality almost everywhere,
$$
u(t)=
\begin{cases}
-1,&0<t<\frac{1}{10},\\
0,&\frac{1}{10}<t<\frac{1}{5},\\
1,&\frac{1}{5}<t<\frac{1}{2},\\
-1,&\frac{1}{2}<t<\frac{4}{5},\\
0,&\frac{4}{5}<t<\frac{9}{10},\\
1,&\frac{9}{10}<t<1.
\end{cases}
$$
Equality in Step 2 forces one positive triangular excursion, one capped negative excursion in each outer packet, no zero gap, and the symmetric split $L=R$, $B_L=B_R$. Step 3 then forces $z=1/2$. The displayed state profile is therefore the only equality profile, and its derivative is the unique optimizer up to equality almost everywhere.

Final Answer: $\boxed{\frac{1}{2000}}$

---

## Answer

$\frac{1}{2000}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- layer-cake representation
- lipschitz excursion extremals
- moment-balanced packing
- barycenter-constrained convexity
- equality-case reconstruction