## Steps

Step 1: Package the gallery metric in the Hecke algebra

Write a flag as $F=(P<L<H)$, with dimensions $1,2,3$. There are
$$
15\cdot 7\cdot 3=315
$$
flags. Fixing a base flag, Bruhat decomposition assigns to every other flag a relative position $w\in S_4$, and the graph distance is the Coxeter length $\ell(w)$.

Let $T_i$ sum over the two neighbors obtained by changing only the $i$-th member of a flag. Each panel contains three flags, so
$$
T_i^2=T_i+2I,
$$
and the $T_i$ satisfy the type-$A_3$ braid relations. If $T_w$ is the product along a reduced word for $w$ and
$$
A_r=\sum_{\ell(w)=r}T_w,
$$
then the powered distance matrix is
$$
D_p=\sum_{r=1}^6 r^pA_r.
$$
Introduce
$$
R(z)=\sum_{r=0}^6z^rA_r.
$$
The insertion decomposition of permutations in $S_4$ gives
$$
R(z)=(I+zT_1)(I+zT_2+z^2T_2T_1)(I+zT_3+z^2T_3T_2+z^3T_3T_2T_1).
$$
All distance shells are therefore obtained from one three-factor expression.

Step 2: Construct the critical eigenspace

Let $\mathcal{P}$ and $\mathcal{H}$ be the $15$ points and $15$ planes of $\operatorname{PG}(3,2)$. For a mean-zero function $u:\mathcal{P}\to\mathbb{R}$, define
$$
c_u(P,L,H)=u(P)-\frac{1}{2}\sum_{Q\subset H}u(Q).
$$
Let $N$ be the point-plane incidence matrix. Every point is contained in $7$ planes and two distinct points are contained in exactly $3$ common planes, so
$$
NN^T=4I+3J.
$$
For $\sum_Q u(Q)=0$ this gives $\|N^T u\|^2=4\|u\|^2$. Since every incident pair $P\subset H$ admits three intermediate lines,
$$
\begin{aligned}
\|c_u\|^2
&=3\sum_{P\subset H}\left(u(P)-\frac{1}{2}(N^T u)(H)\right)^2\\
&=3\left(7\|u\|^2-\|N^T u\|^2+\frac{7}{4}\|N^T u\|^2\right)\\
&=30\|u\|^2.
\end{aligned}
$$
Therefore
$$
W=\left\{c_u:\sum_Q u(Q)=0\right\}
$$
has dimension $14$ and lies in $\mathbf{1}^{\perp}$.

Fix a point $Q$ and a flag $F=(P,L,H)$. Relative to $F$, the point $Q$ is in one of four states: $Q=P$; $Q\subset L$ but $Q\ne P$; $Q\subset H$ but $Q\not\subset L$; or $Q\not\subset H$. On coefficients $(a,b,c,d)$ for these states,
$$
T_1(a,b,c,d)=(2b,a+b,2c,2d),
$$
$$
T_2(a,b,c,d)=(2a,2c,b+c,2d),
$$
$$
T_3(a,b,c,d)=(2a,2b,2d,c+d).
$$
The coefficient of $u(Q)$ in $c_u(F)$ is represented, modulo constants, by
$$
h=\left(\frac{1}{2},-\frac{1}{2},-\frac{1}{2},0\right).
$$
Applying the factorization from Step 1 gives
$$
R(z)h\equiv(16z^6-16z^4-6z^3+2z^2+3z+1)h
$$
modulo the constant vector. So every $c_u\in W$ satisfies
$$
D_p c_u=L(p)c_u,
$$
where
$$
L(p)=3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p.
$$

Step 3: Locate the critical exponent

We have
$$
L(0)=-1,
\qquad
L'(0)=2\log\frac{243}{128}>0,
$$
and
$$
L''(p)=2(\log 2)^2 2^p-6(\log 3)^2 3^p-16(\log 4)^2 4^p+16(\log 6)^2 6^p.
$$
For $p\geq0$, since $6^p\geq4^p\geq3^p$,
$$
L''(p)\geq2(\log 2)^2 2^p+\left(16((\log 6)^2-(\log 4)^2)-6(\log 3)^2\right)4^p>0.
$$
$L'$ is increasing and remains positive, so $L$ is strictly increasing on $[0,\infty)$. Outward-rounded evaluation gives
$$
L(0.26554)<-8.4\cdot10^{-6},
\qquad
L(0.26555)>6.0\cdot10^{-5}.
$$
This gives a unique root
$$
\alpha\in(0.26554,0.26555),
\qquad
L(\alpha)=0,
$$
with $\alpha\approx0.2655412194$.

Step 4: Exclude every other Hecke mode with one spectral certificate

Let $G=\operatorname{GL}_4(2)$. The commuting $G$- and $H_2(S_4)$-actions on chambers give the double-centralizer decomposition
$$
\mathbb{R}^{X}\cong\bigoplus_{\lambda\vdash4}V_{\lambda}\otimes S^{\lambda}.
$$
Every $D_p$ lies in the Hecke factor. The map $u\mapsto c_u$ from Step 2 is $G$-equivariant and injective. Since $G$ is $2$-transitive on the $15$ projective points, the mean-zero point module is irreducible of dimension $14$: its permutation character has inner product $2$ with itself, while the trivial constituent occurs once. The parabolic branching rule for the point action has Hecke side $S^{(4)}\oplus S^{(31)}$, so $W$ is the $V_{(31)}$ multiplicity space attached to one line in the three-dimensional module $S^{(31)}$.

Use the Young seminormal basis. If $t$ is a standard tableau and $d=c_t(i)-c_t(i+1)$, then at $q=2$
$$
T_i e_t=\frac{1}{1-2^{d}}e_t+b_d e_{s_i t},
\qquad
b_d^2=\frac{2(1-2^{d-1})(1-2^{d+1})}{(1-2^{d})^2},
$$
with the $e_{s_i t}$ term omitted when $s_i t$ is not standard. For $d=-1$ and $d=1$ this gives $T_i=2$ and $T_i=-1$. Put $x_r=r^{\alpha}$. Applying this formula to the standard tableaux of shapes $(31),(22),(211),(1111)$ and multiplying the three factors for $R(z)$ from Step 1 gives the complete nonconstant blocks below after replacing the coefficient of $z^r$ by $x_r$.

For the two noncritical directions in $S^{(31)}$,
$$
Q_{31}=\begin{pmatrix}
8x_2+10x_3+8x_4-16x_5-16x_6+5&4x_2+4x_3-8x_4\\
11x_2+14x_3-4x_4-24x_5+3&-2x_2-4x_3+4x_4+16x_5-16x_6+1
\end{pmatrix}.
$$
For $S^{(211)}$ there is one scalar direction
$$
L_{211}=-4x_2+3x_3+2x_4-6x_5+4x_6
$$
and a two-dimensional block
$$
Q_{211}=\begin{pmatrix}
7x_3-12x_4+10x_5-4x_6-2&2x_2+2x_3-4x_4\\
-2x_3+3x_4-2x_5+1&-3x_2-4x_3+6x_4+2x_5-4x_6+2
\end{pmatrix}.
$$
For $S^{(22)}$,
$$
Q_{22}=\begin{pmatrix}
\frac{4}{3}x_2-8x_3-\frac{26}{3}x_4+\frac{8}{3}x_5+8x_6+\frac{11}{3}&\frac{28}{9}x_2-\frac{14}{3}x_3-\frac{56}{9}x_4+\frac{56}{9}x_5+\frac{14}{9}\\
2x_2-3x_3-4x_4+4x_5+1&-\frac{13}{3}x_2+8x_3+\frac{8}{3}x_4-\frac{44}{3}x_5+8x_6-\frac{2}{3}
\end{pmatrix}.
$$
On $S^{(1111)}$ the scalar is
$$
S=-3+5x_2-6x_3+5x_4-3x_5+x_6.
$$
These formulas make the sign check reproducible from the seminormal action and the single product for $R(z)$.

From Step 3,
$$
\begin{aligned}
1.20208&<x_2<1.20210,&1.33873&<x_3<1.33876,\\
1.44501&<x_4<1.44504,&1.53322&<x_5<1.53325,\\
1.60927&<x_6<1.60931.
\end{aligned}
$$
Using $\operatorname{tr}Q=Q_{11}+Q_{22}$ and $\det Q=Q_{11}Q_{22}-Q_{12}Q_{21}$, interval arithmetic in the displayed entries gives
$$
\begin{array}{c|c|c}
\text{block}&\operatorname{tr}&\det\\
\hline
Q_{31}&(-12.914,-12.910)&(12.886,12.911)\\
Q_{211}&(-2.737,-2.734)&(1.497,1.501)\\
Q_{22}&(-1.928,-1.925)&(0.820,0.824)
\end{array}
$$
and
$$
-0.665<L_{211}<-0.664,
\qquad
-0.788<S<-0.787.
$$
Although the displayed matrices use convenient bases, each represents a restriction of the real symmetric operator $D_{\alpha}$, so its eigenvalues are real. A real $2\times2$ block with negative trace and positive determinant has two negative eigenvalues. Every noncritical Hecke direction is strictly negative, while the critical line in $S^{(31)}$ has eigenvalue $L(\alpha)=0$.

The only zero eigenvalue of $D_{\alpha}$ on $\mathbf{1}^{\perp}$ is therefore that critical line. Its multiplicity in the chamber space is $\dim V_{(31)}=14$, and Step 2 already supplies $14$ independent zero vectors. Therefore
$$
\ker(D_{\alpha}|_{\mathbf{1}^{\perp}})=W.
$$

Step 5: Read off the supremal negative type and equality dimension

Step 4 shows that $D_{\alpha}$ is negative semidefinite on $\mathbf{1}^{\perp}$, so $(X,d)$ has $\alpha$-negative type. If $p>\alpha$, then strict monotonicity from Step 3 gives $L(p)>0$; choosing any nonzero $c\in W$ yields
$$
c^T D_p c=L(p)\|c\|^2>0,
$$
so $p$-negative type fails. Therefore $\wp=\alpha$. Step 4 also gives $E=W$, so $\dim E=14$.

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

- finite building chamber metrics
- Iwahori-Hecke algebra
- Young seminormal representations
- conditional negative type
- double centralizer decomposition
