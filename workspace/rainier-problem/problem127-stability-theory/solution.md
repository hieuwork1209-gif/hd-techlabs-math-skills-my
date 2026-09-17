## Steps

Step 1: Compute the exact finite-time growth of one mode
Let
$$
m=\frac{\alpha+\beta}{2},
\qquad
\delta=\frac{\beta-\alpha}{2}>0.
$$
Then
$$
A_1=-mI+C,
\qquad
C=\begin{pmatrix}\delta&\kappa\\0&-\delta\end{pmatrix},
\qquad
C^2=\delta^2I.
$$
Hence
$$
e^{hA_1}=e^{-mh}
\left(
\cosh(\delta h)I+\frac{\sinh(\delta h)}{\delta}C
\right).
$$
Put
$$
B_h=e^{mh}e^{hA_1}.
$$
Then
$$
B_h=
\begin{pmatrix}
e^{\delta h}&\frac{\kappa}{\delta}\sinh(\delta h)\\
0&e^{-\delta h}
\end{pmatrix},
\qquad
\det B_h=1.
$$
Therefore
$$
\operatorname{tr}(B_h^TB_h)
=e^{2\delta h}+e^{-2\delta h}
+\frac{\kappa^2}{\delta^2}\sinh^2(\delta h).
$$
Using
$$
e^{2x}+e^{-2x}=2+4\sinh^2x
$$
and
$$
\eta^2=1+\frac{\kappa^2}{4\delta^2}
=1+\frac{\kappa^2}{(\beta-\alpha)^2},
$$
this becomes
$$
\operatorname{tr}(B_h^TB_h)
=2+4\eta^2\sinh^2(\delta h).
$$
Define
$$
q(h)=\operatorname{arsinh}\left(\eta\sinh(\delta h)\right).
$$
Since
$$
2+4\eta^2\sinh^2(\delta h)=2\cosh(2q(h))
$$
and $\det(B_h^TB_h)=1$, the two eigenvalues of $B_h^TB_h$ are $e^{2q(h)}$ and $e^{-2q(h)}$. Therefore
$$
\|e^{hA_1}\|_2=e^{-mh+q(h)}.
$$
The same norm formula holds for $A_2=A_1^T$.

Differentiate twice:
$$
q''(h)=
\frac{\eta\delta^2(1-\eta^2)\sinh(\delta h)}
{\left(1+\eta^2\sinh^2(\delta h)\right)^{3/2}}
<0
$$
for $h>0$. Thus $q$ is concave and $q(0)=0$, so $q(h)/h$ is strictly decreasing on $(0,\infty)$. Consequently
$$
r(h):=\frac1h\log\|e^{hA_1}\|_2
=-m+\frac{q(h)}h
$$
is strictly decreasing.

Step 2: Bound every switching law with minimum dwell time
Let a switching signal have successive switching times separated by at least $\tau$. Every completed constant-mode interval therefore has length $h\geq\tau$, and Step 1 gives
$$
\|e^{hA_i}\|_2\leq e^{r(\tau)h}
$$
for $i=1,2$.

At an arbitrary observation time there is at most one terminal piece of the currently active interval. If its elapsed length $s\geq\tau$, the same decreasing-rate bound applies directly. If $0\leq s<\tau$, use the finite constant
$$
C_\tau=
\max_{i\in\{1,2\}}\max_{0\leq s\leq\tau}
\left(e^{-r(\tau)s}\|e^{sA_i}\|_2\right).
$$
Submultiplicativity therefore gives, in every case,
$$
\|\Phi_\sigma(t)\|_2\leq C_\tau e^{r(\tau)t}
$$
for every admissible switching signal and every $t\geq0$. Hence
$$
\limsup_{t\to\infty}\frac1t\log\|\Phi_\sigma(t)\|_2
\leq r(\tau),
$$
so
$$
\Lambda_\tau\leq r(\tau).
$$

Step 3: Construct a dwell-time switching law that attains the bound
Alternate periodically between $A_1$ and $A_2$, using each mode for exactly time $\tau$. Put
$$
E=e^{\tau A_1}.
$$
Since $A_2=A_1^T$,
$$
e^{\tau A_2}=E^T.
$$
Thus the monodromy over one period $2\tau$ is
$$
M=E^TE.
$$
This matrix is symmetric positive definite, with
$$
\rho(M)=\|E\|_2^2.
$$
After $n$ periods,
$$
\Phi_\sigma(2n\tau)=M^n,
$$
and therefore
$$
\|\Phi_\sigma(2n\tau)\|_2
=\rho(M)^n
=\|E\|_2^{2n}.
$$
The corresponding asymptotic exponent is exactly
$$
\frac1\tau\log\|e^{\tau A_1}\|_2
=r(\tau).
$$
Hence
$$
\Lambda_\tau\geq r(\tau).
$$
Together with Step 2,
$$
\Lambda_\tau=r(\tau).
$$

Step 4: Write the exact closed form
Substituting $h=\tau$ into the formula from Step 1 yields
$$
\Lambda_\tau
=-\frac{\alpha+\beta}{2}
+\frac1\tau\operatorname{arsinh}
\left(\eta\sinh\frac{(\beta-\alpha)\tau}{2}\right).
$$

Final Answer: $\boxed{-\frac{\alpha+\beta}{2}+\tau^{-1}\operatorname{arsinh}(\eta\sinh((\beta-\alpha)\tau/2))}$

---

## Answer

$-\frac{\alpha+\beta}{2}+\tau^{-1}\operatorname{arsinh}(\eta\sinh((\beta-\alpha)\tau/2))$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- switched linear systems
- minimum dwell time
- singular values of matrix exponentials
- concavity of transient growth rates
- periodic switching monodromy
