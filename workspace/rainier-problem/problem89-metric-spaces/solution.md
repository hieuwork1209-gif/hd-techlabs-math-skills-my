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
Thus all distance shells are obtained from one three-factor expression.

Step 2: Construct the critical eigenspace

Let $\mathcal{P}$ and $\mathcal{H}$ be the $15$ points and $15$ planes of $\operatorname{PG}(3,2)$. For a mean-zero function $u:\mathcal{P}\to\mathbb{R}$, define
$$
c_u(P,L,H)=u(P)-\frac{1}{2}\sum_{Q\subset H}u(Q).
$$
Let $N$ be the point-plane incidence matrix. Every point is contained in $7$ planes and two distinct points are contained in exactly $3$ common planes, hence
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
has dimension $14$ and lies in $\mathbf{1}^\perp$.

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
R(z)h\equiv(1+3z+2z^2-6z^3-16z^4+16z^6)h
$$
modulo the constant vector. Hence every $c_u\in W$ satisfies
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
Thus $L'$ is increasing and positive, so $L$ is strictly increasing on $[0,\infty)$. Outward-rounded evaluation gives
$$
L(0.26554)<-8.4\cdot10^{-6},
\qquad
L(0.26555)>6.0\cdot10^{-5}.
$$
Consequently there is a unique root
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
Every $D_p$ lies in the Hecke factor. The map $u\mapsto c_u$ from Step 2 is $G$-equivariant and injective. Since $G$ is $2$-transitive on the $15$ projective points, the mean-zero point module is irreducible of dimension $14$: its permutation character has inner product $2$ with itself, while the trivial constituent occurs once. Thus $W$ is the $V_{(31)}$ multiplicity space attached to one line in the three-dimensional Hecke module $S^{(31)}$.

It remains only to determine the sign on the other Hecke directions. Use the orthonormal Young seminormal basis. If $t$ is a standard tableau and $d=c_t(i)-c_t(i+1)$ is the content difference, then at $q=2$
$$
T_i e_t=\frac{1}{1-2^{d}}e_t+b_d e_{s_i t},
\qquad
b_d^2=\frac{2(1-2^{d-1})(1-2^{d+1})}{(1-2^{d})^2},
$$
where the $e_{s_i t}$ term is omitted when $s_i t$ is not standard. For $d=-1$ and $d=1$ this gives respectively $T_i=2$ and $T_i=-1$. Hence the same three-factor formula for $R(z)$ in Step 1 produces every block $M_{\lambda}(p)$ without introducing separate representations.

From the bracket in Step 3,
$$
\begin{aligned}
1.20208&<2^{\alpha}<1.20210,&1.33873&<3^{\alpha}<1.33876,\\
1.44501&<4^{\alpha}<1.44504,&1.53322&<5^{\alpha}<1.53325,\\
1.60927&<6^{\alpha}<1.60931.
\end{aligned}
$$
Substitution into this single seminormal recipe gives a short sign certificate. Let $M_{(31)}^{\mathrm{res}}$ denote the restriction to the two directions of $S^{(31)}$ orthogonal to the critical line. The displayed power intervals give
$$
-13<\operatorname{tr}M_{(31)}^{\mathrm{res}}<-12.8,
\qquad
\det M_{(31)}^{\mathrm{res}}>12.8.
$$
Because this restriction is self-adjoint, its two eigenvalues are real; negative trace and positive determinant force both to be negative. For the other two nontrivial blocks use the elementary Gershgorin bound: if $M=(m_{ij})$ is real symmetric, every eigenvalue is at most
$$
\max_i\left(m_{ii}+\sum_{j\ne i}|m_{ij}|\right).
$$
The same substitution into the seminormal formula gives this upper bound $<-0.60$ on $S^{(22)}$ and $<-0.29$ on $S^{(211)}$. On $S^{(1111)}$ each $T_i=-1$, and direct substitution into the factorized shells gives the scalar value $<-0.78$. Thus every noncritical Hecke direction is strictly negative.

Therefore the only zero eigenvalue of $D_\alpha$ on $\mathbf{1}^\perp$ is the critical line in $S^{(31)}$. Its multiplicity in the chamber space is $\dim V_{(31)}=14$, and Step 2 already supplies $14$ independent zero vectors. Hence
$$
\ker(D_\alpha|_{\mathbf{1}^\perp})=W.
$$

Step 5: Read off the supremal negative type and equality dimension

Step 4 shows that $D_\alpha$ is negative semidefinite on $\mathbf{1}^\perp$, so $(X,d)$ has $\alpha$-negative type. If $p>\alpha$, then strict monotonicity from Step 3 gives $L(p)>0$; choosing any nonzero $c\in W$ yields
$$
c^T D_p c=L(p)\|c\|^2>0,
$$
so $p$-negative type fails. Therefore $\wp=\alpha$. Step 4 also gives $E=W$, hence $\dim E=14$.

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
