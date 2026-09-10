## Steps

Step 1: Compute the rational spectrum

Let
$$
m=\binom n2,\qquad N=n+m,
$$
and write $B=B_n$. The pair-incidence matrix satisfies
$$
BB^T=(n-2)I_n+J_n.
$$
Set
$$
L=\begin{pmatrix}
(2n-1)I_n-J_n&-B\\
-B^T&2nI_m-B^TB
\end{pmatrix}.
$$
Every row of $L$ sums to $0$.

Let
$$
U=\{x\in\mathbb Q^n:\mathbf1^Tx=0\}.
$$
For $x\in U$, put $w=B^Tx$. Since $J_nx=0$ and $BB^Tx=(n-2)x$, the span of $(x,0)$ and $(0,w)$ is $L$-invariant, with coefficient matrix
$$
R=\begin{pmatrix}
2n-1&-(n-2)\\
-1&n+2
\end{pmatrix}.
$$
Its eigenvalues are $n+1$ and $2n$. Thus each occurs with multiplicity $n-1$ on these standard subspaces. If $y\in\ker B$, then
$$
L(0,y)=(0,2ny),
$$
so $2n$ occurs another $m-n$ times. Finally, on the span of $(\mathbf1_n,0)$ and $(0,\mathbf1_m)$, the coefficient matrix is
$$
\begin{pmatrix}
n-1&-(n-1)\\
-2&2
\end{pmatrix},
$$
whose eigenvalues are $0$ and $n+1$. Hence
$$
\operatorname{Spec}(L)=\{0^1,(n+1)^n,(2n)^{m-1}\}.
$$
The rational kernel is the primitive all-ones line.

Step 2: Determine the torsion order and exponent

Let
$$
K=\operatorname{Tor}(\operatorname{coker}L).
$$
Since $L$ is symmetric of rank $N-1$ with primitive kernel vector $\mathbf1_N$, the product of its nonzero Smith factors is the common cofactor. Using the spectrum,
$$
|K|=\frac{(n+1)^n(2n)^{m-1}}{N}.
$$
Because
$$
N=\frac{n(n+1)}2,
$$
we get
$$
|K|=2^m n^{m-2}(n+1)^{n-1}.
$$

The spectrum also yields the integral identity
$$
L^2-(3n+1)L+2n(n+1)I_N=4J_N.
$$
Indeed the left side vanishes on both nonzero eigenspaces and equals $2n(n+1)$ on the all-ones line, while $2n(n+1)/N=4$.

The coordinate-sum map descends to $\operatorname{coker}L$ and kills torsion. Thus every torsion class has a representative $v$ with $\mathbf1_N^Tv=0$, and then $J_Nv=0$. Consequently
$$
2n(n+1)v=L\bigl((3n+1)I_N-L\bigr)v.
$$
Therefore the exponent of $K$ divides $2n(n+1)$.

Step 3: Determine the odd-primary components

Fix an odd prime $p$. Over $\mathbb F_p$, the map $B^T$ is injective: if $B^Tx=0$, then $x_i+x_j=0$ for every pair, and three distinct indices give $2x_i=0$, hence $x=0$.

Suppose first that $p\mid n$. Modulo $p$, the equations $L(x,y)=0$ are
$$
(-I-J)x-By=0,
$$
$$
-B^T(x+By)=0.
$$
Injectivity of $B^T$ gives $x=-By$. Substitution into the first equation gives $Jx=0$, equivalently $\mathbf1^Ty=0$ because $\mathbf1^TBy=2\mathbf1^Ty$. Hence
$$
\dim_{\mathbb F_p}\ker L=m-1.
$$
After removing the one-dimensional free kernel, the $p$-rank of $K$ is $m-2$. If $p^a\Vert n$, the exponent bound and the order formula force
$$
K_p\cong(\mathbb Z_{p^a})^{m-2}.
$$

Now suppose $p\mid n+1$. Then $n\equiv-1\pmod p$ and $2n$ is invertible. Put $z=By$ and $t=\mathbf1^Tx$. The first block equation gives
$$
z=-3x-t\mathbf1.
$$
The second gives
$$
2ny=B^T(x+z),
$$
so $x$ determines $y$ uniquely. Since
$$
BB^T\equiv-3I+J,
$$
one checks directly that applying $B$ to the displayed formula for $y$ recovers $z$. Thus every $x\in\mathbb F_p^n$ gives one kernel vector, so
$$
\dim_{\mathbb F_p}\ker L=n.
$$
Therefore the $p$-rank of $K$ is $n-1$. If $p^a\Vert n+1$, again the exponent bound and order give
$$
K_p\cong(\mathbb Z_{p^a})^{n-1}.
$$

Step 4: Determine the 2-primary component when $n$ is even

Write
$$
a=v_2(n)\ge1.
$$
First reduce modulo $2$. Since $n$ is even,
$$
L\equiv
\begin{pmatrix}
I+J&B\\
B^T&B^TB
\end{pmatrix}\pmod2.
$$
For a kernel vector $(x,y)$ put $z=x+By$. The equations become
$$
z+Jx=0,\qquad B^Tz=0.
$$
Over $\mathbb F_2$, $\ker B^T=\langle\mathbf1\rangle$, so $z=t\mathbf1$. Taking coordinate sums in $z=x+By$ gives $\mathbf1^Tx=0$ because $n$ is even and every column of $B$ has sum $2$. The first equation then forces $t=0$. Hence
$$
x=By,
$$
and $y\in\mathbb F_2^m$ is arbitrary. Thus
$$
\dim_{\mathbb F_2}\ker L=m.
$$
After removing the free kernel, exactly $m-1$ nonzero Smith factors are even.

It remains to locate their exact 2-adic valuations. Work over
$$
R=\mathbb Z/2^{a+1}\mathbb Z.
$$
Because $2n\equiv0$ in $R$, multiplying $L$ by the unit $-1$ shows that $Lv\equiv0\pmod{2^{a+1}}$ is equivalent to
$$
\begin{pmatrix}
I+J&B\\
B^T&B^TB
\end{pmatrix}
\binom{x}{y}=0.
$$
Again put $z=x+By$. Then
$$
z+Jx=0,\qquad B^Tz=0.
$$
The condition $B^Tz=0$ says $z_i+z_j=0$ for every pair. Using three indices gives
$$
z=c\mathbf1,\qquad 2c=0.
$$
Hence $c$ is either $0$ or $2^a$ in $R$. The first equation gives
$$
\mathbf1^Tx=-c.
$$
Writing $s=\mathbf1^Ty$ and using $x=c\mathbf1-By$, this is equivalent to
$$
2s=c(n+1)\pmod{2^{a+1}}.
$$
Therefore the reductions modulo $2$ of such vectors are exactly
$$
( B\bar y,\bar y),
$$
where $\bar y$ is arbitrary if $a=1$, while $\mathbf1^T\bar y=0$ if $a\ge2$. Their dimensions are respectively
$$
m\quad(a=1),\qquad m-1\quad(a\ge2).
$$

Now use Smith coordinates over $\mathbb Z_2$. If $r$ nonzero Smith factors are divisible by $2^{a+1}$, then the reduction modulo $2$ of
$$
\{v:Lv\in2^{a+1}\mathbb Z_2^N\}
$$
has dimension $1+r$, the extra $1$ coming from the zero Smith factor. Hence
$$
r=m-1\quad(a=1),\qquad r=m-2\quad(a\ge2).
$$
The exponent bound says no 2-primary factor exceeds $2^{a+1}$. Also
$$
v_2(|K|)=m+a(m-2).
$$
Combining this valuation with the fact that exactly $m-1$ nonzero factors are even forces, in every case,
$$
K_{(2)}\cong\mathbb Z_4\oplus(\mathbb Z_{2^{a+1}})^{m-2}.
$$
For $a=1$ this simply means $(\mathbb Z_4)^{m-1}$.

Step 5: Assemble the invariant factors

The odd part of $n$ occurs in exactly $m-2$ factors, and Step 4 supplies $m-2$ matching 2-primary factors of size $2^{a+1}$. Together they give $m-2$ factors divisible by
$$
2n.
$$
Among these, the odd primes dividing $n+1$ occur in exactly $n-1$ factors, producing
$$
2n(n+1)
$$
in the last $n-1$ positions. Thus the remaining $m-n-1$ of these factors are $2n$. The sole unpaired 2-primary factor is $4$.

Since $n$ is even,
$$
4\mid2n\mid2n(n+1),
$$
so these are already in divisibility order. There are $m-1$ nontrivial finite factors and one zero factor. As $L$ has size $N=n+m$, the remaining $n$ nonzero Smith factors are units. Therefore
$$
\operatorname{SNF}(L)=I_n\oplus[4]\oplus2nI_{m-n-1}\oplus2n(n+1)I_{n-1}\oplus[0].
$$
Final Answer: $\boxed{I_n\oplus[4]\oplus2nI_{m-n-1}\oplus2n(n+1)I_{n-1}\oplus[0]}$

---

## Answer

$I_n\oplus[4]\oplus2nI_{m-n-1}\oplus2n(n+1)I_{n-1}\oplus[0]$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Canonical form

---

## Solution Concepts

- Smith normal form
- block incidence matrices
- 2-adic lifting
- modular nullity
- spectral decomposition

---

## Black-Box Audit — no issues found

The hardening changes only the natural parity regime of the same canonical incidence matrix. For even $n$, the odd-degree shortcut available in the previous case disappears and the 2-primary structure changes from two order-$2$ corrections to one order-$4$ correction. The added difficulty is therefore a genuine 2-adic obstruction intrinsic to the matrix, not extra notation, tuned constants, or artificial casework.
