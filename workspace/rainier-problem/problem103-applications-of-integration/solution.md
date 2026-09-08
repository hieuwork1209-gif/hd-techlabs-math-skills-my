## Steps

Step 1: Rescale the half-mass condition

For each $n$, the Gaussian mass of the disk centered at $(1,0)$ with radius $1+\lambda$ is continuous and strictly increasing for $\lambda>-1$, from $0$ to $\pi/n$. Hence there is a unique $\lambda_n>-1$ with mass $\pi/(2n)$.

Put
$$
\varepsilon=n^{-1/2},\qquad X=\sqrt n\,x,\qquad Y=\sqrt n\,y.
$$
After multiplying the defining equation by $n$, the disk condition becomes
$$
(\varepsilon X-1)^2+\varepsilon^2Y^2\le (1+\lambda_n)^2.
$$
For fixed $Y$ in the Gaussian main range, the relevant left boundary is
$$
T_n(Y)=\frac{1-\sqrt{(1+\lambda_n)^2-\varepsilon^2Y^2}}{\varepsilon}.
$$
The right boundary is $2\varepsilon^{-1}+O(1)$, and the omitted region $|Y|>(1+\lambda_n)/\varepsilon$ is also exponentially far out. Thus both give an error smaller than every fixed power of $\varepsilon$.

Writing
$$
\Phi(z)=\int_0^z e^{-x^2}\,dx,
$$
and subtracting the Gaussian mass of the half-plane $X\ge0$, the half-mass condition is
$$
\int_{-\infty}^{\infty}e^{-Y^2}\Phi(T_n(Y))\,dY=o(\varepsilon^m)
$$
for every fixed $m$.

Step 2: Determine the scale of the radius correction

The previous equation is strictly decreasing in $\lambda_n$. If $\lambda=c\varepsilon^2$ with $c$ bounded, then uniformly on every Gaussian main range,
$$
T(Y)=\varepsilon\left(\frac{Y^2}{2}-c\right)+O\left(\varepsilon^3(1+Y^4)\right).
$$
Since $\Phi(z)=z+O(z^3)$ near $0$, the defining equation gives at first order
$$
0=\varepsilon\sqrt\pi\left(\frac14-c\right)+O(\varepsilon^3).
$$
Therefore
$$
\lambda_n=\frac14\varepsilon^2+O(\varepsilon^4).
$$
Write more precisely
$$
\lambda_n=c\varepsilon^2+d\varepsilon^4+o(\varepsilon^4).
$$
The first-order calculation already gives $c=1/4$.

Step 3: Expand the curved boundary to the first nonlinear order

For bounded $c,d$,
$$
(1+\lambda_n)^2-\varepsilon^2Y^2
=1+\varepsilon^2(2c-Y^2)+\varepsilon^4(c^2+2d)+o(\varepsilon^4).
$$
Using the square-root expansion,
$$
T_n(Y)=\varepsilon A(Y)+\varepsilon^3B(Y)+o(\varepsilon^3),
$$
where
$$
A(Y)=\frac{Y^2}{2}-c,
\qquad
B(Y)=-d-\frac{cY^2}{2}+\frac{Y^4}{8}.
$$
Also
$$
\Phi(z)=z-\frac{z^3}{3}+O(z^5).
$$
Hence, after dividing the half-mass equation by $\sqrt\pi$ and using the probability density $\pi^{-1/2}e^{-Y^2}$,
$$
0=\varepsilon\mathbb E[A]
+\varepsilon^3\left(\mathbb E[B]-\frac13\mathbb E[A^3]\right)
+o(\varepsilon^3).
$$

Step 4: Evaluate the Gaussian moments

For the density $\pi^{-1/2}e^{-Y^2}$,
$$
\mathbb E[Y^2]=\frac12,
\qquad
\mathbb E[Y^4]=\frac34,
\qquad
\mathbb E[Y^6]=\frac{15}{8}.
$$
The coefficient of $\varepsilon$ gives
$$
0=\mathbb E[A]=\frac14-c,
$$
so $c=1/4$. With this value,
$$
\mathbb E[B]
=-d-\frac18\mathbb E[Y^2]+\frac18\mathbb E[Y^4]
=-d+\frac1{32}.
$$
Moreover
$$
A=\frac{Y^2}{2}-\frac14,
$$
so
$$
\mathbb E[A^3]
=\frac18\mathbb E[Y^6]-\frac{3}{16}\mathbb E[Y^4]
+\frac{3}{32}\mathbb E[Y^2]-\frac1{64}
=\frac18.
$$
Therefore the coefficient of $\varepsilon^3$ gives
$$
-d+\frac1{32}-\frac1{24}=0,
$$
so
$$
d=-\frac1{96}.
$$

Step 5: Recover the requested limit

Since $\varepsilon^2=n^{-1}$,
$$
\lambda_n=rac{1}{4n}-\frac{1}{96n^2}+o(n^{-2}).
$$
Hence
$$
\lim_{n\to\infty}n^2\left(\lambda_n-\frac{1}{4n}\right)
=-\frac1{96}.
$$
Final Answer: $\boxed{-\frac{1}{96}}$

---

## Answer

$-\frac{1}{96}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- Gaussian rescaling
- tangent-disk geometry
- curved-boundary expansion
- Gaussian tail nonlinearity
- implicit asymptotic correction
