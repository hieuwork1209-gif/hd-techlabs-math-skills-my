# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
T=\{(x,y)\in\mathbb{R}^2:x\geq0,\ y\geq0,\ x+y\leq1\},
\qquad z=1-x-y,
$$
and define
$$
\Delta=(x-y)(y-z)(z-x).
$$
For each integer $n\geq1$, put
$$
I_n=\iint_T \Delta^2 e^{-nxyz}\,dx\,dy.
$$
Let Euler's constant be
$$
\gamma=\lim_{m\to\infty}\left(\sum_{k=1}^m\frac{1}{k}-\log m\right).
$$
Evaluate
$$
\lim_{n\to\infty}
\left(n^2I_n-\frac{n}{10}+6\log n\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The integral is taken over the standard simplex and uses the squared Vandermonde factor, the natural eigenvalue-repulsion weight for three coordinates summing to one. The product $xyz$ vanishes on boundary strata of different codimensions, so the asymptotic expansion receives a simple-pole contribution from edges and a double-pole contribution from vertices. Determining the renormalized limit is an exact asymptotic-integration problem in Calculus -> Applications of integration.
