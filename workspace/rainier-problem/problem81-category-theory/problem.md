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
f(L,R)=\left|\{S\subseteq[n]:C(S)=S\}\right|,
$$
$$
h(L,R)=\left|\{S\subseteq[n]:C(S)=S,\ |S|=n-1\}\right|.
$$
Order the pairs $(f(L,R),h(L,R))$ lexicographically. Let
$$
(M_n,H_n)
$$
be the largest possible pair, and let $N_n$ be the number of adjunctions attaining it.

Determine the ordered triple
$$
(M_n,H_n,N_n)
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

The problem asks for a lexicographic extremal profile of fixed objects of the closure monad arising from an adjunction on a finite poset category, followed by a count of all adjunctions attaining equality. The bipartite tree is the atom-level relation canonically encoding the left adjoint; graph-theoretic arguments are derived from the adjunction, its fixed-point condition, and the equality case. Thus Logic, Set Theory, and Foundations -> Category theory is the best fit.
