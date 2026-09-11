## Steps

Step 1: Set up the variational eigenvalue and prove attainment

Let
$$
\mathcal V=\left\{f\in H^2(-1,1):
 f(-x)=f(x),\ f(\pm1)=f'(\pm1)=0,\ \int_{-1}^1 f(x)\,dx=0\right\}.
$$
For nonzero $f\in\mathcal V$ write
$$
R[f]=\frac{\int_{-1}^1 (f''(x))^2\,dx}
{\int_{-1}^1 f(x)^2\,dx},
\qquad
\Lambda=\inf_{0\ne f\in\mathcal V}R[f].
\tag{1}
$$
The boundary conditions imply, for $-1\le x\le1$,
$$
f'(x)=\int_{-1}^x f''(s)\,ds,
$$
so by Cauchy-Schwarz
$$
|f'(x)|\le \sqrt2\,\|f''\|_2.
$$
Integrating once more from $-1$ gives a bound for $\|f\|_\infty$ in terms of $\|f''\|_2$. Hence a minimizing sequence normalized by $\|f\|_2=1$ is bounded in $H^2$. The same integral formulas give uniform boundedness and equicontinuity of both $f$ and $f'$, while $f''$ is weakly bounded in $L^2$. Passing to a subsequence gives uniform convergence of $f,f'$ and weak $L^2$ convergence of $f''$. Thus evenness, the clamped boundary conditions, the zero-mean condition, and $\|f\|_2=1$ pass to the limit, while
$$
\|f''\|_2^2\le \liminf \|f_j''\|_2^2.
$$
Therefore the infimum is attained by some nonzero $f\in\mathcal V$.

Step 2: Derive the forced Euler-Lagrange equation

Let $f$ be a minimizer with $\|f\|_2=1$, and put $\lambda=R[f]=\Lambda$. For every even $g\in H^2(-1,1)$ satisfying the clamped boundary conditions and $\int_{-1}^1g=0$, differentiating the Rayleigh quotient at $f$ gives
$$
\int_{-1}^1 f''g''\,dx
=\lambda\int_{-1}^1 fg\,dx.
\tag{2}
$$
On the full even clamped test space, the linear functional
$$
g\longmapsto
\int f''g''-\lambda\int fg
$$
vanishes on the kernel of $g\mapsto\int g$. Hence it is a scalar multiple of that one remaining linear functional: there is a constant $\mu$ such that
$$
\int_{-1}^1 f''g''\,dx
=\lambda\int_{-1}^1 fg\,dx+\mu\int_{-1}^1g\,dx
\tag{3}
$$
for every even clamped $g$. Thus, in the weak sense and hence classically after solving the constant-coefficient equation,
$$
f^{(4)}=\lambda f+\mu.
\tag{4}
$$
Because a nonzero clamped function cannot have $f''\equiv0$, one has $\lambda>0$. Write
$$
\lambda=k^4,
\qquad k>0.
$$
Every even solution of (4) has the form
$$
f(x)=A\cosh(kx)+B\cos(kx)+C,
\tag{5}
$$
where $C=-\mu/k^4$.

Step 3: Obtain the exact secular equation

The conditions $f(1)=0$, $f'(1)=0$, and $\int_0^1 f=0$ give
$$
\begin{pmatrix}
\cosh k&\cos k&1\\
\sinh k&-\sin k&0\\
\dfrac{\sinh k}{k}&\dfrac{\sin k}{k}&1
\end{pmatrix}
\begin{pmatrix}A\\B\\C\end{pmatrix}
=0.
\tag{6}
$$
A nonzero solution exists exactly when the determinant vanishes. Expanding (6) gives
$$
k\sin k\cosh k+k\cos k\sinh k-2\sin k\sinh k=0.
\tag{7}
$$
For $k>0$ with $\sin k\ne0$, this is equivalent to
$$
F(k):=k(\cot k+\coth k)-2=0.
\tag{8}
$$
If $k=j\pi$ with $j\ge1$, the left side of (7) equals $k\cos k\sinh k\ne0$, so no roots were lost by using (8).

Step 4: Prove which root is the first one

We first exclude $0<k<\pi$. The Euler products
$$
\frac{\sin k}{k}=\prod_{j=1}^{\infty}\left(1-\frac{k^2}{j^2\pi^2}\right),
\qquad
\frac{\sinh k}{k}=\prod_{j=1}^{\infty}\left(1+\frac{k^2}{j^2\pi^2}\right)
$$
give, after multiplication and logarithmic differentiation on compact subintervals of $(0,\pi)$,
$$
F(k)
=k\frac{d}{dk}\log\!\left(\frac{\sin k\,\sinh k}{k^2}\right)
=-4k^4\sum_{j=1}^{\infty}
\frac1{j^4\pi^4-k^4}<0.
\tag{9}
$$
Hence there is no root in $(0,\pi)$.

For $\pi<k<3\pi/2$, both $\cot k$ and $\coth k$ are positive, and $\coth k>1$, so
$$
F(k)>k-2>0.
$$
At $k=3\pi/2$, one still has
$$
F(3\pi/2)=\frac{3\pi}{2}\coth(3\pi/2)-2>0.
$$
On $(3\pi/2,2\pi)$, $F(k)\to-\infty$ as $k\to2\pi^-$. Moreover
$$
\frac d{dk}(k\cot k)=\cot k-k\csc^2k<-k
\tag{10}
$$
because $\cot k<0$ there. Also, for every $k>0$,
$$
\frac d{dk}(k\coth k)=\coth k-k\operatorname{csch}^2k<1,
\tag{11}
$$
because (11) is equivalent to
$$
\frac{1-e^{-2k}}2<k.
$$
Therefore on $(3\pi/2,2\pi)$,
$$
F'(k)<1-k<0.
$$
So there is a unique root
$$
\kappa\in\left(\frac{3\pi}{2},2\pi\right),
\qquad
\kappa(\cot\kappa+\coth\kappa)=2,
\tag{12}
$$
and (9)-(12) show that $\kappa$ is the smallest positive root of the secular equation.

Step 5: Construct the extremizer and close the sharp value

Define
$$
\begin{aligned}
f_\kappa(x)
={}&\sin\kappa\,\cosh(\kappa x)
+\sinh\kappa\,\cos(\kappa x)\\
&-\sin\kappa\cosh\kappa
-\sinh\kappa\cos\kappa.
\end{aligned}
\tag{13}
$$
This function is even. Directly from (13),
$$
f_\kappa(1)=f_\kappa'(1)=0,
$$
and the same holds at $-1$. Also
$$
\int_0^1 f_\kappa(x)\,dx
=\frac{2\sin\kappa\sinh\kappa}{\kappa}
-\sin\kappa\cosh\kappa
-\sinh\kappa\cos\kappa=0
$$
by (12). Thus $f_\kappa\in\mathcal V$ and is nonzero.

Its fourth derivative satisfies
$$
f_\kappa^{(4)}=\kappa^4(f_\kappa-C),
$$
where $C$ is the constant term in (13). Integrating twice by parts, the clamped conditions give
$$
\int_{-1}^1(f_\kappa'')^2
=\int_{-1}^1 f_\kappa f_\kappa^{(4)}
=\kappa^4\int_{-1}^1 f_\kappa^2,
$$
because $\int f_\kappa=0$. Hence
$$
R[f_\kappa]=\kappa^4.
$$
Every minimizer must yield a positive root of the secular equation by Steps 2-3, and no such root lies below $\kappa$ by Step 4. Therefore
$$
\Lambda=\kappa^4.
$$

## Solution Concepts

- Constrained Rayleigh-quotient minimization for a clamped beam energy.
- Euler-Lagrange equation with a Lagrange multiplier forced by the zero-mean constraint.
- Secular determinant and exact localization of its first positive root.

Final Answer: $\displaystyle \kappa^4,\quad \frac{3\pi}{2}<\kappa<2\pi,\quad \kappa(\cot\kappa+\coth\kappa)=2$.
