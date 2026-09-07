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

Step 3: Collapse both finite differences

Put
$$
N=\sqrt n,\qquad h=\log2,\qquad \delta=N^{-1/2}=n^{-1/4}.
$$
In the $(j,k,t)$ term set $u=n^{1/4}2^jp$, $v=n^{1/4}2^kq$. The $(j,k)$ alternating sum of the product-density logarithms is exactly $h^2$. Therefore
$$
S_n=\frac{h^2}{N}(H_0-2H_1+H_2)+o\!\left(\delta^{25/2}e^{-4N}\right), \tag{4}
$$
where $H_t$ is the $(u,v)$ integral of $A_t(e^{-N\Phi_t^+}-e^{-N\Phi_t^-})$ over the positive quadrant.

Step 4: Put the three saddle families in one normal form

Write
$$
K_t=\left(1+\frac{s}{\delta}\right)R_t+(s-\delta).
$$
Then exactly
$$
\Phi_t^\pm=4+(K_t\mp\delta)^2+(s-\delta)^2,
\qquad
A_t=K_t^2-\frac52\delta^2. \tag{5}
$$
Set $x=uv-1$, $y=u-v$. Since
$$
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|=\sqrt{y^2+4(1+x)}, \tag{6}
$$
scale
$$
x=\delta X,\qquad y=\delta^{1/2}Y,\qquad T=Y^2-1,
$$
and put
$$
a=1+Y^2,\qquad W=aX+T-ta\delta. \tag{7}
$$
Then $K_t=\delta W$, $N\delta^2=1$, and
$$
N(\Phi_t^\pm-4)=(W\mp1)^2+T^2,
\qquad
A_t=\delta^2\left(W^2-\frac52\right). \tag{8}
$$
If
$$
Z=\frac{W-T}{a}+\frac{Y^2}{4},
$$
then
$$
H_t=\frac12e^{-4N}\delta^{7/2}\int_{\mathbb R^2}
\frac{Q(W)e^{-T^2}}a(1+\delta Z+t\delta^2)^{-1/2}\,dW\,dY, \tag{9}
$$
where
$$
Q(W)=\left(W^2-\frac52\right)\left(e^{-(W-1)^2}-e^{-(W+1)^2}\right). \tag{10}
$$

Step 5: Use the second family difference and moment annihilation

The needed moments are
$$
\int W^kQ(W)\,dW=0\quad(k=0,1,2),
\qquad
\int W^3Q(W)\,dW=7\sqrt\pi. \tag{11}
$$
For $f_t=(1+\delta Z+t\delta^2)^{-1/2}$,
$$
\begin{aligned}
f_0-2f_1+f_2={}&\frac34\delta^4-\frac{15}{8}\delta^5Z
+\delta^6\left(\frac{105}{32}Z^2-\frac{15}{8}\right)\\
&+\delta^7\left(-\frac{315}{64}Z^3+\frac{105}{16}Z\right)+O(\delta^8(1+|Z|^4)).
\end{aligned} \tag{12}
$$
By (11), all terms through order $\delta^6$ vanish after integration, as does the linear $Z$ term at order $\delta^7$. Only the $W^3/a^3$ part of $Z^3$ survives. Hence, by the definition of $\mathcal D$,
$$
H_0-2H_1+H_2\sim-\frac{2205\sqrt\pi}{128}\mathcal D\,\delta^{21/2}e^{-4N}. \tag{13}
$$
Thus
$$
S_n\sim-\frac{2205\sqrt\pi}{128}\mathcal D(\log2)^2\delta^{25/2}e^{-4N}. \tag{14}
$$
Combining (1), (3), and (14),
$$
\lambda_n\sim\frac{2205\mathcal D(\log2)^2}{8\sqrt\pi}
\frac{e^{-4\sqrt n}}{n^{17/8}(\log n)^2}.
$$
Therefore
$$
\alpha=\frac{17}{8},\qquad \beta=2,\qquad c=4,
\qquad L=\frac{2205\mathcal D(\log2)^2}{8\sqrt\pi}.
$$
Final Answer: $\boxed{\left(\frac{17}{8},2,4,\frac{2205\mathcal D(\log2)^2}{8\sqrt\pi}\right)}$

---

## Answer

$\left(\frac{17}{8},2,4,\frac{2205\mathcal D(\log2)^2}{8\sqrt\pi}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- second finite difference of saddle families
- common nonlinear saddle normal form
- signed Gaussian moment annihilation
- delayed Jacobian curvature term
