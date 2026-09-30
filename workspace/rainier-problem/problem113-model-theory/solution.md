## Steps

Step 1: Set up the interval invariant
For a finite linear order, adjoin two virtual endpoints
$$
-\infty
\qquad\text{and}\qquad
+\infty.
$$
After some rounds, list the distinct pebbled elements in increasing order between these endpoints. Consecutive pebbled or virtual endpoints determine gaps. The size of a gap is the number of unpebbled elements strictly between its endpoints.

A partial isomorphism between two linear orders must preserve the order of the pebbled elements, so corresponding pebbles determine corresponding gaps.

For an integer $s\geq0$, define
$$
T_s=2^s-1.
$$
With $s$ rounds remaining, call two corresponding gaps of sizes $d,e$ admissible when
$$
d=e
$$
or
$$
d,e\geq T_s.
$$

Step 2: Prove that admissible gaps let Duplicator survive
We show by induction on $s$ that if every corresponding gap is admissible with $s$ rounds remaining, then Duplicator can survive those $s$ rounds.

For $s=0$ there is nothing to play. Suppose $s\geq1$, and let
$$
T=T_{s-1}=2^{s-1}-1.
$$
Then
$$
T_s=2T+1.
$$

If Spoiler repeats a previously chosen element, Duplicator repeats the corresponding element. Otherwise Spoiler chooses a new element inside a gap of size $d$.

If the corresponding gap has the same size $e=d$, Duplicator chooses the element in the same relative position. The two new pairs of gaps then have equal sizes.

Now assume
$$
d,e\geq2T+1.
$$
Suppose Spoiler's chosen element splits the first gap into subgaps of sizes $a,b$, so
$$
a+b=d-1.
$$
If $a<T$, Duplicator chooses the response so that the corresponding left subgap also has size $a$. Then
$$
b=d-1-a
\geq
2T-(T-1)
=
T+1,
$$
and the other new subgap in the response order also has size at least $T+1$. The case $b<T$ is symmetric.

If both $a$ and $b$ are at least $T$, Duplicator chooses a point in the corresponding gap that leaves at least $T$ elements on each side. This is possible because
$$
e-1\geq2T.
$$

Thus every new corresponding gap pair is admissible for $s-1$ remaining rounds. The induction proves Duplicator's strategy.

Step 3: Prove the converse interval strategy for Spoiler
Suppose a corresponding pair of gaps has unequal sizes
$$
d<e
$$
and
$$
d<T_s.
$$
We show by induction on $s$ that Spoiler can force a win in at most $s$ rounds by playing inside these gaps.

For $s=1$, we have
$$
T_1=1.
$$
Thus $d=0<e$. Spoiler chooses any element in the larger gap. There is no element in the smaller corresponding gap, so Duplicator cannot preserve the order relation to the two endpoints.

Now let $s\geq2$, and put
$$
T=T_{s-1}.
$$
If
$$
d<T,
$$
the induction hypothesis with $s-1$ already applies.

It remains to treat
$$
T\leq d<e
$$
with
$$
d<T_s=2T+1.
$$
Spoiler chooses an element in the larger gap leaving exactly $T$ elements on its left. The two subgaps there have sizes
$$
T
\qquad\text{and}\qquad
e-1-T.
$$

Duplicator must answer inside the smaller corresponding gap to preserve order. Write the resulting subgap sizes as
$$
a+b=d-1.
$$
Since
$$
d-1<2T,
$$
at least one of $a,b$ is less than $T$.

If $a<T$, then the left new gap pair has sizes $a$ and $T$, so it is unequal with one size below $T=T_{s-1}$. The induction hypothesis applies.

If instead $b<T$, suppose the right new gap pair were admissible for $s-1$ rounds. Because $b<T$, admissibility would force
$$
b=e-1-T.
$$
The left response subgap must then satisfy
$$
a\geq T,
$$
and therefore
$$
d-1=a+b
\geq
T+(e-1-T)
=
e-1,
$$
which contradicts $d<e$. Hence in this case too, one of the new gap pairs is unequal with one size below $T$, and the induction hypothesis applies.

Therefore Spoiler wins within $s$ rounds whenever a corresponding gap pair violates the admissibility criterion.

Step 4: Apply the two interval strategies to the two orders
Let
$$
A_m=\{1,\ldots,2^m\},
\qquad
B_m=\{1,\ldots,2^m+1\},
$$
with their usual linear orders.

Before any move, the virtual endpoints determine one gap in each structure, of sizes
$$
2^m
\qquad\text{and}\qquad
2^m+1.
$$

For an $m$-round game,
$$
T_m=2^m-1.
$$
Both initial gaps have size at least $T_m$, so Step 2 gives Duplicator a winning strategy for all $m$ rounds.

For an $(m+1)$-round game,
$$
T_{m+1}=2^{m+1}-1.
$$
The two initial gap sizes are unequal, and
$$
2^m<T_{m+1}.
$$
Step 3 gives Spoiler a winning strategy in at most $m+1$ rounds.

Thus Duplicator wins the $m$-round game but Spoiler wins the $(m+1)$-round game. The least winning length is
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
- finite linear orders
- partial isomorphisms
- interval splitting
- inductive game strategies
