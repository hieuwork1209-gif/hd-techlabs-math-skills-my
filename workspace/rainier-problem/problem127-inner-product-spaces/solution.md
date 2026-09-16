## Steps

Step 1: Translate the basis conditions into Gram-matrix constraints
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
for every $i$. If $W=[w_1\ w_2\ w_3\ w_4]$ is the matrix of the Euclidean dual basis, then
$$
V^TW=I_4,
$$
so $W=V^{-T}$ and therefore
$$
W^TW=G^{-1}.
$$
The conditions $\|w_i\|=\sqrt2$ give
$$
(G^{-1})_{ii}=2
$$
for every $i$. Hence
$$
\operatorname{tr}G=4,
\qquad
\operatorname{tr}(G^{-1})=8.
$$

Let
$$
x=\frac12(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4)^T,
\qquad
y=\frac12(\eta_1,\eta_2,\eta_3,\eta_4)^T.
$$
Since the entries are signs and $\sum_i\varepsilon_i\eta_i=0$, the vectors $x,y$ are orthonormal. Moreover
$$
\left\|\sum_{i=1}^4\varepsilon_i v_i\right\|^2=4x^TGx,
\qquad
\left\|\sum_{i=1}^4\eta_i v_i\right\|^2=4y^TGy.
$$
Thus the target equals
$$
4\sqrt{(x^TGx)(y^TGy)}.
$$

Step 2: Bound the two signed-sum directions by the top two eigenvalues
Let the eigenvalues of $G$ be
$$
\lambda_1\geq\lambda_2\geq\lambda_3\geq\lambda_4>0.
$$
Because $x,y$ are orthonormal, the Ky Fan variational principle gives
$$
x^TGx+y^TGy\leq\lambda_1+\lambda_2.
$$
Using the arithmetic-geometric mean inequality,
$$
4\sqrt{(x^TGx)(y^TGy)}
\leq2\bigl(x^TGx+y^TGy\bigr)
\leq2(\lambda_1+\lambda_2).
$$
It remains to maximize the sum of the two largest eigenvalues under the trace constraints from Step 1.

Step 3: Optimize the top-two spectral sum
Set
$$
A=\lambda_1+\lambda_2,
\qquad
B=\lambda_3+\lambda_4=4-A.
$$
Since the first two eigenvalues are the larger pair, $A\geq2$. By Cauchy-Schwarz applied separately to the two pairs,
$$
\frac1{\lambda_1}+\frac1{\lambda_2}\geq\frac4A,
\qquad
\frac1{\lambda_3}+\frac1{\lambda_4}\geq\frac4B.
$$
Therefore
$$
8=\sum_{i=1}^4\frac1{\lambda_i}
\geq\frac4A+\frac4{4-A}.
$$
Equivalently,
$$
A(4-A)\geq2.
$$
Since $A\geq2$, this implies
$$
A\leq2+\sqrt2.
$$
Combining this with Step 2 yields
$$
\left\|\sum_{i=1}^4\varepsilon_i v_i\right\|
\left\|\sum_{i=1}^4\eta_i v_i\right\|
\leq4+2\sqrt2.
$$

Step 4: Construct a Gram matrix attaining equality
Let
$$
a=1+\frac1{\sqrt2},
\qquad
b=1-\frac1{\sqrt2},
$$
and let $P$ be the orthogonal projection onto $\operatorname{span}\{x,y\}$. Because every coordinate of both $x$ and $y$ has squared value $1/4$,
$$
P_{ii}=x_i^2+y_i^2=\frac12
$$
for every $i$.

Define
$$
G=aP+b(I_4-P).
$$
Then $G$ is positive definite and
$$
G_{ii}=\frac{a+b}{2}=1.
$$
Also
$$
G^{-1}=\frac1aP+\frac1b(I_4-P).
$$
Since $a+b=2$ and $ab=1/2$,
$$
\frac1a+\frac1b=4,
$$
so
$$
(G^{-1})_{ii}=\frac12\left(\frac1a+\frac1b\right)=2.
$$
Thus $G$ is the Gram matrix of a basis satisfying both the primal and dual norm conditions.

Finally, $x$ and $y$ lie in the $a$-eigenspace of $G$, so
$$
x^TGx=y^TGy=a.
$$
Hence the target value is
$$
4a=4+2\sqrt2,
$$
and the bound is attained.

Final Answer: $\boxed{4+2\sqrt2}$

---

## Answer

$4+2\sqrt2$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- dual bases
- gram matrices
- ky fan variational principle
- reciprocal eigenvalue constraints
- orthogonal projections
