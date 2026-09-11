# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$ and define
$$
A_1=\begin{pmatrix}-1&a\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\b&-1\end{pmatrix}.
$$
For every piecewise-constant switching signal $\sigma:[0,\infty)\to\{1,2\}$ with finitely many switches on each bounded time interval, consider
$$
\dot z(t)=A_{\sigma(t)}z(t),
\qquad z(t)\in\mathbb R^2.
$$
Determine all pairs $(a,b)$ for which the origin is uniformly globally exponentially stable under arbitrary switching; that is, there exist constants $C,\gamma>0$, depending only on $(a,b)$, such that every switching signal and every initial state satisfy
$$
\|z(t)\|\le C e^{-\gamma t}\|z(0)\|
\qquad(t\ge0).
$$

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

This is a robust stability problem for a switched linear system. Although each subsystem is Hurwitz, arbitrary switching can destabilize the origin. The exact gain region is determined by a common quadratic Lyapunov function together with a sharp periodic-switching obstruction at the boundary of uniform exponential stability.
