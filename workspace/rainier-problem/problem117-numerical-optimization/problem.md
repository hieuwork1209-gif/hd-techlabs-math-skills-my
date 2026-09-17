# Normalized Math Problem

## LaTeX (Normalized)

For
$$
\tau\in[-4,-2],
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
b=\begin{pmatrix}1\\3\\1\\3\end{pmatrix}.
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
Determine all $\tau\in[-4,-2]$ for which $\mathcal X_\tau$ is not a singleton. Prove that there is exactly one such parameter, denote it by $\tau_*$, and determine $\tau_*$ exactly.

Your reasoning must account for every parameter in the interval at which the shifted stationarity system can become singular, distinguish which such candidates actually meet the unit trust-region boundary, and prove the exact number of global minimizers at the exceptional parameter.

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

This problem asks for the exact parameter at which a quadratic trust-region subproblem develops multiple global minimizers. The decisive issue is the numerical-optimization hard case together with feasibility of the singular stationary affine set at the prescribed radius, so the primary classification is Optimization and Numerical Mathematics and Numerical optimization; tridiagonal spectral recurrences provide the structural reduction.
