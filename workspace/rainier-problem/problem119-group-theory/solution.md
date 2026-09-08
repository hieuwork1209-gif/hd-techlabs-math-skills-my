## Steps

Step 1: Pass to a three-dimensional Lagrangian graph

Let
$$
U=\mathbb F_p^3,\qquad Z=Z(G)=\{(0,0,t):t\in\mathbb F_p\}.
$$
For
$$
x=(u,v,t),\qquad y=(u',v',t'),
$$
the commutator is
$$
[x,y]=(0,0,u\cdot v'-u'\cdot v).
$$
Hence
$$
G/Z\cong U\oplus U
$$
with symplectic form
$$
\omega((u,v),(u',v'))=u\cdot v'-u'\cdot v.
$$
If $A\ge Z$ is abelian of order $p^4$, then $L=A/Z$ is a three-dimensional Lagrangian subspace. The two coordinate-intersection conditions make $L$ transverse to both coordinate copies of $U$, so
$$
L=\{(u,Tu):u\in U\}
$$
for a unique invertible linear map $T:U\to U$. Isotropy of $L$ is equivalent to $T$ being symmetric. Moreover
$$
L\cap\Delta=\{(u,u):(T-I)u=0\},
$$
where $\Delta=\{(u,u):u\in U\}$. Thus the diagonal intersection has order $p^2$ exactly when
$$
\dim\ker(T-I)=1.
$$
Therefore, with
$$
S=T-I,
$$
we must count symmetric $3\times3$ matrices $S$ of rank $2$ such that $I+S$ is invertible.

Step 2: Count all symmetric rank-two matrices

A symmetric matrix $S$ of rank $2$ has a unique radical line
$$
K=\ker S\subset U.
$$
Conversely, for a fixed line $K$, such matrices are exactly the pullbacks to $U$ of nondegenerate symmetric bilinear forms on the two-dimensional quotient $U/K$.

There are
$$
p^2+p+1
$$
lines in $U$. On a two-dimensional space there are $p^3$ symmetric matrices in total. The singular ones consist of the zero matrix together with the $p^2-1$ nonzero rank-one symmetric matrices, hence there are $p^2$ singular symmetric matrices. Thus the number of invertible symmetric $2\times2$ matrices is
$$
p^3-p^2=p^2(p-1).
$$
It follows that the total number of symmetric rank-two $3\times3$ matrices is
$$
(p^2+p+1)p^2(p-1)=p^2(p^3-1).
$$

Step 3: Count the forbidden matrices for a fixed anisotropic radical line

Let
$$
q(x)=x\cdot x=x_1^2+x_2^2+x_3^2,
$$
and let $K=\langle k\rangle$ be anisotropic, so $q(k)\ne0$. Then
$$
U=K\perp K^\perp.
$$
Since $S$ is self-adjoint for the dot product and has kernel $K$, its restriction $A=S|_{K^\perp}$ is an invertible self-adjoint operator on the two-dimensional nondegenerate space $K^\perp$.

Choose an orthogonal basis of $K^\perp$ with Gram matrix
$$
J=\begin{pmatrix}r&0\\0&s\end{pmatrix},\qquad d=rs\ne0.
$$
A self-adjoint operator has matrix
$$
A=\begin{pmatrix}a&sz\\rz&e\end{pmatrix}.
$$
Put $B=I+A$. The singular self-adjoint matrices $B$ are exactly
$$
B=\begin{pmatrix}x&sz\\rz&y\end{pmatrix},\qquad xy-dz^2=0.
$$
There are $p^2$ of them: if $x\ne0$, then $y$ is forced, while if $x=0$, then $z=0$ and $y$ is arbitrary.

We need $B$ singular but $A=B-I$ invertible. The matrices for which both are singular satisfy
$$
xy=dz^2,
$$
and
$$
(x-1)(y-1)=dz^2.
$$
Subtracting gives $x+y=1$, so after
$$
X=2x-1,\qquad Z=2z,
$$
we obtain
$$
X^2+dZ^2=1.
$$
Let $\chi$ be the quadratic character, with $\chi(0)=0$. The number of solutions of this equation is
$$
p-\chi(-d).
$$
Indeed,
$$
\sum_X\bigl(1+\chi(d^{-1}(1-X^2))\bigr)
=p+\chi(d)\sum_X\chi(1-X^2)
=p-\chi(-d),
$$
using $\sum_X\chi(X^2-1)=-1$, which follows by counting factorizations $(X-Y)(X+Y)=1$.

Hence the forbidden count for this fixed anisotropic $K$ is
$$
p^2-p+\chi(-d).
$$
Because the determinant of the standard dot product is a square and
$$
U=K\perp K^\perp,
$$
we have
$$
\chi(d)=\chi(q(k)).
$$
Writing
$$
\varepsilon=\chi(-1),
$$
the forbidden count is therefore
$$
p^2-p+\varepsilon\chi(q(k)).
$$

Step 4: Count the forbidden matrices for a fixed isotropic radical line

Now let $K=\langle e\rangle$ be isotropic. Choose a Witt basis $e,f,h$ such that the Gram matrix of the dot product is
$$
J=\begin{pmatrix}0&1&0\\1&0&0\\0&0&d\end{pmatrix},\qquad d\ne0.
$$
A self-adjoint operator $S$ with $Se=0$ then has matrix
$$
S=\begin{pmatrix}
0&a&dr\\
0&0&0\\
0&r&g
\end{pmatrix}.
$$
Its rank is $2$ exactly when
$$
ag-dr^2\ne0,
$$
and
$$
\det(I+S)=1+g.
$$
Thus $I+S$ is singular exactly when $g=-1$, after which the rank condition becomes
$$
a\ne-dr^2.
$$
There are $p$ choices for $r$ and $p-1$ choices for $a$, so a fixed isotropic radical line contributes
$$
p(p-1)=p^2-p
$$
forbidden matrices.

Step 5: Count radical lines of each quadratic type

First, the number of isotropic lines for $q$ is $p+1$. To see this, note that
$$
\sum_{x,y\in\mathbb F_p}\chi(x^2+y^2)=0:
$$
for $y=0$ the contribution is $p-1$, while for each $y\ne0$ scaling by $y$ gives
$$
\sum_t\chi(t^2+1)=-1.
$$
Therefore the number of vectors satisfying
$$
x^2+y^2+z^2=0
$$
is
$$
p^2+\chi(-1)\sum_{x,y}\chi(x^2+y^2)=p^2.
$$
Removing the zero vector and dividing by $p-1$ gives $p+1$ isotropic lines.

There remain $p^2$ anisotropic lines. Let $N_+$ and $N_-$ be the numbers whose nonzero norm is respectively a square or a nonsquare. Since scalar multiplication changes the norm by a square, each anisotropic line has a well-defined sign $\chi(q(k))$.

Let
$$
M=\#\{(x,y):x^2+y^2=0\}=p+(p-1)\varepsilon.
$$
For fixed $(x,y)$,
$$
\sum_z\chi(x^2+y^2+z^2)
$$
equals $p-1$ if $x^2+y^2=0$ and $-1$ otherwise. Hence
$$
\sum_{x,y,z}\chi(q(x,y,z))
=M(p-1)-(p^2-M)=p(p-1)\varepsilon.
$$
Dividing by the $p-1$ nonzero vectors on each anisotropic line gives
$$
N_+-N_-=p\varepsilon.
$$
Together with $N_++N_-=p^2$, this yields
$$
N_+=\frac{p(p+\varepsilon)}2,\qquad
N_-=\frac{p(p-\varepsilon)}2.
$$

Step 6: Subtract the forbidden matrices

The total forbidden count is
$$
(p+1)(p^2-p)
+\frac{p(p+\varepsilon)}2(p^2-p+\varepsilon)
+\frac{p(p-\varepsilon)}2(p^2-p-\varepsilon).
$$
The anisotropic contribution simplifies to
$$
p^4-p^3+p,
$$
while the isotropic contribution is
$$
p^3-p.
$$
Hence exactly
$$
p^4
$$
rank-two symmetric matrices make $I+S$ singular.

Therefore the required number is
$$
p^2(p^3-1)-p^4
=p^2(p^3-p^2-1).
$$

Final Answer: $\boxed{p^2(p^3-p^2-1)}$

---

## Answer

$p^2(p^3-p^2-1)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- extraspecial finite group
- symplectic quotient
- Lagrangian graph
- symmetric bilinear forms
- finite quadratic geometry

---

## Black-Box Audit

No Level 2 or Level 3 black-box issues found.
