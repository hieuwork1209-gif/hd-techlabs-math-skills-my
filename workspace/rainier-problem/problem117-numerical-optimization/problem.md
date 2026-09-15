# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A=\begin{bmatrix}
4&1&1\\
1&3&1\\
1&1&2
\end{bmatrix},
\qquad
f(x)=\frac12x^TAx.
$$
A randomized two-coordinate descent step is defined as follows. Choose an index $I\in\{1,2,3\}$ with probabilities
$$
\mathbb P(I=i)=p_i,
\qquad p_i>0,
\qquad p_1+p_2+p_3=1.
$$
After choosing $I=i$, keep coordinate $i$ fixed and re-minimize exactly over the other two coordinates:
$$
x^+=\operatorname*{argmin}_{z\in\mathbb R^3:\ z_i=x_i} f(z).
$$
Define the worst-case expected one-step energy contraction
$$
\rho(p_1,p_2,p_3)
=\sup_{x\ne0}\frac{\mathbb E[f(x^+)\mid x]}{f(x)}.
$$
Determine exactly
$$
\rho_*:=\min_{p_i>0,\ p_1+p_2+p_3=1}\rho(p_1,p_2,p_3),
$$
and determine the unique minimizing sampling distribution. Give the answer as
$$
\left(\rho_*,p_1:p_2:p_3\right).
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

This problem optimizes the sampling law of an exact randomized block-coordinate method for a symmetric positive-definite quadratic. The objective is the worst-case expected energy contraction, so the task is a numerical-optimization problem requiring a global spectral lower-bound certificate together with an equality-case uniqueness argument.
