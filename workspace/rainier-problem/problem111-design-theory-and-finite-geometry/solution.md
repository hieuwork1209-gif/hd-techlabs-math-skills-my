## Steps

Step 1: Recover affine collinearity from the hypergraph
For distinct $a,b\in V$, let
$$
L(a,b)=\{x\in V:\{a,b,x\}\in\mathscr H\}.
$$
Fix distinct $a,b,c$ and translate so that $a=0$. Put
$$
B(x)=\det(b,x),
\qquad
C(x)=\det(c,x).
$$
If $a,b,c$ are noncollinear, then $B$ and $C$ are linearly independent, so
$$
x\longmapsto (B(x),C(x))
$$
is a bijection from $V$ to $\mathbb F_\ell^2$. Hence
$$
|L(a,b)\cap L(a,c)|
=
\left(\frac{\ell-1}{2}\right)^2.
$$

If $a,b,c$ are collinear, write $c=tb$ with $t\neq0$. Then $C=tB$. If $\chi(t)=-1$, the two square conditions are incompatible and the intersection is empty. If $\chi(t)=1$, the functional $B$ has exactly $\ell$ preimages of each value, so
$$
|L(a,b)\cap L(a,c)|
=
\frac{\ell(\ell-1)}{2}.
$$
For $\ell\geq5$, the three values
$$
0,
\qquad
\left(\frac{\ell-1}{2}\right)^2,
\qquad
\frac{\ell(\ell-1)}{2}
$$
are distinct. Thus $\mathscr H$ determines collinearity, and every element of $\operatorname{Aut}(\mathscr H)$ maps affine lines to affine lines.

Step 2: Determine the full hypergraph automorphism group
Let $\sigma\in\operatorname{Aut}(\mathscr H)$. After translating the image of $0$, assume $\sigma(0)=0$. Since collinearity and disjointness of lines are preserved, parallel lines are preserved.

Choose independent $e_1,e_2$. There are bijections $\varphi_1,\varphi_2:\mathbb F_\ell\to\mathbb F_\ell$ with $\varphi_i(0)=0$ such that
$$
\sigma(te_i)=\varphi_i(t)\sigma(e_i).
$$
Using intersections of lines parallel to the two coordinate axes gives
$$
\sigma(se_1+te_2)
=
\varphi_1(s)\sigma(e_1)+\varphi_2(t)\sigma(e_2).
$$
The image of the line $\mathbb F_\ell(e_1+e_2)$ shows $\varphi_1=\varphi_2=: \varphi$.

In the coordinates with axes $\sigma(e_1),\sigma(e_2)$, the line
$$
\{se_1+(s+t)e_2:s\in\mathbb F_\ell\}
$$
is parallel to the line of slope $1$. Its image therefore gives
$$
\varphi(s+t)=\varphi(s)+\varphi(t).
$$
Likewise the image of the line $\mathbb F_\ell(e_1+te_2)$ gives
$$
\varphi(st)=\varphi(s)\varphi(t).
$$
Thus $\varphi$ is a field automorphism of the prime field $\mathbb F_\ell$, hence the identity. Restoring the translation,
$$
\sigma(x)=Ax+b
$$
for some $A\in GL_2(\mathbb F_\ell)$ and $b\in V$.

Such a map satisfies
$$
\det\bigl(A(v-u),A(w-u)\bigr)
=
\det(A)\det(v-u,w-u),
$$
so it preserves $\mathscr H$ exactly when $\chi(\det A)=1$. Therefore
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

Step 3: Restrict the possible linear projections of a regular subgroup
Let $G\leq\operatorname{Aut}(\mathscr H)$ act regularly on $V$. Since $|V|=\ell^2$, regularity gives
$$
|G|=\ell^2.
$$
Let
$$
\pi:G\to GL_2^+(\mathbb F_\ell)
$$
be the linear-part homomorphism. Because
$$
|GL_2(\mathbb F_\ell)|
=
\ell(\ell-1)^2(\ell+1),
$$
every $\ell$-subgroup of $GL_2(\mathbb F_\ell)$ has order at most $\ell$. Hence
$$
|\pi(G)|\in\{1,\ell\}.
$$

If $\pi(G)=1$, then $G$ consists only of translations. The full translation group already has order $\ell^2$, so in this case
$$
G=V.
$$

Assume now $|\pi(G)|=\ell$. Every $\ell$-element of the affine group has order dividing $\ell$. Indeed, if its linear part is nontrivial, then it has the form $A=I+N$ with $N^2=0$, and for $g(x)=Ax+b$,
$$
g^\ell(x)
=
x+
\left(\sum_{j=0}^{\ell-1}A^j\right)b.
$$
Since
$$
A^j=I+jN
$$
and $\ell$ is odd,
$$
\sum_{j=0}^{\ell-1}A^j
=
\ell I+\frac{\ell(\ell-1)}{2}N
=
0.
$$
The same conclusion is immediate for a translation. Thus $G$ has exponent $\ell$ and is elementary abelian.

Step 4: Identify the translation line and the unique linear subgroup attached to it
Let
$$
K=G\cap V.
$$
Since $|G|=\ell^2$ and $|\pi(G)|=\ell$, the group $K$ has order $\ell$, so its translation vectors form a line $U\leq V$.

Because $G$ is abelian, an element $(A,b)\in G$ commutes with every translation by $u\in U$. Conjugating a translation by $(A,b)$ sends $u$ to $Au$, hence
$$
Au=u
\qquad(u\in U).
$$
For nonidentity $A\in\pi(G)$, the fixed space is one-dimensional, so it is exactly $U$.

Write $A=I+N$. Then $N\neq0$, $N^2=0$, and
$$
\ker N=\operatorname{im}N=U.
$$
Conversely, for a fixed line $U$, the space of maps $N:V/U\to U$ is one-dimensional. Any two nonzero such maps are scalar multiples and generate the same subgroup
$$
P_U=\{I+tN:t\in\mathbb F_\ell\}.
$$
Therefore each line $U$ determines exactly one possible order-$\ell$ linear projection $P_U$, and every element of $P_U$ has determinant $1$.

Step 5: Convert regularity into an isomorphism between two one-dimensional groups
Fix a line $U$ and its subgroup $P_U$. For $A\in P_U$, let $C_A$ be the set of vectors $b$ such that $(A,b)\in G$. Each fiber has $\ell$ elements and is a coset of $U$. Define
$$
\lambda(A)=C_A/U\in V/U.
$$

For $A,B\in P_U$, multiplication in the affine group gives
$$
(A,b)(B,c)=(AB,b+Ac).
$$
Every $A\in P_U$ acts trivially on $V/U$ because $(A-I)V\subseteq U$. Therefore
$$
\lambda(AB)=\lambda(A)+\lambda(B).
$$
So $\lambda:P_U\to V/U$ is a group homomorphism.

If $A\neq I$ and $\lambda(A)=0$, then every $b\in C_A$ lies in
$$
U=\operatorname{im}(I-A),
$$
so the affine map $x\mapsto Ax+b$ has a fixed point. This contradicts regularity. Hence $\lambda$ is injective, and since both groups have order $\ell$, it is an isomorphism.

Conversely, every isomorphism $\lambda:P_U\to V/U$ defines
$$
G_{U,\lambda}
=
\{(A,b):A\in P_U,\ b+U=\lambda(A)\}.
$$
The homomorphism identity makes this a subgroup of order $\ell^2$. If $A=I$, its nonidentity elements are nonzero translations. If $A\neq I$, then $\lambda(A)\neq0$, so
$$
b\notin U=\operatorname{im}(I-A),
$$
and the affine map has no fixed point. Thus every nonidentity element is fixed-point-free. Since the group has the same size as $V$, its action is regular.

Step 6: Count all regular subgroups
There are
$$
\frac{\ell^2-1}{\ell-1}=\ell+1
$$
lines $U$ in $V$. For each line, both $P_U$ and $V/U$ are cyclic groups of order $\ell$, so there are exactly $\ell-1$ isomorphisms
$$
\lambda:P_U\to V/U.
$$
Hence the regular subgroups with nontrivial linear projection number
$$
(\ell+1)(\ell-1)=\ell^2-1.
$$
Adding the unique full translation subgroup gives
$$
1+(\ell^2-1)=\ell^2.
$$
Final Answer: $\boxed{\ell^2}$

---

## Answer

$\ell^2$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quadratic characters
- affine geometry
- regular group actions
- affine semidirect products
- elementary abelian groups
