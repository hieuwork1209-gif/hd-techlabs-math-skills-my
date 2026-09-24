## Steps

Step 1: Compute the one-period matrix
Write
$$
A_i=-\alpha I+N_i.
$$
The three nilpotent parts satisfy $N_i^2=0$, so for $s\geq0$,
$$
e^{sA_i}=e^{-\alpha s}(I+sN_i).
$$
For fixed $x,y,z\geq0$ with $x+y+z=1$, the transition over one full period is
$$
\Phi(x,y,z)=e^{zA_3}e^{yA_2}e^{xA_1}
=e^{-\alpha}M(x,y,z),
$$
where direct multiplication gives
$$
M(x,y,z)=
\begin{pmatrix}
1&x&0\\
0&1&y\\
z&zx&1
\end{pmatrix}.
$$
Therefore exponential behavior at integer times is controlled by the spectral radius of this explicit three-parameter matrix.

Step 2: Reduce the spectral radius to one scalar parameter
Set $q=xyz$. Expanding the determinant along the first row gives
$$
\det(\lambda I-M)
=(\lambda-1)^3-q\lambda.
$$
Assume first that $q>0$. Then $M$ is nonnegative, has positive diagonal entries, and its positive off-diagonal entries contain the directed cycle
$$
1\to3\to2\to1.
$$
Thus its directed graph is strongly connected, so $M$ is irreducible. The Perron-Frobenius theorem in the form used here says that an irreducible nonnegative matrix has a positive eigenvalue equal to its spectral radius, and no eigenvalue has larger modulus. Hence
$$
\rho(M)=1+r
$$
for the positive solution $r$ of
$$
r^3=q(r+1).
$$
Equivalently,
$$
q=\frac{r^3}{r+1}.
$$
For $r\geq0$,
$$
\frac{d}{dr}\frac{r^3}{r+1}
=\frac{r^2(2r+3)}{(r+1)^2}\geq0,
$$
with strict inequality for $r>0$. Hence $r$, and therefore $\rho(M)$, increases with $q$. When $q=0$, the characteristic polynomial is $(\lambda-1)^3$, so $\rho(M)=1$, agreeing with the limiting value.

Step 3: Find the worst dwell distribution
Since $x,y,z\geq0$ and $x+y+z=1$, the arithmetic-geometric mean inequality gives
$$
xyz\leq\left(\frac{x+y+z}{3}\right)^3=\frac{1}{27},
$$
with equality exactly at
$$
x=y=z=\frac{1}{3}.
$$
By Step 2, the largest possible value of $\rho(M)$ is attained there. Let this value be $\rho_*$. Substituting $q=1/27$ into
$$
(\lambda-1)^3-q\lambda=0
$$
gives
$$
27(\rho_*-1)^3=\rho_*.
$$
Moreover $\rho_*>1$, and it is the largest real root because it is the Perron root at the maximizing dwell triple. Thus
$$
\rho_*=
\max\{r\in\mathbb{R}:27(r-1)^3=r\}.
$$
Consequently,
$$
\max_{x+y+z=1}\rho(\Phi(x,y,z))
=e^{-\alpha}\rho_*.
$$

Step 4: Prove a uniform exponential bound when the worst multiplier is below one
Assume
$$
e^{-\alpha}\rho_*<1.
$$
Choose $R$ with
$$
e^{-\alpha}\rho_*<R<1.
$$
The simplex of triples $(x,y,z)$ is compact, and $\\Phi(x,y,z)$ depends continuously on the triple. Hence the family
$$
\mathcal F=\{\Phi(x,y,z):x,y,z\geq0,\ x+y+z=1\}
$$
is compact. Step 3 shows that every spectrum lies in $|w|<R$. Therefore
$$
K=
\max_{\Phi\in\mathcal F,\ |w|=R}
\|(wI-\Phi)^{-1}\|_2
$$
is finite, because the resolvent is continuous on this compact set. Cauchy's matrix formula gives, for every integer $n\geq0$,
$$
\Phi^n=
\frac{1}{2\pi i}\int_{|w|=R}
w^n(wI-\Phi)^{-1}\,dw,
$$
and therefore
$$
\|\Phi^n\|_2\leq K R^{n+1}.
$$
This bound is uniform in $(x,y,z)$.

For a time lying inside the next period, the remaining transition is a product of at most three factors $e^{sA_i}$ whose total elapsed time is at most $1$. Since
$$
\|A_i\|_2\leq\alpha+1,
$$
that transition has norm at most $e^{\alpha+1}$. Combining this with the integer-time bound yields constants $M,\gamma>0$, independent of $(x,y,z)$, such that
$$
\|X(t)\|_2\leq M e^{-\gamma t}\|X(0)\|_2.
$$

Step 5: Prove necessity and state the parameter range
Take the equal dwell triple
$$
x=y=z=\frac{1}{3}.
$$
Its one-period matrix has the positive eigenvalue
$$
e^{-\alpha}\rho_*.
$$
If $e^{-\alpha}\rho_*>1$, an eigenvector grows at integer times. If $e^{-\alpha}\rho_*=1$, the same eigenvector is nondecaying at integer times. Either case contradicts exponential stability. Together with Step 4, uniform exponential stability holds exactly when
$$
e^{-\alpha}\rho_*<1,
$$
or equivalently
$$
\alpha>\log\rho_*.
$$
Using the prompt-independent description of $\rho_*$ from Step 3 gives the requested region.
Final Answer: $\boxed{\alpha>\log\max\{r\in\mathbb{R}:27(r-1)^3=r\}}$

---

## Answer

$\alpha>\log\max\{r\in\mathbb{R}:27(r-1)^3=r\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- periodic linear systems
- monodromy matrices
- Perron-Frobenius theorem
- spectral radius
- uniform exponential stability
