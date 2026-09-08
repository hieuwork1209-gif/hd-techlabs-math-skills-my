## Steps

Step 1: Separate the mean eigenvalue and evaluate the angular integral

Use the orthonormal coordinates
$$
x_1=\frac m{\sqrt3}+\frac u{\sqrt2}+\frac v{\sqrt6},\qquad
x_2=\frac m{\sqrt3}-\frac u{\sqrt2}+\frac v{\sqrt6},
$$
$$
x_3=\frac m{\sqrt3}-\frac{2v}{\sqrt6}.
$$
Then
$$
x_1^2+x_2^2+x_3^2=m^2+u^2+v^2.
$$
Writing
$$
u=r\cos\theta,\qquad v=r\sin\theta,
$$
one also has
$$
\Delta(x)=-\frac{r^3}{\sqrt2}\cos3\theta.
$$
Hence
$$
\begin{aligned}
I_n={}&\int_{-\infty}^{\infty}\int_0^\infty
\frac{r^4}{\sqrt2}e^{-n(m^2+r^2)^4}\\
&\qquad\times
\left(\int_0^{2\pi}|\cos3\theta|
 e^{-nr^6\cos^2(3\theta)/2}\,d\theta\right)dr\,dm.
\end{aligned}
$$
For $a>0$, periodicity gives
$$
\int_0^{2\pi}|\cos3\theta|e^{-a\cos^2(3\theta)}\,d\theta
=4\int_0^{\pi/2}\cos t\,e^{-a\cos^2t}\,dt
=\frac{2\sqrt\pi}{\sqrt a}\operatorname{erf}(\sqrt a).
$$
Therefore the exact reduction is
$$
I_n=\frac{2\sqrt\pi}{\sqrt n}
\int_{-\infty}^{\infty}\int_0^\infty
r\,e^{-n(m^2+r^2)^4}
\operatorname{erf}\left(\sqrt{\frac n2}\,r^3\right)dr\,dm.
$$

Step 2: Compute the outer repeated-eigenvalue contribution

Replace the error function in Step 1 by its limiting value $1$. The resulting integral is
$$
L_n=\frac{2\sqrt\pi}{\sqrt n}
\int_{-\infty}^{\infty}\int_0^\infty
r\,e^{-n(m^2+r^2)^4}\,dr\,dm.
$$
Using polar coordinates in the half-plane $(m,r)$,
$$
\int_{-\infty}^{\infty}\int_0^\infty
r\,e^{-n(m^2+r^2)^4}\,dr\,dm
=2\int_0^\infty \rho^2e^{-n\rho^8}\,d\rho
=\frac14\Gamma\left(\frac38\right)n^{-3/8}.
$$
Thus
$$
L_n=\frac{\sqrt\pi\,\Gamma(3/8)}{2n^{7/8}}.
$$
This is the contribution from the regular part of the repeated-eigenvalue sheets.

Step 3: Isolate the triple-collision transition layer

Let
$$
D_n=I_n-L_n.
$$
Since $1-\operatorname{erf}=\operatorname{erfc}$,
$$
D_n=-\frac{2\sqrt\pi}{\sqrt n}
\int_{-\infty}^{\infty}\int_0^\infty
r\,e^{-n(m^2+r^2)^4}
\operatorname{erfc}\left(\sqrt{\frac n2}\,r^3\right)dr\,dm.
$$
The transition of the complementary error function occurs at
$$
r\asymp n^{-1/6},
$$
while the mean direction remains on the outer scale
$$
m\asymp n^{-1/8}.
$$
Set
$$
m=n^{-1/8}M,\qquad r=n^{-1/6}S.
$$
Then
$$
\begin{aligned}
n^{23/24}D_n=-2\sqrt\pi
\int_{-\infty}^{\infty}\int_0^\infty
&S\,\exp\left(-(M^2+n^{-1/12}S^2)^4\right)\\
&\times\operatorname{erfc}\left(\frac{S^3}{\sqrt2}\right)dS\,dM.
\end{aligned}
$$
The integrand is dominated by
$$
e^{-M^8}S\operatorname{erfc}\left(\frac{S^3}{\sqrt2}\right),
$$
which is integrable. Hence dominated convergence gives
$$
\lim_{n\to\infty}n^{23/24}D_n
=-2\sqrt\pi
\left(\int_{-\infty}^{\infty}e^{-M^8}\,dM\right)
\left(\int_0^\infty S\operatorname{erfc}\left(\frac{S^3}{\sqrt2}\right)dS\right).
$$

Step 4: Evaluate the two transition integrals

First,
$$
\int_{-\infty}^{\infty}e^{-M^8}\,dM
=\frac14\Gamma\left(\frac18\right).
$$
For the second integral, put $t=S^3/\sqrt2$. Then
$$
\int_0^\infty S\operatorname{erfc}\left(\frac{S^3}{\sqrt2}\right)dS
=\frac{2^{1/3}}3\int_0^\infty t^{-1/3}\operatorname{erfc}(t)\,dt.
$$
Using
$$
\operatorname{erfc}(t)=\frac2{\sqrt\pi}\int_t^\infty e^{-u^2}\,du
$$
and reversing the order of integration,
$$
\int_0^\infty t^{-1/3}\operatorname{erfc}(t)\,dt
=\frac{3}{2\sqrt\pi}\Gamma\left(\frac56\right).
$$
Therefore
$$
\int_0^\infty S\operatorname{erfc}\left(\frac{S^3}{\sqrt2}\right)dS
=\frac{2^{1/3}}{2\sqrt\pi}\Gamma\left(\frac56\right).
$$
Substituting into Step 3 yields
$$
\lim_{n\to\infty}n^{23/24}D_n
=-\frac{\Gamma(1/8)\Gamma(5/6)}{2^{5/3}}.
$$

Step 5: Recover the requested limit

Combining Steps 2--4,
$$
I_n=\frac{\sqrt\pi\,\Gamma(3/8)}{2n^{7/8}}
-\frac{\Gamma(1/8)\Gamma(5/6)}{2^{5/3}n^{23/24}}
+o(n^{-23/24}).
$$
Therefore
$$
\lim_{n\to\infty}n^{23/24}
\left(
I_n-\frac{\sqrt\pi\,\Gamma(3/8)}{2n^{7/8}}
\right)
=-\frac{\Gamma(1/8)\Gamma(5/6)}{2^{5/3}}.
$$
Final Answer: $\boxed{-\frac{\Gamma(1/8)\Gamma(5/6)}{2^{5/3}}}$

---

## Answer

$-\frac{\Gamma(1/8)\Gamma(5/6)}{2^{5/3}}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- eigenvalue discriminant geometry
- exact angular reduction
- repeated-eigenvalue sheets
- triple-collision transition layer
- Gamma-function moments
