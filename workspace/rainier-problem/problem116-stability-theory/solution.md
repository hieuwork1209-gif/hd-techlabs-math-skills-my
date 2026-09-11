## Steps

Step 1: Symmetrize the gains and remove the common scalar decay
Let
$$
A_1=\begin{pmatrix}-1&a\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\b&-1\end{pmatrix},
\qquad a,b>0,
$$
and let the switching mode be the two-state continuous-time Markov chain that jumps from either state to the other at rate $1$.

Put
$$
p=\sqrt{ab},
\qquad
D=\operatorname{diag}(\sqrt b,\sqrt a).
$$
With $y=Dz$,
$$
\dot y=B_{\sigma(t)}y,
\qquad
B_1=\begin{pmatrix}-1&p\\0&-1\end{pmatrix},
\qquad
B_2=\begin{pmatrix}-1&0\\p&-1\end{pmatrix}.
$$
Thus the almost-sure exponential growth rate depends on $(a,b)$ only through $p=\sqrt{ab}$.

Now write
$$
y(t)=e^{-t}x(t).
$$
Then
$$
\dot x=pE_{\sigma(t)}x,
\qquad
E_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
E_2=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$
If $\lambda_x$ denotes the top almost-sure exponential growth rate of this shear system, then the top exponent of the original system is
$$
\Lambda(p)=-1+\lambda_x.
$$

Step 2: Find the stationary law of the projective process
Start with a vector in the positive quadrant and set
$$
r=\frac{x_2}{x_1}>0.
$$
In mode $1$,
$$
\dot r=-pr^2,
$$
while in mode $2$,
$$
\dot r=p.
$$
Hence $(r,\sigma)$ is a piecewise-deterministic Markov process on $(0,\infty)\times\{1,2\}$.

Let $f_1,f_2$ be stationary densities for $r$ conditional on the two modes. The stationary transport equations are
$$
0=\frac d{dr}(pr^2f_1)-f_1+f_2,
$$
$$
0=-\frac d{dr}(pf_2)+f_1-f_2.
$$
Adding them shows that the stationary probability flux is constant. Integrability at $0$ and $\infty$ forces this constant to be zero, so
$$
f_2=r^2f_1.
$$
Substituting into the first equation and writing $g=r^2f_1$ gives
$$
p g'+\left(1-\frac1{r^2}\right)g=0.
$$
Therefore
$$
g(r)=C\exp\left[-\frac1p\left(r+\frac1r\right)\right],
$$
and hence
$$
f_1(r)=Cr^{-2}\exp\left[-\frac1p\left(r+\frac1r\right)\right],
$$
$$
f_2(r)=C\exp\left[-\frac1p\left(r+\frac1r\right)\right].
$$
These densities are integrable at both endpoints, so after normalization they give the unique invariant probability law of the irreducible projective process.

For $q>0$, use the integral representation
$$
K_\nu(q)=\frac12\int_0^\infty r^{\nu-1}
\exp\left[-\frac q2\left(r+\frac1r\right)\right]dr
$$
for the modified Bessel function of the second kind. Since $K_{-1}=K_1$,
$$
1=C\int_0^\infty(1+r^{-2})e^{-(r+1/r)/p}\,dr
=4C K_1(2/p).
$$
Thus
$$
C=\frac1{4K_1(2/p)}.
$$

Step 3: Compute the top Lyapunov exponent
For either switching mode,
$$
\frac d{dt}\log\|x\|_2
=\frac{x^T\dot x}{\|x\|_2^2}
=p\frac{x_1x_2}{x_1^2+x_2^2}
=p\frac{r}{1+r^2}.
$$
The projective process is ergodic, so its time average equals the stationary average almost surely. Therefore
$$
\lambda_x
=p\int_0^\infty\frac{r}{1+r^2}(f_1(r)+f_2(r))\,dr.
$$
Using
$$
\frac{r}{1+r^2}(r^{-2}+1)=\frac1r,
$$
we get
$$
\lambda_x
=pC\int_0^\infty r^{-1}e^{-(r+1/r)/p}\,dr
=2pC K_0(2/p).
$$
Hence
$$
\lambda_x
=\frac p2\frac{K_0(2/p)}{K_1(2/p)},
$$
and so
$$
\Lambda(p)
=-1+\frac p2\frac{K_0(2/p)}{K_1(2/p)}.
$$

Step 4: Relate the top exponent to every initial state
Every fundamental matrix of the $x$-system has nonnegative entries. For any such matrix $M$,
$$
\|M\|_1\le \|M(1,1)^T\|_1.
$$
Thus the exponential growth rate obtained from a positive initial vector also controls the operator norm and hence every deterministic initial state. Conversely, a positive initial vector realizes the top exponent. The initial Markov mode affects only a transient because the two-state chain is irreducible.

Therefore the original system is almost surely exponentially stable exactly when
$$
\Lambda(p)<0.
$$
At equality the top exponent is zero, so no strictly negative almost-sure exponential rate exists; if $\Lambda(p)>0$, a positive initial state has positive almost-sure growth exponent.

Step 5: State the exact parameter region
Since $p=\sqrt{ab}$, the condition $\Lambda(p)<0$ is
$$
\sqrt{ab}\,K_0\left(\frac{2}{\sqrt{ab}}\right)
<2K_1\left(\frac{2}{\sqrt{ab}}\right).
$$
Thus the exact region is
$$
\left\{(a,b):a,b>0,\ \sqrt{ab}K_0(2/\sqrt{ab})<2K_1(2/\sqrt{ab})\right\}.
$$
Final Answer: $\boxed{\{(a,b):a,b>0,\sqrt{ab}K_0(2/\sqrt{ab})<2K_1(2/\sqrt{ab})\}}$

---

## Answer

$\{(a,b):a,b>0,\sqrt{ab}K_0(2/\sqrt{ab})<2K_1(2/\sqrt{ab})\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- Markov jump linear systems
- almost-sure exponential stability
- projective piecewise-deterministic Markov processes
- stationary densities
- modified Bessel functions

---

## Black-Box Audit — no issues found
