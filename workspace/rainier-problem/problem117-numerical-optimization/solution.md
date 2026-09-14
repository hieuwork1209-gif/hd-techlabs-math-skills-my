## Steps

Step 1: Extract three local condition-number obstructions from the common scaling
Let
$$
D=\operatorname{diag}(d_1,d_2,d_3),
\qquad d_i>0.
$$
The active $2\times2$ blocks of $A_1,A_2,A_3$ have positive leading entries and determinants $3,12,3$, respectively, while each isolated diagonal entry is $2$. Hence all three $A_k$ are positive definite, and so are the congruences $DA_kD$.

For any symmetric positive-definite matrix $M$ and any principal submatrix $B$, the Rayleigh-quotient formulas give
$$
\lambda_{\min}(M)\leq\lambda_{\min}(B)
\leq\lambda_{\max}(B)\leq\lambda_{\max}(M),
$$
so
$$
\kappa_2(M)\geq\kappa_2(B).
$$

For the first scenario, the principal block of $DA_1D$ on coordinates $1,2$ is
$$
\begin{bmatrix}
d_1^2&d_1d_2\\
d_1d_2&4d_2^2
\end{bmatrix}
=2d_1d_2
\begin{bmatrix}
r_1&1/2\\
1/2&r_1^{-1}
\end{bmatrix},
\qquad
r_1=\frac{d_1}{2d_2}.
$$
For the second scenario, the principal block on coordinates $2,3$ is
$$
\begin{bmatrix}
d_2^2&2d_2d_3\\
2d_2d_3&16d_3^2
\end{bmatrix}
=4d_2d_3
\begin{bmatrix}
r_2&1/2\\
1/2&r_2^{-1}
\end{bmatrix},
\qquad
r_2=\frac{d_2}{4d_3}.
$$
For the third scenario, order the active coordinates as $3,1$. The corresponding principal block is
$$
\begin{bmatrix}
d_3^2&d_3d_1\\
d_3d_1&4d_1^2
\end{bmatrix}
=2d_3d_1
\begin{bmatrix}
r_3&1/2\\
1/2&r_3^{-1}
\end{bmatrix},
\qquad
r_3=\frac{d_3}{2d_1}.
$$
Thus, with
$$
C(r)=\begin{bmatrix}r&1/2\\1/2&r^{-1}\end{bmatrix},
$$
every common scaling satisfies
$$
\max_{1\leq k\leq3}\kappa_2(DA_kD)
\geq \max_{1\leq i\leq3}\kappa_2(C(r_i)).
$$
The three local imbalance parameters obey the compatibility identity
$$
r_1r_2r_3=\frac1{16}=\gamma^{-3}.
$$

Step 2: Convert the local obstructions into a global lower bound
For $r>0$, put
$$
T(r)=r+r^{-1}.
$$
The matrix $C(r)$ has trace $T(r)$ and determinant $3/4$, so its eigenvalues are
$$
\lambda_{\pm}(r)
=\frac{T(r)\pm\sqrt{T(r)^2-3}}{2}.
$$
Hence
$$
\Psi(r):=\kappa_2(C(r))
=\frac{T(r)+\sqrt{T(r)^2-3}}
{T(r)-\sqrt{T(r)^2-3}}.
$$
Because
$$
T(r)=2\cosh(\log r),
$$
$T(r)$ is strictly increasing with $|\log r|$. Also
$$
\Psi(r)=\frac{\left(T(r)+\sqrt{T(r)^2-3}\right)^2}{3},
$$
and the right side is strictly increasing with $T(r)\geq2$. Therefore $\Psi(r)$ is strictly increasing with $|\log r|$.

Now
$$
\log r_1+\log r_2+\log r_3=-\log16=-3\log\gamma.
$$
Therefore
$$
\max_i|\log r_i|\geq\log\gamma.
$$
At least one local block consequently has condition number at least
$$
\Psi(\gamma^{-1}).
$$
Since $H=\gamma+\gamma^{-1}$,
$$
\Psi(\gamma^{-1})
=\frac{H+\sqrt{H^2-3}}{H-\sqrt{H^2-3}}.
$$
Thus every positive diagonal $D$ satisfies
$$
\max_k\kappa_2(DA_kD)
\geq
\frac{H+\sqrt{H^2-3}}{H-\sqrt{H^2-3}}.
$$

Step 3: Construct a common scaling that attains the lower bound
Let
$$
\eta=2^{1/3},
\qquad
D_*=\operatorname{diag}(\eta,\eta^2,1).
$$
Since $\gamma=\eta^4$, the three imbalance parameters are
$$
\frac{\eta}{2\eta^2}
=\frac{\eta^2}{4}
=\frac{1}{2\eta}
=\gamma^{-1}.
$$
Thus every active $2\times2$ block has condition number $\Psi(\gamma^{-1})$.

It remains to check that the isolated coordinate in each $3\times3$ matrix does not enlarge the condition number. Let $\lambda_-<\lambda_+$ be the eigenvalues of $C(\gamma^{-1})$. Its characteristic polynomial is
$$
q(s)=s^2-Hs+\frac34.
$$
Since $H>2$,
$$
q\left(\frac12\right)=1-\frac H2<0,
$$
so $1/2$ lies strictly between $\lambda_-$ and $\lambda_+$. For the first two scenarios, the active blocks are respectively
$$
4C(\gamma^{-1}),
\qquad
4\eta^2C(\gamma^{-1}),
$$
while their isolated eigenvalues are respectively $2$ and $2\eta^2$, exactly one half of the corresponding block factors.

For the third scenario, the active block is $2\eta C(\gamma^{-1})$, while the isolated eigenvalue is
$$
2\eta^4=4\eta,
$$
which is twice the block factor. Since $\gamma^3=16>(5/2)^3$, we have $\gamma>5/2$, hence $H>5/2>19/8$. Therefore
$$
q(2)=\frac{19}{4}-2H<0,
$$
so $2$ also lies strictly between $\lambda_-$ and $\lambda_+$.

Thus in all three scenarios the isolated eigenvalue lies between the two active-block eigenvalues. Hence
$$
\max_k\kappa_2(D_*A_kD_*)
=\Psi(\gamma^{-1}),
$$
so the lower bound in Step 2 is attained.

Step 4: Prove uniqueness of the minimizing scaling class
Suppose $D$ attains the optimal robust condition number. Then every local principal-block condition number is at most the optimum, so Step 2 and the strict monotonicity of $\Psi$ imply
$$
|\log r_i|\leq\log\gamma,
\qquad i=1,2,3.
$$
But their sum is exactly $-3\log\gamma$. The only way three numbers, each at least $-\log\gamma$, can have this sum is
$$
\log r_1=\log r_2=\log r_3=-\log\gamma.
$$
Hence
$$
\frac{d_1}{2d_2}
=\frac{d_2}{4d_3}
=\frac{d_3}{2d_1}
=\gamma^{-1}.
$$
Setting $d_3=1$ fixes the class uniquely:
$$
d_2=\frac4\gamma=2^{2/3},
\qquad
d_1=\frac{2d_2}{\gamma}=2^{1/3}.
$$
Therefore every minimizer is a positive scalar multiple of
$$
\operatorname{diag}(2^{1/3},2^{2/3},1).
$$

Step 5: State the robust optimum and the unique common scaling
The global lower bound, attainment, and equality case together determine both requested components.

Final Answer: $\boxed{\left(\frac{H+\sqrt{H^2-3}}{H-\sqrt{H^2-3}},2^{1/3}:2^{2/3}:1\right)}$

---

## Answer

$\left(\frac{H+\sqrt{H^2-3}}{H-\sqrt{H^2-3}},2^{1/3}:2^{2/3}:1\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- robust diagonal preconditioning
- principal-submatrix spectral bounds
- condition-number minimax
- logarithmic compatibility
- equality certificate
