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
Thus $e(a)=m(a)-2(H-a)$ is nonnegative and nonincreasing. Layer cake gives
$$
B=H^2+\int_0^He(a)\,da,\qquad
Q=\frac{H^4}{2}+\int_0^H3a^2e(a)\,da.
$$
Since $a^2$ is increasing and $e$ is nonincreasing,
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2}.
$$
Equality holds exactly for the triangular tent of height $\sqrt B$ and length $2\sqrt B$.

For the reverse cubic bound at fixed $B,L$, let $b$ be the smaller root of $B=bL-b^2$ and set $v_b(t)=\min\{t,L-t,b\}$. With $\phi(s)=s^3-3b^2s$, one has $\phi(v)\geq\phi(v_b)$ pointwise: where $v_b<b$, the endpoint Lipschitz bounds give $v\leq v_b\leq b$ and $\phi$ is decreasing, while where $v_b=b$,
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0.
$$
Therefore
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2},
$$
with equality exactly for the capped tent $v_b$. Also $\Phi_L<0$, so for fixed area extra available length can only decrease the least possible cubic cost.

Step 2: Compress the sign pattern and solve the barycenter placement
We use the preceding estimates as a signed compression lemma. Decompose $x$ into its nonzero excursions. Replacing positive excursions by triangular extremals and merging them at their area-weighted barycenter weakly increases the positive cubic and uses no more total time because
$$
2\sqrt{B_1+B_2}\leq2\sqrt{B_1}+2\sqrt{B_2}.
$$
The replacement preserves the positive area and its first moment. On each side of that barycenter, concatenate negative excursions and apply the capped-tent lower bound to the concatenation; this weakly decreases the negative cubic. Any freed zero time can be absorbed into a negative block, again decreasing its cubic cost because $\Phi_L<0$. The common-barycenter condition forces negative mass on both sides of the positive block. Thus every competitor is dominated by a three-block path consisting of a central positive triangle and one negative capped tent on each side; equality in the compression forces this same three-block geometry.

Let the positive area be $A=h^2$, so its triangle has height $h$ and length $2h$. Let the left negative block have length $L$, the right one length
$$
R=1-2h-L,
$$
and let their areas be $B_L,B_R$. Since the three symmetric blocks tile $[0,1]$, their centers are $L/2$, $L+h$, and $L+2h+R/2$. The equations
$$
B_L+B_R=h^2,\qquad
B_L\frac L2+B_R\left(L+2h+\frac R2\right)=h^2(L+h)
$$
give
$$
B_L=\frac{h^2(1-L)}{1+2h},\qquad
B_R=\frac{h^2(1-R)}{1+2h}.
$$
Put
$$
k=\frac{h^2}{1+2h},\qquad B(s)=k(1-s),\qquad F_h(s)=\Phi(B(s),s).
$$
If $b(s)$ is the smaller root of $B(s)=b(s-b)$, implicit differentiation gives
$$
b'(s)=-\frac{k+b}{s-2b}<0.
$$
Since $F_h(s)=b^3s-\frac32b^4$, differentiation along the barycenter constraint yields the simple formula
$$
F_h'(s)=-b^2(2b+3k).
$$
The right side is strictly increasing in $s$ because $b'(s)<0$. Hence $F_h$ is strictly convex on its feasible interval. Since $L+R=1-2h$, the total negative cubic
$$
F_h(L)+F_h(R)
$$
is uniquely minimized at
$$
L=R=\ell:=\frac{1-2h}{2},\qquad B_L=B_R=\frac{h^2}{2}.
$$
Feasibility of either cap is $h^2/2\leq\ell^2/4$, equivalently
$$
2h(1+\sqrt2)\leq1.
$$
Thus every maximizer is symmetric about $1/2$ and has one central positive triangle and two congruent outer negative capped tents.

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
The cap-fit condition $2b\leq\ell$ is equivalent to $0<z\leq1/\sqrt2$.

The positive triangle contributes $h^4/2$, while the two negative caps contribute $h^2b^2-b^4$. Hence
$$
J(z)=\frac{h^4}{2}-h^2b^2+b^4
=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}{(2z^2+2z+1)^5}.
$$
Therefore $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so the unique maximizing ratio is $z=1/2$. Consequently
$$
h=\frac15,\qquad b=\frac1{10},\qquad J_{\max}=\frac1{2000}.
$$

Step 4: Recover the unique optimal control
For $h=1/5$ and $b=1/10$, each negative block has length $3/10$ and flat part of length $1/10$. The equality profile is
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
Its positive area is $1/25$ and its two negative areas are $1/50$ each. Symmetry about $1/2$ gives both moment constraints. Differentiating yields, up to equality almost everywhere,
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
Every inequality in Steps 1 and 2 is strict unless the excursion shapes, the three-block packing, and the left-right split are exactly those displayed. Hence this control is the unique optimizer almost everywhere.

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
- equality-case reconstruction