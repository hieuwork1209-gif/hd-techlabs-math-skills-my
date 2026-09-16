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
c(\mathcal M)=\left|\{j\in[n]:0\to j\text{ is a cofibration}\}\right|,
$$
and let $\nu(\mathcal M)$ be the total number of morphisms of $[n]$ that are fibrations, including identities.

Fix integers $r,s\geq1$ with
$$
3\leq r+s\leq n+2,
$$
and put
$$
t=n+2-r-s.
$$
Write $x_+=\max\{x,0\}$, and let $[P]$ denote $1$ if a statement $P$ holds and $0$ otherwise.

Among all contractible model structures satisfying
$$
f(\mathcal M)=r,\qquad c(\mathcal M)=s,
$$
let $A_{n;r,s}$ be the maximum possible value of $\nu(\mathcal M)$, and let $K_{n;r,s}$ be the number of model structures attaining this maximum.

Determine the ordered pair
$$
(A_{n;r,s},K_{n;r,s})
$$
exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Logic, Set Theory, and Foundations |
| Sub-domain | Category theory |
| Problem Type | Optimization |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem asks for an extremal refinement of contractible Quillen model structures on a finite poset category, using fibrant objects, cofibrant objects, and the total size of the fibration class. The solution reconstructs the weak factorization system from lifting and factorization properties before translating the categorical data into ordered-forest statistics whose equality cases must be classified. Thus Logic, Set Theory, and Foundations -> Category theory is primary, with Catalan combinatorics serving as the subordinate method.
