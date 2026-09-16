## Steps

Step 1: Recover the relation encoded by the adjunction
Write $\mathcal B_n=\mathcal P([n])$, ordered by inclusion, and let $L\dashv R$ be an adjunction $\mathcal B_n\rightleftarrows\mathcal B_n$. Since $L$ is a left adjoint, it preserves unions. Put
$$
A_i=L(\{i\}).
$$
Then for every $S\subseteq[n]$,
$$
L(S)=\bigcup_{i\in S}A_i.
$$
The adjunction condition $L(S)\subseteq T$ if and only if $S\subseteq R(T)$ now forces
$$
R(T)=\{i\in[n]:A_i\subseteq T\}.
$$
Thus the bipartite graph $G_L$ in the prompt is exactly the relation $i_-\sim j_+$ when $j\in A_i$, and every bipartite relation arises from such an adjunction by the displayed formulas.

For the closure monad $C=RL$,
$$
C(S)=\left\{i\in[n]:A_i\subseteq\bigcup_{s\in S}A_s\right\}.
$$
If $N(S)$ denotes the set of right-hand neighbors of the left vertex set $S_-$ in $G_L$, then
$$
C(S)=S
$$
exactly when every left vertex $i_-\notin S_-$ has a neighbor outside $N(S)$.

Step 2: Identify fixed objects with maximal independent sets
For a fixed point $S=C(S)$ define
$$
I_S=S_-\cup\bigl([n]_+\setminus N(S)\bigr).
$$
This is independent because no vertex of $S_-$ is adjacent to a right vertex outside $N(S)$. It is maximal: every right vertex in $N(S)$ is adjacent to some vertex of $S_-$, while every left vertex outside $S_-$ has, by the fixed-point condition from Step 1, a neighbor in $[n]_+\setminus N(S)$.

Conversely, let $I$ be a maximal independent set of $G_L$ and put $S_-=I\cap[n]_-$, identified with $S\subseteq[n]$. Independence gives
$$
I\cap[n]_+\subseteq[n]_+\setminus N(S).
$$
Every right vertex outside $N(S)$ must actually lie in $I$, since otherwise it could be added to $I$. Hence
$$
I\cap[n]_+=[n]_+\setminus N(S).
$$
For each $i_-\notin S_-$, maximality gives a neighbor in this right-hand set, so $A_i\nsubseteq N(S)$. Therefore $C(S)=S$.

The two constructions are inverse. Consequently
$$
|\{S:C(S)=S\}|=\mu(G_L),
$$
where $\mu(G)$ denotes the number of maximal independent sets of $G$.

Step 3: Prove a uniform bound for maximal independent sets of forests
We first show that every forest $F$ on $m$ vertices satisfies
$$
\mu(F)\leq2^{\lfloor m/2\rfloor}.
$$
Proceed by induction on $m$. If $v$ is isolated, every maximal independent set contains $v$, so
$$
\mu(F)=\mu(F-v),
$$
and the induction bound applies.

Otherwise choose a leaf $u$ with neighbor $v$. Every maximal independent set contains exactly one of $u,v$. Those containing $u$ correspond bijectively to maximal independent sets of $F-\{u,v\}$, and those containing $v$ correspond bijectively to maximal independent sets of $F-N[v]$. Therefore
$$
\mu(F)=\mu(F-\{u,v\})+\mu(F-N[v]).
$$
Both forests on the right have at most $m-2$ vertices, so induction gives
$$
\mu(F)\leq2\cdot2^{\lfloor(m-2)/2\rfloor}=2^{\lfloor m/2\rfloor}.
$$

Step 4: Determine the maximum and construct an extremal adjunction
We prove by induction on $n$ that every tree $T$ on $2n$ vertices satisfies
$$
\mu(T)\leq2^{n-1}+1.
$$
The case $n=1$ is a single edge and has two maximal independent sets.

If $T$ is a star, then $\mu(T)=2$, so suppose it is not a star. Choose a penultimate vertex $v$ on a longest path. Then $v$ has $d\geq1$ leaf neighbors and exactly one nonleaf neighbor $w$. Remove $v$ and its $d$ leaf neighbors, and call the remaining tree $P$. A maximal independent set either contains all $d$ leaf neighbors and not $v$, leaving a maximal independent set of $P$, or contains $v$, forcing $w$ and all those leaves out and leaving a maximal independent set of $P-w$. Thus
$$
\mu(T)=\mu(P)+\mu(P-w).
$$
If $d=1$, then $P$ has $2n-2$ vertices, so the tree induction and Step 3 give
$$
\mu(T)\leq(2^{n-2}+1)+2^{n-2}=2^{n-1}+1.
$$
If $d\geq2$, then $P$ has at most $2n-3$ vertices and $P-w$ at most $2n-4$, so Step 3 gives
$$
\mu(T)\leq2^{n-2}+2^{n-2}=2^{n-1}<2^{n-1}+1.
$$

The bound is attained by a balanced bipartite tree. Take left vertices
$$
c,\ell_1,\ldots,\ell_{n-1}
$$
and right vertices
$$
x,r_1,\ldots,r_{n-1},
$$
with edges $c-x$, $c-r_i$, and $r_i-\ell_i$. If $c$ belongs to a maximal independent set, all $\ell_i$ are then forced in, giving one set. If $c$ does not belong, $x$ is forced in and on each edge $r_i-\ell_i$ exactly one endpoint is chosen independently, giving $2^{n-1}$ sets. Hence this tree has
$$
2^{n-1}+1
$$
maximal independent sets. By Step 1 it comes from an allowed adjunction. Therefore
$$
M_n=2^{n-1}+1.
$$

Step 5: Determine the minimum and construct an extremal adjunction
For $n\geq2$, an allowed tree has bipartition sizes $n,n$, so it cannot be a star. Hence it contains a path on four consecutive vertices $a-b-c-d$. Any independent set in a finite graph extends to a maximal independent set. Extend each of
$$
\{b\},\qquad\{c\},\qquad\{a,d\}
$$
to a maximal independent set. The first contains $b$, the second contains $c$, and the third contains neither $b$ nor $c$, so the three extensions are distinct. Thus every allowed tree has at least three maximal independent sets.

This is sharp. Take a central edge $u-v$ with $u$ on the left and $v$ on the right, attach $n-1$ right leaves to $u$, and attach $n-1$ left leaves to $v$. A maximal independent set either contains $u$, contains $v$, or contains neither; in the third case all leaves are forced. These are exactly three maximal independent sets. Again Step 1 realizes this tree by an allowed adjunction. Hence
$$
m_n=3.
$$

Final Answer: $\boxed{\left(2^{n-1}+1,3\right)}$

---

## Answer

$\left(2^{n-1}+1,3\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- adjunctions on posets
- closure monads
- maximal independent sets
- extremal tree induction
- bipartite relation graphs
