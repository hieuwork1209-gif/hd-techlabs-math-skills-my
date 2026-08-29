## Steps

Step 1: Reduce power boundedness to two competing scalar bands

Write
$$
R=R_{a,b}(s),\qquad
S=S_{a,b}(s)
=1-s+\frac32as^2+\frac52bs^3.
$$
A direct induction gives
$$
M_{a,b}(s)^m
=
\begin{pmatrix}
R^m&s(R^m-S^m)\\
0&S^m
\end{pmatrix}
\qquad(m\geq1).
$$
Therefore the orbit is bounded for every initial vector exactly when
$$
|R_{a,b}(s)|\leq1
\quad\text{and}\quad
|S_{a,b}(s)|\leq1. \tag{1}
$$
Indeed, these inequalities make every entry of the displayed power bounded, while the diagonal entries show necessity.

Step 2: Derive the sharp length from a positive dual inequality

Assume that a pair $(a,b)$ is stable on $[0,L]$, and fix any $x\in(0,1)$. Put
$$
E_1=R_{a,b}(xL)+1,\qquad
E_2=1-R_{a,b}(L),\qquad
E_3=S_{a,b}(L)+1.
$$
By (1),
$$
E_1,E_2,E_3\geq0.
$$
Now set
$$
\beta=\frac{x^2(5-3x)}2,
\qquad
\gamma=x^2(1-x).
$$
Both weights are positive for $0<x<1$. Moreover,
$$
x^2-\beta+\frac32\gamma=0,
\qquad
x^3-\beta+\frac52\gamma=0. \tag{2}
$$
Consequently, in the combination $E_1+\beta E_2+\gamma E_3$, the coefficients of $a$ and $b$ cancel. Expanding the remaining terms gives the identity
$$
E_1+\beta E_2+\gamma E_3
=\frac{x(1-x)(2-x)}2\bigl(\Phi(x)-L\bigr), \tag{3}
$$
where
$$
\Phi(x)=\frac{4\bigl(1+x^2(1-x)\bigr)}{x(1-x)(2-x)}. \tag{4}
$$
The left side of (3) is nonnegative, and the prefactor on the right is positive. Hence every stable interval satisfies
$$
L\leq\Phi(x)\qquad(0<x<1). \tag{5}
$$
Thus the minimax geometry itself gives the universal upper bound
$$
L\leq\min_{0<x<1}\Phi(x). \tag{6}
$$

We now determine this minimum. Differentiating (4),
$$
\Phi'(x)
=\frac{4D(x)}{x^2(1-x)^2(2-x)^2},
$$
where
$$
D(x)=2x^4-4x^3-x^2+6x-2. \tag{7}
$$
Also
$$
D'(x)=2(x-1)(4x^2-2x-3).
$$
The quadratic factor is negative on $(0,1)$, so $D'(x)>0$ there. Since
$$
D(0)=-2,\qquad D(1)=1,
$$
there is a unique $x_0\in(0,1)$ with
$$
D(x_0)=0. \tag{8}
$$
Because $\Phi(x)\to+\infty$ as $x\to0^+$ or $x\to1^-$, this $x_0$ is the unique global minimizer. Define
$$
r=\Phi(x_0). \tag{9}
$$
Then (5) implies that every stable interval has length at most $r$, so
$$
\rho_*\leq r. \tag{10}
$$

It remains to identify $r$ in the requested exact form. Let
$$
P(y)=y^4-8y^3+52y^2-864y-1984.
$$
A direct substitution of (4) gives
$$
P(\Phi(x))
=\frac{64D(x)^2\bigl(12x^4-36x^3+25x^2+2x+1\bigr)}
{x^4(1-x)^4(2-x)^4}. \tag{11}
$$
Hence (8) yields $P(r)=0$. To locate this root, note that
$$
P(11)=-1203,\qquad P(12)=2048,
$$
and
$$
P'(y)=4g(y),
\qquad
g(y)=y^3-6y^2+26y-216.
$$
Since
$$
g'(y)=3(y-2)^2+14>0,
$$
$g$ is strictly increasing. Thus $P$ first decreases and then increases on $(0,\infty)$. As $P(0)<0$ and $P(y)\to+\infty$, $P$ has exactly one positive root. Therefore
$$
r=\operatorname{Root}_{(11,12)}(P). \tag{12}
$$

Step 3: Equality in the dual bound forces the contact pattern and the candidate

The active contacts are now consequences of equality in the bound, rather than assumptions used to guess the extremizer. Suppose a pair $(a,b)$ is stable on $[0,r]$. In (3), take $L=r$ and $x=x_0$. By (9), the right side is zero, while
$$
E_1\geq0,\qquad \beta E_2\geq0,\qquad \gamma E_3\geq0
$$
and $\beta,\gamma>0$. Hence all three slacks vanish:
$$
R_{a,b}(x_0r)=-1,
\qquad
R_{a,b}(r)=1,
\qquad
S_{a,b}(r)=-1. \tag{13}
$$
Put
$$
t=x_0r.
$$
Since $0<t<r$ and stability gives $R_{a,b}(s)\geq-1$ throughout $[0,r]$, the first equality in (13) is an interior minimum. Therefore
$$
R_{a,b}'(t)=0. \tag{14}
$$
Thus the full contact pattern
$$
R(t)=-1,\qquad R'(t)=0,\qquad R(r)=1,\qquad S(r)=-1
$$
is forced by the minimax equality case.

The two endpoint equations in (13) already determine the coefficients. Writing
$$
A=ar^2,\qquad B=br^3,
$$
we obtain
$$
A+B=r,
\qquad
\frac32A+\frac52B=r-2.
$$
Hence
$$
A=\frac{3r+4}{2},
\qquad
B=-\frac{r+4}{2},
$$
so necessarily
$$
a_*=\frac{3r+4}{2r^2},
\qquad
b_*=-\frac{r+4}{2r^3}. \tag{15}
$$
This gives the only possible extremizing pair.

We also recover the interior contacts algebraically for this candidate without assuming feasibility. By construction,
$$
R_{a_*,b_*}(r)=1,
\qquad
S_{a_*,b_*}(r)=-1,
$$
so $E_2=E_3=0$. Since $r=\Phi(x_0)$, identity (3) then gives
$$
R_{a_*,b_*}(t)=-1. \tag{16}
$$
Furthermore, after substituting $r=\Phi(x)$ into the derivative of the candidate,
$$
R_{a_*,b_*}'(rx)
=\frac{D(x)}{2\bigl(1+x^2(1-x)\bigr)}.
$$
At $x=x_0$, (8) therefore gives
$$
R_{a_*,b_*}'(t)=0. \tag{17}
$$

Step 4: Verify feasibility on the full interval and conclude uniqueness

The derivative $R_{a_*,b_*}'$ is a downward-opening quadratic because $b_*<0$. We have
$$
R_{a_*,b_*}'(0)=-1,
\qquad
R_{a_*,b_*}'(t)=0,
$$
and
$$
R_{a_*,b_*}'(r)=\frac12-\frac2r>0
$$
because $r>11$. Hence $t$ is the smaller critical point and the other critical point lies to the right of $r$. Using
$$
R_{a_*,b_*}(0)=R_{a_*,b_*}(r)=1,
\qquad
R_{a_*,b_*}(t)=-1,
$$
we obtain
$$
|R_{a_*,b_*}(s)|\leq1
\qquad(0\leq s\leq r). \tag{18}
$$

For the companion mode,
$$
1-S_{a_*,b_*}(s)
=s\left(
1-\frac{3(3r+4)}{4r^2}s
+\frac{5(r+4)}{4r^3}s^2
\right).
$$
The discriminant of the quadratic in parentheses is
$$
\frac{r^2-104r+144}{16r^4}<0
$$
for $11<r<12$, and its leading coefficient is positive. Thus
$$
S_{a_*,b_*}(s)\leq1
\qquad(s\geq0). \tag{19}
$$
Moreover,
$$
1+S_{a_*,b_*}(s)
=\frac{(r-s)Q_r(s)}{4r^3},
$$
where
$$
Q_r(s)
=(5r+20)s^2+(-4r^2+8r)s+8r^2.
$$
Its discriminant is
$$
16r^2(r^2-14r-36)<0,
$$
so $Q_r(s)>0$ for all real $s$. Therefore
$$
S_{a_*,b_*}(s)\geq-1
\qquad(0\leq s\leq r). \tag{20}
$$
Equations (1), (18), (19), and (20) show that
$$
\rho(a_*,b_*)\geq r. \tag{21}
$$
Combined with the universal upper bound (10), this proves
$$
\rho_*=r.
$$

Finally, suppose $\rho(a,b)=r$. The set of stable interval lengths is downward closed, so the pair is stable on every $[0,L]$ with $L<r$; continuity of $R_{a,b}$ and $S_{a,b}$ then extends the inequalities to $s=r$. Thus the pair is stable on $[0,r]$, and the equality argument in Step 3 forces the endpoint contacts in (13), hence the unique coefficients (15). Therefore the maximizer is unique.

Final Answer: $\boxed{(r,\frac{3r+4}{2r^2},-\frac{r+4}{2r^3}),\ r=\operatorname{Root}_{(11,12)}(x^4-8x^3+52x^2-864x-1984)}$

## Answer

$(r,\frac{3r+4}{2r^2},-\frac{r+4}{2r^3}),\ r=\operatorname{Root}_{(11,12)}(x^4-8x^3+52x^2-864x-1984)$

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

## Solution Concepts

- power-bounded triangular amplification
- positive dual minimax certificate
- equality-case contact forcing
- competing cubic stability modes
- equality-case rigidity

## Black-Box Audit

Power boundedness is proved from an explicit formula for the matrix powers. The sharp interval bound is derived before the candidate from the positive dual identity (3); equality in that bound forces the active contact pattern, after which the coefficients are determined. The full stability interval is then checked by elementary derivative, factorization, and discriminant arguments. No numerical optimizer, root-location theorem, or external extremal-polynomial result is used.
