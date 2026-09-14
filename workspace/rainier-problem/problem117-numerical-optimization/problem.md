# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A=\begin{bmatrix}
4&1&1\\
1&3&1\\
1&1&2
\end{bmatrix}.
$$
For a positive diagonal matrix
$$
D=\operatorname{diag}(d_1,d_2,d_3),
\qquad d_1,d_2,d_3>0,
$$
define
$$
\kappa(D)=\frac{\lambda_{\max}(DAD)}{\lambda_{\min}(DAD)}.
$$
Since multiplying $D$ by a positive scalar does not change $\kappa(D)$, regard two positive diagonal matrices as equivalent when they differ by a common positive scalar.

Determine exactly
$$
\kappa_*:=\inf_{D>0\text{ diagonal}}\kappa(D),
$$
and determine the unique minimizing scaling class. Give the answer as the ordered pair
$$
\left(\kappa_*,d_1:d_2:d_3\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem asks for the optimal positive diagonal congruence preconditioner of a fixed symmetric positive-definite matrix, measured by the spectral condition number. It requires a global lower-bound certificate, attainment, and uniqueness of the optimal scaling class.
