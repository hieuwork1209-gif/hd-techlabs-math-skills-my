## Steps

Step 1: Recover the primal Gram matrix from the normalized dual Gram matrix
Let
$$
G=(\langle v_i,v_j\rangle)_{1\le i,j\le n}.
$$
Because $(v_1,\dots,v_n)$ is a basis, $G$ is positive definite. The hypotheses give
$$
G_{ii}=1,
\qquad
|G_{ij}|=a\quad(i\ne j).
$$
If $(w_1,\dots,w_n)$ is the Euclidean dual basis, then its Gram matrix is
$$
H=G^{-1}.
$$
Put
$$
r_i=\|w_i\|,
\qquad
R=\operatorname{diag}(r_1,\dots,r_n),
$$
and let $C$ be the Gram matrix of the normalized dual vectors $z_i=w_i/r_i$. Then
$$
C=R^{-1}HR^{-1}=R^{-1}G^{-1}R^{-1}.
$$
Hence
$$
C^{-1}=RGR.
$$
Since $G_{ii}=1$,
$$
(C^{-1})_{ii}=r_i^2,
$$
and therefore
$$
\frac{(C^{-1})_{ij}}
{\sqrt{(C^{-1})_{ii}(C^{-1})_{jj}}}
=G_{ij}.
$$
Thus the absolute off-diagonal entries of the normalized inverse of $C$ are all equal to $a$.

Step 2: Use positive definiteness to determine the sign pattern of the dual correlations
By hypothesis,
$$
C_{ii}=1,
\qquad
C_{ij}=\frac{\varepsilon_{ij}}2
\quad(i\ne j),
$$
where each $\varepsilon_{ij}\in\{-1,1\}$ and $\varepsilon_{ij}=\varepsilon_{ji}$.

For any three distinct indices $i,j,k$, the corresponding principal $3\times3$ minor is
$$
\det
\begin{pmatrix}
1&\varepsilon_{ij}/2&\varepsilon_{ik}/2\\
\varepsilon_{ij}/2&1&\varepsilon_{jk}/2\\
\varepsilon_{ik}/2&\varepsilon_{jk}/2&1
\end{pmatrix}
=
\frac{1+\varepsilon_{ij}\varepsilon_{ik}\varepsilon_{jk}}4.
$$
Because $C$ is positive definite, every principal minor is positive. Hence
$$
\varepsilon_{ij}\varepsilon_{ik}\varepsilon_{jk}=1
$$
for every triple.

Fix
$$
\sigma_1=1,
\qquad
\sigma_i=\varepsilon_{1i}\quad(i>1).
$$
Applying the triangle relation to $1,i,j$ gives
$$
\varepsilon_{ij}=\sigma_i\sigma_j.
$$
Therefore, if
$$
D=\operatorname{diag}(\sigma_1,\dots,\sigma_n),
$$
then
$$
DCD=\frac12(I_n+J_n),
$$
where $J_n$ is the all-ones matrix.

Step 3: Invert the switched correlation matrix
Since
$$
(I_n+J_n)^{-1}=I_n-\frac1{n+1}J_n,
$$
we have
$$
(DCD)^{-1}
=2\left(I_n-\frac1{n+1}J_n\right).
$$
Its diagonal entries are
$$
\frac{2n}{n+1},
$$
and every off-diagonal entry is
$$
-\frac2{n+1}.
$$
Thus the absolute value of every off-diagonal entry after normalizing the inverse to have diagonal $1$ is
$$
\frac{2/(n+1)}{2n/(n+1)}=\frac1n.
$$
Conjugation by $D$ changes only signs, so the same absolute value holds for the normalized inverse of $C$. By Step 1,
$$
a=\frac1n.
$$

Step 4: Verify that the value is attainable
Consider
$$
G_0=\left(1+\frac1n\right)I_n-\frac1nJ_n.
$$
Its diagonal entries are $1$ and its off-diagonal entries are $-1/n$. On the line spanned by the all-ones vector its eigenvalue is
$$
\frac1n,
$$
and on its orthogonal complement its eigenvalue is
$$
1+\frac1n.
$$
Hence $G_0$ is positive definite, so it is the Gram matrix of a basis of unit vectors.

Moreover,
$$
G_0^{-1}=\frac{n}{n+1}(I_n+J_n).
$$
The diagonal entries of $G_0^{-1}$ are $2n/(n+1)$ and the off-diagonal entries are $n/(n+1)$. Therefore the normalized dual vectors have pairwise inner products of absolute value
$$
\frac{n/(n+1)}{2n/(n+1)}=\frac12.
$$
Thus the hypotheses are realizable with $a=1/n$.

Final Answer: $\boxed{\frac1n}$

---

## Answer

$\frac1n$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- dual bases and gram matrices
- correlation matrices
- principal minors and sign switching
- rank-one matrix inversion
- positive definite gram matrices
