## Steps

Step 1: Reduce the recurrence to two coupled stability inequalities

For fixed $z$, the recurrence gives
$$
u_m=R_{a,b}(z)^m u_0.
$$
Thus it is bounded for every complex $u_0$ exactly when $|R_{a,b}(z)|\leq1$. Hence an admissible $L$ must satisfy this bound on both pieces of $\Sigma_L$.

If $L>2$, put
$$
u=a+bL.
$$
At the real endpoint $z=L$, the lower bound $R_{a,b}(L)\geq-1$ gives
$$
u\geq\frac{L-2}{L^2}. \tag{1}
$$
At the imaginary endpoint $z=iL/2$,
$$
|R_{a,b}(iL/2)|^2
=\left(1-\frac{aL^2}{4}\right)^2
+\frac{L^2}{4}\left(1+\frac{bL^2}{4}\right)^2. \tag{2}
$$

Step 2: Derive a sharp upper bound from a hidden square completion

Substitute $a=u-bL$ into the right side of (2). Direct expansion gives the exact identity
$$
|R_{a,b}(iL/2)|^2
=
\frac15\left(L-1+\frac{L^2u}{4}\right)^2
+\frac{5L^6}{64}
\left(
b-\frac{4(L^2u-L-4)}{5L^3}
\right)^2. \tag{3}
$$
If $L$ is admissible, then the left side is at most $1$. By (1), for $L>2$,
$$
L-1+\frac{L^2u}{4}
\geq L-1+\frac{L-2}{4}
=\frac{5L-6}{4}>0.
$$
Therefore (3) implies
$$
1\geq\frac{(5L-6)^2}{80}.
$$
Thus every admissible $L>2$ satisfies
$$
L\leq r:=\frac{6+4\sqrt5}{5}.
$$
Since $r>2$, the same bound is automatic when $L\leq2$. Hence
$$
\rho(a,b)\leq r
$$
for every pair $(a,b)$.

Step 3: Determine the only possible equality pair

Suppose $L=r$ is admissible. Equality must hold at every stage of Step 2. Hence
$$
u=\frac{r-2}{r^2}
$$
and the second square in (3) must vanish. Consequently
$$
b_*=-\frac{24}{5r^3},
\qquad
a_*=u-b_*r=\frac{5r+14}{5r^2}. \tag{4}
$$
Since $r=(6+4\sqrt5)/5$, these simplify to
$$
a_*=\frac{425-155\sqrt5}{121},
\qquad
b_*=\frac{15525-7050\sqrt5}{1331}. \tag{5}
$$
Thus any maximizer, if it exists, is unique.

Step 4: Verify the real-axis constraint for the candidate

From (4),
$$
a_*+b_*r=\frac{r-2}{r^2},
$$
so
$$
R_{a_*,b_*}(r)=-1.
$$
Also
$$
R_{a_*,b_*}'(s)=-1+2a_*s+3b_*s^2.
$$
The discriminant of this quadratic is $4(a_*^2+3b_*)$. Using
$$
25r^2-60r-44=0
$$
one obtains
$$
a_*^2+3b_*=
\frac{25r^2-220r+196}{25r^4}
=\frac{80(3-2r)}{25r^4}<0,
$$
because $2<r<3$. Hence $R_{a_*,b_*}'(s)<0$ for every real $s$. Therefore $R_{a_*,b_*}$ decreases from $1$ at $s=0$ to $-1$ at $s=r$, and
$$
|R_{a_*,b_*}(s)|\leq1
\qquad(0\leq s\leq r).
$$

Step 5: Verify the imaginary-axis constraint and finish uniqueness

For $y\in[0,r/2]$, put $t=y^2$. Then
$$
|R_{a_*,b_*}(iy)|^2-1
=tG(t),
$$
where
$$
G(t)=1-2a_*+(a_*^2+2b_*)t+b_*^2t^2.
$$
The polynomial $G$ is convex because its quadratic coefficient is $b_*^2>0$. Also $a_*>1/2$, so $G(0)<0$. Equality in (3) at $L=r$ gives
$$
|R_{a_*,b_*}(ir/2)|=1,
$$
hence $G(r^2/4)=0$. A convex function lies below the chord joining its endpoint values, so
$$
G(t)\leq0
\qquad\left(0\leq t\leq\frac{r^2}{4}\right).
$$
Thus
$$
|R_{a_*,b_*}(iy)|\leq1
\qquad(0\leq y\leq r/2).
$$
Therefore $\rho(a_*,b_*)\geq r$, while Step 2 gives $\rho_*\leq r$. Hence $\rho_* = r$.

If another pair had $\rho(a,b)=r$, continuity would make $r$ admissible, and the equality conditions in Steps 2 and 3 would force exactly the coefficients in (4). Thus the maximizing pair is unique.

Final Answer: $\boxed{(\frac{6+4\sqrt5}{5},\frac{425-155\sqrt5}{121},\frac{15525-7050\sqrt5}{1331})}$

## Answer

$(\frac{6+4\sqrt5}{5},\frac{425-155\sqrt5}{121},\frac{15525-7050\sqrt5}{1331})$

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

## Solution Concepts

- coupled real and imaginary stability
- endpoint square completion
- equality-case rigidity
- convex quadratic envelope

## Black-Box Audit

The sharp bound comes from the explicit identity (3), followed by elementary endpoint and convexity arguments. No extremal-polynomial theorem or computational black box is used.
