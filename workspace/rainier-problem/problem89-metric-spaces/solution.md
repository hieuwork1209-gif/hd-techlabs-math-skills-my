## Steps

Step 1: Package the gallery metric into one Hecke generating function

Write a flag as $F=(P<L<H)$, with $\dim P=1$, $\dim L=2$, and $\dim H=3$. There are
$$
15\cdot7\cdot3=315
$$
flags. Fixing a base flag, Bruhat decomposition assigns to every other flag a relative position $w\in S_4$, and the graph distance is the Coxeter length $\ell(w)$.

Let $T_i$ be the operator summing over the two neighbors obtained by changing only the $i$-th member of the flag. Since each panel contains three flags,
$$
T_i^2=T_i+2I,
$$
and the $T_i$ satisfy the type-$A_3$ braid relations. If $T_w$ is the product along a reduced word for $w$, then with
$$
A_r=\sum_{\ell(w)=r}T_w
$$
we have
$$
D_p=\sum_{r=1}^6 r^pA_r.
$$

Instead of expanding the $24$ Bruhat positions one by one, use the length-generating element
$$
R(z):=\sum_{r=0}^6z^rA_r.
$$
The usual insertion decomposition of a permutation in $S_4$ gives the factorization
$$
R(z)
=(I+zT_1)
(I+zT_2+z^2T_2T_1)
(I+zT_3+z^2T_3T_2+z^3T_3T_2T_1).
$$
This factorization computes all six distance shells simultaneously.

Step 2: Construct the $14$-dimensional critical space and compute its eigenvalue

Let $\mathcal P$ and $\mathcal H$ be the $15$ points and $15$ planes of $\operatorname{PG}(3,2)$. For a mean-zero function $u:\mathcal P\to\mathbb{R}$, define
$$
c_u(P,L,H)=u(P)-\frac{1}{2}\sum_{Q\subset H}u(Q).
$$
Let $N$ be the point-plane incidence matrix. Every point lies in $7$ planes and two distinct points lie in exactly $3$ common planes, hence
$$
NN^T=4I+3J.
$$
Thus, when $\sum_Qu(Q)=0$,
$$
\|N^Tu\|^2=4\|u\|^2.
$$
For every incident pair $P\subset H$ there are three possible lines $L$, so
$$
\begin{aligned}
\|c_u\|^2
&=3\sum_{P\subset H}\left(u(P)-\frac{1}{2}(N^Tu)(H)\right)^2\\
&=3\left(7\|u\|^2-\|N^Tu\|^2+\frac{7}{4}\|N^Tu\|^2\right)\\
&=30\|u\|^2.
\end{aligned}
$$
Therefore
$$
W:=\left\{c_u:\sum_Qu(Q)=0\right\}
$$
has dimension $14$. Its vectors also have coordinate sum $0$.

It remains to find the action of the shells $A_r$ on $W$. Fix a point $Q$ and a flag $F=(P,L,H)$. Relative to $F$, the point $Q$ is in exactly one of four states:
$$
Q=P,\qquad Q\subset L,\ Q\ne P,\qquad Q\subset H,\ Q\not\subset L,\qquad Q\not\subset H.
$$
For a coefficient vector $(a,b,c,d)$ on these four states, changing one member of the flag gives
$$
T_1(a,b,c,d)=(2b,a+b,2c,2d),
$$
$$
T_2(a,b,c,d)=(2a,2c,b+c,2d),
$$
$$
T_3(a,b,c,d)=(2a,2b,2d,c+d).
$$
For example, if $Q=P$ and $P$ is changed, both new points are different from $Q$, which explains the first coordinate $2b$ in the first rule. The other entries follow in the same way from the three choices in each panel.

The coefficient of $u(Q)$ in $c_u(F)$ is represented by
$$
h=\left(\frac{1}{2},-\frac{1}{2},-\frac{1}{2},0\right).
$$
Since $\sum_Qu(Q)=0$, adding a constant vector to $h$ does not change the resulting function on flags. Applying the factorization of $R(z)$ from Step 1 to $h$ gives, modulo constant vectors,
$$
R(z)h\equiv
\left(1+3z+2z^2-6z^3-16z^4+16z^6\right)h.
$$
More explicitly,
$$
R(z)h=
\left(1+3z+2z^2-6z^3-16z^4+16z^6\right)h
-
\left(\frac{z}{2}+3z^2+9z^3+16z^4+16z^5+8z^6\right)\mathbf{1}.
$$
The constant term disappears after summing against $u$. Hence every $c_u\in W$ satisfies
$$
A_1c_u=3c_u,\quad
A_2c_u=2c_u,\quad
A_3c_u=-6c_u,\quad
A_4c_u=-16c_u,\quad
A_5c_u=0,\quad
A_6c_u=16c_u.
$$
Therefore
$$
D_pc_u=L(p)c_u,
$$
where
$$
L(p)=3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p.
$$

Step 3: Locate the unique zero of the critical eigenvalue

We have
$$
L(0)=-1,
\qquad
L'(0)=2\log\frac{243}{128}>0.
$$
Also
$$
L''(p)
=2(\log 2)^2 2^p-6(\log 3)^2 3^p-16(\log 4)^2 4^p+16(\log 6)^2 6^p.
$$
For $p\geq0$, using $6^p\geq4^p\geq3^p$ gives
$$
L''(p)
\geq
2(\log 2)^2 2^p
+\left(16\big((\log 6)^2-(\log 4)^2\big)-6(\log 3)^2\right)4^p>0.
$$
Thus $L'$ is increasing and positive, so $L$ is strictly increasing on $[0,\infty)$.

A direct outward-rounded evaluation gives
$$
L(0.265)<-0.0037,
\qquad
L(0.266)>0.0031.
$$
Hence there is a unique
$$
\alpha\in(0.265,0.266)
$$
such that
$$
3+2\cdot2^{\alpha}-6\cdot3^{\alpha}-16\cdot4^{\alpha}+16\cdot6^{\alpha}=0.
$$
Numerically, $\alpha\approx0.2655412194$.

Step 4: Prove that no other nonconstant Hecke mode reaches zero at $p=\alpha$

The chamber representation is the permutation module on $G/B$, where $G=\operatorname{GL}_4(2)$. Since $H_2(S_4)$ is semisimple, double centralizer theory gives
$$
\mathbb R^X\cong
V_{(4)}\otimes S^{(4)}
\oplus V_{(31)}\otimes S^{(31)}
\oplus V_{(22)}\otimes S^{(22)}
\oplus V_{(211)}\otimes S^{(211)}
\oplus V_{(1111)}\otimes S^{(1111)}.
$$
The Hecke dimensions are
$$
\dim S^{(4)},\dim S^{(31)},\dim S^{(22)},\dim S^{(211)},\dim S^{(1111)}
=1,3,2,3,1.
$$
The multiplicities of these Hecke modules in the full chamber space are the dimensions of the corresponding unipotent $G$-modules. The $q$-hook formula at $q=2$ gives
$$
\dim V_\lambda
=2^{\sum_i(i-1)\lambda_i}
\frac{\prod_{j=1}^4(2^j-1)}{\prod_{u\in\lambda}(2^{h(u)}-1)},
$$
so
$$
\begin{array}{c|ccccc}
\lambda&(4)&(31)&(22)&(211)&(1111)\\
\hline
\dim S^\lambda&1&3&2&3&1\\
\dim V_\lambda&1&14&20&56&64
\end{array}
$$
and indeed
$$
1\cdot1+14\cdot3+20\cdot2+56\cdot3+64\cdot1=315.
$$
Thus, on the $\lambda$-isotypic summand, every Hecke element, and in particular $D_p$, acts as
$$
I_{\dim V_\lambda}\otimes M_\lambda(p).
$$
Consequently the nullity in the full chamber space is obtained by multiplying the nullity of each small Hecke block by the corresponding number in the second row of the table.

We now compute those small blocks. Put
$$
x_r=r^\alpha\qquad(2\le r\le6).
$$
From $0.265<\alpha<0.266$ we have the outward-rounded intervals
$$
\begin{aligned}
1.2016&<x_2<1.2025,\\
1.3379&<x_3<1.3395,\\
1.4439&<x_4<1.4460,\\
1.5318&<x_5<1.5344,\\
1.6077&<x_6<1.6107.
\end{aligned}
$$

For $S^{(31)}$, inducing the trivial module from $H_2(S_3)$ gives $S^{(4)}\oplus S^{(31)}$. Removing the constant summand, one eigenvalue is the already identified
$$
L(\alpha)=0,
$$
and the other two eigenvalues are the roots of the characteristic polynomial of
$$
Q_{31}=
\begin{pmatrix}
8x_2+10x_3+8x_4-16x_5-16x_6+5&4x_2+4x_3-8x_4\\
11x_2+14x_3-4x_4-24x_5+3&-2x_2-4x_3+4x_4+16x_5-16x_6+1
\end{pmatrix}.
$$
Substituting the five intervals above entrywise gives
$$
Q_{31,11}\in(-10.7786,-10.6490),\quad
Q_{31,12}\in(-1.4100,-1.3832),
$$
$$
Q_{31,21}\in(-7.6614,-7.5583),\quad
Q_{31,22}\in(-2.2498,-2.1436).
$$
Hence
$$
\operatorname{tr}Q_{31}\in(-13.0284,-12.7926),
$$
and, using $\det Q=Q_{11}Q_{22}-Q_{12}Q_{21}$ with interval multiplication,
$$
\det Q_{31}\in(12.0246,13.7951).
$$
Therefore the two remaining $S^{(31)}$ eigenvalues are both strictly negative.

For $S^{(211)}$, inducing the sign module from the same parabolic gives one scalar eigenvalue
$$
L_{211}=-4x_2+3x_3+2x_4-6x_5+4x_6
\in(-0.6841,-0.6439),
$$
and a quadratic block
$$
Q_{211}=
\begin{pmatrix}
7x_3-12x_4+10x_5-4x_6-2&2x_2+2x_3-4x_4\\
-2x_3+3x_4-2x_5+1&-3x_2-4x_3+6x_4+2x_5-4x_6+2
\end{pmatrix}.
$$
The same entrywise interval substitution yields
$$
Q_{211,11}\in(-1.1115,-1.0371),\quad
Q_{211,12}\in(-0.7050,-0.6916),
$$
$$
Q_{211,21}\in(-0.4161,-0.4014),\quad
Q_{211,22}\in(-1.6813,-1.6424),
$$
so
$$
\operatorname{tr}Q_{211}\in(-2.7928,-2.6795),
\qquad
\det Q_{211}\in(1.4100,1.5912).
$$
Thus all three $S^{(211)}$ eigenvalues are strictly negative.

For $S^{(22)}$ one may use the concrete Hecke representation
$$
T_1=T_3=
\begin{pmatrix}2&0\\0&-1\end{pmatrix},
\qquad
T_2=
\begin{pmatrix}-1/3&14/9\\1&4/3\end{pmatrix},
$$
which satisfies $T_i^2=T_i+2I$ and the braid relations. Substituting these matrices into the factorized $R(z)$ of Step 1 and then replacing the coefficient of $z^r$ by $x_r$ gives
$$
Q_{22}=
\begin{pmatrix}
\frac43x_2-8x_3-\frac{26}3x_4+\frac83x_5+8x_6+\frac{11}3&
\frac{28}9x_2-\frac{14}3x_3-\frac{56}9x_4+\frac{56}9x_5+\frac{14}9\\
2x_2-3x_3-4x_4+4x_5+1&
-\frac{13}3x_2+8x_3+\frac83x_4-\frac{44}3x_5+8x_6-\frac23
\end{pmatrix}.
$$
Its entries satisfy
$$
Q_{22,11}\in(-1.0328,-0.9696),\quad
Q_{22,12}\in(-0.4233,-0.3837),
$$
$$
Q_{22,21}\in(-0.2721,-0.2467),\quad
Q_{22,22}\in(-0.9669,-0.8824),
$$
whence
$$
\operatorname{tr}Q_{22}\in(-1.9997,-1.8520),
\qquad
\det Q_{22}\in(0.7404,0.9039).
$$
Thus both $S^{(22)}$ eigenvalues are strictly negative.

Finally, on $S^{(1111)}$ the generators act by $-1$, so the distance operator is the scalar
$$
S=-3+5x_2-6x_3+5x_4-3x_5+x_6
\in(-0.8050,-0.7696),
$$
again strictly negative.

Each chamber-space distance operator is real symmetric. Hence the roots of every displayed quadratic factor are real, and a quadratic block with negative trace and positive determinant has two negative eigenvalues. We have therefore shown that the only zero eigenvalue among all nonconstant Hecke blocks at $p=\alpha$ is the single eigenvalue $L(\alpha)=0$ inside $S^{(31)}$.

Because that zero is simple in the $3$-dimensional Hecke module $S^{(31)}$, while $S^{(31)}$ occurs with multiplicity exactly
$$
\dim V_{(31)}=14,
$$
the full zero eigenspace inside $\mathbf 1^\perp$ has dimension exactly $14$. The space $W$ from Step 2 already supplies $14$ independent zero vectors, so in fact
$$
\ker(D_\alpha|_{\mathbf1^\perp})=W.
$$

Step 5: Determine the supremal negative type and the equality space

Let $0<p<\alpha$ and put $s=p/\alpha\in(0,1)$. For $t\geq0$,
$$
t^s=c_s\int_0^\infty(1-e^{-ut})u^{-1-s}\,du
$$
with $c_s>0$. Since $D_{\alpha}$ is conditionally negative semidefinite, $e^{-u d(F,H)^{\alpha}}$ is positive semidefinite for every $u>0$. Thus for every real family $c_F$ with $\sum_Fc_F=0$,
$$
\sum_{F,H}c_Fc_Hd(F,H)^p
=-c_s\int_0^\infty
\sum_{F,H}c_Fc_He^{-u d(F,H)^{\alpha}}
\,u^{-1-s}\,du\leq0.
$$
Hence $(X,d)$ has $p$-negative type for every $p\leq\alpha$.

For $p>\alpha$, Step 2 gives $L(p)>0$ because $L$ is strictly increasing. Any nonzero $c_u\in W$ then satisfies
$$
c_u^TD_pc_u=L(p)\|c_u\|^2>0,
$$
so $p$-negative type fails. Therefore
$$
\wp=\alpha.
$$
At $p=\alpha$, Step 4 shows that the only zero directions in $\mathbf{1}^{\perp}$ are those in $W$. Consequently
$$
E=W,
\qquad
\dim E=14.
$$

Final Answer: $\boxed{(\min\{p>0:3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p=0\},14)}$

---

## Answer

$(\min\{p>0:3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p=0\},14)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- negative type of finite metric spaces
- complete flag graph metrics
- point-plane incidence operators
- Iwahori-Hecke algebra
