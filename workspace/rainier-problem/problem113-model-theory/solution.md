## Steps

Step 1: Establish the gap invariant for Duplicator
For a cycle with at least one pebbled vertex, list the distinct pebbled vertices in cyclic order. Consecutive pebbled vertices cut the cycle into gaps; the length of a gap is its number of edges. If there is only one distinct pebbled vertex, regard the whole cycle as one circular gap whose length is the length of the cycle.

Suppose the current matching of pebbled vertices preserves cyclic order, up to one global reversal. With $s$ rounds remaining, call a pair of corresponding gaps with lengths $d,e$ admissible when
$$
d=e
$$
or
$$
d,e\geq2^{s+1}.
$$
We claim that if every corresponding gap is admissible, then Duplicator can survive the remaining $s$ rounds.

Use induction on $s$. When $s=0$, every corresponding pair of distinct pebbles is adjacent in one cycle exactly when it is adjacent in the other: a gap of length $1$ must be matched by a gap of length $1$, while two unequal admissible gaps both have length at least $2$. Equality of pebbles is already preserved by repeating a previous response whenever Spoiler repeats a vertex.

Now let $s\geq1$, and suppose Spoiler chooses a new vertex inside a gap of length $d$. If the corresponding gap has the same length $e=d$, Duplicator chooses the vertex at the same distance from the corresponding endpoint. The two new gap pairs then have equal lengths.

Assume instead that
$$
d,e\geq2^{s+1}.
$$
Write the split in Spoiler's gap as
$$
d=a+b,
\qquad
a,b\geq1.
$$
For the next position the threshold is $2^s$. If $a<2^s$, Duplicator chooses the response so that the corresponding first subgap also has length $a$. Then
$$
b\geq2^{s+1}-(2^s-1)>2^s
$$
and the other new subgap in the response cycle also has length greater than $2^s$. The case $b<2^s$ is symmetric. If both $a$ and $b$ are at least $2^s$, Duplicator splits the corresponding gap into two pieces each of length at least $2^s$, which is possible because $e\geq2^{s+1}$.

Thus after the response every new corresponding gap pair is admissible for $s-1$ remaining rounds. The induction proves the claim.

Step 2: Establish the complementary gap strategy for Spoiler
We also need the converse form of the gap criterion. Suppose a corresponding pair of gaps has unequal lengths
$$
d<e
$$
and
$$
d<2^{s+1}.
$$
Then Spoiler can force a win in at most $s$ further rounds while playing inside these gaps.

Again use induction on $s$. For $s=0$, the inequality $d<2$ forces $d=1$. For an ordinary gap with distinct pebbled endpoints, those endpoints are adjacent in the first cycle and not adjacent across the longer gap in the second, so the current matching is already not a partial isomorphism.

Let $s\geq1$. If
$$
d<2^s,
$$
the same pair already satisfies the induction hypothesis with $s-1$ in place of $s$, so Spoiler can win without using all $s$ available rounds.

It remains to consider
$$
2^s\leq d<e.
$$
Spoiler plays in the longer gap at distance exactly $2^s$ from one endpoint. This splits that gap into lengths
$$
2^s
\qquad\text{and}\qquad
e-2^s.
$$
Suppose Duplicator responds inside the shorter gap, splitting it into lengths $a,b$ with
$$
a+b=d.
$$
Because $d<2^{s+1}$, at least one of $a,b$ is less than $2^s$.

If both resulting gap pairs were admissible for $s-1$ rounds, the subgap of length less than $2^s$ would have to equal its corresponding subgap exactly. It cannot correspond to the piece of length $2^s$, so it must equal $e-2^s$. The other response subgap would then have to be at least $2^s$, which would give
$$
d=a+b\geq(e-2^s)+2^s=e,
$$
contrary to $d<e$.

Therefore at least one new corresponding gap pair is unequal and has one length below $2^s$. The induction hypothesis for $s-1$ applies to that pair, so Spoiler wins.

The same first split works for a circular gap whose two endpoints are the same pebbled vertex; after that move the two new gaps have distinct pebbled endpoints, so the ordinary-gap argument applies.

Step 3: Show that Duplicator survives $m$ rounds
Let
$$
N=2^m.
$$
Consider the $m$-round game on
$$
C_N
\qquad\text{and}\qquad
C_{N+1}.
$$
On the first round, Duplicator answers any chosen vertex by an arbitrary vertex of the other cycle. There is then one pebbled vertex in each cycle, so the two circular gaps have lengths
$$
N
\qquad\text{and}\qquad
N+1.
$$
There are $m-1$ rounds left, and
$$
N=2^m=2^{(m-1)+1}.
$$
Hence both circular gaps meet the large-gap threshold from Step 1. Duplicator can therefore maintain the admissible-gap invariant for all remaining rounds.

Thus Duplicator wins the $m$-round game, so Spoiler needs more than $m$ rounds.

Step 4: Show that Spoiler wins in $m+1$ rounds
Now give Spoiler $m+1$ rounds. On the first round, Spoiler chooses any vertex of $C_N$. After Duplicator responds in $C_{N+1}$, the two circular gaps again have lengths
$$
N
\qquad\text{and}\qquad
N+1.
$$
There are now $m$ rounds left. These gap lengths are unequal, and
$$
N=2^m<2^{m+1}.
$$
Step 2 therefore gives Spoiler a winning strategy within those remaining $m$ rounds.

Duplicator survives $m$ rounds by Step 3, while Spoiler wins in $m+1$ rounds. Hence the least winning length is
$$
m+1.
$$
Final Answer: $\boxed{m+1}$

---

## Answer

$m+1$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Ehrenfeucht-Fraisse games
- partial isomorphisms
- cycle gap decompositions
- inductive game strategies
- quantifier rank
