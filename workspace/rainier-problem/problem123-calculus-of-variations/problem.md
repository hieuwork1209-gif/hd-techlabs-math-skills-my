# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\mathcal V=\left\{f\in H^2(-1,1):
 f(-x)=f(x),\ f(\pm1)=f'(\pm1)=0,\ \int_{-1}^1 f(x)\,dx=0\right\}.
$$
Determine exactly
$$
\Lambda
=\inf_{0\ne f\in\mathcal V}
\frac{\displaystyle\int_{-1}^1 (f''(x))^2\,dx}
{\displaystyle\int_{-1}^1 f(x)^2\,dx}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Calculus of variations |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The requested quantity is the sharp value of a constrained Rayleigh-quotient minimization for the bending energy of an even clamped function. Its defining task is therefore a variational extremum with a linear integral constraint; the fourth-order boundary-value equation and its secular spectrum arise from the Euler-Lagrange condition.
