# Normalized Math Problem

## LaTeX (Normalized)

Let $n\geq2$ and regard
$$
[n]=\{0<1<\cdots<n\}
$$
as a category. A contractible Quillen model structure on $[n]$ means a model structure in which every morphism is a weak equivalence.

For such a model structure $\mathcal M$, define
$$
f(\mathcal M)=\left|\{i\in[n]:i\to n\text{ is a fibration}\}\right|,
$$
$$
c(\mathcal M)=\left|\{j\in[n]:0\to j\text{ is a cofibration}\}\right|.
$$
Fix integers $r,s\geq1$ with
$$
r+s\leq n+2.
$$
Let $T_{n;r,s}$ be the number of contractible Quillen model structures $\mathcal M$ on $[n]$ satisfying
$$
f(\mathcal M)=r,\qquad c(\mathcal M)=s.
$$

Determine $T_{n;r,s}$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Logic, Set Theory, and Foundations |
| Sub-domain | Category theory |
| Problem Type | Exact computation |
| Answer Type | Exact scalar |

---

## Domain Explanation

The problem asks for a refined enumeration of Quillen model structures on a finite poset category using the categorical notions of weak factorization systems, fibrant objects, and cofibrant objects. The solution reconstructs the relevant weak factorization system from lifting and factorization properties before translating the resulting categorical data into Dyck-path statistics. Thus Logic, Set Theory, and Foundations -> Category theory is the primary classification, with Catalan enumeration serving as the subordinate combinatorial method.
