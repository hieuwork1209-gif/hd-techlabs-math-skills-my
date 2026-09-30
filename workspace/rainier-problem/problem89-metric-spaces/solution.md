## Steps

Step 1: Reduce the negative-type form to the Kneser adjacency spectrum

Write the vertices of $X$ as the $2$-subsets of $[7]$. Distinct vertices are at distance $1$ when they are disjoint and at distance $2$ when they meet in one point, because any two intersecting $2$-subsets have a common disjoint $2$-subset.

Let $M$ be the adjacency matrix of $KG(7,2)$, let $J$ be the all-ones matrix, and put $q=2^p$. Then
$$
D_p=(d(A,B)^p)_{A,B\in X}=M+q(J-I-M).
$$
On the zero-sum subspace $J$ vanishes, so
$$
D_p=(1-q)M-qI.
$$

Step 2: Determine the critical exponent and the equality space

For $u=(u_1,\ldots,u_7)\in\mathbb R^7$, define
$$
(Tu)_{\{i,j\}}=u_i+u_j.
$$
The map $T$ is injective. If $s=\sum_i u_i$, then
$$
(MTu)_{\{i,j\}}
=\sum_{\{k,l\}\subset[7]\setminus\{i,j\}}(u_k+u_l)
=4(s-u_i-u_j).
$$
Hence the constant vector has adjacency eigenvalue $10$, while
$$
T\left(\left\{u:\sum_i u_i=0\right\}\right)
$$
is a $6$-dimensional eigenspace with eigenvalue $-4$.

Let
$$
W=\left\{c\in\mathbb R^X:\sum_{j\neq i}c_{\{i,j\}}=0\text{ for every }i\right\}.
$$
The seven row-sum equations have rank $7$ because their transpose is $T$, so $\dim W=14$. For $c\in W$,
$$
(Mc)_{\{i,j\}}
=\sum_{\{k,l\}\cap\{i,j\}=\varnothing}c_{\{k,l\}}
=c_{\{i,j\}},
$$
so the remaining adjacency eigenvalue is $1$ with multiplicity $14$.

Therefore the two eigenvalues of $D_p$ on the zero-sum subspace are
$$
-4+3q
\qquad\text{and}\qquad
1-2q.
$$
Since $q>1$, the second is always negative, while the first is nonpositive exactly for $q\leq4/3$. Thus
$$
\wp=\log_2\left(\frac43\right).
$$
At equality,
$$
E=T(V_0),\qquad
V_0=\left\{u\in\mathbb R^7:\sum_i u_i=0\right\},
$$
so $\dim E=6$.

Step 3: Translate missing support coordinates into a graph constraint

Let $U\leq V_0$ and $L=T(U)\leq E$. Since $T$ is injective, $\dim L=\dim U$. Define $G_U$ on $[7]$ by
$$
ij\in E(G_U)
\iff
u_i+u_j=0\quad\text{for every }u\in U.
$$
Then
$$
|\operatorname{supp}(L)|=21-e(G_U).
$$

For a graph $G$ on $[7]$, put
$$
W_G=\left\{u\in V_0:u_i+u_j=0\text{ for every }ij\in E(G)\right\}.
$$
On a connected bipartite component with bipartition $(P,Q)$, the edge equations force one parameter $t$, with value $t$ on $P$ and $-t$ on $Q$. On a connected non-bipartite component an odd cycle forces all coordinates to be zero.

Let $b$ be the number of bipartite connected components, counting isolated vertices, and for such a component let
$$
\delta_C=|P_C|-|Q_C|,
$$
with $\delta_C=1$ for an isolated vertex. The condition $\sum_i u_i=0$ becomes
$$
\sum_C\delta_C t_C=0.
$$
Hence
$$
\dim W_G=
\begin{cases}
b,&\delta_C=0\text{ for every bipartite component},\\
b-1,&\text{otherwise}.
\end{cases}
$$

Step 4: Obtain the sharp upper bound for the number of missing coordinates

Let $z$ be the total number of vertices in non-bipartite components and let the bipartite component sizes be $s_1,\ldots,s_b$, with total $B=7-z$. A non-bipartite part has at most $\binom z2$ edges, while a bipartite component of size $s$ has at most
$$
f(s)=\left\lfloor\frac{s^2}{4}\right\rfloor.
$$
Also
$$
f(a)+f(b)\leq f(a+b-1)\qquad(a,b\geq1),
$$
so
$$
\sum_{i=1}^b f(s_i)\leq f(B-b+1).
$$

If some $\delta_C\neq0$ and $\dim W_G\geq r$, then $b\geq r+1$, hence
$$
e(G)\leq \binom z2+f(7-z-r),
$$
where either $z=0$ or $z\geq3$, and $z\leq6-r$. The unbalanced maxima are explicit:
$
\begin{aligned}
r=1:&\ \max\left\{f(6),\binom{3}{2}+f(3),\binom{4}{2}+f(2),\binom{5}{2}+f(1)\right\}=10,\\
r=2:&\ \max\left\{f(5),\binom{3}{2}+f(2),\binom{4}{2}+f(1)\right\}=6,\\
r=3:&\ \max\left\{f(4),\binom{3}{2}+f(1)\right\}=4,
\end{aligned}
$
while $r=4,5,6$ give $f(3)=2$, $f(2)=1$, and $f(1)=0$.

If every bipartite component is balanced, then $\dim W_G=b$. Every such component has even size, so because there are seven vertices, a non-bipartite part of odd size at least $3$ is present. This case is possible only for $r\leq2$. For $r=1$, the best choice is a $5$-vertex non-bipartite part together with one balanced $2$-vertex component, giving
$$
\binom52+1=11.
$$
For $r=2$, at least two balanced components use four vertices, leaving at most three non-bipartite vertices, so the bound is at most
$$
\binom32+1+1=5.
$$
Therefore, if $t_r$ denotes the largest possible number of missing coordinates for an $r$-dimensional subspace,
$$
(t_1,t_2,t_3,t_4,t_5,t_6)=(11,6,4,2,1,0).
$$

Step 5: Determine every attainable support size, not only the minima

For $U\leq V_0$ with $\dim U=r$, let $v_i\in U^*$ be the coordinate functional $v_i(u)=u_i$. These seven functionals span $U^*$ and satisfy
$$
v_1+\cdots+v_7=0.
$$
Moreover,
$$
ij\in E(G_U)\iff v_i=-v_j.
$$
Conversely, any seven covectors in $\mathbb R^r$ that span $\mathbb R^r$ and sum to zero define an injective map into $V_0$, hence arise from some $U$. Thus the problem is exactly to count opposite pairs among a spanning zero-sum $7$-tuple.

For $r=5,4,3,2$, the values $0,\ldots,\min(3,6-r)$ are attained by taking that many disjoint opposite pairs and choosing the remaining covectors generically so that the whole tuple has sum zero, spans $\mathbb R^r$, and creates no further opposite pairs. The remaining extremal values are attained by the following tuples, where the displayed letters are independent:
$$
\begin{array}{c|c|c}
r&t& (v_1,\ldots,v_7)\\
\hline
3&4&(a,a,-a,-a,b,c,-b-c)\\
2&4&(a,a,-a,-a,b,b,-2b)\\
2&5&(0,0,0,a,-a,b,-b)\\
2&6&(0,0,0,0,a,b,-a-b).
\end{array}
$$
Together with Step 4, this proves that the attainable missing-coordinate counts are
$$
\{0,1\},\quad
\{0,1,2\},\quad
\{0,1,2,3,4\},\quad
\{0,1,2,3,4,5,6\},\quad
\{0\}
$$
for $r=5,4,3,2,6$, respectively.

It remains to handle $r=1$. Now the $v_i$ are scalars. Counts $0,1,\ldots,5$ are attainable as follows: for $1\leq k\leq5$, take $k$ copies of $1$, one copy of $-1$, and choose the remaining $6-k$ scalars so that the total sum is zero and no additional opposite pair appears; for $k\leq4$ the remaining affine solution space has positive dimension and finitely many forbidden hyperplanes cannot cover it, while for $k=5$ the last scalar is $-4$. Count $0$ is obtained by a generic zero-sum tuple with no opposite pair. The remaining values are witnessed by
$$
\begin{aligned}
6&:(1,1,1,-1,-1,2,-3),\\
7&:(-1,-1,0,0,0,1,1),\\
8&:(-2,-1,-1,1,1,1,1),\\
9&:(-1,-1,-1,0,1,1,1),\\
11&:(-1,0,0,0,0,0,1).
\end{aligned}
$$

Count $10$ is impossible. Let $z$ be the number of zero entries. If $1\leq z\leq4$, then the number of opposite pairs is at most
$$
\binom z2+\left\lfloor\frac{(7-z)^2}{4}\right\rfloor<10.
$$
If $z=5$, the two remaining scalars must be opposites, so the count is $\binom52+1=11$. Values $z\geq6$ cannot occur in a nonzero zero-sum spanning $1$-tuple. Finally, if $z=0$, partition the seven entries into classes $\{a,-a\}$. A class of size $m$ contributes at most $\lfloor m^2/4\rfloor$ opposite pairs. Any partition of $7$ into at least two classes gives at most $9$ in total, while a single class would consist entirely of $\pm a$ and could sum to zero only with equal multiplicities, impossible for seven entries. Hence the $r=1$ counts are exactly
$$
\{0,1,\ldots,9,11\}.
$$

Since support size is $21-t$, and $I(a)=\{a,a+1,\ldots,21\}$, we obtain
$$
\Sigma_1=\{10\}\cup I(12),\quad
\Sigma_2=I(15),\quad
\Sigma_3=I(17),\quad
\Sigma_4=I(19),\quad
\Sigma_5=I(20),\quad
\Sigma_6=\{21\}.
$$

Final Answer: $\boxed{\left(\log_2(4/3),6,\{10\}\cup I(12),I(15),I(17),I(19),I(20),\{21\}\right)}$

---

## Answer

$\left(\log_2(4/3),6,\{10\}\cup I(12),I(15),I(17),I(19),I(20),\{21\}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- negative type metrics
- Kneser graph spectrum
- support spectra
- signed graph constraints
- extremal graph decomposition
