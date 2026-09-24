## Steps

Step 1: Encode the moment constraints by a Toeplitz matrix
Let
$$
c_j=int_{|z|=1} z^j,dmu(z),
qquad
c_{-j}=overline{c_j},
qquad
c_0=1.
$$
For any coefficients $a_0,ldots,a_r$,
$$
sum_{j,k=0}^{r} a_joverline{a_k}c_{j-k}
=
int_{|z|=1}
left|
sum_{j=0}^{r}a_jz^j
ight|^2
dmu(z)
geq0.
$$
Thus the Toeplitz matrix
$$
T=
(c_{j-k})_{0leq j,kleq r}
$$
is positive semidefinite.

The constraints give
$$
c_1=ho,
qquad
c_2=cdots=c_{r-1}=0.
$$
Write $w=c_r$. If the endpoint indices $0,r$ are placed first and the interior indices $1,ldots,r-1$ last, then
$$
T=
egin{pmatrix}
A&B\\
B^*&C
end{pmatrix},
$$
where
$$
A=
egin{pmatrix}
1&overline w\\
w&1
end{pmatrix},
$$
the matrix $C$ is the $(r-1)	imes(r-1)$ tridiagonal matrix with diagonal entries $1$ and adjacent off-diagonal entries $ho$, and
$$
B=
egin{pmatrix}
ho&0&cdots&0\\
0&cdots&0&ho
end{pmatrix}.
$$

Step 2: Compute the sharp positive-semidefinite bound
Let $P_m$ be the $m	imes m$ tridiagonal matrix with diagonal $1$ and adjacent off-diagonal entries $ho$. Expanding its determinant along the last row gives
$$
det P_m=D_m,
$$
where
$$
D_0=D_1=1,
qquad
D_m=D_{m-1}-ho^2D_{m-2}.
$$

The eigenvectors of $P_m$ have coordinates
$$
sinrac{jkpi}{m+1},
qquad
1leq jleq m,
$$
and the corresponding eigenvalues are
$$
1+2hocosrac{kpi}{m+1}.
$$
Since
$$
0<ho<rac{1}{2cos(pi/(r+1))},
$$
every $P_m$ with $mleq r$ is positive definite. In particular $C=P_{r-1}$ is invertible.

Set
$$
alpha=(C^{-1})_{11},
qquad
eta=(C^{-1})_{1,r-1}.
$$
Cofactor formulas give
$$
alpha=rac{D_{r-2}}{D_{r-1}},
qquad
eta=rac{(-ho)^{r-2}}{D_{r-1}}.
$$
Indeed, the first cofactor is $det P_{r-2}$, while deleting the last row and first column leaves a triangular minor whose determinant is $ho^{r-2}$ with cofactor sign $(-1)^r$.

The Schur complement of $C$ in $T$ is
$$
S
=
A-BC^{-1}B^*
=
egin{pmatrix}
d&overline w-ho^2eta\\
w-ho^2eta&d
end{pmatrix},
$$
where
$$
d
=
1-ho^2alpha
=
rac{D_r}{D_{r-1}}
>0.
$$
Thus $Tgeq0$ if and only if
$$
|w-ho^2eta|leq d.
$$
The center and radius of this disk are real, so
$$
operatorname{Re}w
leq
ho^2eta+d
=
1-rac{ho^2left(D_{r-2}-(-ho)^{r-2}ight)}{D_{r-1}}.
$$
Equality in the real part occurs at the unique boundary point
$$
w_*
=
1-rac{ho^2left(D_{r-2}-(-ho)^{r-2}ight)}{D_{r-1}}.
$$

Step 3: Show that the extremal Toeplitz matrix is realized by a measure
Let $T_*$ be the Toeplitz matrix obtained by setting $c_r=w_*$. Its Schur complement $S$ has rank $1$, while $C$ has rank $r-1$. Hence
$$
operatorname{rank}T_*=r.
$$
Also the leading $r	imes r$ principal block is $P_r$, which is positive definite.

Choose vectors $v_0,ldots,v_r$ in an $r$-dimensional inner-product space with Gram matrix $T_*$. Since $P_r$ is positive definite, $v_0,ldots,v_{r-1}$ are a basis. The vectors $v_1,ldots,v_r$ are also a basis because their Gram matrix is the same $P_r$.

Define
$$
Uv_j=v_{j+1},
qquad
0leq jleq r-1.
$$
Toeplitz structure gives
$$
langle v_{j+1},v_{k+1}angle
=
langle v_j,v_kangle,
$$
so $U$ preserves inner products on a basis and is unitary.

By the finite-dimensional spectral theorem,
$$
U=sum_{zeta} zeta E_{zeta},
$$
where the distinct eigenvalues $zeta$ lie on the unit circle and the $E_{zeta}$ are orthogonal spectral projections. Define
$$
mu_*({zeta})
=
|E_{zeta}v_0|^2.
$$
These weights are nonnegative and sum to $|v_0|^2=1$. Since $v_j=U^jv_0$,
$$
int z^j,dmu_*(z)
=
langle U^jv_0,v_0angle
=
c_j
$$
for $0leq jleq r$. Therefore $mu_*$ satisfies the stated moment constraints and attains the bound from Step 2.

Step 4: Determine the support size of every maximizer
Let $mu$ be any maximizing measure. Equality in Step 2 forces
$$
c_r=w_*,
$$
so its order-$r$ Toeplitz matrix is exactly $T_*$.

Because $operatorname{rank}T_*=r$, the kernel is one-dimensional. Let
$$
a=(a_0,ldots,a_r)
eq0
$$
span this kernel and set
$$
p(z)=sum_{j=0}^{r}a_jz^j.
$$
The leading coefficient $a_r$ is nonzero, because otherwise the first $r$ coordinates of $a$ would give a nonzero kernel vector for the positive-definite principal block $P_r$. Thus $p$ has degree exactly $r$.

For the maximizing measure,
$$
0
=
a^*T_*a
=
int |p(z)|^2,dmu(z).
$$
Hence $operatorname{supp}mu$ is contained in the zero set of $p$ on the unit circle, so
$$
|operatorname{supp}mu|leq r.
$$
On the other hand, a measure supported on $s$ points produces a moment matrix of rank at most $s$. Since $T_*$ has rank $r$,
$$
|operatorname{supp}mu|geq r.
$$
Therefore every maximizing measure has exactly $r$ support points.

Step 5: Prove uniqueness of the maximizing measure
The construction in Step 3 gives one maximizing measure, so the kernel polynomial $p$ has at least $r$ distinct roots on the unit circle. Since $deg p=r$, these are all of its roots.

Any maximizing measure has support contained in this same root set and, by Step 4, uses all $r$ roots. Once the support points
$$
zeta_1,ldots,zeta_r
$$
are fixed, their weights are uniquely determined by the moments $c_0,ldots,c_{r-1}$: the equations
$$
sum_{m=1}^{r}lambda_mzeta_m^j=c_j,
qquad
0leq jleq r-1,
$$
have Vandermonde coefficient matrix
$$
(zeta_m^j)_{0leq jleq r-1, 1leq mleq r},
$$
whose determinant is nonzero because the $zeta_m$ are distinct. Hence there is exactly one maximizing measure.

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
