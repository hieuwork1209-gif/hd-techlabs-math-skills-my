# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. For $(x_1,x_2,x_3,x_4)\in[0,1]^4$, put
$$
P=x_1x_2,\qquad Q=x_3x_4.
$$
For each integer $n\ge1$, real $\lambda$, and $j,k\in\{0,1\}$, set
$$
U_j=n^{1/4}2^jP,\qquad V_k=n^{1/4}2^kQ.
$$
Define
$$
\begin{aligned}
I_n(\lambda)=\int_{[0,1]^4}\Bigg[&\sinh(\lambda)e^{-n(P^2+Q^2)}\\
&+\sum_{j,k=0}^1(-1)^{2-j-k}2^{j+k}\Bigg\{
 e^{-\sqrt n[4+(U_j^2+V_k^2-1)^2]}\\
&\qquad-\sqrt\pi\,n^{1/4}e^{-\sqrt n(4+U_j^2+V_k^2)}
+\frac\pi8\sqrt n\,e^{-\sqrt n(5+U_j+V_k)}
\Bigg\}\Bigg]d\mathbf x.
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

The problem asks for a sharp asymptotic of an implicitly defined root of a four-dimensional integral. Splitting into two product coordinates creates a two-dimensional logarithmic density, and a double finite difference removes it. The surviving integral couples a radial Morse-Bott saddle, an isolated Gaussian saddle tuned to cancel its full local contribution, and a corner endpoint term that cancels the leading exponentially smaller tail. The first nonzero term is therefore a subleading endpoint correction, so Calculus -> Applications of integration is the best fit.
