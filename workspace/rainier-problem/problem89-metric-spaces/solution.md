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
B_{u,v}=1_{\{u\cdot v=0\}}.
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
c_x=\left(x,-\frac{1}{\sqrt{2}}Bx\right),
\qquad x\in W.
$$
Thus zeros on the point side are zeros of $x$, while zeros on the line side are zeros of $Bx$.

For $v,u\in V$, define
$$
p_v=e_v-\frac{1}{7}\mathbf{1},
$$
and
$$
\ell_u=1_{\{v:u\cdot v=0\}}-\frac{3}{7}\mathbf{1}.
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

Step 4: Control the line vectors lying in a span of point vectors

Any six vectors among the seven $p_v$ are independent. Indeed, if a linear combination supported on at most six coordinates represents a constant vector, the omitted coordinate forces that constant to be zero, and then every coefficient vanishes.

For $S\subseteq V$ with $|S|=s\leq5$, let
$$
P_S=\operatorname{span}\{p_v:v\in S\},
\qquad
R=V\setminus S.
$$
A vector of $W$ belongs to $P_S$ exactly when all its coordinates on $R$ are equal. The vector $\ell_u$ has value $\frac{4}{7}$ on the three points of the line $L_u$ and $-\frac{3}{7}$ elsewhere. Hence
$$
\ell_u\in P_S
$$
exactly when either
$$
R\subseteq L_u
$$
or
$$
R\cap L_u=\varnothing.
$$

This gives the required line counts:

- if $s=1$ or $2$, no line vector lies in $P_S$;
- if $s=3$, there is one exactly when $S$ itself is a Fano line;
- if $s=4$, there is exactly one;
- if $s=5$, there are exactly three.

For $s=4$, if $R$ is a line it is the unique line containing $R$. If $R=\{a,b,c\}$ is not a line, then $a,b,c$ are a basis of $\mathbb{F}_2^3$, and
$$
\{a+b,a+c,b+c\}
$$
is the unique line disjoint from $R$. For $s=5$, the two points in $R$ lie on one common line, four lines meet exactly one of them, and the remaining two lines are disjoint from $R$, giving three in total.

Step 5: Determine every extremal flat size

Fix $0\leq k\leq5$ and a $k$-dimensional subspace $H\leq W$. Let
$$
a=|\{v:p_v\in H\}|,
\qquad
b=|\{u:\ell_u\in H\}|.
$$
Using the self-duality from Step 3, replace $H$ by $BH$ if necessary and assume
$$
a\geq b.
$$
Since any six point vectors are independent,
$$
a\leq k.
$$

If $a\leq k-1$, then
$$
a+b\leq2k-2.
$$
If $a=k$, the point vectors in $H$ span all of $H$, so Step 4 applies directly.

It follows that
$$
M_0=0,\qquad M_1=1,\qquad M_2=2,\qquad M_3=4,\qquad M_4\leq6,\qquad M_5\leq8.
$$
All these bounds are attained. For $M_3$, take the three point vectors on one Fano line together with that line vector.

For $M_4$, let $L$ be a Fano line, let $v\in L$, and let $L,M,N$ be the three lines through $v$. The three point vectors on $L$ are independent and span $\ell_L$. Adding $\ell_M$ raises the dimension to $4$. Also
$$
\ell_L+\ell_M+\ell_N=2p_v,
$$
so the same $4$-space contains the three point vectors on $L$ and all three line vectors through $v$, giving six elements of $\mathcal{A}$.

For $M_5$, take any five point vectors. They span a $5$-space, and Step 4 shows that exactly three line vectors lie in that span, giving eight elements.

Finally $M_6=14$. Therefore
$$
(M_0,M_1,M_2,M_3,M_4,M_5,M_6)
=(0,1,2,4,6,8,14).
$$

Step 6: Read off the generalized support hierarchy

Since
$$
d_r=14-M_{6-r},
$$
the six generalized support minima are
$$
(d_1,d_2,d_3,d_4,d_5,d_6)
=(6,8,10,12,13,14).
$$
Together with Step 2,
$$
\wp=\inf\{p>0:\sqrt{2}(3^p-1)>2^p\},
\qquad
\dim E=6.
$$

Final Answer: $\boxed{\left(\inf\{p>0:\sqrt{2}(3^p-1)>2^p\},6,(6,8,10,12,13,14)\right)}$

---

## Answer

$\left(\inf\{p>0:\sqrt{2}(3^p-1)>2^p\},6,(6,8,10,12,13,14)\right)$

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
