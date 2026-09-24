## Steps

Step 1: Recover affine collinearity from the hypergraph
Fix $u\in V$. On $V\setminus\{u\}$, join $x$ and $y$ when $\{u,x,y\}\in\mathscr H$. Write $a=x-u$ and $b=y-u$.

If $b=\lambda a$ with $\lambda\in\mathbb F_\ell^\times$, then a common neighbor $z$ must satisfy
$$
\chi(\det(a,z-u))=1
$$
and
$$
\chi(\lambda\det(a,z-u))=1.
$$
If $\chi(\lambda)=-1$, there are no common neighbors. If $\chi(\lambda)=1$, the nonzero square values of the linear functional $t\mapsto\det(a,t)$ each have exactly $\ell$ preimages, so the number of common neighbors is
$$
\frac{\ell(\ell-1)}{2}.
$$

If $a,b$ are linearly independent, write $z-u=sa+tb$. Since $\chi(-1)=1$, the two adjacency conditions prescribe the square classes of the two nonzero scalars $s,t$. Hence the number of common neighbors is
$$
\left(\frac{\ell-1}{2}\right)^2.
$$
For $\ell\geq5$, this differs from both collinear counts. Thus the hypergraph determines exactly which triples are collinear, so every $\sigma\in\operatorname{Aut}(\mathscr H)$ preserves affine lines.

Step 2: Show every hypergraph automorphism is affine
Let $\sigma\in\operatorname{Aut}(\mathscr H)$ and put $b=\sigma(0)$. Replacing $\sigma$ by $x\mapsto\sigma(x)-b$, assume $\sigma(0)=0$.

Because $\sigma$ preserves collinearity, it sends every line through $0$ to a line through $0$. It also preserves parallelism: two disjoint affine lines have disjoint images, since an intersection point of the images would have a preimage lying on both original lines.

Choose independent vectors $e_1,e_2$. There are bijections $\varphi_1,\varphi_2:\mathbb F_\ell\to\mathbb F_\ell$ with $\varphi_i(0)=0$ such that
$$
\sigma(te_i)=\varphi_i(t)\sigma(e_i).
$$
The point $se_1+te_2$ is the intersection of the line through $se_1$ parallel to $\mathbb F_\ell e_2$ and the line through $te_2$ parallel to $\mathbb F_\ell e_1$. Parallelism preservation therefore gives
$$
\sigma(se_1+te_2)
=
\varphi_1(s)\sigma(e_1)+\varphi_2(t)\sigma(e_2).
$$
Applying this to the line $\mathbb F_\ell(e_1+e_2)$ shows $\varphi_1=\varphi_2=: \varphi$, because every image point on that line has equal coordinates relative to $\sigma(e_1),\sigma(e_2)$.

Use these image vectors as coordinate axes. The line
$
\{se_1+(s+t)e_2:s\in\mathbb F_\ell\}
$
is parallel to $\mathbb F_\ell(e_1+e_2)$. Its image is therefore parallel to the line of slope $1$ and contains $(0,\varphi(t))$. Hence for every $s,t$,
$
\varphi(s+t)=\varphi(s)+\varphi(t).
$
Likewise the line $\mathbb F_\ell(e_1+te_2)$ passes through $(1,t)$, so its image is the line through the origin and $(1,\varphi(t))$. The image of the point $se_1+st e_2$ lies on this line, giving
$
\varphi(st)=\varphi(s)\varphi(t).
$
Thus $\varphi$ is a field automorphism of the prime field $\mathbb F_\ell$, so $\varphi$ is the identity. Therefore
$$
\sigma(x)=Ax+b
$$
for some $A\in GL_2(\mathbb F_\ell)$ and $b\in V$.

Step 3: Determine which affine maps preserve the square-determinant relation
For an affine map $x\mapsto Ax+b$,
$$
\det\bigl(A(v-u),A(w-u)\bigr)
=
\det(A)\det(v-u,w-u).
$$
Thus square determinants remain square exactly when $\chi(\det A)=1$. Therefore
$$
\operatorname{Aut}(\mathscr H)
=
V\rtimes GL_2^+(\mathbb F_\ell),
$$
where
$$
GL_2^+(\mathbb F_\ell)
=
\{A\in GL_2(\mathbb F_\ell):\chi(\det A)=1\}.
$$

Step 4: Count square-determinant matrices with eigenvalue $1$
Let $n_1$ be the number of nonidentity matrices $A\in GL_2^+(\mathbb F_\ell)$ having eigenvalue $1$. Count pairs $(v,A)$ with $v\neq0$ and $Av=v$.

For a fixed nonzero $v$, choose a basis beginning with $v$. Then
$$
A=
\begin{pmatrix}
1&a\\
0&d
\end{pmatrix},
$$
where $a\in\mathbb F_\ell$ and $d$ is a nonzero square. Hence there are
$$
\frac{\ell(\ell-1)}{2}
$$
choices of $A$ for each $v$, and therefore
$$
(\ell^2-1)\frac{\ell(\ell-1)}{2}
$$
such pairs.

The identity contributes $\ell^2-1$ pairs. Every other matrix counted by $n_1$ has a one-dimensional fixed space and therefore contributes $\ell-1$ nonzero fixed vectors. Consequently
$$
n_1
=
\frac{(\ell^2-1)\left(\frac{\ell(\ell-1)}{2}-1\right)}{\ell-1}
=
\frac{(\ell+1)^2(\ell-2)}{2}.
$$

Step 5: Count the fixed-point-free affine automorphisms
For $g(x)=Ax+b$, a fixed point exists exactly when
$$
b\in\operatorname{Im}(I-A).
$$
If $A=I$, exactly the $\ell^2-1$ nonzero translations are fixed-point-free.

If $A\neq I$ has eigenvalue $1$, then $\operatorname{rank}(I-A)=1$, so $\operatorname{Im}(I-A)$ has $\ell$ elements. Hence each such $A$ gives $\ell^2-\ell$ fixed-point-free choices of $b$.

If $A$ has no eigenvalue $1$, then $I-A$ is invertible, so every $b$ yields a unique fixed point. Therefore the desired number is
$$
(\ell^2-1)+(\ell^2-\ell)n_1.
$$
Substituting the value from Step 4 gives
$$
(\ell^2-1)
+
(\ell^2-\ell)\frac{(\ell+1)^2(\ell-2)}{2}
=
\frac{(\ell-1)^2(\ell+1)(\ell^2-2)}{2}.
$$
Final Answer: $\boxed{\frac{(\ell-1)^2(\ell+1)(\ell^2-2)}{2}}$

---

## Answer

$\frac{(\ell-1)^2(\ell+1)(\ell^2-2)}{2}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quadratic characters
- affine geometry
- hypergraph automorphisms
- eigenvalue counting
- fixed point criterion
