# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. For $(x_1,x_2,x_3,x_4)\in[0,1]^4$, put
$$
P=x_1x_2,\qquad Q=x_3x_4.
$$
For each integer $n\ge1$, real $\lambda$, and $j,k\in\{0,1\}$, set
$$
U_j=n^{1/4}2^jP,\qquad V_k=n^{1/4}2^kQ,
$$
$$
X_{jk}=U_jV_k-1,\qquad D_{jk}=U_j-V_k.
$$
Define
$$
\begin{aligned}
I_n(\lambda)=\int_{[0,1]^4}\Bigg[&\sinh(\lambda)e^{-n(P^2+Q^2)}\\
&+\sum_{j,k=0}^1(-1)^{2-j-k}2^{j+k}
\left(X_{jk}^2-2D_{jk}^4+\frac12X_{jk}D_{jk}^2\right)\\
&\qquad\times\exp\!\left(-\sqrt n\,[4+X_{jk}^2+D_{jk}^4]\right)\Bigg]d\mathbf x.
\end{aligned}
$$
For each $n$, let $\lambda_n$ be the unique real number satisfying $I_n(\lambda_n)=0$.

Determine the unique constants $\alpha>0$, $\beta>0$, $c>0$, and $L\ne0$ such that
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

The problem asks for a sharp asymptotic of an implicitly defined root of a four-dimensional integral. Splitting into two product coordinates creates a two-dimensional logarithmic density, and a double finite difference removes it. The remaining integral has an isolated mixed-order saddle: one direction is quadratic and the other quartic. A nonlinear saddle coordinate change introduces a coupled Jacobian, while the amplitude cancels the first two moment coefficients, so the first nonzero term occurs two orders deeper in the local expansion. This is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
