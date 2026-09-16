# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A_5=
\begin{bmatrix}
2&-1&0&0&0\\
-1&2&-1&0&0\\
0&-1&2&-1&0\\
0&0&-1&2&-1\\
0&0&0&-1&2
\end{bmatrix},
\qquad
f_5(x)=\frac12x^TA_5x
\qquad(x\in\mathbb R^5).
$$

Consider randomized exact adjacent-block coordinate descent. Choose a probability vector
$$
p=(p_1,p_2,p_3,p_4),
\qquad
p_i\geq0,
\qquad
\sum_{i=1}^4p_i=1.
$$
Given a current point $x$, sample $I\in\{1,2,3,4\}$ with $\mathbb P(I=i)=p_i$, and replace the adjacent pair $(x_I,x_{I+1})$ by its exact minimizer while keeping the other three coordinates fixed. Equivalently, $x^+$ is the unique vector satisfying
$$
x_j^+=x_j\quad(j\notin\{I,I+1\})
$$
and
$$
f_5(x^+)=\min\left\{f_5(y):y_j=x_j\text{ for }j\notin\{I,I+1\}\right\}.
$$

Define the worst-case one-step expected contraction
$$
\Gamma(p)
=\sup_{x\ne0}
\frac{\mathbb E[f_5(x^+)\mid x]}{f_5(x)}.
$$
Determine exactly
$$
\Gamma_*:=\min_p\Gamma(p),
$$
determine the unique minimizing distribution $p_*$, and determine the linear span $\mathcal L_*$ of all nonzero initial vectors $x$ attaining the supremum in $\Gamma(p_*)$.

Give the final answer as
$$
(p_*,\Gamma_*,\mathcal L_*).
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

This problem asks for the sampling distribution that optimizes the worst-case expected one-step contraction of an exact randomized block coordinate-descent method on a structured positive-definite quadratic, together with the equality-case directions. The primary task is therefore algorithmic minimax tuning in Optimization and Numerical Mathematics and Numerical optimization. Linear Algebra, especially generalized Rayleigh quotients and positive-semidefinite certificates, supplies the proof tools and is subordinate to the optimization objective.
