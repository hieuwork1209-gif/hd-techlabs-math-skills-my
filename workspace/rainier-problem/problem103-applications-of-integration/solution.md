## Steps

Step 1: Separate the implicit root

Let
$$
A_n=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf x,
$$
and let $J_n=I_n(0)$. Then
$$
I_n(\lambda)=A_n\sinh\lambda+J_n.
$$
Since $A_n>0$, $I_n$ is strictly increasing and tends to $\pm\infty$ as $\lambda\to\pm\infty$. Hence the root is unique and
$$
\sinh\lambda_n=-\frac{J_n}{A_n}. \tag{1}
$$

Step 2: Reduce to two product coordinates

For every integrable $F$ on $(0,1)^2$,
$$
\int_{[0,1]^4}F(P,Q)\,d\mathbf x
=\int_0^1\int_0^1(-\log p)(-\log q)F(p,q)\,dp\,dq. \tag{2}
$$
Indeed, each product of two independent uniform variables has density $-\log p$ on $(0,1)$, and the two pairs are independent.

Therefore
$$
A_n=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2.
$$
With $y=\sqrt n\,p$,
$$
\int_0^1(-\log p)e^{-np^2}\,dp
\sim\frac{\sqrt\pi}{4}n^{-1/2}\log n,
$$
so
$$
A_n\sim\frac\pi{16}n^{-1}(\log n)^2. \tag{3}
$$

Step 3: Collapse the double finite difference

Put
$$
N=\sqrt n,\qquad a=n^{1/4},\qquad h=\log2.
$$
For $u,v\ge0$ define
$$
\begin{aligned}
F_N(u,v)=&\ e^{-N[4+(u^2+v^2-1)^2]}
-\sqrt\pi\,N^{1/2}e^{-N(4+u^2+v^2)}\\
&+\frac\pi8N e^{-N(5+u+v)}.
\end{aligned}
$$
For the term indexed by $(j,k)$, use (2) and set
$$
u=a2^jp,\qquad v=a2^kq.
$$
The factor $2^{j+k}$ cancels the Jacobian apart from $a^{-2}=N^{-1}$, while
$$
-\log p=\log a+jh-\log u,
\qquad
-\log q=\log a+kh-\log v.
$$
Hence
$$
\sum_{j,k=0}^1(-1)^{2-j-k}(X+jh)(Y+kh)=h^2. \tag{4}
$$
The different upper limits may be replaced by infinity with an error super-exponentially smaller than $e^{-5N}$. Thus
$$
J_n=\frac{h^2}{N}H_N+o(N^{-3}e^{-5N}), \tag{5}
$$
where
$$
H_N=\int_0^\infty\int_0^\infty F_N(u,v)\,du\,dv. \tag{6}
$$

Step 4: Cancel the radial saddle, isolated saddle, and leading corner tail

For the first channel, polar coordinates in the first quadrant give
$$
\begin{aligned}
R_N
&=\frac\pi2e^{-4N}\int_0^\infty r e^{-N(r^2-1)^2}\,dr\\
&=\frac\pi4e^{-4N}\int_{-1}^\infty e^{-Nz^2}\,dz. \tag{7}
\end{aligned}
$$
For the second channel,
$$
G_N=\sqrt\pi N^{1/2}e^{-4N}
\left(\int_0^\infty e^{-Nu^2}du\right)^2
=\frac{\pi\sqrt\pi}{4}N^{-1/2}e^{-4N}. \tag{8}
$$
Since
$$
\int_{-\infty}^{\infty}e^{-Nz^2}dz=\sqrt\pi N^{-1/2},
$$
(7)-(8) imply the exact cancellation
$$
R_N-G_N=-\frac\pi4e^{-4N}\int_1^\infty e^{-Nz^2}dz. \tag{9}
$$
The third channel is exact:
$$
C_N=\frac\pi8N e^{-5N}
\left(\int_0^\infty e^{-Nu}du\right)^2
=\frac\pi8N^{-1}e^{-5N}. \tag{10}
$$
Integration by parts at the endpoint gives
$$
\int_1^\infty e^{-Nz^2}dz
=\frac{e^{-N}}{2N}\left(1-\frac1{2N}+O(N^{-2})\right). \tag{11}
$$
Thus the $N^{-1}e^{-5N}$ term in (9) is exactly canceled by (10), and
$$
H_N\sim\frac\pi{16}N^{-2}e^{-5N}. \tag{12}
$$
Therefore
$$
J_n\sim\frac\pi{16}(\log2)^2N^{-3}e^{-5N}
=\frac\pi{16}(\log2)^2n^{-3/2}e^{-5\sqrt n}. \tag{13}
$$

Step 5: Recover the root

By (3) and (13), $J_n/A_n\to0$, so (1) and $\operatorname{arsinh}u\sim u$ give
$$
\lambda_n\sim-\frac{J_n}{A_n}
\sim-(\log2)^2\frac{e^{-5\sqrt n}}{n^{1/2}(\log n)^2}.
$$
Hence
$$
\alpha=\frac12,\qquad \beta=2,\qquad c=5,\qquad L=-(\log2)^2.
$$
Final Answer: $\boxed{\left(\frac12,2,5,-(\log2)^2\right)}$

---

## Answer

$\left(\frac12,2,5,-(\log2)^2\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- double finite-difference cancellation
- Morse-Bott radial saddle
- isolated Gaussian cancellation
- subleading endpoint tail
