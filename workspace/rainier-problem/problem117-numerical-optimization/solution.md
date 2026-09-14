## Steps

Step 1: Rewrite the condition-number optimization as a diagonal Loewner sandwich
The leading principal minors of
$$
A=\begin{bmatrix}
4&1&1\\
1&3&1\\
1&1&2
\end{bmatrix}
$$
are $4,11,17$, so $A$ is positive definite. Let
$$
D=\operatorname{diag}(d_1,d_2,d_3),
\qquad d_i>0,
$$
and write
$$
m=\lambda_{\min}(DAD),
\qquad
M=\lambda_{\max}(DAD),
\qquad
t=\frac{M}{m}.
$$
Then
$$
mI\preceq DAD\preceq MI.
$$
Congruence by $D^{-1}$ gives
$$
S\preceq A\preceq tS,
\qquad
S=mD^{-2},
$$
where $S$ is positive diagonal. Conversely, if a positive diagonal $S$ satisfies $S\preceq A\preceq tS$, then with $D=S^{-1/2}$ every eigenvalue of $DAD$ lies in $[1,t]$. Therefore the optimal condition number is exactly the least $t$ for which such a diagonal sandwich exists.

Step 2: Derive a global lower bound from sign flips
Let $J$ be any diagonal sign matrix and put $y=Jx$. Since $S$ is diagonal,
$$
y^TSy=x^TSx.
$$
Hence every feasible sandwich satisfies
$$
y^TAy\leq t\,y^TSy=t\,x^TSx\leq t\,x^TAx,
$$
so for every nonzero $x$,
$$
t\geq\frac{x^TJAJx}{x^TAx}.
$$
Take
$$
J=\operatorname{diag}(1,1,-1).
$$
The largest possible value of the quotient is the largest generalized eigenvalue $\tau$ satisfying
$$
\det(JAJ-\tau A)=0.
$$
Here
$$
JAJ-\tau A=
\begin{bmatrix}
4(1-\tau)&1-\tau&-(1+\tau)\\
1-\tau&3(1-\tau)&-(1+\tau)\\
-(1+\tau)&-(1+\tau)&2(1-\tau)
\end{bmatrix},
$$
and expanding this $3\times3$ determinant gives
$$
\det(JAJ-\tau A)=-(\tau-1)(17\tau^2-54\tau+17).
$$
Thus its largest generalized eigenvalue is
$$
\tau_*:=\frac{27+2\sqrt{110}}{17},
$$
and every positive diagonal scaling satisfies
$$
\kappa_2(DAD)\geq\tau_*.
$$

Step 3: Construct a scaling attaining the lower bound
Choose
$$
D_*=\operatorname{diag}(2,\sqrt{6},\sqrt{11}).
$$
Then
$$
D_*AD_*=
\begin{bmatrix}
16&2\sqrt{6}&2\sqrt{11}\\
2\sqrt{6}&18&\sqrt{66}\\
2\sqrt{11}&\sqrt{66}&22
\end{bmatrix}.
$$
For this explicit matrix,
$$
\det(\lambda I-D_*AD_*)
=(\lambda-12)(\lambda^2-44\lambda+374).
$$
Hence its eigenvalues are
$$
22-\sqrt{110},\qquad 12,\qquad 22+\sqrt{110}.
$$
Since $22-\sqrt{110}<12<22+\sqrt{110}$,
$$
\kappa_2(D_*AD_*)
=\frac{22+\sqrt{110}}{22-\sqrt{110}}
=\frac{27+2\sqrt{110}}{17}
=\tau_*.
$$
Thus the lower bound is sharp.

Step 4: Prove the minimizing diagonal scaling is unique up to a common factor
Let
$$
r=\sqrt{110},
\qquad
x=\begin{bmatrix}-4\\-6\\r\end{bmatrix},
\qquad
y=Jx=\begin{bmatrix}-4\\-6\\-r\end{bmatrix}.
$$
Substitution into the generalized eigenvalue equation from Step 2 gives
$$
y^TAy=\tau_*x^TAx.
$$
Suppose a diagonal scaling attains $\tau_*$. Normalize it so that $\lambda_{\min}(DAD)=1$, and let $S=D^{-2}$. Then
$$
S\preceq A\preceq\tau_*S.
$$
For the displayed $x,y$, the inequality chain from Step 2 starts and ends with equal quantities, so equality holds throughout. In particular,
$$
x^T(A-S)x=0.
$$
Because $A-S\succeq0$, this forces $(A-S)x=0$. All coordinates of $x$ are nonzero, so the diagonal entries of $S$ are uniquely determined by
$$
s_i=\frac{(Ax)_i}{x_i}.
$$
Now
$$
Ax=\begin{bmatrix}-22+r\\-22+r\\-10+2r\end{bmatrix},
$$
which yields
$$
S=(22-r)\operatorname{diag}\left(\frac14,\frac16,\frac1{11}\right).
$$
Therefore $D=S^{-1/2}$ is proportional to
$$
\operatorname{diag}(2,\sqrt{6},\sqrt{11}).
$$
Hence the minimizing scaling class is unique.

Step 5: State the requested optimum and unique scaling ratio
The least possible spectral condition number is $\tau_*$, and every minimizing diagonal is a positive scalar multiple of $D_*$. Therefore the requested ordered pair is the optimal condition number together with the unique ratio $d_1:d_2:d_3$.

Final Answer: $\boxed{\left(\frac{27+2\sqrt{110}}{17},2:\sqrt{6}:\sqrt{11}\right)}$

---

## Answer

$\left(\frac{27+2\sqrt{110}}{17},2:\sqrt{6}:\sqrt{11}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- diagonal preconditioning
- spectral condition number
- Loewner order
- generalized Rayleigh quotient
- equality certificate
