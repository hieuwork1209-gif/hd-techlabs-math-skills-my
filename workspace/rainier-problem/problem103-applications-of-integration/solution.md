## Steps

Step 1: Reduce the invariant matrix integral to eigenvalues

Write
$$
M=\begin{pmatrix}
a&d&e\\
d&b&f\\
e&f&c
\end{pmatrix}.
$$
For a real symmetric matrix, write $M=Q\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)Q^T$. Infinitesimally, if $Q^TdQ=\Omega$ is skew-symmetric, then the off-diagonal part of $Q^TdMQ$ is
$$
(\lambda_j-\lambda_i)\Omega_{ij}.
$$
Hence, after integrating the orthogonal variables, the Euclidean volume element has the form
$$
C\,|\Delta(\lambda)|\,d\lambda_1d\lambda_2d\lambda_3,
\qquad
\Delta(\lambda)=\prod_{i<j}(\lambda_i-\lambda_j),
$$
for a constant $C$.

We determine $C$ from the Gaussian integral. Directly in the six matrix entries,
$$
\int e^{-\operatorname{tr}(M^2)}\,dM
=\pi^{3/2}\left(\frac\pi2\right)^{3/2}
=\frac{\pi^3}{2^{3/2}}.
$$
On the eigenvalue side use the orthonormal coordinates
$$
\lambda_1=\frac m{\sqrt3}+\frac u{\sqrt2}+\frac v{\sqrt6},\quad
\lambda_2=\frac m{\sqrt3}-\frac u{\sqrt2}+\frac v{\sqrt6},\quad
\lambda_3=\frac m{\sqrt3}-\frac{2v}{\sqrt6}.
$$
Then
$$
|\Delta|=\frac{r^3}{\sqrt2}|\cos 3\theta|,
\qquad u=r\cos\theta,\quad v=r\sin\theta.
$$
Therefore
$$
\int_{\mathbb R^3}e^{-\sum\lambda_i^2}|\Delta|\,d\lambda
=\sqrt\pi\,\frac1{\sqrt2}
\left(\int_0^\infty r^4e^{-r^2}\,dr\right)
\left(\int_0^{2\pi}|\cos3\theta|\,d\theta\right)
=\frac{3\pi}{2^{3/2}}.
$$
Thus
$$
C=\frac{\pi^2}{3}.
$$
Consequently
$$
I_n=\frac{\pi^2}{3}\int_{\mathbb R^3}
|\Delta(\lambda)|
 e^{-n\left((\lambda_1\lambda_2\lambda_3)^2+(\lambda_1^2+\lambda_2^2+\lambda_3^2)^4\right)}d\lambda.
$$

Step 2: Compute the leading rank-two contribution

The determinant-zero set is the union of the three coordinate planes $\lambda_i=0$. Away from their intersections, take for example $\lambda_3$ as the normal variable. Then
$$
|\Delta(\lambda)|
=|\lambda_1-\lambda_2|\,|\lambda_1\lambda_2|+o(1)
$$
in the normal scale, while
$$
\int_{-\infty}^{\infty}
 e^{-n(\lambda_1\lambda_2)^2\lambda_3^2}\,d\lambda_3
=\frac{\sqrt\pi}{\sqrt n\,|\lambda_1\lambda_2|}.
$$
Hence one rank-two plane contributes
$$
\frac{\sqrt\pi}{\sqrt n}
\int_{\mathbb R^2}|x-y|e^{-n(x^2+y^2)^4}\,dx\,dy.
$$
With $x=n^{-1/8}X$, $y=n^{-1/8}Y$ this equals
$$
\sqrt\pi\,n^{-7/8}
\int_{\mathbb R^2}|X-Y|e^{-(X^2+Y^2)^4}\,dX\,dY.
$$
Using polar coordinates,
$$
\int_{\mathbb R^2}|X-Y|e^{-(X^2+Y^2)^4}\,dX\,dY
=4\sqrt2\int_0^\infty r^2e^{-r^8}\,dr
=\frac{\sqrt2}{2}\Gamma\left(\frac38\right).
$$
There are three rank-two planes, so after multiplying by $\pi^2/3$,
$$
I_n=\frac{\pi^{5/2}}{\sqrt2}\Gamma\left(\frac38\right)n^{-7/8}
+o(n^{-7/8}).
$$

Step 3: Identify the next stratum

The rank-two approximation is nonuniform where two eigenvalues vanish. Near the $\lambda_1$-axis use the rank-one scaling
$$
\lambda_1=n^{-1/8}X,\qquad
\lambda_2=n^{-3/16}Y,\qquad
\lambda_3=n^{-3/16}Z.
$$
Then
$$
n(\lambda_1\lambda_2\lambda_3)^2\to X^2Y^2Z^2,
\qquad
n(\lambda_1^2+\lambda_2^2+\lambda_3^2)^4\to X^8,
$$
and
$$
|\Delta(\lambda)|\,d\lambda
=n^{-15/16}|X|^2|Y-Z|\,dX\,dY\,dZ+o(n^{-15/16}).
$$
Thus the rank-one intersections occur at order $n^{-15/16}$.

The two rank-two plane models meeting on this axis must be subtracted. For fixed $X$, their combined local contribution is the finite part
$$
K(X)=\lim_{R\to\infty}\left[
\int_{-R}^R\int_{-R}^R
|X|^2|Y-Z|e^{-X^2Y^2Z^2}\,dY\,dZ
-4R\sqrt\pi\,|X|
\right].
$$
With
$$
a=\sqrt{|X|}\,Y,\qquad b=\sqrt{|X|}\,Z,
$$
we get
$$
K(X)=|X|^{1/2}K_0,
$$
where
$$
K_0=\lim_{L\to\infty}\left[
\int_{-L}^L\int_{-L}^L|a-b|e^{-a^2b^2}\,da\,db
-4L\sqrt\pi
\right].
$$

Step 4: Evaluate the universal rank-one finite part

By splitting the square into same-sign and opposite-sign quadrants,
$$
\int_{-L}^L\int_{-L}^L|a-b|e^{-a^2b^2}\,da\,db
=8\int_0^L a\int_0^a e^{-a^2b^2}\,db\,da.
$$
With $t=ab$ and then reversing the order,
$$
\begin{aligned}
8\int_0^L a\int_0^a e^{-a^2b^2}\,db\,da
={}&8L\int_0^{L^2}e^{-t^2}\,dt\\
&-8\int_0^{L^2}t^{1/2}e^{-t^2}\,dt.
\end{aligned}
$$
Therefore
$$
K_0=-8\int_0^\infty t^{1/2}e^{-t^2}\,dt
=-4\Gamma\left(\frac34\right).
$$
Also
$$
\int_{-\infty}^{\infty}|X|^{1/2}e^{-X^8}\,dX
=\frac14\Gamma\left(\frac3{16}\right).
$$
Hence one rank-one axis contributes
$$
-\Gamma\left(\frac3{16}\right)\Gamma\left(\frac34\right)n^{-15/16}.
$$
There are three such axes. Multiplying by the spectral factor $\pi^2/3$ gives
$$
-\pi^2\Gamma\left(\frac3{16}\right)\Gamma\left(\frac34\right)n^{-15/16}.
$$
Regular corrections along the rank-two planes are $O(n^{-9/8})$, while the rank-zero apex is $O(n^{-1})$, so both are smaller than $n^{-15/16}$.

Step 5: Recover the requested limit

Thus
$$
I_n=
\frac{\pi^{5/2}\Gamma(3/8)}{\sqrt2\,n^{7/8}}
-\frac{\pi^2\Gamma(3/16)\Gamma(3/4)}{n^{15/16}}
+o(n^{-15/16}).
$$
Therefore
$$
\lim_{n\to\infty}n^{15/16}
\left(I_n-
\frac{\pi^{5/2}\Gamma(3/8)}{\sqrt2\,n^{7/8}}
\right)
=-\pi^2\Gamma\left(\frac3{16}\right)\Gamma\left(\frac34\right).
$$
Final Answer: $\boxed{-\pi^2\Gamma\left(\frac3{16}\right)\Gamma\left(\frac34\right)}$

---

## Answer

$-\pi^2\Gamma\left(\frac3{16}\right)\Gamma\left(\frac34\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- symmetric-matrix eigenvalue reduction
- determinant rank stratification
- nonuniform rank-two asymptotics
- rank-one finite-part matching
- Gamma-function moments
