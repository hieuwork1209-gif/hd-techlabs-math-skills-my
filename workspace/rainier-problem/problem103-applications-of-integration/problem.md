# Normalized Math Problem

## LaTeX (Normalized)

For $n\ge1$, define
$$
M_n=\int_{-1/2}^{1/2}
\int_{x^2}^{\frac{1-\sqrt{1-4x^2}}{2}}
 e^{-n(x^2+y^2)}\,dy\,dx.
$$
Evaluate
$$
\lim_{n\to\infty}n^{7/2}
\left(M_n-\frac{3\sqrt\pi}{4n^{5/2}}\right).
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

The upper graph is the lower arc of the circle $x^2+(y-1/2)^2=1/4$, which is the osculating circle of the parabola $y=x^2$ at the origin. The Gaussian localizes the integral near this fourth-order contact point. The leading term comes from the quartic separation of the curves, while the next term couples the sixth-order geometric correction with the vertical Gaussian decay. This is a natural asymptotic integration problem in Calculus -> Applications of integration.
