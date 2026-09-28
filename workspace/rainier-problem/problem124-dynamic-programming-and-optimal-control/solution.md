## Steps

Step 1: Convert the terminal constraints to moments and prove sharp excursion bounds
Write $x=x_u$. From $y_u(1)=z_u(1)=0$,
$$
\int_0^1x(t)\,dt=0,\qquad \int_0^1(1-t)x(t)\,dt=0,
$$
so also $\int_0^1t x(t)\,dt=0$. Thus $x_+$ and $x_-$ have the same area and the same barycenter.

Let $v\geq0$ be $1$-Lipschitz on an interval of length $L$, vanish at its endpoints, and write
$$
B=\int v,\qquad Q=\int v^3,\qquad H=\max v.
$$
For $0\leq a<H$, put $m(a)=|\{v>a\}|$. If $a<b<H$, the $(b-a)$-neighborhood of $\{v>b\}$ lies in $\{v>a\}$, hence
$$
m(a)\geq m(b)+2(b-a).
$$
So $e(a)=m(a)-2(H-a)$ is nonnegative and nonincreasing. Layer cake gives
$$
B=H^2+\int_0^He(a)\,da,\qquad
Q=\frac{H^4}{2}+\int_0^H3a^2e(a)\,da.
$$
Since $a^2$ is increasing and $e$ is nonincreasing,
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2}.
$$
Equality holds exactly for the triangular tent of height $\sqrt B$ and length $2\sqrt B$.

For the reverse bound at fixed $B,L$, let $b$ be the smaller root of $B=bL-b^2$ and set
$$
v_b(t)=\min\{t,L-t,b\}.
$$
With $\phi(s)=s^3-3b^2s$, one has $\phi(v)\geq\phi(v_b)$ pointwise: where $v_b<b$, the endpoint Lipschitz bounds give $v\leq v_b\leq b$ and $\phi$ is decreasing; where $v_b=b$,
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0.
$$
Therefore
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2},
$$
with equality exactly for the capped tent $v_b$. Differentiating $B=bL-b^2$ at fixed $B$ gives
$$
\Phi_L(B,L)=-b^3<0.
$$

Step 2: Compress the signed excursions with exact first-moment bookkeeping
Put
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt A.
$$
We use the following one-dimensional compression lemma.

**Moment-preserving compression lemma.** For every admissible $x$ with $A>0$ there are $B_L,B_R,L,R>0$ such that
$$
B_L+B_R=A,\qquad 2h+L+R\leq1,
$$
$$
B_L(L+2h)=B_R(R+2h),
$$
and
$$
\int_0^1x(t)^3\,dt
\leq
\frac{A^2}{2}-\Phi(B_L,L)-\Phi(B_R,R).
$$
Moreover the right side is realized by a left negative capped tent, one positive triangle of area $A$, and a right negative capped tent.

To prove the lemma, first truncate to finitely many excursions; the general case follows because the omitted area, cubic integral, and first moment tend to $0$. Each excursion is zero-ended, so packets may be cut and reassembled only at zeros without violating the $1$-Lipschitz condition. Give a packet $E$ its signed area $m_E$ and length $\ell_E$. If adjacent packets $E,F$ are interchanged, then
$$
M(FE)-M(EF)=m_E\ell_F-m_F\ell_E,
$$
where $M=\int t x(t)\,dt$. In particular, moving a positive packet to the right across a negative packet increases $M$ by
$$
m_E\ell_F+|m_F|\ell_E>0.
$$
Starting from the original ordering, whose moment is $0$, move every positive excursion successively to the far left. Each swap decreases $M$, hence the all-positive-left ordering has moment $M_-\leq0$. Moving them instead to the far right increases $M$, hence the all-positive-right ordering has moment $M_+\geq0$. These signs are therefore consequences of the original moment identity, not assumptions.

Now concatenate the positive excursions in either extreme ordering. If their areas are $A_i$, Step 1 gives
$$
\int_0^1x_+^3\,dt\leq\frac12\sum_iA_i^2\leq\frac{A^2}{2},
$$
and their total length is at least
$$
2\sum_i\sqrt{A_i}\geq2\sqrt A=2h.
$$
Replace the whole positive packet by the triangle of area $A$ and length $2h$. The triangle can be placed inside the old positive packet with the same packet barycenter: indeed the argument from Step 1 applied to a nonnegative packet of area $A$ shows that its barycenter lies at least $h$ from each end of its span. Thus this replacement preserves the signed first moment exactly and releases only zero time.

For the negative excursions, keep their order and slide the compressed positive triangle from the left extreme to the right extreme. When it meets one negative excursion, use the released zero time as a separator and transfer that excursion continuously from the right packet to the left packet by the following operation: for a transfer parameter $s\in[0,1]$, split its area and available length continuously as
$$
B(s)=sB,\qquad L(s)=sL,
$$
on the left and $(1-s)B,(1-s)L$ on the right, then replace the two pieces by the corresponding capped-tent minimizers from Step 1. The endpoint configurations are exactly the two packet orders. The first moment of the resulting three-packet profile is continuous in $s$, because capped-tent centers and the roots of $B=bL-b^2$ depend continuously on $(B,L)$; at $s=0$ and $s=1$ it equals the two adjacent-order moments. The negative cubic does not exceed the pre-transfer cubic: applying the fixed-area lower bound from Step 1 separately to the two transferred pieces and summing gives the least cubic compatible with that split. Repeating this transfer across the finitely many negative excursions produces a continuous family joining the compressed all-left and all-right configurations. Since its endpoint moments satisfy $M_-\leq0\leq M_+$, the intermediate value theorem gives a configuration with $M=0$.

At that parameter value collect all negative material to the left into one packet and all negative material to the right into one packet. If their areas and lengths are $B_L,L$ and $B_R,R$, Step 1 gives the two capped-tent bounds. Writing the three block centers as
$$
\frac L2,\qquad L+h,\qquad L+2h+\frac R2,
$$
the identity $M=0$ becomes
$$
B_L\frac L2+B_R\left(L+2h+\frac R2\right)=A(L+h).
$$
Using $A=B_L+B_R$ gives
$$
B_L(L+2h)=B_R(R+2h),
$$
which proves the lemma.

Write
$$
\delta=1-(2h+L+R)\geq0.
$$
Keep $B_L,B_R$ fixed and increase
$$
L\mapsto L+\delta\frac{B_R}{A},\qquad
R\mapsto R+\delta\frac{B_L}{A}.
$$
The added lengths sum to $\delta$ and satisfy
$$
B_L\Delta L=B_R\Delta R,
$$
so the moment-balance identity is preserved. Since $\Phi_L<0$, a maximizer must use all available time:
$$
L+R=1-2h.
$$
Together with $B_L+B_R=h^2$, this yields
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
Thus $F_h'$ is strictly increasing and $F_h$ is strictly convex. Since $L+R=1-2h$,
$$
F_h(L)+F_h(R)\geq2F_h\left(\frac{1-2h}{2}\right),
$$
so the optimal split is
$$
L=R=\ell:=\frac{1-2h}{2},\qquad B_L=B_R=\frac{h^2}{2}.
$$
The cap condition is
$$
\frac{h^2}{2}\leq\frac{\ell^2}{4},
$$
equivalently $2h(1+\sqrt2)\leq1$.

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
h=\frac{z}{1+2z+2z^2},
$$
and the cap condition is $0<z\leq1/\sqrt2$.

The positive triangle contributes $h^4/2$, while the two negative caps contribute $h^2b^2-b^4$. Hence
$$
J(z)=\frac{h^4}{2}-h^2b^2+b^4
=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}{(2z^2+2z+1)^5}.
$$
Therefore $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so the unique maximizing ratio is $z=1/2$. Thus
$$
h=\frac15,\qquad b=\frac1{10},\qquad J_{\max}=\frac1{2000}.
$$

Step 4: Verify attainment
For $h=1/5$ and $b=1/10$, define
$$
x(t)=
\begin{cases}
-t,&0\leq t\leq\frac1{10},\\
-\frac1{10},&\frac1{10}\leq t\leq\frac15,\\
t-\frac3{10},&\frac15\leq t\leq\frac12,\\
\frac7{10}-t,&\frac12\leq t\leq\frac45,\\
-\frac1{10},&\frac45\leq t\leq\frac9{10},\\
t-1,&\frac9{10}\leq t\leq1.
\end{cases}
$$
It is $1$-Lipschitz, has positive area $1/25$, two negative areas $1/50$, and is symmetric about $1/2$. Hence
$$
\int_0^1x(t)\,dt=\int_0^1t,x(t)\,dt=0.
$$
Taking $u=x'$ almost everywhere gives an admissible control, and direct substitution in the cubic integral gives
$$
\int_0^1x(t)^3\,dt=\frac1{2000}.
$$
Therefore the upper bound is attained.

Final Answer: $\boxed{\frac1{2000}}$

---

## Answer

$\frac1{2000}$

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
- optimal-control attainment
