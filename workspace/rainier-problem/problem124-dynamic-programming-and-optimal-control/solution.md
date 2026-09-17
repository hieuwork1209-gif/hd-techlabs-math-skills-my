## Steps

Step 1: Convert the terminal constraints to moments and prove the one-excursion bounds
Write $x=x_u$. Since $y_u(1)=0$ and $z_u(1)=0$,
$$
\int_0^1x(t)\,dt=0,\qquad \int_0^1(1-t)x(t)\,dt=0,
$$
so also $\int_0^1t x(t)\,dt=0$. Thus $x$ is $1$-Lipschitz, $x(0)=x(1)=0$, and its positive and negative parts have the same area and the same barycenter.

We need two sharp one-excursion estimates. Let $v\geq0$ be $1$-Lipschitz on an interval of length $L$, vanish at both endpoints, and set
$$
B=\int v,\qquad Q=\int v^3,\qquad H=\max v.
$$
For $0\leq a<H$, let $m(a)=|\{v>a\}|$. If $0\leq a<b<H$, the $(b-a)$-neighborhood of $\{v>b\}$ lies in $\{v>a\}$, hence
$$
m(a)\geq m(b)+2(b-a).
$$
Therefore $e(a)=m(a)-2(H-a)$ is nonnegative and nonincreasing. Layer cake gives
$$
B=H^2+\int_0^H e(a)\,da,
$$
$$
Q=\frac{H^4}{2}+\int_0^H3a^2e(a)\,da.
$$
Since $a^2$ is increasing and $e$ is nonincreasing,
$$
\int_0^H3a^2e(a)\,da\leq H^2\int_0^He(a)\,da.
$$
Thus
$$
Q\leq H^2B-\frac{H^4}{2}.
$$
Also $B\geq H^2$, so the right side is at most $B^2/2$. Equality holds exactly for the triangular tent of height $\sqrt B$ and length $2\sqrt B$.

For the opposite direction assume $0<B\leq L^2/4$, and let $b$ be the smaller root of
$$
B=bL-b^2.
$$
Set $v_b(t)=\min\{t,L-t,b\}$ and $\phi(s)=s^3-3b^2s$. Where $v_b<b$, both $v$ and $v_b$ lie in $[0,b]$ and $\phi$ is decreasing; where $v_b=b$,
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0.
$$
Hence $\phi(v)\geq\phi(v_b)$ pointwise. Because $\int v=\int v_b=B$,
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2},
$$
with equality exactly for the capped tent $v_b$. Writing $D=\sqrt{L^2-4B}$, differentiation gives
$$
\Phi_{BB}=\frac{3(L-D)}{D}\geq0,\qquad \det D^2\Phi=0,
$$
$$
\Phi_L=-\frac{(L-D)^3}{4}<0.
$$
Thus $\Phi$ is jointly convex and decreases when more length is available.

Step 2: Prove the moment-balanced compression and identify the extremal geometry
Let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt>0,
$$
so the moment identities from Step 1 give
$$
\int_0^1t x_+(t)\,dt=\int_0^1t x_-(t)\,dt.
$$
Put $h=\sqrt A$.

We first compress excursions without worsening the objective. Concatenating positive excursions at zero preserves their total area and cubic integral, and Step 1 bounds the latter by $A^2/2=h^4/2$; the equality profile is one triangle and uses the minimum possible positive length $2h$. On either side of the common barycenter, concatenate all negative excursions and use the lower estimate from Step 1 on the concatenation. This preserves the side area and available length while replacing that side by one capped tent with no larger negative cubic contribution. Zero gaps can then be translated between the three remaining blocks without changing any integral; their positions are fixed by the common-barycenter equation. Hence an extremizer may be sought among three alternating blocks: one positive triangle and one negative block on each side.

To solve the placement constraint, write the left and right negative areas as $Ap^2$ and $Aq^2$, where $p^2+q^2=1$. Their minimum possible lengths are $2hp$ and $2hq$. Put the positive triangle of length $2h$ between them and let $g_1,g_2\geq0$ be the two zero gaps. Taking the left endpoint as $0$, the three block centers are
$$
hp,\qquad 2hp+g_1+h,\qquad 2hp+g_1+2h+g_2+hq.
$$
Equating the area-weighted negative center to the positive center gives
$$
-p^2g_1+q^2g_2+h(q-p)(1+pq+p+q)=0.
$$
Assume $q\geq p$ and put $r=q/p\geq1$. The least total gap has $g_2=0$, and the corresponding total span $T$ is
$$
\frac{T}{h}=\frac{r^3+r^2\sqrt{1+r^2}+2r+\sqrt{1+r^2}+1}{\sqrt{1+r^2}}.
$$
Its derivative has numerator
$$
2r^4+2r^3\sqrt{1+r^2}+3r^2+2r\sqrt{1+r^2}-r+2>0
$$
for $r\geq1$. Therefore the least span occurs only at $r=1$, so the extremal placement has equal outer areas and no asymmetric gap. In particular feasibility requires
$$
2h(1+\sqrt2)\leq1.
$$

The positive triangle leaves total negative time $1-2h$. Let
$$
\ell=\frac{1-2h}{2}.
$$
For left/right negative data $(B_1,L_1)$ and $(B_2,L_2)$, one has $B_1+B_2=A$ and $L_1+L_2\leq1-2h$. Joint convexity and monotonicity of $\Phi$ give
$$
\Phi(B_1,L_1)+\Phi(B_2,L_2)
\geq2\Phi\left(\frac A2,\frac{L_1+L_2}{2}\right)
\geq2\Phi\left(\frac A2,\ell\right).
$$
Thus the negative cubic is minimized by two congruent capped tents of length $\ell$, and all available time is used. Combined with the positive equality condition, every maximizer has one central positive triangle and two congruent outer negative capped tents. The equality statements in Step 1 show that no other excursion shapes can attain the same value.

Step 3: Optimize the two heights
Let $b$ be the depth of either negative cap. Since each negative block has area $A/2=h^2/2$ and length $\ell=(1-2h)/2$,
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
The cap must fit in its block, $2b\leq\ell$, which is equivalent to $0<z\leq1/\sqrt2$.

The positive triangle contributes $h^4/2$. The two negative caps contribute
$$
h^2b^2-b^4.
$$
Hence
$$
J(z)=\frac{h^4}{2}-h^2b^2+b^4
=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}{(2z^2+2z+1)^5}.
$$
Thus $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so the unique maximizing ratio is $z=1/2$. Consequently
$$
h=\frac15,\qquad b=\frac1{10},\qquad J_{\max}=\frac1{2000}.
$$

Step 4: Recover the unique optimal control
For $h=1/5$ and $b=1/10$, each negative block has length $3/10$ and its flat part has length $1/10$. The equality profile is
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
Its positive area is $1/25$ and its two negative areas are $1/50$ each; symmetry about $1/2$ then gives both terminal moment constraints. Differentiating yields, up to equality almost everywhere,
$$
u(t)=
\begin{cases}
-1,&0<t<\frac1{10},\\
0,&\frac1{10}<t<\frac15,\\
1,&\frac15<t<\frac12,\\
-1,&\frac12<t<\frac45,\\
0,&\frac45<t<\frac9{10},\\
1,&\frac9{10}<t<1.
\end{cases}
$$
Every bound in Steps 1 and 2 is sharp only for the displayed triangle/caps and the symmetric packing, so this control is the unique optimizer almost everywhere.

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
- convexity of capped-tent cost
- equality-case reconstruction