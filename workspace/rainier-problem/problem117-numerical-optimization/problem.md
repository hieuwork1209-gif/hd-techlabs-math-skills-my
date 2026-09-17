# Normalized Math Problem

## LaTeX (Normalized)

For
$$
\tau\in\left[-\frac52,-\frac{17}{7}\right],
$$
define
$$
A_\tau=
\begin{pmatrix}
-3&1&0&0\\
1&0&1&0\\
0&1&\tau&1\\
0&0&1&4
\end{pmatrix},
\qquad
b=\begin{pmatrix}0\\1\\1\\1\end{pmatrix}.
$$
Consider the unit trust-region problem
$$
m(\tau)=\min_{\|x\|_2\le1}
\left(\frac12x^TA_\tau x+b^Tx\right),
$$
and let
$$
\mathcal X_\tau=
\operatorname*{argmin}_{\|x\|_2\le1}
\left(\frac12x^TA_\tau x+b^Tx\right).
$$
There is exactly one parameter $\tau_*$ in the stated interval for which $\mathcal X_\tau$ is not a singleton. Determine $\tau_*$ exactly.

Your reasoning must also prove that $\mathcal X_\tau$ is a singleton for every $\tau\ne\tau_*$ in the interval, show that $|\mathcal X_{\tau_*}|=2$, and compute $m(\tau_*)$ exactly.

For a polynomial $f$ with a unique real zero in $(a,b)$, write $\operatorname{root}_{(a,b)}(f)$ for that zero.

Give the final answer as $\tau_*$.

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

This problem asks when a parameterized quadratic trust-region problem loses uniqueness and requires an exact characterization of the hard case through the shifted Hessian and the lowest eigenspace. That is a standard structural question in Optimization and Numerical Mathematics and Numerical optimization; the tridiagonal eigenvector recurrence is the linear-algebra mechanism used to locate the exceptional parameter.
