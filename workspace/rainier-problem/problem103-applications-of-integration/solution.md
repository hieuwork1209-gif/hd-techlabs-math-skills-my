## Steps

Step 1: Separate the implicit root

Let
$$
B_n=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf x,
$$
and let $S_n=I_n(0)$. Then
$$
I_n(\lambda)=B_n\sinh\lambda+S_n,
$$
so the unique root satisfies
$$
\sinh\lambda_n=-\frac{S_n}{B_n}. \tag{1}
$$

Step 2: Evaluate the denominator

For every integrable $F$,
$$
\int_{[0,1]^4}F(P,Q)\,d\mathbf x
=\int_0^1\int_0^1(-\log p)(-\log q)F(p,q)\,dp\,dq. \tag{2}
$$
Hence
$$
B_n=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2
\sim\frac\pi{16}n^{-1}(\log n)^2. \tag{3}
$$

Step 3: Collapse the double finite difference

Put
$$
N=\sqrt n,\qquad h=\log2,\qquad \delta=N^{-1/2}=n^{-1/4}.
$$
In the $(j,k)$ term set $u=n^{1/4}2^jp$, $v=n^{1/4}2^kq$. The factor $2^{j+k}$ cancels the Jacobian apart from $N^{-1}$, while
$$
\sum_{j,k=0}^1(-1)^{2-j-k}(X+jh)(Y+kh)=h^2. \tag{4}
$$
Extending the unequal upper limits to infinity changes only exponentially smaller terms. Therefore
$$
S_n=\frac{h^2}{N}H_N+o\!\left(\delta^{17/2}e^{-4N}\right), \tag{5}
$$
where
$$
H_N=\int_0^\infty\int_0^\infty A_n(u,v)
\left(e^{-N\Phi_n^+(u,v)}-e^{-N\Phi_n^-(u,v)}\right)du\,dv. \tag{6}
$$

Step 4: Recover the two equal-action saddle channels

Write
$$
r=uv,\qquad s=(u-v)^2,
$$
and define
$$
K=\left(1+\frac{s}{\delta}\right)(r-1)+(s-\delta). \tag{7}
$$
Direct expansion of the displayed expressions in the problem gives
$$
\Phi_n^\pm=4+(K\mp\delta)^2+(s-\delta)^2, \tag{8}
$$
and
$$
A_n=K^2-\frac52\delta^2. \tag{9}
$$
Thus the two channels have the same minimum action $4$.

Set
$$
x=uv-1,\qquad y=u-v.
$$
Then
$$
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|
=\sqrt{y^2+4(1+x)}. \tag{10}
$$
Scale
$$
x=\delta X,\qquad y=\delta^{1/2}Y,\qquad T=Y^2-1,
$$
and put
$$
W=(1+Y^2)X+T. \tag{11}
$$
Then $K=\delta W$, $N\delta^2=1$, and
$$
N(\Phi_n^\pm-4)=(W\mp1)^2+T^2,
\qquad
A_n=\delta^2\left(W^2-\frac52\right). \tag{12}
$$
Also $dX=dW/(1+Y^2)$ and
$$
\frac1{\sqrt{y^2+4(1+x)}}
=\frac12(1+\delta Z)^{-1/2},
$$
where
$$
Z=\frac{W-T}{1+Y^2}+\frac{Y^2}{4}. \tag{13}
$$
Hence, with
$$
F(W)=e^{-(W-1)^2}-e^{-(W+1)^2},
$$
we obtain
$$
H_N=\frac12e^{-4N}\delta^{7/2}
\int_{\mathbb R^2}\frac{\left(W^2-\frac52\right)F(W)e^{-T^2}}{1+Y^2}
(1+\delta Z)^{-1/2}\,dW\,dY. \tag{14}
$$

Step 5: Use the inter-channel moment cancellations

The function $F$ is odd. Its odd moments are
$$
\int WF(W)\,dW=2\sqrt\pi,\qquad
\int W^3F(W)\,dW=5\sqrt\pi,
$$
$$
\int W^5F(W)\,dW=\frac{39}{2}\sqrt\pi. \tag{15}
$$
Therefore, for $P(W)=W^2-\frac52$,
$$
\int WP(W)F(W)\,dW=0,\qquad
\int W^3P(W)F(W)\,dW=7\sqrt\pi. \tag{16}
$$
Expand
$$
(1+\delta Z)^{-1/2}
=1-\frac12\delta Z+\frac38\delta^2Z^2-\frac5{16}\delta^3Z^3+O(\delta^4). \tag{17}
$$
Since $P$ is even, the order $\delta^0$ vanishes by parity. Writing
$$
Z=\frac{W}{1+Y^2}+b(Y),
$$
the orders $\delta^1$ and $\delta^2$ vanish by (16) and parity. At order $\delta^3$, only the $W^3$ term survives. Thus, by the definition of $\mathcal D$,
$$
H_N\sim-\frac{35\sqrt\pi}{32}\mathcal D\,\delta^{13/2}e^{-4N}. \tag{18}
$$
Consequently
$$
S_n\sim-\frac{35\sqrt\pi}{32}\mathcal D(\log2)^2
\delta^{17/2}e^{-4N}. \tag{19}
$$
Combining (1), (3), and (19), and using $\delta=n^{-1/4}$,
$$
\lambda_n\sim\frac{35\mathcal D(\log2)^2}{2\sqrt\pi}
\frac{e^{-4\sqrt n}}{n^{9/8}(\log n)^2}.
$$
Therefore
$$
\alpha=\frac98,\qquad \beta=2,\qquad c=4,
\qquad L=\frac{35\mathcal D(\log2)^2}{2\sqrt\pi}.
$$
Final Answer: $\boxed{\left(\frac98,2,4,\frac{35\mathcal D(\log2)^2}{2\sqrt\pi}\right)}$

---

## Answer

$\left(\frac98,2,4,\frac{35\mathcal D(\log2)^2}{2\sqrt\pi}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- equal-action saddle-channel cancellation
- nonlinear saddle coordinate recovery
- signed Gaussian moment matching
- Jacobian-order cancellation
