## Steps

Step 1: Obtain a switching-independent upper bound
Let
$$
A_1=\begin{pmatrix}-\alpha&\kappa\\0&-\beta\end{pmatrix},
\qquad
A_2=A_1^T.
$$
Both matrices have the same symmetric part
$$
S=\frac{A_i+A_i^T}{2}
=\begin{pmatrix}
-\alpha&\frac{\kappa}{2}\\
\frac{\kappa}{2}&-\beta
\end{pmatrix}.
$$
Let $\lambda_+$ be the largest eigenvalue of $S$. For any switching signal $\sigma$ and any solution of
$$
\dot x=A_{\sigma(t)}x,
$$
one has, at every time away from switching instants,
$$
\frac{d}{dt}\|x(t)\|_2^2
=2x(t)^TSx(t)
\leq2\lambda_+\|x(t)\|_2^2.
$$
Integrating this differential inequality on each constant-switch interval and concatenating the intervals gives
$$
\|\Phi_\sigma(t)\|_2\leq e^{\lambda_+t}
$$
for every $t\geq0$. Hence
$$
\limsup_{t\to\infty}\frac1t\log\|\Phi_\sigma(t)\|_2\leq\lambda_+
$$
for every admissible $\sigma$, so
$$
\Lambda(\alpha,\beta,\kappa)\leq\lambda_+.
$$

Step 2: Build periodic switching laws that approach the upper bound
Fix $h>0$ and alternate periodically: use $A_1$ for time $h$, then $A_2$ for time $h$, and repeat. Put
$$
E_h=e^{hA_1}.
$$
Since $A_2=A_1^T$,
$$
e^{hA_2}=E_h^T.
$$
Therefore the monodromy over one period $2h$ is
$$
M_h=E_h^TE_h.
$$
This matrix is symmetric positive definite, and its largest eigenvalue is
$$
\rho(M_h)=\|E_h\|_2^2.
$$
After $n$ full periods,
$$
\Phi_\sigma(2nh)=M_h^n,
$$
and because $M_h$ is symmetric positive definite,
$$
\|M_h^n\|_2=\rho(M_h)^n.
$$
Thus this periodic switching law has asymptotic growth exponent at least
$$
\frac{1}{2h}\log\rho(M_h)
=\frac1h\log\|e^{hA_1}\|_2.
$$
Consequently
$$
\Lambda(\alpha,\beta,\kappa)
\geq\sup_{h>0}\frac1h\log\|e^{hA_1}\|_2.
$$

Step 3: Show that fast alternation saturates the common energy bound
The matrix exponential has the expansion
$$
e^{hA_1}=I+hA_1+O(h^2)
$$
in operator norm as $h\to0^+$. Let $v$ be a unit eigenvector of $S$ for $\lambda_+$. Then
$$
\|e^{hA_1}v\|_2^2
=\|v+hA_1v+O(h^2)\|_2^2
=1+2h\,v^TSv+O(h^2)
=1+2\lambda_+h+O(h^2).
$$
Hence
$$
\|e^{hA_1}\|_2
\geq1+\lambda_+h+O(h^2).
$$
On the other hand, Step 1 applied to the constant signal $\sigma\equiv1$ gives
$$
\|e^{hA_1}\|_2\leq e^{\lambda_+h}
=1+\lambda_+h+O(h^2).
$$
Therefore
$$
\lim_{h\to0^+}\frac1h\log\|e^{hA_1}\|_2=\lambda_+.
$$
Combining this with Step 2 yields
$$
\Lambda(\alpha,\beta,\kappa)\geq\lambda_+.
$$
Together with Step 1,
$$
\Lambda(\alpha,\beta,\kappa)=\lambda_+.
$$

Step 4: Compute the largest eigenvalue explicitly
The characteristic equation of $S$ is
$$
(\lambda+\alpha)(\lambda+\beta)-\frac{\kappa^2}{4}=0.
$$
Thus
$$
\lambda_+
=\frac{\sqrt{(\alpha-\beta)^2+\kappa^2}-\alpha-\beta}{2}.
$$
Therefore the exact worst-case asymptotic growth exponent over all admissible switching signals is the displayed quantity.

Final Answer: $\boxed{\frac{\sqrt{(\alpha-\beta)^2+\kappa^2}-\alpha-\beta}{2}}$

---

## Answer

$\frac{\sqrt{(\alpha-\beta)^2+\kappa^2}-\alpha-\beta}{2}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- switched linear systems
- common quadratic growth bound
- matrix exponential asymptotics
- periodic switching monodromy
- worst-case Lyapunov exponent
