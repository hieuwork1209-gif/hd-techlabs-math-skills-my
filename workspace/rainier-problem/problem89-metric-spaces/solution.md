## Steps

Step 1: Derive the distance algebra and adjacency spectrum of the Heawood graph

Let
$$
V=\mathbb{F}_2^3\setminus\{0\}.
$$
Index both the point part and the line part by $V$, with a point $P_v$ adjacent to a line $L_u$ exactly when
$$
u\cdot v=0.
$$
Let $B$ be the $7\times7$ incidence matrix, so
$$
B_{u,v}=\mathbf{1}_{\{u\cdot v=0\}}.
$$
Each row contains three ones. For $u\neq v$, the equations
$$
u\cdot w=v\cdot w=0
$$
have exactly one nonzero solution $w$, whereas for $u=v$ there are three. Hence
$$
B^2=2I+J,
\qquad
B\mathbf{1}=3\mathbf{1}.
$$

With the point part first and the line part second, the adjacency matrix is
$$
A=
\begin{pmatrix}
0&B\\
B&0
\end{pmatrix}.
$$
Thus $A$ has eigenvalues $3,-3,\sqrt{2},-\sqrt{2}$, with multiplicities $1,1,6,6$. Indeed, on
$$
W=\{x\in\mathbb{R}^7:\langle x,\mathbf{1}\rangle=0\},
$$
one has $B^2=2I$, and the $\pm\sqrt{2}$ eigenspaces of $A$ are
$$
\left\{\left(x,\pm\frac{1}{\sqrt{2}}Bx\right):x\in W\right\}.
$$

Let $A_j$ be the distance-$j$ matrix. Since the graph has diameter $3$,
$$
A_1=A.
$$
Two vertices on the same side have one common neighbor, so
$$
A_2=A^2-3I.
$$
Also a vertex at distance $1$ has two neighbors at distance $2$ from the other endpoint, while a vertex at distance $3$ has three, giving
$$
AA_2=2A+3A_3.
$$
Therefore
$$
A_3=\frac{A^3-5A}{3}.
$$

Step 2: Determine the supremal negative type

Put
$$
q=2^p,\qquad r=3^p.
$$
The matrix of $d^p$ is
$$
D_p=A+qA_2+rA_3.
$$
On an adjacency eigenspace with eigenvalue $\lambda$, its eigenvalue is
$$
\mu_p(\lambda)
=\lambda+q(\lambda^2-3)+\frac{r}{3}(\lambda^3-5\lambda).
$$
For the three nonconstant adjacency eigenvalues,
$$
\mu_p(-3)=-3+6\cdot2^p-4\cdot3^p,
$$
$$
\mu_p(\sqrt{2})=\sqrt{2}(1-3^p)-2^p,
$$
and
$$
\mu_p(-\sqrt{2})=\sqrt{2}(3^p-1)-2^p.
$$

The middle expression is negative for every $p>0$. For the first, write $t=2^p$ and $\alpha=\log_2 3$. Since $3^2>2^3$, one has $\alpha>\frac{3}{2}$, and
$$
3+4t^\alpha-6t
$$
has derivative
$$
4\alpha t^{\alpha-1}-6>0
$$
for $t\geq1$. Its value at $t=1$ is $1$, so $\mu_p(-3)<0$ for every $p\geq0$.

Finally,
$$
f(p)=\sqrt{2}(3^p-1)-2^p
$$
is strictly increasing. In terms of $t=2^p$,
$$
f=\sqrt{2}(t^\alpha-1)-t,
$$
whose derivative is
$$
\sqrt{2}\alpha t^{\alpha-1}-1>0.
$$
Moreover $f(0)=-1$ and $f(1)=2\sqrt{2}-2>0$. Hence $f$ has a unique positive zero and
$$
\wp=\inf\{p>0:\sqrt{2}(3^p-1)>2^p\}.
$$
At $p=\wp$, the critical equality space is exactly the $-\sqrt{2}$ eigenspace, so
$$
\dim E=6.
$$

Step 3: Identify the critical equality space as a self-dual support code

Every vector in $E$ has the form
$$
c=\left(x,-\frac{1}{\sqrt{2}}Bx\right),
\qquad x\in W.
$$
Thus zeros on the point side are zeros of $x$, while zeros on the line side are zeros of $Bx$.

For $v,u\in V$, define
$$
p_v=e_v-\frac{1}{7}\mathbf{1},
$$
and
$$
\ell_u=\mathbf{1}_{\{v:u\cdot v=0\}}-\frac{3}{7}\mathbf{1}.
$$
For $x\in W$,
$$
x_v=\langle x,p_v\rangle,
\qquad
(Bx)_u=\langle x,\ell_u\rangle.
$$
Therefore, for an $r$-dimensional subspace $U\leq W$, the coordinates missing from the support of the corresponding subspace of $E$ are precisely
$$
\mathcal{A}\cap U^\perp,
\qquad
\mathcal{A}=\{p_v:v\in V\}\cup\{\ell_u:u\in V\}.
$$

Let
$$
M_k=\max_{\substack{H\leq W\\ \dim H=k}}|\mathcal{A}\cap H|.
$$
Then
$$
d_r=14-M_{6-r}.
$$

The configuration $\mathcal{A}$ is self-dual. Since $B$ is symmetric,
$$
Bp_v=\ell_v,
$$
and, because $B^2=2I$ on $W$,
$$
B\ell_v=2p_v.
$$
Thus the invertible map $B:W\to W$ swaps the two seven-element families up to nonzero scalars.

Step 4: Derive the quotient-trace lemma for Fano line vectors

Any six vectors among the seven $p_v$ are independent. Indeed, if a linear combination supported on at most six coordinates represents a constant vector, the omitted coordinate forces that constant to be zero, and then every coefficient vanishes.

For $S\subseteq V$ with $|S|=s\leq5$, let
$$
P_S=\operatorname{span}\{p_v:v\in S\},
\qquad
R=V\setminus S.
$$
Every vector in $P_S$ has equal coordinates on $R$. Conversely, the subspace of $W$ with equal coordinates on $R$ has dimension $s$, so it equals $P_S$.

The line vector $\ell_u$ has value $\frac{4}{7}$ on the three points of the Fano line $L_u$ and $-\frac{3}{7}$ elsewhere. Hence
$$
\ell_u\in P_S
$$
exactly when either
$$
R\subseteq L_u
\qquad\text{or}\qquad
R\cap L_u=\varnothing.
$$

To control one-dimensional extensions of $P_S$, restrict coordinates to $R$ and quotient by constant vectors. The class of $\ell_u$ is represented by the indicator of $L_u\cap R$. If $A,C$ are nonempty proper subsets of $R$, then the classes of $\mathbf{1}_A$ and $\mathbf{1}_C$ are proportional exactly when
$$
A=C
\qquad\text{or}\qquad
A=R\setminus C.
$$
Indeed, a relation
$$
\mathbf{1}_A=c\mathbf{1}_C+d\mathbf{1}_R
$$
with $c\neq0$ has two distinct values on $C$ and its complement, and these values must be $0$ and $1$.

Now use the Fano incidence rules. For $s=2$, no line vector lies in $P_S$; two distinct line traces cannot agree because the symmetric difference of two Fano lines has four points, and they cannot be complementary on the five-point set $R$, so the seven quotient classes are distinct. For $s=3$, if $S=L_u$ is a Fano line then $\ell_u\in P_S$, and the other six lines pair according to their common intersection point on $S$, giving three proportional pairs. If $S$ is not a line, equal traces are impossible and complementary traces would force $S$ to be the complement of the symmetric difference of two lines, which is itself a Fano line; hence all seven classes are distinct. For $s=4$, exactly one line vector lies in $P_S$; the other six form three proportional pairs, by equal singleton traces when $R$ is a line and by complementary traces when $R$ is not a line. For $s=5$, exactly three line vectors lie in $P_S$.

Step 5: Determine and count all extremal flats of the support configuration

Let $C_k$ be the number of $k$-dimensional subspaces attaining $M_k$. For a $k$-dimensional subspace $H\leq W$, put
$$
a=|\{v:p_v\in H\}|,
\qquad
b=|\{u:\ell_u\in H\}|.
$$
By the self-duality from Step 3, replace $H$ by $BH$ if necessary and assume $a\geq b$. Since any six point vectors are independent,
$$
a\leq k.
$$
If $a\leq k-1$, then
$$
a+b\leq2k-2.
$$

For $k=1$, the configuration has $14$ distinct projective points, so
$$
M_1=1,\qquad C_1=14.
$$
For $k=2$, the maximum is $M_2=2$. Every unordered pair of configuration points spans a unique extremal plane, and every extremal plane contains exactly that pair, so
$$
C_2=\binom{14}{2}=91.
$$

For $k=3$, the bound gives $M_3\leq4$. If $a=3$, then $H=P_S$, and Step 4 gives four configuration vectors exactly when $S$ is a Fano line. If $a=2$, equality would require $b=2$, but for $s=2$ a one-dimensional extension of $P_S$ contains at most one line vector. Thus the extremal $3$-spaces are the seven point-line spans and their seven duals. The two families are disjoint because their point/line counts are $(3,1)$ and $(1,3)$:
$$
M_3=4,
\qquad
C_3=14.
$$

For $k=4$, one has $M_4\leq6$. The case $a=4$ gives only one line vector, hence five configuration vectors. Equality therefore requires $a=b=3$. Step 4 shows that this happens exactly when the three point vectors form a Fano line and the extra dimension chooses one of the three proportional pairs of the remaining line vectors. Hence
$$
M_4=6,
\qquad
C_4=7\cdot3=21.
$$

For $k=5$, one has $M_5\leq8$. If $a=5$, then $H=P_S$ and Step 4 gives exactly three line vectors, so the bound is attained. If $a=4$, equality would require $b=4$, but a one-dimensional extension of $P_S$ contains the one line already in $P_S$ plus at most one proportional pair, so $b\leq3$. Thus the extremal $5$-spaces are the $\binom{7}{5}=21$ spans of five point vectors and their $21$ duals. The two families are disjoint because their point/line counts are $(5,3)$ and $(3,5)$:
$$
M_5=8,
\qquad
C_5=42.
$$

Finally
$$
M_0=0,\qquad C_0=1,
$$
and
$$
M_6=14,\qquad C_6=1.
$$
Therefore
$$
(M_0,\ldots,M_6)=(0,1,2,4,6,8,14)
$$
and
$$
(C_0,\ldots,C_6)=(1,14,91,14,21,42,1).
$$

Step 6: Read off the generalized support minima and their multiplicities

For an $r$-dimensional subspace $U\leq W$, the missing coordinates are $\mathcal{A}\cap U^\perp$. Orthogonal complementation is a bijection between $r$-spaces and $(6-r)$-spaces. Hence
$$
d_r=14-M_{6-r},
$$
and the number $n_r$ of $r$-dimensional subspaces attaining $d_r$ is
$$
n_r=C_{6-r}.
$$
Thus
$$
(d_1,d_2,d_3,d_4,d_5,d_6)
=(6,8,10,12,13,14)
$$
and
$$
(n_1,n_2,n_3,n_4,n_5,n_6)
=(42,21,14,91,14,1).
$$
Together with Step 2,
$$
\wp=\inf\{p>0:\sqrt{2}(3^p-1)>2^p\},
\qquad
\dim E=6.
$$

Final Answer: $\boxed{\left(\inf\{p>0:\sqrt{2}(3^p-1)>2^p\},6,(6,8,10,12,13,14),(42,21,14,91,14,1)\right)}$

---

## Answer

$\left(\inf\{p>0:\sqrt{2}(3^p-1)>2^p\},6,(6,8,10,12,13,14),(42,21,14,91,14,1)\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- negative type metrics
- distance-regular graph algebra
- Heawood graph spectrum
- generalized support weights
- Fano plane self-duality
