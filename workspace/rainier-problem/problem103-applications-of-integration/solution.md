## Steps

Step 1: Localize near the osculation point

Let
$$
h(x)=\frac{1-\sqrt{1-4x^2}}{2}.
$$
The graph $y=h(x)$ is the lower arc of the circle
$$
x^2+\left(y-\frac12\right)^2=\frac14,
$$
and it has the same tangent and curvature at the origin as the parabola $y=x^2$.

Put
$$
\varepsilon=n^{-1/2}.
$$
Since the factor $e^{-nx^2}$ localizes the $x$-integral to $|x|=O(\varepsilon)$, set
$$
x=\varepsilon X,\qquad y=\varepsilon^2 Z.
$$
Then
$$
M_n=\varepsilon^3\int_{-1/(2\varepsilon)}^{1/(2\varepsilon)}e^{-X^2}
\int_{X^2}^{h(\varepsilon X)/\varepsilon^2}
e^{-\varepsilon^2Z^2}\,dZ\,dX.
$$
For any fixed power of $\varepsilon$, the contribution from $|X|>\varepsilon^{-1/4}$ is smaller because of the Gaussian factor $e^{-X^2}$. Hence all expansions below may be made uniformly on $|X|\le\varepsilon^{-1/4}$ and then extended to the whole real line with an $o(\varepsilon^7)$ error.

Step 2: Use the quartic contact of the two curves

The binomial expansion gives
$$
h(x)=x^2+x^4+2x^6+O(x^8).
$$
Therefore
$$
\frac{h(\varepsilon X)}{\varepsilon^2}
=X^2+\varepsilon^2X^4+2\varepsilon^4X^6
+O\left(\varepsilon^6X^8\right).
$$
Write the width of the scaled vertical interval as
$$
\Delta_\varepsilon(X)
=\varepsilon^2X^4+2\varepsilon^4X^6
+O\left(\varepsilon^6X^8\right).
$$
The quartic term is the first nonzero separation because the circle is the osculating circle of the parabola at the origin.

Step 3: Expand the vertical Gaussian across the thin strip

On the interval
$$
X^2\le Z\le X^2+\Delta_\varepsilon(X),
$$
we have
$$
e^{-\varepsilon^2Z^2}
=1-\varepsilon^2X^4
+O\left(\varepsilon^4(1+|X|^{12})\right),
$$
uniformly on the Gaussian main range. Since the interval width is $O(\varepsilon^2(1+|X|^4))$, integrating across it gives
$$
\begin{aligned}
\int_{X^2}^{X^2+\Delta_\varepsilon(X)}e^{-\varepsilon^2Z^2}\,dZ
={}&\varepsilon^2X^4\\
&+\varepsilon^4\left(2X^6-X^8\right)
+O\left(\varepsilon^6(1+|X|^{16})\right).
\end{aligned}
$$
Substituting this into Step 1 yields
$$
\begin{aligned}
M_n={}&\varepsilon^5\int_{-\infty}^{\infty}X^4e^{-X^2}\,dX\\
&+\varepsilon^7\int_{-\infty}^{\infty}
\left(2X^6-X^8\right)e^{-X^2}\,dX
+o(\varepsilon^7).
\end{aligned}
$$

Step 4: Evaluate the Gaussian moments

The even Gaussian moments are
$$
\int_{-\infty}^{\infty}X^4e^{-X^2}\,dX
=\frac{3\sqrt\pi}{4},
$$
$$
\int_{-\infty}^{\infty}X^6e^{-X^2}\,dX
=\frac{15\sqrt\pi}{8},
\qquad
\int_{-\infty}^{\infty}X^8e^{-X^2}\,dX
=\frac{105\sqrt\pi}{16}.
$$
Hence
$$
\int_{-\infty}^{\infty}
\left(2X^6-X^8\right)e^{-X^2}\,dX
=\left(\frac{30}{8}-\frac{105}{16}\right)\sqrt\pi
=-\frac{45\sqrt\pi}{16}.
$$
Therefore
$$
M_n
=\frac{3\sqrt\pi}{4}\varepsilon^5
-\frac{45\sqrt\pi}{16}\varepsilon^7
+o(\varepsilon^7).
$$

Step 5: Recover the requested limit

Since $\varepsilon=n^{-1/2}$,
$$
M_n
=\frac{3\sqrt\pi}{4n^{5/2}}
-\frac{45\sqrt\pi}{16n^{7/2}}
+o\left(n^{-7/2}\right).
$$
Thus
$$
\lim_{n\to\infty}n^{7/2}
\left(M_n-\frac{3\sqrt\pi}{4n^{5/2}}\right)
=-\frac{45\sqrt\pi}{16}.
$$
Final Answer: $\boxed{-\frac{45\sqrt\pi}{16}}$

---

## Answer

$-\frac{45\sqrt\pi}{16}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- Gaussian localization
- osculating-circle geometry
- quartic contact asymptotics
- thin-strip rescaling
- Gaussian moment expansion
