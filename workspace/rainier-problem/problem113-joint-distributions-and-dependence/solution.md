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
Thus every polynomial in $S$ of degree at most $5$ has the same expectation as it would for
$$
B\sim\operatorname{Bin}(10,1/2).
$$

Conversely, for an exchangeable $0$-$1$ vector, these factorial-moment identities through degree $5$ imply 5-wise independence. They give the correct probability $2^{-j}$ that any chosen $j$ coordinates are all $1$, and inclusion-exclusion then gives probability $2^{-j}$ for every prescribed $0$-$1$ pattern on those coordinates.

Step 2: Derive a sharp lattice-polynomial bound for the all-equal event
Set
$$
T=S-5.
$$
Then $T$ is integer-valued with
$$
-5\leq T\leq5.
$$
Since only moments through degree $5$ are fixed, a degree-$4$ certificate is available. On the integer lattice, take the even quartic
$$
P(T)=(T^2-1)(T^2-4).
$$
For every integer $T$ in this range,
$$
P(T)\geq0,
$$
because $T^2$ is one of $0,1,4,9,16,25$. At the two all-equal outcomes,
$$
P(\pm5)=(25-1)(25-4)=504.
$$
Therefore the pointwise inequality
$$
\mathbf 1_{\{|T|=5\}}
\leq
\frac{(T^2-1)(T^2-4)}{504}
$$
holds for every possible value of $T$.

By Step 1, moments through degree $5$ agree with those of
$$
B\sim\operatorname{Bin}(10,1/2).
$$
Hence
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
Therefore
$$
\mathbb P(S\in\{0,10\})
=
\mathbb P(|T|=5)
\leq
\frac{\mathbb E[T^4]-5\mathbb E[T^2]+4}{504}
=
\frac1{56}.
$$

Equality in the expectation bound requires equality in the pointwise bound almost surely. Besides $T=\pm5$, equality occurs only at
$$
T=\pm1,\pm2.
$$
Therefore every extremizer satisfies
$$
S\in\{0,3,4,6,7,10\}
$$
almost surely.

Step 3: Use the fifth moment to force symmetry of the equality-support law
Let
$$
T=S-5.
$$
For an extremizer, the only possible values of $T$ are
$$
-5,-2,-1,1,2,5.
$$
Since the first five moments of $S$ match those of $B\sim\operatorname{Bin}(10,1/2)$, the first five centered moments of $T$ match those of $B-5$. The binomial law is symmetric about $5$, so
$$
\mathbb E[T]
=
\mathbb E[T^3]
=
\mathbb E[T^5]
=
0.
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
The three odd-moment equations are
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
Substitution yields
$$
2520u=0,
$$
so
$$
u=v=w=0.
$$
Therefore every extremizer is symmetric under $S\mapsto10-S$.

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

Step 4: Determine the unique extremal masses and verify attainability
Normalization gives
$$
a+b+c=\frac12.
$$
By Step 2,
$$
\mathbb E[T^2]=\frac52,
\qquad
\mathbb E[T^4]=\frac{35}{2}.
$$
Using the support values $|T|=5,2,1$ gives
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
Solving these two linear equations gives
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
and, conditional on $S=s$, choosing uniformly among the $\binom{10}{s}$ binary vectors with $s$ ones. For this law, symmetry gives centered moments of orders $1,3,5$ equal to $0$, while the equations above give the same centered moments of orders $2$ and $4$ as the fair binomial law. Together with normalization, its ordinary moments through degree $5$ match those of $\operatorname{Bin}(10,1/2)$, so its falling-factorial moments do as well. Step 1 then implies that this law is 5-wise independent. It attains
$$
\mathbb P(S\in\{0,10\})
=
\frac1{56}.
$$
The equality-support and moment arguments above show that no other exchangeable law can attain the same value. The extremal distribution of $S$ is therefore unique and equals the requested vector.
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
