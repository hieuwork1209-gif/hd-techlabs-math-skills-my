# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
0<\alpha<\beta,
\qquad
\kappa>0,
\qquad
\tau>0,
$$
and define
$$
A_1=\begin{pmatrix}-\alpha&\kappa\\0&-\beta\end{pmatrix},
\qquad
A_2=A_1^T,
\qquad
\eta=\sqrt{1+\frac{\kappa^2}{(\beta-\alpha)^2}}.
$$
For every piecewise-constant switching signal $\sigma:[0,\infty)\to\{1,2\}$ whose successive switching times are separated by at least $\tau$, let $\Phi_\sigma(t)$ be the fundamental matrix of
$$
\dot x=A_{\sigma(t)}x,
\qquad
\Phi_\sigma(0)=I.
$$
Using the Euclidean operator norm, define
$$
\Lambda_\tau(\alpha,\beta,\kappa)
=\sup_\sigma\limsup_{t\to\infty}
\frac1t\log\|\Phi_\sigma(t)\|_2.
$$
Determine $\Lambda_\tau(\alpha,\beta,\kappa)$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Differential Equations and Dynamical Systems and Stability theory: it asks for the exact worst-case exponential growth rate of a switched linear system subject to a minimum dwell-time constraint. The solution must combine finite-time transient growth of each mode with a global switching bound and an extremal periodic switching law.
