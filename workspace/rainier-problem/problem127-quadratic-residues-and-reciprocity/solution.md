## Steps

Step 1: Derive the global parity obstruction from quadratic reciprocity
Assume that distinct primes $p_1,\ldots,p_n$, all congruent to $3$ modulo $4$, satisfy the required condition. For $i\ne j$, write
$$
\varepsilon_{ij}=\left(\frac{p_i}{p_j}\right)\in\{-1,1\}.
$$
The condition at $p_j$ is
$$
\prod_{i\ne j}\varepsilon_{ij}=1.
$$
Because $p_i\equiv p_j\equiv3\pmod4$, quadratic reciprocity gives
$$
\varepsilon_{ij}\varepsilon_{ji}
=\left(\frac{p_i}{p_j}\right)\left(\frac{p_j}{p_i}\right)
=-1.
$$
Multiplying the $n$ residue conditions and grouping the factors by unordered pairs yields
$$
1
=\prod_{j=1}^n\prod_{i\ne j}\varepsilon_{ij}
=\prod_{1\le i<j\le n}\varepsilon_{ij}\varepsilon_{ji}
=(-1)^{\binom n2}.
$$
Hence $\binom n2$ is even. Checking $n$ modulo $4$ gives the necessary condition
$$
n\equiv0\text{ or }1\pmod4.
$$

Step 2: Build an abstract Legendre-symbol pattern when the parity obstruction vanishes
Suppose now that $n\equiv0$ or $1\pmod4$. We first construct signs $\varepsilon_{ij}\in\{-1,1\}$ such that
$$
\varepsilon_{ji}=-\varepsilon_{ij}
$$
for every $i\ne j$ and
$$
\prod_{i\ne j}\varepsilon_{ij}=1
$$
for every $j$.

Interpret the signs as a tournament: orient the edge from $i$ to $j$ exactly when $\varepsilon_{ij}=-1$. Then the product in the $j$th column is $(-1)^{d_j}$, where $d_j$ is the indegree of vertex $j$. Thus it is enough to construct a tournament in which every indegree is even.

If $n=4k+1$, use the cyclic tournament on $\mathbb Z/n\mathbb Z$ in which $i$ points to $j$ when
$$
j-i\pmod n\in\{1,2,\ldots,2k\}.
$$
Every vertex has indegree $2k$, which is even.

If $n=4k$, first take the cyclic regular tournament on $4k-1$ vertices. Every old vertex then has indegree
$$
\frac{4k-2}{2}=2k-1.
$$
Add one new vertex and orient every new edge from the new vertex toward an old vertex. Each old indegree becomes $2k$, while the new vertex has indegree $0$. Again all indegrees are even.

Therefore the required abstract sign pattern exists for every $n\equiv0$ or $1\pmod4$.

Step 3: Realize the sign pattern by actual primes
We now construct distinct primes $p_1,\ldots,p_n\equiv3\pmod4$ satisfying
$$
\left(\frac{p_i}{p_j}\right)=\varepsilon_{ij}
$$
for every $i\ne j$.

Choose any prime $p_1\equiv3\pmod4$. Suppose $p_1,\ldots,p_{j-1}$ have already been chosen. For each $i<j$, choose a nonzero residue $r_i$ modulo $p_i$ such that
$$
\left(\frac{r_i}{p_i}\right)=-\varepsilon_{ij}.
$$
Both Legendre-symbol values occur among the nonzero residue classes modulo an odd prime, so such an $r_i$ exists.

By the Chinese remainder theorem there is a residue class $r$ modulo
$$
M=4p_1p_2\cdots p_{j-1}
$$
satisfying
$$
r\equiv3\pmod4,
\qquad
r\equiv r_i\pmod{p_i}
$$
for every $i<j$. This class is coprime to $M$. Dirichlet's theorem on primes in arithmetic progressions states that if $\gcd(r,M)=1$, then the progression $r+M\mathbb Z$ contains infinitely many primes. Choose a prime $p_j$ in this progression larger than all previously chosen primes.

Then $p_j\equiv3\pmod4$, and for each $i<j$,
$$
\left(\frac{p_j}{p_i}\right)
=\left(\frac{r_i}{p_i}\right)
=-\varepsilon_{ij}.
$$
Since both primes are $3$ modulo $4$, quadratic reciprocity gives
$$
\left(\frac{p_i}{p_j}\right)
=-\left(\frac{p_j}{p_i}\right)
=\varepsilon_{ij}.
$$
Induction realizes the entire sign pattern by distinct primes.

Step 4: Verify sufficiency and conclude the classification
For every $j$, multiplicativity of the Legendre symbol gives
$$
\left(\frac{\prod_{i\ne j}p_i}{p_j}\right)
=\prod_{i\ne j}\left(\frac{p_i}{p_j}\right)
=\prod_{i\ne j}\varepsilon_{ij}
=1.
$$
Thus the complementary product is a quadratic residue modulo every $p_j$. Step 1 showed that no other congruence classes of $n$ are possible, while Steps 2 and 3 construct suitable primes whenever $n\equiv0$ or $1\pmod4$.

Final Answer: $\boxed{n\equiv0\text{ or }1\pmod4}$

---

## Answer

$n\equiv0\text{ or }1\pmod4$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Equation or inequality

---

## Solution Concepts

- quadratic reciprocity
- Legendre symbol multiplicativity
- tournament indegree parity
- Chinese remainder theorem
- primes in arithmetic progressions
