# Draft solution

Let
$$
A_1=\begin{pmatrix}-\alpha&1&0\\0&-\alpha&0\\0&0&-\alpha\end{pmatrix},\quad
A_2=\begin{pmatrix}-\alpha&0&0\\0&-\alpha&1\\0&0&-\alpha\end{pmatrix},\quad
A_3=\begin{pmatrix}-\alpha&0&0\\0&-\alpha&0\\1&0&-\alpha\end{pmatrix}.
$$
Write $A_i=-\alpha I+N_i$. Since $N_i^2=0$,
$$
e^{sA_i}=e^{-\alpha s}(I+sN_i).
$$
For dwell fractions $x,y,z\geq0$ with $x+y+z=1$, the one-period matrix is
$$
\Phi(x,y,z)=e^{-\alpha}M(x,y,z),
$$
where
$$
M=(I+zN_3)(I+yN_2)(I+xN_1)
=\begin{pmatrix}
1&x&0\\
0&1&y\\
z&zx&1
\end{pmatrix}.
$$

Set $q=xyz$. Direct determinant expansion gives
$$
\det(\lambda I-M)=(\lambda-1)^3-q\lambda.
$$
For $q>0$, $M$ is nonnegative and irreducible, so Perron-Frobenius gives a positive eigenvalue equal to $\rho(M)$. Writing it as $\lambda=1+r$ gives
$$
r^3=q(r+1).
$$
There is a unique $r\geq0$ satisfying this equation, since
$$
q=\frac{r^3}{r+1}
$$
is strictly increasing for $r\geq0$. Hence $\rho(M)$ is an increasing function of $q$. The boundary cases $q=0$ follow by continuity.

Under $x+y+z=1$, AM-GM gives $q\leq1/27$, with equality exactly at $x=y=z=1/3$. Therefore the largest possible spectral radius of $M$ is the number $\rho_*>1$ satisfying
$$
27(\rho_*-1)^3=\rho_*.
$$
Equivalently,
$$
\rho_* = \max\{r\in\mathbb R:27(r-1)^3=r\}.
$$

If $e^{-\alpha}\rho_*<1$, choose $R$ with $e^{-\alpha}\rho_*<R<1$. The family
$$
\mathcal F=\{\Phi(x,y,z):x,y,z\geq0,\ x+y+z=1\}
$$
is compact and every member has spectrum in $|w|<R$. On the compact set
$$
\{(\Phi,w):\Phi\in\mathcal F,\ |w|=R\},
$$
the resolvent $(wI-\Phi)^{-1}$ is continuous and uniformly bounded. Cauchy's formula for matrix powers gives a constant $C$ independent of $x,y,z$ such that
$$
\|\Phi(x,y,z)^n\|_2\leq C R^n.
$$
The flow during the remaining fraction of a period is uniformly bounded because every active matrix has norm at most $\alpha+1$. Thus there are $M,\gamma>0$, independent of the dwell fractions, giving uniform exponential decay.

Conversely, for $x=y=z=1/3$, the monodromy matrix has eigenvalue $e^{-\alpha}\rho_*$. If this number is at least $1$, an eigenvector produces a nondecaying solution at integer times, so uniform exponential stability is impossible. Therefore the exact condition is
$$
\alpha>\log\max\{r\in\mathbb R:27(r-1)^3=r\}.
$$
