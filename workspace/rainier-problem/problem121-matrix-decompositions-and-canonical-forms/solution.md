## Steps

Step 1: Build a torsion quotient map from the incidence matrix

Write $B=B_n$, $M=M_n$, and set
$$
m=\binom{n}{2},\qquad d=n-1,\qquad \beta=m-n+1=\frac{(n-1)(n-2)}{2}.
$$
Each diagonal entry of $BB^T$ is $n-1$, and each off-diagonal entry is $1$, so
$$
BB^T=(n-2)I_n+J_n.
$$
Let
$$
L_0=nI_n-J_n.
$$
Then
$$
BM=2dB-BB^TB=L_0B,
$$
and, after transposing,
$$
MB^T=B^TL_0.
$$

We first determine the torsion of $\operatorname{coker}L_0$. Starting from $L_0=nI_n-J_n$, replace row $i$ by row $i$ minus row $1$ for $2\leq i\leq n$, replace column $1$ by the sum of all columns, replace column $j$ by column $j$ minus column $2$ for $3\leq j\leq n$, replace row $2$ by row $2+n\,\text{row }1$, and then replace row $2$ by the sum of rows $2,\ldots,n$. These unimodular operations reduce $L_0$, up to row and column permutations and a sign change, to
$$
\operatorname{diag}(1,\underbrace{n,\ldots,n}_{n-2},0).
$$
Therefore
$$
\operatorname{Tor}(\operatorname{coker}L_0)\cong(\mathbb{Z}_n)^{n-2}.
$$

The classes of the vectors $e_i-e_j$ generate this torsion subgroup. Indeed,
$$
L_0(e_i-e_j)=n(e_i-e_j),
$$
so their classes are torsion. After quotienting $\operatorname{coker}L_0$ by these classes, all coordinate vectors become equal and the remaining quotient is infinite cyclic, so it is torsion-free.

For distinct $i,j,k$, if $f_{ab}$ denotes the standard basis vector in $\mathbb{Z}^m$ indexed by $\{a,b\}$, then
$$
B(f_{ik}-f_{jk})=e_i-e_j.
$$
Therefore $B$ induces a surjection
$$
K:=\operatorname{Tor}(\operatorname{coker}M)\longrightarrow(\mathbb{Z}_n)^{n-2}.
$$
Let $H$ be its kernel. If $[x]\in H$, then $Bx=L_0y$ for some $y\in\mathbb{Z}^n$. Using $MB^T=B^TL_0$,
$$
2d[x]=[B^TBx]=[B^TL_0y]=[MB^Ty]=0.
$$
So every element of $H$ is killed by $2d$.

Step 2: Compute the order of the torsion subgroup

The eigenvalues of
$$
BB^T=(n-2)I_n+J_n
$$
are $2d$ on the all-ones vector and $n-2$ with multiplicity $n-1$. Since $B$ has rank $n$, the eigenvalues of $B^TB$ are
$$
2d\ (1),\qquad n-2\ (n-1),\qquad 0\ (m-n).
$$
Therefore the eigenvalues of $M=2dI_m-B^TB$ are
$$
0\ (1),\qquad n\ (n-1),\qquad 2d\ (m-n).
$$
In particular, $\ker M$ is the line spanned by the all-ones vector in $\mathbb{Q}^m$.

If the nonzero Smith factors of $M$ are $s_1,\ldots,s_{m-1}$, then $s_1\cdots s_{m-1}$ is the greatest common divisor of the maximal minors. Since $M$ has rank $m-1$ and both its left and right kernels are spanned by the primitive vector $\mathbf{1}$,
$$
\operatorname{adj}(M)=c\,\mathbf{1}\mathbf{1}^T
$$
for some integer $c$, so every nonzero maximal minor has absolute value $|c|$. In an orthonormal eigenbasis, the nonzero eigenvalue of $\operatorname{adj}(M)$ is the product of the nonzero eigenvalues of $M$, while $c\,\mathbf{1}\mathbf{1}^T$ has nonzero eigenvalue $cm$. Therefore
$$
|K|=|c|=\frac{n^{n-1}(2d)^{m-n}}{m}.
$$
Since $m=nd/2$ and $m-n-1=\beta-2$,
$$
|K|=4n^{n-2}(2d)^{\beta-2}.
$$
The quotient in Step 1 has order $n^{n-2}$, so
$$
|H|=4(2d)^{\beta-2}.
$$

Step 3: Determine the primary invariant factors of the kernel

We use a local Smith observation. Suppose an integer matrix $A$ has one-dimensional rational kernel, and an integer eigenvalue $\lambda\neq0$ has rational eigenspace of dimension $q$. If $\ell^a\mid\lambda$, then at least $q-1$ nonzero Smith factors of $A$ are divisible by $\ell^a$.

To see this, work over $\mathbb{Z}_\ell$ and let $E$ be the saturated rank-$q$ lattice in the $\lambda$-eigenspace. Since
$$
AE=\lambda E\subseteq\ell^a\mathbb{Z}_\ell^N,
$$
the image of $E/\ell E$ lies in
$$
A^{-1}(\ell^a\mathbb{Z}_\ell^N)/\ell\mathbb{Z}_\ell^N.
$$
In Smith coordinates this latter space has dimension one plus the number of nonzero Smith factors divisible by $\ell^a$. Since $E/\ell E$ has dimension $q$, the claim follows.

For $M$, the eigenvalue $2d$ has eigenspace dimension
$$
m-n=\beta-1.
$$
If $\ell^a\Vert2d$, at least $\beta-2$ nonzero Smith factors are divisible by $\ell^a$. Since $n$ is odd,
$$
\gcd(n,2d)=1,
$$
so every primary component for a prime dividing $2d$ lies in $H$.

For an odd prime $\ell\mid d$, the $\ell$-part of $|H|$ is exactly
$$
\ell^{a(\beta-2)}.
$$
The lower bound on the number of Smith factors forces
$$
H_\ell\cong(\mathbb{Z}_{\ell^a})^{\beta-2}.
$$

It remains to determine the extra $2$-primary factor. Modulo $2$,
$$
M\equiv B^TB.
$$
The equation $B^Ty=0$ says $y_i+y_j=0$ for every pair $\{i,j\}$, so
$$
\ker B^T=\langle\mathbf{1}\rangle
$$
and $\operatorname{rank}_{\mathbb{F}_2}B=n-1$. The image of $B$ is the even-coordinate-sum subspace of $\mathbb{F}_2^n$. Since $n$ is odd, $\mathbf{1}$ is not in this image. Therefore
$$
\ker(B^TB)=\ker B
$$
and
$$
\dim_{\mathbb{F}_2}\ker M=m-(n-1)=\beta.
$$
Because $\operatorname{coker}M\cong\mathbb{Z}\oplus K$,
$$
\dim_{\mathbb{F}_2}K/2K=\beta-1.
$$
The quotient $(\mathbb{Z}_n)^{n-2}$ has odd order, so the same dimension holds for $H/2H$.

If $2^a\Vert2d$, the $\beta-2$ forced factors account for $2^{a(\beta-2)}$ in $|H|$. The remaining $2$-primary order is $4$. Since $H/2H$ needs exactly one additional generator, this remaining factor is $\mathbb{Z}_4$, not $\mathbb{Z}_2\oplus\mathbb{Z}_2$. Combining all prime components gives
$$
H\cong(\mathbb{Z}_{2d})^{\beta-2}\oplus\mathbb{Z}_4.
$$

Step 4: Assemble the Smith normal form

Prime-by-prime decomposition of the exact sequence from Step 1 gives
$$
K\cong(\mathbb{Z}_{2d})^{\beta-2}\oplus\mathbb{Z}_4\oplus(\mathbb{Z}_n)^{n-2},
$$
because $\gcd(n,2d)=1$. Pair $n-2$ copies of $\mathbb{Z}_{2d}$ with the $\mathbb{Z}_n$ factors:
$$
\mathbb{Z}_{2d}\oplus\mathbb{Z}_n\cong\mathbb{Z}_{2dn}.
$$
The number of unpaired $\mathbb{Z}_{2d}$ factors is
$$
(\beta-2)-(n-2)=\beta-n=\frac{n^2-5n+2}{2}.
$$
Since $n$ is odd, $4\mid2(n-1)$, so these factors are already in divisibility order. Therefore
$$
K\cong
\mathbb{Z}_4\oplus
\mathbb{Z}_{2(n-1)}^{(n^2-5n+2)/2}\oplus
\mathbb{Z}_{2n(n-1)}^{n-2}.
$$

The matrix $M$ has rank $m-1$. The number of nontrivial finite invariant factors above is
$$
1+\frac{n^2-5n+2}{2}+(n-2)=\beta-1.
$$
So the number of unit Smith factors is
$$
(m-1)-(\beta-1)=n-1.
$$
The remaining Smith factor is $0$. Therefore the Smith normal form is
$$
I_{n-1}\oplus[4]\oplus
2(n-1)I_{(n^2-5n+2)/2}\oplus
2n(n-1)I_{n-2}\oplus[0].
$$
Final Answer: $\boxed{I_{n-1}\oplus[4]\oplus2(n-1)I_{(n^2-5n+2)/2}\oplus2n(n-1)I_{n-2}\oplus[0]}$

---

## Answer

$I_{n-1}\oplus[4]\oplus2(n-1)I_{(n^2-5n+2)/2}\oplus2n(n-1)I_{n-2}\oplus[0]$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Canonical form

---

## Solution Concepts

- Smith normal form
- incidence matrices
- local Smith invariants
- primary decomposition
- adjugate and eigenvalues

---

## Black-Box Audit — no issues found
