# Normalized Math Problem

## LaTeX (Normalized)

Let $\mathcal H$ be the set of real-valued absolutely continuous odd functions $f$ on $[-1,1]$ such that
$$
f(-1)=f(1)=0,
\qquad
f'\in L^2(-1,1),
$$
and
$$
\int_{-1}^1xf(x)\,dx=0,
\qquad
\int_{-1}^1x^3f(x)\,dx=0.
$$

Determine the sharp constant $C$ such that
$$
\int_{-1}^1f(x)^2\,dx
\leq
C
\int_{-1}^1f'(x)^2\,dx
$$
for every $f\in\mathcal H$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Functional analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the best constant in a quadratic inequality on a closed linear subspace defined by boundary, parity, and moment constraints. The main task is to identify the constrained Rayleigh minimizer and characterize its eigenvalue through the Euler-Lagrange equation and the induced finite-dimensional compatibility condition. Therefore Analysis / Functional analysis is the primary classification. Differential Equations and Dynamical Systems / Boundary value problems is secondary because the boundary-value equation appears only after the variational reduction.
