## Steps

Step 1: Diagonalize one symmetric matrix

For a conjugation-invariant integrand on $\operatorname{Sym}_3(\mathbb R)$,
$$
\int F(A)\,dA=C\int_{\mathbb R^3}|\Delta(\lambda)|
F(\operatorname{diag}\lambda)\,d\lambda,
\qquad
\Delta(\lambda)=\prod_{i<j}(\lambda_i-\lambda_j).
$$
The infinitesimal off-diagonal directions give the Vandermonde factor. To find $C$, use $F(A)=e^{-\operatorname{tr}(A^2)}$. Directly in the six matrix entries,
$$
\int e^{-\operatorname{tr}(A^2)}\,dA
=\pi^{3/2}\left(\frac\pi2\right)^{3/2}
=\frac{\pi^3}{2^{3/2}}.
$$
The corresponding eigenvalue integral is
$$
\int_{\mathbb R^3}e^{-\sum\lambda_i^2}|\Delta(\lambda)|\,d\lambda
=\frac{3\pi}{2^{3/2}},
$$
obtained by separating the mean eigenvalue and using polar coordinates in the traceless plane. Hence
$$
C=\frac{\pi^2}{3}.
$$

Write $A=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ and
$$
B=\begin{pmatrix}d_1&p&q\\p&d_2&r\\q&r&d_3\end{pmatrix}.
$$
Then
$$
\|AB-BA\|_F^2
=2\sum_{i<j}(\lambda_i-\lambda_j)^2b_{ij}^2,
$$
while
$$
\|A\|_F^2+\|B\|_F^2
=\sum_i\lambda_i^2+\sum_i d_i^2+2(p^2+q^2+r^2).
$$

Step 2: Compute the regular commuting contribution

Away from eigenvalue collisions, $p,q,r$ are Gaussian normal variables. Thus
$$
\int_{\mathbb R}e^{-2n(\lambda_i-\lambda_j)^2u^2}\,du
=\frac{\sqrt\pi}{\sqrt{2n}\,|\lambda_i-\lambda_j|}.
$$
The three factors cancel $|\Delta(\lambda)|$. The remaining six variables are
$$
(\lambda_1,\lambda_2,\lambda_3,d_1,d_2,d_3)\in\mathbb R^6,
$$
so
$$
\int_{\mathbb R^6}e^{-n|z|^8}\,dz
=\frac{\pi^3}{8}\Gamma\left(\frac34\right)n^{-3/4}.
$$
Therefore
$$
I_n=
\frac{\pi^2}{3}\frac{\pi^{3/2}}{2^{3/2}n^{3/2}}
\frac{\pi^3}{8}\Gamma\left(\frac34\right)n^{-3/4}
+o(n^{-9/4}),
$$
that is,
$$
I_n=
\frac{\pi^{13/2}\Gamma(3/4)}{48\sqrt2}\,n^{-9/4}
+o(n^{-9/4}).
$$

Step 3: Isolate one eigenvalue-collision stratum

Consider $\lambda_1=\lambda_2$. Integrating the still-regular variables $q$ and $r$ gives
$$
\frac{\pi}{2n|\lambda_1-\lambda_3||\lambda_2-\lambda_3|},
$$
so the Vandermonde leaves $|\lambda_1-\lambda_2|$.

Put
$$
a=\frac{\lambda_1+\lambda_2}{\sqrt2},\qquad
 g=\frac{\lambda_1-\lambda_2}{\sqrt2},
$$
and let
$$
z=(a,\lambda_3,d_1,d_2,d_3)\in\mathbb R^5.
$$
The collision scale is
$$
z,p\asymp n^{-1/8},\qquad g\asymp n^{-3/8}.
$$
After subtracting the regular Gaussian model for $p$, the scaled collision correction for fixed $z$ is the finite part
$$
K(z)=\frac{\sqrt2}{4}\int_{\mathbb R}
\frac{e^{-(|z|^2+2p^2)^4}-e^{-|z|^8}}{p^2}\,dp.
$$
Indeed, for $p\ne0$ the scaled $g$-integral is
$$
\int_{\mathbb R}\sqrt2|g|e^{-4g^2p^2}\,dg
=\frac{\sqrt2}{4p^2},
$$
and the regular model subtracts precisely the $p=0$ singular part. Splitting at $|p|=\eta$ and then letting $n\to\infty$ followed by $\eta\to0$ gives the displayed finite part.

Step 4: Evaluate the collision finite part

Integrating by parts in $p$ gives
$$
K(z)=-8\sqrt2\int_0^\infty
(|z|^2+2p^2)^3e^{-(|z|^2+2p^2)^4}\,dp.
$$
With $q=\sqrt2p$,
$$
K(z)=-8\int_0^\infty
(|z|^2+q^2)^3e^{-(|z|^2+q^2)^4}\,dq.
$$
Hence
$$
\begin{aligned}
\int_{\mathbb R^5}K(z)\,dz
&=-4\int_{\mathbb R^6}|y|^6e^{-|y|^8}\,dy\\
&=-4\pi^3\int_0^\infty r^{11}e^{-r^8}\,dr\\
&=-\frac{\pi^{7/2}}4.
\end{aligned}
$$
Thus one collision plane contributes
$$
\frac{\pi^2}{3}\frac\pi2
\left(-\frac{\pi^{7/2}}4\right)n^{-5/2}
=-\frac{\pi^{13/2}}{24}n^{-5/2}.
$$
There are three pairwise eigenvalue-collision planes, so their total contribution is
$$
-\frac{\pi^{13/2}}8n^{-5/2}.
$$

Step 5: Exclude smaller strata and recover the limit

On the regular commuting stratum, the first correction from the off-diagonal variables inside the radial term is of relative order $n^{-1/2}$, hence $O(n^{-11/4})$. At a triple eigenvalue collision, the two gap coordinates have scale $n^{-3/8}$, the Vandermonde has degree $3$ in those gaps, and the remaining seven variables have scale $n^{-1/8}$; this again gives $O(n^{-11/4})$. Therefore neither affects the $n^{-5/2}$ term.

Consequently
$$
I_n=
\frac{\pi^{13/2}\Gamma(3/4)}{48\sqrt2}\,n^{-9/4}
-\frac{\pi^{13/2}}8\,n^{-5/2}
+o(n^{-5/2}).
$$
Thus
$$
\lim_{n\to\infty}n^{5/2}
\left(
I_n-
\frac{\pi^{13/2}\Gamma(3/4)}{48\sqrt2\,n^{9/4}}
\right)
=-\frac{\pi^{13/2}}8.
$$
Final Answer: $\boxed{-\frac{\pi^{13/2}}8}$

---

## Answer

$-\frac{\pi^{13/2}}8$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- simultaneous orthogonal invariance
- commuting symmetric matrices
- eigenvalue-collision strata
- finite-part matching
- degenerate Laplace asymptotics
