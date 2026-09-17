## Steps

Step 1: Compute the exact finite-time growth of one mode
Let
$$
m=\frac{\alpha+\beta}{2},
\qquad
s=\frac{\beta-\alpha}{2},
$$
so
$$
A_1=-mI+C,
\qquad
C=\begin{pmatrix}s&\kappa\\0&-s\end{pmatrix},
\qquad
C^2=s^2I.
$$
First suppose $s\neq0$, and put $d=|s|$. Then
$$
e^{hA_1}=e^{-mh}
\left(
\cosh(sh)I+\frac{\sinh(sh)}{s}C
\right).
$$
With
$$
B_h=e^{mh}e^{hA_1},
$$
one has
$$
B_h=
\begin{pmatrix}
e^{sh}&\frac{\kappa}{s}\sinh(sh)\\
0&e^{-sh}
\end{pmatrix},
\qquad
\det B_h=1.
$$
Therefore
$$
\operatorname{tr}(B_h^TB_h)
=e^{2sh}+e^{-2sh}
+\frac{\kappa^2}{s^2}\sinh^2(sh).
$$
Since this expression is unchanged when $s$ is replaced by $d$, define
$$
\eta=\sqrt{1+\frac{\kappa^2}{4d^2}},
\qquad
q(h)=\operatorname{arsinh}\left(\eta\sinh(dh)\right).
$$
Using $e^{2x}+e^{-2x}=2+4\sinh^2x$ gives
$$
\operatorname{tr}(B_h^TB_h)=2\cosh(2q(h)).
$$
Since $\det(B_h^TB_h)=1$, its eigenvalues are $e^{2q(h)}$ and $e^{-2q(h)}$. Hence
$$
\|e^{hA_1}\|_2=e^{-mh+q(h)}.
$$
Moreover,
$$
q''(h)=
\frac{\eta d^2(1-\eta^2)\sinh(dh)}
{\left(1+\eta^2\sinh^2(dh)\right)^{3/2}}
<0
$$
for $h>0$.

If $s=0$, then $C^2=0$ and
$$
B_h=I+hC=
\begin{pmatrix}1&\kappa h\\0&1\end{pmatrix}.
$$
Now
$$
\operatorname{tr}(B_h^TB_h)=2+\kappa^2h^2
=2\cosh\left(2\operatorname{arsinh}\frac{\kappa h}{2}\right).
$$
Thus in this case
$$
\|e^{hA_1}\|_2
=e^{-mh+q(h)},
\qquad
q(h)=\operatorname{arsinh}\frac{\kappa h}{2},
$$
and
$$
q''(h)=
-\frac{(\kappa/2)^3h}{\left(1+(\kappa h/2)^2\right)^{3/2}}<0
$$
for $h>0$.

In both cases $q$ is concave with $q(0)=0$, so $q(h)/h$ is strictly decreasing. Therefore
$$
r(h):=\frac1h\log\|e^{hA_1}\|_2
=-m+\frac{q(h)}h
$$
is strictly decreasing on $(0,\infty)$. Since $A_2=A_1^T$, the same norm formula holds for $e^{hA_2}$.

Step 2: Bound every switching law with minimum dwell time
Let a switching signal have successive switching times separated by at least $\tau$. Every completed constant-mode interval therefore has length $h\geq\tau$, and Step 1 gives
$$
\|e^{hA_i}\|_2\leq e^{r(\tau)h}
$$
for $i=1,2$.

At an arbitrary observation time there is at most one terminal piece of the currently active interval. If its elapsed length $u\geq\tau$, the same decreasing-rate bound applies directly. If $0\leq u<\tau$, use the finite constant
$$
C_\tau=
\max_{i\in\{1,2\}}\max_{0\leq u\leq\tau}
\left(e^{-r(\tau)u}\|e^{uA_i}\|_2\right).
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

Step 4: Record the exact answer and its parameter form
The equality from Step 3 gives the compact exact answer directly. When $\alpha\neq\beta$, Step 1 also gives
$$
\Lambda_\tau
=-\frac{\alpha+\beta}{2}
+\frac1\tau\operatorname{arsinh}
\left(
\sqrt{1+\frac{\kappa^2}{(\beta-\alpha)^2}}
\sinh\frac{|\beta-\alpha|\tau}{2}
\right).
$$
When $\alpha=\beta$, the corresponding formula is
$$
\Lambda_\tau
=-\alpha+\frac1\tau\operatorname{arsinh}\frac{\kappa\tau}{2}.
$$

Final Answer: $\boxed{\tau^{-1}\log\|e^{\tau A_1}\|_2}$

---

## Answer

$\tau^{-1}\log\|e^{\tau A_1}\|_2$

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
