# Normalized Math Problem

## LaTeX (Normalized)

Let $V$ be a $9$-dimensional complex vector space equipped with a nondegenerate symmetric bilinear form $\langle\cdot,\cdot\rangle$. Let $N:V\to V$ be nilpotent with a single Jordan block of size $9$, and assume that $N$ is skew-adjoint:
$$
\langle Nv,w\rangle+\langle v,Nw\rangle=0
$$
for all $v,w\in V$.

Set
$$
W=\Lambda^4V,
$$
and let $D:W\to W$ be the induced derivation
$$
D(v_1\wedge v_2\wedge v_3\wedge v_4)
=\sum_{j=1}^{4}v_1\wedge\cdots\wedge Nv_j\wedge\cdots\wedge v_4.
$$
Equip $W$ with the induced symmetric bilinear form
$$
B(v_1\wedge\cdots\wedge v_4,w_1\wedge\cdots\wedge w_4)
=\det\bigl(\langle v_i,w_j\rangle\bigr)_{i,j=1}^{4}.
$$
Define
$$
\mathfrak{so}(W,B)
=\{T\in\operatorname{End}_{\mathbb C}(W):B(Tu,v)+B(u,Tv)=0\text{ for all }u,v\in W\}.
$$
Determine exactly
$$
\dim_{\mathbb C}\{T\in\mathfrak{so}(W,B):TD=DT\}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Linear transformations |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The central object is a nilpotent linear transformation and the space of skew-adjoint endomorphisms commuting with its induced action on an exterior power. The bilinear form supplies a natural structural constraint on the commutant, but the requested quantity is determined by the Jordan structure and centralizer of a linear transformation, so Linear Algebra -> Linear transformations is the best fit rather than Inner product spaces or Tensor and multilinear algebra.
