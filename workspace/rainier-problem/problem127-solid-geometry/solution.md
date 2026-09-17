## Steps

Step 1: Reduce volume maximization to a Gram determinant
Let
$$
x=B-A,\qquad y=C-A,\qquad z=D-A,
$$
and define the oriented area vectors
$$
u=\frac{1}{2}(y\times z),\qquad
v=\frac{1}{2}(z\times x),\qquad
w=\frac{1}{2}(x\times y).
$$
The three faces through $A$ have area $1$, so
$$
\|u\|=\|v\|=\|w\|=1.
$$
The opposite face satisfies
$$
\frac{1}{2}((y-x)\times(z-x))=u+v+w,
$$
up to orientation, hence
$$
\|u+v+w\|=s.
$$

Put
$$
U=\begin{pmatrix}u&v&w\end{pmatrix},
\qquad
E=\begin{pmatrix}x&y&z\end{pmatrix}.
$$
The columns of $\operatorname{cof}(E)$ are $y\times z$, $z\times x$, and $x\times y$, so
$$
U=\frac{1}{2}\operatorname{cof}(E).
$$
Since $|\det E|=6V$, where $V$ is the tetrahedron volume,
$$
|\det U|=\frac{1}{8}|\det E|^2=\frac{9}{2}V^2.
$$
For the Gram matrix
$$
G=U^TU,
$$
this gives
$$
\det G=(\det U)^2=\frac{81}{4}V^4.
$$
Thus maximizing the volume is equivalent to maximizing $\det G$.

Step 2: Determine the unique Gram matrix of every maximizer
Write
$$
G=
\begin{pmatrix}
1&p&q\\
p&1&r\\
q&r&1
\end{pmatrix}.
$$
The condition $\|u+v+w\|=s$ gives
$$
p+q+r=\frac{s^2-3}{2}.
$$
Average $G$ over all six simultaneous permutations of rows and columns. The average is
$$
\overline G=
\begin{pmatrix}
1&c&c\\
c&1&c\\
c&c&1
\end{pmatrix},
\qquad
c=\frac{s^2-3}{6}.
$$
Because $0<s<3$, one has $-1/2<c<1$, so $\overline G$ is positive definite.

On the cone of positive definite matrices, $\log\det$ is strictly concave. Along
$$
H(t)=(1-t)H_0+tH_1,
$$
its second derivative is
$$
\frac{d^2}{dt^2}\log\det H(t)
=-\operatorname{tr}\left(
\left[H(t)^{-1/2}(H_1-H_0)H(t)^{-1/2}\right]^2
\right),
$$
which is negative unless $H_0=H_1$. Therefore, if $G$ is positive definite,
$$
\log\det\overline G
\geq\frac{1}{6}\sum_P\log\det(P^TGP)
=\log\det G.
$$
A singular feasible $G$ has determinant $0<\det\overline G$, so the same bound holds for every feasible $G$.

Equality for a positive definite $G$ forces all six permutation-conjugates $P^TGP$ to be equal. Hence
$$
p=q=r=c.
$$
Thus every volume maximizer has the same area-vector Gram matrix $\overline G$.

Step 3: Reconstruct the edge metric of every maximizer
For a maximizing tetrahedron, let
$$
d=\det U=\sqrt{\det\overline G}>0,
\qquad
H=E^TE.
$$
Since
$$
U=\frac{1}{2}\det(E)E^{-T},
$$
we have
$$
d=\frac{1}{8}(\det E)^2
$$
and
$$
\overline G=U^TU
=\frac{1}{4}(\det E)^2E^{-1}E^{-T}
=2dH^{-1}.
$$
Therefore
$$
H=2d\,\overline G^{-1}.
$$

For
$$
\overline G=(1-c)I+cJ,
$$
where $J$ is the all-ones matrix,
$$
\overline G^{-1}
=\frac{1}{1-c}I
-\frac{c}{(1-c)(1+2c)}J,
$$
and
$$
d=(1-c)\sqrt{1+2c}.
$$
Hence the diagonal entries of $H$ are all
$$
L^2=\frac{2(1+c)}{\sqrt{1+2c}}
=\frac{s^2+3}{\sqrt{3}\,s},
$$
while its off-diagonal entries are all
$$
-\frac{2c}{\sqrt{1+2c}}.
$$
It follows that
$$
AB=AC=AD=L
$$
and
$$
BC^2=BD^2=CD^2
=\frac{4s}{\sqrt{3}}.
$$
Thus the base $BCD$ is equilateral. If its side length is $M$, then
$$
M^2=\frac{4s}{\sqrt{3}}.
$$

Step 4: Prove attainment and compute the circumradius
Because $\overline G$ is positive definite, choose $U$ with
$$
U^TU=\overline G,
\qquad
\det U=d>0,
$$
and define
$$
E=\sqrt{2d}\,U^{-T}.
$$
Then
$$
\frac{1}{2}\det(E)E^{-T}=U,
$$
so the columns of $E$ form a tetrahedron whose adjacent face-area vectors are the columns of $U$. Their norms are $1$, and
$$
\|u+v+w\|^2=3+6c=s^2,
$$
so the fourth face has area $s$. This realizes $\overline G$, hence the determinant bound is attained.

Every maximizer has the same edge Gram matrix $H=2d\,\overline G^{-1}$. If $E$ and $E'$ are edge matrices of two maximizers, then $E^TE=E'^TE'$, so $E'E^{-1}$ is orthogonal. Therefore all maximizers are congruent and have the same circumradius.

Let $O$ be the center of the equilateral base $BCD$, and let $h$ be the distance from $A$ to the base plane. Since $AB=AC=AD=L$, the point $A$ lies on the line through $O$ perpendicular to the base. The base circumradius is $M/\sqrt{3}$, so
$$
h^2=L^2-\frac{M^2}{3}
=\frac{9-s^2}{3\sqrt{3}\,s}.
$$
The circumcenter of the tetrahedron also lies on this perpendicular line. If its signed distance from the base plane is $z_0$, equating its distances to $A$ and to a base vertex gives
$$
\frac{M^2}{3}+z_0^2=(h-z_0)^2.
$$
Hence the circumradius $R$ satisfies
$$
R=\frac{h^2+M^2/3}{2h}
=\frac{L^2}{2h}.
$$
Substituting the formulas for $L^2$ and $h^2$ yields
$$
R^2
=\frac{(s^2+3)^2\sqrt{3}}{4s(9-s^2)}.
$$
Since $0<s<3$, the positive square root gives the required circumradius.

Final Answer: $\boxed{\frac{3^{1/4}(s^2+3)}{2\sqrt{s(9-s^2)}}}$

---

## Answer

$\frac{3^{1/4}(s^2+3)}{2\sqrt{s(9-s^2)}}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- oriented face area vectors
- strict log-determinant concavity
- cofactor reconstruction
- edge Gram matrices
- tetrahedron circumradius
