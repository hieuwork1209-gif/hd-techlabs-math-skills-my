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
A singular feasible $G$ has determinant $0<\det\overline G$, so the same determinant bound holds for every feasible $G$.

Moreover, equality for a positive definite $G$ forces all six permutation-conjugates $P^TGP$ to be equal. Hence
$$
p=q=r=c.
$$
Thus every volume-maximizing tetrahedron has the same area-vector Gram matrix $\overline G$.

Step 3: Recover the edge lengths from the maximizing area-vector Gram matrix
For a maximizing tetrahedron, let
$$
d=\det U=\sqrt{\det\overline G}>0
$$
and let
$$
H=E^TE
$$
be the Gram matrix of the three edge vectors from $A$. Since
$$
U=\frac{1}{2}\det(E)E^{-T},
$$
we have
$$
d=\frac{1}{8}(\det E)^2
$$
and therefore
$$
G=U^TU
=\frac{1}{4}(\det E)^2E^{-1}E^{-T}
=2dH^{-1}.
$$
Hence
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
Thus every diagonal entry of $H$ equals
$$
\frac{2(1+c)}{\sqrt{1+2c}},
$$
while every off-diagonal entry equals
$$
-\frac{2c}{\sqrt{1+2c}}.
$$
Therefore
$$
AB^2=AC^2=AD^2
=\frac{2(1+c)}{\sqrt{1+2c}}
=\frac{s^2+3}{\sqrt3\,s}.
$$
Also
$$
BC^2=BD^2=CD^2
=\frac{4(1+2c)}{\sqrt{1+2c}}
=\frac{4s}{\sqrt3}.
$$

Step 4: Prove attainment and uniqueness up to congruence
Because $\overline G$ is positive definite, choose a matrix $U$ with
$$
U^TU=\overline G,
\qquad
\det U=d>0.
$$
Define
$$
E=\sqrt{2d}\,U^{-T}.
$$
Then
$$
\det E=2\sqrt{2d},
\qquad
E^{-T}=\frac{1}{\sqrt{2d}}U,
$$
so
$$
\frac{1}{2}\det(E)E^{-T}=U.
$$
Hence the columns of $E$ are edge vectors of a tetrahedron whose three adjacent face-area vectors are the columns of $U$. Their norms are $1$, and
$$
\|u+v+w\|^2=3+6c=s^2,
$$
so the fourth face has area $s$. This tetrahedron realizes $\overline G$, and therefore attains the determinant bound from Step 2.

Every maximizer has the same edge Gram matrix $H=2d\,\overline G^{-1}$. If $E$ and $E'$ are edge matrices of two maximizers, then
$$
E^TE=E'^TE'=H.
$$
Thus $Q=E'E^{-1}$ satisfies $Q^TQ=I$, so the two tetrahedra differ only by an orthogonal transformation and translation. Hence all maximizers are congruent, with the two common edge lengths found in Step 3.

Final Answer: $\boxed{\left(\sqrt{\frac{s^2+3}{\sqrt3\,s}},2\sqrt{\frac{s}{\sqrt3}}\right)}$

---

## Answer

$\left(\sqrt{\frac{s^2+3}{\sqrt3\,s}},2\sqrt{\frac{s}{\sqrt3}}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- oriented face area vectors
- Gram matrices
- strict log-determinant concavity
- cofactor reconstruction
- congruence from edge Gram matrices
