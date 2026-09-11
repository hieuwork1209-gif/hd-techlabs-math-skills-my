# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$ and define
$$
A_1=\begin{pmatrix}-1&a\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\b&-1\end{pmatrix}.
$$
Let $\sigma(t)$ be the continuous-time Markov chain on $\{1,2\}$ that jumps from either state to the other at rate $1$. Consider
$$
\dot z(t)=A_{\sigma(t)}z(t),
\qquad z(t)\in\mathbb R^2.
$$
Determine all pairs $(a,b)$ for which the origin is almost surely exponentially stable; that is, there exists $\gamma>0$, depending only on $(a,b)$, such that for every deterministic initial state $z(0)\ne0$ and every initial mode,
$$
\limsup_{t\to\infty}\frac1t\log\frac{\|z(t)\|}{\|z(0)\|}\le-\gamma
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

This is an almost-sure stability problem for a Markov jump linear system. After removing the common scalar decay, the top Lyapunov exponent is determined by the stationary law of a one-dimensional projective piecewise-deterministic Markov process, leading to an exact criterion involving modified Bessel functions.
