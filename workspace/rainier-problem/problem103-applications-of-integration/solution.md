## Steps

Step 1: Separate the implicit root

Let
$$
A_n^{(0)}=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf x,
$$
and let $J_n=I_n(0)$. Then
$$
I_n(\lambda)=A_n^{(0)}\sinh\lambda+J_n.
$$
Since $A_n^{(0)}>0$, the root is unique and
$$
\sinh\lambda_n=-\frac{J_n}{A_n^{(0)}}. \tag{1}
$$

Step 2: Reduce to two product coordinates

For every integrable $F$ on $(0,1)^2$,
$$
\int_{[0,1]^4}F(P,Q)\,d\mathbf x
=\int_0^1\int_0^1(-\log p)(-\log q)F(p,q)\,dp\,dq. \tag{2}
$$
Hence
$$
A_n^{(0)}=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2
\sim\frac\pi{16}n^{-1}(\log n)^2. \tag{3}
$$

Step 3: Collapse the double finite difference

Put
$$
N=\sqrt n,\qquad a=n^{1/4},\qquad h=\log2.
$$
For the term indexed by $(j,k)$, set
$$
u=a2^jp,\qquad v=a2^kq.
$$
The factor $2^{j+k}$ cancels the Jacobian apart from $a^{-2}=N^{-1}$, while
$$
-\log p=\log a+jh-\log u,
\qquad
-\log q=\log a+kh-\log v.
$$
Therefore
$$
\sum_{j,k=0}^1(-1)^{2-j-k}(X+jh)(Y+kh)=h^2. \tag{4}
$$
The different upper limits may be extended to infinity with exponentially smaller error. Thus
$$
J_n=\frac{h^2}{N}H_N+o\!\left(N^{-15/4}e^{-4N}\right), \tag{5}
$$
where
$$
H_N=\int_0^\infty\int_0^\infty
A_n(u,v)e^{-N\Psi_n(u,v)}\,du\,dv. \tag{6}
$$

Step 4: Recover the hidden normal form and the coalescing saddle

Since $\delta_n=N^{-1/2}$, direct factorization gives
$$
\Psi_n(u,v)=4+(uv-1)^2+\left((u-v)^2-\delta_n\right)^2, \tag{7}
$$
and
$$
A_n(u,v)=(uv-1)^2-2(u-v)^2\left((u-v)^2-\delta_n\right)
+\frac12(uv-1)(u-v)^2. \tag{8}
$$
Set
$$
x=uv-1,\qquad y=u-v.
$$
This maps the positive quadrant bijectively onto $\{x>-1,\ y\in\mathbb R\}$, with
$$
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|
=\sqrt{y^2+4(1+x)}. \tag{9}
$$
Now scale
$$
x=N^{-1/2}X,\qquad y=N^{-1/4}Y.
$$
Then
$$
N\left[x^2+(y^2-\delta_n)^2\right]
=X^2+(Y^2-1)^2, \tag{10}
$$
while
$$
A_n(u,v)=N^{-1}A_0(X,Y),
$$
where
$$
A_0=X^2-2Y^2(Y^2-1)+\frac12XY^2. \tag{11}
$$
Also, with
$$
Z=X+\frac{Y^2}{4},
$$
we have
$$
\frac1{\sqrt{y^2+4(1+x)}}
=\frac12\left[1-\frac{Z}{2N^{1/2}}+\frac{3Z^2}{8N}+O(N^{-3/2}(1+|Z|^3))\right]. \tag{12}
$$
Therefore
$$
\begin{aligned}
H_N=e^{-4N}N^{-7/4}\frac12
\int_{\mathbb R^2}A_0e^{-X^2-(Y^2-1)^2}
\left[1-\frac{Z}{2N^{1/2}}+\frac{3Z^2}{8N}+O(N^{-3/2})\right]dX\,dY.
\end{aligned} \tag{13}
$$

Step 5: Use the crossover moment recurrence

Let
$$
M_r=\int_{\mathbb R}Y^{2r}e^{-(Y^2-1)^2}\,dY.
$$
Integration by parts applied to $Y^{2r+1}e^{-(Y^2-1)^2}$ gives
$$
M_{r+2}-M_{r+1}=\frac{2r+1}{4}M_r. \tag{14}
$$
In particular $M_0=\mathcal C$. Using (14), parity in $X$, and the Gaussian moments,
$$
\int_{\mathbb R^2}A_0e^{-X^2-(Y^2-1)^2}\,dX\,dY=0, \tag{15}
$$
$$
\int_{\mathbb R^2}A_0Ze^{-X^2-(Y^2-1)^2}\,dX\,dY=0, \tag{16}
$$
and
$$
\int_{\mathbb R^2}A_0Z^2e^{-X^2-(Y^2-1)^2}\,dX\,dY
=\frac{\sqrt\pi\,\mathcal C}{2}. \tag{17}
$$
For example, (15) uses $M_2-M_1=M_0/4$, (16) uses $M_3-M_2=3M_1/4$, and (17) reduces to
$$
\sqrt\pi\left(\frac34M_0+M_1-M_2\right)=\frac{\sqrt\pi M_0}{2}.
$$
Thus from (13),
$$
H_N\sim\frac{3\sqrt\pi\,\mathcal C}{32}N^{-11/4}e^{-4N}. \tag{18}
$$
Hence
$$
J_n\sim\frac{3\sqrt\pi\,\mathcal C}{32}(\log2)^2
N^{-15/4}e^{-4N}. \tag{19}
$$
Combining (1), (3), and (19),
$$
\lambda_n\sim-\frac{3\mathcal C(\log2)^2}{2\sqrt\pi}
\frac{e^{-4\sqrt n}}{n^{7/8}(\log n)^2}.
$$
Therefore
$$
\alpha=\frac78,\qquad \beta=2,\qquad c=4,
\qquad L=-\frac{3\mathcal C(\log2)^2}{2\sqrt\pi}.
$$
Final Answer: $\boxed{\left(\frac78,2,4,-\frac{3\mathcal C(\log2)^2}{2\sqrt\pi}\right)}$

---

## Answer

$\left(\frac78,2,4,-\frac{3\mathcal C(\log2)^2}{2\sqrt\pi}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- hidden symmetric phase factorization
- critically coalescing mixed-order saddle
- crossover moment recurrence
- two consecutive Jacobian cancellations
