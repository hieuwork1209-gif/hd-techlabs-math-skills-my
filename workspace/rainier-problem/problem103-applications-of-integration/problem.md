# Normalized Math Problem

## LaTeX (Normalized)

For each $n\ge1$, let $\lambda_n>-1$ be the unique real number satisfying
$$
\iint_{(x-1)^2+y^2\le(1+\lambda_n)^2}
 e^{-n(x^2+y^2)}\,dx\,dy
=\frac{\pi}{2n}.
$$
Evaluate
$$
\lim_{n\to\infty}n^2\left(\lambda_n-\frac{1}{4n}\right).
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

The disk centered at $(1,0)$ with radius $1$ is tangent to the origin, where the Gaussian mass concentrates as $n\to\infty$. The problem asks for the second asymptotic correction to the radius needed to capture exactly half of the Gaussian mass. The leading correction comes from the circle's curvature, while the next term also uses the cubic nonlinearity of the Gaussian tail. This is a natural asymptotic integration problem in Calculus -> Applications of integration.
