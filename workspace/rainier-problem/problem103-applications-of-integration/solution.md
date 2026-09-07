## Steps

Step 1: Separate the implicit root

Let
$$
A_n=\int_{[0,1]^4}e^{-nT^2}\,d\mathbf x,
$$
and let $J_n=I_n(0)$. Then
$$
I_n(\lambda)=A_n\sinh\lambda+J_n.
$$
Since $A_n>0$, $I_n$ is strictly increasing and tends to $\pm\infty$ as $\lambda\to\pm\infty$. Hence the root is unique and
$$
\sinh\lambda_n=-\frac{J_n}{A_n}. \tag{1}
$$

Step 2: Reduce the product variable

For every integrable $F$ on $(0,1)$,
$$
\int_{[0,1]^4}F(x_1x_2x_3x_4)\,d\mathbf x
=\frac16\int_0^1(-\log t)^3F(t)\,dt. \tag{2}
$$
Indeed, with $x_i=e^{-u_i}$ and $s=u_1+\cdots+u_4$, the simplex $u_i\ge0$ has three-dimensional volume $s^3/6$, and then $t=e^{-s}$ gives (2).

Thus
$$
A_n=\frac16\int_0^1(-\log t)^3e^{-nt^2}\,dt
\sim\frac{\sqrt\pi}{96}n^{-1/2}(\log n)^3. \tag{3}
$$

Step 3: Collapse the third finite difference

Put
$$
N=n^{1/3},\qquad a=(2n)^{1/3}=2^{1/3}N,
$$
and
$$
\Phi_1(y)=3+(y-1)^2+(y-1)^4,
\qquad
\Phi_2(y)=3+4(y-2)^2+(y-2)^4.
$$
For the term indexed by $j$, apply (2) and substitute $u=2^jt$. The factor $2^j$ cancels the Jacobian, and
$$
-\log t=-\log u+j\log2.
$$
On the common interval $0<u<1$,
$$
\sum_{j=0}^3(-1)^{3-j}\binom3j(-\log u+j\log2)^3=6(\log2)^3. \tag{4}
$$
The pieces with $u\ge1$ are super-exponentially smaller than $e^{-3N}$, because $au\asymp N$ there and each phase contains a positive quartic term. Therefore
$$
J_n=(\log2)^3K_n+o\!\left(N^{-5/2}e^{-3N}\right), \tag{5}
$$
where
$$
K_n=\int_0^\infty\left[e^{-N\Phi_1(au)}-2e^{-N\Phi_2(au)}\right]du. \tag{6}
$$
With $y=au$,
$$
K_n=\frac1{2^{1/3}N}\left(I_1(N)-2I_2(N)\right), \tag{7}
$$
where
$$
I_r(N)=\int_0^\infty e^{-N\Phi_r(y)}\,dy.
$$

Step 4: Compare the two equal-action saddles

The phase $\Phi_1$ has its unique minimum at $y=1$, while $\Phi_2$ has its unique minimum at $y=2$, and both minima equal $3$. Thus both channels have the same exponential action $e^{-3N}$.

For $I_1$, set $y=1+z/\sqrt N$. Since the omitted range $z<-\sqrt N$ has phase at least $5$, it is exponentially negligible. Expanding $e^{-z^4/N}$ gives
$$
I_1(N)=e^{-3N}N^{-1/2}\left[\sqrt\pi-\frac{3\sqrt\pi}{4N}+O(N^{-2})\right]. \tag{8}
$$
For $I_2$, set $y=2+z/\sqrt N$. Similarly,
$$
I_2(N)=e^{-3N}N^{-1/2}\left[\frac{\sqrt\pi}{2}-\frac{3\sqrt\pi}{128N}+O(N^{-2})\right]. \tag{9}
$$
Indeed,
$$
\int_{\mathbb R}z^4e^{-az^2}\,dz=\frac{3\sqrt\pi}{4a^{5/2}}.
$$
The factor $2$ in (7) is tuned so that the two Gaussian leading terms cancel exactly. Hence
$$
I_1(N)-2I_2(N)
\sim-\frac{45\sqrt\pi}{64}N^{-3/2}e^{-3N}. \tag{10}
$$
Combining (7) and (10),
$$
K_n\sim-\frac{45\sqrt\pi}{64\,2^{1/3}}N^{-5/2}e^{-3N}. \tag{11}
$$
Therefore
$$
J_n\sim-\frac{45\sqrt\pi}{64\,2^{1/3}}(\log2)^3
n^{-5/6}e^{-3n^{1/3}}. \tag{12}
$$

Step 5: Recover the root

By (3) and (12), $J_n/A_n\to0$, so (1) and $\operatorname{arsinh}u\sim u$ give
$$
\lambda_n\sim-\frac{J_n}{A_n}
\sim\frac{135(\log2)^3}{2^{4/3}}
\frac{e^{-3n^{1/3}}}{n^{1/3}(\log n)^3}.
$$
Thus the unique constants are
$$
\alpha=\frac13,\qquad \beta=3,\qquad c=3,
\qquad L=\frac{135(\log2)^3}{2^{4/3}}.
$$
Final Answer: $\boxed{\left(\frac13,3,3,\frac{135(\log2)^3}{2^{4/3}}\right)}$

---

## Answer

$\left(\frac13,3,3,\frac{135(\log2)^3}{2^{4/3}}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- product-integral reduction
- third finite-difference cancellation
- competing equal-action saddles
- leading Laplace coefficient cancellation
- implicit root asymptotics
