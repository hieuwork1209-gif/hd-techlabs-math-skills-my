## Steps

Step 1: Reformulate the volume as a Gram determinant
Let $V=[v_1\ v_2\ v_3\ v_4\ v_5]$ and let
$$
G=V^{T}V.
$$
Then $G$ is positive semidefinite, $g_{ii}=1$, and
$$
g_{i,i+1}=g_{i+1,i}=\frac12
$$
with indices modulo $5$. Moreover
$$
|\det V|^{2}=\det(V^{T}V)=\det G.
$$
Thus it is enough to maximize $\det G$ over all positive semidefinite matrices with these prescribed entries.

The feasible set is compact: every unspecified entry satisfies $|g_{ij}|\leq1$ because each $2\times2$ principal minor is nonnegative. It is also nonempty with positive determinant. Indeed, take every unspecified entry equal to $0$. For the resulting matrix $G_0$, every real vector $z=(z_1,\dots,z_5)^{T}$ satisfies
$$
z^{T}G_0z
=\sum_{i=1}^{5}z_i^{2}+\sum_{i=1}^{5}z_iz_{i+1}
=\frac12\sum_{i=1}^{5}(z_i+z_{i+1})^{2}.
$$
Equality would force $z_{i+1}=-z_i$ for all $i$; going around the odd cycle then gives $z_1=-z_1$, hence $z=0$. Thus $G_0$ is positive definite. A determinant maximizer therefore exists, and every maximizer has positive determinant, so it is positive definite.

Step 2: Use cyclic symmetry to reduce the completion to one parameter
Let $P$ be the permutation matrix for the cyclic shift $1\mapsto2\mapsto\cdots\mapsto5\mapsto1$. If $G$ is feasible and positive definite, then each
$$
P^{j}G(P^{j})^{T},\qquad j=0,1,2,3,4,
$$
is feasible and has the same determinant.

For positive definite matrices, $\log\det$ is strictly concave. To see this directly, along an affine line $A(t)=A+tH$ inside the positive definite cone, Jacobi's formula gives
$$
\frac{d}{dt}\log\det A(t)=\operatorname{tr}(A(t)^{-1}H),
$$
and hence
$$
\frac{d^{2}}{dt^{2}}\log\det A(t)
=-\operatorname{tr}\left((A(t)^{-1/2}HA(t)^{-1/2})^{2}\right)\leq0,
$$
with equality only when $H=0$.

Therefore the cyclic average
$$
\overline G=\frac15\sum_{j=0}^{4}P^{j}G(P^{j})^{T}
$$
is feasible and satisfies $\det\overline G\geq\det G$. Hence some maximizer is cyclically invariant. Its diagonal and adjacent entries are already fixed, while all five nonadjacent pairs form one cyclic orbit, so it has the form
$$
G(x)=
\begin{pmatrix}
1&\frac12&x&x&\frac12\\
\frac12&1&\frac12&x&x\\
x&\frac12&1&\frac12&x\\
x&x&\frac12&1&\frac12\\
\frac12&x&x&\frac12&1
\end{pmatrix}.
$$

Step 3: Compute the determinant and the positive-definite interval
Let $\zeta=e^{2\pi i/5}$. For $k=0,1,2,3,4$, the vector
$$
w_k=(1,\zeta^{k},\zeta^{2k},\zeta^{3k},\zeta^{4k})^{T}
$$
is an eigenvector because multiplication by the circulant matrix $G(x)$ gives
$$
G(x)w_k=
\left(1+\frac12(\zeta^{k}+\zeta^{-k})+x(\zeta^{2k}+\zeta^{-2k})\right)w_k.
$$
Using
$$
\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{4},
\qquad
\cos\frac{4\pi}{5}=-\frac{\sqrt5+1}{4},
$$
the eigenvalues are
$$
\lambda_0=2+2x,
$$
$$
\lambda_1=\lambda_4=
\frac{3+\sqrt5}{4}-\frac{\sqrt5+1}{2}x,
$$
and
$$
\lambda_2=\lambda_3=
\frac{3-\sqrt5}{4}+\frac{\sqrt5-1}{2}x.
$$
Multiplying the two distinct repeated eigenvalues gives
$$
\lambda_1\lambda_2=\frac{1+2x-4x^{2}}{4}.
$$
Consequently
$$
D(x):=\det G(x)
=\frac{(x+1)(1+2x-4x^{2})^{2}}{8}.
$$
The conditions $\lambda_0,\lambda_1,\lambda_2>0$ reduce to
$$
\frac{1-\sqrt5}{4}<x<\frac{1+\sqrt5}{4}.
$$
At either endpoint one of the repeated eigenvalues vanishes, so the determinant is $0$ there.

Step 4: Optimize the one-variable determinant
Differentiating the displayed polynomial gives
$$
D'(x)=\frac58(4x^{2}-2x-1)(4x^{2}+2x-1).
$$
The zeros of the first quadratic are exactly the two endpoints of the feasible interval. The second quadratic has roots
$$
\frac{-1-\sqrt5}{4},\qquad \frac{-1+\sqrt5}{4},
$$
and only
$$
x_*:=\frac{\sqrt5-1}{4}
$$
lies in the feasible interval. Since $D(x)>0$ in the interior and tends to $0$ at both endpoints, this unique interior critical point is the global maximum.

The relation $4x_*^{2}+2x_*-1=0$ gives
$$
1+2x_*-4x_*^{2}=4x_*.
$$
Hence
$$
D(x_*)=\frac{(x_*+1)(4x_*)^{2}}{8}
=2x_*^{2}(x_*+1)=\frac14.
$$

Step 5: Verify attainment by realizing the maximizing Gram matrix
At $x=x_*$ the three distinct eigenvalues are
$$
\frac{3+\sqrt5}{2},
\qquad
\frac{1+\sqrt5}{4},
\qquad
\frac{3-\sqrt5}{2},
$$
all positive. Thus $G(x_*)$ is positive definite. Diagonalize it as
$$
G(x_*)=Q\Lambda Q^{T}
$$
with $Q$ orthogonal and $\Lambda$ positive diagonal, and set
$$
V=\Lambda^{1/2}Q^{T}.
$$
Then $V^{T}V=G(x_*)$, so the columns of $V$ are admissible vectors in $\mathbb{R}^{5}$. Therefore the determinant bound is attained, and
$$
|\det V|=\sqrt{\det G(x_*)}=\frac12.
$$

Final Answer: $\boxed{\frac12}$

---

## Answer

$\frac12$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- gram matrices
- concavity of log determinant
- circulant matrix eigenvalues
- positive definite matrix completion
