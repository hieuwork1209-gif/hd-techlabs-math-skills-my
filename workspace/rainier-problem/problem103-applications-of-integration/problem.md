# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Put
$$
P=x_1x_2,\qquad Q=x_3x_4,
$$
and define
$$
\mathcal D=\int_{-\infty}^{\infty}\frac{e^{-(z^2-1)^2}}{(1+z^2)^4}\,dz.
$$
For $n\ge1$, $j,k,t\in\{0,1\}$, set
$$
U_j=n^{1/4}2^jP,\quad V_k=n^{1/4}2^kQ,\quad \delta=n^{-1/4}.
$$
For $u,v\ge0$, write $r=uv$, $s=(u-v)^2$, $R_t=r-1-t\delta^2$, and define
$$
\begin{aligned}
\Phi_t^\pm(u,v)=4&+\left(1+\frac{s}{\delta}\right)^2R_t^2
+2\left(1+\frac{s}{\delta}\right)(s-\delta\mp\delta)R_t\\
&+(s-\delta\mp\delta)^2+(s-\delta)^2,
\end{aligned}
$$
$$
A_t(u,v)=\left(1+\frac{s}{\delta}\right)^2R_t^2
+2\left(1+\frac{s}{\delta}\right)(s-\delta)R_t
+(s-\delta)^2-\frac52\delta^2.
$$
Define
$$
\begin{aligned}
I_n(\lambda)=\int_{[0,1]^4}\Bigg[&\sinh(\lambda)e^{-n(P^2+Q^2)}\\
&+\sum_{j,k,t=0}^1(-1)^{3-j-k-t}2^{j+k}A_t(U_j,V_k)
\left(e^{-\sqrt n\,\Phi_t^+(U_j,V_k)}-e^{-\sqrt n\,\Phi_t^-(U_j,V_k)}\right)\Bigg]d\mathbf x.
\end{aligned}
$$
For each $n$, let $\lambda_n$ be the unique real root of $I_n(\lambda)=0$.
Determine the unique $\alpha,\beta,c>0$ and $L\ne0$ such that
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

The problem asks for a sharp asymptotic of an implicitly defined root of a four-dimensional integral. After a finite-difference reduction, two equal-action saddle families agree through their first surviving local term and separate only through a subleading saddle translation, so the asymptotic requires coupled saddle cancellation rather than a single-channel expansion. This is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
