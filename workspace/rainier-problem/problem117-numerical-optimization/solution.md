## Steps

Step 1: Reduce the three shifts to a two-parameter rational minimax problem
Let the three positive shifts be $\alpha,\beta,\delta$ with $\alpha\beta\delta=8$, and put
$$
A=\alpha+\beta+\delta,
\qquad
B=\alpha\beta+\alpha\delta+\beta\delta.
$$
The three-step spectral factor is
$$
r_{A,B}(x)
=\prod_{s\in\{\alpha,\beta,\delta\}}\frac{x-s}{x+s}
=\frac{x^3-Ax^2+Bx-8}{x^3+Ax^2+Bx+8}.
$$
Its denominator is positive for $x>0$. Define
$$
\phi_{A,B}(x)=\frac{1+r_{A,B}(x)}{1-r_{A,B}(x)}
=\frac{x(x^2+B)}{Ax^2+8}.
$$
Since $|r|=\tanh(|\log\phi|/2)$, minimizing the worst value of $|r|$ is equivalent to minimizing the multiplicative envelope $K\ge1$ for which
$$
K^{-1}\le \phi_{A,B}(x)\le K.
$$
Also
$$
r_{A,B}'(x)
=\frac{2\bigl(Ax^4+(24-AB)x^2+8B\bigr)}{(x^3+Ax^2+Bx+8)^2}. \tag{1}
$$
Thus there are at most two positive stationary points.

We will repeatedly use the following exact optimality certificate. Suppose $a<b<c$ are active with signs $+,-,+$ and level $C$, and set
$$
K=\frac{1+C}{1-C}.
$$
For fixed $C$, the three inequalities $r(a)\le C$, $-r(b)\le C$, $r(c)\le C$ are half-planes in $(A,B)$. After positive rescaling their outward normals are
$$
n_+(x)=(-Kx^2,x),
\qquad
n_-(x)=(x^2,-Kx).
$$
The three cofactors are
$$
bc(b-K^2c),
\qquad Kac(a-c),
\qquad ab(K^2a-b).
$$
Hence if
$$
K^2a<b<K^2c, \tag{2}
$$
all three cofactors have the same sign. The three normals then positively span $\mathbb R^2$, so the intersection of the three active half-planes is the single point $(A,B)$. Therefore no other parameters can have norm at most $C$ even on those three points. If the candidate also satisfies the envelope on all of $E_\gamma$, it is the unique global minimizer.

Step 2: Parametrize every moving-branch candidate and find the first transition
Let $u\in(1,2)$ be the positive interior active point, while $8$ is the other positive active point. Imposing
$$
r'(u)=0,
\qquad
\phi(u)=\phi(8)
$$
and using (1) gives, after eliminating $A,B$,
$$
A(u)=\frac{2(u+4)}{u^2},
\qquad
B(u)=u(u+16). \tag{3}
$$
For these values,
$$
\phi(u)=\phi(8)=u^2. \tag{4}
$$
The second stationary point is
$$
v(u)=2\sqrt{\frac{u(u+16)}{u+4}}, \tag{5}
$$
which is strictly increasing in $u$.

If $b$ is the negative active point, the opposite-level condition
$$
\phi(b)=u^{-2}
$$
is exactly
$$
F(b,u)=0, \tag{6}
$$
where
$$
F(x,u)=u^4x^3-2(u+4)x^2+u^5(u+16)x-8u^2.
$$
In the initial plateau the negative active point is the second stationary point $v$. At a stationary point $x$, equation (1) gives
$$
\phi(x)=\frac{2x^3}{Ax^2-8}.
$$
Using the two stationary roots in (1), one finds
$$
\phi(u)\phi(v)=\frac{(uv)^3}{64}.
$$
Since the active values are reciprocal, $uv=4$. At the first transition $v=\gamma_1$, so $u_0=4/\gamma_1$. Combining $uv=4$ with (5) gives
$$
\gamma_1^4+\gamma_1^3-64\gamma_1-16=0. \tag{7}
$$
The polynomial in (7) is negative at $3$, positive at $4$, and has positive derivative on $[3,4]$, hence it has a unique root there. Thus
$$
\gamma_1=\mathrm{root}_{(3,4)}(x^4+x^3-64x-16),
\qquad
u_0:=\frac4{\gamma_1}.
$$
Numerically, $\gamma_1\approx3.7787240783$ and $u_0\approx1.0585583697$.

For $3\le\gamma<\gamma_1$, the parameters (3) with $u=u_0$ are fixed. The two stationary points are $u_0$ and $\gamma_1$, and
$$
\mathcal A_\gamma=\{u_0,\gamma_1,8\}
$$
with signs $+,-,+$. At $\gamma=\gamma_1$ the same set is active, with $r'(\gamma_1)=0$.

Step 3: Follow the moving regime and locate the final plateau
Define
$$
G(u)=u^6+16u^5+4u^4-4u^2-4u-16. \tag{8}
$$
Since
$$
G(1)=-3,
\qquad
G(2)=600,
$$
and
$$
G'(u)=6u^5+80u^4+16u^3-8u-4>0
\qquad(1\le u\le2),
$$
there is a unique
$$
u_*:=\mathrm{root}_{(1,2)}(G). \tag{9}
$$
In fact $1.03<u_*<1.04<u_0<1.06$.

For $\gamma_1<\gamma<\gamma_2$, define $u_\gamma$ by
$$
F(\gamma,u_\gamma)=0,
\qquad
u_*<u_\gamma<u_0. \tag{10}
$$
This root is unique: on
$$
3.77\le x\le6.31,
\qquad
1.03\le u\le1.06,
$$
one has $F_u>0$. At $u=u_0$, using (7),
$$
F(x,u_0)=\frac{128}{\gamma_1^4}(2x-1)(x-\gamma_1)^2>0
\qquad(x>\gamma_1).
$$
At $u=u_*$, equation (8) gives
$$
F(x,u_*)=(x-2)
\left[u_*^4x^2+2(u_*^4-u_*-4)x+4u_*^2\right]. \tag{11}
$$
The quadratic in (11) has one root below $1$ and one root in $(6,7)$; call the latter $\gamma_2$. Therefore (10) has exactly one solution throughout the open middle regime.

The moment at which the unused endpoint $2$ reaches the negative level is
$$
F(2,u)=2G(u)=0,
$$
so it occurs precisely at $u=u_*$. Solving the quadratic in (11) gives
$$
\gamma_2
=\frac{4+u_*-u_*^4+
\sqrt{(u_*^4-u_*-4)^2-4u_*^6}}{u_*^4}. \tag{12}
$$
Thus $6<\gamma_2<7$ and numerically $\gamma_2\approx6.3031785765$.

For the middle regime, (3), (4), and (6) give
$$
\phi(u_\gamma)=\phi(8)=u_\gamma^2,
\qquad
\phi(\gamma)=u_\gamma^{-2}.
$$
The other stationary point $v(u_\gamma)$ lies in $(2,\gamma)$ because $u_\gamma<u_0$ and (5) is increasing. On the left interval,
$$
\phi(u)\phi(1)-1
=\frac{(u-1)(u^5+17u^4+18u^3+18u^2+10u+8)}{\text{positive denominator}}>0,
$$
while
$$
\phi(u)\phi(2)-1
=\frac{G(u)}{\text{positive denominator}}>0
$$
for $u>u_*$. Hence the whole left interval stays inside the envelope. On $[\gamma,8]$, $\phi$ is increasing because its second stationary point lies in the gap. Therefore
$$
\mathcal A_\gamma=\{u_\gamma,\gamma,8\}
\qquad(\gamma_1<\gamma<\gamma_2).
$$
At $\gamma=\gamma_2$ the endpoint $2$ joins the active set:
$$
\mathcal A_{\gamma_2}=\{u_*,2,\gamma_2,8\}.
$$

Step 4: Verify the final plateau, shift feasibility, and optimality
For $\gamma_2<\gamma\le7$, keep $u=u_*$ and the fixed coefficients (3). The second stationary point is
$$
v_*=2\sqrt{\frac{u_*(u_*+16)}{u_*+4}}<4<\gamma_2.
$$
The equation for the negative level factors as (11): besides $2$ and $\gamma_2$, its third crossing lies below $1$. Thus on $[1,2]$ the only active points are $u_*$ and $2$, while on $[\gamma,8]$ the function is monotone and only $8$ is active. Hence
$$
\mathcal A_\gamma=\{u_*,2,8\}
\qquad(\gamma_2<\gamma\le7).
$$

It remains to check that the parameters (3) really come from three positive shifts. Their shifts are the roots of
$$
t^3-A(u)t^2+B(u)t-8.
$$
For $u_*\le u\le u_0\subset(1.03,1.06)$ its discriminant is
$$
-\frac{4(u-1)(u+1)(u^2+1)}{u^6}
\left(u^8+48u^7+768u^6+4096u^5-64u^3-768u^2-3072u-4096\right)>0.
$$
The parenthesized factor is increasing but still negative at $1.06$. Thus there are three distinct real roots; since $A(u)>0$, $B(u)>0$, and their product is $8>0$, all three are positive.

Finally, all three regimes have an active triple $a<b<8$ with signs $+,-,+$, where $a=u\in(1.03,1.06)$, $b\ge2$, and $K=\phi(u)=u^2$. Hence
$$
K^2a=u^5<2\le b<8u^4=K^2\cdot8.
$$
Condition (2) holds, so the half-plane certificate from Step 1 proves global optimality and uniqueness in every regime.

Step 5: Determine the regularity of the optimal contraction factor at the transitions
On the moving branch, (4) gives
$$
\mathcal C_\gamma^*
=\frac{u_\gamma^2-1}{u_\gamma^2+1},
\qquad
F(\gamma,u_\gamma)=0. \tag{13}
$$
Both outer regimes are plateaus, so all one-sided derivatives from the left of $\gamma_1$ and from the right of $\gamma_2$ vanish.

At $\gamma_1$, put $g=\gamma_1$ and $u_0=4/g$. The factorization in Step 3 shows
$$
F_x(g,u_0)=0,
$$
so implicit differentiation of (13) gives $u_\gamma'(g+)=0$. Hence $(\mathcal C_\gamma^*)'(g+)=0$, matching the plateau derivative on the left. Differentiating once more gives
$$
u_\gamma''(g+)=-\frac{F_{xx}(g,u_0)}{F_u(g,u_0)}.
$$
Using
$$
F_{xx}(g,u_0)=\frac{256(2g-1)}{g^4},
$$
$$
F_u(g,u_0)
=-\frac{2\left(g^6-128g^4+32g^3-10240g-3072\right)}{g^4},
$$
and
$$
\frac{d}{du}\frac{u^2-1}{u^2+1}\Big|_{u=4/g}
=\frac{16g^3}{(g^2+16)^2},
$$
we obtain the first nonzero derivative from the moving side:
$$
\boxed{
(\mathcal C_\gamma^*)''(\gamma_1+)
=\frac{2048g^3(2g-1)}{(g^2+16)^2
\left(g^6-128g^4+32g^3-10240g-3072\right)}
}. \tag{14}
$$
This number is negative (numerically about $-0.0125006593$), whereas $(\mathcal C_\gamma^*)''(\gamma_1-)=0$. Thus $\mathcal C_\gamma^*$ is $C^1$ but not $C^2$ at $\gamma_1$.

At $\gamma_2$, put $s=u_*$ and $h=\gamma_2$. From (13),
$$
u_\gamma'(h-)=-\frac{F_x(h,s)}{F_u(h,s)}.
$$
Therefore the first nonzero derivative from the moving side is
$$
\boxed{
(\mathcal C_\gamma^*)'(\gamma_2-)
=-\frac{4s\left(3s^4h^2-4(s+4)h+s^5(s+16)\right)}
{(s^2+1)^2\left(4s^3h^3-2h^2+(6s^5+80s^4)h-16s\right)}
}. \tag{15}
$$
It is nonzero and negative (numerically about $-0.0166392750$), while $(\mathcal C_\gamma^*)'(\gamma_2+)=0$ on the final plateau. Hence $\mathcal C_\gamma^*$ is continuous but not $C^1$ at $\gamma_2$.

Therefore the exact pair requested for the final answer is $\gamma_1$ from (7) and $u_*$ from (9); equation (12) gives the second transition exactly, while (14)-(15) give the requested transition sensitivities.

Final Answer: $\boxed{\left(\mathrm{root}_{(3,4)}(x^4+x^3-64x-16),\mathrm{root}_{(1,2)}(x^6+16x^5+4x^4-4x^2-4x-16)\right)}$

---

## Answer

$(\mathrm{root}_{(3,4)}(x^4+x^3-64x-16),\mathrm{root}_{(1,2)}(x^6+16x^5+4x^4-4x^2-4x-16))$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- constrained ADI shift tuning
- rational minimax envelopes
- active-set sensitivity
- algebraic phase transitions
