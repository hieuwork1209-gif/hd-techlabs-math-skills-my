## Steps

Step 1: Convert the terminal constraints to moments and prove the one-excursion bounds
Write $x=x_u$. Since $y_u(1)=0$ and $z_u(1)=0$,
$$
\int_0^1x(t)\,dt=0,\qquad \int_0^1(1-t)x(t)\,dt=0,
$$
so also $\int_0^1t x(t)\,dt=0$. Thus $x$ is $1$-Lipschitz, $x(0)=x(1)=0$, and its positive and negative parts have the same area and the same barycenter.

We use two sharp estimates. Let $v\geq0$ be $1$-Lipschitz on an interval of length $L$, vanish at both endpoints, and set
$$
B=\int v,\qquad Q=\int v^3.
$$
If $H=\max v$, layer cake with $m(a)=|\{v>a\}|$ gives $B\geq H^2$ and
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2}.
$$
Equality in the last bound holds exactly for the triangular tent of height $\sqrt B$ and length $2\sqrt B$.

For the opposite direction assume $0<B\leq L^2/4$, and let $b$ be the smaller root of
$$
B=bL-b^2.
$$
For $v_b(t)=\min\{t,L-t,b\}$ and $\phi(s)=s^3-3b^2s$, one has $\phi(v)\geq\phi(v_b)$ pointwise: on $[0,b]$ the function $\phi$ is decreasing, while for $s\geq b$,
$$
\phi(s)-\phi(b)=(s-b)^2(s+2b)\geq0.
$$
Since $\int v=\int v_b=B$,
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2},
$$
with equality exactly for the capped tent $v_b$. Writing $D=\sqrt{L^2-4B}$, direct differentiation gives
$$
\Phi_{BB}=\frac{3(L-D)}{D}\geq0,\qquad \det D^2\Phi=0,
$$
and
$$
\Phi_L=-\frac{(L-D)^3}{4}<0.
$$
Hence $\Phi$ is jointly convex and decreases with the available length.

Step 2: Reduce every maximizer to a symmetric three-block profile
Let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt>0.
$$
The moment identities from Step 1 also give
$$
\int_0^1t x_+(t)\,dt=\int_0^1t x_-(t)\,dt.
$$
Put $h=\sqrt A$. Concatenating positive excursions at zero does not change their area or cubic integral. The first estimate in Step 1 therefore gives
$$
\int x_+^3\leq\frac{A^2}{2}=\frac{h^4}{2},
$$
and the comparison triangle uses the least possible positive time, namely $2h$.

For fixed $A$, compress same-sign excursions before comparing their placement: replacing a positive excursion of area $B$ by its triangular extremal uses the minimum length $2\sqrt B$ and does not decrease its cubic integral, while concatenating negative excursions on the same side and replacing the concatenation by the capped-tent extremal does not increase the negative cubic integral. The block centers can then be translated while preserving the common barycenter. Thus the least-span configuration relevant to a maximizer has one positive block between one negative block on each side.

Write the left and right negative areas as $Ap^2$ and $Aq^2$, where $p^2+q^2=1$. Their least possible support lengths are $2hp$ and $2hq$. Place the positive triangle of length $2h$ between them and let $g_1,g_2\geq0$ be the two intervening zero gaps. Equality of the positive and negative barycenters is then
$$
-p^2g_1+q^2g_2+h(q-p)(1+pq+p+q)=0.
$$
Assume $q\geq p$ and put $r=q/p\geq1$. For fixed $p,q$, the least total gap has $g_2=0$. The resulting total span $T$ satisfies
$$
\frac{T}{h}=\frac{r^3+r^2\sqrt{1+r^2}+2r+\sqrt{1+r^2}+1}{\sqrt{1+r^2}}.
$$
Its derivative has numerator
$$
2r^4+2r^3\sqrt{1+r^2}+3r^2+2r\sqrt{1+r^2}-r+2>0
$$
for $r\geq1$. Thus the least span occurs at $p=q=1/\sqrt2$, with no asymmetric gap. Consequently every feasible moment-balanced path satisfies
$$
2h(1+\sqrt2)\leq1,
$$
and, for maximizing the cubic, it is optimal to center the positive triangle and split the negative area equally on the two sides.

The positive triangle leaves total negative time $1-2h$. Let
$$
\ell=\frac{1-2h}{2}.
$$
If the two negative sides have data $(B_1,L_1)$ and $(B_2,L_2)$, then $B_1+B_2=A$ and $L_1+L_2\leq1-2h$. By the convexity and monotonicity of $\Phi$,
$$
\Phi(B_1,L_1)+\Phi(B_2,L_2)
\geq2\Phi\left(\frac A2,\frac{L_1+L_2}{2}\right)
\geq2\Phi\left(\frac A2,\ell\right).
$$
Therefore a maximizer must have one central positive triangle and two congruent outer negative capped tents, with no unused time. This reduction also shows that equality forces this three-block geometry.

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
Thus $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so the unique maximizing ratio is
$$
z=\frac12.
$$
Therefore
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
Its positive area equals the total negative area, and it is symmetric about $1/2$, so both moment constraints hold. Differentiating gives, up to equality almost everywhere,
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
Every inequality in Steps 1 and 2 must be an equality at the optimum, so the positive triangle, equal outer areas, equal negative caps, and absence of gaps are forced. Hence this control is the unique optimizer almost everywhere.

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