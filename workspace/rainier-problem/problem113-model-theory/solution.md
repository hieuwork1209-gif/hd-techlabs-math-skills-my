## Steps

Step 1: Establish a distance-halving certificate for Spoiler
For vertices $x,y$ in a graph, let $d(x,y)$ be their graph distance, with
$$
d(x,y)=\infty
$$
when they lie in different connected components.

Suppose two already matched pebble pairs have distances
$$
d\neq e
$$
in the two structures and
$$
\min(d,e)\leq2^s.
$$
Then Spoiler can force a win in at most $s$ further rounds.

Use induction on $s$. For $s=0$, the smaller distance is $0$ or $1$. If it is $0$, equality is already violated; if it is $1$, adjacency is already violated.

Now let $s\geq1$. Suppose without loss of generality that
$$
d<e,
\qquad
d\leq2^s.
$$
Spoiler plays a midpoint vertex on a shortest path of length $d$ in the first graph. The two new distances from this midpoint to the endpoints are at most
$$
2^{s-1}.
$$
If Duplicator could match both of those distances exactly, the triangle inequality in the second graph would give
$$
e\leq d,
$$
a contradiction. Thus one of the two new matched pebble pairs has unequal distances and smaller distance at most $2^{s-1}$. The induction hypothesis applies.

Step 2: Build a locality strategy for Duplicator
Let
$$
A=C_{2^{m+1}},
\qquad
B=C_{2^m}\sqcup C_{2^m},
$$
where graph distance across the two components of $B$ is $\infty$.

Duplicator will survive $m$ rounds. On the first round, Duplicator answers an arbitrary chosen vertex by an arbitrary vertex of the other graph. There are then
$$
m-1
$$
rounds left.

We use the following invariant with $s$ rounds remaining. For every two matched pebbles, either their graph distances are equal and less than
$
2^{s+1},
$
or both distances are at least $2^{s+1}$, where $\infty$ counts as larger than every finite number. In addition, on every overlapping family of local path neighborhoods, choose orientations consistently so that matched pebbles at distance less than $2^{s+1}$ have the same signed path coordinate, up to one common reflection on that local cluster.

This local-coordinate clause makes sense because
$$
s\leq m-1
$$
throughout the remaining game, while every cycle in both structures has length at least
$$
2^m\geq2^{s+1}.
$$
Hence every open ball of radius $2^s$ is a path.

Assume the invariant holds with $s\geq1$ rounds remaining and Spoiler chooses a new vertex $x$. Let $\mathcal N$ be the set of old pebbles whose distance from $x$ is less than $2^s$.

If $\mathcal N$ is nonempty, all of its pebbles together with $x$ lie in one path segment of length less than $2^{s+1}$. Choose any pebble in $\mathcal N$ as an anchor. The current oriented local chart around that anchor identifies the corresponding old pebbles with the same signed coordinates. Duplicator chooses the vertex $y$ having the same signed coordinate as $x$. Then every distance from $x$ to a pebble in $\mathcal N$ is matched exactly.

For any old pebble outside $\mathcal N$, the corresponding pebble must stay at distance at least $2^s$ from $y$. Otherwise it and the anchor would both lie in the same oriented local chart as $y$. Their signed-coordinate differences would then force the original mate to lie within distance less than $2^s$ of $x$, contradicting the definition of $\mathcal N$. The restricted local charts for radius $2^s$ inherit the same orientations, so the invariant is preserved with $s-1$ rounds remaining.

If $\mathcal N$ is empty, Duplicator chooses a vertex $y$ at distance at least $2^s$ from every old response pebble. Such a vertex always exists. At this stage at most
$$
m-s
$$
vertices have already been pebbled in either graph. A ball of radius $2^s-1$ in a cycle contains at most
$$
2^{s+1}-1
$$
vertices, so the total number of forbidden vertices is at most
$$
(m-s)(2^{s+1}-1).
$$
Put
$$
k=m-s\geq1.
$$
Since
$$
k\leq2^{k-1},
$$
we have
$$
k(2^{m-k+1}-1)
<
2^{m+1},
$$
which is the total number of vertices in each structure. Therefore some admissible $y$ exists. All new distances are then at least $2^s$, so the invariant again holds for $s-1$ rounds.

After the first response the invariant is vacuous except for one pebble pair, so the induction applies through all remaining $m-1$ rounds. Duplicator wins the $m$-round game.

Step 3: Force a win in $m+1$ rounds
Set
$$
q=2^{m-1}.
$$
Spoiler first plays a vertex $a_0$ of the long cycle $A$. After Duplicator responds with $b_0$, Spoiler chooses a vertex $a_1$ satisfying
$$
d_A(a_0,a_1)=q.
$$
Let Duplicator answer with $b_1$.

If
$$
d_B(b_0,b_1)\neq q,
$$
then the two matched distances are unequal and their smaller value is at most
$$
q=2^{m-1}.
$$
There are $m-1$ rounds left, so Step 1 gives Spoiler a win.

The only remaining case is
$$
d_B(b_0,b_1)=q.
$$
Then $b_0,b_1$ lie in the same short cycle and are antipodal.

In the long cycle $A$, the two vertices $a_0,a_1$ cut the cycle into arcs of lengths
$$
q
\qquad\text{and}\qquad
3q.
$$
Spoiler now chooses $a_2$ on the longer arc at distance
$$
\frac{q}{2}=2^{m-2}
$$
from $a_0$. Therefore
$$
d_A(a_2,a_0)=\frac{q}{2},
\qquad
d_A(a_2,a_1)=\frac{3q}{2}.
$$
Let Duplicator respond with $b_2$.

If $b_2$ lies in the other component of $B$, then
$$
d_B(b_2,b_0)=\infty,
$$
while
$$
d_A(a_2,a_0)=2^{m-2}.
$$
Step 1 gives a win in the remaining $m-2$ rounds.

Suppose instead that $b_2$ lies in the same short cycle as $b_0,b_1$. If
$$
d_B(b_2,b_0)\neq\frac{q}{2},
$$
Step 1 again applies to the pair $(a_2,a_0)$ and its mate. If
$$
d_B(b_2,b_0)=\frac{q}{2},
$$
then antipodality of $b_0,b_1$ forces
$$
d_B(b_2,b_1)=\frac{q}{2}.
$$
But
$$
d_A(a_2,a_1)=\frac{3q}{2},
$$
so Step 1 applies to the pair $(a_2,a_1)$ and its mate, again with smaller distance
$$
\frac{q}{2}=2^{m-2}.
$$
Thus Spoiler wins within the remaining $m-2$ rounds.

Step 4: Identify the exact threshold
Step 2 gives Duplicator a winning strategy for $m$ rounds. Step 3 gives Spoiler a winning strategy for $m+1$ rounds. Therefore the least winning length is
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
- graph distance
- locality invariants
- midpoint strategies
- disconnected graph components
