## Steps

Step 1: Translate the basis and dual-basis norm conditions into a Gram-matrix problem
Let
$$
V=[v_1\ v_2\ v_3\ v_4]
$$
and let
$$
G=V^TV.
$$
Because the $v_i$ are unit vectors,
$$
G_{ii}=1
$$
for every $i$. If $W=[w_1\ w_2\ w_3\ w_4]$ is the matrix of the dual basis, then
$$
V^TW=I_4,
$$
so
$$
W=V^{-T}.
$$
Hence the Gram matrix of the dual basis is
$$
W^TW=V^{-1}V^{-T}=G^{-1}.
$$
The conditions $\|w_i\|=\sqrt2$ therefore give
$$
(G^{-1})_{ii}=2
$$
for every $i$.

Let $\lambda_1,\dots,\lambda_4>0$ be the eigenvalues of $G$. Taking traces yields
$$
\sum_{i=1}^4\lambda_i=\operatorname{tr}G=4
$$
and
$$
\sum_{i=1}^4\frac1{\lambda_i}=\operatorname{tr}(G^{-1})=8.
$$
Moreover
$$
|\det V|^2=\det G=\prod_{i=1}^4\lambda_i.
$$
Thus it remains to maximize the product of four positive numbers with the two displayed spectral constraints.

Step 2: Determine the possible spectra at a product maximizer
The constraints imply $\lambda_i\leq4$ and $\lambda_i\geq1/8$, so the feasible spectral set is compact. At a maximizer of
$$
\sum_{i=1}^4\log\lambda_i,
$$
Lagrange multipliers give constants $\alpha,\beta$ such that
$$
\frac1{\lambda_i}=\alpha-\frac{\beta}{\lambda_i^2}
$$
for every $i$. Multiplying by $\lambda_i^2$ shows that every $\lambda_i$ is a root of the same quadratic
$$
\alpha t^2-t-\beta=0.
$$
Hence a maximizing spectrum has at most two distinct values.

If the multiplicities are $2+2$, write the two values as $a,b$. Then
$$
a+b=2,
\qquad
\frac1a+\frac1b=4.
$$
Thus $ab=1/2$, so
$$
\det G=a^2b^2=\frac14.
$$

For a $1+3$ split, let $a$ have multiplicity $1$ and $b$ multiplicity $3$. The constraints become
$$
a+3b=4,
\qquad
\frac1a+\frac3b=8.
$$
Eliminating $a$ gives
$$
6b^2-10b+3=0,
$$
so
$$
b=\frac{5\pm\sqrt7}{6},
\qquad
a=\frac{3\mp\sqrt7}{2}.
$$
The corresponding products are
$$
\frac{29+4\sqrt7}{108}
\qquad\text{and}\qquad
\frac{29-4\sqrt7}{108}.
$$
Since
$$
\frac{29+4\sqrt7}{108}>\frac14>\frac{29-4\sqrt7}{108},
$$
the largest possible spectral product is
$$
\det G\leq\frac{29+4\sqrt7}{108}.
$$

Step 3: Show that the maximizing spectrum is compatible with both diagonal conditions
Set
$$
a=\frac{3-\sqrt7}{2},
\qquad
b=\frac{5+\sqrt7}{6},
$$
and let
$$
u=\frac12(1,1,1,1)^T.
$$
Define
$$
G=bI_4+(a-b)uu^T.
$$
Then $G$ has eigenvalue $a$ in the direction of $u$ and eigenvalue $b$ on $u^\perp$, so it has exactly the maximizing spectrum from Step 2.

Because every coordinate of $u$ has squared value $1/4$,
$$
G_{ii}=b+\frac{a-b}{4}=\frac{a+3b}{4}=1.
$$
Also
$$
G^{-1}=\frac1b I_4+\left(\frac1a-\frac1b\right)uu^T,
$$
so
$$
(G^{-1})_{ii}
=\frac1b+\frac14\left(\frac1a-\frac1b\right)
=\frac14\left(\frac1a+\frac3b\right)
=2.
$$
Thus the spectral optimizer is not merely formal: it is realized by a positive definite Gram matrix satisfying both the primal and dual norm constraints.

Step 4: Realize the Gram matrix by a basis and evaluate the maximum volume
Since $G$ is positive definite with diagonal entries $1$, choose an invertible matrix $V$ with
$$
V^TV=G.
$$
Its columns $v_1,\dots,v_4$ form a basis of unit vectors. For the dual basis matrix $W=V^{-T}$,
$$
W^TW=G^{-1},
$$
whose diagonal entries are all $2$, so every dual vector has norm $\sqrt2$.

Therefore equality is attained, and
$$
|\det V|
=\sqrt{\det G}
=\sqrt{\frac{29+4\sqrt7}{108}}.
$$
Since
$$
29+4\sqrt7=(1+2\sqrt7)^2,
$$
this becomes
$$
|\det V|=\frac{1+2\sqrt7}{6\sqrt3}.
$$

Final Answer: $\boxed{\frac{1+2\sqrt7}{6\sqrt3}}$

---

## Answer

$\frac{1+2\sqrt7}{6\sqrt3}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- dual bases
- gram matrices
- inverse gram matrices
- eigenvalue optimization
- lagrange multipliers
