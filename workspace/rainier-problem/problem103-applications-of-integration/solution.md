## Steps

Step 1: Separate the implicit root and evaluate its denominator

Let
$$
B_n=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf{x},\qquad S_n=I_n(0).
$$
Then
$$
I_n(\lambda)=B_n\sinh\lambda+S_n.
$$
Because $B_n>0$, the function $I_n$ is strictly increasing, so the real root is unique and
$$
\sinh\lambda_n=-\frac{S_n}{B_n}.
$$
Using the product-density identity
$$
\int_{[0,1]^2}F(x_1x_2)\,dx_1dx_2=\int_0^1F(p)(-\log p)\,dp,
$$
we obtain
$$
B_n=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2.
$$
With $y=\sqrt n\,p$,
$$
\int_0^1(-\log p)e^{-np^2}\,dp
=n^{-1/2}\int_0^{\sqrt n}e^{-y^2}\left(\frac{1}{2}\log n-\log y\right)dy
\sim\frac{\sqrt\pi}{4}n^{-1/2}\log n,
$$
so
$$
B_n\sim\frac{\pi}{16}n^{-1}(\log n)^2
=\frac{\pi}{16}\delta^4(\log n)^2.
$$

Step 2: Collapse the dyadic finite difference

Put $h=\log 2$. In the $(j,k,t)$ term use
$$
p=\delta 2^{-j}u,\qquad q=\delta 2^{-k}v.
$$
The factor $2^{j+k}$ cancels the Jacobian factor $2^{-j-k}$, leaving the common factor $\delta^2$. Also
$$
-\log p=-\log\delta+jh-\log u,
\qquad
-\log q=-\log\delta+kh-\log v,
$$
and therefore
$$
\sum_{j,k=0}^1(-1)^{j+k}
(-\log\delta+jh-\log u)(-\log\delta+kh-\log v)=h^2.
$$
The scaled upper limits are at least $\delta^{-1}$. If $u\ge\delta^{-1}$ or $v\ge\delta^{-1}$, then either $s=(u-v)^2$ or $r=uv$ grows as a positive power of $\delta^{-1}$, so $\Psi_t$ exceeds its relevant bounded region by a positive power of $\delta^{-1}$. Hence extending each scaled domain to the positive quadrant changes the integral by an amount smaller than $e^{-5N}$ times every fixed power of $\delta$. Thus
$$
S_n=\delta^2h^2\sum_{t=0}^2(-1)^t\binom{2}{t}J_t+o\left(\delta^6e^{-5N}\right),
$$
where
$$
J_t=\int_{(0,\infty)^2}G_t(u,v)\,du\,dv.
$$

Step 3: Use the hidden total-derivative certificate

Set
$$
r=uv,\qquad y=u-v,\qquad s=y^2.
$$
Since
$$
\left|\frac{\partial(r,y)}{\partial(u,v)}\right|=u+v=\sqrt{y^2+4r},
$$
we have
$$
du\,dv=\frac{dr\,dy}{u+v}.
$$
Moreover
$$
|u^2-v^2|=|y|(u+v).
$$
The integrand is even in $y$, and
$$
\int_{-\infty}^{\infty}|y|F(y^2)\,dy=\int_0^\infty F(s)\,ds.
$$
Therefore
$$
\begin{aligned}
J_t=\int_0^\infty\int_0^\infty C(s)
\left[1-2N(r+1)(r-a_t(s))\right]\\
\times e^{-N\left(4+(s-\delta)^2+(r-a_t(s))^2\right)}\,dr\,ds.
\end{aligned}
$$
For fixed $s$, the bracket is exactly the derivative factor
$$
\frac{\partial}{\partial r}\left[(r+1)e^{-N\left(4+(s-\delta)^2+(r-a_t(s))^2\right)}\right].
$$
The expression in brackets tends to $0$ as $r\to\infty$, while at $r=0$ its prefactor is $1$. Hence the whole bulk saddle cancels exactly and
$$
J_t=-\int_0^\infty C(s)e^{-N\left(4+(s-\delta)^2+a_t(s)^2\right)}\,ds.
$$

Step 4: Evaluate the boundary layer and its centered moment cancellation

Set
$$
s=\delta(1+z),\qquad z\in[-1,\infty).
$$
Then
$$
C(s)=z-\mu,\qquad a_t(s)=1+\delta^3(t+z),
$$
so the preceding exact identity becomes
$$
J_t=-\delta e^{-5N}\int_{-1}^{\infty}(z-\mu)e^{-z^2}
 e^{-2\delta(t+z)-\delta^4(t+z)^2}\,dz.
$$
Define
$$
D_\delta(z)=\sum_{t=0}^2(-1)^t\binom{2}{t}
 e^{-2\delta(t+z)-\delta^4(t+z)^2}.
$$
A Taylor expansion for the three fixed values of $t$ gives
$$
D_\delta(z)=4\delta^2-8\delta^3(z+1)+O\left(\delta^4(1+z^2)\right).
$$
This expansion is uniform on $|z|\le\delta^{-1/4}$, while the complementary Gaussian tail is smaller than every power of $\delta$, so it may be integrated termwise. By the definition of $\mu$,
$$
\int_{-1}^{\infty}(z-\mu)e^{-z^2}\,dz=0.
$$
Also
$$
\mathcal M=\int_{-1}^{\infty}z(z-\mu)e^{-z^2}\,dz
=\int_{-1}^{\infty}(z-\mu)^2e^{-z^2}\,dz>0.
$$
Consequently
$$
\int_{-1}^{\infty}(z-\mu)e^{-z^2}D_\delta(z)\,dz
=-8\mathcal M\delta^3+O(\delta^4),
$$
and therefore
$$
\sum_{t=0}^2(-1)^t\binom{2}{t}J_t
=8\mathcal M\delta^4e^{-5N}\left(1+O(\delta)\right).
$$

Step 5: Recover the asymptotic root

Step 2 and Step 4 give
$$
S_n\sim8\mathcal M(\log 2)^2\delta^6e^{-5N}.
$$
Combining this with the denominator from Step 1 yields
$$
\frac{S_n}{B_n}
\sim\frac{128\mathcal M(\log 2)^2}{\pi}
\frac{\delta^2e^{-5N}}{(\log n)^2}\to0.
$$
Thus $\lambda_n\to0$, so $\sinh\lambda_n\sim\lambda_n$, and
$$
\lambda_n\sim-\frac{128\mathcal M(\log 2)^2}{\pi}
\frac{n^{-1/2}e^{-5\sqrt n}}{(\log n)^2}.
$$
Hence
$$
\alpha=\frac{1}{2},\qquad \beta=2,\qquad c=5,
\qquad L=-\frac{128\mathcal M(\log 2)^2}{\pi}.
$$
Final Answer: $\boxed{\left(\frac{1}{2},2,5,-\frac{128\mathcal M(\log 2)^2}{\pi}\right)}$

---

## Answer

$\left(\frac{1}{2},2,5,-\frac{128\mathcal M(\log 2)^2}{\pi}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- product-density finite difference
- hidden total-derivative certificate
- boundary-layer asymptotics
- second finite difference
- centered truncated-Gaussian moment
