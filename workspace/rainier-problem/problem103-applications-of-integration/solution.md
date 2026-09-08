## Steps

Step 1: Reduce the discriminant integral to two variables

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
one has
$$
\Delta(x)=-\frac{r^3}{\sqrt2}\cos3\theta.
$$
Therefore
$$
I_n=\frac1{\sqrt2}\int_{-\infty}^{\infty}\int_0^\infty
r^4e^{-n(m^2+r^2)^4}A\left(\frac{nr^6}{2}\right)\,dr\,dm,
$$
where
$$
A(t)=\int_0^{2\pi}|\cos3\theta|e^{-t\cos^2(3\theta)}\,d\theta.
$$
By periodicity,
$$
A(t)=4\int_0^{\pi/2}\cos\phi\,e^{-t\cos^2\phi}\,d\phi
=4e^{-t}\int_0^1e^{ty^2}\,dy.
$$
Hence
$$
A(t)\le C\min(1,t^{-1}),
\qquad
tA(t)\longrightarrow2
$$
as $t\to\infty$.

Step 2: Put the radial part on its natural outer scale

Set
$$
m=n^{-1/8}M,\qquad r=n^{-1/8}R,\qquad \lambda=n^{1/4}.
$$
Then
$$
I_n=\frac{n^{-3/4}}{\sqrt2}J(\lambda),
$$
where
$$
J(\lambda)=\int_0^\infty R^4F(R)A\left(\frac{\lambda R^6}{2}\right)\,dR
$$
and
$$
F(R)=\int_{-\infty}^{\infty}e^{-(M^2+R^2)^4}\,dM.
$$
At the triple-collision line,
$$
F(0)=\int_{-\infty}^{\infty}e^{-M^8}\,dM
=\frac14\Gamma\left(\frac18\right).
$$

Step 3: Extract the exact leading transition term

Write
$$
J(\lambda)=F(0)\int_0^\infty R^4A\left(\frac{\lambda R^6}{2}\right)\,dR
+\int_0^\infty R^4(F(R)-F(0))A\left(\frac{\lambda R^6}{2}\right)\,dR.
$$
For the first integral put $t=\lambda R^6/2$. Then
$$
\int_0^\infty R^4A\left(\frac{\lambda R^6}{2}\right)\,dR
=\frac{2^{5/6}}{6}\lambda^{-5/6}
\int_0^\infty t^{-1/6}A(t)\,dt.
$$
Using the definition of $A$ and Tonelli's theorem,
$$
\begin{aligned}
\int_0^\infty t^{-1/6}A(t)\,dt
&=\Gamma\left(\frac56\right)
\int_0^{2\pi}|\cos3\theta|^{-2/3}\,d\theta\\
&=2\Gamma\left(\frac56\right)
B\left(\frac16,\frac12\right)\\
&=\frac{4\pi^{3/2}}{\Gamma(2/3)}.
\end{aligned}
$$
Here we used
$$
\Gamma\left(\frac16\right)\Gamma\left(\frac56\right)=2\pi.
$$
Thus
$$
J(\lambda)=
\frac{\pi^{3/2}\Gamma(1/8)}{3\,2^{1/6}\Gamma(2/3)}\lambda^{-5/6}
+\text{remainder}.
$$

Step 4: Evaluate the outer finite-part correction

Since $F(R)-F(0)=O(R^2)$ as $R\to0$, while $F$ is bounded, the estimate from Step 1 gives an integrable bound for
$$
\lambda R^4(F(R)-F(0))A\left(\frac{\lambda R^6}{2}\right).
$$
Also, for each fixed $R>0$,
$$
\lambda A\left(\frac{\lambda R^6}{2}\right)\longrightarrow\frac4{R^6}.
$$
Dominated convergence therefore yields
$$
\lambda\left[J(\lambda)-
\frac{\pi^{3/2}\Gamma(1/8)}{3\,2^{1/6}\Gamma(2/3)}\lambda^{-5/6}
\right]
=4\int_0^\infty\frac{F(R)-F(0)}{R^2}\,dR+o(1).
$$
Integrating by parts,
$$
\int_0^\infty\frac{F(R)-F(0)}{R^2}\,dR
=\int_0^\infty\frac{F'(R)}R\,dR.
$$
Now
$$
F'(R)=-8R\int_{-\infty}^{\infty}(M^2+R^2)^3e^{-(M^2+R^2)^4}\,dM.
$$
Hence, using polar coordinates in the half-plane $R\ge0$,
$$
\begin{aligned}
\int_0^\infty\frac{F'(R)}R\,dR
&=-8\int_0^\infty\int_{-\infty}^{\infty}
(M^2+R^2)^3e^{-(M^2+R^2)^4}\,dM\,dR\\
&=-8\pi\int_0^\infty \rho^7e^{-\rho^8}\,d\rho\\
&=-\pi.
\end{aligned}
$$
Therefore
$$
J(\lambda)=
\frac{\pi^{3/2}\Gamma(1/8)}{3\,2^{1/6}\Gamma(2/3)}\lambda^{-5/6}
-4\pi\lambda^{-1}+o(\lambda^{-1}).
$$

Step 5: Recover the requested limit

Since $\lambda=n^{1/4}$,
$$
I_n=
\frac{\pi^{3/2}\Gamma(1/8)}{3\,2^{2/3}\Gamma(2/3)}n^{-23/24}
-2\sqrt2\,\pi\,n^{-1}
+o(n^{-1}).
$$
Therefore
$$
\lim_{n\to\infty}n\left(
I_n-
\frac{\pi^{3/2}\Gamma(1/8)}{3\,2^{2/3}\Gamma(2/3)n^{23/24}}
\right)
=-2\sqrt2\,\pi.
$$
Final Answer: $\boxed{-2\sqrt2\,\pi}$

---

## Answer

$-2\sqrt2\,\pi$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- eigenvalue discriminant geometry
- triple-collision transition layer
- nonuniform asymptotic matching
- finite-part correction
- Gamma-function moments
