## Steps

Step 1: Count all admissible colorings

Write a black vertex as $1$ and a white vertex as $0$. Put $n=2m$, so $m=2^{r-1}$. For a coloring $x=(x_0,\ldots,x_{n-1})$, its admissibility parity is
$$
Q(x)=\sum_{i\in\mathbb Z/n\mathbb Z}x_ix_{i+1}+\sum_{i=0}^{m-1}x_ix_{i+m}\pmod 2.
$$
Let
$$
S=\sum_{x\in\{0,1\}^n}(-1)^{Q(x)}.
$$
Then the number $N$ of admissible colorings is $(2^n-S)/2$.

Set $a_i=x_i$ and $b_i=x_{i+m}$. Then
$$
Q=\sum_{i=0}^{m-2}(a_ia_{i+1}+b_ib_{i+1})+a_{m-1}b_0+b_{m-1}a_0+\sum_{i=0}^{m-1}a_ib_i.
$$
Now put $u_i=a_i+b_i$ in $\mathbb F_2$. Substituting $b_i=a_i+u_i$ and collecting the terms containing each $a_i$ gives
$$
Q=\sum_{i=0}^{m-1}a_i(1+u_{i-1}+u_i+u_{i+1})+\sum_{i=0}^{m-2}u_iu_{i+1},
$$
where the subscripts in the first sum are modulo $m$. Summing first over the $a_i$ gives zero unless
$$
u_{i-1}+u_i+u_{i+1}=1
$$
for every $i$, in which case it gives $2^m$. This recurrence implies $u_{i+3}=u_i$. Since $m$ is a power of $2$, $\gcd(m,3)=1$, so a cyclic solution of length $m$ must be constant. The equation then forces $u_i=1$ for every $i$. For this solution the second sum is $m-1$, which is odd. Hence
$$
S=-2^m,
\qquad
N=2^{n-1}+2^{m-1}.\tag{1}
$$

Step 2: Reduce the stabilizer count to involutions

Let $c$ be rotation by one vertex and let $h=c^m$ be the half-turn. Because $n$ is a power of $2$, every nontrivial subgroup of $\langle c\rangle$ contains $h$. Thus a coloring has nontrivial rotational stabilizer exactly when it is fixed by $h$.

Outside $\operatorname{Fix}(h)$, a coloring cannot be fixed by two distinct reflections, since the product of two distinct reflections is a nontrivial rotation. Therefore the number of admissible colorings with trivial dihedral stabilizer is obtained by removing the $h$-fixed colorings and then, for each reflection, removing its fixed colorings that are not already $h$-fixed.

Step 3: Count half-turn fixed colorings

If $h$ fixes a coloring, write $x_{i+m}=x_i=t_i$. The side contributions occur twice and cancel modulo $2$, while the diameter contribution is
$$
Q=\sum_{i=0}^{m-1}t_i.
$$
Exactly half of the $2^m$ choices have odd sum, so
$$
A:=|\operatorname{Fix}(h)\cap X|=2^{m-1},\tag{2}
$$
where $X$ denotes the admissible colorings.

Step 4: Count the two reflection classes and their intersections with the half-turn

There are $m$ reflections through opposite vertices and $m$ reflections through opposite sides. In a reflection-fixed coloring, every pair of sides or diameters interchanged by the reflection contributes twice and cancels modulo $2$.

Write a reflection as $i\mapsto k-i$. A diameter $\{i,i+m\}$ is fixed as a set exactly when $2i\equiv k\pmod m$. Thus a vertex-axis reflection, for which $k$ is even, fixes two diameters as sets and no side as a set. On the diameter lying along the axis, let the two endpoint colors be $a,b$; on the other fixed diameter the endpoints are interchanged and have a common color $t$. Hence
$$
Q=ab+t.
$$
A vertex-axis reflection has $m+1$ vertex orbits. For each $a,b$, exactly one value of $t$ makes $Q=1$, so
$$
V:=|\operatorname{Fix}(\rho_v)\cap X|=2^m.\tag{3}
$$
If the coloring is also $h$-fixed, it is described by $m$ diameter colors. The induced reflection on these $m$ colors has two fixed coordinates, and their sum is $Q$. Thus
$$
V_h:=|\operatorname{Fix}(h,\rho_v)\cap X|=2^{m/2}.\tag{4}
$$

For a side-axis reflection, $k$ is odd. The congruence $2i\equiv k\pmod m$ has no solution, so no diameter is fixed as a set, while exactly two sides are fixed as sets. If the two fixed side colors are $a,b$, then
$$
Q=a+b.
$$
The reflection has $m$ vertex orbits, so
$$
E:=|\operatorname{Fix}(\rho_e)\cap X|=2^{m-1}.\tag{5}
$$
Under the additional half-turn condition, the induced reflection on the $m$ diameter colors has no fixed coordinate. Their sum is therefore even, so
$$
E_h:=|\operatorname{Fix}(h,\rho_e)\cap X|=0.\tag{6}
$$

Step 5: Assemble the free orbits

Using (1) through (6), the number of admissible colorings with trivial stabilizer is
$$
\begin{aligned}
F
&=N-A-m(V-V_h)-m(E-E_h)\\
&=2^{n-1}-m\left(3\cdot2^{m-1}-2^{m/2}\right).
\end{aligned}
$$
Every such orbit has $2n$ elements. Substituting $m=n/2$ and dividing by $2n$ gives
$$
\frac{2^{n-1}-\frac n2\left(3\cdot2^{n/2-1}-2^{n/4}\right)}{2n}.
$$
For the smallest case $n=8$, the formula gives $3$; the fixed-point counts are $N=136$, $A=8$, $V=16$, $V_h=4$, $E=8$, and $E_h=0$, leaving $48$ free colorings and hence $48/16=3$ orbits.

Final Answer: $\boxed{\frac{2^{n-1}-\frac n2(3\cdot2^{n/2-1}-2^{n/4})}{2n}}$

---

## Answer

$\frac{2^{n-1}-\frac n2(3\cdot2^{n/2-1}-2^{n/4})}{2n}$

## Classification

| Field | Value |
|---|---|
| Domain | Discrete Mathematics and Combinatorics |
| Sub-domain | Basic counting principles |
| Problem Type | Exact computation |
| Answer Type | Exact symbolic expression |

## Solution Concepts

- quadratic character sums
- recurrence over finite fields
- dihedral stabilizers
- reflection fixed points
- orbit-stabilizer counting
