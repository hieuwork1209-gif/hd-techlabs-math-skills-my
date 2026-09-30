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

Step 2: Build a sharp polynomial majorant for the all-equal event
For integers $s\in\{0,1,\ldots,10\}$ define
$$
Q(s)
=
\frac{(s-3)(s-4)(s-6)(s-7)}{504}.
$$
The factorization shows
$$
Q(s)\geq0
$$
for every integer $1\leq s\leq9$, while
$$
Q(0)=Q(10)=1.
$$
Hence
$$
\mathbf 1_{\{0,10\}}(s)\leq Q(s)
$$
on the whole support of $S$.

To evaluate its expectation without any numerical search, expand the numerator in falling factorials:
$$
(s-3)(s-4)(s-6)(s-7)
=
504-324(s)_1+92(s)_2-14(s)_3+(s)_4.
$$
The moment identities from Step 1 give
$$
\mathbb E(S)_1=5,
$$
$$
\mathbb E(S)_2=\frac{45}{2},
$$
$$
\mathbb E(S)_3=90,
$$
and
$$
\mathbb E(S)_4=315.
$$
Therefore
$$
\mathbb E Q(S)
=
\frac{
504-324\cdot5
+92\cdot\frac{45}{2}
-14\cdot90
+315
}{504}
=
\frac{1}{56}.
$$
It follows that
$$
\mathbb P(S\in\{0,10\})
\leq
\frac{1}{56}.
$$

Equality can hold only when
$$
Q(S)=\mathbf 1_{\{0,10\}}(S)
$$
almost surely. The strict positivity of $Q$ at $1,2,5,8,9$ therefore forces every extremizer to satisfy
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
\mathbb ET
=
\mathbb ET^3
=
\mathbb ET^5
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
hence
$$
u=v=w=0.
$$
Thus every extremizer is symmetric under $S\mapsto10-S$.

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
For $T=S-5$, the independent fair-binomial moments are
$$
\mathbb ET^2=\frac52
$$
and
$$
\mathbb ET^4=\frac{35}{2}.
$$
The second identity follows by writing
$$
T=\sum_{i=1}^{10}\left(X_i-\frac12\right)
$$
for fully independent fair Bernoulli variables: the fourth moment is
$$
10\cdot\frac1{16}
+
6\binom{10}{2}\frac1{16}
=
\frac{35}{2}.
$$
Since our variables are 5-wise independent, these degree-$2$ and degree-$4$ moments are the same.

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
Therefore
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
and, conditional on $S=s$, choosing uniformly among the $\binom{10}{s}$ binary vectors with $s$ ones. The displayed masses satisfy the factorial-moment identities of Step 1 through degree $5$, so this law is 5-wise independent. It attains
$$
\mathbb P(S\in\{0,10\})
=
\frac1{56}.
$$
The equality-support and moment arguments above show that no other exchangeable law can attain the same value. Hence the unique extremal distribution of $S$ is the requested vector.
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
