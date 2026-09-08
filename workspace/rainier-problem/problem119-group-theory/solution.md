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
If $u\ne0$, choose $v'$ with $u\cdot v'\ne0$; if $v\ne0$, choose $u'$ with $u'\cdot v\ne0$. So only elements with $u=v=0$ commute with every element, and the displayed $Z$ is the full center. The commutator calculation gives
$$
G/Z\cong U\oplus U
$$
with symplectic form
$$
\omega((u,v),(u',v'))=u\cdot v'-u'\cdot v.
$$
If $A\ge Z$ is abelian of order $p^4$, then $L=A/Z$ is a three-dimensional Lagrangian subspace. The two coordinate-intersection conditions make $L$ transverse to both coordinate copies of $U$. The condition $L\cap(0\oplus U)=0$ makes projection onto the first copy of $U$ an isomorphism, so
$$
L=\{(u,Tu):u\in U\}
$$
for a unique linear map $T:U\to U$. The condition $L\cap(U\oplus0)=0$ gives $\ker T=0$, so $T$ is invertible. For $u,u'\in U$,
$$
\omega((u,Tu),(u',Tu'))=u\cdot Tu'-u'\cdot Tu,
$$
so isotropy of $L$ is equivalent to $T$ being symmetric. Also,
$$
L\cap\Delta=\{(u,u):(T-I)u=0\},
$$
where $\Delta=\{(u,u):u\in U\}$. The corresponding diagonal subgroup of $G$ contains $Z$ and maps onto $\Delta$, so its intersection with $A$ has order $p$ times the size of $L\cap\Delta$. Therefore the required order $p^2$ is equivalent to
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
lines in $U$. To count singular symmetric $2\times2$ matrices, write
$$
C=\begin{pmatrix}a&b\\b&c\end{pmatrix}.
$$
For a nonzero singular $C$, the equation $ac=b^2$ gives $p(p-1)$ choices when $a\ne0$: choose $a$ and $b$, then $c=b^2/a$ is forced. When $a=0$, we must have $b=0$ and $c\ne0$, giving $p-1$ more choices. So there are
$$
p^2-1
$$
nonzero rank-one symmetric matrices. Including the zero matrix, there are $p^2$ singular symmetric matrices out of the $p^3$ symmetric matrices in total. The number of invertible symmetric $2\times2$ matrices is therefore
$$
p^3-p^2=p^2(p-1).
$$
The total number of symmetric rank-two $3\times3$ matrices is
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
U=K\perp K^{\perp}.
$$
Since $S$ is self-adjoint for the dot product and has kernel $K$, $K^{\perp}$ is $S$-invariant: for $x\in K^{\perp}$ and $k\in K$, one has $Sx\cdot k=x\cdot Sk=0$. Because $K$ is anisotropic, $U=K\perp K^{\perp}$ and $K\cap K^{\perp}=0$, so the restriction $A=S|_{K^{\perp}}$ is invertible and self-adjoint on the two-dimensional nondegenerate space $K^{\perp}$.

Choose an orthogonal basis of $K^{\perp}$ with Gram matrix
$$
J=\begin{pmatrix}r&0\\0&s\end{pmatrix},\qquad d=rs\ne0.
$$
Writing the self-adjointness condition as $JA=A^TJ$ gives
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
=p-\chi(-d).
$$
For the remaining sum, the equation $Y^2=X^2-1$ is equivalent to $(X-Y)(X+Y)=1$, so it has $p-1$ pairs $(X,Y)$. It also has $p+\sum_X\chi(X^2-1)$ pairs, and therefore $\sum_X\chi(X^2-1)=-1$. Since $\chi(1-X^2)=\chi(-1)\chi(X^2-1)$, this gives $\sum_X\chi(1-X^2)=-\chi(-1)$, which yields the last equality in the displayed sum.

The forbidden count for this fixed anisotropic $K$ is therefore
$$
p^2-p+\chi(-d).
$$
In the basis formed by $k$ and the chosen basis of $K^{\perp}$, the Gram determinant is $q(k)d$. A change of basis multiplies a Gram determinant by a square, while the standard dot product has determinant $1$. Therefore
$$
\chi(q(k)d)=1,
$$
so
$$
\chi(d)=\chi(q(k)).
$$
Writing
$$
\varepsilon=\chi(-1),
$$
the forbidden count is
$$
p^2-p+\varepsilon\chi(q(k)).
$$

Step 4: Count the forbidden matrices for a fixed isotropic radical line

Now let $K=\langle e\rangle$ be isotropic. Choose a Witt basis $e,f,h$ such that the Gram matrix of the dot product is
$$
J=\begin{pmatrix}0&1&0\\1&0&0\\0&0&d\end{pmatrix},\qquad d\ne0.
$$
For a self-adjoint operator $S$ with $Se=0$, the condition $JS=S^TJ$ gives
$$
S=\begin{pmatrix}
0&a&dr\\
0&0&0\\
0&r&g
\end{pmatrix}.
$$
The second row is zero, so the rank is at most $2$. The minor on rows $1,3$ and columns $2,3$ has determinant $ag-dr^2$, so the rank is $2$ exactly when
$$
ag-dr^2\ne0.
$$
Also,
$$
\det(I+S)=1+g.
$$
So $I+S$ is singular exactly when $g=-1$, after which the rank condition becomes
$$
a\ne-dr^2.
$$
There are $p$ choices for $r$ and $p-1$ choices for $a$, so a fixed isotropic radical line contributes
$$
p(p-1)=p^2-p
$$
forbidden matrices.

Step 5: Count radical lines of each quadratic type

First, the number of isotropic lines for $q$ is $p+1$. For any nonzero $a\in\mathbb F_p$, consider
$$
y^2=x^2-a.
$$
The factorization $(x-y)(x+y)=a$ gives exactly $p-1$ pairs $(x,y)$, since each nonzero value of $x-y$ determines $x+y$. On the other hand, the number of pairs is
$$
p+\sum_x\chi(x^2-a),
$$
so
$$
\sum_x\chi(x^2-a)=-1.
$$
Applying this with $a=-1$ gives
$$
\sum_t\chi(t^2+1)=-1.
$$
Therefore
$$
\sum_{x,y\in\mathbb F_p}\chi(x^2+y^2)=0:
$$
for $y=0$ the contribution is $p-1$, while each $y\ne0$ contributes $-1$ after scaling by $y$. The number of vectors satisfying
$$
x^2+y^2+z^2=0
$$
is then
$$
p^2+\chi(-1)\sum_{x,y}\chi(x^2+y^2)=p^2.
$$
Removing the zero vector and dividing by $p-1$ gives $p+1$ isotropic lines.

There remain $p^2$ anisotropic lines. Let $N_+$ and $N_-$ be the numbers whose nonzero norm is respectively a square or a nonsquare. Since scalar multiplication changes the norm by a square, each anisotropic line has a well-defined sign $\chi(q(k))$.

Let
$$
M=\#\{(x,y):x^2+y^2=0\}.
$$
When $y=0$, only $x=0$ works. For each $y\ne0$, the ratio $x/y$ must satisfy $(x/y)^2=-1$, which has $1+\varepsilon$ solutions. This gives
$$
M=1+(p-1)(1+\varepsilon)=p+(p-1)\varepsilon.
$$
For fixed $(x,y)$ with $x^2+y^2\ne0$, the displayed character-sum identity applied with $a=-(x^2+y^2)$ gives
$$
\sum_z\chi(x^2+y^2+z^2)=-1.
$$
If $x^2+y^2=0$, the same sum is $p-1$. Therefore
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
So exactly
$$
p^4
$$
rank-two symmetric matrices make $I+S$ singular. Subtracting them from the total in Step 2 gives
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

## Black-Box Audit — no issues found
