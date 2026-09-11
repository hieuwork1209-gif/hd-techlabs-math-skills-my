## Steps

Step 1: Convert the moment constraint into a boundary condition

Let
$$
H=\left\{f\in L^2(0,1):\int_0^1 x f(x)\,dx=0\right\},
\qquad
(Tf)(x)=\int_0^x f(t)\,dt.
$$
For $f\in H$, put $y=Tf$. Then $y\in H^1(0,1)$, $y(0)=0$, and $y'=f$ almost everywhere. Integration by parts gives
$$
0=\int_0^1 x y'(x)\,dx
=y(1)-\int_0^1 y(x)\,dx.
$$
Thus $T$ identifies $H$ with
$$
\mathcal Y=\left\{y\in H^1(0,1):y(0)=0,\quad y(1)=\int_0^1y(x)\,dx\right\},
$$
and under this identification
$$
\|f\|_2=\|y'\|_2,
\qquad
\|Tf\|_2=\|y\|_2.
$$
Conversely, every $y\in\mathcal Y$ has $f=y'\in H$ and $Tf=y$, so
$$
\|T|_H\|^2
=\sup_{0\ne y\in\mathcal Y}\frac{\|y\|_2^2}{\|y'\|_2^2}
=\frac1{\lambda_1},
$$
where
$$
\lambda_1:=\inf_{0\ne y\in\mathcal Y}
\frac{\int_0^1|y'|^2}{\int_0^1|y|^2}.
$$

Step 2: Prove that the Rayleigh minimum is positive and attained

If $y(0)=0$, then
$$
|y(x)|=\left|\int_0^x y'(t)\,dt\right|
\le \sqrt{x}\,\|y'\|_2,
$$
so
$$
\|y\|_2^2\le\frac12\|y'\|_2^2.
$$
Hence $\lambda_1\ge2>0$.

Take a minimizing sequence $y_n\in\mathcal Y$ with $\|y_n\|_2=1$. The preceding estimate and the minimizing property bound $\|y_n\|_{H^1}$. After passing to a subsequence, $y_n\rightharpoonup y$ weakly in $H^1(0,1)$ and $y_n\to y$ strongly in $L^2(0,1)$ by compactness of the embedding $H^1(0,1)\hookrightarrow L^2(0,1)$. The trace $y\mapsto y(1)$ and the functional $y\mapsto\int_0^1y$ are continuous on $H^1$, so $\mathcal Y$ is weakly closed. Therefore $y\in\mathcal Y$, $\|y\|_2=1$, and weak lower semicontinuity gives
$$
\|y'\|_2^2\le\liminf_n\|y_n'\|_2^2=\lambda_1.
$$
Thus the infimum is attained.

Step 3: Derive the Euler equation including the nonlocal constraint

Let
$$
V=\{h\in H^1(0,1):h(0)=0\},
\qquad
C(h)=h(1)-\int_0^1h(x)\,dx.
$$
Then $\mathcal Y=\ker C$. For a normalized minimizer $y$, first variation along every $h\in\ker C$ gives
$$
\int_0^1 y'h'\,dx=\lambda_1\int_0^1 yh\,dx.
$$
Hence the continuous linear functional
$$
h\longmapsto\int_0^1 y'h'\,dx-\lambda_1\int_0^1yh\,dx
$$
vanishes on $\ker C$ and therefore equals $\mu C(h)$ for some real $\mu$. Thus for every $h\in V$,
$$
\int_0^1 y'h'\,dx-\lambda_1\int_0^1yh\,dx
=\mu\left(h(1)-\int_0^1h\,dx\right).
$$
Testing first with compactly supported $h$ shows, in the distributional sense,
$$
y''+\lambda_1y=\mu.
$$
Consequently $y$ is smooth. Integrating by parts in the full identity and using $h(0)=0$ then gives the endpoint condition
$$
y'(1)=\mu.
$$
Together with membership in $\mathcal Y$, every extremizer satisfies
$$
y''+\lambda_1y=\mu,\qquad
y(0)=0,\qquad y'(1)=\mu,\qquad
y(1)=\int_0^1y.
$$

Step 4: Obtain the exact characteristic equation

Write $\lambda_1=\kappa^2$ with $\kappa>0$. The general solution of
$$
y''+\kappa^2y=\mu,\qquad y(0)=0,
$$
is
$$
y(x)=A\sin(\kappa x)+\frac{\mu}{\kappa^2}\bigl(1-\cos(\kappa x)\bigr).
$$
The condition $y'(1)=\mu$ is
$$
A\kappa\cos\kappa
+\mu\left(\frac{\sin\kappa}{\kappa}-1\right)=0.
$$
Also
$$
y(1)-\int_0^1y(x)\,dx
=A\left(\sin\kappa-\frac{1-\cos\kappa}{\kappa}\right)
+\frac{\mu}{\kappa^2}\left(-\cos\kappa+\frac{\sin\kappa}{\kappa}\right),
$$
so the nonlocal boundary condition gives a second homogeneous equation in $(A,\mu)$. A nonzero extremizer exists exactly when the determinant vanishes:
$$
\det\begin{pmatrix}
\kappa\cos\kappa & \dfrac{\sin\kappa}{\kappa}-1\\[1.2ex]
\sin\kappa-\dfrac{1-\cos\kappa}{\kappa} &
\dfrac{-\cos\kappa+\sin\kappa/\kappa}{\kappa^2}
\end{pmatrix}=0.
$$
Multiplying this determinant by $\kappa^3$ and simplifying gives
$$
\kappa\Bigl((\kappa^2+1)\sin\kappa+\kappa\cos\kappa-2\kappa\Bigr)=0.
$$
Since $\kappa>0$, the characteristic equation is
$$
(\kappa^2+1)\sin\kappa+\kappa\cos\kappa-2\kappa=0.
$$

Step 5: Prove that the least positive root is exactly the minimizing frequency

Conversely, let $k>0$ satisfy
$$
(k^2+1)\sin k+k\cos k-2k=0.
$$
The determinant in Step 4 is then zero, so there is a nonzero pair $(A,\mu)$ producing a nonzero function
$$
y(x)=A\sin(kx)+\frac{\mu}{k^2}(1-\cos(kx))
$$
that satisfies
$$
y(0)=0,\qquad y'(1)=\mu,\qquad y(1)=\int_0^1y,\qquad y''+k^2y=\mu.
$$
Multiplying the differential equation by $y$ and integrating yields
$$
\bigl[y'y\bigr]_0^1-\int_0^1|y'|^2+k^2\int_0^1|y|^2
=\mu\int_0^1y.
$$
Because $y(0)=0$, $y'(1)=\mu$, and $y(1)=\int_0^1y$, the boundary term cancels the right-hand side. Hence
$$
\int_0^1|y'|^2=k^2\int_0^1|y|^2.
$$
Therefore every positive root $k$ produces an admissible Rayleigh quotient $k^2$, while the minimizing extremizer from Steps 2--4 produces the root $\kappa=\sqrt{\lambda_1}$. It follows that $\kappa$ is precisely the smallest positive root of the characteristic equation.

Consequently
$$
\|T|_H\|=\frac1{\sqrt{\lambda_1}}=\frac1\kappa.
$$
For a numerical check, the least positive root is $\kappa\approx1.8732066665091482$, giving $\|T|_H\|\approx0.533843925434864$.

## Solution Concepts

- Volterra operator as a Sobolev antiderivative and conversion of a moment constraint into a nonlocal boundary condition.
- Constrained Rayleigh quotient, compactness, and existence of a norm-attaining extremizer.
- Lagrange-multiplier boundary-value equation and exact characteristic determinant.

Final Answer: $\displaystyle \frac1\kappa$, where $\kappa$ is the smallest positive solution of $(\kappa^2+1)\sin\kappa+\kappa\cos\kappa-2\kappa=0$.