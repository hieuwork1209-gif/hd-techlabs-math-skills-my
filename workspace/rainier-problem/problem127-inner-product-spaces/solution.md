## Steps

Step 1: Reduce the two projections to principal-angle parameters
Let $U=\operatorname{im}P$. The operator
$$
A=(PQP)|_{U}
$$
is self-adjoint and satisfies $0\leq A\leq I_{U}$. Choose an orthonormal eigenbasis $e_1,\dots,e_4$ of $U$, with
$$
Ae_i=x_i e_i,
\qquad 0\leq x_i\leq1.
$$
These $x_i$ are the squared cosines of the principal angles between $\operatorname{im}P$ and $\operatorname{im}Q$.

For $0<x_i<1$, write
$$
Qe_i=x_i e_i+\sqrt{x_i(1-x_i)}\,f_i,
$$
where $f_i\in U^{\perp}$ is a unit vector. If $i\neq j$, then
$$
\langle Qe_i,Qe_j\rangle
=\langle e_i,Qe_j\rangle
=\langle e_i,PQPe_j\rangle
=0,
$$
so the corresponding $f_i$ are orthogonal. Since $Q^2=Q$, on $\operatorname{span}\{e_i,f_i\}$ the matrices of $P$ and $Q$ are
$$
P_i=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
Q_i=
\begin{pmatrix}
x_i&\sqrt{x_i(1-x_i)}\\
\sqrt{x_i(1-x_i)}&1-x_i
\end{pmatrix}.
$$
The endpoint cases $x_i=0,1$ are obtained by the same orthogonal decomposition with the evident limiting blocks. Therefore
$$
\det(P_i+Q_i)=1-x_i,
$$
and hence
$$
\det(P+Q)=\prod_{i=1}^{4}(1-x_i).
$$

Also
$$
\operatorname{tr}(PQ)=\operatorname{tr}(PQP)=\sum_{i=1}^{4}x_i=2,
$$
and, because $PQP-\frac12P$ is supported on $U$ with eigenvalues $x_i-\frac12$,
$$
\sum_{i=1}^{4}\left(x_i-\frac12\right)^2=\frac25.
$$

Step 2: Convert the spectral constraints to a bounded product problem
Set
$$
z_i=1-x_i.
$$
Then $0\leq z_i\leq1$, and the two constraints become
$$
\sum_{i=1}^{4}z_i=2
$$
and
$$
\sum_{i=1}^{4}\left(z_i-\frac12\right)^2=\frac25.
$$
Expanding the second identity and using $\sum z_i=2$ gives
$$
\sum_{i=1}^{4}z_i^2=\frac75.
$$
Thus the original problem is equivalent to maximizing
$$
z_1z_2z_3z_4
$$
over $0\leq z_i\leq1$ subject to
$$
\sum z_i=2,
\qquad
\sum z_i^2=\frac75.
$$
There are feasible points with positive product, for example the two-value configuration found below, so a maximizer cannot have any $z_i=0$.

Step 3: Analyze maximizers with no coordinate on the upper boundary
Assume first that $0<z_i<1$ for every $i$. At an interior maximizer of the product, equivalently of $\sum_i\log z_i$, Lagrange multipliers give constants $\alpha,\beta$ such that
$$
\frac1{z_i}=\alpha+2\beta z_i
$$
for each $i$. Hence every $z_i$ is a root of the same quadratic
$$
2\beta t^2+\alpha t-1=0,
$$
so there are at most two distinct values.

A multiplicity split $1+3$ would have one value
$$
\frac12\pm\sqrt{\frac3{10}},
$$
because the deviations from $\frac12$ have sum $0$ and squared sum $\frac25$. One sign is greater than $1$ and the other is negative, so no $1+3$ interior configuration is feasible.

Thus the only interior possibility has multiplicities $2+2$. The two values are
$$
\frac12\pm\frac1{\sqrt{10}},
$$
which indeed have sum $2$ and squared sum $\frac75$. Their product is
$$
\left(\frac14-\frac1{10}\right)^2
=\frac9{400}.
$$

Step 4: Analyze the upper-boundary configuration
Now suppose a maximizer has a coordinate equal to $1$. Two coordinates cannot both equal $1$, because then $\sum z_i^2\geq2>\frac75$. After relabeling, let $z_1=1$. The remaining three positive numbers $a,b,c$ satisfy
$$
a+b+c=1,
\qquad
a^2+b^2+c^2=\frac25.
$$
We must maximize $abc$. An interior Lagrange-multiplier calculation for these three variables again shows that at most two distinct values occur. Since they cannot all be equal, two are equal. Write them as $u,u,v$. Then
$$
2u+v=1,
\qquad
2u^2+v^2=\frac25.
$$
Eliminating $v$ gives
$$
30u^2-20u+3=0,
$$
so
$$
u=\frac{10\pm\sqrt{10}}{30}.
$$
For
$$
u=\frac{10-\sqrt{10}}{30},
\qquad
v=\frac{5+\sqrt{10}}{15},
$$
the product is
$$
u^2v=\frac{35+\sqrt{10}}{1350}.
$$
The other sign gives
$$
\frac{35-\sqrt{10}}{1350},
$$
so the first boundary configuration is better. It also beats the only interior candidate, because
$$
\frac{35+\sqrt{10}}{1350}-\frac9{400}
=\frac{37+8\sqrt{10}}{10800}>0.
$$
Therefore
$$
\det(P+Q)\leq\frac{35+\sqrt{10}}{1350}.
$$

Step 5: Realize the maximizing spectral data
Let
$$
u=\frac{10-\sqrt{10}}{30},
\qquad
v=\frac{5+\sqrt{10}}{15},
$$
and choose
$$
(z_1,z_2,z_3,z_4)=(1,u,u,v).
$$
Set $x_i=1-z_i$. The identities in Step 4 give
$$
\sum_{i=1}^{4}x_i=2,
\qquad
\sum_{i=1}^{4}\left(x_i-\frac12\right)^2=\frac25.
$$
For each $i$, on an orthogonal two-dimensional block define
$$
P_i=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
Q_i=
\begin{pmatrix}
x_i&\sqrt{x_i(1-x_i)}\\
\sqrt{x_i(1-x_i)}&1-x_i
\end{pmatrix}.
$$
Each $P_i$ and $Q_i$ is a rank-one orthogonal projection. Taking the orthogonal direct sums of the four blocks produces rank-$4$ orthogonal projections $P,Q$ on $\mathbb{R}^{8}$ satisfying the two required constraints, and
$$
\det(P+Q)=\prod_{i=1}^{4}(1-x_i)=u^2v
=\frac{35+\sqrt{10}}{1350}.
$$
Thus the bound is attained.

Final Answer: $\boxed{\frac{35+\sqrt{10}}{1350}}$

---

## Answer

$\frac{35+\sqrt{10}}{1350}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- principal angles between subspaces
- orthogonal projections
- spectral theorem
- lagrange multipliers
- constrained product optimization
