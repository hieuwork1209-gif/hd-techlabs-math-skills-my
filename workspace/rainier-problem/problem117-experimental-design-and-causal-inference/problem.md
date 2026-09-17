# Normalized Math Problem

## LaTeX (Normalized)

For $\tau>0$, let
$$
f_1=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
f_2=\begin{pmatrix}0\\1\\0\end{pmatrix},\quad
f_3=\begin{pmatrix}0\\0\\1\end{pmatrix},
$$
$$
f_4(\tau)=\begin{pmatrix}\tau\\1/3\\1/3\end{pmatrix},\qquad
f_5(\tau)=\begin{pmatrix}1/3\\\tau\\1/3\end{pmatrix}.
$$
For weights
$$
w_i\ge0,\qquad \sum_{i=1}^5w_i=1,
$$
define
$$
M_\tau(w)=\sum_{i=1}^5w_if_if_i^T,
\qquad
\Psi(\tau)=\max_w\log\det M_\tau(w),
$$
with $\log\det M=-\infty$ when $M$ is singular.

Set
$$
\tau_c=\sup\{\tau>0:\Psi(\tau)=-3\log3\}.
$$
Determine exactly
$$
\left(
\tau_c,
\lim_{h\downarrow0}
\frac{\Psi(\tau_c+h)-\Psi(\tau_c)}{h^2}
\right).
$$

Your reasoning must prove that the optimizer is uniquely
$$
\left(\frac13,\frac13,\frac13,0,0\right)
$$
for $0<\tau\le\tau_c$, that both $w_4$ and $w_5$ are positive for $\tau>\tau_c$ sufficiently close to $\tau_c$, and that the stated one-sided limit exists.

Give the final answer as an ordered pair.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Experimental design and causal inference |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem asks for the exact simultaneous support transition of a D-optimal approximate design and the second-order sensitivity of the optimal log-determinant information criterion. The primary object is an optimal experimental design through its information matrix, so it belongs to Probability and Statistics, specifically Experimental design and causal inference.
