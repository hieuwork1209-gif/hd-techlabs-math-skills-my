## Steps

Step 1: Prove termination and identify the unique normal form
Write $|t|$ for the number of occurrences of $z$ in a term $t$. Define
$$
P(z)=0,
\qquad
P(b(u,v))=P(u)+P(v)+|u|-1.
$$
For one reduction
$$
b(b(x,y),w)\longrightarrow b(x,b(y,w)),
$$
the value of $P$ changes by
$$
\begin{aligned}
&P(b(b(x,y),w))-P(b(x,b(y,w)))\\
&=\bigl(P(x)+P(y)+P(w)+2|x|+|y|-2\bigr)\\
&\qquad-\bigl(P(x)+P(y)+P(w)+|x|+|y|-2\bigr)\\
&=|x|\geq1.
\end{aligned}
$$
Thus every reduction strictly decreases the nonnegative integer $P$, so every reduction terminates.

A term is irreducible exactly when every internal node has left child $z$. Indeed, any internal left child gives a subterm of the form $b(b(x,y),w)$, while if every left child is $z$ no rule applies. Hence a term with $N$ leaves has a unique irreducible form, the right comb
$$
b\bigl(z,b(z,\ldots,b(z,z)\ldots)\bigr).
$$
Therefore every reduction of $T_h$ can be completed and every complete reduction ends at the same normal form.

Step 2: Determine the shortest possible complete reduction
Let $\rho(t)$ be the number of internal nodes on the right spine of $t$, obtained by starting at the root and repeatedly taking the right child, and set
$$
Q(t)=|t|-1-\rho(t).
$$
If a rewrite is performed at a node not on the right spine, then $\rho$ is unchanged. If it is performed at a right-spine node, then locally
$$
b(b(x,y),w)\longrightarrow b(x,b(y,w))
$$
replaces one right-spine edge into $w$ by two successive right-spine edges through $b(y,w)$, so $\rho$ increases by exactly $1$. Hence every step decreases $Q$ by either $0$ or $1$.

The normal form with $N$ leaves has right-spine length $N-1$, so its $Q$-value is $0$. Thus every complete reduction from $t$ has at least $Q(t)$ steps. This bound is attained. If $t$ is not normal, then some node on its right spine has an internal left child; otherwise every right-spine node would have left child $z$, which already makes the whole tree a right comb. Reducing such a right-spine redex decreases $Q$ by exactly $1$. Repeating this choice reaches the normal form in exactly $Q(t)$ steps.

For $T_h$, there are $2^h$ leaves and the right spine has $h$ internal nodes, so the minimum complete-reduction length is
$$
2^h-h-1.
$$

Step 3: Determine the longest possible complete reduction
By Step 1, each rewrite decreases $P$ by $|x|\geq1$, while the normal form has $P=0$. Therefore every complete reduction from $t$ has at most $P(t)$ steps.

This upper bound is also attained. If $t$ is not normal, choose any redex. If its displayed first component $x$ is not $z$, then the left child $b(x,y)$ is itself a redex; descend to that redex and continue. Since the tree is finite, this process reaches a redex of the form
$$
b(b(z,y),w),
$$
for which $|x|=1$. Reducing such a redex decreases $P$ by exactly $1$. Repeating this choice therefore gives a complete reduction of exactly $P(t)$ steps.

Let $p_h=P(T_h)$. Since $T_h=b(T_{h-1},T_{h-1})$ and $|T_{h-1}|=2^{h-1}$,
$$
p_h=2p_{h-1}+2^{h-1}-1,
\qquad
p_1=0.
$$
Induction gives
$$
p_h=(h-2)2^{h-1}+1.
$$
Hence this is the maximum complete-reduction length of $T_h$.

Step 4: Show that every intermediate length occurs
It remains to exclude gaps between the two extremal lengths. Consider all complete reductions from a fixed term $t$. We show by induction on $P(t)$ that any two complete reductions can be connected by a chain of complete reductions in which consecutive lengths differ by at most $1$.

If the two reductions begin with the same redex, apply the induction hypothesis to the two tails after that common first step. Suppose their first redexes are distinct. If the two redexes are disjoint, or one lies entirely inside one of the variable subterms of the other rule instance, the rule is linear and the two contractions commute: doing them in either order reaches the same term in two steps. Appending one fixed completion from that common term gives two complete reductions of equal length, and the induction hypothesis connects each original tail to the corresponding commuting tail because the first reduct has smaller $P$.

The only genuine overlap occurs, up to context, in
$$
b(b(b(r,s),u),v).
$$
Reducing the outer redex first gives
$$
b(b(r,s),b(u,v))\longrightarrow b(r,b(s,b(u,v)))
$$
in two steps total from the source. Reducing the inner redex first gives
$$
b(b(r,b(s,u)),v)
\longrightarrow b(r,b(b(s,u),v))
\longrightarrow b(r,b(s,b(u,v)))
$$
in three steps total. Thus the unique critical overlap is a pentagon whose two sides have lengths $2$ and $3$. As in the commuting case, append a fixed completion from the common endpoint and use induction on the smaller first reducts. This proves the connectivity claim.

Take a shortest complete reduction and a longest one. Along a connecting chain, the integer-valued length changes by at most $1$ at each move. Therefore every integer between the minimum and maximum lengths is attained.

Step 5: Evaluate the full length spectrum for the balanced term
Steps 2 and 3 give the endpoints for $T_h$, and Step 4 shows that no integer between them is missing. Therefore
$$
\mathcal L_h=
\left\{\ell\in\mathbb Z:2^h-h-1\leq\ell\leq(h-2)2^{h-1}+1\right\}.
$$
Final Answer: $\boxed{\{\ell\in\mathbb{Z}:2^h-h-1\leq\ell\leq(h-2)2^{h-1}+1\}}$

---

## Answer

$\{\ell\in\mathbb{Z}:2^h-h-1\leq\ell\leq(h-2)2^{h-1}+1\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- term rewriting systems
- termination potentials
- binary tree rotations
- critical pair analysis
- local confluence
