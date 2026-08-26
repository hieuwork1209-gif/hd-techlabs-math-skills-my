# Normalized Math Problem

## LaTeX (Normalized)

Fix an integer $r\geq2$ and put
$$
n=2^r.
$$

Work in the simply typed linear lambda calculus with exchange, no constants, atomic types $p$ and $q_i$ $(i\in\mathbb Z/n\mathbb Z)$, linear implication $\multimap$, and tensor $\otimes$. There is no weakening or contraction.

Let $\Theta_n$ have curried arguments
$$
b_i:p\multimap p\multimap p,\qquad h_i:p\multimap q_i,\qquad x_i:p,\qquad y_i:p
$$
for $i=0,\ldots,n-1$, followed by result type
$$
q_0\otimes q_1\otimes\cdots\otimes q_{n-1}.
$$
Let $\mathcal N_n$ be the closed beta-eta-long normal inhabitants of $\Theta_n$, up to alpha-conversion.

Let $c$ add $1$ modulo $n$ to every subscript and then restore the binders and tensor components to displayed index order. Define $s$ by
$$
s(x_i)=x_{-i},\quad s(y_i)=y_{-i},\quad
s(b_iUV)=b_{-i}s(V)s(U),\quad
s(h_iU)=h_{-i}s(U),
$$
with all indices modulo $n$, again restoring binders and tensor components to displayed index order. Thus $s^2=1$ and $scs=c^{-1}$, so $c,s$ generate a dihedral group $D_{2n}$ of order $2n$ acting on $\mathcal N_n$.

Determine the number of $D_{2n}$-orbits of size exactly $2n$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Discrete Mathematics and Combinatorics |
| **Sub-domain** | Basic counting principles |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The normal inhabitants are labeled plane binary forests. The hard part is then a dihedral stabilizer count: rotational periodicity, the two reflection classes for even $n$, and their stabilizer intersections must all be controlled exactly. This is an enumerative-combinatorics problem using direct counting and finite group actions.
