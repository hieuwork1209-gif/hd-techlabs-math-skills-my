## Steps

Step 1: Classify the maximum families
Let $\mathcal F\subseteq\binom{[4q+2]}{3}$ satisfy $|A\cap B|\neq1$ for distinct $A,B\in\mathcal F$. Join two members when they intersect in two elements. Distinct connected components have disjoint supports.

Take adjacent triples
$$
A=\{1,2,3\},
\qquad
B=\{1,2,4\}.
$$
Every triple in their connected component meets both $A$ and $B$ in two elements: otherwise a shortest overlap-two path to a triple disjoint from one of them gives a last edge whose two-element overlap is impossible. A triple meeting both $A$ and $B$ in two elements either contains the pair $\{1,2\}$ or is one of
$$
\{1,3,4\},
\qquad
\{2,3,4\}.
$$
If one of these latter triples occurs, compatibility forces the whole component to lie inside $\{1,2,3,4\}$. Hence each component is either a fixed-pair family or a subfamily of the four triples on one $4$-set.

For a component $\mathcal C$, let
$$
\Delta(\mathcal C)
=
|\operatorname{supp}(\mathcal C)|-|\mathcal C|.
$$
A full $4$-set component has deficit $0$, a $3$-triple subfamily on a $4$-set has deficit $1$, and every fixed-pair component or singleton has deficit $2$.

If $u$ ground elements are unused, then
$$
(4q+2)-|\mathcal F|
=
u+\sum_{\mathcal C}\Delta(\mathcal C).
$$
The right side cannot be $0$ or $1$, because all support sizes would then be multiples of $4$ while $4q+2-u$ is not divisible by $4$ for $u=0,1$. Thus
$$
|\mathcal F|\leq4q.
$$

Equality has exactly two forms.

- Type $0$: $q$ disjoint $4$-sets, each contributing all four triples, and two unused points.
- Type $j$ for $1\leq j\leq q$: one fixed-pair component on $4j+2$ points, containing all $4j$ triples through its center pair, together with $q-j$ full $4$-set components.

The deficit distribution and the congruence modulo $4$ exclude every other equality case.

Step 2: Bound the overlap when one family has type 0
Let $\mathcal F$ be type $0$, with full $4$-set blocks
$$
B_1,\ldots,B_q
$$
and two unused points.

For another maximum family $\mathcal G$, consider one block $B_i$. If all four triples on $B_i$ lie in $\mathcal G$, then they form a full $4$-set component of $\mathcal G$ on the same support. If the block is not common, then at most two of its four triples can lie in $\mathcal G$: three common triples would form a $3$-triple component on $B_i$, which cannot occur in a maximum family.

If $c$ of the $q$ blocks are common to both families, then
$$
|\mathcal F\cap\mathcal G|
\leq
4c+2(q-c).
$$
For distinct families $c\leq q-1$, so
$$
|\mathcal F\cap\mathcal G|
\leq4q-2.
$$

Equality requires $c=q-1$ and exactly two common triples from the remaining block $B$. The common $q-1$ blocks use $4q-4$ points, leaving six points. On those six points, $\mathcal F$ consists of the four triples on $B$ plus two unused points.

A second type-$0$ family on these six points can share at most one of the four triples on $B$, because two distinct $4$-sets have at most one common $3$-subset. Hence equality forces $\mathcal G$ to be type $1$ on these six points. Its center pair $P$ must lie inside $B$, and then the two common triples are
$$
P\cup\{x\},
\qquad
x\in B\setminus P.
$$
Thus every equality pair with a type-$0$ member is obtained by replacing one full $4$-set block together with the two unused points by a six-point star centered at a pair inside that block.

Step 3: Rule out overlap $4q-2$ between two positive types
Let $\mathcal F$ have type $j\geq1$, with star center $P$, star support $S$, and $q-j$ full $4$-set blocks. Suppose
$$
|\mathcal F\cap\mathcal G|\geq4q-2.
$$
Then at most two triples of $\mathcal F$ are missing from $\mathcal G$.

Any full block of $\mathcal F$ that is not also a full block of $\mathcal G$ loses at least two triples from the intersection by the argument of Step 2. Therefore all but at most one full block of $\mathcal F$ are common blocks.

If $j\geq2$, the star of $\mathcal F$ contains $4j\geq8$ triples, so at least $4j-2\geq6$ of them lie in $\mathcal G$. Three triples through the same pair $P$ cannot lie in a full $4$-set component, which contains at most two triples through any fixed pair. Hence they lie in the star component of $\mathcal G$, whose center must also be $P$.

Let $a$ leaves of the star of $\mathcal F$ be omitted by the star of $\mathcal G$, and let $b$ new leaves be added. Since star sizes are multiples of $4$,
$$
b-a\equiv0\pmod4.
$$
If $a>0$, the star already loses at least one common triple, and every source block supplying a new leaf is no longer a common full block and loses at least two more triples. This gives total loss at least $3$.

If $a=0$ and $b>0$, then $b\geq4$. At least one full block is absorbed into the new star, and all four triples of that block disappear from the intersection. This gives total loss at least $4$. Thus the only way to lose at most two triples is $a=b=0$, which makes the star component identical. The same block argument then forces every full block to be identical, so $\mathcal F=\mathcal G$.

It remains to consider $j=1$. If at least three of the four star triples are common, the same-center argument above applies and again forces equality of the families when the total loss is at most two. If exactly two star triples are common, then losing only two triples overall forces all $q-1$ full blocks of $\mathcal F$ to be common blocks of $\mathcal G$. The six remaining ground points contain the star of $\mathcal F$. A different maximum family on those six points sharing exactly two of these star triples must be type $0$, by the six-point analysis in Step 2. Hence a pair with overlap $4q-2$ always consists of one type-$0$ family and one type-$1$ family.

Therefore, for distinct maximum families,
$$
|\mathcal F\cap\mathcal G|\leq4q-2,
$$
and equality is characterized exactly by the local replacement described in Step 2.

Step 4: Count the equality pairs
The number of type-$0$ families is
$$
N_0
=
\binom{4q+2}{2}
\frac{(4q)!}{(4!)^q q!}
=
\frac{(4q+2)!}{2\cdot24^q q!}.
$$

Fix one type-$0$ family. To obtain a distinct maximum family with overlap $4q-2$, choose one of its $q$ full $4$-set blocks and then choose the center pair of the replacing six-point star inside that block. There are
$$
q\binom42=6q
$$
choices.

Each resulting unordered pair is counted once, because exactly one member has type $0$ and the other has type $1$. Hence the number of unordered equality pairs is
$$
N_0\cdot6q
=
\frac{(4q+2)!}{8\cdot24^{q-1}(q-1)!}.
$$

Step 5: State the requested ordered tuple
The largest intersection size between two distinct maximum families is $4q-2$, and the number of unordered pairs attaining it is the count from Step 4.
Final Answer: $\boxed{\left(4q-2,\frac{(4q+2)!}{8\cdot24^{q-1}(q-1)!}\right)}$

---

## Answer

$\left(4q-2,\frac{(4q+2)!}{8\cdot24^{q-1}(q-1)!}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- extremal set systems
- component decomposition
- equality case classification
- overlap extremization
- labeled set partitions
