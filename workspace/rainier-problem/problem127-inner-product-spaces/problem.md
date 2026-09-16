# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge4$, and let $(v_1,\dots,v_n)$ be a basis of $\mathbb R^n$ such that
$$
\|v_i\|=1
$$
for every $i$, and for some positive real number $a$,
$$
|\langle v_i,v_j\rangle|=a
\qquad(i\ne j).
$$
Let $(w_1,\dots,w_n)$ be the Euclidean dual basis, so
$$
\langle v_i,w_j\rangle=\delta_{ij},
$$
and define
$$
z_i=\frac{w_i}{\|w_i\|}.
$$
Suppose that
$$
|\langle z_i,z_j\rangle|=\frac12
\qquad(i\ne j).
$$
Determine $a$ in terms of $n$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Inner product spaces |
| **Problem Type** | Parameter identification |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Linear Algebra and Inner product spaces: a unit equiangular basis and its Euclidean dual basis are linked through inverse Gram matrices, while normalizing the dual vectors turns that inverse relation into a correlation-matrix reconstruction problem. Positive definiteness imposes a global compatibility condition on the signs of the dual correlations, and resolving that compatibility determines the original common angle.
