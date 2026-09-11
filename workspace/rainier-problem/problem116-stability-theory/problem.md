# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$, let $W_t$ be a standard one-dimensional Brownian motion, and define
$$
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
A=-I+aS+J.
$$
Consider the planar linear Stratonovich stochastic differential equation
$$
dZ_t=A Z_t\,dt+bJZ_t\circ dW_t,
\qquad Z_t\in\mathbb R^2.
$$
Determine all pairs $(a,b)$ for which the deterministic system $\dot z=Az$ is not exponentially stable, but the stochastic origin is almost surely exponentially stable; that is, for every deterministic $Z_0\ne0$ there exists a constant $\gamma>0$, depending only on $(a,b)$, such that
$$
\limsup_{t\to\infty}\frac1t\log\frac{\|Z_t\|}{\|Z_0\|}\le-\gamma
$$
almost surely.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Solve for unknowns |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

This is a noise-induced stabilization problem for a planar linear Stratonovich system. The deterministic instability threshold follows from the eigenvalues of a constant strain-plus-rotation matrix, while the stochastic top Lyapunov exponent is determined by a non-equilibrium angular diffusion with nonzero stationary probability flux and an exact complex-order modified-Bessel representation.
