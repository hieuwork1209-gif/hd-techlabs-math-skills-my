# Normalized Math Problem

## LaTeX (Normalized)

For $n\ge1$, define
$$
I_n=\iint_{\mathbb{R}^2}
 e^{-n(x^4+x^2y^2+y^6)}\,dx\,dy.
$$
Let
$$
\gamma=\lim_{m\to\infty}\left(\sum_{k=1}^m\frac1k-\log m\right)
$$
be the Euler-Mascheroni constant. Evaluate
$$
\lim_{n\to\infty}
\left(\sqrt n\,I_n-\frac{\sqrt\pi}{6}\log n\right).
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

The phase $x^4+x^2y^2+y^6$ has a degenerate minimum at the origin with two competing scaling regimes. Their overlap produces a logarithmic term, and the requested limit is the finite part after that divergence is removed. This is a natural degenerate Laplace-asymptotic problem in Calculus -> Applications of integration.
