# Normalized Math Problem

## LaTeX (Normalized)

For each $n\ge1$, let $\lambda_n>-1$ be the unique real number satisfying
$$
\iint_{\substack{(x-1)^2+y^2\le(1+\lambda_n)^2\\
x^2+(y-1)^2\le(1+\lambda_n)^2}}
 e^{-n(x^2+y^2)}\,dx\,dy
=\frac{\pi}{4n}.
$$
Evaluate
$$
\lim_{n\to\infty}n^{3/2}
\left(\lambda_n-\frac{1}{4n}\right).
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

At radius $1$, the two disks centered at $(1,0)$ and $(0,1)$ meet at the origin with perpendicular tangent lines, so their intersection locally approaches a quadrant where the Gaussian mass concentrates. The problem asks for the next radius correction required to capture exactly one quarter of the total Gaussian mass. The second term comes from the interaction of the two curved boundary layers near their common corner, making this a natural asymptotic integration problem in Calculus -> Applications of integration.
