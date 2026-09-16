## Steps

Step 1: Reduce contractible model structures to right-bracketing functions
Let $[n]=\{0<1<\cdots<n\}$. In a contractible model structure every morphism is a weak equivalence, so acyclic fibrations are exactly fibrations and acyclic cofibrations are exactly cofibrations. Hence such a model structure is exactly one weak factorization system $(\mathcal L,\mathcal R)$, with $\mathcal R$ the fibrations.

For each $i$, define
$$
r_i=\max\{j:i\to j\in\mathcal R\}.
$$
The identity gives $r_i\geq i$. Pullback closure shows that $i\to j\in\mathcal R$ exactly when $i\leq j\leq r_i$, and composition forces
$$
i<j\leq r_i\quad\Longrightarrow\quad r_j\leq r_i.
$$
Conversely, any tuple $(r_0,\ldots,r_n)$ with $i\leq r_i\leq n$ satisfying this implication defines a right class by $i\to j\in\mathcal R$ iff $j\leq r_i$. Let $\mathcal L={}^\perp\mathcal R$. Then $a\to b\in\mathcal L$ exactly when $r_x<b$ for every $a\leq x<b$. For any $a\leq b$, choose the least $c\in[a,b]$ with $r_c\geq b$. Minimality and the bracketing condition give $r_x<c$ for $a\leq x<c$, so
$$
a\to c\in\mathcal L,\qquad c\to b\in\mathcal R.
$$
Thus every arrow factors, and the retract argument gives $\mathcal R=\mathcal L^\perp$. These tuples classify the contractible model structures.

Step 2: Translate the categorical statistics into an ordered forest
Put $N=n+1$. Under the matching construction, a right-bracketing tuple is equivalent to a Dyck path of semilength $N$: the up-step $U_i$ is matched with the down-step closing the interval whose last up-step is $U_{r_i}$. Equivalently, the Dyck path is an ordered forest with $N$ vertices, one vertex for each up-step.

The fibrant objects are exactly the $i$ with $r_i=n$, hence their number is the final descent length $r$. The cofibrant objects are exactly the starts of primitive Dyck components, hence their number is the number $s$ of rooted trees in the ordered forest.

For a vertex $i$, the interval from $U_i$ to its matching down-step contains exactly the vertices in the rooted subtree of $i$. Therefore
$$
r_i-i+1=|\operatorname{subtree}(i)|.
$$
The total number of fibrations, including identities, is
$$
\nu(\mathcal M)=\sum_{i=0}^n(r_i-i+1).
$$
Summing subtree sizes counts each vertex once for itself and once for every proper ancestor, so
$$
\nu(\mathcal M)=N+\sum_v\operatorname{depth}(v).
$$
Thus the problem is an extremal total-depth problem for ordered forests with $N$ vertices, $s$ components, and final descent length $r$.

Step 3: Bound the depth contribution of the components
The final descent length $r$ means that the rightmost leaf of the last rooted tree has depth $r-1$. Its rightmost root-to-leaf spine has $r$ vertices and contributes
$$
0+1+\cdots+(r-1)=\binom{r}{2}
$$
to the depth sum.

If $r=1$, the last component is a single vertex. Assume $r\geq2$ and let $q$ be the number of other vertices in the last component. Remove the rightmost spine. Every remaining vertex lies in a subtree attached to one of the first $r-1$ spine vertices, so after its attachment edge it receives an offset at most $r-1$. A forest on $q$ vertices has internal depth sum at most $\binom{q}{2}$: ordering its vertices so parents precede children, the $k$th vertex has depth at most $k-1$. Equality requires one chain. Hence the last component contributes at most
$$
\binom{r}{2}+q(r-1)+\binom{q}{2}.
$$
For $q>0$, equality forces the $q$ extra vertices to form one chain attached as an earlier child of the penultimate vertex on the rightmost spine.

For the first $s-1$ components, write their sizes as $1+x_1,\ldots,1+x_{s-1}$ with $x_j\geq0$. The same parent-before-child argument shows that the $j$th component has depth sum at most
$$
\binom{x_j+1}{2},
$$
with equality only for a chain.

Since
$$
t=n+2-r-s=N+1-r-s,
$$
the vertices left after reserving one root for each earlier component and the $r$ vertices of the final spine satisfy
$$
x_1+\cdots+x_{s-1}+q=t.
$$

Step 4: Optimize the slack distribution and classify equality
For $r\geq2$, the variable part of the depth sum is bounded by
$$
\sum_{j=1}^{s-1}\binom{x_j+1}{2}+q(r-1)+\binom{q}{2},
\qquad
x_1+\cdots+x_{s-1}+q=t.
$$
If two earlier buckets have positive sizes $x,y$, merging them changes their contribution by
$$
\binom{x+y+1}{2}-\binom{x+1}{2}-\binom{y+1}{2}=xy>0.
$$
Thus at most one earlier bucket is positive at a maximum. If that bucket has size $t-q$, the variable contribution becomes
$$
\binom{t-q+1}{2}+q(r-1)+\binom{q}{2},
$$
a strictly convex quadratic in $q$. Its maximum on $0\leq q\leq t$ is therefore at an endpoint. The endpoint $q=0$ gives $\binom{t+1}{2}$, while $q=t$ gives
$$
t(r-1)+\binom{t}{2}=\binom{t+1}{2}+t(r-2).
$$
For $r=1$ the last bucket is unavailable, so only the first endpoint occurs. Therefore the maximal depth sum is
$$
\binom{r}{2}+\binom{t+1}{2}+t(r-2)_+,
$$
where $x_+=\max\{x,0\}$. By Step 2,
$$
A_{n;r,s}=n+1+\binom{r}{2}+\binom{t+1}{2}+t(r-2)_+.
$$

If $t=0$, the forest is forced, so there is one maximizer. Suppose $t>0$. If $r=1$, all slack forms a chain in exactly one of the first $s-1$ components, giving $s-1$ maximizers. If $r=2$, the two endpoints tie, so either one of the first $s-1$ components carries the chain or the last component carries the unique extremal extra chain, giving $s$ maximizers. If $r\geq3$, the last endpoint is strictly larger, so the maximizing forest is unique. Consequently
$$
K_{n;r,s}=1+[t>0]\bigl((s-2)[r=1]+(s-1)[r=2]\bigr).
$$

Step 5: State the extremal categorical profile
The Dyck-path and ordered-forest constructions are bijections, so every equality shape counted in Step 4 corresponds to exactly one contractible model structure and no other structure attains the same number of fibrations. Therefore the required pair is the maximum total number of fibrations together with the number of model structures attaining it.

Final Answer: $\boxed{\left(n+1+\binom{r}{2}+\binom{t+1}{2}+t(r-2)_+,1+[t>0]((s-2)[r=1]+(s-1)[r=2])\right)}$

---

## Answer

$\left(n+1+\binom{r}{2}+\binom{t+1}{2}+t(r-2)_+,1+[t>0]((s-2)[r=1]+(s-1)[r=2])\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- Quillen model structures on finite posets
- weak factorization systems
- right-bracketing functions
- Dyck paths and ordered forests
- extremal depth in rooted forests
