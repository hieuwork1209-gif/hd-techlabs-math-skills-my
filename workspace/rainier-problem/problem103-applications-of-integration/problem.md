# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Put
$$
P=x_1x_2,\qquad Q=x_3x_4,
$$
and define the universal constant
$$
\mathcal C=\int_{-\infty}^{\infty}e^{-(s^2-1)^2}\,ds.
$$
For each integer $n\ge1$, real $\lambda$, and $j,k\in\{0,1\}$, set
$$
U_j=n^{1/4}2^jP,\qquad V_k=n^{1/4}2^kQ,\qquad \delta_n=n^{-1/4}.
$$
For $u,v\ge0$ define
$$
\begin{aligned}
\Psi_n(u,v)=&\ 5+\delta_n^2+u^4+v^4-4uv(u^2+v^2)+7u^2v^2\\
&+(-2+4\delta_n)uv-2\delta_n(u^2+v^2),
\end{aligned}
$$
and
$$
\begin{aligned}
A_n(u,v)=&\ 1-\frac12(u^2+v^2)-uv-2(u^4+v^4)\\
&+\frac{17}{2}uv(u^2+v^2)-12u^2v^2
+2\delta_n(u^2+v^2-2uv).
\end{aligned}
$$
Define
$$
\begin{aligned}
I_n(\lambda)=\int_{[0,1]^4}\Bigg[&\sinh(\lambda)e^{-n(P^2+Q^2)}\\
&+\sum_{j,k=0}^1(-1)^{2-j-k}2^{j+k}
A_n(U_j,V_k)e^{-\sqrt n\,\Psi_n(U_j,V_k)}\Bigg]d\mathbf x.
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

The problem asks for a sharp asymptotic of an implicitly defined root of a four-dimensional integral. A double finite difference removes the logarithmic product density. The remaining phase hides a critically coalescing quadratic-quartic saddle behind a symmetric polynomial; after recovering the nonlinear saddle coordinates, two consecutive Jacobian-moment coefficients cancel before the crossover profile contributes. This is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
