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

Step 2: Prove a moment-preserving three-block compression with an explicit slack interval
Let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt{A}.
$$
If $A=0$, then $x=0$, so assume $A>0$. We use the excursions, namely the components of $\{x\neq0\}$. Every excursion is zero-ended, so concatenating excursions at zero endpoints preserves continuity and the $1$-Lipschitz bound.

For the positive excursions, let the areas be $A_i$. Step 1 gives
$$
\int_0^1x_+^3\,dt\leq\frac12\sum_iA_i^2
\leq\frac12\left(\sum_iA_i\right)^2
=\frac{A^2}{2}.
$$
Their total occupied length is at least $2\sum_i\sqrt{A_i}\geq2h$. Thus they may be replaced, for the purpose of an upper bound, by one positive triangular packet $P$ of area $A$ and length $2h$; the replacement releases only zero time. Equality here requires one positive excursion, already equal to that triangle.

For any collection $\mathcal G$ of negative excursions with total area $B$ and total occupied length $S$, concatenate them at their zero endpoints. Step 1 then gives
$$
\sum_{J\in\mathcal G}\int_Jx_-^3\,dt\geq\Phi(B,S).
$$
Hence once the negative excursions have been divided into a left packet and a right packet, with data $(B_L,L)$ and $(B_R,R)$, replacing each packet by its capped tent can only decrease the negative cubic.

It remains to justify that such a division can be made without losing the first-moment constraint. We use the following packet-sweep fact. Give a zero-ended packet $E$ its signed area $m_E$ and length $\ell_E$. If adjacent packets $E,F$ are interchanged, their contribution to the signed first moment changes by
$$
m_F\ell_E-m_E\ell_F.
$$
If a zero interval of length $q$ is inserted after a prefix of signed area $M$, the complementary suffix is translated by $q$, so the signed first moment changes by $-qM$.

Compress all positive excursions into $P$, but keep track of every unit of length released by this compression together with every zero interval already present. During the finite packet sweep, negative excursions already passed by $P$ form the left packet and those not yet passed form the right packet. Let $D$ be the signed first moment of the corresponding gapless order and let $q$ be the total currently available zero length. If $q_L$ is placed between the left negative packet and $P$ and $q_R=q-q_L$ between $P$ and the right negative packet, then
$$
M(q_L)=D+B_Lq_L-B_Rq_R
      =D-qB_R+Aq_L.
$$
Therefore the admissible first moments for this fixed packet split form the entire closed interval
$$
I=[D-qB_R,\,D+qB_L].
$$
This is the required continuous interpolation: varying $q_L$ through $[0,q]$ changes an actual zero gap continuously, never cuts a nonzero excursion, and preserves the $1$-Lipschitz condition.

We now show that one of these intervals contains $0$. Before the sweep starts, place every negative packet to the left of $P$. Since the positive and negative masses are both $A$, if their barycenters are $c_+$ and $c_-$ then $c_-<c_+$ and
$$
M_{\mathrm{left}}=A(c_+-c_-)>0.
$$
With every negative packet to the right, $c_->c_+$ and
$$
M_{\mathrm{right}}=A(c_+-c_-)<0.
$$
Between two consecutive packet splits, only one adjacent negative excursion changes side. The gapless moment changes by the interchange formula above, while the two endpoints of $I$ change affinely by exactly the moment obtained by putting all currently available zero time on the corresponding interface. Thus the right endpoint of the earlier interval and the left endpoint of the later interval are the two endpoint placements of the same zero-gap translation; the intermediate placements are $M(q_L)$ and fill the whole interval between them. Consequently the union of the successive admissible intervals is connected and joins a positive value to a negative value. The intermediate value theorem therefore gives a split and a placement of the available zero time for which $M=0$. For countably many excursions, apply the argument to finite truncations; the omitted area, cubic integral, and first moment tend to $0$.

For that split,
$$
B_L+B_R=A,\qquad 2h+L+R\leq1,
$$
and
$$
\int_0^1x(t)^3\,dt
\leq\frac{A^2}{2}-\Phi(B_L,L)-\Phi(B_R,R).
$$
Write the unused time as
$$
\delta=1-(2h+L+R)\geq0.
$$
Keeping $B_L,B_R$ fixed, enlarge the two negative lengths by
$$
\Delta L=\delta\frac{B_R}{A},\qquad
\Delta R=\delta\frac{B_L}{A}.
$$
Then $\Delta L+\Delta R=\delta$ and $B_L\Delta L=B_R\Delta R$, so the signed first moment is unchanged. Since $\Phi_L(B,L)<0$, a maximizer must use all available time:
$$
L+R=1-2h.
$$
The three block centers are then
$$
\frac{L}{2},\qquad L+h,\qquad L+2h+\frac{R}{2}.
$$
The zero first moment is therefore
$$
B_L\frac{L}{2}+B_R\left(L+2h+\frac{R}{2}\right)=A(L+h),
$$
or, using $A=B_L+B_R$,
$$
B_L(L+2h)=B_R(R+2h).
$$
Hence
$$
B_L=\frac{h^2(1-L)}{1+2h},\qquad
B_R=\frac{h^2(1-R)}{1+2h}.
$$

Put
$$
k=\frac{h^2}{1+2h},\qquad B(s)=k(1-s),\qquad F_h(s)=\Phi(B(s),s).
$$
If $b(s)$ is the smaller root of $B(s)=b(s-b)$, then
$$
b'(s)=-\frac{k+b}{s-2b}<0,
$$
and
$$
F_h'(s)=-b^2(2b+3k).
$$
Thus $F_h'$ is strictly increasing, so $F_h$ is strictly convex. Since $L+R=1-2h$,
$$
F_h(L)+F_h(R)\geq2F_h\left(\frac{1-2h}{2}\right),
$$
with equality only when
$$
L=R=\ell:=\frac{1-2h}{2},\qquad
B_L=B_R=\frac{h^2}{2}.
$$
The capped tents exist exactly when
$$
\frac{h^2}{2}\leq\frac{\ell^2}{4},
$$
equivalently $2h(1+\sqrt{2})\leq1$. Equality in the compression therefore forces one central positive triangle, two congruent outer negative capped tents, and no zero gap.

Step 3: Optimize the two heights
Let $b$ be the depth of either negative cap. Since each cap has area $h^2/2$ and length $\ell=(1-2h)/2$,
$$
\frac{h^2}{2}=b\ell-b^2,
$$
so
$$
h^2=b(1-2h)-2b^2.
$$
Put $z=b/h$. Then
$$
h=\frac{z}{1+2z+2z^2}.
$$
The cap-fit condition $2b\leq\ell$ is equivalent to $0<z\leq1/\sqrt{2}$.

The positive triangle contributes $h^4/2$, while the two negative caps contribute $h^2b^2-b^4$. Hence
$$
J(z)=\frac{h^4}{2}-h^2b^2+b^4
=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}{(2z^2+2z+1)^5}.
$$
Therefore $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt{2})$, so the unique maximizing ratio is $z=1/2$. This gives
$$
h=\frac{1}{5},\qquad b=\frac{1}{10},\qquad J_{\max}=\frac{1}{2000}.
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