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

Step 2: Derive the algebraic candidate from the active contacts

We first locate a candidate by imposing the contact pattern
$$
R(t)=-1,\qquad R'(t)=0,\qquad R(L)=1,\qquad S(L)=-1,
$$
with $0<t<L$. Step 4 will give a positive certificate proving that this candidate is globally forced.

The two endpoint equations give
$$
a=\frac{3L+4}{2L^2},
\qquad
b=-\frac{L+4}{2L^3}. \tag{2}
$$
Put $x=t/L$. The two conditions at $t$ become
$$
3(L+4)x^2-2(3L+4)x+2L=0, \tag{3}
$$
and
$$
4-2Lx+(3L+4)x^2-(L+4)x^3=0. \tag{4}
$$
Eliminating $x$ from (3) and (4) gives
$$
-4(L+4)P(L)=0,
$$
where
$$
P(L)=L^4-8L^3+52L^2-864L-1984. \tag{5}
$$
Now
$$
P(11)=-1203,\qquad P(12)=2048,
$$
and
$$
P'(L)=4\bigl(L^3-6L^2+26L-216\bigr)>0
\qquad(11\leq L\leq12),
$$
because the cubic in parentheses is already positive at $11$ and has derivative
$$
3L^2-12L+26=3(L-2)^2+14>0.
$$
Hence there is a unique
$$
r=\operatorname{Root}_{(11,12)}(P).
$$
Define
$$
a_*=\frac{3r+4}{2r^2},
\qquad
b_*=-\frac{r+4}{2r^3}, \tag{6}
$$
and put
$$
d=\sqrt{3r^2+16},
\qquad
x=\frac{3r+4-d}{3(r+4)},
\qquad
t=rx.
$$
Then $0<x<1$, equation (3) holds, and therefore $R_{a_*,b_*}'(t)=0$. Also
$$
R_{a_*,b_*}(r)=1,
\qquad
S_{a_*,b_*}(r)=-1. \tag{7}
$$
Finally,
$$
R_{a_*,b_*}(t)+1
=
-\frac{(3r^2+16)^{3/2}-(18r^2+432r+928)}
{27(r+4)^2}. \tag{8}
$$
The identity
$$
(3r^2+16)^3-(18r^2+432r+928)^2
=27(r+4)^2P(r)=0
$$
and positivity of both square roots show that the numerator in (8) vanishes. Thus
$$
R_{a_*,b_*}(t)=-1. \tag{9}
$$

Step 3: Verify both stability bands on the full interval

The derivative $R_{a_*,b_*}'$ is a downward-opening quadratic. The number $t$ is its smaller root, while
$$
R_{a_*,b_*}'(r)=\frac12-\frac2r>0.
$$
Hence the other critical point lies to the right of $r$. Using
$$
R_{a_*,b_*}(0)=R_{a_*,b_*}(r)=1,
\qquad
R_{a_*,b_*}(t)=-1,
$$
we obtain
$$
|R_{a_*,b_*}(s)|\leq1
\qquad(0\leq s\leq r). \tag{10}
$$

For the companion mode,
$$
1-S_{a_*,b_*}(s)
=
s\left(
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
\qquad(s\geq0). \tag{11}
$$
Moreover,
$$
1+S_{a_*,b_*}(s)
=
\frac{(r-s)Q_r(s)}{4r^3},
$$
where
$$
Q_r(s)
=(5r+20)s^2+(-4r^2+8r)s+8r^2.
$$
The discriminant of $Q_r$ equals
$$
16r^2(r^2-14r-36)<0,
$$
so $Q_r(s)>0$ for all real $s$. Therefore
$$
S_{a_*,b_*}(s)\geq-1
\qquad(0\leq s\leq r). \tag{12}
$$
Equations (1), (10), (11), and (12) prove
$$
\rho(a_*,b_*)\geq r. \tag{13}
$$

Step 4: Prove the sharp upper bound and uniqueness by a positive certificate

Let $\widehat R,\widehat S$ be the two modes associated with any real pair $(a,b)$ that is stable on $[0,r]$. Define
$$
E_1=\widehat R(t)+1,\qquad
E_2=1-\widehat R(r),\qquad
E_3=\widehat S(r)+1.
$$
By stability, all three numbers are nonnegative. With $x=t/r$, set
$$
\beta=\frac{x^2(5-3x)}2,
\qquad
\gamma=x^2(1-x).
$$
Since $0<x<1$, both weights are positive. The exact identity
$$
E_1+\beta E_2+\gamma E_3=0 \tag{14}
$$
holds for every pair $(a,b)$. To see this, the coefficients of $a$ and $b$ on the left are respectively
$$
r^2\left(x^2-\beta+\frac32\gamma\right)=0,
\qquad
r^3\left(x^3-\beta+\frac52\gamma\right)=0.
$$
The remaining expression is independent of $(a,b)$; evaluating it at $(a_*,b_*)$, where all three contact terms vanish by (7) and (9), shows that it is zero.

Because (14) is a positive combination of nonnegative quantities, it forces
$$
E_1=E_2=E_3=0.
$$
In particular,
$$
\widehat R(r)=1,\qquad \widehat S(r)=-1.
$$
Solving these two endpoint equations gives exactly
$$
a=\frac{3r+4}{2r^2},
\qquad
b=-\frac{r+4}{2r^3}.
$$
Thus $(a_*,b_*)$ is the only pair stable through $r$.

If some pair were stable on $[0,L]$ with $L>r$, it would first have to equal $(a_*,b_*)$ on $[0,r]$. But
$$
R_{a_*,b_*}'(r)=\frac12-\frac2r>0,
$$
so $R_{a_*,b_*}(s)>1$ immediately to the right of $r$, a contradiction. Hence $\rho_*\leq r$, while (13) gives equality.

Finally, if $\rho(a,b)=r$, downward closure and continuity imply that the pair is stable at $s=r$ itself, so the same certificate forces $(a,b)=(a_*,b_*)$. The maximizer is therefore unique.

Final Answer: $\boxed{\operatorname{Root}_{(11,12)}(x^4-8x^3+52x^2-864x-1984)}$

## Answer

$\operatorname{Root}_{(11,12)}(x^4-8x^3+52x^2-864x-1984)$

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

## Solution Concepts

- power-bounded triangular amplification
- competing cubic stability modes
- active-contact elimination
- positive dual certificate
- equality-case rigidity

## Black-Box Audit

Power boundedness is proved from an explicit formula for the matrix powers. The sharp bound is certified by the displayed positive identity (14), and all interval inequalities are verified by elementary discriminant and monotonicity arguments. No numerical optimizer, root-location theorem, or external extremal-polynomial result is used.
