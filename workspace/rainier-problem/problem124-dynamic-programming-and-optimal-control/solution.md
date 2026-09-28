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

Step 2: Compress signed excursions while preserving the moments
Let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt{A}.
$$
We use a signed excursion-compression lemma. If $x$ is $1$-Lipschitz, $x(0)=x(1)=0$, and
$$
\int_0^1x(t)\,dt=\int_0^1t\,x(t)\,dt=0,
$$
then there are $L,R>0$ and $B_L,B_R>0$ with
$$
B_L+B_R=A,\qquad 2h+L+R\leq1,\qquad B_L(L+2h)=B_R(R+2h),
$$
such that
$$
\int_0^1x(t)^3\,dt\leq\frac{A^2}{2}-\Phi(B_L,L)-\Phi(B_R,R).
$$
The right side is attained by a left negative capped tent of area $B_L$ and length $L$, a positive triangular tent of area $A$ and length $2h$, and a right negative capped tent of area $B_R$ and length $R$.

To prove the lemma, use the components of $\{x\neq0\}$ as excursions. Each excursion has one sign and vanishes at both endpoints. Cutting and reassembling only at such endpoints preserves continuity and the $1$-Lipschitz bound. A rigid translation preserves length, area, and cubic integral. If a packet of signed area $m$ is translated by $d$, its signed first moment changes by $md$.

For the positive excursions, let their areas be $A_i$. Step 1 gives
$$
\int_0^1x_+^3\leq\frac{1}{2}\sum_iA_i^2
\leq\frac{1}{2}\left(\sum_iA_i\right)^2
=\frac{A^2}{2}.
$$
Every positive excursion of area $A_i$ has length at least $2\sqrt{A_i}$, and
$$
\sum_i2\sqrt{A_i}\geq2\sqrt{\sum_iA_i}=2h.
$$
So all positive excursions can be replaced by one triangular tent of area $A$ and length $2h$ without using more time. Equality in both positive estimates requires exactly one positive excursion, and Step 1 then forces that excursion to be the triangular tent.

For any collection $\mathcal G$ of negative excursions with total length $S$ and total area $B$, concatenate them at their zero endpoints. The result is a nonnegative $1$-Lipschitz function on an interval of length $S$. Step 1 gives
$$
\sum_{J\in\mathcal G}\int_Jx_-^3\,dt\geq\Phi(B,S).
$$
Equality requires the concatenated profile to be one capped tent, so an equality packet contains one nonzero negative excursion.

It remains to arrange one positive packet between two negative packets without changing the signed first moment. For adjacent zero-ended packets $E,F$, with lengths $\ell_E,\ell_F$ and signed areas $m_E,m_F$, interchanging their order changes the signed first moment by
$$
m_F\ell_E-m_E\ell_F.
$$
If a zero interval of length $q$ is inserted after a prefix of signed area $M$, the complementary suffix shifts by $q$, changing the signed first moment by $-qM$. Starting from the original ordering, commute positive excursions until they form one packet. After each interchange, distribute the available zero time, including the time released by replacing the positive excursions with their minimal triangle, across neighboring interfaces so that the affine moment correction cancels the interchange change. The correction varies continuously with inserted zero length. The all-left-negative and all-right-negative placements give opposite signs, while the original arrangement has signed first moment $0$, so the sweep reaches a placement with signed first moment exactly $0$. Every cut is made at a zero endpoint, so the positive and negative parts remain disjoint and the $1$-Lipschitz condition is unchanged. For countably many excursions, apply the construction to finite truncations and pass to the limit; the omitted area, cubic integral, and first moment tend to $0$.

After the sweep, merge each negative packet into the capped tent from Step 1. Put their areas and lengths equal to $B_L,L$ and $B_R,R$. Translating the three-block packet so that its left endpoint is $0$, the block centers are
$$
\frac{L}{2},\qquad L+h,\qquad L+2h+\frac{R}{2}.
$$
Equality of the positive and negative first moments becomes
$$
B_L\frac{L}{2}+B_R\left(L+2h+\frac{R}{2}\right)=A(L+h).
$$
Using $A=B_L+B_R$ reduces this to
$$
B_L(L+2h)=B_R(R+2h),
$$
which proves the stated moment balance.

Write the unused time as
$$
\delta=1-(2h+L+R)\geq0.
$$
Keep $B_L,B_R$ fixed and set
$$
\Delta L=\delta\frac{B_R}{A},\qquad
\Delta R=\delta\frac{B_L}{A}.
$$
Then $\Delta L+\Delta R=\delta$ and $B_L\Delta L=B_R\Delta R$, so replacing $L,R$ by $L+\Delta L,R+\Delta R$ preserves the balance identity and uses all free time. Since $\Phi_L(B,L)<0$ for $B>0$, a maximizer must have
$$
L+R=1-2h.
$$
Combining this with $B_L+B_R=h^2$ and the balance identity gives
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
Because $b'(s)<0$, $F_h'$ is strictly increasing, so $F_h$ is strictly convex. Since $L+R=1-2h$,
$$
F_h(L)+F_h(R)\geq2F_h\left(\frac{1-2h}{2}\right),
$$
with equality only when
$$
L=R=\ell:=\frac{1-2h}{2},\qquad B_L=B_R=\frac{h^2}{2}.
$$
The capped tents exist exactly when
$$
\frac{h^2}{2}\leq\frac{\ell^2}{4},
$$
equivalently $2h(1+\sqrt{2})\leq1$. Equality in the compression forces one central positive triangle, two congruent outer negative capped tents, and no zero gaps.

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