# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A_1=
\begin{bmatrix}
1&1&0\\
1&4&0\\
0&0&2
\end{bmatrix},
\qquad
A_2=
\begin{bmatrix}
2&0&0\\
0&1&2\\
0&2&16
\end{bmatrix},
\qquad
A_3=
\begin{bmatrix}
4&0&1\\
0&2&0\\
1&0&1
\end{bmatrix}.
$$
For a positive diagonal matrix
$$
D=\operatorname{diag}(d_1,d_2,d_3),
\qquad d_1,d_2,d_3>0,
$$
define the robust spectral condition number
$$
\mathcal K(D)
=\max_{1\leq k\leq3}
\frac{\lambda_{\max}(DA_kD)}{\lambda_{\min}(DA_kD)}.
$$
Since multiplying $D$ by a positive scalar does not change $\mathcal K(D)$, regard two positive diagonal matrices as equivalent when they differ by a common positive scalar.

Set
$$
\gamma=\sqrt[3]{16},
\qquad
H=\gamma+\gamma^{-1}.
$$
Determine exactly
$$
\mathcal K_*:=\inf_{D>0\text{ diagonal}}\mathcal K(D),
$$
and determine the unique minimizing scaling class. Give the answer as the ordered pair
$$
\left(\mathcal K_*,d_1:d_2:d_3\right).
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

This problem asks for one positive diagonal preconditioner that is simultaneously effective for three symmetric positive-definite scenario matrices. The objective is the worst spectral condition number across the scenarios, so the task is a robust numerical-preconditioning problem requiring a global minimax certificate and uniqueness of the common scaling class.
