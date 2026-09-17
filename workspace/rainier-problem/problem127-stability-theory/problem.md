# Normalized Math Problem

## LaTeX (Normalized)

Let $\alpha,\beta,\kappa>0$, and define
$$
A_1=\begin{pmatrix}-\alpha&\kappa\\0&-\beta\end{pmatrix},
\qquad
A_2=A_1^T.
$$
For every piecewise-constant switching signal $\sigma:[0,\infty)\to\{1,2\}$ having only finitely many switches on each bounded interval, let $\Phi_\sigma(t)$ be the fundamental matrix of
$$
\dot x=A_{\sigma(t)}x,
\qquad
\Phi_\sigma(0)=I.
$$
Using the Euclidean operator norm, define
$$
\Lambda(\alpha,\beta,\kappa)
=\sup_\sigma\limsup_{t\to\infty}
\frac1t\log\|\Phi_\sigma(t)\|_2.
$$
Determine $\Lambda(\alpha,\beta,\kappa)$ exactly.

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

This problem is primarily Differential Equations and Dynamical Systems and Stability theory: it asks for the exact worst-case exponential growth rate of a switched linear system over all admissible switching laws. The classification requires both a switching-independent Lyapunov bound and a matching family of switching signals that asymptotically saturates it.
