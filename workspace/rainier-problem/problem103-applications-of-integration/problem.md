# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Put
$$
P=x_1x_2,\qquad Q=x_3x_4.
$$
For $n\ge1$, let
$$
N=\sqrt{n},\qquad \delta=n^{-1/4},\qquad
U_j=\delta^{-1}2^jP,\quad V_k=\delta^{-1}2^kQ.
$$
For $u,v\ge0$, write
$$
r=uv,\qquad s=(u-v)^2,
$$
and for $t\in\{0,1,2\}$ set
$$
a_t=1+t\delta^3,\qquad b_t=1+(t+1)\delta^3,
$$
$$
\Psi_t(r,s)=4+(r-a_t)^2+(s-b_t)^2,
$$
$$
G_t(u,v)=-2N|u^2-v^2|(r+s+1)
\left(r+s-1-\frac{\delta^2}{4}\right)
(r-s+\delta^3)e^{-N\Psi_t(r,s)}.
$$
Define
$$
\begin{aligned}
I_n(\lambda)=\int_{[0,1]^4}\Bigg[&\sinh(\lambda)e^{-n(P^2+Q^2)}\\
&+\sum_{j,k=0}^1\sum_{t=0}^2(-1)^{j+k+t}\binom{2}{t}2^{j+k}G_t(U_j,V_k)\Bigg]d\mathbf{x}.
\end{aligned}
$$
For each $n$, let $\lambda_n$ be the unique real root of $I_n(\lambda)=0$. Determine the unique $\alpha,\beta,c>0$ and $L\ne0$ such that
$$
\lim_{n\to\infty}n^\alpha(\log n)^\beta e^{c\sqrt{n}}\lambda_n=L.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The product-density reduction hides a directional-derivative identity whose two boundary contributions have the same exponential action. Their leading Gaussian terms cancel again under a second finite difference, so the first nonzero contribution is a coupled boundary correction. This is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
