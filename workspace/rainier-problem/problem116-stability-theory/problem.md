# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$ and define
$$
A_1=\begin{pmatrix}-1&a\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\b&-1\end{pmatrix}.
$$
Let $\sigma(t)$ be the continuous-time Markov chain on $\{1,2\}$ that jumps from either state to the other at rate $1$. Consider the Markov jump linear system
$$
\dot z(t)=A_{\sigma(t)}z(t),
\qquad z(t)\in\mathbb R^2.
$$
Determine all pairs $(a,b)$ for which the origin is uniformly globally mean-square exponentially stable; that is, there exist constants $C,\gamma>0$, depending only on $(a,b)$, such that for every deterministic initial state, every initial mode, and every $t\ge0$,
$$
\mathbb E\|z(t)\|^2\le C e^{-\gamma t}\|z(0)\|^2.
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

This is a mean-square stability problem for a Markov jump linear system. The second moments form a finite-dimensional lifted linear system whose reflection symmetry splits the spectral calculation into two cubic factors; the exact stability threshold is then determined by the Routh-Hurwitz criterion.
