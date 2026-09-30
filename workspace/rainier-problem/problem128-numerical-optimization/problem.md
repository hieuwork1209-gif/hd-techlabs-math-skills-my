# Normalized Math Problem

## LaTeX (Normalized)

For each integer $d\geq1$, let $\mathcal F_d$ be the class of differentiable convex functions
$
f:\mathbb R^d\to\mathbb R
$
whose gradients are $1$-Lipschitz and which attain their minimum value $f_*$. For $h>0$, perform one gradient step
$$
x_1=x_0-h\nabla f(x_0).
$$
Define
$$
W(h)=
\sup_{\substack{d\geq1,\ f\in\mathcal F_d,\ x_*\in\operatorname*{argmin}f\\
\|x_0-x_*\|\leq1}}
\bigl(f(x_1)-f_*\bigr).
$$
Let $h_*$ be the unique minimizer of $W(h)$ over $h>0$, and let
$$
W_*=\min_{h>0}W(h).
$$
Determine the ordered pair $(h_*,W_*)$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the constant gradient-descent step size that minimizes the exact worst-case one-step objective error over all smooth convex objectives with a normalized initial distance. The main task is parameter tuning for a first-order optimization method under a worst-case performance criterion, so the primary sub-domain is Numerical optimization.
