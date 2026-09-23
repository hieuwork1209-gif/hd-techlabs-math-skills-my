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
B=H^2+\int_0^He(a)\,da,
$$
$$
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

Step 2: Replace the informal layer slide by a moment-preserving excursion compression
Let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,\qquad h=\sqrt A.
$$
We use the following lemma. Its point is that no superlevel set is slid independently, so there is no hidden compatibility issue between nesting, disjointness, the barycenter constraint, and the Lipschitz bound.

**Signed excursion-compression lemma.** Suppose \(x\) is \(1\)-Lipschitz, \(x(0)=x(1)=0\), and
\[
\int_0^1x=0,\qquad \int_0^1t\,x(t)\,dt=0.
\]
If \(A>0\), then there are \(L,R>0\) and \(B_L,B_R>0\) such that
\[
B_L+B_R=A,\qquad 2h+L+R\leq1,
\]
\[
B_L(L+2h)=B_R(R+2h),
\tag{2.1}
\]
and
\[
\int_0^1x(t)^3\,dt
\leq
\frac{A^2}{2}-\Phi(B_L,L)-\Phi(B_R,R).
\tag{2.2}
\]
The right side is realized by a contiguous packet consisting of a left negative capped tent of area \(B_L\) and length \(L\), then a positive triangular tent of area \(A\) and length \(2h\), then a right negative capped tent of area \(B_R\) and length \(R\). Equality in the compression part of (2.2) can occur only when the positive part of \(x\) is already one triangular excursion and the negative part consists of exactly two excursions which, after deleting zero intervals, are the two capped tents in that order.

Here is a proof with the moment bookkeeping made explicit. Since \(x\) is continuous, each component of \(\{x\neq0\}\) is an open interval on which \(x\) has one sign and vanishes at the two endpoints. Call such a component an excursion. Cutting and reassembling only at these zero endpoints never creates a jump, and rigid horizontal translation of an excursion preserves its slopes, its area, and its cubic integral. If an excursion of unsigned area \(B\) is translated by \(d\), its unsigned first moment changes by exactly \(Bd\). Thus translating a positive packet of area \(P\) by \(d_+\) and a negative packet of area \(N\) by \(d_-\) preserves equality of the two barycenters precisely when
\[
P\,d_+=N\,d_-.
\tag{2.3}
\]

For a positive excursion \(I_i\), let its area be \(A_i\). Step 1 gives
\[
\int_{I_i}x_+^3\leq\frac{A_i^2}{2}.
\]
Hence
\[
\int_0^1x_+^3
\leq\frac12\sum_iA_i^2
\leq\frac12\left(\sum_iA_i\right)^2
=\frac{A^2}{2}.
\tag{2.4}
\]
Also every positive excursion of area \(A_i\) has length at least \(2\sqrt{A_i}\), so all positive excursions can be replaced by one triangular tent of area \(A\) and length \(2h\) without using more time. Both inequalities in (2.4), together with the length inequality, are equalities only when there is one positive excursion and it is exactly the triangular tent from Step 1.

For the negative excursions, first retain their individual lengths and areas. If a collection \(\mathcal G\) of negative excursions has total length \(S\) and total area \(B\), concatenate those excursions at their zero endpoints. This gives a nonnegative \(1\)-Lipschitz function on an interval of length \(S\), still of area \(B\), whose cubic integral is the sum of the cubics of the excursions. The reverse inequality from Step 1 therefore gives
\[
\sum_{J\in\mathcal G}\int_Jx_-^3\geq\Phi(B,S).
\tag{2.5}
\]
Equality in (2.5) forces the concatenated profile to be the single capped tent, so in particular there can be no nontrivial internal zero and hence only one nonzero excursion in that packet.

It remains only to explain why the excursions may be packed into two negative packets around the one positive packet while preserving the common barycenter. This is a one-dimensional cut-and-paste statement. Give every excursion its signed area
\[
m(I)=\int_Ix(t)\,dt,
\]
so positive excursions have \(m(I)>0\), negative excursions have \(m(I)<0\), and \(\sum_I m(I)=0\). For a packet starting at \(s\), its signed first moment is its intrinsic signed first moment plus \(s\) times its signed area. Thus all dependence on horizontal placement is affine.

For two adjacent zero-ended packets \(E,F\), of lengths \(\ell_E,\ell_F\) and signed areas \(m_E,m_F\), interchanging their order changes the total signed first moment by
\[
\Delta(E,F)=m_F\ell_E-m_E\ell_F.
\tag{2.6}
\]
Likewise, inserting a zero interval of length \(q\) after a prefix of signed area \(M\) shifts the complementary suffix by \(q\) and changes the signed first moment by
\[
-qM,
\tag{2.7}
\]
because the total signed area is zero. Equations (2.6) and (2.7) give an explicit balancing algorithm: bubble all positive excursions into one middle packet. Whenever an adjacent interchange changes the signed first moment, put the necessary amount of the available zero time, including the time released when the positive excursions are replaced by their single minimal triangle, at the interface whose prefix has the opposite signed area; (2.7) gives the unique nonnegative correction. If the correction exhausts that interface, continue at the next one. Because the original ordering itself has signed first moment \(0\), the running signed moment starts on one side of \(0\) in the all-left-negative ordering and ends on the other side in the all-right-negative ordering, so this finite or countable sweep must stop with signed moment exactly \(0\). No block is ever cut away from a zero: the only operations are interchange at zero endpoints, rigid translation, and replacement by the Step 1 extremal. Therefore disjointness and the \(1\)-Lipschitz bound are preserved throughout. For countably many excursions, apply the construction to the first finitely many nonzero excursions and pass to the limit; the omitted total area and cubic tend to \(0\), while the moment identities are continuous.

At the end of this sweep there is one positive packet between a left and a right negative packet. Merge each negative packet by (2.5). If their areas and lengths are \(B_L,L\) and \(B_R,R\), respectively, translate the whole three-block packet as one unit so that its left endpoint is \(0\). The three block centers are then
\[
\frac L2,\qquad L+h,\qquad L+2h+\frac R2.
\]
Equality of the positive and negative first moments is therefore
\[
B_L\frac L2+B_R\left(L+2h+\frac R2\right)
=A(L+h),
\]
which, using \(A=B_L+B_R\), is exactly (2.1). This proves the lemma and, at the same time, proves that the rearrangement is feasible rather than merely formal.

We now remove the remaining zero time explicitly. Put
\[
\delta=1-(2h+L+R)\geq0.
\]
Keep \(B_L,B_R\) fixed and set
\[
\Delta L=\delta\,\frac{B_R}{A},\qquad
\Delta R=\delta\,\frac{B_L}{A}.
\tag{2.8}
\]
Then \(\Delta L+\Delta R=\delta\), and
\[
B_L\Delta L=B_R\Delta R.
\]
Consequently (2.1) remains true after replacing \(L,R\) by \(L+\Delta L,R+\Delta R\). Thus the extra time is absorbed into the two negative blocks while preserving both their total area and the common barycenter. Since \(\Phi_L(B,L)<0\) whenever \(B>0\), this operation strictly decreases the total negative cubic unless \(\delta=0\). Therefore every maximizer must satisfy
\[
L+R=1-2h.
\tag{2.9}
\]

With (2.9), equations \(B_L+B_R=h^2\) and (2.1) give
\[
B_L=\frac{h^2(1-L)}{1+2h},\qquad
B_R=\frac{h^2(1-R)}{1+2h}.
\tag{2.10}
\]
Put
\[
k=\frac{h^2}{1+2h},\qquad B(s)=k(1-s),\qquad F_h(s)=\Phi(B(s),s).
\]
If \(b(s)\) is the smaller root of \(B(s)=b(s-b)\), then
\[
b'(s)=-\frac{k+b}{s-2b}<0.
\]
Since
\[
F_h(s)=b^3s-\frac32b^4,
\]
differentiation along the constraint \(B(s)=k(1-s)\) gives
\[
F_h'(s)=-b^2(2b+3k).
\]
Because \(b'(s)<0\), this derivative is strictly increasing, so \(F_h\) is strictly convex on its feasible interval. From \(L+R=1-2h\),
\[
F_h(L)+F_h(R)
\geq
2F_h\!\left(\frac{1-2h}{2}\right),
\]
with equality only at
\[
L=R=\ell:=\frac{1-2h}{2}.
\]
Then (2.10) gives
\[
B_L=B_R=\frac{h^2}{2}.
\]
The cap-feasibility condition \(h^2/2\leq\ell^2/4\) is equivalent to
\[
2h(1+\sqrt2)\leq1.
\]
Thus, for fixed \(h\), equality in the sharp compression bound forces one central positive triangle and two congruent outer negative capped tents, with no zero gaps.

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
The equality conditions are now explicit. Equality in (2.4) forces a single positive triangular excursion. Equality in (2.5) forces exactly one capped negative excursion in each outer packet. Equality in the zero-time step forces \(\delta=0\), and strict convexity of \(F_h\) forces \(L=R\) and \(B_L=B_R\). Finally Step 3 has the unique maximizing ratio \(z=1/2\). Hence the displayed state profile is the only equality profile; differentiating it shows that the displayed control is the unique optimizer up to equality almost everywhere.

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