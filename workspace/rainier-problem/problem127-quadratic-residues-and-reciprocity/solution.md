## Steps

Step 1: Convert the residue conditions into a tournament score condition
Let $m,n\ge2$. Suppose distinct primes
$$
p_1,\ldots,p_n\equiv3\pmod4
$$
have the required property. For $i\ne j$, orient the edge between $i$ and $j$ from $i$ to $j$ exactly when
$$
\left(\frac{p_i}{p_j}\right)=-1.
$$
Because both primes are congruent to $3$ modulo $4$, quadratic reciprocity gives
$$
\left(\frac{p_i}{p_j}\right)
\left(\frac{p_j}{p_i}\right)=-1.
$$
Hence exactly one of the two Legendre symbols is $-1$, so this indeed defines a tournament.

For a vertex $j$, its indegree is exactly the number of indices $i\ne j$ for which $p_i$ is a quadratic nonresidue modulo $p_j$. Therefore the prime problem is equivalent to asking whether there is a tournament on $n$ vertices all of whose indegrees are divisible by $m$, together with a realization of that tournament by primes.

Step 2: Derive the two necessary numerical conditions
Let the indegrees be $d_1,\ldots,d_n$. Since every edge contributes $1$ to exactly one indegree,
$$
\sum_{j=1}^n d_j=\binom n2.
$$
If every $d_j$ is divisible by $m$, then necessarily
$$
m\mid\binom n2.
$$

We also claim that
$$
n\ge2m.
$$
Suppose instead that $n<2m$. Every indegree is a multiple of $m$ lying between $0$ and $n-1$, so the only possible values are $0$ and $m$; if $m>n-1$, only $0$ is available and the positive total degree is already impossible.

Thus assume $m\le n-1$. Let $r$ be the number of vertices of indegree $m$. A tournament has at most one vertex of indegree $0$, because two such vertices would be joined by an edge entering one of them. Hence
$$
r\ge n-1.
$$
Therefore
$$
\binom n2=rm\ge(n-1)m,
$$
which gives $n\ge2m$, contradicting $n<2m$. So both
$$
n\ge2m,
\qquad
m\mid\binom n2
$$
are necessary.

Step 3: Construct a tournament whenever the numerical conditions hold
Assume now that
$$
n\ge2m,
\qquad
m\mid\binom n2.
$$
Set
$$
L=m\left\lfloor\frac{n-1}{2m}\right\rfloor,
\qquad
U=L+m,
$$
and
$$
t=n-1-2L.
$$
Then
$$
0\le t<2m.
$$
Define
$$
r=\frac{nt}{2m}.
$$
This is an integer, because
$$
\binom n2-nL=\frac{nt}{2}
$$
and both terms on the left are divisible by $m$. Also $0\le r<n$.

Consider the nondecreasing integer sequence consisting of $n-r$ copies of $L$ followed by $r$ copies of $U$. Its sum is
$$
(n-r)L+rU
=nL+rm
=nL+\frac{nt}{2}
=\binom n2.
$$
The values lie in the tournament degree range. Clearly $L\ge0$. If $n>2m$, then $n-1\ge2m$ and
$$
U=L+m\le\frac{n-1}{2}+m\le n-1.
$$
If $n=2m$, then $L=0$ and $U=m\le n-1$.

We use the following exact form of Landau's tournament score theorem: a nondecreasing sequence
$$
0\le d_1\le\cdots\le d_n\le n-1
$$
is the indegree sequence of a tournament if and only if
$$
\sum_{i=1}^k d_i\ge\binom k2
$$
for every $1\le k<n$, with equality at $k=n$.

We verify these inequalities for our two-level sequence.

If $k\le n-r$, then
$$
\sum_{i=1}^k d_i=kL.
$$
Since
$$
t=n-1-2L
$$
and
$$
r=\frac{nt}{2m}\ge t
$$
by $n\ge2m$, we have
$$
n-r-1\le2L.
$$
Thus $k-1\le2L$, and therefore
$$
kL\ge\binom k2.
$$

Now let $k>n-r$ and write $k=n-h$, where $0\le h<r$. Using the total sum,
$$
\sum_{i=1}^k d_i
=\binom n2-hU.
$$
Hence
$$
\sum_{i=1}^k d_i-\binom k2
=\frac h2\bigl(2n-h-1-2U\bigr).
$$
It is enough to show $r\le2n-2U$. Since $n=2m+q$ for some $q\ge0$,
$$
2n-2U=n+1+t-2m=q+1+t,
$$
while
$$
r=\frac{nt}{2m}
=t+\frac{qt}{2m}
< t+q+1.
$$
Thus the required prefix inequalities hold. Landau's theorem therefore gives a tournament on $n$ vertices whose every indegree is either $L$ or $U$, hence divisible by $m$.

Step 4: Realize the tournament by primes
Fix such a tournament $T$. We construct distinct primes
$$
p_1,\ldots,p_n\equiv3\pmod4
$$
so that, for $i\ne j$,
$$
i\to j
\quad\Longleftrightarrow\quad
\left(\frac{p_i}{p_j}\right)=-1.
$$

Choose any prime $p_1\equiv3\pmod4$. Suppose $p_1,\ldots,p_k$ have already been chosen with the correct Legendre-symbol relations among them. To choose $p_{k+1}$, for each $i\le k$ select a nonzero residue $r_i$ modulo $p_i$ with
$$
\left(\frac{r_i}{p_i}\right)
=
\begin{cases}
1,& i\to k+1,\\
-1,& k+1\to i.
\end{cases}
$$
Both symbol values occur among the nonzero classes modulo an odd prime.

By the Chinese remainder theorem, choose a residue class $r$ modulo
$$
M=4p_1\cdots p_k
$$
satisfying
$$
r\equiv3\pmod4,
\qquad
r\equiv r_i\pmod{p_i}
$$
for all $i\le k$. This class is coprime to $M$. Dirichlet's theorem on primes in arithmetic progressions then provides a prime
$$
p_{k+1}\equiv r\pmod M
$$
larger than all previous primes.

For each $i\le k$, if $i\to k+1$, then
$$
\left(\frac{p_{k+1}}{p_i}\right)=1,
$$
so quadratic reciprocity gives
$$
\left(\frac{p_i}{p_{k+1}}\right)=-1.
$$
If $k+1\to i$, the same argument with signs reversed gives
$$
\left(\frac{p_{k+1}}{p_i}\right)=-1.
$$
Thus the tournament is realized exactly.

At each vertex $j$, the number of indices $i\ne j$ for which $p_i$ is a quadratic nonresidue modulo $p_j$ is precisely the indegree of $j$, hence is divisible by $m$.

Therefore the numerical conditions from Step 2 are also sufficient.

Final Answer: $\boxed{n\ge2m\text{ and }m\mid\binom n2}$

---

## Answer

$n\ge2m\text{ and }m\mid\binom n2$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Equation or inequality

---

## Solution Concepts

- quadratic reciprocity
- tournament score sequences
- Landau score criterion
- Chinese remainder theorem
- primes in arithmetic progressions
