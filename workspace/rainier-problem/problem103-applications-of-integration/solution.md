## Steps

Step 1: Reduce the degenerate Gaussian integral to product-ratio coordinates

Set
$$
u=x^2,\qquad v=y^2.
$$
Using both signs of $x$ and $y$,
$$
I_n=\int_0^\infty\int_0^\infty
u^{-1/2}v^{-1/2}e^{-n(u^2+uv+v^3)}\,du\,dv.
$$
Now write
$$
u=\sqrt t\,e^s,\qquad v=\sqrt t\,e^{-s}.
$$
Then $uv=t$, the Jacobian has absolute value $1$, and
$$
u^2=t e^{2s},\qquad v^3=t^{3/2}e^{-3s}.
$$
Therefore
$$
I_n=\int_0^\infty\int_{-\infty}^{\infty}
t^{-1/2}e^{-n(t+t e^{2s}+t^{3/2}e^{-3s})}\,ds\,dt.
$$
The logarithm in the final asymptotic comes from the fact that no single scaling of $s$ makes both $e^{2s}$ and $t^{1/2}e^{-3s}$ simultaneously order one.

Step 2: Isolate the scale-free transition integral

Put $t=z/n$ and then shift
$$
r=s+\frac12\log z.
$$
With $\varepsilon=n^{-1/2}$ this gives
$$
I_n=n^{-1/2}\int_0^\infty z^{-1/2}e^{-z}
K(\varepsilon z^3)\,dz,
$$
where
$$
K(\rho)=\int_{-\infty}^{\infty}
 e^{-e^{2r}-\rho e^{-3r}}\,dr.
$$
Thus the problem reduces to the small-$\rho$ finite part of $K(\rho)$.

Step 3: Compute the logarithmic divergence and its finite part

Set $q=e^{2r}$. Then
$$
K(\rho)=\frac12\int_0^\infty
\frac{e^{-q-\rho q^{-3/2}}}{q}\,dq.
$$
Split at $q=1$:
$$
\begin{aligned}
K(\rho)={}&\frac12\int_0^1\frac{e^{-\rho q^{-3/2}}}{q}\,dq\\
&+\frac12\int_0^1\frac{(e^{-q}-1)e^{-\rho q^{-3/2}}}{q}\,dq
+\frac12\int_1^\infty\frac{e^{-q}e^{-\rho q^{-3/2}}}{q}\,dq.
\end{aligned}
$$
In the first integral use $w=\rho q^{-3/2}$. This gives
$$
\frac12\int_0^1\frac{e^{-\rho q^{-3/2}}}{q}\,dq
=\frac13\int_\rho^\infty\frac{e^{-w}}{w}\,dw
=-\frac13\log\rho-\frac\gamma3+o(1).
$$
For the other two terms, dominated convergence gives
$$
\frac12\left[
\int_0^1\frac{e^{-q}-1}{q}\,dq
+\int_1^\infty\frac{e^{-q}}{q}\,dq
\right]
=-\frac\gamma2.
$$
The bracketed identity is the standard integral representation of the Euler-Mascheroni constant and follows directly from
$$
\gamma=\lim_{m\to\infty}\left(\sum_{k=1}^m\frac1k-\log m\right)
$$
by writing $1/k=\int_0^\infty e^{-kt}\,dt$ and passing to the limit. Hence
$$
K(\rho)=-\frac13\log\rho-\frac{5\gamma}{6}+o(1).
$$

Step 4: Integrate the finite part against the remaining Gaussian weight

From Step 2,
$$
\sqrt n\,I_n=\int_0^\infty z^{-1/2}e^{-z}K(\varepsilon z^3)\,dz.
$$
Split the $z$-integral at $z=\varepsilon^{-1/12}$. On the first part, $0<\varepsilon z^3\le\varepsilon^{3/4}$, so the remainder in Step 3 is uniform there by the definition of the limit as $\rho\to0$. The complementary $e^{-z}$ tail is smaller than every power of $\varepsilon$. Therefore termwise integration gives
$$
\begin{aligned}
\sqrt n\,I_n
={}&\frac{\sqrt\pi}{6}\log n
-\int_0^\infty z^{-1/2}e^{-z}\log z\,dz\\
&-\frac{5\gamma}{6}\sqrt\pi+o(1).
\end{aligned}
$$
Now
$$
\int_0^\infty z^{-1/2}e^{-z}\log z\,dz
=\Gamma'(1/2).
$$
Differentiating the duplication formula
$$
\Gamma(w)\Gamma\left(w+\frac12\right)
=2^{1-2w}\sqrt\pi\,\Gamma(2w)
$$
at $w=1/2$, and using $\Gamma'(1)=-\gamma$, gives
$$
\Gamma'(1/2)=\sqrt\pi\,(-\gamma-2\log2).
$$
Hence
$$
\sqrt n\,I_n
=\frac{\sqrt\pi}{6}\log n
+\sqrt\pi\left(2\log2+\frac\gamma6\right)+o(1).
$$

Step 5: Recover the requested limit

Subtracting the logarithmic term from Step 4 yields
$$
\lim_{n\to\infty}
\left(\sqrt n\,I_n-\frac{\sqrt\pi}{6}\log n\right)
=\sqrt\pi\left(2\log2+\frac\gamma6\right).
$$
Final Answer: $\boxed{\sqrt\pi\left(2\log2+\frac\gamma6\right)}$

---

## Answer

$\sqrt\pi\left(2\log2+\frac\gamma6\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- degenerate Laplace integral
- product-ratio coordinates
- competing asymptotic scales
- logarithmic finite part
- Gamma-function differentiation
