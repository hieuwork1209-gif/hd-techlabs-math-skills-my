# Normalized Math Problem

## LaTeX (Normalized)

For each integer $n\geq1$ and real $\lambda$, define
$$
I_n(\lambda)=\int_0^1(2x-1)\exp\!\left(-n x^2(1-x)^2(1+x)+\lambda x\right)\,dx.
$$
For each $n$, let $\lambda_n$ be the unique real number satisfying
$$
I_n(\lambda_n)=0.
$$
Determine the exact value of
$$
\lim_{n\to\infty}\sqrt n\left(\lambda_n-\frac12\log2\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for a sharp asymptotic quantity defined implicitly by an exponential integral. The decisive work is to localize the integral near two competing endpoint minima, balance their leading contributions, and compute the first correction needed to locate the implicit root. These are applications of integration and asymptotic evaluation of definite integrals, so Calculus -> Applications of integration is the best fit.
