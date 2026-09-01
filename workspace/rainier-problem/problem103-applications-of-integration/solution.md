## Steps

Step 1: Establish the implicit root and its monotonicity

Put
$$
V(x)=x^2(1-x)^2(1+x),
$$
and define
$$
Z_n(\lambda)=\int_0^1 e^{-nV(x)+\lambda x}\,dx,
\qquad
M_n(\lambda)=\frac{\int_0^1 x e^{-nV(x)+\lambda x}\,dx}{Z_n(\lambda)}.
$$
Then
$$
I_n(\lambda)=Z_n(\lambda)\bigl(2M_n(\lambda)-1\bigr).
$$
Differentiating the normalized mean gives
$$
M_n'(\lambda)
=\frac{\int_0^1 x^2e^{-nV+\lambda x}\,dx}{Z_n(\lambda)}-M_n(\lambda)^2,
$$
which is the variance of $x$ under a positive density on $(0,1)$. Hence $M_n'(\lambda)>0$. Also
$$
M_n(\lambda)\to0\quad(\lambda\to-\infty),
\qquad
M_n(\lambda)\to1\quad(\lambda\to+\infty).
$$
Therefore there is exactly one $\lambda_n$ for which $M_n(\lambda_n)=1/2$, equivalently $I_n(\lambda_n)=0$.

Step 2: Compute the two endpoint contributions through the first correction

The only zeros of $V$ on $[0,1]$ are the endpoints. On every fixed interval $[\varepsilon,1-\varepsilon]$, $V$ is bounded below by a positive constant, so that part of $I_n(\lambda)$ is exponentially small, uniformly for $\lambda$ in a fixed compact set.

Near $x=0$,
$$
V(x)=x^2-x^3-x^4+O(x^5),
$$
and
$$
(2x-1)e^{\lambda x}=-1+(2-\lambda)x+O(x^2).
$$
Set $x=t/\sqrt n$. Expanding the exponential to relative order $n^{-1/2}$ gives
$$
e^{-nV(t/\sqrt n)}
=e^{-t^2}\left(1+\frac{t^3}{\sqrt n}+O\left(\frac{t^4+t^6}{n}\right)\right).
$$
Hence the contribution from $x=0$ is
$$
-\frac{1}{\sqrt n}\int_0^\infty e^{-t^2}\,dt
+\frac1n\int_0^\infty\bigl((2-\lambda)t-t^3\bigr)e^{-t^2}\,dt
+O(n^{-3/2}).
$$
Using
$$
\int_0^\infty e^{-t^2}\,dt=\frac{\sqrt\pi}{2},
\qquad
\int_0^\infty te^{-t^2}\,dt
=\int_0^\infty t^3e^{-t^2}\,dt=\frac12,
$$
this becomes
$$
-\frac{\sqrt\pi}{2\sqrt n}+\frac{1-\lambda}{2n}+O(n^{-3/2}). \tag{1}
$$

For the endpoint $x=1$, write $y=1-x$. Then
$$
V(1-y)=2y^2-5y^3+4y^4+O(y^5),
$$
and
$$
(2x-1)e^{\lambda x}=e^\lambda\bigl(1-(\lambda+2)y+O(y^2)\bigr).
$$
With $y=t/\sqrt n$,
$$
e^{-nV(1-t/\sqrt n)}
=e^{-2t^2}\left(1+\frac{5t^3}{\sqrt n}+O\left(\frac{t^4+t^6}{n}\right)\right).
$$
Therefore the contribution from $x=1$ is
$$
\frac{e^\lambda}{\sqrt n}\int_0^\infty e^{-2t^2}\,dt
+\frac{e^\lambda}{n}\int_0^\infty\bigl(- (\lambda+2)t+5t^3\bigr)e^{-2t^2}\,dt
+O(n^{-3/2}).
$$
Since
$$
\int_0^\infty e^{-2t^2}\,dt=\frac{\sqrt\pi}{2\sqrt2},
\qquad
\int_0^\infty te^{-2t^2}\,dt=\frac14,
\qquad
\int_0^\infty t^3e^{-2t^2}\,dt=\frac18,
$$
this equals
$$
\frac{e^\lambda\sqrt\pi}{2\sqrt{2n}}
+\frac{e^\lambda(1-2\lambda)}{8n}
+O(n^{-3/2}). \tag{2}
$$
Combining (1) and (2), uniformly for $\lambda$ in compact sets,
$$
I_n(\lambda)
=\frac{\sqrt\pi}{2\sqrt n}\left(-1+\frac{e^\lambda}{\sqrt2}\right)
+\frac1n\left(\frac{1-\lambda}{2}+\frac{e^\lambda(1-2\lambda)}8\right)
+O(n^{-3/2}). \tag{3}
$$

Step 3: Locate $\lambda_n$ at the correct scale

Let
$$
L=\frac12\log2.
$$
For any fixed $\eta>0$, the leading term in (3) is negative at $L-\eta$ and positive at $L+\eta$ for all sufficiently large $n$. Since $I_n$ has a unique zero,
$$
\lambda_n\to L.
$$
Using (3) at $\lambda=\lambda_n$ now gives
$$
0=\frac{\sqrt\pi}{2\sqrt n}\left(-1+\frac{e^{\lambda_n}}{\sqrt2}\right)+O(n^{-1}),
$$
so
$$
\frac{e^{\lambda_n}}{\sqrt2}=1+O(n^{-1/2}).
$$
Thus
$$
\lambda_n-L=O(n^{-1/2}).
$$
Write
$$
\delta_n=\sqrt n\,(\lambda_n-L).
$$
Then $(\delta_n)$ is bounded.

Step 4: Extract the first nonzero balance

Since $e^L=\sqrt2$,
$$
\frac{e^{\lambda_n}}{\sqrt2}
=e^{\delta_n/\sqrt n}
=1+\frac{\delta_n}{\sqrt n}+O(n^{-1}).
$$
Substitute this and $\lambda_n=L+o(1)$ into (3). Multiplying by $n$ gives
$$
0=\frac{\sqrt\pi}{2}\delta_n
+\frac{1-L}{2}
+\frac{\sqrt2(1-2L)}8
+o(1).
$$
Hence
$$
\delta_n\to
-\frac{2}{\sqrt\pi}\left(\frac{1-L}{2}+\frac{\sqrt2(1-2L)}8\right).
$$
With $L=\frac12\log2$, this simplifies to
$$
\frac{\log4-4+\sqrt2(\log2-1)}{4\sqrt\pi}.
$$
Final Answer: $\boxed{\frac{\log4-4+\sqrt2(\log2-1)}{4\sqrt\pi}}$

---

## Answer

$\frac{\log4-4+\sqrt2(\log2-1)}{4\sqrt\pi}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- implicit integral roots
- competing endpoint asymptotics
- Laplace scaling
- first-order balance
