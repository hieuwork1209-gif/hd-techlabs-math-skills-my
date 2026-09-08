## Steps

Step 1: Compute the leading rank-three contribution

Write
$$
\Delta_3(x_1,x_2,x_3)=\prod_{1\le i<j\le3}(x_i-x_j).
$$
Near the hyperplane $x_4=0$, with $x_1x_2x_3\ne0$,
$$
|\Delta(x)|=|\Delta_3(x_1,x_2,x_3)|\,|x_1x_2x_3|+o(1)
$$
in the normal scale, while
$$
\int_{-\infty}^{\infty}
 e^{-n(x_1x_2x_3)^2x_4^2}\,dx_4
=\frac{\sqrt\pi}{\sqrt n\,|x_1x_2x_3|}.
$$
Thus one rank-three hyperplane contributes
$$
\frac{\sqrt\pi}{\sqrt n}
\int_{\mathbb R^3}|\Delta_3(x)|
 e^{-n(x_1^2+x_2^2+x_3^2)^5}\,dx.
$$
After the scaling $x=n^{-1/10}X$, this becomes
$$
\sqrt\pi\,n^{-11/10}
\int_{\mathbb R^3}|\Delta_3(X)|e^{-(X_1^2+X_2^2+X_3^2)^5}\,dX.
$$

To evaluate the radial integral, first note that the orthonormal coordinates
$$
X_1=\frac m{\sqrt3}+\frac u{\sqrt2}+\frac v{\sqrt6},\quad
X_2=\frac m{\sqrt3}-\frac u{\sqrt2}+\frac v{\sqrt6},\quad
X_3=\frac m{\sqrt3}-\frac{2v}{\sqrt6}
$$
give, for $u=r\cos\theta$, $v=r\sin\theta$,
$$
|\Delta_3|=\frac{r^3}{\sqrt2}|\cos3\theta|.
$$
Hence
$$
\int_{\mathbb R^3}e^{-|X|^2}|\Delta_3(X)|\,dX
=\frac{3\pi}{2^{3/2}}.
$$
Since $|\Delta_3|$ is homogeneous of degree $3$, its spherical angular factor is therefore $3\pi/2^{3/2}$. Consequently
$$
\int_{\mathbb R^3}|\Delta_3(X)|e^{-|X|^{10}}\,dX
=\frac{3\pi}{2^{3/2}}
\int_0^\infty r^5e^{-r^{10}}\,dr
=\frac{3\pi\Gamma(3/5)}{10\,2^{3/2}}.
$$
There are four rank-three hyperplanes, so
$$
I_n=
\frac{3\pi^{3/2}\Gamma(3/5)}{5\sqrt2}\,n^{-11/10}
+o(n^{-11/10}).
$$

Step 2: Extract the rank-two finite part

The rank-three approximation is nonuniform where two coordinates vanish. Consider the intersection $x_3=x_4=0$ and keep the two surviving coordinates $x,y$. In the local scale,
$$
|\Delta(x,y,u,v)|
=|x-y|\,|x|^2|y|^2|u-v|+o(1),
$$
and the determinant term is
$$
nx^2y^2u^2v^2.
$$
The two rank-three models meeting on this intersection must be subtracted. Their universal transverse finite part is
$$
K_0=\lim_{L\to\infty}\left[
\int_{-L}^L\int_{-L}^L|a-b|e^{-a^2b^2}\,da\,db
-4L\sqrt\pi
\right].
$$
Splitting into same-sign and opposite-sign quadrants gives
$$
\int_{-L}^L\int_{-L}^L|a-b|e^{-a^2b^2}\,da\,db
=8\int_0^L a\int_0^a e^{-a^2b^2}\,db\,da.
$$
With $t=ab$ and then reversing the order,
$$
8\int_0^L a\int_0^a e^{-a^2b^2}\,db\,da
=8L\int_0^{L^2}e^{-t^2}\,dt
-8\int_0^{L^2}t^{1/2}e^{-t^2}\,dt.
$$
Therefore
$$
K_0=-4\Gamma\left(\frac34\right).
$$

For fixed $x,y$, put $\kappa=\sqrt n\,|xy|$ and scale
$$
u=\kappa^{-1/2}a,
\qquad
v=\kappa^{-1/2}b.
$$
After subtracting the two rank-three models, the local correction is
$$
K_0\,n^{-3/4}|x-y|\,|xy|^{1/2}.
$$
Thus one rank-two intersection contributes
$$
K_0n^{-3/4}
\int_{\mathbb R^2}|x-y|\,|xy|^{1/2}
 e^{-n(x^2+y^2)^5}\,dx\,dy.
$$
Scaling $x=n^{-1/10}X$, $y=n^{-1/10}Y$ shows that this is of order $n^{-23/20}$.

Step 3: Evaluate the tangential rank-two integral

Put
$$
B=\int_{\mathbb R^2}|X-Y|\,|XY|^{1/2}
 e^{-(X^2+Y^2)^5}\,dX\,dY.
$$
In polar coordinates, the radial and angular factors separate:
$$
B=\left(\int_0^\infty r^3e^{-r^{10}}\,dr\right)H,
$$
where
$$
H=\int_0^{2\pi}|\cos\theta-\sin\theta|
|\cos\theta\sin\theta|^{1/2}\,d\theta.
$$
The radial factor is
$$
\int_0^\infty r^3e^{-r^{10}}\,dr
=\frac1{10}\Gamma\left(\frac25\right).
$$
For the angular factor, put $\phi=\theta-\pi/4$. Then
$$
H=4\int_0^1|2u^2-1|^{1/2}\,du.
$$
Splitting at $u=1/\sqrt2$ gives
$$
H=2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2).
$$
Hence
$$
B=\frac1{10}
\left(2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2)\right)
\Gamma\left(\frac25\right).
$$

Step 4: Sum the rank-two strata and exclude smaller terms

There are six pairwise intersections of the four coordinate hyperplanes. Therefore the total rank-two correction is
$$
6K_0B\,n^{-23/20}.
$$
Using Step 2 and Step 3,
$$
6K_0B
=-\frac{12}{5}
\left(2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2)\right)
\Gamma\left(\frac25\right)
\Gamma\left(\frac34\right).
$$

It remains to check that no other contribution occurs at this order. Along a regular rank-three hyperplane the normal scale is $n^{-1/5}$ while the tangential scale is $n^{-1/10}$; odd normal corrections vanish, so the first regular correction is of relative order $n^{-1/5}$, hence $O(n^{-13/10})$. Near a rank-one stratum the natural scaling is one coordinate of size $n^{-1/10}$ and three coordinates of size $n^{-2/15}$, giving total order $n^{-6/5}$. At the rank-zero point the homogeneous determinant scale gives order $n^{-5/4}$. All of these are smaller than $n^{-23/20}$.

Step 5: Recover the requested limit

Combining the preceding steps,
$$
\begin{aligned}
I_n={}&
\frac{3\pi^{3/2}\Gamma(3/5)}{5\sqrt2}\,n^{-11/10}\\
&-\frac{12}{5}
\left(2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2)\right)
\Gamma\left(\frac25\right)
\Gamma\left(\frac34\right)n^{-23/20}
+o(n^{-23/20}).
\end{aligned}
$$
Therefore
$$
\lim_{n\to\infty}n^{23/20}
\left(
I_n-
\frac{3\pi^{3/2}\Gamma(3/5)}{5\sqrt2\,n^{11/10}}
\right)
=-\frac{12}{5}
\left(2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2)\right)
\Gamma\left(\frac25\right)
\Gamma\left(\frac34\right).
$$
Final Answer: $\boxed{-\frac{12}{5}\left(2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2)\right)\Gamma\left(\frac25\right)\Gamma\left(\frac34\right)}$

---

## Answer

$-\frac{12}{5}\left(2+\frac\pi{\sqrt2}-\sqrt2\log(1+\sqrt2)\right)\Gamma(2/5)\Gamma(3/4)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- Vandermonde eigenvalue density
- determinant rank stratification
- nonuniform rank-three asymptotics
- rank-two finite-part matching
- Gamma-function moments
