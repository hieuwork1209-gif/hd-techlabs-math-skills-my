# Normalized Math Problem

## LaTeX (Normalized)

For each integer $n\geq1$ and real $\lambda$, define
$$
I_n(\lambda)=2\int_0^1\!\int_0^1\left[
\sinh(\lambda)e^{-n(xy)^2}
+\left(1-\sqrt[3]{2n}\,xy\right)^5
\exp\!\left(-n(xy)^2-\frac1{xy}\right)
\right]dx\,dy,
$$
where the second exponential is interpreted as $0$ when $xy=0$. For each $n$, let $\lambda_n$ be the unique real number satisfying
$$
I_n(\lambda_n)=0.
$$
Determine the unique constants $\alpha>0$, $c>0$, and $L\neq0$ such that
$$
\lim_{n\to\infty}n^\alpha e^{c n^{1/3}}\lambda_n=L.
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

The problem asks for a sharp asymptotic quantity defined by a two-dimensional definite integral. The product $xy$ creates a logarithmic density after reduction to one variable, while the flat exponential term creates a moving saddle at scale $n^{-1/3}$. Its amplitude has a fifth-order zero exactly at that saddle, so several ordinary Laplace contributions cancel before the first nonzero term appears. Determining the surviving balance and the implicit root is an application of asymptotic integration, so Calculus -> Applications of integration is the best fit.
