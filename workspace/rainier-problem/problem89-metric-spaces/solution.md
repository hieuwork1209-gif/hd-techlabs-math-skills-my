## Steps

Step 1: Record the metric structure of the Petersen graph

Let the Petersen graph have vertices
$$
P=\{u_i,v_i:i\in\mathbb{Z}/5\mathbb{Z}\},
$$
with edges
$$
u_i u_{i+1},\qquad u_i v_i,\qquad v_i v_{i+2}.
$$
Both the outer $u$-vertices and the inner $v$-vertices form $5$-cycles, the latter in the order of step $2$ modulo $5$.

Its shortest-path metric $d_P$ has diameter $2$. For two outer vertices this is immediate from the outer $5$-cycle, and similarly for two inner vertices. For $u_i$ and $v_j$, either $j=i$, or $j=i\pm1$ and
$$
u_i-u_j-v_j
$$
has length $2$, or $j=i\pm2$ and
$$
u_i-v_i-v_j
$$
has length $2$. Hence, for distinct Petersen vertices,
$$
d_P(x,y)=
\begin{cases}
1,&x\sim y,\\
2,&x\not\sim y.
\end{cases}
$$

The Petersen graph has girth $5$. A triangle or $4$-cycle lying in one layer is impossible because each layer is a $5$-cycle. A cycle using spokes crosses between the two layers an even number of times. A triangle with two spokes would require the same pair of indices to differ by both $1$ and $2$ modulo $5$. A $4$-cycle with two spokes gives the same contradiction, while four consecutive spoke crossings are impossible because a spoke has no second endpoint in the opposite layer. Thus there are no cycles of length $3$ or $4$, while the outer $5$-cycle exists.

Step 2: Show that every bijection has forward Lipschitz constant two

Let $C=\mathbb{Z}/10\mathbb{Z}$ with cycle metric
$$
d_C(i,j)=\min\{|i-j|,10-|i-j|\}.
$$
For a bijection $f:C\to P$,
$$
\operatorname{Lip}(f)=
\max_{i\neq j}\frac{d_P(f(i),f(j))}{d_C(i,j)}
\leq2.
$$

The Petersen graph is not Hamiltonian. Suppose a Hamiltonian cycle used $s$ spokes. Since a cycle crosses the cut between the outer and inner layers an even positive number of times,
$$
s\in\{2,4\}.
$$
If $s=2$, at spoke indices $a,b$, the outer part and the inner part of the Hamiltonian cycle would each be spanning paths on their respective $5$-cycles. The endpoints of a spanning path in the outer cycle differ by $\pm1$ modulo $5$, while in the inner cycle they differ by $\pm2$, a contradiction.

If $s=4$, let $a$ be the unique omitted spoke index. The outer edges are forced to be
$$
u_{a-1}u_a,\qquad u_au_{a+1},\qquad u_{a+2}u_{a-2},
$$
and the inner edges are forced to be
$$
v_{a-2}v_a,\qquad v_av_{a+2},\qquad v_{a-1}v_{a+1}.
$$
Together with the four used spokes these edges form two disjoint $5$-cycles, not one Hamiltonian cycle. Thus no Hamiltonian cycle exists.

Therefore some consecutive pair of $C$ is sent to nonadjacent Petersen vertices, and for that pair the ratio is $2$. Hence
$$
\operatorname{Lip}(f)=2
$$
for every bijection $f$.

Step 3: Reduce the inverse Lipschitz constant to a circular bandwidth

For a bijection $f:C\to P$, define
$$
M(f)=\max\{d_C(i,j):f(i)\sim f(j)\}.
$$
For a Petersen edge the inverse ratio is exactly $d_C(i,j)$, while for a nonedge it is
$$
\frac{d_C(i,j)}{2}\leq\frac{5}{2}.
$$
Once $M(f)\geq3$, it follows that
$$
\operatorname{Lip}(f^{-1})=M(f).
$$
Thus the distortion becomes
$$
\operatorname{dist}(f)
=\operatorname{Lip}(f)\operatorname{Lip}(f^{-1})
=2M(f).
$$

It remains to prove that every cyclic ordering of the Petersen vertices has some Petersen edge at cyclic distance at least $3$.

Step 4: Prove the circular bandwidth lower bound

Assume for contradiction that $M(f)\leq2$. Pull the Petersen edges back to the ten cycle positions. The resulting graph $G$ is a copy of the Petersen graph contained in the square $C_{10}^{2}$, whose edges join positions at cyclic distance $1$ or $2$.

The graph $C_{10}^{2}$ is $4$-regular, whereas $G$ is $3$-regular. Therefore
$$
F=E(C_{10}^{2})\setminus E(G)
$$
is a perfect matching.

The ten triangles of $C_{10}^{2}$ are exactly
$$
T_i=\{i,i+1,i+2\},
\qquad i\in\mathbb{Z}/10\mathbb{Z}.
$$
Since the Petersen graph is triangle-free, every $T_i$ contains an edge of $F$. An edge of cyclic length $1$ belongs to two of these triangles, while an edge of cyclic length $2$ belongs to only one. The five edges of the matching $F$ must cover all ten triangles, so every edge of $F$ has cyclic length $1$. Hence $F$ is one of the two alternating perfect matchings of the $10$-cycle.

After rotating indices, take
$$
F=\{01,23,45,67,89\}.
$$
Then the four edges
$$
02,\qquad21,\qquad19,\qquad90
$$
all belong to $G$, producing the $4$-cycle
$$
0-2-1-9-0.
$$
This contradicts the girth-$5$ property from Step 1. Therefore
$$
M(f)\geq3
$$
for every bijection.

Step 5: Construct a bijection with circular bandwidth three

Place the Petersen vertices around $C_{10}$ in the cyclic order
$$
u_0,u_1,u_2,u_4,u_3,v_2,v_4,v_3,v_0,v_1.
$$
The five outer edges have cyclic spans
$$
1,1,2,1,3.
$$
The five spokes have spans
$$
2,2,3,3,3.
$$
The five inner edges $v_i v_{i+2}$ have spans
$$
3,2,1,1,3.
$$
Thus every Petersen edge has cyclic span at most $3$, and some have span exactly $3$. Hence this bijection satisfies
$$
M(f)=3.
$$

Step 6: Evaluate the optimal distortion

Step 4 gives $M(f)\geq3$ for every bijection, so Steps 2 and 3 give
$$
\operatorname{dist}(f)\geq2\cdot3=6.
$$
The cyclic ordering in Step 5 has $M(f)=3$, hence
$$
\operatorname{Lip}(f)=2,
\qquad
\operatorname{Lip}(f^{-1})=3,
$$
and its distortion is $6$. Therefore the minimum possible distortion is $6$.

Final Answer: $\boxed{6}$

---

## Answer

$6$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- bi-Lipschitz distortion
- graph metrics
- circular bandwidth
- Petersen graph
- cycle graph squares
