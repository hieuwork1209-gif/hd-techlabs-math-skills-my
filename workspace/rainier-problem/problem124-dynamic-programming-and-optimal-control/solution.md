## Steps

Step 1: Convert the terminal constraints to moments and prove the two excursion bounds
Write $x=x_u$. From $y_u(1)=z_u(1)=0$,
$$
\int_0^1x(t)\,dt=0,\qquad \int_0^1(1-t)x(t)\,dt=0,
$$
so also
$$
\int_0^1t\,x(t)\,dt=0.
$$
Thus $x_+$ and $x_-$ have the same area and the same barycenter.

Let $v\geq0$ be $1$-Lipschitz on an interval of length $L$, vanish at its endpoints, and set
$$
B=\int v,\qquad Q=\int v^3,\qquad H=\max v.
$$
For $0\leq a<H$, put $m(a)=|\{v>a\}|$. If $0\leq a<b<H$, the $(b-a)$-neighborhood of $\{v>b\}$ lies in $\{v>a\}$, hence
$$
m(a)\geq m(b)+2(b-a).
$$
Therefore $e(a)=m(a)-2(H-a)$ is nonnegative and nonincreasing. Layer cake gives
$$
B=H^2+\int_0^He(a)\,da,
$$
and
$$
Q=\frac{H^4}{2}+\int_0^H3a^2e(a)\,da.
$$
Since $a^2$ is increasing and $e$ is nonincreasing,
$$
\int_0^H3a^2e(a)\,da\leq H^2\int_0^He(a)\,da,
$$
so
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2}.
$$
Equality is attained by the triangular tent of height $\sqrt B$ and length $2\sqrt B$.

For the reverse bound at fixed $B,L$, let $b$ be the smaller root of $B=bL-b^2$ and set
$$
v_b(t)=\min\{t,L-t,b\}.
$$
With $\phi(s)=s^3-3b^2s$, one has $\phi(v)\geq\phi(v_b)$ pointwise: where $v_b<b$, the endpoint Lipschitz bounds give $v\leq v_b\leq b$ and $\phi$ is decreasing, while where $v_b=b$,
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0.
$$
Since $\int v=\int v_b=B$,
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2}.
$$
Also $\Phi_L(B,L)<0$ for $B>0$.

Step 2: Prove the moment-preserving three-block compression with an explicit slack interval
Put
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt A.
$$
If $A=0$, then $x=0$. Assume $A>0$.

We use the following one-dimensional packet lemma. For a finite collection of zero-ended signed $1$-Lipschitz excursions with total signed area and signed first moment both zero, replace all positive excursions by one triangular tent of area $A$ and length $2h$. Partition the negative excursions into a left packet and a right packet, then concatenate within each packet. Let their unsigned areas and occupied lengths be $B_L,B_R$ and $L,R$. The packets can be chosen so that
$$
B_L+B_R=A,qquad 2h+L+R\leq1,
$$
and, with
$$
q=1-(2h+L+R),
$$
the signed first moment $D$ of the gapless order
$$
\text{left negative packet},\quad\text{positive triangle},\quad\text{right negative packet}
$$
satisfies
$$
-qB_L\leq D\leq qB_R.
$$

Here is the bookkeeping. Rigid translation of a packet of signed area $m$ by $d$ changes its signed first moment by $md$. If adjacent packets $E,F$, with lengths $\ell_E,\ell_F$ and signed areas $m_E,m_F$, are interchanged, then
$$
\Delta M=m_E\ell_F-m_F\ell_E.
$$
Starting with the original excursion order, move positive excursions toward one another. At each adjacent positive-negative interchange, assign the negative excursion to the side it has just entered and record the released zero length created when the positive excursions already collected are replaced by their single minimal triangle. A direct induction on these interchanges gives the invariant
$$
-qB_L\leq D\leq qB_R.
$$
Indeed, before an interchange the admissible corrections to $D$ form the interval obtained by placing all currently unused zero time immediately before or immediately after the positive packet. When a positive packet of signed area $P>0$ and length $p$ crosses a negative packet of unsigned area $B>0$ and length $r$, the gapless moment changes by
$$
Pr+Bp.
$$
The two endpoint corrections change by exactly the same quantities, because moving a zero interval of length $s$ from the right interface to the left interface changes the signed first moment by
$$
s(B_L+B_R)=sA.
$$
Thus the old correction interval and the new correction interval meet at the interchange value, so their union is again an interval. Iterating from the original configuration, whose signed first moment is $0$, proves that $0$ remains inside the final correction interval. For countably many excursions, apply the finite statement to truncations and pass to the limit; the omitted areas and first moments tend to zero.

Now place a zero gap of length $q_L$ between the left negative packet and the positive triangle and a gap of length $q_R=q-q_L$ between the positive triangle and the right negative packet. Relative to the gapless moment $D$, the first gap shifts the suffix of signed area $B_L$, while the second shifts only the right negative packet. Hence
$$
M(q_L)=D+B_Lq_L-B_Rq_R
      =D-qB_R+Aq_L.
$$
As $q_L$ runs through $[0,q]$, this fills the entire interval
$$
[D-qB_R,\,D+qB_L].
$$
The invariant above is exactly
$$
D-qB_R\leq0\leq D+qB_L,
$$
so there is a choice of $q_L$ for which $M(q_L)=0$. This proves the missing continuity statement and shows explicitly that the available slack is sufficient.

Concatenate the negative excursions inside each packet. By Step 1 their cubic contributions satisfy
$$
\int_{\mathrm{left}}x_-^3\,dt\geq\Phi(B_L,L),\qquad
\int_{\mathrm{right}}x_-^3\,dt\geq\Phi(B_R,R).
$$
The positive contribution is at most $A^2/2$. Therefore
$$
\int_0^1x(t)^3\,dt
\leq
\frac{A^2}{2}-\Phi(B_L,L)-\Phi(B_R,R).
$$

Any remaining zero time can now be absorbed into the two negative lengths without losing the moment constraint. Set
$$
\Delta L=q\frac{B_R}{A},\qquad
\Delta R=q\frac{B_L}{A}.
$$
Then $\Delta L+\Delta R=q$ and $B_L\Delta L=B_R\Delta R$, so the signed first moment remains zero. Since $\Phi_L<0$, this only improves the upper bound. Hence we may assume
$$
L+R=1-2h.
$$
For the resulting contiguous three-block profile, the block centers are
$$
\frac{L}{2},\qquad L+h,\qquad L+2h+\frac{R}{2}.
$$
The zero first moment is therefore equivalent to
$$
B_L(L+2h)=B_R(R+2h).
$$
Together with $B_L+B_R=h^2$, this gives
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
and differentiation gives
$$
F_h'(s)=-b^2(2b+3k).
$$
Thus $F_h'$ is strictly increasing and $F_h$ is strictly convex. Since $L+R=1-2h$,
$$
F_h(L)+F_h(R)\geq
2F_h\left(\frac{1-2h}{2}\right).
$$
Hence the sharp upper bound for fixed $h$ is obtained at
$$
L=R=\ell:=\frac{1-2h}{2},\qquad B_L=B_R=\frac{h^2}{2}.
$$
The capped tents exist exactly when
$$
\frac{h^2}{2}\leq\frac{\ell^2}{4},
$$
equivalently
$$
2h(1+\sqrt2)\leq1.
$$

Step 3: Optimize the remaining scalar parameter
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
and the cap-fit condition is $0<z\leq1/\sqrt2$.

The positive triangle contributes $h^4/2$, while the two negative caps contribute $h^2b^2-b^4$. Therefore
$$
J(z)=\frac{h^4}{2}-h^2b^2+b^4
=\frac{z^4(2z^4-2z^2+1)}{2(2z^2+2z+1)^4}.
$$
Differentiation gives
$$
J'(z)=\frac{2z^3(z+1)^2(2z-1)(2z^2-1)}{(2z^2+2z+1)^5}.
$$
Thus $J$ increases on $(0,1/2)$ and decreases on $(1/2,1/\sqrt2)$, so its maximum occurs at $z=1/2$. Consequently
$$
h=\frac15,\qquad b=\frac1{10},\qquad J_{\max}=\frac1{2000}.
$$

Step 4: Exhibit an admissible control that attains the upper bound
For $h=1/5$ and $b=1/10$, take
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
Its positive area is $1/25$ and the two negative areas are $1/50$ each. The profile is symmetric about $1/2$, so
$$
\int_0^1x(t)\,dt=0,qquad
\int_0^1t\,x(t)\,dt=\frac12\int_0^1x(t)\,dt=0.
$$
Thus the three terminal constraints hold. Its derivative satisfies $|x'|\leq1$ almost everywhere, so it comes from an admissible control. The cubic integral equals the upper bound computed in Step 3, namely $1/2000$.

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
- optimal control with state constraints