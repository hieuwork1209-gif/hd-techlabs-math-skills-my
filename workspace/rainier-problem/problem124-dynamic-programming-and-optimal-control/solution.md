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
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt{A}.
$$
If $A=0$, then $x=0$, so assume $A>0$.

If $v\geq0$ is $1$-Lipschitz on an interval of length $S$, vanishes at both endpoints, has area $B>0$, and has barycenter
$$
\beta=\frac{1}{B}\int_0^S t\,v(t)\,dt,
$$
then
$$
\sqrt{B}\leq\beta\leq S-\sqrt{B}.
$$
Let $H=\max v$ and $m(a)=|\{v>a\}|$. Since $v(t)\leq t$, the first moment of $\{v>a\}$ is at least
$$
a\,m(a)+\frac{m(a)^2}{2}.
$$
From Step 1 write $m(a)=2(H-a)+e(a)$ with $e$ nonnegative and nonincreasing, and put $E=\int_0^H e(a)\,da$. Layer cake gives $B=H^2+E$, while integrating the preceding level-set bound gives
$$
\int_0^S t\,v(t)\,dt
\geq H^3+\frac{3H}{2}E+\frac{E^2}{2H}.
$$
The inequality
$
\left(1+\frac32r+\frac12r^2\right)^2\geq(1+r)^3,qquad r=E/H^2,
$
shows that this is at least $B^{3/2}$. Thus $\beta\geq\sqrt B$; reflection gives $\beta\leq S-\sqrt B$. Equality forces the triangular tent.

Concatenate the positive excursions, preserving shapes and order, into a zero-ended compound packet $P$. Let its occupied length be $S$ and let its intrinsic barycenter, measured from the left end of its span, be $\beta$. Applying the barycenter margin to this compound packet gives
$$
h\leq\beta\leq S-h.
$$
The triangle of area $A$ and length $2h$ centered at $\beta$ therefore fits inside $P$. Replacing $P$ by it preserves area and intrinsic barycenter, hence preserves signed first moment, and raises the positive cubic at most to $A^2/2$ because
$$
\frac12\sum_i A_i^2\leq\frac12\left(\sum_iA_i\right)^2=\frac{A^2}{2}.
$$
The replacement releases $S-2h$ units of zero time without changing the signed first moment.

Now sweep the negative excursions across this barycenter-preserving positive triangle. For a fixed split, let $B_L$ be the unsigned area of the negative excursions already moved to the left and let $B_R=A-B_L$ be the unsigned area of those still on the right. Let $D$ be the signed first moment of the corresponding gapless packet order, and let $q$ be the total available zero time, including both the original zero intervals and the time released from $P$. If $q_L$ is placed between the left negative packet and the positive triangle, and $q_R=q-q_L$ between the triangle and the right negative packet, then translating the suffixes gives
$$
M(q_L)=D+B_Lq_L-B_Rq_R
      =D-qB_R+Aq_L.
$$
Thus, for this split, the admissible signed first moments form the whole interval
$$
[D-qB_R,\ D+qB_L].
$$
Varying $q_L$ preserves all excursion shapes and the $1$-Lipschitz bound.

At the all-left split the signed first moment is positive; at the all-right split it is negative. Between consecutive splits, one negative excursion crosses the positive packet. The right endpoint of the earlier admissible interval and the left endpoint of the later interval are the two extreme placements of the same available zero time during that crossing, so the successive intervals meet. Hence the union of admissible intervals is connected and crosses $0$, giving a split with zero signed first moment. Countably many excursions follow by finite truncation.

Let the chosen negative packet areas be $B_L,B_R$, so
$$
B_L+B_R=A.
$$
Let $c$ be the barycenter of the positive triangle. Put
$$
L=c-h,\qquad R=1-c-h,
$$
so
$$
L+R=1-2h.
$$
All left negative mass lies in $[0,L]$ and all right negative mass lies in $[L+2h,1]$. We do not replace either negative packet by a symmetric shape. Instead, extend each packet by zero to its whole outer interval and apply Step 1 directly:
$$
\int_0^1x_-^3\,dt\geq\Phi(B_L,L)+\Phi(B_R,R).
$$
Therefore
$$
\int_0^1x^3\,dt
\leq\frac{h^4}{2}-\Phi(B_L,L)-\Phi(B_R,R).
$$

Write
$$
p=\sqrt{B_L},\qquad q=\sqrt{B_R},
$$
so $p^2+q^2=h^2$. Let $c_L,c_R$ be the barycenters of the two negative packets. The barycenter margin on the two outer intervals gives
$$
p\leq c_L\leq L-p,\qquad
L+2h+q\leq c_R\leq1-q.
$$
Since the positive and negative barycenters agree and the positive triangle is centered at $c=L+h$,
$$
p^2(c-c_L)=q^2(c_R-c)=:T.
$$
Hence
$$
T\geq p^2(h+p),\qquad T\geq q^2(h+q),
$$
and
$$
\frac{T}{p^2}+\frac{T}{q^2}
=c_R-c_L\leq1-p-q.
$$

Assume $p\leq q$. Using the second lower bound for $T$ gives the necessary inequality
$$
p^2(1-p-q)\geq h^2(h+q).
$$
Set $q=\sqrt{h^2-p^2}$ and define
$$
G_h(p)=p^2(1-p-q)-h^2(h+q).
$$
On $0<p\leq h/\sqrt2$,
$$
G_h'(p)
=p\left(2-3p-q+\frac{2p^2}{q}\right)>0,
$$
because Step 1 gives $h\leq1/2$, so $3p+q\leq2\sqrt2\,h\leq\sqrt2<2$. Thus feasibility implies
$$
0\leq G_h(p)\leq G_h\left(\frac{h}{\sqrt2}\right)
=\frac{h^2}{2}\left(1-2(1+\sqrt2)h\right),
$$
so
$$
h\leq\frac{1}{2(1+\sqrt2)}.
$$

For such $h$, let $b_0$ be the smaller positive root of
$$
2b+\frac{h^2}{b}=1-2h.
$$
Then $0<b_0\leq h/\sqrt2$. Write $z=b_0/h$ and $r=\sqrt{1-z^2}$. The defining equation gives
$$
h=\frac{z}{1+2z+2z^2}.
$$
Substituting $p=b_0$ into $G_h$ yields
$$
G_h(b_0)
=\frac{z^3\left(z^3-z^2r+2z^2+z-r-1\right)}
{(1+2z+2z^2)^3}.
$$
Since $0<z\leq1/\sqrt2$ gives $r\geq z$,
$$
z^3-z^2r+2z^2+z-r-1
\leq2z^2-1\leq0.
$$
Thus $G_h(b_0)\leq0$. Because $G_h$ is increasing and every feasible $p$ has $G_h(p)\geq0$, we obtain $p\geq b_0$. Reflection gives $q\geq b_0$. No negative packet has been symmetrically replaced.

Step 3: Minimize the negative cubic and optimize one scalar
For fixed $B$, let $b(B,S)$ be the smaller root of
$$
B=b(S-b).
$$
By Step 1,
$$
\Phi(B,S)=Bb^2-\frac{b^4}{2}.
$$
Differentiating at fixed $B$ gives
$$
\frac{\partial\Phi}{\partial S}=-2b^3.
$$
Since $b(B,S)$ decreases with $S$, this derivative increases, so $\Phi(B,S)$ is strictly convex in $S$.

For fixed $h,p,q$ with $p^2+q^2=h^2$, minimize
$$
\Phi(p^2,L)+\Phi(q^2,R)
$$
under $L+R=1-2h$. Strict convexity makes the minimum equalize the two cap depths. Since $p,q\geq b_0$ and $2b_0+h^2/b_0=1-2h$, the minimum is attained at
$$
L=b_0+\frac{p^2}{b_0},\qquad
R=b_0+\frac{q^2}{b_0},
$$
and therefore
$$
\Phi(B_L,L)+\Phi(B_R,R)
\geq h^2b_0^2-b_0^4.
$$
Thus
$$
\int_0^1x^3\,dt
\leq\frac{h^4}{2}-h^2b_0^2+b_0^4.
$$

Put $z=b_0/h$. The relation from Step 2 gives
$$
h=\frac{z}{1+2z+2z^2},\qquad 0<z\leq\frac{1}{\sqrt2}.
$$
The upper bound becomes
$$
J(z)=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}
{(2z^2+2z+1)^5}.
$$
Therefore $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so
$$
z=\frac12,\qquad h=\frac15,\qquad b_0=\frac1{10},
$$
and the maximum upper bound is
$$
\frac1{2000}.
$$

At equality, the reverse cubic bounds force the two negative packets themselves to be capped tents with the common depth $b_0$. Their lengths are
$
L=b_0+\frac{p^2}{b_0},\qquad
R=b_0+\frac{q^2}{b_0}.
$
Their barycenters are therefore the midpoints of the two outer intervals. Substituting these midpoints into the zero first-moment condition gives
$
0=\frac{(p-q)(p+q)\left(b_0^2+2b_0h+p^2+q^2\right)}{2b_0},
$
so $p=q=h/\sqrt2$. Hence $B_L=B_R=h^2/2$, and with $h=1/5$, $b_0=1/10$ the length formulas give
$
L=R=\frac3{10}.
$

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
Equality in Step 2 forces one positive triangular excursion, one capped negative excursion in each outer packet, no zero gap, and the symmetric split $L=R$, $B_L=B_R$. Step 3 then forces $z=1/2$. Thus the displayed derivative is the unique optimizer up to equality almost everywhere.

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