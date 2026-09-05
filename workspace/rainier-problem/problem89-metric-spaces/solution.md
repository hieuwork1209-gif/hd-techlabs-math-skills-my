## Steps

Step 1: Decompose the zero-sum space by the tree symmetries

Let $T$ be the complete rooted binary tree of height $3$. Its vertices are the binary words of lengths $0,1,2,3$, with an edge from a word to each one-letter extension. Thus the level sizes are
$$
1,2,4,8.
$$
Write
$$
a_k=k^p\qquad(2\le k\le6).
$$
The powered-distance matrix is invariant under every independent swap of the two children of an internal vertex.

Use these swaps to split the zero-sum space into mutually orthogonal invariant pieces:
- four leaf-pair contrast lines;
- two copies of a $2$-dimensional depth-$1$ contrast space;
- one $3$-dimensional root-contrast space;
- one $3$-dimensional radial zero-sum space.

The dimensions are
$$
4+2\cdot2+3+3=14,
$$
which is the full zero-sum dimension.

For $p=1$, the tree metric is a sum of edge-cut metrics. If $A_e$ is one side of the cut defined by an edge $e$, then for every zero-sum family $(c_x)$,
$$
\sum_{x,y}c_xc_y d(x,y)
=-2\sum_e\left(\sum_{x\in A_e}c_x\right)^2\le0.
$$
Moreover, for $0<p<1$,
$$
t^p=\frac{p}{\Gamma(1-p)}\int_0^\infty(1-e^{-st})s^{-p-1}\,ds.
$$
For a tree metric, $e^{-sd}$ is positive semidefinite because it is the entrywise product, over the edges, of the positive semidefinite kernels $e^{-s\delta_e}$ of the cut metrics. Hence $d^p$ is conditionally negative definite for every $0<p\le1$.

Step 2: Write the four symmetry blocks

A leaf-pair contrast vector has quadratic value
$$
-2a_2 t^2,
$$
so these four lines are always strictly negative.

For either depth-$1$ vertex, take as basis the contrast of its two child vertices and the contrast of the two corresponding pairs of leaves. The block is
$$
B_p=
\begin{pmatrix}
-2a_2&4-4a_3\\
4-4a_3&4a_2-8a_4
\end{pmatrix}.
$$

For the root-contrast space, use the differences between the left and right halves on levels $1,2,3$. The block is
$$
C_p=
\begin{pmatrix}
-2a_2&4-4a_3&8a_2-8a_4\\
4-4a_3&4a_2-8a_4&8a_3-16a_5+8\\
8a_2-8a_4&8a_3-16a_5+8&8a_2+16a_4-32a_6
\end{pmatrix}.
$$

Finally, let $r_j$ be $1$ on level $j$, $-2^j$ at the root, and $0$ elsewhere. In the basis $(r_1,r_2,r_3)$, the radial zero-sum block is
$$
R_p=
\begin{pmatrix}
2a_2-8&-8a_2+4a_3-4&8a_2-16a_3+8a_4-16\\
-8a_2+4a_3-4&-28a_2+8a_4&-32a_2-24a_3+16a_5+8\\
8a_2-16a_3+8a_4-16&-32a_2-24a_3+16a_5+8&8a_2-128a_3+16a_4+32a_6
\end{pmatrix}.
$$

Step 3: Isolate the only block that can become singular first

Apply Sylvester's criterion to the displayed blocks. Expanding the relevant principal minors as exponential polynomials and differentiating on
$$
1\le p\le\frac75
$$
gives the uniform bounds
$$
\det B_p>24,
$$
$$
\det C_p<-168,
$$
while the first two leading principal minors of $C_p$ have the alternating signs required for negative definiteness.

For the radial block, throughout the same interval,
$$
(R_p)_{11}<-2,
$$
$$
\det (R_p)_{\{1,2\}\times\{1,2\}}>7.
$$
Thus the sign of the full determinant
$$
\Delta(p)=\det R_p
$$
controls the first radial loss of negative definiteness.

The same direct differentiation gives
$$
\Delta'(p)>600
\qquad\left(1\le p\le\frac75\right).
$$
Also
$$
\Delta\left(\frac43\right)<-35,
$$
whereas
$$
\Delta\left(\frac75\right)>17.
$$
Therefore there is a unique
$$
\alpha\in\left(\frac43,\frac75\right)
$$
with
$$
\Delta(\alpha)=0.
$$
Numerically,
$$
\alpha\approx1.3743135549.
$$

Step 4: Determine the supremal negative type

For $1\le p<\alpha$, the leaf contrasts are strictly negative, both $B_p$ blocks are negative definite, $C_p$ is negative definite, and the three leading principal minors of $R_p$ have signs
$$
-,+,-.
$$
Hence the powered-distance form is negative definite on the zero-sum subspace.

At $p=\alpha$, the same statements remain strict except that
$$
\det R_\alpha=0.
$$
The first two radial leading minors are still nonzero, so $R_\alpha$ has a one-dimensional kernel and two negative eigenvalues.

For $p>\alpha$ sufficiently close to $\alpha$, the first two radial leading minors keep their signs while
$$
\det R_p>0,
$$
so $R_p$ has a positive direction. Thus negative type fails immediately above $\alpha$. Together with Step 1, this proves
$$
\wp=\alpha.
$$

Step 5: Compute the equality-space dimension

At $p=\alpha$, every nonradial symmetry block is strictly negative. The radial block has nullity exactly $1$. Consequently the equality space is precisely that radial kernel, so
$$
\dim E=1.
$$

Final Answer: $\boxed{(\alpha,1),\quad\alpha=\min\{p>1:\det R_p=0\}}$

---

## Answer

$(\alpha,1),\quad\alpha=\min\{p>1:\det R_p=0\}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- complete binary tree metrics
- hierarchical Haar symmetry decomposition
- conditional negative type
- Sylvester criterion on symmetry blocks
- radial boundary mode
