# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$, let $W_t$ be a standard one-dimensional Brownian motion, and define
$$
A=\begin{pmatrix}-1&a\\a&-1\end{pmatrix},
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$
Consider the linear Stratonovich stochastic differential equation
$$
dZ_t=A Z_t\,dt+bJZ_t\circ dW_t,
\qquad Z_t\in\mathbb R^2.
$$
Determine all pairs $(a,b)$ for which the origin is almost surely exponentially stable but is not mean-square exponentially stable. Here almost-sure exponential stability means that there exists $\gamma>0$ such that for every deterministic $Z_0\ne0$,
$$
\limsup_{t\to\infty}\frac1t\log\frac{\|Z_t\|}{\|Z_0\|}\le-\gamma
$$
almost surely, while mean-square exponential stability means that there exist $C,\gamma>0$ such that
$$
\mathbb E\|Z_t\|^2\le Ce^{-\gamma t}\|Z_0\|^2
$$
for every deterministic $Z_0$ and every $t\ge0$.

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

This problem compares two distinct stochastic stability notions for a planar linear Stratonovich system. The almost-sure exponent is determined by the invariant law of an angular diffusion, while mean-square stability is governed by a closed second-moment system; the required region is where these two criteria separate.
