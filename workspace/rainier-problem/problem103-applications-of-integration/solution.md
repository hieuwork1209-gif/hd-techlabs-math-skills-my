## Steps

Step 1: Separate the implicit root

Let
$$
B_n=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf{x},
$$
and let $S_n=I_n(0)$. Then
$$
I_n(\lambda)=B_n\sinh\lambda+S_n.
$$
Because $B_n>0$, $I_n$ is strictly increasing in $\lambda$, so the root is unique and satisfies
$$
\sinh\lambda_n=-\frac{S_n}{B_n}.
$$

Step 2: Evaluate the denominator

For every integrable $F$,
$$
\int_{[0,1]^4}F(P,Q)\,d\mathbf{x}
=\int_0^1\int_0^1(-\log p)(-\log q)F(p,q)\,dp\,dq.
$$
Therefore
$$
B_n=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2.
$$
With $y=\sqrt{n}\,p$,
$$
\int_0^1(-\log p)e^{-np^2}\,dp
=n^{-1/2}\int_0^{\sqrt{n}}e^{-y^2}\left(\frac{1}{2}\log n-\log y\right)dy
\sim\frac{\sqrt{\pi}}{4}n^{-1/2}\log n,
$$
so
$$
B_n\sim\frac{\pi}{16}n^{-1}(\log n)^2.
$$

Step 3: Collapse both finite differences

Put
$$
N=\sqrt{n},\qquad h=\log 2,\qquad \delta=N^{-1/2}=n^{-1/4}.
$$
In the $(j,k,t)$ term set
$$
u=n^{1/4}2^jp,\qquad v=n^{1/4}2^kq.
$$
The factor $2^{j+k}$ cancels the corresponding Jacobian factor, leaving the common prefactor $N^{-1}$. Also
$$
-\log p=\frac{1}{4}\log n+jh-\log u,
\qquad
-\log q=\frac{1}{4}\log n+kh-\log v,
$$
and hence
$$
\sum_{j,k=0}^1(-1)^{j+k}
\left(X+jh\right)\left(Y+kh\right)=h^2.
$$
For fixed $t$, define
$$
K_t=\left(1+\frac{s}{\delta}\right)R_t+(s-\delta).
$$
Completing the square in the displayed definition of $\Phi_t^{\pm}$ gives
$$
\Phi_t^{\pm}=4+(K_t\mp\delta)^2+(s-\delta)^2.
$$
Let $H_t$ be the positive-quadrant integral of
$$
A_t(u,v)\left(e^{-N\Phi_t^{+}(u,v)}-e^{-N\Phi_t^{-}(u,v)}\right).
$$
The finite upper limits after scaling are at least $\delta^{-1}$. If, for example, $u\geq\delta^{-1}$, then either $v\leq u/2$, which gives $s=(u-v)^2\geq1/(4\delta^2)$, or $v>u/2$, which gives $r=uv\geq1/(2\delta^2)$. The same dichotomy holds when $v\geq\delta^{-1}$. The square-completed phase therefore exceeds $4$ by a quantity growing as a positive power of $\delta^{-1}$ on every omitted region, so those tails are exponentially smaller than $e^{-4N}$ times any fixed power of $\delta$. Thus
$$
S_n=\frac{h^2}{N}(H_0-2H_1+H_2)+o\left(\delta^{25/2}e^{-4N}\right).
$$

Step 4: Put the three saddle families in one local normal form

Using the square-completed variable $K_t$ from Step 3, the amplitude also satisfies
$$
A_t=K_t^2-\frac{5}{2}\delta^2.
$$
Set
$$
x=uv-1,\qquad y=u-v.
$$
Since
$$
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|
=u+v=\sqrt{y^2+4(1+x)},
$$
scale
$$
x=\delta X,\qquad y=\delta^{1/2}Y,
\qquad T=Y^2-1,
$$
and define
$$
a=1+Y^2,\qquad W=aX+T-ta\delta.
$$
Then
$$
K_t=\delta W,
\qquad
N\left(\Phi_t^{\pm}-4\right)=(W\mp1)^2+T^2,
\qquad
A_t=\delta^2\left(W^2-\frac{5}{2}\right).
$$
Because $X=(W-T)/a+t\delta$, put
$$
Z=\frac{W-T}{a}+\frac{Y^2}{4}.
$$
The exact transformed domain is
$$
D_{t,\delta}=
\left\{(W,Y):\frac{W-T}{a}+t\delta>-\delta^{-1}\right\},
$$
and the Jacobian gives
$$
H_t=\frac{1}{2}e^{-4N}\delta^{7/2}
\int_{D_{t,\delta}}
\frac{Q(W)e^{-T^2}}{a}
\left(1+\delta Z+t\delta^2\right)^{-1/2}
\,dW\,dY,
$$
where
$$
Q(W)=\left(W^2-\frac{5}{2}\right)
\left(e^{-(W-1)^2}-e^{-(W+1)^2}\right).
$$
To justify the expansion, restrict first to
$$
\Omega_{\delta}=\left\{|W|\leq\delta^{-1/8},\ |Y|\leq\delta^{-1/8}\right\}.
$$
For small $\delta$, $\Omega_{\delta}\subset D_{t,\delta}$ for all $t$, and on $\Omega_{\delta}$ one has
$$
|\delta Z|\leq C\delta^{3/4}.
$$
Outside $\Omega_{\delta}$, either the Gaussian factor in $W$ is $O(e^{-c\delta^{-1/4}})$ or $e^{-T^2}=O(e^{-c\delta^{-1/2}})$. The only possible Jacobian singularity is the integrable square-root singularity inherited from $1/\sqrt{y^2+4(1+x)}$, so it cannot offset this Gaussian decay. Hence the complement contributes
$$
o\left(\delta^m e^{-4N}\right)
$$
for every fixed $m$. The binomial expansion may therefore be used uniformly on $\Omega_{\delta}$, and its polynomial remainders are integrable against the Gaussian factors.

Step 5: Evaluate the first surviving moment and recover the root

For
$$
Q(W)=\left(W^2-\frac{5}{2}\right)
\left(e^{-(W-1)^2}-e^{-(W+1)^2}\right),
$$
parity gives
$$
\int_{\mathbb{R}}Q(W)\,dW=0,
\qquad
\int_{\mathbb{R}}W^2Q(W)\,dW=0.
$$
Using
$$
\int_{\mathbb{R}}e^{-z^2}\,dz=\sqrt{\pi},\qquad
\int_{\mathbb{R}}z^2e^{-z^2}\,dz=\frac{\sqrt{\pi}}{2},\qquad
\int_{\mathbb{R}}z^4e^{-z^2}\,dz=\frac{3\sqrt{\pi}}{4},
$$
a shift $W=z+a$ gives
$$
\int_{\mathbb{R}}\left(W^3-\frac{5}{2}W\right)e^{-(W-a)^2}\,dW
=\sqrt{\pi}(a^3-a),
$$
and
$$
\int_{\mathbb{R}}\left(W^5-\frac{5}{2}W^3\right)e^{-(W-a)^2}\,dW
=\sqrt{\pi}\left(a^5+\frac{5}{2}a^3\right).
$$
Evaluating at $a=1$ and $a=-1$ yields
$$
\int_{\mathbb{R}}WQ(W)\,dW=0,
\qquad
\int_{\mathbb{R}}W^3Q(W)\,dW=7\sqrt{\pi}.
$$
For
$$
f_t=\left(1+\delta Z+t\delta^2\right)^{-1/2},
$$
the uniform binomial expansion from Step 4 gives
$$
\begin{aligned}
f_0-2f_1+f_2={}&\frac{3}{4}\delta^4-\frac{15}{8}\delta^5Z
+\delta^6\left(\frac{105}{32}Z^2-\frac{15}{8}\right)\\
&+\delta^7\left(-\frac{315}{64}Z^3+\frac{105}{16}Z\right)
+O\left(\delta^8(1+|Z|^4)\right).
\end{aligned}
$$
Since $Z=W/a+b(Y)$ and $\int_{\mathbb{R}}W^kQ(W)\,dW=0$ for $k=0,1,2$, every term through order $\delta^6$ vanishes after the $W$ integration, and the linear $Z$ term at order $\delta^7$ vanishes as well. In $Z^3$, only $W^3/a^3$ survives the $W$ integration. Therefore
$$
\begin{aligned}
H_0-2H_1+H_2
&\sim\frac{1}{2}e^{-4N}\delta^{7/2}
\left(-\frac{315}{64}\delta^7\right)
(7\sqrt{\pi})
\int_{-\infty}^{\infty}\frac{e^{-(Y^2-1)^2}}{(1+Y^2)^4}\,dY\\
&=-\frac{2205\sqrt{\pi}}{128}\mathcal D\,\delta^{21/2}e^{-4N}.
\end{aligned}
$$
Step 3 then gives
$$
S_n\sim-\frac{2205\sqrt{\pi}}{128}\mathcal D(\log 2)^2
\delta^{25/2}e^{-4N}.
$$
Using $\delta=n^{-1/4}$, $N=\sqrt{n}$, and the denominator from Step 2, the quotient $S_n/B_n$ tends to $0$. Step 1 then gives $\lambda_n\to0$, so $\sinh\lambda_n\sim\lambda_n$ and
$$
\lambda_n\sim
\frac{2205\mathcal D(\log 2)^2}{8\sqrt{\pi}}
\frac{e^{-4\sqrt{n}}}{n^{17/8}(\log n)^2}.
$$
Hence
$$
\alpha=\frac{17}{8},\qquad \beta=2,\qquad c=4,
\qquad L=\frac{2205\mathcal D(\log 2)^2}{8\sqrt{\pi}}.
$$
Final Answer: $\boxed{\left(\frac{17}{8},2,4,\frac{2205\mathcal D(\log 2)^2}{8\sqrt{\pi}}\right)}$

---

## Answer

$\left(\frac{17}{8},2,4,\frac{2205\mathcal D(\log 2)^2}{8\sqrt{\pi}}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- second finite difference of saddle families
- nonlinear saddle normal form
- signed Gaussian moment cancellation
- localized saddle expansion
