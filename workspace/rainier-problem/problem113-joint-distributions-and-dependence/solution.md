## Steps

Step 1: Reduce 5-wise independence to moment constraints for the exchangeable sum
Let
$$
S=X_1+\cdots+X_{10}.
$$
Because the vector is exchangeable, conditional on $S=s$ every $0$-$1$ vector with exactly $s$ ones has the same probability.

For $0\leq j\leq5$, write
$$
(S)_j=S(S-1)\cdots(S-j+1),
$$
with $(S)_0=1$. Counting ordered $j$-tuples of distinct indices whose coordinates are all equal to $1$ gives
$$
\mathbb E[(S)_j]
=
(10)_j
\mathbb P(X_1=\cdots=X_j=1).
$$
Under 5-wise independence and $\mathbb P(X_i=1)=1/2$,
$$
\mathbb E[(S)_j]
=
\frac{(10)_j}{2^j}
\qquad
(0\leq j\leq5).
$$
It follows that every polynomial in $S$ of degree at most $5$ has the same expectation as it would for
$$
B\sim\operatorname{Bin}(10,1/2).
$$

Conversely, for an exchangeable $0$-$1$ vector, these factorial-moment identities through degree $5$ imply 5-wise independence. They give the correct probability $2^{-j}$ that any chosen $j$ coordinates are all $1$, and inclusion-exclusion gives probability $2^{-j}$ for every prescribed $0$-$1$ pattern on those coordinates.

Step 2: Build a degree-five certificate for the one-sided endpoint event
Set
$$
T=S-5.
$$
Then $T$ is integer-valued with
$$
-5\leq T\leq5.
$$
The objective $S=0$ is the one-sided endpoint $T=-5$. The even quartic
$$
R(T)=(T^2-1)(T^2-4)
$$
is nonnegative at every allowed integer value because
$$
T^2\in\{0,1,4,9,16,25\}.
$$
To distinguish $T=-5$ from the opposite endpoint $T=5$ while staying within the available degree-$5$ moments, multiply by the nonnegative linear factor $5-T$. This gives
$$
Q(T)
=
\frac{(5-T)(T^2-1)(T^2-4)}{5040}.
$$
For every integer $-5\leq T\leq5$,
$$
Q(T)\geq0,
$$
while
$$
Q(-5)=1.
$$
Therefore
$$
\mathbf 1_{\{T=-5\}}\leq Q(T)
$$
pointwise.

By Step 1, the first five centered moments of $T$ agree with those of $B-5$. Symmetry of the fair binomial law gives
$$
\mathbb E[T]
=
\mathbb E[T^3]
=
\mathbb E[T^5]
=
0.
$$
Also,
$$
\mathbb E[T^2]=\frac52.
$$
For the fourth moment, write
$$
B-5=\sum_{i=1}^{10}Y_i,
\qquad
Y_i\in\left\{-\frac12,\frac12\right\},
$$
with the $Y_i$ independent and centered. Expanding the fourth power, only the terms $Y_i^4$ and $Y_i^2Y_j^2$ have nonzero expectation, so
$$
\mathbb E[T^4]
=
10\cdot\frac1{16}
+
6\binom{10}{2}\frac1{16}
=
\frac{35}{2}.
$$
Thus
$$
\begin{aligned}
\mathbb P(S=0)
&=
\mathbb P(T=-5)\\
&\leq
\mathbb E[Q(T)]\\
&=
\frac{
5\left(\mathbb E[T^4]-5\mathbb E[T^2]+4\right)
-
\left(\mathbb E[T^5]-5\mathbb E[T^3]+4\mathbb E[T]\right)
}{5040}\\
&=
\frac{45}{5040}
=
\frac1{112}.
\end{aligned}
$$

Equality requires $Q(T)=0$ whenever $T\neq-5$ has positive probability. On the allowed lattice, the zeros of $Q$ are
$$
T\in\{-2,-1,1,2,5\}.
$$
Hence every maximizing law must satisfy
$$
S\in\{0,3,4,6,7,10\}
$$
almost surely.

Step 3: Use the odd moments to determine the endpoint balance
For a maximizing law, the only possible values of $T$ are
$$
-5,-2,-1,1,2,5.
$$
Write
$$
u=\mathbb P(T=5)-\mathbb P(T=-5),
$$
$$
v=\mathbb P(T=2)-\mathbb P(T=-2),
$$
and
$$
w=\mathbb P(T=1)-\mathbb P(T=-1).
$$
The equations
$$
\mathbb E[T]
=
\mathbb E[T^3]
=
\mathbb E[T^5]
=
0
$$
become
$$
5u+2v+w=0,
$$
$$
125u+8v+w=0,
$$
and
$$
3125u+32v+w=0.
$$
Subtracting the first equation from the second gives
$$
120u+6v=0,
$$
so
$$
v=-20u.
$$
Subtracting the second equation from the third gives
$$
3000u+24v=0.
$$
Substituting $v=-20u$ gives
$$
2520u=0.
$$
Therefore
$$
u=v=w=0,
$$
so every maximizing law is symmetric under $S\mapsto10-S$.

Set
$$
a=\mathbb P(S=0)=\mathbb P(S=10),
$$
$$
b=\mathbb P(S=3)=\mathbb P(S=7),
$$
and
$$
c=\mathbb P(S=4)=\mathbb P(S=6).
$$

Step 4: Recover the unique maximizing distribution and verify attainability
Normalization gives
$$
a+b+c=\frac12.
$$
The second and fourth centered moments from Step 2 give
$$
25a+4b+c=\frac54
$$
and
$$
625a+16b+c=\frac{35}{4}.
$$
Subtracting the normalization equation from the second-moment equation gives
$$
8a+b=\frac14.
$$
Subtracting the second-moment equation from the fourth-moment equation gives
$$
50a+b=\frac58.
$$
Solving gives
$$
a=\frac1{112},
\qquad
b=\frac5{28},
\qquad
c=\frac5{16}.
$$

Define an exchangeable law by assigning
$$
\mathbb P(S=s)
=
\begin{cases}
\frac1{112},&s\in\{0,10\},\\
\frac5{28},&s\in\{3,7\},\\
\frac5{16},&s\in\{4,6\},\\
0,&\text{otherwise},
\end{cases}
$$
and, conditional on $S=s$, choosing uniformly among the $\binom{10}{s}$ binary vectors with $s$ ones. Symmetry gives centered moments of orders $1,3,5$ equal to $0$, while the equations above give the same centered moments of orders $2$ and $4$ as the fair binomial law. Together with normalization, its ordinary moments through degree $5$ match those of $\operatorname{Bin}(10,1/2)$, so its falling-factorial moments do as well. Step 1 then implies that the law is 5-wise independent.

It has
$$
\mathbb P(S=0)=\frac1{112},
$$
so the bound from Step 2 is attained. The equality-support and moment arguments force the same masses for every maximizing law, making the maximizing distribution unique.
Final Answer: $\boxed{\left(\frac1{112},0,0,\frac5{28},\frac5{16},0,\frac5{16},\frac5{28},0,0,\frac1{112}\right)}$

---

## Answer

$\left(\frac1{112},0,0,\frac5{28},\frac5{16},0,\frac5{16},\frac5{28},0,0,\frac1{112}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Vector

---

## Solution Concepts

- exchangeable Bernoulli variables
- limited independence
- factorial moments
- polynomial dual certificate
- moment reconstruction
