# Normalized Math Problem

## LaTeX (Normalized)

Let $\xi$ range over all Borel probability measures on $[0,1]$ satisfying
$$
\int_0^1 x\,d\xi(x)=\frac13.
$$
For
$$
v(x)=\begin{pmatrix}1\\x\\x^2\\x^3\\x^4\end{pmatrix},
$$
define the information matrix
$$
M(\xi)=\int_0^1 v(x)v(x)^T\,d\xi(x).
$$
Determine exactly
$$
\max_{\xi}\det M(\xi).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Experimental design and causal inference |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem is an exact constrained optimal-design problem: $M(\xi)$ is the polynomial-regression information matrix of a design measure, and the task is to maximize its determinant subject to an allocation-moment constraint, so Probability and Statistics and Experimental design and causal inference is the primary classification. Convex optimization is a secondary component because concavity of the log-determinant and a dual sensitivity inequality certify global optimality, but those optimization tools are subordinate to the experimental-design structure.
