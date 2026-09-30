## Steps

Step 1: Establish a directed-distance halving lemma
For vertices $x,y$ in a directed cycle, let
$$
\delta(x,y)
$$
be the length of the unique directed path from $x$ to $y$. For vertices in different connected components, set
$$
\delta(x,y)=\infty.
$$

Suppose two already matched ordered pebble pairs have directed distances
$$
d\neq e
$$
and
$$
\min(d,e)\leq2^s.
$$
Then Spoiler can force a win in at most $s$ further rounds.

Use induction on $s$. For $s=0$, the smaller distance is $0$ or $1$. Distance $0$ detects equality, while distance $1$ detects the successor relation, so the current correspondence already fails to be a partial isomorphism.

Now let $s\geq1$, and suppose without loss of generality that
$$
d<e,
\qquad
d\leq2^s.
$$
Spoiler plays a midpoint vertex on the directed path of length $d$. The two directed subpaths have lengths at most
$$
2^{s-1}.
$$
If Duplicator matched both subpath lengths exactly, concatenating the two corresponding directed paths in the other structure would give a directed walk of length $d$ from the first endpoint to the second. Hence its directed distance would be at most $d$, contradicting $e>d$. Therefore one of the two new ordered pebble pairs has unequal directed distances and smaller value at most $2^{s-1}$. The induction hypothesis applies.

Step 2: Maintain a truncated-distance invariant for Duplicator
Let
$$
A=D_{2^{m+1}},
\qquad
B=D_{2^m}\sqcup D_{2^m},
$$
where $D_n$ is a directed cycle with its successor orientation.

Duplicator will survive $m$ rounds. On the first round, Duplicator answers an arbitrary chosen vertex by an arbitrary vertex of the other structure. There are then $m-1$ rounds left.

With $s$ rounds remaining, Duplicator maintains the following invariant for every ordered pair of matched pebbles:
$$
\delta_A(x_i,x_j)=\delta_B(y_i,y_j)<2^{s+1},
$$
or else both directed distances are at least $2^{s+1}$, where $\infty$ is larger than every finite number.

Assume the invariant holds with $s\geq1$ rounds remaining and Spoiler chooses a new vertex $x$. Let $\mathcal N$ be the set of old pebbles $x_i$ for which
$$
\delta_A(x_i,x)<2^s
$$
or
$$
\delta_A(x,x_i)<2^s.
$$

Suppose first that $\mathcal N$ is nonempty. Choose an anchor $x_i\in\mathcal N$. The position of $x$ relative to $x_i$ is determined uniquely by one of the two directed distances, which is less than $2^s$. Duplicator places $y$ at the same directed offset from the corresponding anchor $y_i$.

For any other pebble $x_j\in\mathcal N$, the vertices $x_i,x_j,x$ lie on an oriented arc of length less than $2^{s+1}$. The current invariant fixes the directed offset from $x_i$ to $x_j$, so the same offset calculation shows that both directed distances between $x$ and $x_j$ are matched exactly whenever they are below $2^s$.

Now take an old pebble $x_j\notin\mathcal N$. If either directed distance between $y$ and $y_j$ were less than $2^s$, then $y_i,y_j,y$ would lie on an oriented arc of length less than $2^{s+1}$. The current invariant would force the same directed offsets in the first structure, putting $x_j$ in $\mathcal N$, a contradiction. Thus all new distances to pebbles outside $\mathcal N$ are at least $2^s$. The invariant holds with $s-1$ rounds remaining.

Suppose instead that $\mathcal N$ is empty. Duplicator chooses $y$ so that both directed distances between $y$ and every old response pebble are at least $2^s$. Such a vertex exists. At this stage at most
$$
m-s
$$
vertices have already been pebbled. For one old pebble, the forbidden vertices consist of itself, the next $2^s-1$ successors, and the previous $2^s-1$ predecessors, for at most
$$
2^{s+1}-1
$$
vertices. Thus the total number of forbidden vertices is at most
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
the total number of vertices in either structure. Hence an admissible $y$ exists, and all new ordered distances are at least $2^s$.

After the first response the invariant is vacuous except for one pebble pair, so Duplicator maintains it through all remaining rounds. When no rounds remain, distances $0$ and $1$ have been preserved exactly, which is precisely preservation of equality and the successor relation. Therefore Duplicator wins the $m$-round game.

Step 3: Force a win in $m+1$ rounds
Set
$$
q=2^{m-1}.
$$
Spoiler first chooses a vertex $a_0$ of the long directed cycle $A$. After Duplicator responds with $b_0$, Spoiler chooses the vertex $a_1$ satisfying
$$
\delta_A(a_0,a_1)=q.
$$
Let Duplicator answer with $b_1$.

If $b_0,b_1$ lie in different components of $B$, then
$$
\delta_B(b_0,b_1)=\infty.
$$
The matched directed distances $q$ and $\infty$ are unequal, with
$$
q=2^{m-1}.
$$
There are $m-1$ rounds left, so Step 1 gives Spoiler a win.

Suppose $b_0,b_1$ lie in the same short directed cycle. Write
$$
d=\delta_B(b_0,b_1).
$$
If
$$
d\neq q,
$$
and $d<q$, then Step 1 applies directly to the ordered pair $(a_0,a_1)$ and its mate. If
$$
d>q,
$$
consider the reversed ordered pair. In the long cycle,
$$
\delta_A(a_1,a_0)=4q-q=3q,
$$
while in the short cycle,
$$
\delta_B(b_1,b_0)=2q-d<q.
$$
Step 1 applies to this reversed pair.

The only remaining case is
$$
d=q.
$$
Then
$$
\delta_B(b_1,b_0)=q,
$$
whereas
$$
\delta_A(a_1,a_0)=3q.
$$
Again Step 1 applies to the reversed ordered pair, with smaller distance
$$
q=2^{m-1}.
$$
In every case Spoiler wins within the remaining $m-1$ rounds.

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
- directed graph distance
- truncated-distance invariants
- midpoint strategies
- disconnected structures
