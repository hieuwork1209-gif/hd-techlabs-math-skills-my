## Steps

Step 1: Reduce power boundedness and derive a parameterized dual bound

Fix $c>0$ and $s\geq0$, and abbreviate
$$
R=R_{a,b}(s),\qquad S=S^{(c)}_{a,b}(s).
$$
A direct induction gives
$$
\left(M^{(c)}_{a,b}(s)\right)^m
=
\begin{pmatrix}
R^m&s(R^m-S^m)\\
0&S^m
\end{pmatrix}
\qquad(m\geq1).
$$
Hence the orbit is bounded for every initial vector exactly when
$$
|R_{a,b}(s)|\leq1,
\qquad
|S^{(c)}_{a,b}(s)|\leq1. \tag{1}
$$

Assume $(a,b)$ is stable on $[0,L]$, and fix $x\in(0,1)$. Set
$$
E_1=R_{a,b}(xL)+1,
\qquad
E_2=1-R_{a,b}(L),
\qquad
E_3=S^{(c)}_{a,b}(L)+1.
$$
By (1), all three are nonnegative. Since
$$
S^{(c)}_{a,b}(s)=1-s+(1+2c)as^2+(1+6c)bs^3,
$$
define
$$
\gamma_c=\frac{x^2(1-x)}{4c},
\qquad
\beta_c=x^2+(1+2c)\gamma_c.
$$
Both weights are positive, and
$$
x^2-\beta_c+(1+2c)\gamma_c=0,
\qquad
x^3-\beta_c+(1+6c)\gamma_c=0. \tag{2}
$$
Thus the $a$- and $b$-terms cancel in $E_1+\beta_cE_2+\gamma_cE_3$. Expanding the remaining terms gives
$$
E_1+\beta_cE_2+\gamma_cE_3
=
\frac{x(1-x)(2-x)}2\bigl(\Phi_c(x)-L\bigr), \tag{3}
$$
where
$$
\Phi_c(x)=
\frac{4c+x^2(1-x)}{c\,x(1-x)(2-x)}. \tag{4}
$$
The left side of (3) is nonnegative and the prefactor is positive, so every stable interval satisfies
$$
L\leq\Phi_c(x)\qquad(0<x<1).
$$
Therefore
$$
\rho_*(c)\leq m(c):=\min_{0<x<1}\Phi_c(x). \tag{5}
$$

Step 2: Prove that the dual bound is locally sharp at $c=1/4$

Put $c_0=1/4$. Then
$$
\Phi_{c_0}(x)=\frac{4\bigl(1+x^2(1-x)\bigr)}{x(1-x)(2-x)},
$$
and
$$
\Phi_{c_0}'(x)
=
\frac{4D(x)}{x^2(1-x)^2(2-x)^2},
\qquad
D(x)=2x^4-4x^3-x^2+6x-2. \tag{6}
$$
Moreover,
$$
D'(x)=2(x-1)(4x^2-2x-3)>0
\qquad(0<x<1),
$$
because both factors are negative there. Since $D(0)=-2$ and $D(1)=1$, there is a unique minimizer $x_0\in(0,1)$. In fact,
$$
D\left(\frac38\right)=-\frac{127}{2048}<0,
\qquad
D\left(\frac25\right)=\frac{22}{625}>0,
$$
so
$$
\frac38<x_0<\frac25. \tag{7}
$$
Let
$$
r_0=\Phi_{c_0}(x_0).
$$
For
$$
P(y)=y^4-8y^3+52y^2-864y-1984,
$$
direct substitution gives
$$
P(\Phi_{c_0}(x))
=
\frac{64D(x)^2(12x^4-36x^3+25x^2+2x+1)}
{x^4(1-x)^4(2-x)^4}. \tag{8}
$$
Hence $P(r_0)=0$. Also $P(11)=-1203$ and $P(12)=2048$. Writing
$$
P'(y)=4g(y),
\qquad
g(y)=y^3-6y^2+26y-216,
$$
we have
$$
g'(y)=3(y-2)^2+14>0.
$$
Thus $P$ decreases once and then increases, so it has exactly one positive root. Consequently
$$
11<r_0<12. \tag{9}
$$

Now let $c\downarrow c_0$ and choose a minimizer $x_c$ of $\Phi_c$. Because $\Phi_c(x)\to+\infty$ at both endpoints, such a minimizer exists. Also $x_c\to x_0$: otherwise a sequence $c_n\to c_0$ would have minimizers staying away from $x_0$; after passing to a convergent subsequence, continuity of $\Phi_c$ would produce a second minimizer of $\Phi_{c_0}$, contradicting uniqueness. Hence
$$
r_c:=m(c)=\Phi_c(x_c)\to r_0. \tag{10}
$$

Define
$$
a_c=\frac{3r_c+c^{-1}}{2r_c^2},
\qquad
b_c=-\frac{r_c+c^{-1}}{2r_c^3}. \tag{11}
$$
Then
$$
R_{a_c,b_c}(r_c)=1,
\qquad
S^{(c)}_{a_c,b_c}(r_c)=-1. \tag{12}
$$
Indeed, with $A=a_cr_c^2$ and $B=b_cr_c^3$,
$$
A+B=r_c,
\qquad
(1+2c)A+(1+6c)B=r_c-2.
$$
Taking $L=r_c$ and $x=x_c$ in (3), the last two slacks vanish by (12), while $r_c=\Phi_c(x_c)$, so
$$
R_{a_c,b_c}(x_cr_c)=-1. \tag{13}
$$
Since $x_c$ is an interior minimizer of $\Phi_c$, differentiating (4) in $x$ gives zero there. A direct substitution of (11) shows that the same numerator occurs in
$$
R'_{a_c,b_c}(x_cr_c),
$$
so
$$
R'_{a_c,b_c}(x_cr_c)=0. \tag{14}
$$

It remains to check that these contacts really give stability for $c$ close to $c_0$. Put $y=s/r_c$. From (11),
$$
R_{a_c,b_c}(r_cy)-1
=-\frac{y(y-1)}{2c}\bigl((cr_c+1)y-2cr_c\bigr). \tag{15}
$$
At $c=c_0$, (9) gives $c_0r_0>1$, so by (10) the factor in parentheses is negative on $0\leq y\leq1$ for all $c$ sufficiently close to $c_0$. Hence $R\leq1$.

The derivative of $R_{a_c,b_c}(r_cy)$ is a downward-opening quadratic. One root is $x_c$ by (14), and the other root $z_c$ satisfies
$$
x_cz_c=\frac{2r_c}{3(r_c+c^{-1})}. \tag{16}
$$
At $c=c_0$, using (7) and (9),
$$
z_0>
\frac{2r_0}{3(r_0+4)(2/5)}
=
\frac{5r_0}{3(r_0+4)}>1.
$$
Thus $z_c>1$ for $c$ sufficiently close to $c_0$. Since $R(0)=1$, (13), and the derivative changes from negative to positive at $x_c$, we obtain
$$
-1\leq R_{a_c,b_c}(s)\leq1
\qquad(0\leq s\leq r_c). \tag{17}
$$

For the companion mode, direct factorization gives
$$
1-S^{(c)}_{a_c,b_c}(r_cy)=\frac{yQ_{c,r_c}(y)}{2c},
\qquad
1+S^{(c)}_{a_c,b_c}(r_cy)=\frac{(1-y)H_{c,r_c}(y)}{2c}, \tag{18}
$$
where
$$
Q_{c,r}(y)
=(6c^2r+cr+6c+1)y^2
-(6c^2r+3cr+2c+1)y
+2cr,
$$
and
$$
H_{c,r}(y)
=(6c^2r+cr+6c+1)y^2
+(-2cr+4c)y
+4c.
$$
At $c=c_0$, their discriminants are
$$
\Delta_Q=\frac{r_0^2-104r_0+144}{64}<0,
\qquad
\Delta_H=\frac{r_0^2-14r_0-36}{4}<0
$$
by (9), while both leading coefficients are positive. By (10) and continuity, the discriminants remain negative for $c$ sufficiently close to $c_0$. Hence both quadratics in (18) stay positive, so
$$
-1\leq S^{(c)}_{a_c,b_c}(s)\leq1
\qquad(0\leq s\leq r_c). \tag{19}
$$
Equations (1), (17), and (19) show that the candidate is stable on $[0,r_c]$. Together with (5), this proves that for all $c>c_0$ sufficiently close to $c_0$,
$$
\rho_*(c)=m(c)=\min_{0<x<1}\Phi_c(x). \tag{20}
$$

Step 3: Compute the right derivative without invoking an envelope theorem

Let $h>0$ be small, put $c_h=c_0+h$, and let $x_h$ minimize $\Phi_{c_h}$. By Step 2, $x_h\to x_0$ and
$$
\rho_*(c_h)=\Phi_{c_h}(x_h),
\qquad
\rho_*(c_0)=\Phi_{c_0}(x_0).
$$
Since $x_0$ minimizes $\Phi_{c_0}$ and $x_h$ minimizes $\Phi_{c_h}$,
$$
\Phi_{c_h}(x_h)-\Phi_{c_0}(x_h)
\leq
\rho_*(c_h)-\rho_*(c_0)
\leq
\Phi_{c_h}(x_0)-\Phi_{c_0}(x_0). \tag{21}
$$
Divide by $h$. From (4),
$$
\frac{\partial\Phi_c}{\partial c}(x)
=-\frac{x}{c^2(2-x)}. \tag{22}
$$
The two outer difference quotients in (21) therefore converge, using $x_h\to x_0$, to the same value
$$
-\frac{x_0}{c_0^2(2-x_0)}
=-\frac{16x_0}{2-x_0}. \tag{23}
$$
Hence the requested right-hand limit exists and
$$
\kappa_*=-\frac{16x_0}{2-x_0}. \tag{24}
$$

Step 4: Eliminate the hidden contact point

Set
$$
k=-\frac{16x_0}{2-x_0}.
$$
Then
$$
x_0=\frac{2k}{k-16}.
$$
Substituting this into $D(x_0)=0$ from (6) gives
$$
D\left(\frac{2k}{k-16}\right)
=
\frac{2\bigl(3k^4+96k^3+2560k^2-8192k-65536\bigr)}{(k-16)^4}=0. \tag{25}
$$
By (7), $3/8<x_0<2/5$. The map $x\mapsto-16x/(2-x)$ is strictly decreasing, so
$$
-4<k<-\frac{48}{13}<-3. \tag{26}
$$
Conversely, any root of the quartic in $(-4,-3)$ maps through $x=2k/(k-16)$ to a root of $D$ in $(0,1)$. Since Step 2 proved that $D$ has only one root in $(0,1)$, the quartic has exactly one root in $(-4,-3)$. Combining this with (24) yields the required exact sensitivity.

Final Answer: $\boxed{\operatorname{Root}_{(-4,-3)}(3x^4+96x^3+2560x^2-8192x-65536)}$

## Answer

$\operatorname{Root}_{(-4,-3)}(3x^4+96x^3+2560x^2-8192x-65536)$

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

## Solution Concepts

- power-bounded triangular families
- parameterized stability minimax
- positive dual certificate
- optimal-value sensitivity
- algebraic elimination

## Black-Box Audit

Power boundedness is derived from an explicit matrix-power formula. The parameterized upper bound comes from a positive dual identity with displayed weights. Local sharpness is proved by an explicit candidate, factorization, critical-point geometry, and discriminant signs. The derivative of the optimal value is obtained from the two elementary minimizer inequalities in (21), not from an envelope theorem. The final algebraic value follows by direct substitution and root localization; no numerical optimizer or external extremal theorem is used.