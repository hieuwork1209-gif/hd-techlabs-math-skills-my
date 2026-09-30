# Normalized Math Problem

## LaTeX (Normalized)

Let $\mathcal F$ be the class of differentiable convex functions
$
f:\mathbb{R}^{3}\to\mathbb R
$
whose gradients are $1$-Lipschitz and which attain their minimum value $f_*$. Choose
$
f\in\mathcal F,
\qquad
f(x_*)=f_*,
\qquad
\|x_0-x_*\|\leq1.
$
Perform two exact span searches. First set
$
g_0=\nabla f(x_0),
$
and choose $x_1$ from the affine line $x_0+\operatorname{span}\{g_0\}$ so that
$
f(x_1)=\min_{x\in x_0+\operatorname{span}\{g_0\}}f(x).
$
Then set
$
g_1=\nabla f(x_1),
$
and choose $x_2$ from the affine plane $x_0+\operatorname{span}\{g_0,g_1\}$ so that
$
f(x_2)=\min_{x\in x_0+\operatorname{span}\{g_0,g_1\}}f(x).
$
The supremum below is taken over all such choices for which the displayed minimizers exist:
$$
W_2=\sup\bigl(f(x_2)-f_*\bigr).
$$
Determine $W_2$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for the exact worst-case two-stage objective error of a first-order optimization scheme that minimizes over the span of the gradients collected so far. The main mathematical task is worst-case convergence analysis of an iterative numerical optimization method, so the primary sub-domain is Numerical optimization.
