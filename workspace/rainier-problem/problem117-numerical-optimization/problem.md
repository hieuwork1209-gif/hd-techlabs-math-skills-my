# Normalized Math Problem

## LaTeX (Normalized)

Let $n\geq3$ and let $A_n\in\mathbb R^{n\times n}$ be the path Hessian
$$
A_n=
\begin{bmatrix}
2&-1&&&\\
-1&2&-1&&\\
&\ddots&\ddots&\ddots&\\
&&-1&2&-1\\
&&&-1&2
\end{bmatrix}.
$$
Define
$$
f_n(x)=\frac12x^TA_nx
\qquad(x\in\mathbb R^n).
$$

Choose a probability vector
$$
p=(p_1,\ldots,p_n),
\qquad
p_i\geq0,
\qquad
\sum_{i=1}^n p_i=1.
$$
Starting from a nonzero $x$, perform one randomized exact coordinate-descent step as follows: sample $I\in\{1,\ldots,n\}$ with $\mathbb P(I=i)=p_i$, and then exactly minimize $f_n$ along coordinate $I$. Equivalently,
$$
x^+=x-\frac{(A_nx)_I}{2}e_I,
$$
where $e_I$ is the $I$th standard basis vector.

Define the worst-case expected one-step energy contraction
$$
\Gamma_n(p)
=
\sup_{x\ne0}
\frac{\mathbb E[f_n(x^+)\mid x]}{f_n(x)}.
$$
Determine the unique probability vector $p^*$ minimizing $\Gamma_n(p)$, and determine the exact optimal value
$$
\Gamma_n^*:=\min_p\Gamma_n(p).
$$
Give the final answer as
$$
\left((p_i^*)_{i=1}^n,\Gamma_n^*\right).
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

This problem asks for the optimal sampling distribution in randomized exact coordinate descent for a structured strongly convex quadratic, minimizing the worst-case expected one-step contraction in the objective energy. The primary task is therefore algorithm-parameter optimization and convergence-rate analysis in Optimization and Numerical Mathematics and Numerical optimization. Linear Algebra, through generalized Rayleigh quotients and positive-semidefinite certificates, is used to prove the sharp rate and uniqueness and is subordinate to the numerical-optimization objective.
