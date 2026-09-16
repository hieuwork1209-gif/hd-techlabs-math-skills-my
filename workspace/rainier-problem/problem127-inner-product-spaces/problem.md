# Normalized Math Problem

## LaTeX (Normalized)

Let $v_1,\dots,v_6$ be unit vectors in $\mathbb R^4$ satisfying the unit-norm tight-frame identity
$$
\sum_{i=1}^6 v_i v_i^T=\frac32 I_4.
$$
For each $4$-element subset $I\subset\{1,\dots,6\}$, let
$$
\Delta_I=\left|\det[v_i]_{i\in I}\right|,
$$
where the selected vectors are used as columns in increasing index order.

Determine the maximum possible value of
$$
\prod_{\substack{I\subset\{1,\dots,6\}\\|I|=4}}\Delta_I.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Inner product spaces |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem is primarily Linear Algebra and Inner product spaces: the constraint is the unit-norm tight-frame identity, each $\Delta_I$ is a Gram-volume invariant of a four-vector subframe, and the decisive reduction uses the orthogonal complement of the analysis operator to convert complementary four-dimensional volumes into two-dimensional areas. The final extremal step uses the inner-product geometry of the planar complement, while determinant inequalities are subordinate tools.
