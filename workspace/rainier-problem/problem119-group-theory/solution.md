## Steps

Step 1: Reduce the subgroup-orbit problem to orthogonal conjugacy

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
As in the subgroup count, every admissible subgroup has the form
$$
A_T=\{(u,Tu,t):u\in U,\ t\in\mathbb F_p\},
$$
where $T$ is a symmetric invertible $3\times3$ matrix and
$$
\dim\ker(T-I)=1.
$$
Indeed, the two coordinate-intersection conditions make $A_T/Z$ the graph of an invertible map $T$, abelianness is equivalent to self-adjointness for the dot product, and the diagonal intersection has order $p^{1+\dim\ker(T-I)}$.

Let
$$
\mathcal O=\{Q\in GL_3(\mathbb F_p):Q^TQ=I\}.
$$
For $Q\in\mathcal O$, the automorphism
$$
\varphi_Q(u,v,t)=(Qu,Qv,t)
$$
sends $A_T$ to
$$
A_{QTQ^{-1}}.
$$
Thus the required number of subgroup orbits is the number of orthogonal-conjugacy classes of symmetric invertible $T$ with one-dimensional $1$-eigenspace.

Step 2: Split according to the algebraic multiplicity of the eigenvalue $1$

Let $m$ be the algebraic multiplicity of $1$ in the characteristic polynomial of $T$. Since $\dim\ker(T-I)=1$, we have
$$
m\in\{1,2,3\}.
$$
For a self-adjoint operator, primary components belonging to coprime factors are orthogonal: Bezout's identity together with $P(T)^*=P(T)$ for every polynomial $P$ gives orthogonality of the corresponding generalized kernels.

If $m=1$, the $1$-eigenspace is a nondegenerate line $L$, and
$$
U=L\perp W,
$$
where $W$ is a nondegenerate two-dimensional space. On $W$, the restriction $B=T|_W$ is self-adjoint and satisfies
$$
\det B\ne0,\qquad \det(B-I)\ne0.
$$
There are two isometry types for $W$, split and anisotropic. By Witt's extension theorem, the orthogonal group of $U$ is transitive on nondegenerate lines with a fixed complement type, so the $m=1$ contribution is the sum of the numbers of orthogonal-conjugacy classes of such $B$ on the two types of planes.

Step 3: Count the two-dimensional conjugacy classes by Burnside's lemma

Put
$$
M=p(p-1)^2.
$$
First take the split plane with Gram matrix
$$
J_+=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
A self-adjoint map has the form
$$
B=\begin{pmatrix}a&b\\c&a\end{pmatrix}.
$$
The equations $\det B=0$ and $\det(B-I)=0$ each have $p^2$ solutions. If both hold, then
$$
a^2=bc=(a-1)^2,
$$
so $a=\frac12$ and $bc=\frac14$, giving $p-1$ common solutions. Hence the number of admissible maps is
$$
S_+=p^3-2p^2+p-1=M-1.
$$

The group $O^+(2,p)$ has $2(p-1)$ elements: rotations
$$
D_r=\begin{pmatrix}r&0\\0&r^{-1}\end{pmatrix}
$$
and reflections
$$
R_r=\begin{pmatrix}0&r\\r^{-1}&0\end{pmatrix},\qquad r\in\mathbb F_p^\times.
$$
The two rotations with $r=\pm1$ fix all $S_+$ admissible maps. Every other rotation fixes only scalar maps $aI$, with $a\notin\{0,1\}$, so it fixes $p-2$ maps. A reflection fixes exactly the matrices with $b=r^2c$. Writing $x=rc$, the two determinant conditions become
$$
a^2-x^2\ne0,\qquad (a-1)^2-x^2\ne0.
$$
With $u=a+x$ and $v=a-x$, this is $u,v\notin\{0,1\}$, giving $(p-2)^2$ fixed maps. Burnside's lemma gives
$$
c_+=\frac{2S_++(p-3)(p-2)+(p-1)(p-2)^2}{2(p-1)}
=\frac{p(3p-5)}2.
$$

For the anisotropic plane, identify the space with $E=\mathbb F_{p^2}$ and use the norm form. Every $\mathbb F_p$-linear map is uniquely $z\mapsto az+b\overline z$ with $a,b\in E$; taking adjoints for the norm form shows that self-adjointness is equivalent to $a\in\mathbb F_p$. Thus every self-adjoint map is
$$
B(z)=az+b\overline z,
$$
with $a\in\mathbb F_p$ and $b\in E$, and a direct determinant computation gives
$$
\det B=a^2-N(b),\qquad \det(B-I)=(a-1)^2-N(b).
$$
Each singularity equation has $p^2$ solutions. Their intersection has $a=\frac12$ and $N(b)=\frac14$, giving $p+1$ solutions. Thus
$$
S_-=p^3-2p^2+p+1=M+1.
$$

The group $O^-(2,p)$ has $2(p+1)$ elements. Its rotations are $z\mapsto uz$ and its reflections are $z\mapsto u\overline z$, where $N(u)=1$. The rotations $u=\pm1$ fix all $S_-$ maps, while the other $p-1$ rotations fix only the $p-2$ eligible scalar maps. A reflection fixes precisely those $b$ with $b=u^2\overline b$, equivalently $b=ux$ for $x\in\mathbb F_p$. Then $N(b)=x^2$, so the same change of variables as in the split case gives $(p-2)^2$ fixed maps. Hence
$$
c_-=\frac{2S_-+(p-1)(p-2)+(p+1)(p-2)^2}{2(p+1)}
=\frac{3p^2-9p+8}{2}.
$$
Therefore the contribution from $m=1$ is
$$
c_++c_-=3p^2-7p+4.
$$

Step 4: Count the classes with algebraic multiplicity $m=2$

Now the generalized $1$-primary space $P$ has dimension $2$, and the remaining primary space is a line. Orthogonal primary decomposition gives
$$
U=P\perp L,
$$
with
$$
T|_P=I+N,
$$
where $N\ne0$, $N^2=0$, and $N$ is self-adjoint. Since $N$ has rank $1$,
$$
\operatorname{im}N=\ker N.
$$
Self-adjointness gives $\operatorname{im}N=(\ker N)^\perp$ inside $P$, so this common line is isotropic. Hence $P$ is the split plane.

The action on $L$ is multiplication by some
$$
\lambda\in\mathbb F_p\setminus\{0,1\},
$$
because $T$ is invertible and $L$ is not part of the $1$-primary space. By Witt's extension theorem there is one orbit of embeddings of the split plane $P$ with its orthogonal complement of the required type. In a hyperbolic basis of $P$, every such nonzero nilpotent self-adjoint map is orthogonally conjugate to
$$
N_a=\begin{pmatrix}0&a\\0&0\end{pmatrix},\qquad a\ne0,
$$
up to exchanging the two isotropic lines. A rotation $\operatorname{diag}(r,r^{-1})$ sends $a$ to $r^2a$, so there are exactly two conjugacy classes, according to whether $a$ is a square or a nonsquare. Thus each of the $p-2$ choices of $\lambda$ gives two classes, for a total of
$$
2(p-2).
$$

Step 5: Count the class with algebraic multiplicity $m=3$

Here
$$
T=I+N,
$$
where $N$ is a regular nilpotent self-adjoint operator: $N^3=0$, $N^2\ne0$, and $\dim\ker N=1$. Choose $v$ with $N^2v\ne0$ and use the cyclic basis
$$
(N^2v,Nv,v).
$$
In this basis,
$$
N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}.
$$
If $G$ is the Gram matrix of the dot product, the equation $N^TG=GN$ forces
$$
G=\begin{pmatrix}0&0&d\\0&d&e\\d&e&f\end{pmatrix},\qquad d\ne0.
$$
A basis change commuting with $N$ has the form
$$
C=xI+yN+zN^2,\qquad x\ne0.
$$
Under $G\mapsto C^TGC$, the parameters become
$$
d'=dx^2,
$$
$$
e'=x(2dy+ex),
$$
and
$$
f'=2dxz+dy^2+2exy+fx^2.
$$
Choose $y$ to make $e'=0$ and then $z$ to make $f'=0$. The square class of $d$ is the only remaining invariant. Since
$$
\det G=-d^3
$$
and the ambient dot product has square determinant, $-d$ must be a square. Therefore $x$ can normalize $d$ to $-1$. All regular nilpotent self-adjoint $N$ are consequently orthogonally conjugate, so the case $m=3$ contributes exactly one class.

Step 6: Add the three primary cases

The three contributions are
$$
3p^2-7p+4,
$$
$$
2(p-2),
$$
and
$$
1.
$$
Their sum is
$$
3p^2-7p+4+2p-4+1=3p^2-5p+1.
$$

Final Answer: $\boxed{3p^2-5p+1}$

---

## Answer

$3p^2-5p+1$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- extraspecial finite group
- orthogonal conjugacy
- self-adjoint operators
- primary decomposition
- Burnside lemma

---

## Black-Box Audit — no issues found
