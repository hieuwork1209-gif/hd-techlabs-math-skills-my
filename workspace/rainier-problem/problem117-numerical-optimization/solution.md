## Steps

Step 1: Express the one-step contraction as a generalized Rayleigh quotient
Let
$$
A=\begin{bmatrix}
4&1&1\\
1&3&1\\
1&1&2
\end{bmatrix}.
$$
Its leading principal minors are $4$, $11$, and $17$, so $A$ is positive definite. Its inverse is
$$
B=A^{-1}=\frac1{17}
\begin{bmatrix}
5&-1&-2\\
-1&7&-3\\
-2&-3&11
\end{bmatrix}.
$$
If block $i$ is chosen, all coordinates except $i$ are re-minimized while $x_i$ is held fixed. The constrained minimizer $z$ satisfies $(Az)_j=0$ for $j\ne i$, so $Az=\lambda e_i$ and therefore $z=\lambda Be_i$. Since $z_i=x_i$, we have
$$
\lambda=\frac{x_i}{B_{ii}}.
$$
Hence
$$
2f(z)=z^TAz=\frac{x_i^2}{B_{ii}}.
$$
For sampling probabilities $p_1,p_2,p_3$, define
$$
C(p)=\operatorname{diag}\left(\frac{p_1}{B_{11}},\frac{p_2}{B_{22}},\frac{p_3}{B_{33}}\right)
=\operatorname{diag}\left(\frac{17p_1}{5},\frac{17p_2}{7},\frac{17p_3}{11}\right).
$$
Then
$$
\frac{\mathbb E[f(x^+)\mid x]}{f(x)}
=\frac{x^TC(p)x}{x^TAx},
$$
so
$$
\rho(p)=\sup_{x\ne0}\frac{x^TC(p)x}{x^TAx}.
$$
Therefore $\rho(p)$ is the least $r$ for which
$$
C(p)\preceq rA.
$$

Step 2: Build a global lower-bound certificate that is independent of the sampling distribution
A lower bound valid for every $p$ should make the diagonal contribution $\operatorname{tr}(LC(p))$ independent of $p$. Since
$$
B_{11}:B_{22}:B_{33}=5:7:11,
$$
seek a positive semidefinite triangle Laplacian whose diagonal is proportional to $5:7:11$. If its edge weights on $(1,2),(1,3),(2,3)$ are $a,b,c$, write
$$
a+b=5q,\qquad a+c=7q,\qquad b+c=11q.
$$
Adding the first two equations and subtracting the third gives $2a=q$; similarly $2b=9q$ and $2c=13q$. Thus $a:b:c=1:9:13$, and we take
$$
L=\begin{bmatrix}
10&-1&-9\\
-1&14&-13\\
-9&-13&22
\end{bmatrix}.
$$
It is positive semidefinite because
$$
y^TLy=(y_1-y_2)^2+9(y_1-y_3)^2+13(y_2-y_3)^2\geq0.
$$
If $C(p)\preceq rA$, then $rA-C(p)\succeq0$, so
$$
0\leq\operatorname{tr}\left(L(rA-C(p))\right)
=r\operatorname{tr}(LA)-\operatorname{tr}(LC(p)).
$$
Now
$$
\operatorname{tr}(LC(p))
=10\frac{17p_1}{5}+14\frac{17p_2}{7}+22\frac{17p_3}{11}
=34(p_1+p_2+p_3)=34.
$$
Also, since every off-diagonal entry of $A$ is $1$,
$$
\begin{aligned}
\operatorname{tr}(LA)
&=10\cdot4+14\cdot3+22\cdot2
+2(-1-9-13)\\
&=40+42+44-46=80.
\end{aligned}
$$
Consequently every sampling distribution satisfies
$$
\rho(p)\geq\frac{34}{80}=\frac{17}{40}.
$$

Step 3: Construct a sampling distribution attaining the lower bound
Choose
$$
(p_1,p_2,p_3)=\left(\frac{15}{40},\frac{14}{40},\frac{11}{40}\right).
$$
Then
$$
C(p)=\operatorname{diag}\left(\frac{51}{40},\frac{17}{20},\frac{17}{40}\right).
$$
With $r=17/40$,
$$
rA-C(p)
=\frac{17}{40}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\succeq0.
$$
Thus $C(p)\preceq rA$, so Step 1 gives
$$
\rho(p)\leq\frac{17}{40}.
$$
Together with the lower bound in Step 2,
$$
\rho_*:=\min_p\rho(p)=\frac{17}{40}.
$$

Step 4: Prove the optimal sampling distribution is unique
Suppose $p$ attains $\rho_*=17/40$, and set
$$
S=\frac{17}{40}A-C(p)\succeq0.
$$
The lower-bound chain in Step 2 is then an equality, so
$$
\operatorname{tr}(LS)=0.
$$
Because $L,S\succeq0$, the matrix $L^{1/2}SL^{1/2}$ is positive semidefinite with trace zero, hence it is zero. Therefore $S^{1/2}L^{1/2}=0$; taking transposes also gives $L^{1/2}S^{1/2}=0$, and consequently $LS=0$.

The graph defining $L$ is connected, so
$$
\ker L=\operatorname{span}\{(1,1,1)^T\}.
$$
Thus every column of $S$ lies in this one-dimensional kernel. Since $S$ is symmetric and positive semidefinite,
$$
S=t\mathbf 1\mathbf 1^T
$$
for some $t\geq0$. Its off-diagonal entries are fixed by the definition of $S$: because every off-diagonal entry of $A$ equals $1$ and $C(p)$ is diagonal,
$$
S_{ij}=\frac{17}{40}
\qquad(i\ne j).
$$
Hence $t=17/40$, so every diagonal entry of $S$ is also $17/40$. Therefore
$$
\frac{17}{40}A_{ii}-\frac{p_i}{B_{ii}}=\frac{17}{40}.
$$
Using
$$
(B_{11},B_{22},B_{33})=\left(\frac5{17},\frac7{17},\frac{11}{17}\right)
$$
gives
$$
p_1=\frac{15}{40},\qquad
p_2=\frac{14}{40},\qquad
p_3=\frac{11}{40}.
$$
So the optimizer is unique.

Step 5: State the optimal contraction and sampling ratio
The optimal expected one-step energy contraction is $17/40$, attained only by the sampling distribution proportional to $15:14:11$.

Final Answer: $\boxed{\left(\frac{17}{40},15:14:11\right)}$

---

## Answer

$\left(\frac{17}{40},15:14:11\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- randomized block coordinate descent
- generalized Rayleigh quotient
- semidefinite order
- graph Laplacian certificate
- complementary slackness
