## Steps

Step 1: Separate the implicit root

Let
$$
B_n=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf x,
$$
and let $S_n=I_n(0)$. Then
$$
I_n(\lambda)=B_n\sinh\lambda+S_n.
$$
Since $B_n>0$, the root is unique and
$$
\sinh\lambda_n=-\frac{S_n}{B_n}. \tag{1}
$$

Step 2: Evaluate the root denominator

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
N=\sqrt n,\qquad a=n^{1/4},\qquad h=\log2,\qquad \delta=N^{-1/2}.
$$
In the $(j,k)$ term set $u=a2^jp$, $v=a2^kq$. The factor $2^{j+k}$ cancels the Jacobian apart from $a^{-2}=N^{-1}$, and
$$
\sum_{j,k=0}^1(-1)^{2-j-k}(X+jh)(Y+kh)=h^2. \tag{4}
$$
The unequal upper limits contribute only an exponentially smaller error. Therefore
$$
S_n=\frac{h^2}{N}H_N+o\!\left(\delta^{19/2}e^{-4N}\right), \tag{5}
$$
where
$$
H_N=\int_0^\infty\int_0^\infty A_n(u,v)e^{-N\Psi_n(u,v)}\,du\,dv. \tag{6}
$$

Step 4: Recover the nonlinear saddle coordinate

Write
$$
r=uv,\qquad s=(u-v)^2,
$$
and define
$$
K=\left(1+\frac{s}{\delta}\right)(r-1)+(s-\delta). \tag{7}
$$
Expanding (7) shows exactly that the displayed polynomials in the problem satisfy
$$
\Psi_n(u,v)=4+K^2+(s-\delta)^2, \tag{8}
$$
$$
A_n(u,v)=K^3-\frac32\delta^2K. \tag{9}
$$
Now set
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
x=\delta X,\qquad y=\delta^{1/2}Y,\qquad T=Y^2-1.
$$
Since $s=\delta Y^2$,
$$
K=\delta W,\qquad W=(1+Y^2)X+T, \tag{11}
$$
and $N\delta^2=1$. Thus
$$
N(\Psi_n-4)=W^2+T^2,
\qquad
A_n=\delta^3\left(W^3-\frac32W\right). \tag{12}
$$
For fixed $Y$, the map $X\mapsto W$ has derivative $1+Y^2$. Also
$$
\frac1{\sqrt{y^2+4(1+x)}}
=\frac12(1+\delta Z)^{-1/2},
$$
where
$$
Z=X+\frac{Y^2}{4}
=\frac{W-T}{1+Y^2}+\frac{Y^2}{4}. \tag{13}
$$
Hence
$$
\begin{aligned}
H_N=\frac12e^{-4N}\delta^{9/2}\int_{\mathbb R^2}
\frac{\left(W^3-\frac32W\right)e^{-W^2-T^2}}{1+Y^2}
(1+\delta Z)^{-1/2}\,dW\,dY.
\end{aligned} \tag{14}
$$

Step 5: Use the three Gaussian cancellations

Expand
$$
(1+\delta Z)^{-1/2}
=1-\frac12\delta Z+\frac38\delta^2Z^2-\frac5{16}\delta^3Z^3+O(\delta^4). \tag{15}
$$
For
$$
H_3(W)=W^3-\frac32W,
$$
Gaussian moments give
$$
\int_{\mathbb R}H_3(W)W^k e^{-W^2}\,dW=0\quad(k=0,1,2), \tag{16}
$$
and
$$
\int_{\mathbb R}H_3(W)W^3e^{-W^2}\,dW=\frac{3\sqrt\pi}{4}. \tag{17}
$$
Since $Z=(1+Y^2)^{-1}W+b(Y)$, the orders $\delta^0,\delta^1,\delta^2$ in (14) vanish for every $Y$. At order $\delta^3$, only the cubic $W$ term survives, so by the definition of $\mathcal D$,
$$
H_N\sim-\frac{15\sqrt\pi}{128}\mathcal D\,\delta^{15/2}e^{-4N}. \tag{18}
$$
Consequently
$$
S_n\sim-\frac{15\sqrt\pi}{128}\mathcal D(\log2)^2
\delta^{19/2}e^{-4N}. \tag{19}
$$
Because $\delta=n^{-1/4}$, equations (1), (3), and (19) yield
$$
\lambda_n\sim\frac{15\mathcal D(\log2)^2}{8\sqrt\pi}
\frac{e^{-4\sqrt n}}{n^{11/8}(\log n)^2}.
$$
Therefore
$$
\alpha=\frac{11}{8},\qquad \beta=2,\qquad c=4,
\qquad L=\frac{15\mathcal D(\log2)^2}{8\sqrt\pi}.
$$
Final Answer: $\boxed{\left(\frac{11}{8},2,4,\frac{15\mathcal D(\log2)^2}{8\sqrt\pi}\right)}$

---

## Answer

$\left(\frac{11}{8},2,4,\frac{15\mathcal D(\log2)^2}{8\sqrt\pi}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- nonlinear coalescing saddle coordinate
- variable Gaussian shear
- Hermite orthogonality
- three consecutive Jacobian cancellations
