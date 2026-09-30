## Steps

Step 1: Reduce the common-preconditioner problem to a condition-number problem
Let
$$
H_0=
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix},
\qquad
H_1=
\begin{pmatrix}
\frac12&1\\
1&4
\end{pmatrix},
\qquad
H_t=(1-t)H_0+tH_1.
$$
For a positive definite preconditioner $P$, the matrix $PH_t$ is similar to
$$
B_t=P^{1/2}H_tP^{1/2},
$$
which is symmetric positive definite. Set
$$
m(P)=\min_{0\leq t\leq1}\lambda_{\min}(B_t),
\qquad
L(P)=\max_{0\leq t\leq1}\lambda_{\max}(B_t).
$$
Because $B_t=(1-t)B_0+tB_1$, the function $t\mapsto\lambda_{\max}(B_t)$ is convex and $t\mapsto\lambda_{\min}(B_t)$ is concave: each is respectively the maximum or minimum, over unit vectors $v$, of the affine function $v^TB_tv$. Hence
$$
L(P)=\max\{\lambda_{\max}(B_0),\lambda_{\max}(B_1)\},
$$
and
$$
m(P)=\min\{\lambda_{\min}(B_0),\lambda_{\min}(B_1)\}.
$$

For fixed $P$, all eigenvalues relevant to the iteration lie in $[m(P),L(P)]$, and both endpoints occur. Therefore
$$
\min_{\eta>0}\max_{0\leq t\leq1}r(I-\eta PH_t)
=
\min_{\eta>0}\max\{|1-\eta m(P)|,|1-\eta L(P)|\}
=
\frac{K(P)-1}{K(P)+1},
$$
where
$$
K(P)=\frac{L(P)}{m(P)}.
$$
The minimizing step is $\eta=2/(L(P)+m(P))$. Multiplying $P$ by a positive scalar does not change the optimized factor because the scalar can be absorbed into $\eta$, so impose
$$
\det P=1.
$$

Step 2: Obtain the invariant lower bound for unrestricted positive definite preconditioners
Both endpoint Hessians have determinant $1$. Under the normalization $\det P=1$,
$$
\det B_0=\det B_1=1.
$$
If
$$
L=\max\{\lambda_{\max}(B_0),\lambda_{\max}(B_1)\},
$$
then each endpoint spectrum is contained in $[1/L,L]$. Thus $m(P)=1/L$ and
$$
K(P)=L^2.
$$

The generalized eigenvalues of the pair $(B_1,B_0)$ are independent of $P$, because
$$
B_0^{-1}B_1
$$
is similar to $H_0^{-1}H_1$. Here
$$
H_0^{-1}=
\begin{pmatrix}
2&-1\\
-1&1
\end{pmatrix},
\qquad
H_0^{-1}H_1=
\begin{pmatrix}
0&-2\\
\frac12&3
\end{pmatrix}.
$$
Its characteristic polynomial is
$$
z^2-3z+1,
$$
so its larger eigenvalue is
$$
\mu=\frac{3+\sqrt5}{2}.
$$
For every nonzero vector $x$,
$$
\frac{x^TB_1x}{x^TB_0x}
\leq
\frac{L\|x\|^2}{L^{-1}\|x\|^2}
=L^2.
$$
To identify the maximum generalized Rayleigh quotient, set $y=B_0^{1/2}x$. Then
$
\frac{x^TB_1x}{x^TB_0x}
=
\frac{y^T(B_0^{-1/2}B_1B_0^{-1/2})y}{y^Ty},
$
whose maximum is the largest eigenvalue $\mu$. Therefore
$
\mu\leq L^2=K(P).
$
Therefore every positive definite preconditioner satisfies $K(P)\geq\mu$.

Step 3: Construct the unrestricted preconditioner that attains the invariant bound
Let
$$
C=H_0^{-1/2}H_1H_0^{-1/2}.
$$
It is symmetric positive definite with eigenvalues $\mu$ and $\mu^{-1}$. Choose an orthogonal matrix $U$ such that
$$
C=U
\begin{pmatrix}
\mu&0\\
0&\mu^{-1}
\end{pmatrix}
U^T,
$$
and define
$$
Q=U
\begin{pmatrix}
\mu^{-1/2}&0\\
0&\mu^{1/2}
\end{pmatrix}
U^T,
\qquad
P_*=H_0^{-1/2}QH_0^{-1/2}.
$$
Since $\det H_0=\det Q=1$, one has $\det P_*=1$.

The similarities
$
H_0^{1/2}(P_*H_0)H_0^{-1/2}=Q
$
and
$
H_0^{1/2}(P_*H_1)H_0^{-1/2}=QC
$
show that $P_*H_0$ has eigenvalues
$
\mu^{-1/2},\quad \mu^{1/2},
$
while $P_*H_1$ has the eigenvalues of $QC$. Since $Q$ and $C$ are diagonal in the same $U$-basis, these are again
$$
\mu^{-1/2},\quad \mu^{1/2}.
$$
Thus
$$
\mu^{-1/2}I\preceq B_0,B_1\preceq\mu^{1/2}I.
$$
The same Loewner bounds hold for every convex combination $B_t$. Hence $K(P_*)=\mu$, so the unrestricted robust factor is
$$
\rho_{\mathrm{full}}
=
\frac{\mu-1}{\mu+1}.
$$
Using $\mu=(3+\sqrt5)/2$,
$$
\rho_{\mathrm{full}}=\frac{1}{\sqrt{5}}.
$$

Step 4: Solve the diagonal-preconditioner minimax problem
Now restrict $P$ to be diagonal. After the same determinant normalization, write
$$
P=
\begin{pmatrix}
s&0\\
0&s^{-1}
\end{pmatrix},
\qquad s>0.
$$
The endpoint matrices $B_0,B_1$ still have determinant $1$, while their traces are
$$
T_0(s)=s+\frac2s,
\qquad
T_1(s)=\frac{s}{2}+\frac4s.
$$
For a positive definite $2\times2$ matrix of determinant $1$ and trace $T\geq2$, the larger eigenvalue is
$$
\Phi(T)=\frac{T+\sqrt{T^2-4}}{2},
$$
which is strictly increasing in $T$. Therefore minimizing $K(P)$ is equivalent to minimizing
$$
\max\{T_0(s),T_1(s)\}.
$$

At $s=2$ both traces equal $3$. This value is minimal. Indeed, for $0<s\leq2$,
$$
T_1(s)-3
=
\frac{(s-2)(s-4)}{2s}
\geq0,
$$
while for $s\geq2$,
$$
T_0(s)-3
=
\frac{(s-1)(s-2)}{s}
\geq0.
$$
Hence the unique minimizer is $s=2$, and the largest endpoint eigenvalue is
$$
\Phi(3)=\frac{3+\sqrt5}{2}=\mu.
$$
Therefore
$$
K_{\mathrm{diag}}=\mu^2.
$$

Step 5: Evaluate the diagonal factor and assemble the ordered pair
For
$$
P_{\mathrm{diag}}=
\begin{pmatrix}
2&0\\
0&\frac12
\end{pmatrix},
$$
both endpoint spectra lie in $[\mu^{-1},\mu]$. Since every $B_t$ is their convex combination, the same spectral enclosure holds for the full family, so the bound from Step 4 is attained.

The optimized diagonal-preconditioned factor is therefore
$$
\rho_{\mathrm{diag}}
=
\frac{\mu^2-1}{\mu^2+1}.
$$
Because $\mu+\mu^{-1}=3$ and $\mu-\mu^{-1}=\sqrt5$,
$$
\rho_{\mathrm{diag}}
=
\frac{\mu-\mu^{-1}}{\mu+\mu^{-1}}
=
\frac{\sqrt{5}}{3}.
$$
Combining this with the unrestricted value from Step 3 gives the required pair.
Final Answer: $\boxed{\left(\frac{1}{\sqrt{5}},\frac{\sqrt{5}}{3}\right)}$

---

## Answer

$\left(\frac{1}{\sqrt{5}},\frac{\sqrt{5}}{3}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- common preconditioning
- generalized eigenvalues
- condition-number optimization
- convexity of extremal eigenvalues
- diagonal matrix scaling
