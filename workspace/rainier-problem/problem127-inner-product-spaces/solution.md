## Steps

Step 1: Convert the constant-angle conditions into skew complex structures
For an orthogonal transformation $T$ satisfying
$$
\langle x,Tx\rangle=c\|x\|^2
$$
for every $x$, polarization gives
$$
T+T^T=2cI_4.
$$
Set
$$
s=\sqrt{1-c^2}
$$
and, for each $i$,
$$
J_i=\frac{T_i-cI_4}{s}.
$$
Then
$$
J_i^T=-J_i.
$$
Using $T_i^TT_i=I_4$,
$$
(cI_4-sJ_i)(cI_4+sJ_i)=I_4,
$$
so
$$
J_i^2=-I_4.
$$
Thus each $J_i$ is an orthogonal complex structure.

Step 2: Use the conditions on the products $T_iT_j$
For $i\ne j$,
$$
T_iT_j=c^2I_4+cs(J_i+J_j)+s^2J_iJ_j.
$$
The hypothesis
$$
\langle x,T_iT_jx\rangle=c\|x\|^2
$$
for every $x$ is equivalent to
$$
T_iT_j+(T_iT_j)^T=2cI_4.
$$
Because $J_i^T=-J_i$, this yields
$$
2c^2I_4+s^2(J_iJ_j+J_jJ_i)=2cI_4.
$$
Hence
$$
J_iJ_j+J_jJ_i=2\gamma I_4,
\qquad
\gamma=\frac{c}{1+c}.
$$

On the real vector space of skew-symmetric $4\times4$ matrices, use the inner product
$$
\langle A,B\rangle_*=-\frac14\operatorname{tr}(AB).
$$
Since $J_i^2=-I_4$,
$$
\|J_i\|_*^2=1.
$$
Taking traces in the anticommutator relation gives
$$
\langle J_i,J_j\rangle_*=-\gamma
\qquad(i\ne j).
$$
Thus the four $J_i$ have Gram matrix
$$
G=(1+\gamma)I_4-\gamma\mathbf 1\mathbf 1^T.
$$

Step 3: Show that the four $J_i$ span at most three dimensions
Fix $J_1$. For $i=2,3,4$, define
$$
K_i=\frac{J_i+\gamma J_1}{\sqrt{1-\gamma^2}}.
$$
Using
$$
J_1J_i+J_iJ_1=2\gamma I_4
$$
and $J_1^2=-I_4$, we obtain
$$
J_1K_i+K_iJ_1=0.
$$
Therefore every $K_i$ lies in the linear space
$$
\mathcal A=\{K:K^T=-K,\ J_1K+KJ_1=0\}.
$$

Choose an orthonormal basis in which
$$
J_1=
\begin{pmatrix}
0&-I_2\\
I_2&0
\end{pmatrix}.
$$
Write a general skew-symmetric matrix as
$$
K=
\begin{pmatrix}
A&B\\
-B^T&D
\end{pmatrix},
$$
where $A,D$ are skew-symmetric $2\times2$ matrices. The equation $J_1K+KJ_1=0$ is equivalent to
$$
B+B^T=0,
\qquad
D=-A.
$$
A skew-symmetric $2\times2$ matrix has one free parameter, so $A$ contributes one parameter and $B$ contributes one parameter. Hence
$$
\dim\mathcal A=2.
$$
Consequently
$$
\dim\operatorname{span}\{J_1,J_2,J_3,J_4\}\le3.
$$
Therefore the Gram matrix $G$ has rank at most $3$.

Step 4: Extract the unique value of $c$
The eigenvalues of
$$
G=(1+\gamma)I_4-\gamma\mathbf 1\mathbf 1^T
$$
are
$$
1+\gamma
$$
with multiplicity $3$, and
$$
1-3\gamma
$$
with multiplicity $1$. Since $0<c<1$, we have $\gamma>0$, so $1+\gamma>0$. Rank at most $3$ therefore forces
$$
1-3\gamma=0.
$$
Thus
$$
\gamma=\frac13.
$$
Since
$$
\gamma=\frac{c}{1+c},
$$
we get
$$
\frac{c}{1+c}=\frac13,
$$
so
$$
c=\frac12.
$$

Step 5: Construct four transformations attaining the value
Let $I,J,K$ be the following skew-symmetric orthogonal matrices:
$$
I=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
\quad
J=
\begin{pmatrix}
0&0&-1&0\\
0&0&0&1\\
1&0&0&0\\
0&-1&0&0
\end{pmatrix},
$$
$$
K=
\begin{pmatrix}
0&0&0&-1\\
0&0&-1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix}.
$$
They satisfy
$$
I^2=J^2=K^2=-I_4
$$
and pairwise anticommute.

Take the four unit vectors
$$
q_1=\frac1{\sqrt3}(1,1,1),
\quad
q_2=\frac1{\sqrt3}(1,-1,-1),
$$
$$
q_3=\frac1{\sqrt3}(-1,1,-1),
\quad
q_4=\frac1{\sqrt3}(-1,-1,1).
$$
They satisfy
$$
q_i\cdot q_j=-\frac13
\qquad(i\ne j).
$$
Define
$$
J_i=(q_i)_1I+(q_i)_2J+(q_i)_3K.
$$
Then
$$
J_i^2=-I_4
$$
and, for $i\ne j$,
$$
J_iJ_j+J_jJ_i
=-2(q_i\cdot q_j)I_4
=\frac23I_4.
$$
Finally set
$$
T_i=\frac12I_4+\frac{\sqrt3}{2}J_i.
$$
Each $T_i$ is orthogonal and satisfies
$$
T_i+T_i^T=I_4.
$$
Also, for $i\ne j$,
$$
\frac12\bigl(T_iT_j+(T_iT_j)^T\bigr)
=\frac14I_4+\frac38\left(\frac23I_4\right)
=\frac12I_4.
$$
Hence all the stated conditions hold with $c=1/2$.

Final Answer: $\boxed{\frac12}$

---

## Answer

$\frac12$

---

## Classification

**Problem Type:** Exact determination

**Answer Type:** Exact scalar

---

## Solution Concepts

- orthogonal transformations
- polarization identity
- orthogonal complex structures
- anticommuting skew-symmetric maps
- gram matrix rank
