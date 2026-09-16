# Normalized Math Problem

## LaTeX (Normalized)

Let $0\leq x_1<x_2<x_3<x_4<x_5\leq1$ satisfy
$$
\frac15\sum_{i=1}^5x_i=\frac13.
$$
For
$$
v(x)=\begin{pmatrix}1\\x\\x^2\\x^3\\x^4\end{pmatrix},
$$
define the equally weighted information matrix
$$
M(x_1,\ldots,x_5)=\frac15\sum_{i=1}^5v(x_i)v(x_i)^T.
$$
Determine exactly
$$
\max\det M(x_1,\ldots,x_5).
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

This is an exact D-optimal design problem for quartic polynomial regression with five equally weighted design points and a prescribed design centroid. Maximizing the determinant of the information matrix is an experimental-design optimality criterion, while the centroid condition is a balance constraint on the design. Strict concavity and multiplier arguments provide the optimization certificate, but those tools are subordinate to the experimental-design structure.
