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
The Toeplitz matrix
$$
T=(c_{j-k})_{0\leq j,k\leq r}
$$
is therefore positive semidefinite.

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

Step 2: Compute the sharp positive-semidefinite bound
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
Since
$$
0<\rho<\frac{1}{2\cos(\pi/(r+1))},
$$
every $P_m$ with $m\leq r$ is positive definite. In particular $C=P_{r-1}$ is invertible.

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
The first cofactor is $\det P_{r-2}$. For the second, deleting the last row and first column leaves a triangular minor with determinant $\rho^{r-2}$, while its cofactor sign is $(-1)^r$.

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
Because $C$ is positive definite, $T$ is positive semidefinite exactly when $S$ is positive semidefinite. The two diagonal entries of $S$ are $d>0$, so this is equivalent to
$$
|w-\rho^2\beta|\leq d.
$$
The center and radius of this disk are real. Hence
$$
\operatorname{Re}w
\leq
\rho^2\beta+d
=
1-\frac{\rho^2\left(D_{r-2}-(-\rho)^{r-2}\right)}{D_{r-1}}.
$$
Equality in the real part occurs at the unique point
$$
w_*
=
1-\frac{\rho^2\left(D_{r-2}-(-\rho)^{r-2}\right)}{D_{r-1}}.
$$

Step 3: Realize the extremal Toeplitz matrix by a measure
Let $T_*$ be the Toeplitz matrix obtained by setting $c_r=w_*$. Its Schur complement has rank $1$, while $C$ has rank $r-1$. The rank formula for a block matrix with invertible $C$ gives
$$
\operatorname{rank}T_*=r.
$$
The leading $r\times r$ principal block is $P_r$, which is positive definite.

Factor $T_*=XX^*$ with $X$ having $r$ columns, and let $v_0,\ldots,v_r$ be the row vectors of $X$. Use the inner product that is linear in the first slot, so
$$
\langle v_j,v_k\rangle=(T_*)_{jk}=c_{j-k}.
$$
Since $P_r$ is positive definite, $v_0,\ldots,v_{r-1}$ are a basis. The vectors $v_1,\ldots,v_r$ are also a basis because their Gram matrix is the same $P_r$.

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
so $U$ preserves inner products on a basis and is unitary.

The finite-dimensional spectral theorem gives
$$
U=\sum_{\zeta}\zeta E_{\zeta},
$$
where the distinct eigenvalues $\zeta$ lie on the unit circle and the $E_{\zeta}$ are orthogonal spectral projections. Define
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
for $0\leq j\leq r$. Thus $\mu_*$ satisfies the stated moment constraints and attains the bound from Step 2.

Step 4: Determine the support size of every maximizer
Let $\mu$ be any maximizing measure. Equality in Step 2 forces
$$
c_r=w_*,
$$
so its order-$r$ Toeplitz matrix is exactly $T_*$.

Because $\operatorname{rank}T_*=r$, the kernel is one-dimensional. Let
$$
a=(a_0,\ldots,a_r)\neq0
$$
span this kernel and set
$$
p(z)=\sum_{j=0}^{r}a_jz^j.
$$
The leading coefficient $a_r$ is nonzero, because otherwise the first $r$ coordinates of $a$ would give a nonzero kernel vector for the positive-definite principal block $P_r$. Thus $p$ has degree exactly $r$.

For the maximizing measure,
$$
0
=
a^*T_*a
=
\int |p(z)|^2\,d\mu(z).
$$
Hence $\operatorname{supp}\mu$ is contained in the zero set of $p$ on the unit circle, so
$$
|\operatorname{supp}\mu|\leq r.
$$
A measure supported on $s$ points produces a moment matrix of rank at most $s$. Since $T_*$ has rank $r$,
$$
|\operatorname{supp}\mu|\geq r.
$$
Every maximizing measure therefore has exactly $r$ support points.

Step 5: Prove uniqueness of the maximizing measure
The measure $\mu_*$ from Step 3 is maximizing. By Step 4 it has $r$ distinct support points, all of which are roots of the degree-$r$ kernel polynomial $p$. Hence these support points are exactly the roots of $p$.

Any maximizing measure has support contained in this same root set and, by Step 4, uses all $r$ roots. Once the support points
$$
\zeta_1,\ldots,\zeta_r
$$
are fixed, their weights are determined by the moments $c_0,\ldots,c_{r-1}$. The equations
$$
\sum_{m=1}^{r}\lambda_m\zeta_m^j=c_j,
\qquad
0\leq j\leq r-1,
$$
have coefficient matrix
$$
(\zeta_m^j)_{0\leq j\leq r-1,\ 1\leq m\leq r}.
$$
Its Vandermonde determinant is
$$
\prod_{1\leq i<j\leq r}(\zeta_j-\zeta_i)\neq0,
$$
so the weights are unique. There is exactly one maximizing measure.

The requested ordered triple is the maximum real part, the support size of every maximizer, and the number of maximizing measures.
Final Answer: $\boxed{\left(1-\frac{\rho^2(D_{r-2}-(-\rho)^{r-2})}{D_{r-1}},r,1\right)}$

---

## Answer

$\left(1-\frac{\rho^2(D_{r-2}-(-\rho)^{r-2})}{D_{r-1}},r,1\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- trigonometric moment matrices
- schur complement
- tridiagonal determinants
- spectral theorem for unitary maps
- vandermonde uniqueness
