## Steps

Step 1: Compute the rational spectrum of the block matrix

Let
$$
m=\binom{n}{2},\qquad N=n+m,
$$
and write $B=B_n$. For the pair-incidence matrix,
$$
BB^T=(n-2)I_n+J_n.
$$
Define
$$
L=\begin{pmatrix}
(2n-1)I_n-J_n&-B\\
-B^T&2nI_m-B^TB
\end{pmatrix}.
$$
Every row of $L$ sums to $0$.

Let
$$
U=\{x\in\mathbb Q^n:\mathbf 1^Tx=0\}.
$$
For $x\in U$, put $w=B^Tx$. Since $J_nx=0$ and $BB^Tx=(n-2)x$, the subspace spanned by pairs $(x,0)$ and $(0,w)$ is $L$-invariant, and on the coefficient pair it acts by
$$
R=\begin{pmatrix}
2n-1&-(n-2)\\
-1&n+2
\end{pmatrix}.
$$
Its trace is $3n+1$ and its determinant is $2n(n+1)$, so its eigenvalues are
$$
n+1,\qquad 2n.
$$
Thus each occurs with multiplicity $n-1$ on these standard subspaces.

If $y\in\ker B$, then
$$
L(0,y)=(0,2ny),
$$
so $2n$ occurs with another multiplicity $m-n$. Finally, on the span of $(\mathbf 1_n,0)$ and $(0,\mathbf 1_m)$, the coefficient matrix is
$$
\begin{pmatrix}
n-1&-(n-1)\\
-2&2
\end{pmatrix},
$$
whose eigenvalues are $0$ and $n+1$. Hence the spectrum of $L$ is
$$
0\ (1),\qquad n+1\ (n),\qquad 2n\ (m-1).
$$
In particular, the rational kernel is exactly the line spanned by the primitive all-ones vector $\mathbf 1_N$.

Step 2: Determine the torsion order and a global exponent bound

Let
$$
K=\operatorname{Tor}(\operatorname{coker}L).
$$
Because $L$ is symmetric of rank $N-1$ with primitive left and right kernel vector $\mathbf 1_N$, one has
$$
\operatorname{adj}(L)=c\,\mathbf 1_N\mathbf 1_N^T
$$
for some integer $c$. The nonzero eigenvalue of the adjugate equals the product of the nonzero eigenvalues of $L$, whereas $c\mathbf 1_N\mathbf 1_N^T$ has nonzero eigenvalue $cN$. Therefore
$$
|K|=|c|=\frac{(n+1)^n(2n)^{m-1}}{N}.
$$
Since
$$
N=n+m=\frac{n(n+1)}2,
$$
this simplifies to
$$
|K|=2^m n^{m-2}(n+1)^{n-1}.
$$

The three rational eigenvalues also give an integral matrix identity. The matrix
$$
(L-(n+1)I_N)(L-2nI_N)
$$
vanishes on both nonzero eigenspaces and acts by $2n(n+1)$ on $\mathbf 1_N$. Since the projection onto the all-ones line is $J_N/N$ and $2n(n+1)/N=4$,
$$
L^2-(3n+1)L+2n(n+1)I_N=4J_N.
$$
Every torsion class has a representative $v$ with $\mathbf 1_N^Tv=0$, because the coordinate-sum map descends from $\operatorname{coker}L$ to $\mathbb Z$ and kills torsion. For such $v$, $J_Nv=0$, so
$$
2n(n+1)v=L\bigl((3n+1)I_N-L\bigr)v.
$$
Thus every element of $K$ is killed by
$$
2n(n+1).
$$

Step 3: Determine all odd-primary components

Fix an odd prime $p$. Over $\mathbb F_p$, the map $B^T$ is injective: if $B^Tx=0$, then $x_i+x_j=0$ for every pair $\{i,j\}$; using three distinct indices gives $2x_i=0$, hence $x=0$.

First suppose $p\mid n$. Modulo $p$ the block equations $L(x,y)=0$ become
$$
(-I-J)x-By=0,
$$
$$
-B^T(x+By)=0.
$$
Injectivity of $B^T$ gives
$$
x=-By.
$$
Substituting into the first equation gives $Jx=0$, so $\mathbf 1^Tx=0$. Since
$$
\mathbf 1^TBy=2\mathbf 1^Ty
$$
and $p$ is odd, this is equivalent to $\mathbf 1^Ty=0$. Therefore the kernel is parametrized by the codimension-one subspace of $\mathbb F_p^m$ with coordinate sum $0$, and
$$
\dim_{\mathbb F_p}\ker L=m-1.
$$
The one-dimensional rational kernel accounts for one of these dimensions, so the $p$-rank of $K$ is $m-2$.

If $p^a\Vert n$, Step 2 shows that the $p$-primary exponent divides $p^a$, while the order formula gives total $p$-valuation $a(m-2)$. Hence
$$
K_p\cong(\mathbb Z_{p^a})^{m-2}.
$$
Combining all odd primes dividing $n$ gives an $n$-primary contribution
$$
(\mathbb Z_n)^{m-2}.
$$

Now suppose $p\mid n+1$. Then $n\equiv-1\pmod p$, so $2n\not\equiv0$. Put $z=By$ and $t=\mathbf 1^Tx$. The first block equation gives
$$
z=-3x-t\mathbf 1.
$$
The second equation is
$$
2ny=B^T(x+z),
$$
so for a chosen $x$ it determines $y$ uniquely. It remains only to check that its image under $B$ is the displayed $z$. Since
$$
BB^T=(n-2)I+J\equiv-3I+J,
$$
and
$$
x+z=-2x-t\mathbf 1,
$$
one has
$$
\mathbf 1^T(x+z)=-t
$$
and hence
$$
BB^T(x+z)=6x+2t\mathbf 1=-2z.
$$
Because $2n\equiv-2$, applying $B$ to the formula for $y$ indeed gives $By=z$. Thus every $x\in\mathbb F_p^n$ produces exactly one kernel vector, so
$$
\dim_{\mathbb F_p}\ker L=n.
$$
Therefore the $p$-rank of $K$ is $n-1$. If $p^a\Vert n+1$, the exponent bound and the order formula force
$$
K_p\cong(\mathbb Z_{p^a})^{n-1}.
$$

Step 4: Determine the 2-primary component

Because $n$ is odd, modulo $2$ one has
$$
L\equiv
\begin{pmatrix}
I+J&B\\
B^T&B^TB
\end{pmatrix}.
$$
The equation $B^Tx=0$ says all coordinates of $x$ are equal, so
$$
\ker B^T=\langle\mathbf 1\rangle.
$$
Also, the image of $B$ is the even-coordinate-sum subspace of $\mathbb F_2^n$: every column has even coordinate sum, and $\operatorname{rank}B=n-1$.

For a kernel vector $(x,y)$ put $z=By$. The second block equation gives
$$
B^T(x+z)=0,
$$
so
$$
x+z=t\mathbf 1
$$
for some $t\in\mathbb F_2$. Since $z$ has even coordinate sum and $n$ is odd,
$$
\mathbf 1^Tx=t.
$$
The first block equation is then
$$
x+Jx+z=(x+z)+(\mathbf 1^Tx)\mathbf 1=0.
$$
Thus $y\in\mathbb F_2^m$ and $t\in\mathbb F_2$ are arbitrary, with $x$ determined by them. Hence
$$
\dim_{\mathbb F_2}\ker L=m+1,
$$
so
$$
\dim_{\mathbb F_2}K/2K=m.
$$
Therefore exactly $m$ nonzero Smith factors are even.

Write
$$
b=v_2(n+1).
$$
The exponent bound from Step 2 shows that no 2-primary invariant factor exceeds $2^{b+1}$. We now force $n-1$ factors to attain this largest power.

Let
$$
U_2=\{u\in\mathbb Z_2^n:\mathbf 1^Tu=0\}.
$$
For $u\in U_2$, define
$$
z_u=\bigl((n+2)u,\,B^Tu\bigr)\in\mathbb Z_2^{N}.
$$
Using $J_nu=0$ and $BB^Tu=(n-2)u$, a direct block multiplication gives
$$
Lz_u=\bigl(2n(n+1)u,0\bigr).
$$
Hence every $z_u$ lies in
$$
L^{-1}\bigl(2^{b+1}\mathbb Z_2^N\bigr).
$$
Modulo $2$, the map $u\mapsto z_u$ is injective because $n+2$ is odd. Its image has dimension $n-1$. The all-ones kernel vector is independent of this image modulo $2$, since its vertex part has odd coordinate sum whereas every $u\in U_2$ has even coordinate sum.

In Smith coordinates, if $r$ nonzero Smith factors are divisible by $2^{b+1}$, then the image modulo $2$ of
$$
L^{-1}\bigl(2^{b+1}\mathbb Z_2^N\bigr)
$$
has dimension $1+r$, the extra $1$ coming from the zero Smith factor. The preceding $n$ independent classes therefore give
$$
r\geq n-1.
$$

From the order formula,
$$
v_2(|K|)=m+b(n-1).
$$
There are exactly $m$ even nonzero factors, each contributes at least one power of $2$, and at least $n-1$ of them contribute at least $b+1$ powers. This already accounts for
$$
m+b(n-1)
$$
powers of $2$, exactly the total available. Therefore equality holds throughout:
$$
K_{(2)}\cong(\mathbb Z_2)^{m-n+1}\oplus(\mathbb Z_{2^{b+1}})^{n-1}.
$$

Step 5: Assemble the invariant factors

The odd primes dividing $n$ contribute
$$
(\mathbb Z_n)^{m-2}.
$$
The odd part of $n+1$ occurs in exactly $n-1$ factors, and Step 4 supplies $n-1$ 2-primary factors of size $2^{b+1}$. Pairing those components gives $n-1$ factors
$$
2n(n+1).
$$
The remaining $n$-parts pair with $m-n-1$ of the order-$2$ components, giving $m-n-1$ factors
$$
2n.
$$
Two order-$2$ components remain unpaired. Thus
$$
K\cong
\mathbb Z_2^2\oplus
\mathbb Z_{2n}^{m-n-1}\oplus
\mathbb Z_{2n(n+1)}^{n-1}.
$$
These are already in divisibility order.

There are $m$ nontrivial finite invariant factors and one zero factor. Since $L$ has size $N=n+m$, the remaining
$$
(N-1)-m=n-1
$$
nonzero Smith factors are units. Therefore
$$
\operatorname{SNF}(L)=
I_{n-1}\oplus2I_2\oplus2nI_{m-n-1}\oplus2n(n+1)I_{n-1}\oplus[0].
$$
Final Answer: $\boxed{I_{n-1}\oplus2I_2\oplus2nI_{m-n-1}\oplus2n(n+1)I_{n-1}\oplus[0]}$

---

## Answer

$I_{n-1}\oplus2I_2\oplus2nI_{m-n-1}\oplus2n(n+1)I_{n-1}\oplus[0]$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Canonical form

---

## Solution Concepts

- Smith normal form
- block incidence matrices
- primary decomposition
- modular nullity
- spectral decomposition

---

## Black-Box Audit — no issues found
