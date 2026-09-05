## Steps

Step 1: Realize the graph as a chamber graph

Let $\mathcal A$ be the hyperplane arrangement in $\mathbb R^n$ consisting of
$$
H_i=\{x_i=0\}\qquad(1\le i\le n)
$$
and
$$
H_{ij}^{\pm}=\{x_i=\pm x_j\}\qquad(1\le i<j\le n).
$$
There are
$$
n+2\binom n2=n^2
$$
hyperplanes.

For a signed permutation $w=(w_1,\ldots,w_n)$, write $x_{-j}=-x_j$ and define
$$
C_w=\{x\in\mathbb R^n:0<x_{w_1}<x_{w_2}<\cdots<x_{w_n}\}.
$$
These are exactly the chambers of $\mathcal A$. Swapping two adjacent entries of $w$ crosses one wall of the form $x_i=\pm x_j$, while changing the sign of $w_1$ crosses one wall $x_i=0$. Hence the graph in the problem is exactly the chamber-adjacency graph of $\mathcal A$.

For each $H\in\mathcal A$, let $\varepsilon_H(w)\in\{0,1\}$ record which side of $H$ contains $C_w$. Any graph path from $u$ to $v$ must cross every hyperplane that separates $C_u$ from $C_v$, so
$$
d(u,v)\ge\sum_{H\in\mathcal A}|\varepsilon_H(u)-\varepsilon_H(v)|.
$$
Conversely, choose interior points of $C_u$ and $C_v$ so that the segment joining them meets no two hyperplanes simultaneously. A linear defining form for $H$ changes sign along the segment exactly when $H$ separates the two chambers, and then it vanishes exactly once. The successive chambers crossed by the segment therefore give a path of exactly that length. Thus
$$
d(u,v)=\sum_{H\in\mathcal A}|\varepsilon_H(u)-\varepsilon_H(v)|.
$$
So the metric is a Hamming metric on the $n^2$ chamber-side coordinates.

Step 2: Prove $1$-negative type

Let $(c_w)$ satisfy $\sum_wc_w=0$. For one binary coordinate $\varepsilon_H$,
$$
|\varepsilon_H(u)-\varepsilon_H(v)|
=\varepsilon_H(u)+\varepsilon_H(v)-2\varepsilon_H(u)\varepsilon_H(v).
$$
Summing against $c_uc_v$, the first two terms vanish. Therefore
$$
\sum_{u,v}c_uc_vd(u,v)
=-2\sum_{H\in\mathcal A}\left(\sum_wc_w\varepsilon_H(w)\right)^2\le0.
$$
Hence the metric has $1$-negative type. Equality holds exactly when
$$
\sum_wc_w\varepsilon_H(w)=0
$$
for every $H\in\mathcal A$.

Step 3: Show that every exponent $p>1$ fails

Because $n\ge3$, consider
$$
e=(1,2,3,4,\ldots,n),
$$
$$
a=(-1,2,3,4,\ldots,n),
\qquad
b=(1,3,2,4,\ldots,n),
$$
$$
ab=(-1,3,2,4,\ldots,n).
$$
Changing the sign of the first entry and swapping the second and third entries commute, so these four vertices form an isometric square: four edges have length $1$ and the two diagonals have length $2$.

Assign coefficients $1,-1,-1,1$ to $e,a,b,ab$. Their sum is $0$, and the powered quadratic form is
$$
4\cdot2^p-8>0
$$
for every $p>1$. Thus no exponent larger than $1$ has negative type. Since Step 2 gives $1$-negative type,
$$
\wp=1.
$$

Step 4: Compute the equality-space dimension

At $p=1$, the equality space is the kernel of the linear map
$$
c\longmapsto
\left(\sum_wc_w,\left(\sum_wc_w\varepsilon_H(w)\right)_{H\in\mathcal A}\right).
$$
It remains to compute its rank.

The constant function together with the $n^2$ side-indicator functions $\varepsilon_H$ are linearly independent. Indeed, suppose
$$
a_0+\sum_{H\in\mathcal A}a_H\varepsilon_H(w)=0
$$
for every chamber $C_w$. Fix $H\in\mathcal A$ and choose a point of $H$ lying on no other hyperplane of $\mathcal A$. Two sufficiently close points on opposite sides of $H$ lie in adjacent chambers that differ only in the coordinate $\varepsilon_H$. Subtracting the two corresponding equations gives $a_H=0$. Doing this for every $H$ leaves $a_0=0$.

Thus the map has rank
$$
1+n^2.
$$
There are $2^n n!$ signed permutations, so
$$
\dim E=2^n n!-n^2-1.
$$

Final Answer: $\boxed{(1,2^n n!-n^2-1)}$

---

## Answer

$(1,2^n n!-n^2-1)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- hyperoctahedral group
- type B hyperplane arrangement
- chamber graphs and Hamming embeddings
- negative type of finite metric spaces
- commuting simple reflections
