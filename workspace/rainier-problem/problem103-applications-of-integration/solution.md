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
A_n=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2
\sim\frac\pi{16}n^{-1}(\log n)^2. \tag{3}
$$

Step 3: Collapse the double finite difference

Put
$$
N=\sqrt n,\qquad a=n^{1/4},\qquad h=\log2.
$$
For $u,v>0$ define
$$
x=uv-1,\qquad y=u-v,
$$
and
$$
A(x,y)=x^2-2y^4+\frac12xy^2.
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
The different upper limits may be replaced by infinity with an error exponentially smaller than the main term. Therefore
$$
J_n=\frac{h^2}{N}H_N+o\!\left(N^{-15/4}e^{-4N}\right), \tag{5}
$$
where
$$
H_N=\int_0^\infty\int_0^\infty
A(uv-1,u-v)e^{-N[4+(uv-1)^2+(u-v)^4]}\,du\,dv. \tag{6}
$$

Step 4: Resolve the mixed-order saddle and two cancellations

The map
$$
(u,v)\mapsto(x,y)=(uv-1,u-v)
$$
is a bijection from the positive quadrant onto $\{x>-1,\ y\in\mathbb R\}$. Since
$$
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|=u+v
=\sqrt{y^2+4(1+x)},
$$
we have
$$
H_N=e^{-4N}\int_{-1}^\infty\int_{\mathbb R}
\frac{A(x,y)e^{-N(x^2+y^4)}}{\sqrt{y^2+4(1+x)}}\,dy\,dx. \tag{7}
$$
The part with $x$ bounded away from $0$ is exponentially smaller, so set
$$
x=N^{-1/2}X,\qquad y=N^{-1/4}Y,
$$
and write
$$
Z=X+\frac{Y^2}{4},
\qquad
A_0=X^2-2Y^4+\frac12XY^2.
$$
Then
$$
\begin{aligned}
H_N
=e^{-4N}N^{-7/4}\frac12
\int_{\mathbb R^2}A_0e^{-X^2-Y^4}
\left[1-\frac{Z}{2N^{1/2}}+\frac{3Z^2}{8N}+O(N^{-3/2}(1+|Z|^3))\right]dX\,dY.
\end{aligned} \tag{8}
$$
The leading coefficient vanishes because
$$
\int_{\mathbb R^2}A_0e^{-X^2-Y^4}\,dX\,dY=0. \tag{9}
$$
The next coefficient also vanishes:
$$
\int_{\mathbb R^2}A_0Ze^{-X^2-Y^4}\,dX\,dY=0. \tag{10}
$$
Indeed, using parity and
$$
\int_{\mathbb R}X^2e^{-X^2}dX=\frac{\sqrt\pi}{2},
\qquad
\frac{\int_{\mathbb R}Y^4e^{-Y^4}dY}{\int_{\mathbb R}e^{-Y^4}dY}=\frac14,
$$
proves (9), while
$$
A_0Z\equiv\frac34X^2Y^2-\frac12Y^6
$$
modulo terms odd in $X$, and
$$
\frac{\int Y^6e^{-Y^4}dY}{\int e^{-Y^4}dY}
=\frac34\frac{\Gamma(3/4)}{\Gamma(1/4)}
$$
proves (10).

For the first surviving term,
$$
A_0Z^2\equiv X^4-\frac{27}{16}X^2Y^4-\frac18Y^8
$$
modulo terms odd in $X$. Hence
$$
\int_{\mathbb R^2}A_0Z^2e^{-X^2-Y^4}\,dX\,dY
=\frac{\sqrt\pi\,\Gamma(1/4)}4. \tag{11}
$$
Substituting (9)-(11) into (8) yields
$$
H_N\sim\frac{3\sqrt\pi\,\Gamma(1/4)}{64}
N^{-11/4}e^{-4N}. \tag{12}
$$
Therefore
$$
J_n\sim\frac{3\sqrt\pi\,\Gamma(1/4)}{64}(\log2)^2
N^{-15/4}e^{-4N}. \tag{13}
$$

Step 5: Recover the root

By (3) and (13), $J_n/A_n\to0$, so from (1),
$$
\lambda_n\sim-\frac{J_n}{A_n}
\sim-\frac{3\Gamma(1/4)(\log2)^2}{4\sqrt\pi}
\frac{e^{-4\sqrt n}}{n^{7/8}(\log n)^2}.
$$
Thus
$$
\alpha=\frac78,\qquad \beta=2,\qquad c=4,
\qquad L=-\frac{3\Gamma(1/4)(\log2)^2}{4\sqrt\pi}.
$$
Final Answer: $\boxed{\left(\frac78,2,4,-\frac{3\Gamma(1/4)(\log2)^2}{4\sqrt\pi}\right)}$

---

## Answer

$\left(\frac78,2,4,-\frac{3\Gamma(1/4)(\log2)^2}{4\sqrt\pi}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- double finite-difference cancellation
- mixed quadratic-quartic saddle
- nonlinear Jacobian expansion
- two consecutive moment cancellations
