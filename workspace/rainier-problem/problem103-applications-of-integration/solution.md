## Steps

Step 1: Rescale the quarter-mass condition

Let $D_\lambda$ be the intersection of the two disks
$$
(x-1)^2+y^2\le(1+\lambda)^2,
\qquad
x^2+(y-1)^2\le(1+\lambda)^2.
$$
As $\lambda>-1$ increases, $D_\lambda$ increases strictly once it is nonempty, so its positive Gaussian mass is continuous and strictly increasing from $0$ to $\pi/n$. Hence the required $\lambda_n$ is unique.

Put
$$
\varepsilon=n^{-1/2},\qquad X=\sqrt n\,x,\qquad Y=\sqrt n\,y.
$$
After multiplying the defining equation by $n$, the target mass is $\pi/4$. In the Gaussian main range, the two relevant disk boundaries are
$$
X\ge T_{\varepsilon,\lambda}(Y),
\qquad
Y\ge T_{\varepsilon,\lambda}(X),
$$
where
$$
T_{\varepsilon,\lambda}(z)
=\frac{1-\sqrt{(1+\lambda)^2-\varepsilon^2z^2}}{\varepsilon}.
$$
The opposite disk boundaries are at distance $2\varepsilon^{-1}+O(1)$, and the regions where the square roots cease to be real are also Gaussian tails. Their contributions are exponentially small.

Step 2: Find the leading radius correction

Write temporarily
$$
\lambda=c\varepsilon^2
$$
with bounded $c$. Uniformly on every Gaussian main range,
$$
T_{\varepsilon,\lambda}(z)
=\varepsilon\left(\frac{z^2}{2}-c\right)
+O\left(\varepsilon^3(1+z^4)\right).
$$
At $\varepsilon=0$ the limiting region is the first quadrant, whose Gaussian mass is $\pi/4$.

Consider first the change caused by the $X$-boundary while keeping $Y\ge0$. Using the signed integral convention when $T<0$,
$$
-\int_0^\infty e^{-Y^2}
\int_0^{T_{\varepsilon,\lambda}(Y)}e^{-X^2}\,dX\,dY
=-\varepsilon A(c)+O(\varepsilon^3),
$$
where
$$
A(c)=\int_0^\infty
\left(\frac{Y^2}{2}-c\right)e^{-Y^2}\,dY
=\sqrt\pi\left(\frac18-\frac c2\right).
$$
The $Y$-boundary gives the same contribution.

The two strip corrections overlap only in an $O(\varepsilon)\times O(\varepsilon)$ corner near the origin. There
$$
T_{\varepsilon,\lambda}(0)=-c\varepsilon+O(\varepsilon^3),
$$
so the independent-strip calculation misses the corner square of Gaussian mass
$$
c^2\varepsilon^2+O(\varepsilon^3).
$$
Therefore the scaled mass satisfies
$$
M_\varepsilon(c)
=\frac\pi4
+\sqrt\pi\left(c-\frac14\right)\varepsilon
+c^2\varepsilon^2
+O(\varepsilon^3).
$$
Taking, for example, $c=0$ and $c=1$ shows by monotonicity that the exact root has bounded $c_n=\lambda_n/\varepsilon^2$, and the displayed expansion then gives
$$
c_n=\frac14+O(\varepsilon).
$$
Thus
$$
\lambda_n=\frac14\varepsilon^2+O(\varepsilon^3).
$$

Step 3: Resolve the coupled corner term

Write
$$
\lambda_n=\frac14\varepsilon^2+d_n\varepsilon^3.
$$
Step 2 shows that $d_n=O(1)$. For bounded $d$,
$$
T_{\varepsilon,\lambda}(z)
=\varepsilon\left(\frac{z^2}{2}-\frac14\right)
-d\varepsilon^2
+O\left(\varepsilon^3(1+z^4)\right).
$$
Since
$$
\int_0^\infty
\left(\frac{Y^2}{2}-\frac14\right)e^{-Y^2}\,dY=0,
$$
the signed $X$-strip now contributes
$$
\frac{d\sqrt\pi}{2}\varepsilon^2+O(\varepsilon^3),
$$
and the $Y$-strip contributes the same amount.

The corner correction is determined only by the leading boundary displacement. Since both boundaries satisfy
$$
T_{\varepsilon,\lambda}(0)=-\frac14\varepsilon+O(\varepsilon^2),
$$
the overlap square has side $\varepsilon/4+O(\varepsilon^2)$. Because $e^{-X^2-Y^2}=1+O(\varepsilon^2)$ there, its mass is
$$
\frac1{16}\varepsilon^2+O(\varepsilon^3).
$$
Hence, uniformly for bounded $d$,
$$
M_\varepsilon(d)
=\frac\pi4
+\left(d\sqrt\pi+\frac1{16}\right)\varepsilon^2
+O(\varepsilon^3).
$$

Step 4: Determine the second coefficient

The defining condition is $M_\varepsilon(d_n)=\pi/4$. Therefore
$$
d_n\sqrt\pi+\frac1{16}=O(\varepsilon),
$$
so
$$
d_n\longrightarrow-\frac1{16\sqrt\pi}.
$$
Consequently
$$
\lambda_n
=\frac{1}{4n}
-\frac{1}{16\sqrt\pi\,n^{3/2}}
+o\left(n^{-3/2}\right).
$$

Step 5: Recover the requested limit

Multiplying the preceding expansion by $n^{3/2}$ gives
$$
\lim_{n\to\infty}n^{3/2}
\left(\lambda_n-\frac{1}{4n}\right)
=-\frac1{16\sqrt\pi}.
$$
Final Answer: $\boxed{-\frac{1}{16\sqrt\pi}}$

---

## Answer

$-\frac{1}{16\sqrt\pi}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- Gaussian rescaling
- intersecting tangent disks
- coupled boundary layers
- corner overlap correction
- implicit asymptotic shift
