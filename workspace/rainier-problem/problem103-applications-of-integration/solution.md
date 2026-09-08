## Steps

Step 1: Localize at the astroid cusp

The phase $(x-1)^2+y^2$ has its unique minimum on the astroid at the cusp $(1,0)$. Away from any fixed neighborhood of that point it is bounded below by a positive constant, so those regions contribute exponentially little.

Write
$$
u=1-x,
$$
so near the cusp $u\ge0$ and the astroid boundary is
$$
|y|\le h(u),\qquad
h(u)=\left(1-(1-u)^{2/3}\right)^{3/2}.
$$
Put
$$
\varepsilon=n^{-1/2},\qquad
u=\varepsilon U,\qquad
y=\varepsilon^{3/2}V.
$$
Then
$$
n\left((x-1)^2+y^2\right)=U^2+\varepsilon V^2,
$$
and $du\,dy=\varepsilon^{5/2}dU\,dV$. Hence, up to an exponentially small error,
$$
M_n=\varepsilon^{5/2}\int_0^\infty e^{-U^2}
\int_{-H_\varepsilon(U)}^{H_\varepsilon(U)}
 e^{-\varepsilon V^2}\,dV\,dU,
$$
where
$$
H_\varepsilon(U)=\frac{h(\varepsilon U)}{\varepsilon^{3/2}}.
$$

Step 2: Expand the cusp geometry

The binomial expansion gives
$$
1-(1-u)^{2/3}
=\frac23u+\frac19u^2+O(u^3).
$$
Raising this to the power $3/2$ yields
$$
h(u)=\frac{2\sqrt6}{9}u^{3/2}
+\frac{\sqrt6}{18}u^{5/2}
+O(u^{7/2}).
$$
Therefore
$$
H_\varepsilon(U)
=aU^{3/2}+b\varepsilon U^{5/2}
+O\left(\varepsilon^2U^{7/2}\right),
$$
with
$$
a=\frac{2\sqrt6}{9},\qquad b=\frac{\sqrt6}{18}.
$$
On $U\le\varepsilon^{-1/8}$ this expansion is uniform, while the complementary $e^{-U^2}$ tail is smaller than every power of $\varepsilon$.

Step 3: Expand the vertical Gaussian on the anisotropic scale

For bounded $H$,
$$
\int_{-H}^{H}e^{-\varepsilon V^2}\,dV
=2H-\frac{2}{3}\varepsilon H^3
+O\left(\varepsilon^2H^5\right).
$$
Substituting the expansion of $H_\varepsilon(U)$ gives
$$
\begin{aligned}
\int_{-H_\varepsilon(U)}^{H_\varepsilon(U)}e^{-\varepsilon V^2}\,dV
={}&2aU^{3/2}\\
&+2\varepsilon\left(
 bU^{5/2}-\frac{a^3}{3}U^{9/2}
\right)
+O\left(\varepsilon^2(1+U^{15/2})\right).
\end{aligned}
$$
The remainder is integrable against $e^{-U^2}$, so termwise integration is valid.

Step 4: Evaluate the two surviving coefficients

For $p>-1$,
$$
\int_0^\infty U^p e^{-U^2}\,dU
=\frac12\Gamma\left(\frac{p+1}{2}\right).
$$
Thus
$$
M_n=\varepsilon^{5/2}C_0+\varepsilon^{7/2}C_1+o\left(\varepsilon^{7/2}\right),
$$
where
$$
C_0=a\Gamma\left(\frac54\right)
=\frac{\sqrt6\,\Gamma(1/4)}{18}.
$$
Also
$$
C_1=b\Gamma\left(\frac74\right)
-\frac{a^3}{3}\Gamma\left(\frac{11}{4}\right).
$$
Using
$$
\Gamma\left(\frac74\right)=\frac34\Gamma\left(\frac34\right),
\qquad
\Gamma\left(\frac{11}{4}\right)=\frac{21}{16}\Gamma\left(\frac34\right),
$$
and the values of $a$ and $b$, we obtain
$$
C_1=\frac{25\sqrt6\,\Gamma(3/4)}{1944}.
$$

Step 5: Recover the requested limit

Since $\varepsilon=n^{-1/2}$,
$$
M_n=
\frac{\sqrt6\,\Gamma(1/4)}{18n^{5/4}}
+\frac{25\sqrt6\,\Gamma(3/4)}{1944n^{7/4}}
+o\left(n^{-7/4}\right).
$$
Therefore
$$
\lim_{n\to\infty}n^{7/4}
\left(M_n-\frac{\sqrt6\,\Gamma(1/4)}{18n^{5/4}}\right)
=\frac{25\sqrt6\,\Gamma(3/4)}{1944}.
$$
Final Answer: $\boxed{\frac{25\sqrt6\,\Gamma(3/4)}{1944}}$

---

## Answer

$\frac{25\sqrt6\,\Gamma(3/4)}{1944}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- Gaussian localization at a cusp
- anisotropic scaling
- astroid boundary expansion
- vertical Gaussian correction
- Gamma-function moments
