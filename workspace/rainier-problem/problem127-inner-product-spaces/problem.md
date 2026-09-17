# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
0<\rho<\cos\frac\pi5.
$$
Let $v_1,\ldots,v_5\in\mathbb C^5$ be unit vectors, with indices taken modulo $5$, such that
$$
|\langle v_i,v_{i+1}\rangle|=\rho
$$
for every $i$, and
$$
\prod_{i=1}^5\langle v_i,v_{i+1}\rangle=-\rho^5.
$$
Determine, in closed form as a function of $\rho$, the largest possible value of
$$
|\det[v_1\ v_2\ v_3\ v_4\ v_5]|.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Inner product spaces |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Linear Algebra and Inner product spaces: it asks for a sharp determinant bound under Hermitian inner-product constraints. The cyclic product fixes a gauge-invariant phase obstruction, so the extremal Gram matrix must satisfy both cyclic symmetry and a nontrivial phase-compatibility condition before its spectrum can be optimized.
