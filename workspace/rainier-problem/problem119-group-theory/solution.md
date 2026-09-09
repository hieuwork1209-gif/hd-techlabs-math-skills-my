## Steps

Step 1: Relate the triangular-graph Laplacian to the complete-graph Laplacian

Let $n\geq5$ be odd, let
$$
m=\binom{n}{2},\qquad d=n-1,\qquad \beta=m-n+1=\frac{(n-1)(n-2)}{2},
$$
and let $T_n=L(K_n)$ be the triangular graph. Let $B$ be the unsigned $n\times m$ vertex-edge incidence matrix of $K_n$. Since two edges of $K_n$ meet in one vertex exactly when the corresponding vertices of $T_n$ are adjacent,
$$
B^TB=2I+A(T_n).
$$
The Laplacian of $T_n$ is
$$
L=2(n-2)I-A(T_n)=2dI-B^TB.
$$
Also
$$
BB^T=(n-2)I+J.
$$
If
$$
L_0=nI-J
$$
is the Laplacian of $K_n$, then
$$
BL=L_0B.
$$
So $B$ induces a homomorphism from the torsion subgroup of $\operatorname{coker}L$, namely $K(T_n)$, to $K(K_n)$.

To determine $K(K_n)$ explicitly, delete the same row and column from $L_0$. The resulting $(n-1)\times(n-1)$ matrix has diagonal entries $n-1$ and off-diagonal entries $-1$. For each $i\geq2$, replace row $i$ by row $i$ minus row $1$. Then add columns $2,\ldots,n-1$ to column $1$, and finally add column $1$ to each column $2,\ldots,n-1$. These unimodular operations give
$$
\operatorname{diag}(1,n,\ldots,n),
$$
with $n$ repeated $n-2$ times. Therefore
$$
K(K_n)\cong(\mathbb{Z}_n)^{n-2}.
$$
The induced map is surjective: for distinct $i,j,k$,
$$
B(e_{ik}-e_{jk})=e_i-e_j,
$$
and such differences generate the torsion of $\operatorname{coker}L_0$.

Let $H$ be the kernel. If $[x]\in H$, then $Bx=L_0y$ for some integral $y$. Using $LB^T=B^TL_0$,
$$
2d[x]=[B^TBx]=[B^TL_0y]=[LB^Ty]=0.
$$
So every element of $H$ is killed by $2d$.

Step 2: Compute the order of the kernel

The matrix $BB^T=(n-2)I+J$ has eigenvalue $2d$ on the all-ones vector and eigenvalue $n-2$ with multiplicity $n-1$. So $B^TB$ has eigenvalues
$$
2d\ (1),\qquad n-2\ (n-1),\qquad 0\ (m-n).
$$
So $L=2dI-B^TB$ has eigenvalues
$$
0\ (1),\qquad n\ (n-1),\qquad 2d\ (m-n).
$$
By the matrix-tree theorem,
$$
|K(T_n)|=\frac{n^{n-1}(2d)^{m-n}}{m}.
$$
Since $m=nd/2$ and $m-n-1=\beta-2$,
$$
|K(T_n)|=4n^{n-2}(2d)^{\beta-2}.
$$
Because the map onto $K(K_n)$ is surjective,
$$
|H|=4(2d)^{\beta-2}.
$$

Step 3: Determine the primary structure of $H$

We use the following elementary local Smith observation. Suppose an integral matrix $M$ has one-dimensional rational kernel, and an integer eigenvalue $\lambda\neq0$ has rational eigenspace of dimension $q$. If $\ell^a\mid\lambda$, then at least $q-1$ invariant factors of the torsion of $\operatorname{coker}M$ are divisible by $\ell^a$.

Indeed, over $\mathbb{Z}_\ell$, let $E$ be the saturated rank-$q$ lattice in that eigenspace. Since $ME=\lambda E\subseteq\ell^a\mathbb{Z}_\ell^N$, the reduction of $E$ modulo $\ell$ lies in
$$
M^{-1}(\ell^a\mathbb{Z}_\ell^N)/\ell\mathbb{Z}_\ell^N.
$$
In Smith coordinates this space has dimension one plus the number of nonzero Smith entries divisible by $\ell^a$. Since $E/\ell E$ has dimension $q$, the claim follows.

Apply this to $L$ and its eigenvalue $2d$, whose eigenspace has dimension
$$
m-n=\beta-1.
$$
If $\ell^a\Vert2d$, at least $\beta-2$ invariant factors are divisible by $\ell^a$. Since $n$ is odd and $\gcd(n,2d)=1$, all such primary torsion lies in $H$.

For an odd prime $\ell\mid d$, the $\ell$-part of $|H|$ is exactly
$$
\ell^{a(\beta-2)}.
$$
The lower bound forces
$$
H_\ell\cong(\mathbb{Z}_{\ell^a})^{\beta-2}.
$$

It remains to determine the extra $2$-primary factor. Over $\mathbb{F}_2$ we have
$$
L\equiv B^TB.
$$
The incidence matrix $B$ has rank $n-1$. Also,
$$
\ker B^T=\langle\mathbf{1}\rangle,
$$
while every vector in $\operatorname{im}B$ has even coordinate sum; because $n$ is odd, $\mathbf{1}\notin\operatorname{im}B$. So
$$
\ker(B^TB)=\ker B
$$
and
$$
\dim_{\mathbb{F}_2}\ker L=m-(n-1)=\beta.
$$
Since $\operatorname{coker}L\cong\mathbb{Z}\oplus K(T_n)$,
$$
\dim_{\mathbb{F}_2}K(T_n)/2K(T_n)=\beta-1.
$$
The quotient $K(K_n)$ has odd order, so the same dimension holds for $H/2H$.

If $2^a\Vert2d$, the $\beta-2$ full-size factors already contribute $2^{a(\beta-2)}$, while the remaining $2$-part of $|H|$ is $4$. Since $H/2H$ has exactly $\beta-1$ generators, this remainder is one cyclic factor $\mathbb{Z}_4$, not two copies of $\mathbb{Z}_2$. Combining all primes by the Chinese remainder theorem gives
$$
H\cong(\mathbb{Z}_{2d})^{\beta-2}\oplus\mathbb{Z}_4.
$$

Step 4: Split the coprime parts and put the answer in invariant-factor form

The exact sequence
$$
0\longrightarrow H\longrightarrow K(T_n)\longrightarrow(\mathbb{Z}_n)^{n-2}\longrightarrow0
$$
splits prime-by-prime because $\gcd(n,2d)=1$. So
$$
K(T_n)\cong(\mathbb{Z}_{2d})^{\beta-2}\oplus\mathbb{Z}_4\oplus(\mathbb{Z}_n)^{n-2}.
$$
Pair $n-2$ of the $\mathbb{Z}_{2d}$ factors with the $\mathbb{Z}_n$ factors. Since $\gcd(n,2d)=1$,
$$
\mathbb{Z}_{2d}\oplus\mathbb{Z}_n\cong\mathbb{Z}_{2dn}.
$$
There remain
$$
(\beta-2)-(n-2)=\beta-n=\frac{n^2-5n+2}{2}
$$
factors of order $2d=2(n-1)$. So
$$
K(T_n)\cong
\mathbb{Z}_4\oplus
\mathbb{Z}_{2(n-1)}^{\oplus(n^2-5n+2)/2}\oplus
\mathbb{Z}_{2n(n-1)}^{\oplus(n-2)}.
$$

Final Answer: $\boxed{\mathbb{Z}_4\oplus\mathbb{Z}_{2(n-1)}^{(n^2-5n+2)/2}\oplus\mathbb{Z}_{2n(n-1)}^{n-2}}$

---

## Answer

$\mathbb{Z}_4\oplus\mathbb{Z}_{2(n-1)}^{(n^2-5n+2)/2}\oplus\mathbb{Z}_{2n(n-1)}^{n-2}$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Canonical form

---

## Solution Concepts

- critical groups and Smith normal form
- unsigned incidence matrices
- matrix-tree theorem
- local Smith invariants
- Sylow decomposition

---

## Black-Box Audit — no issues found