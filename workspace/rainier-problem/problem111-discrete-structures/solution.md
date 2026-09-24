## Steps

Step 1: Convert cyclic words into Euler tours
Let the alphabet be $\{0,1,2\}$. For a cyclic word
$$
x_0x_1\cdots x_{N-1},
\qquad
N=9m+3,
$$
write $N_{ab}$ for the number of indices $i$ modulo $N$ such that
$$
(x_i,x_{i+1})=(a,b).
$$
The prescribed transition matrix is
$$
(N_{ab})_{a,b\in\{0,1,2\}}
=
\begin{pmatrix}
m&m+1&m\\
m&m&m+1\\
m+1&m&m
\end{pmatrix}.
$$
Every row sum and every column sum is
$$
d=3m+1.
$$

Build a directed multigraph $G$ on vertices $0,1,2$ having exactly $N_{ab}$ directed edges from $a$ to $b$. Reading a cyclic word around the circle gives an Euler tour of $G$, except that parallel edges have not yet been distinguished.

Conversely, an Euler tour of $G$ produces a cyclic word by recording its visited vertices. The desired rotation classes can therefore be counted by first labeling all parallel edges, counting labeled Euler tours, and then removing the edge labels and the choice of starting position.

Step 2: Prove the labeled Euler-tour count by a last-exit bijection
Fix vertex $0$ as the starting vertex, and suppose all parallel edges of $G$ are distinctly labeled.

For a labeled Euler tour starting at $0$, mark, for each vertex $v\neq0$, the last outgoing edge used from $v$. Following marked edges from any nonzero vertex must eventually reach $0$. Indeed, if marked edges formed a directed cycle avoiding $0$, take the first vertex of that cycle whose marked edge is used in the tour; after leaving that vertex along its marked edge, the tour could never later leave the preceding vertex of the cycle, contradicting the order in which the marked edges are supposed to be last exits. The two marked edges therefore form a directed spanning tree oriented toward $0$.

Conversely, fix such an oriented spanning tree. At each nonzero vertex, place its marked tree edge last in a linear order of the outgoing edges. At vertex $0$, choose an arbitrary linear order of all outgoing edges. Starting at $0$, repeatedly take the next unused outgoing edge in the chosen local order.

The walk cannot terminate at a nonzero vertex. If it did so at $v$, all $d$ outgoing edges of $v$ would already have been used, while reaching $v$ for the final time would make the number of used incoming edges equal to the number of used outgoing edges plus $1$, impossible because $v$ has only $d$ incoming edges.

Suppose instead that the walk returns to $0$ and stops while some edge remains unused. Choose a vertex $u$ with an unused outgoing edge. Its marked tree edge is last in its local order, so that marked edge is unused. Let its head be $u_1$. If $u_1\neq0$ and the marked edge out of $u_1$ had already been used, then all $d$ outgoing edges of $u_1$ would have been used, while the unused edge entering $u_1$ would leave fewer than $d$ used incoming edges. This contradicts equality of used indegree and used outdegree at a nonroot vertex of a closed walk. The marked edge out of $u_1$ is also unused. Repeating along the tree path reaches an unused edge entering $0$. But a closed walk at $0$ uses the same number of incoming and outgoing edges, so $0$ would then also have an unused outgoing edge, contradicting termination. Therefore every edge is used exactly once. The local orders are recovered uniquely from the tour.

If $t_0$ denotes the number of directed spanning trees oriented toward $0$, the number of labeled Euler tours starting at $0$ is therefore
$$
t_0\,d!\,(d-1)!^2
=
t_0\,d\,(d-1)!^3.
$$

Step 3: Count the last-exit trees
Loops cannot occur in a tree oriented toward $0$. Vertices $1$ and $2$ each choose one outgoing nonloop edge, and their choices must eventually reach $0$.

There are three allowed patterns.

If
$$
1\to0,
\qquad
2\to0,
$$
there are
$$
m(m+1)
$$
choices of labeled edges.

If
$$
1\to0,
\qquad
2\to1,
$$
there are
$$
m^2
$$
choices.

If
$$
1\to2,
\qquad
2\to0,
$$
there are
$$
(m+1)^2
$$
choices.

The remaining pattern $1\to2$, $2\to1$ is a directed cycle and is not a tree. Therefore
$$
t_0
=
m(m+1)+m^2+(m+1)^2
=
3m^2+3m+1.
$$

Step 4: Remove edge labels and the starting position
For a fixed cyclic word with a distinguished starting position at a symbol $0$, the occurrences of each transition $a\to b$ can be assigned the labels of the corresponding parallel edges in
$$
N_{ab}!
$$
ways, independently for the nine ordered pairs. Each rooted word corresponds to
$$
\prod_{a,b}N_{ab}!
=
(m!)^6((m+1)!)^3
$$
labeled Euler tours.

The number of rooted words whose distinguished position contains $0$ is therefore
$$
\frac{t_0\,d\,(d-1)!^3}
{(m!)^6((m+1)!)^3}.
$$

Every admissible cyclic word is primitive. If it were the $s$-fold repetition of a shorter cyclic word with $s>1$, every transition count $N_{ab}$ would be divisible by $s$. Since both $m$ and $m+1$ occur among the transition counts,
$$
s\mid\gcd(m,m+1)=1,
$$
a contradiction.

A primitive rotation class has exactly $d=3m+1$ rotations whose distinguished symbol is $0$, because every word has exactly $d$ occurrences of $0$. Dividing the rooted count by $d$ gives
$$
\frac{t_0\,(d-1)!^3}
{(m!)^6((m+1)!)^3}.
$$

Step 5: Simplify the final expression
Substituting
$$
t_0=3m^2+3m+1
$$
and
$$
d-1=3m
$$
gives
$$
\frac{(3m^2+3m+1)(3m)!^3}
{(m!)^6((m+1)!)^3}.
$$
Final Answer: $\boxed{\frac{(3m^2+3m+1)(3m)!^3}{(m!)^6((m+1)!)^3}}$

---

## Answer

$\frac{(3m^2+3m+1)(3m)!^3}{(m!)^6((m+1)!)^3}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cyclic words
- euler tours
- last-exit trees
- directed multigraphs
- orbit counting
