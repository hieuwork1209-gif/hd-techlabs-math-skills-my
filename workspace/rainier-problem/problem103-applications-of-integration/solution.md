## Steps

Step 1: Separate the implicit root

Let
$$
A_n=\int_{[0,1]^4}e^{-n(P^2+Q^2)}\,d\mathbf x
$$
and let $J_n=I_n(0)$. Then
$$
I_n(\lambda)=A_n\sinh\lambda+J_n.
$$
Since $A_n>0$, $I_n$ is strictly increasing and tends to $\pm\infty$ as $\lambda\to\pm\infty$. Thus the root is unique and
$$
\sinh\lambda_n=-\frac{J_n}{A_n}. \tag{1}
$$

Step 2: Reduce to the two product coordinates

For every integrable $F$ on $(0,1)^2$,
$$
\int_{[0,1]^4}F(P,Q)\,d\mathbf x
=\int_0^1\int_0^1(-\log p)(-\log q)F(p,q)\,dp\,dq. \tag{2}
$$
Indeed, the product of two independent uniform variables has density $-\log p$ on $(0,1)$, and the two pairs are independent.

Therefore
$$
A_n=\left(\int_0^1(-\log p)e^{-np^2}\,dp\right)^2.
$$
With $y=\sqrt n\,p$,
$$
\int_0^1(-\log p)e^{-np^2}\,dp
=\frac1{\sqrt n}\int_0^{\sqrt n}
\left(\frac12\log n-\log y\right)e^{-y^2}\,dy
\sim\frac{\sqrt\pi}{4}n^{-1/2}\log n.
$$
Hence
$$
A_n\sim\frac\pi{16}n^{-1}(\log n)^2. \tag{3}
$$

Step 3: Collapse the double finite difference

Put
$$
N=\sqrt n,\qquad a=n^{1/4},\qquad h=\log2.
$$
In the term indexed by $(j,k)$, use (2) and set
$$
u=a2^jp,\qquad v=a2^kq.
$$
Then
$$
4^jnp^2+4^knq^2+\frac1{2^{j+k}pq}
=N\Phi(u,v),
\qquad
\Phi(u,v)=u^2+v^2+\frac1{uv}, \tag{4}
$$
and the factor $2^{j+k}$ cancels the Jacobian apart from the common factor $a^{-2}=N^{-1}$. Also
$$
-\log p=\log a+jh-\log u,
\qquad
-\log q=\log a+kh-\log v.
$$
On the common domain, the signed sum factors into two first differences:
$$
\sum_{j,k=0}^1(-1)^{2-j-k}(X+jh)(Y+kh)=h^2. \tag{5}
$$
The pieces outside the common domain have $u\ge a$ or $v\ge a$, hence contribute $O(n^Ce^{-n})$ for some fixed $C$. Extending the common domain to $(0,\infty)^2$ gives
$$
J_n=\frac{h^2}{N}K_N+O(n^Ce^{-n}), \tag{6}
$$
where
$$
K_N=\int_0^\infty\int_0^\infty
\left(u+v-2^{3/4}\right)^3e^{-N\Phi(u,v)}\,du\,dv. \tag{7}
$$

Step 4: Evaluate the parity-delayed two-dimensional saddle

The equations $\nabla\Phi=0$ have the unique positive solution
$$
r=2^{-1/4},\qquad (u,v)=(r,r),
$$
and
$$
c:=\Phi(r,r)=2\sqrt2.
$$
The Hessian there is
$$
H=\begin{pmatrix}6&2\\2&6\end{pmatrix}.
$$
Write
$$
x=u-r,\qquad y=v-r,\qquad
s=\frac{x+y}{\sqrt2},\qquad d=\frac{x-y}{\sqrt2}.
$$
A direct Taylor expansion gives
$$
\Phi(u,v)=c+4s^2+2d^2-\frac{\sqrt2}{r^5}s(s^2+d^2)
+O\!\left((|s|+|d|)^4\right), \tag{8}
$$
while
$$
(u+v-2r)^3=2\sqrt2\,s^3. \tag{9}
$$
Set $s=S/\sqrt N$ and $d=D/\sqrt N$. Then
$$
\begin{aligned}
e^{-N(\Phi-c)}
=e^{-4S^2-2D^2}\Bigg[1
+\frac{\sqrt2}{r^5\sqrt N}S(S^2+D^2)
+O\!\left(\frac{(1+|S|+|D|)^6}{N}\right)\Bigg]. \tag{10}
\end{aligned}
$$
The leading term is odd in $S$ and integrates to zero. Saddle localization gives a Gaussian majorant near $(r,r)$, while away from it $\Phi\ge c+\eta$ for some $\eta>0$, so the expansion can be integrated termwise. Therefore
$$
K_N\sim\frac4{r^5}N^{-3}e^{-cN}
\int_{\mathbb R^2}S^4(S^2+D^2)e^{-4S^2-2D^2}\,dS\,dD. \tag{11}
$$
Using the elementary Gaussian moments,
$$
\int_{\mathbb R^2}S^4(S^2+D^2)e^{-4S^2-2D^2}\,dS\,dD
=\frac{21\sqrt2\,\pi}{2048}.
$$
Since $r^{-5}=2^{5/4}$,
$$
K_N\sim\frac{21\,2^{3/4}\pi}{256}N^{-3}e^{-2\sqrt2N}. \tag{12}
$$
Combining (6) and (12),
$$
J_n\sim\frac{21\,2^{3/4}\pi}{256}(\log2)^2
n^{-2}e^{-2\sqrt{2n}}. \tag{13}
$$

Step 5: Recover the root

By (3) and (13), $J_n/A_n\to0$, so from (1), $\lambda_n\sim-J_n/A_n$. Hence
$$
\lambda_n\sim
-\frac{21(\log2)^2}{2^{13/4}}
\frac{e^{-2\sqrt{2n}}}{n(\log n)^2}.
$$
Thus the unique constants are
$$
\alpha=1,\qquad \beta=2,\qquad c=2\sqrt2,
\qquad L=-\frac{21(\log2)^2}{2^{13/4}}.
$$
Final Answer: $\boxed{\left(1,2,2\sqrt2,-\frac{21(\log2)^2}{2^{13/4}}\right)}$

---

## Answer

$\left(1,2,2\sqrt2,-\frac{21(\log2)^2}{2^{13/4}}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- paired product-coordinate reduction
- double finite-difference cancellation
- coupled two-dimensional saddle
- parity-delayed Laplace asymptotics
- implicit root asymptotics
