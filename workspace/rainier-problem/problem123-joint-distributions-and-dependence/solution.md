## Steps

Step 1: Compute the two conditional order-statistic laws

Let
$$
X:=U_{(r)},
\qquad
Y:=U_{(s)},
\qquad
1\le r<s\le n.
$$
For $0<x<y<1$, placing one sample point near $x$, one near $y$, exactly $r-1$ points below $x$, exactly $s-r-1$ points between $x$ and $y$, and the remaining $n-s$ points above $y$ gives the joint density
$$
f_{X,Y}(x,y)
=\frac{n!}{(r-1)!(s-r-1)!(n-s)!}
 x^{r-1}(y-x)^{s-r-1}(1-y)^{n-s}.
\tag{1}
$$
The marginal densities are
$$
f_X(x)=\frac{n!}{(r-1)!(n-r)!}x^{r-1}(1-x)^{n-r},
$$
$$
f_Y(y)=\frac{n!}{(s-1)!(n-s)!}y^{s-1}(1-y)^{n-s}.
\tag{2}
$$
Dividing (1) by the second density in (2) and substituting $x=yb$ shows that, conditional on $Y=y$,
$$
X=yB,
\qquad
B\sim\operatorname{Beta}(r,s-r).
\tag{3}
$$
Similarly, dividing (1) by the first density in (2) and substituting $y=x+(1-x)c$ shows that, conditional on $X=x$,
$$
Y=x+(1-x)C,
\qquad
C\sim\operatorname{Beta}(s-r,n+1-s).
\tag{4}
$$
Equivalently,
$$
1-C\sim\operatorname{Beta}(n+1-s,s-r).
\tag{5}
$$

For later use, if $Z\sim\operatorname{Beta}(\alpha,\beta)$ and $k\ge0$, then
$$
E Z^k
=\frac{\int_0^1 z^{\alpha+k-1}(1-z)^{\beta-1}\,dz}
{\int_0^1 z^{\alpha-1}(1-z)^{\beta-1}\,dz}
=\frac{(\alpha)_k}{(\alpha+\beta)_k},
\tag{6}
$$
where $(a)_k=a(a+1)\cdots(a+k-1)$ and $(a)_0=1$.

Step 2: Turn the variational problem into an operator norm

Let $L^2_X$ and $L^2_Y$ denote the real $L^2$ spaces for the laws of $X$ and $Y$. Define
$$
(Tf)(y):=E[f(X)\mid Y=y].
\tag{7}
$$
Conditional Jensen gives
$$
E\bigl[(Tf)(Y)^2\bigr]
=E\bigl[(E(f(X)\mid Y))^2\bigr]
\le E\bigl[E(f(X)^2\mid Y)\bigr]
=E f(X)^2,
$$
so $T:L^2_X\to L^2_Y$ is a contraction. Its adjoint is
$$
(T^*g)(x)=E[g(Y)\mid X=x],
\tag{8}
$$
because
$$
\langle Tf,g\rangle_{L^2_Y}
=E[f(X)g(Y)]
=\langle f,T^*g\rangle_{L^2_X}.
$$

Let $L^2_{X,0}$ and $L^2_{Y,0}$ be the mean-zero subspaces. If $f\in L^2_{X,0}$, then $E(Tf)=Ef=0$, so $T$ maps $L^2_{X,0}$ into $L^2_{Y,0}$. Therefore the quantity in the problem is exactly
$$
\|T\|_{L^2_{X,0}\to L^2_{Y,0}}.
\tag{9}
$$
Indeed, for fixed centered $f$ with $\|f\|_2=1$, the supremum over centered $g$ with $\|g\|_2=1$ of $\langle Tf,g\rangle$ is $\|Tf\|_2$; then one takes the supremum over $f$.

Step 3: Derive the singular basis from the invariant polynomial flags

Equations (3) and (4) give the forward reason to look at polynomials: if $h$ is a polynomial of degree at most $k$, then both $Th$ and $T^*h$ are polynomials of degree at most $k$. Thus the nested polynomial spaces of degrees $0,1,2,\dots$ form canonical invariant flags for the two conditional-expectation operators. Since $T^*T$ is self-adjoint, the natural basis adapted simultaneously to this flag and the $L^2$ inner product is obtained by orthogonalizing the monomials.

Accordingly, for each $k\ge0$, let $p_k$ be the monic degree-$k$ polynomial orthogonal to all lower-degree polynomials in $L^2_X$, and let $q_k$ be the analogous monic polynomial in $L^2_Y$.

These families are complete. Indeed, the beta densities in (2) define finite Borel measures on $[0,1]$; continuous functions are dense in the corresponding $L^2$ spaces, and the Weierstrass approximation theorem states that polynomials are uniformly dense in $C[0,1]$. Hence the orthogonalized polynomial families span dense subspaces.

We first compute $Tp_k$. By (3), conditional on $Y=y$ we have $X=yB$. Since $p_k$ is monic,
$$
(Tp_k)(y)=E[p_k(yB)]
$$
is a degree-$k$ polynomial in $y$ whose leading coefficient, by (6), is
$$
a_k:=E B^k=\frac{(r)_k}{(s)_k}.
\tag{10}
$$
We next show that $Tp_k$ is orthogonal to every polynomial in $Y$ of degree less than $k$. Let $h$ have degree $<k$. Then
$$
\langle Tp_k,h\rangle_{L^2_Y}
=E[p_k(X)h(Y)]
=E\!\left[p_k(X)E(h(Y)\mid X)\right].
\tag{11}
$$
By (4), $Y=x+(1-x)C$ conditional on $X=x$, so $E(h(Y)\mid X=x)$ is a polynomial in $x$ of degree at most $\deg h<k$. The last expectation in (11) is therefore zero by the defining orthogonality of $p_k$. Since $q_k$ is the unique monic degree-$k$ polynomial with this orthogonality,
$$
Tp_k=a_k q_k.
\tag{12}
$$

Now apply the same argument to $T^*q_k$. From (4)-(5), conditional on $X=x$,
$$
Y=1-(1-x)D,
\qquad
D\sim\operatorname{Beta}(n+1-s,s-r).
$$
For monic $q_k$, the coefficient of $x^k$ in $E[q_k(Y)\mid X=x]$ is $E D^k$. By (6),
$$
b_k:=E D^k
=\frac{(n+1-s)_k}{(n+1-r)_k}.
\tag{13}
$$
For every polynomial $h(X)$ of degree $<k$,
$$
\langle T^*q_k,h\rangle_{L^2_X}
=\langle q_k,Th\rangle_{L^2_Y}=0,
$$
because (3) makes $Th$ a polynomial of degree $<k$ in $Y$. Thus
$$
T^*q_k=b_k p_k.
\tag{14}
$$

Step 4: Diagonalize the conditional-expectation operator

Combining (12) and (14),
$$
T^*Tp_k=\lambda_k p_k,
$$
where
$$
\lambda_k=a_kb_k
=\frac{(r)_k(n+1-s)_k}{(s)_k(n+1-r)_k}.
\tag{15}
$$
Normalize the complete orthogonal family $p_k$ to an orthonormal basis $e_k$. Then
$$
T^*T e_k=\lambda_k e_k.
$$
For $k=0$, $e_0$ is constant and $\lambda_0=1$. If $f\in L^2_{X,0}$ has expansion
$$
f=\sum_{k\ge1}c_k e_k,
$$
then
$$
\|Tf\|_2^2
=\langle T^*Tf,f\rangle
=\sum_{k\ge1}\lambda_k|c_k|^2.
\tag{16}
$$
Thus the squared operator norm in (9) is $\sup_{k\ge1}\lambda_k$.

Moreover
$$
\frac{\lambda_{k+1}}{\lambda_k}
=\frac{r+k}{s+k}
\frac{n+1-s+k}{n+1-r+k}<1
\qquad(k\ge0),
\tag{17}
$$
because $r<s$ and $n+1-s<n+1-r$. Hence the largest eigenvalue on the centered subspace is $\lambda_1$.

Step 5: Evaluate the supremum and prove attainment

By (9), (15), and (17),
$$
\rho_{r,s}^{(n)}
=\sqrt{\lambda_1}
=\sqrt{\frac{r(n+1-s)}{s(n+1-r)}}.
\tag{18}
$$
The supremum is attained: $p_1(X)=X-EX$ and $q_1(Y)=Y-EY$ are nonzero centered singular functions corresponding to $\lambda_1$, and after normalizing them in $L^2$ and choosing the common sign, equality holds in (9).

Thus no nonlinear choice of $f$ and $g$ can improve on the degree-one pair.

## Solution Concepts

- Conditional Beta laws for pairs of uniform order statistics.
- Conditional expectation as the singular-value operator governing maximal correlation.
- Orthogonal-polynomial diagonalization and monotonicity of the full singular spectrum.

Final Answer: $\displaystyle \sqrt{\frac{r(n+1-s)}{s(n+1-r)}}$.
