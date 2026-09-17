## Steps

Step 1: Establish the sharp one-dimensional Lipschitz bounds
Let $v$ be nonnegative and $1$-Lipschitz on $[0,L]$, with $v(0)=v(L)=0$. Write
$$
B=\int_0^L v(t)\,dt,\qquad Q=\int_0^L v(t)^3\,dt,\qquad H=\max v.
$$
For $0\leq y<H$, let $m(y)=|\{t:v(t)>y\}|$. If $0\leq y<z<H$, the $(z-y)$-neighborhood of $\{v>z\}$ lies in $\{v>y\}$, so in one dimension
$$
m(y)\geq m(z)+2(z-y).
$$
Thus $e(y)=m(y)-2(H-y)$ is nonincreasing and nonnegative. Layer cake gives
$$
B=H^2+\int_0^H e(y)\,dy,
$$
$$
Q=\frac{H^4}{2}+\int_0^H3y^2e(y)\,dy.
$$
Since $y^2$ is increasing and $e$ is nonincreasing,
$$
\int_0^H3y^2e(y)\,dy\leq H^2\int_0^He(y)\,dy.
$$
Hence
$$
Q\leq H^2B-\frac{H^4}{2}.
$$
Also $v(t)\leq\min\{t,L-t,H\}$, so
$$
B\leq HL-H^2.
$$
Equality in both inequalities forces
$$
v(t)=\min\{t,L-t,H\},
$$
a single capped tent; the cap has length $L-2H$. In particular $B\geq H^2$, with equality exactly for the uncapped tent of support length $2H$.

We also need the opposite cubic bound for fixed area and length. Assume $0<B\leq L^2/4$, and let $b\in(0,L/2]$ be the smaller root of
$$
B=bL-b^2.
$$
Set $v_b(t)=\min\{t,L-t,b\}$. For
$$
\phi(s)=s^3-3b^2s,
$$
one has $\phi(v(t))\geq\phi(v_b(t))$ pointwise: where $\min(t,L-t)\geq b$ this is
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0,
$$
and where $\min(t,L-t)<b$, both values lie in $[0,b]$, on which $\phi$ is decreasing. Because $\int v=\int v_b=B$,
$$
Q\geq b^3L-\frac32b^4,
$$
with equality only for $v=v_b$.

Step 2: Reduce the constrained control problem to two geometric parameters
For an admissible control, write $x=x_u$, and let
$$
A=\int_0^1x_+(t)\,dt=\int_0^1x_-(t)\,dt,
$$
where equality follows from $\int_0^1x=0$. If $A=0$, then $x=0$, so consider $A>0$.

Concatenate the positive components of $x$ at their zero endpoints. This preserves area, cubic integral, the $1$-Lipschitz property, and the maximum height. Let their total length be $P$ and let
$$
H=\max x>0.
$$
The state constraint gives $H\leq c$. By Step 1,
$$
\int_0^1x_+^3\leq H^2A-\frac{H^4}{2},
$$
and the capped-tent area bound gives
$$
A\leq HP-H^2,
$$
so
$$
P\geq \frac{A}{H}+H.
$$
Therefore the negative components occupy total length at most
$$
L=1-H-\frac{A}{H}.
$$
Concatenate the negative components and append a zero interval if necessary to reach length $L$. The second estimate in Step 1 applies. Let $b$ be the smaller root of
$$
A=bL-b^2.
$$
Then
$$
\int_0^1x_-^3\geq Ab^2-\frac{b^4}{2}.
$$
The defining equation for $b$ becomes
$$
A=b\left(1-H-\frac{A}{H}-b\right),
$$
so
$$
A=\frac{bH(1-H-b)}{H+b}.
$$
Set $z=b/H$. Since Step 1 gives $A\geq H^2$, substitution yields
$$
H\leq\frac{z}{(1+z)^2}.
$$
A positive objective requires $b<H$, so $0<z<1$.

Combining the positive upper bound and negative lower bound gives
$$
\int_0^1x^3\leq (H^2-b^2)\left(A-\frac{H^2+b^2}{2}\right).
$$
Using the formula for $A$ and $b=zH$, the right side is
$$
G(H,z)=\frac{H^3(1-z)}{2}\left(2z-H(1+z)^3\right).
$$

Step 3: Optimize the active and inactive state-constraint regimes
For fixed feasible $H$,
$$
\frac{\partial G}{\partial z}
=H^3(2z-1)\left(H(1+z)^2-1\right).
$$
The feasibility inequality $H\leq z/(1+z)^2$ implies $H(1+z)^2-1<0$. Hence $G(H,z)$ increases for $z<1/2$ and decreases for $z>1/2$ whenever $z=1/2$ is feasible.

If $0<H\leq2/9$, then $z=1/2$ is feasible and
$$
G(H,z)\leq G\left(H,\frac12\right)
=\frac{H^3(8-27H)}{32}.
$$
This expression is strictly increasing on $0<H<2/9$.

If $H>2/9$, feasibility forces $z>1/2$. Since $G$ decreases with $z$ there, its maximum occurs on the boundary
$$
H=\frac{z}{(1+z)^2}.
$$
Substitution gives
$$
G\leq \frac{z^4(1-z)^2}{2(1+z)^6}.
$$
For $z>1/2$, its logarithmic derivative is
$$
\frac4z-\frac2{1-z}-\frac6{1+z}
=\frac{4(1-2z)}{z(1-z^2)}<0.
$$
Thus every $H>2/9$ gives a value below the boundary value at $H=2/9$, namely $1/1458$.

Since $H\leq c$, the maximizing height is therefore
$$
H_* = \min\left(c,\frac29\right),
$$
and
$$
M(c)=\frac{\min(c,2/9)^3\left(8-27\min(c,2/9)\right)}{32}.
$$

Step 4: Recover all equality cases and all optimal controls
Equality in Step 3 forces
$$
z=\frac12,\qquad b=\frac{H_*}{2}.
$$
The common positive and negative area is then
$$
A=\frac{H_*}{3}-\frac{H_*^2}{2}.
$$
Equality in the support and cubic inequalities from Steps 1 and 2 forces exactly one positive capped tent and one negative capped tent, with no zero-time gap between them. Their flat lengths are
$$
\beta=\frac{A-H_*^2}{H_*}=\frac13-\frac{3H_*}{2},
$$
$$
\alpha=\frac{A-b^2}{b}=\frac23-\frac{3H_*}{2}.
$$
Both are nonnegative because $H_*\leq2/9$.

There are only two possible orders of the two sign components. Put $h=H_*$. If the negative component comes first, the control is, up to equality almost everywhere,
$$
u_-(t)=
\begin{cases}
-1,&0<t<\frac h2,\\
0,&\frac h2<t<\frac23-h,\\
1,&\frac23-h<t<\frac23+\frac h2,\\
0,&\frac23+\frac h2<t<1-h,\\
-1,&1-h<t<1.
\end{cases}
$$
The other optimizer is its time reverse
$$
u_+(t)=-u_-(1-t).
$$
When $c\geq2/9$, one has $h=2/9$, so the positive flat interval has length $0$ and these are exactly the two optimizers of the unconstrained problem. When $0<c<2/9$, the positive state constraint is active and the positive capped tent has a genuine boundary arc $x=c$. The equality conditions in Step 1 force the two component shapes and the no-gap tiling, so no other optimal controls exist.

Final Answer: $\boxed{M(c)=\frac{\min(c,2/9)^3(8-27\min(c,2/9))}{32}}$

---

## Answer

$M(c)=\frac{\min(c,2/9)^3(8-27\min(c,2/9))}{32}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Function or mapping

---

## Solution Concepts

- layer-cake representation
- Lipschitz extremal geometry
- state path constraints
- active constraint regimes
- equality classification
