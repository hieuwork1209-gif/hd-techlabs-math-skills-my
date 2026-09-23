# Normalized Math Problem

## LaTeX (Normalized)

Consider the real degree-four order-two stability polynomials
$$
P(z)=1+z+\frac{z^2}{2}+az^3+bz^4,
\qquad a,b\in\mathbb R.
$$
Restrict to those satisfying
$$
|P(x)|\leq1\qquad(-3\leq x\leq0),
$$
with
$$
P(-3)=1.
$$
For such a polynomial define
$$
I(P)=\sup\left\{
R\geq0:\ |P(iy)|\leq1\ \text{for every }|y|\leq R
\right\}.
$$

Determine exactly
$$
R_*=\max I(P)
$$
over all admissible polynomials. Also determine the unique coefficients $a,b$ that attain this maximum.

Give the final answer as $R_*$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Error analysis and stability |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the degree-four order-two stability polynomial that preserves a prescribed negative-real stability interval while maximizing the symmetric imaginary-axis stability interval. The requested extremum is a stability-region design problem for numerical time-stepping methods, so the primary classification is error analysis and stability.
