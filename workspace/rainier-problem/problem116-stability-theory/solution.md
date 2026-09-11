## Steps

Step 1: Compute the almost-sure exponent
Let
$$
A_1=\begin{pmatrix}-1&3\\0&-1\end{pmatrix},\qquad
A_2=\begin{pmatrix}-1&0\\3&-1\end{pmatrix},
$$
and let the chain jump $1\to2$ at rate $a>0$ and $2\to1$ at rate $b>0$. Put
$$s=a+b,\qquad q=ab.$$
Writing $z(t)=e^{-t}x(t)$ removes the common $-I$. For $r=x_2/x_1>0$, the shear system gives
$$
\dot r=-3r^2\quad(\sigma=1),\qquad \dot r=3\quad(\sigma=2).
$$
If $f_1,f_2$ are stationary projective densities, their forward equations imply zero stationary flux and hence $f_2=r^2f_1$. Thus
$$
f_1=Cr^{-2}e^{-(br+a/r)/3},\qquad f_2=Ce^{-(br+a/r)/3}.
$$
With $\xi=2\sqrt q/3$ and
$$
K_\nu(\xi)=\frac12\int_0^\infty u^{\nu-1}e^{-\frac\xi2(u+u^{-1})}\,du,
$$
normalization gives
$$
C=\frac{\sqrt q}{2sK_1(\xi)}.
$$
Also, in either mode,
$$
\frac d{dt}\log\|x\|_2=3\frac{r}{1+r^2},
$$
so ergodicity yields
$$
\lambda_{\rm sh}
=\frac{3\sqrt q}{s}\frac{K_0(\xi)}{K_1(\xi)}.
$$
Therefore the original system is almost surely exponentially stable exactly when
$$
3\sqrt q\,K_0\left(\frac{2\sqrt q}{3}\right)
<sK_1\left(\frac{2\sqrt q}{3}\right).
$$
The fundamental matrices of the shear system are nonnegative, so the exponent obtained from a positive vector controls the operator norm and hence every deterministic initial state.

Step 2: Compute the mean-square threshold
For the shear system define conditional second moments $u_i,v_i,w_i$ corresponding to $x_1^2,x_1x_2,x_2^2$. They satisfy
$$
\frac d{dt}
\begin{pmatrix}u_1\\v_1\\w_1\\u_2\\v_2\\w_2\end{pmatrix}
=
\begin{pmatrix}
-a&6&0&b&0&0\\
0&-a&3&0&b&0\\
0&0&-a&0&0&b\\
a&0&0&-b&0&0\\
0&a&0&3&-b&0\\
0&0&a&0&6&-b
\end{pmatrix}
\begin{pmatrix}u_1\\v_1\\w_1\\u_2\\v_2\\w_2\end{pmatrix}.
$$
This matrix is irreducible Metzler, so its spectral abscissa is a real Perron eigenvalue $\lambda_*>0$. Set
$$d=\lambda_*(\lambda_*+s).$$
The Perron eigenvalue equations give
$$
du_2=6av_1,\qquad dw_1=6bv_2,
$$
$$
(\lambda_*+a)v_1=b\left(1+\frac{18}{d}\right)v_2,
\qquad
(\lambda_*+b)v_2=a\left(1+\frac{18}{d}\right)v_1.
$$
Multiplying the last two equations and using $(\lambda_*+a)(\lambda_*+b)=d+q$ gives
$$
d^3=36q(d+9).
$$
The left side minus the right side has exactly one positive zero. Since $d=\lambda(\lambda+s)$ increases for $\lambda\ge0$, and $z=e^{-t}x$, mean-square exponential stability is equivalent to $\lambda_*<2$. Substituting $\lambda=2$ gives
$$
\lambda_*<2
\iff 2(s+2)^3>9q(2s+13).
$$
Hence mean-square exponential stability fails exactly when
$$
9q(2s+13)\ge2(s+2)^3.
$$

Step 3: Combine the two criteria
We require almost-sure exponential stability but failure of mean-square exponential stability. Therefore, with $s=a+b$ and $q=ab$, the exact region is
$$
a,b>0,\qquad 9q(2s+13)\ge2(s+2)^3,
$$
$$
3\sqrt qK_0(2\sqrt q/3)<sK_1(2\sqrt q/3).
$$
Final Answer: $\boxed{\{(a,b):a,b>0,9q(2s+13)\ge2(s+2)^3,3\sqrt qK_0(2\sqrt q/3)<sK_1(2\sqrt q/3)\}}$

---

## Answer

$\{(a,b):a,b>0,9q(2s+13)\ge2(s+2)^3,3\sqrt qK_0(2\sqrt q/3)<sK_1(2\sqrt q/3)\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- Markov jump linear systems
- projective piecewise-deterministic processes
- almost-sure Lyapunov exponents
- mean-square stability
- modified Bessel functions

---

## Black-Box Audit — no issues found
