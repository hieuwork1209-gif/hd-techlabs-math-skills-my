# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Put
$$
P=x_1x_2,\qquad Q=x_3x_4,
$$
and define
$$
\mathcal E=\int_{-1}^{\infty}e^{-z^2}\,dz,\qquad
\mu=\frac{e^{-1}}{2\mathcal E},\qquad
\mathcal M=\int_{-1}^{\infty}z(z-\mu)e^{-z^2}\,dz.
$$
For $n\ge1$, let
$$
N=\sqrt n,\qquad \delta=n^{-1/4},\qquad
U_j=\delta^{-1}2^jP,\quad V_k=\delta^{-1}2^kQ.
$$
For $u,v\ge0$, write $r=uv$, $s=(u-v)^2$, and for $t\in\{0,1,2\}$ set
$$
C(s)=\frac{s-\delta}{\delta}-\mu,\qquad
a_t(s)=1+t\delta^3+\delta^2(s-\delta),
$$
$$
\Psi_t(r,s)=4+(s-\delta)^2+(r-a_t(s))^2,
$$
$$
G_t(u,v)=|u^2-v^2|C(s)\left[1-2N(r+1)(r-a_t(s))\right]e^{-N\Psi_t(r,s)}.
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
\lim_{n\to\infty}n^\alpha(\log n)^\beta e^{c\sqrt n}\lambda_n=L.
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

The product-density reduction hides a total-derivative certificate that cancels the apparent bulk saddle exactly. The leading term instead comes from a boundary layer, where a second finite difference and a centered truncated-Gaussian moment produce the first nonzero contribution. This is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
