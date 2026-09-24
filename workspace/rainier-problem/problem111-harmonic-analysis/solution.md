## Steps

Step 1: Encode the moment constraints by a Toeplitz matrix
Let
$$
c_j=\int_{|z|=1} z^j\,d\mu(z),
\qquad
c_{-j}=\overline{c_j},
\qquad
c_0=1.
$$
For any coefficients $a_0,\ldots,a_r$,
$$
\sum_{j,k=0}^{r} a_j\overline{a_k}c_{j-k}
=
\int_{|z|=1}
\left|
\sum_{j=0}^{r}a_jz^j
\right|^2
d\mu(z)
\geq0.
$$
Therefore
$$
T=(c_{j-k})_{0\leq j,k\leq r}
$$
is positive semidefinite.

The constraints give
$$
c_1=\rho,
\qquad
c_2=\cdots=c_{r-1}=0.
$$
Write $w=c_r$. If the endpoint indices $0,r$ are placed first and the interior indices $1,\ldots,r-1$ last, then
$$
T=
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix},
$$
where
$$
A=
\begin{pmatrix}
1&\overline w\\
w&1
\end{pmatrix},
$$
the matrix $C$ is the $(r-1)\times(r-1)$ tridiagonal matrix with diagonal entries $1$ and adjacent off-diagonal entries $\rho$, and
$$
B=
\begin{pmatrix}
\rho&0&\cdots&0\\
0&\cdots&0&\rho
\end{pmatrix}.
$$

Step 2: Compute the sharp moment bound
Let $P_m$ be the $m\times m$ tridiagonal matrix with diagonal $1$ and adjacent off-diagonal entries $\rho$. Expanding its determinant along the last row gives
$$
\det P_m=D_m,
$$
where
$$
D_0=D_1=1,
\qquad
D_m=D_{m-1}-\rho^2D_{m-2}.
$$

For $1\leq k\leq m$, the vector with $j$th coordinate
$$
\sin\frac{jk\pi}{m+1}
$$
is an eigenvector of $P_m$ with eigenvalue
$$
1+2\rho\cos\frac{k\pi}{m+1}.
$$
The hypothesis on $\rho$ makes every $P_m$ with $m\leq r$ positive definite. In particular $C=P_{r-1}$ is invertible.

Set
$$
\alpha=(C^{-1})_{11},
\qquad
\beta=(C^{-1})_{1,r-1}.
$$
Cofactor formulas give
$$
\alpha=\frac{D_{r-2}}{D_{r-1}},
\qquad
\beta=\frac{(-\rho)^{r-2}}{D_{r-1}}.
$$
The first cofactor is $\det P_{r-2}$. For the second, deleting the last row and first column leaves a triangular minor with determinant $\rho^{r-2}$, and its cofactor sign is $(-1)^r$.

The Schur complement of $C$ in $T$ is
$$
S
=
A-BC^{-1}B^*
=
\begin{pmatrix}
d&\overline w-\rho^2\beta\\
w-\rho^2\beta&d
\end{pmatrix},
$$
where
$$
d
=
1-\rho^2\alpha
=
\frac{D_r}{D_{r-1}}
>0.
$$
Because $C$ is positive definite, $T\geq0$ exactly when $S\geq0$, which is equivalent to
$$
|w-\rho^2\beta|\leq d.
$$
The disk has real center and radius, so
$$
\operatorname{Re}w
\leq
\rho^2\beta+d
=
\frac{D_r+(-1)^r\rho^r}{D_{r-1}}.
$$
Equality occurs at the unique real point
$$
w_*
=
\frac{D_r+(-1)^r\rho^r}{D_{r-1}}.
$$

Step 3: Realize the extremal Toeplitz matrix by a measure
Let $T_*$ be the Toeplitz matrix obtained by setting $c_r=w_*$. At equality,
$$
w_*-\rho^2\beta=d,
$$
so the Schur complement is
$$
S_*
=
d
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
$$
It has rank $1$. Since $C$ has rank $r-1$, the block rank formula gives
$$
\operatorname{rank}T_*=r.
$$
The leading $r\times r$ principal block is $P_r$, which is positive definite.

Factor $T_*=XX^*$ with $X$ having $r$ columns, and let $v_0,\ldots,v_r$ be the row vectors of $X$. Use the inner product linear in the first slot, so
$$
\langle v_j,v_k\rangle=(T_*)_{jk}=c_{j-k}.
$$
Since $P_r$ is positive definite, $v_0,\ldots,v_{r-1}$ form a basis. The vectors $v_1,\ldots,v_r$ also form a basis because their Gram matrix is the same $P_r$.

Define
$$
Uv_j=v_{j+1},
\qquad
0\leq j\leq r-1.
$$
Toeplitz structure gives
$$
\langle v_{j+1},v_{k+1}\rangle
=
\langle v_j,v_k\rangle,
$$
so $U$ is unitary. By the finite-dimensional spectral theorem,
$$
U=\sum_{\zeta}\zeta E_{\zeta},
$$
where the eigenvalues $\zeta$ lie on the unit circle and the $E_{\zeta}$ are the orthogonal spectral projections. Define
$$
\mu_*(\{\zeta\})
=
\|E_{\zeta}v_0\|^2.
$$
These weights are nonnegative and sum to $\|v_0\|^2=1$. Since $v_j=U^jv_0$,
$$
\int z^j\,d\mu_*(z)
=
\langle U^jv_0,v_0\rangle
=
c_j
$$
for $0\leq j\leq r$. The measure $\mu_*$ is admissible and attains the bound from Step 2.

Step 4: Determine the support size of every maximizer
Let $\mu$ be any maximizing measure. Equality in Step 2 forces
$$
c_r=w_*,
$$
so its order-$r$ moment matrix is exactly $T_*$.

Because $\operatorname{rank}T_*=r$, its kernel is one-dimensional. Let
$$
a=(a_0,\ldots,a_r)\neq0
$$
span the kernel and set
$$
p(z)=\sum_{j=0}^{r}a_jz^j.
$$
The coefficient $a_r$ is nonzero, because otherwise the first $r$ coordinates of $a$ would give a nonzero kernel vector for the positive-definite block $P_r$. Therefore $\deg p=r$.

For every maximizing measure,
$$
0
=
a^*T_*a
=
\int |p(z)|^2\,d\mu(z).
$$
Its support is therefore contained in the zero set of $p$ on the unit circle, so it has at most $r$ points. Conversely a measure supported on $s$ points gives a moment matrix of rank at most $s$. Since $T_*$ has rank $r$, every maximizing measure has at least $r$ support points. Every maximizer has exactly $r$ support points, and those points are precisely the $r$ roots of $p$.

Step 5: Recover the unweighted sum of the support points
Use the endpoint-first block ordering from Step 1. Since $S_*$ has kernel spanned by $(1,-1)$, the unique kernel vector of $T_*$ may be scaled so that
$$
a_0=1,
\qquad
a_r=-1.
$$
The Toeplitz matrix $T_*$ is invariant under reversing the coordinate order. Its one-dimensional kernel is therefore invariant under reversal. Because reversal swaps the endpoint values $1$ and $-1$, it sends $a$ to $-a$. Therefore
$$
a_{r-j}=-a_j
\qquad
(0\leq j\leq r).
$$

The row indexed by $0$ in $T_*a=0$ is
$$
a_0+\rho a_1+w_*a_r=0.
$$
With $a_0=1$ and $a_r=-1$,
$$
a_1=\frac{w_*-1}{\rho}.
$$
The monic polynomial $-p(z)$ has leading coefficient $1$ and coefficient of $z^{r-1}$ equal to
$$
-a_{r-1}=a_1.
$$
By Vieta's formula, the sum of its $r$ roots, which are the support points of every maximizing measure, is
$$
-a_1
=
\frac{1-w_*}{\rho}
=
\frac{\rho\left(D_{r-2}-(-\rho)^{r-2}\right)}{D_{r-1}}.
$$

The requested ordered triple is the maximum real part, the support size of every maximizer, and the unweighted sum of its support points.
Final Answer: $\boxed{\left(\frac{D_r+(-1)^r\rho^r}{D_{r-1}},r,\frac{\rho(D_{r-2}-(-\rho)^{r-2})}{D_{r-1}}\right)}$

---

## Answer

$\left(\frac{D_r+(-1)^r\rho^r}{D_{r-1}},r,\frac{\rho(D_{r-2}-(-\rho)^{r-2})}{D_{r-1}}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- trigonometric moment matrices
- schur complement
- unitary moment representation
- kernel polynomial
- support reconstruction
