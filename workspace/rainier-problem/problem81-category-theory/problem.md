# Normalized Math Problem

## LaTeX (Normalized)

For $n\geq2$, let $[n]=\{1,\ldots,n\}$ and let
$$
\mathcal B_n=\mathcal P([n])
$$
be the Boolean lattice, regarded as a category under inclusion. Consider adjunctions
$$
L\dashv R:\mathcal B_n\rightleftarrows\mathcal B_n.
$$
Since $L$ preserves unions, associate to $L$ a bipartite graph $G_L$ with left and right vertex sets both equal to $[n]$, joining $i$ on the left to $j$ on the right exactly when
$$
j\in L(\{i\}).
$$
Restrict to adjunctions for which $G_L$ is a tree.

Let $C=RL$ be the induced closure monad and define
$$
f(L,R)=\left|\{S\subseteq[n]:C(S)=S\}\right|.
$$
Let $M_n$ and $m_n$ be respectively the largest and smallest possible values of $f(L,R)$ over all such adjunctions.

Determine the ordered pair
$$
(M_n,m_n)
$$
exactly for every $n\geq2$.

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

The problem asks for extremal numbers of fixed objects of the closure monad arising from an adjunction on a finite poset category. The bipartite tree is the atom-level relation that canonically encodes the left adjoint, and the graph-theoretic argument is derived from the adjunction and its fixed-point condition. Thus Logic, Set Theory, and Foundations -> Category theory is the best fit.
