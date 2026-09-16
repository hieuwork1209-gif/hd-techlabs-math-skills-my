## Steps

Step 1: Compute the fixed-object counts for each iterate
Let $X$ be a finite set and let $g:X\to X$. For the adjoint triple
$$
\exists_g\dashv g^{-1}\dashv\forall_g,
$$
put
$$
C_g=g^{-1}\exists_g,\qquad D_g=\forall_g g^{-1}.
$$
For $S\subseteq X$,
$$
C_g(S)=g^{-1}(g(S)),
$$
so $C_g(S)=S$ exactly when $S$ is a union of fibers of $g$. Hence
$$
|\operatorname{Fix}(C_g)|=2^{|g(X)|}.
$$
Also
$$
D_g(S)=S\cup(X\setminus g(X)).
$$
A set fixed by both $C_g$ and $D_g$ must be a union of fibers of $g$ and must contain $X\setminus g(X)$. Therefore every fiber meeting $X\setminus g(X)$ is forced, while every fiber contained in $g(X)$ is optional. Define
$$
u_g=\#\{y\in g(X):g^{-1}(y)\subseteq g(X)\}.
$$
Then
$$
|\operatorname{Fix}(C_g)\cap\operatorname{Fix}(D_g)|=2^{u_g}.
$$
We apply this to $g=f^k$.

Step 2: Derive the sharp lower bounds for the image sizes of the iterates
Let
$$
M=3d+2,\qquad Y_k=f^k(X),\qquad r_k=|Y_k|.
$$
The hypothesis gives
$$
r_1=2d+2.
$$
For every $k\ge1$, each point of $Y_k\setminus Y_{k+1}$ has no preimage in $Y_k$, but it does have a preimage in $X$ because it lies in $Y_k=f^k(X)$. Hence distinct points of $Y_k\setminus Y_{k+1}$ require distinct preimages in $X\setminus Y_k$, so
$$
r_k-r_{k+1}\le M-r_k.
$$
Equivalently,
$$
r_{k+1}\ge2r_k-M.
$$
Thus
$$
r_2\ge2(2d+2)-(3d+2)=d+2.
$$
Every endomap of a finite set has a periodic point, and the condition $f(x)\ne x$ excludes $1$-cycles, so every $Y_k$ contains at least two periodic points. Hence
$$
r_k\ge2\qquad(k\ge3).
$$
By Step 1,
$$
\sum_{k=1}^{M}|\operatorname{Fix}(C_k)|
=\sum_{k=1}^{M}2^{r_k}
\ge2^{2d+2}+2^{d+2}+(M-2)\cdot4.
$$
Therefore
$$
A_d\ge2^{2d+2}+2^{d+2}+12d.
$$

Step 3: Classify equality in the first optimization
Equality requires
$$
r_1=2d+2,\qquad r_2=d+2,\qquad r_k=2\quad(k\ge3).
$$
Put
$$
L_0=X\setminus Y_1,\qquad L_1=Y_1\setminus Y_2,\qquad L_2=Y_2\setminus Y_3,\qquad C=Y_3.
$$
Then
$$
|L_0|=|L_1|=|L_2|=d,\qquad |C|=2.
$$
Because $L_1$ has no preimages in $Y_1$ and $|L_0|=|L_1|$, equality in the drop bound forces
$$
f:L_0\to L_1
$$
to be a bijection. Similarly,
$$
f:L_1\to L_2
$$
is a bijection. Since $Y_4=f(Y_3)$ also has size $2$, the restriction $f|_C$ is a permutation of $C$. The global fixed-point-free hypothesis forces it to be the transposition. Finally every point of $L_2$ maps into $C$, with no further restriction.

Conversely, every map with this four-layer form has image sizes
$$
2d+2,\ d+2,\ 2,\ 2,\ldots,
$$
so it attains the lower bound. Hence
$$
A_d=2^{2d+2}+2^{d+2}+12d.
$$

Step 4: Optimize the simultaneous fixed-object count inside the equality class
Fix a first-stage minimizer. For $k=1$, the points of $L_1$ have fibers meeting $L_0$, so those $d$ fibers are forced. The fibers over $L_2$ and over the two points of $C$ lie entirely inside $Y_1$. Thus
$$
u_f=d+2
$$
and
$$
|\operatorname{Fix}(C_1)\cap\operatorname{Fix}(D_1)|=2^{d+2}.
$$

For $k=2$, every fiber over $L_2$ contains a point of $L_0$, so those fibers are forced. A point $c\in C$ has an $f^2$-preimage in $L_1$ exactly when $c\in f(L_2)$. Therefore
$$
u_{f^2}=2-|f(L_2)|.
$$
Since $L_2\ne\varnothing$, this is at most $1$, with equality exactly when $f$ is constant on $L_2$. Hence
$$
|\operatorname{Fix}(C_2)\cap\operatorname{Fix}(D_2)|\le2,
$$
with equality exactly in that constant case.

For every $k\ge3$, we have $Y_k=C$. Pick $x\in L_2$ and let $y\in L_1$ be its unique preimage. Then
$$
f^k(y)=f^{k-1}(x),
$$
and once the orbit has entered the $2$-cycle, these two values are the two distinct points of $C$. Thus both $f^k$-fibers over $C$ contain transient points outside $Y_k$, so
$$
u_{f^k}=0
$$
and the simultaneous fixed-object count is $1$.

Therefore, among the first-stage minimizers,
$$
B_d=2^{d+2}+2+(M-2)=2^{d+2}+3d+2,
$$
and equality holds exactly when all points of $L_2$ have the same image in $C$.

Step 5: Count all maps attaining both extrema
Choose the $2$-cycle $C$ in
$$
\binom{M}{2}
$$
ways. Partition the remaining $3d$ points into the ordered layers $L_2,L_1,L_0$, each of size $d$, in
$$
\frac{(3d)!}{(d!)^3}
$$
ways. Choose the bijections
$$
L_0\to L_1,\qquad L_1\to L_2
$$
in $(d!)^2$ ways, and choose the common target in $C$ of all points of $L_2$ in $2$ ways. The transposition on $C$ is then forced.

Hence
$$
K_d=\binom{3d+2}{2}\frac{(3d)!}{(d!)^3}(d!)^2\cdot2
=\frac{(3d+2)!}{d!}.
$$

Final Answer: $\boxed{\left(2^{2d+2}+2^{d+2}+12d,\;2^{d+2}+3d+2,\;\frac{(3d+2)!}{d!}\right)}$

---

## Answer

$\left(2^{2d+2}+2^{d+2}+12d,\;2^{d+2}+3d+2,\;\frac{(3d+2)!}{d!}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- adjoint triples on Boolean lattices
- closure monads from iterated maps
- fixed objects of monads
- functional graph image layers
- extremal image-rank profiles
