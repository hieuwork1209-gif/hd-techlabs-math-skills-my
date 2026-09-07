# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. For $(x_1,x_2,x_3,x_4)\in[0,1]^4$, put
$$
P=x_1x_2,\qquad Q=x_3x_4.
$$
For each integer $n\ge1$ and real $\lambda$, define
$$
\begin{aligned}
I_n(\lambda)=\int_{[0,1]^4}\Bigg[&\sinh(\lambda)e^{-n(P^2+Q^2)}\\
&+\sum_{j,k=0}^1(-1)^{2-j-k}2^{j+k}
\left(n^{1/4}(2^jP+2^kQ)-2^{3/4}\right)^3\\
&\quad\times\exp\!\left(-4^jnP^2-4^knQ^2-\frac1{2^{j+k}PQ}\right)\Bigg]d\mathbf x,
\end{aligned}
$$
where each exponential containing $1/(PQ)$ is interpreted as $0$ when $PQ=0$. For each $n$, let $\lambda_n$ be the unique real number satisfying $I_n(\lambda_n)=0$.

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

The problem asks for a sharp asymptotic of an implicitly defined root of a four-dimensional integral. Splitting the variables into two product coordinates yields a two-dimensional logarithmic density; a double finite difference removes both logarithmic factors, after which the dominant contribution comes from a coupled two-dimensional moving saddle. The centered cubic amplitude annihilates the leading Gaussian term, so the first surviving term is controlled by the cubic part of the phase. This is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
