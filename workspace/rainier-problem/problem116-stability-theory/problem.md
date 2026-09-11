# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$, and set
$$
s=a+b,\qquad q=ab.
$$
Define
$$
A_1=\begin{pmatrix}-1&3\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\3&-1\end{pmatrix}.
$$
Let $\sigma(t)$ be the continuous-time Markov chain on $\{1,2\}$ that jumps from state $1$ to state $2$ at rate $a$ and from state $2$ to state $1$ at rate $b$. Consider
$$
\dot z(t)=A_{\sigma(t)}z(t),
\qquad z(t)\in\mathbb R^2.
$$
Determine all pairs $(a,b)$ for which the origin is almost surely exponentially stable but is not mean-square exponentially stable. Almost-sure exponential stability means that for every deterministic $z(0)\ne0$ and either initial mode, the top sample-path exponential rate is strictly negative almost surely. Mean-square exponential stability means that there exist $C,\gamma>0$ such that
$$
\mathbb E\|z(t)\|^2\le Ce^{-\gamma t}\|z(0)\|^2
$$
for every deterministic initial state, either initial mode, and every $t\ge0$.

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

This problem compares almost-sure and mean-square stability for an asymmetric two-state Markov jump linear system. The sample-path exponent is governed by the stationary projective process, while the mean-square threshold is governed by a Perron eigenvalue of the lifted second-moment dynamics; the two criteria depend differently on the total switching rate $s=a+b$ and the product $q=ab$.
