# Normalized Math Problem

## LaTeX (Normalized)

For each $n\ge1$, let $\lambda_n$ be the unique real number satisfying
$$
\int_{-\infty}^{\infty}
\int_{x^3e^{-x}+\lambda_n}^{\infty}
 e^{-n(x^2+y^2)}\,dy\,dx
=\frac{\pi}{2n}.
$$
Evaluate
$$
\lim_{n\to\infty}n^3\left(\lambda_n-\frac{3}{4n^2}\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Real number |

---

## Domain Explanation

The problem asks for the second asymptotic term in the vertical displacement needed for the Gaussian mass above the smooth curve $y=x^3e^{-x}$ to equal one half of the total mass. The leading local contribution is odd and cancels, so the answer comes from the next term in the Gaussian-scaled boundary geometry. This is a natural asymptotic integration problem in Calculus -> Applications of integration.
