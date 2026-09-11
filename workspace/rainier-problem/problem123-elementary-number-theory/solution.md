## Steps

Step 1: Reduce the possible prime divisors

Let $p$ be an odd prime and define
$$
H_p:=\gcd\left\{\binom{2p}{2j}:1\le j\le p-1\right\}.
$$
Since $j=1$ is allowed,
$$
H_p\mid \binom{2p}{2}=p(2p-1).
\tag{1}
$$
Thus every prime divisor of $H_p$ is either $p$ or a prime divisor of $2p-1$.

We use Lucas' theorem in the following precise form. If $q$ is prime and
$$
N=N_0+N_1q+\cdots+N_rq^r,
\qquad
K=K_0+K_1q+\cdots+K_rq^r,
$$
with $0\le N_i,K_i<q$, then
$$
\binom NK\equiv\prod_{i=0}^r\binom{N_i}{K_i}\pmod q.
\tag{2}
$$
Hence $q\nmid\binom NK$ exactly when every base-$q$ digit of $K$ is at most the corresponding digit of $N$.

Step 2: Determine the $p$-part of the gcd

In base $p$,
$$
2p=(20)_p.
$$
Let $k=2j$ with $1\le j\le p-1$. Then
$$
2\le k\le2p-2.
$$
The only positive multiple of $p$ strictly between $0$ and $2p$ is $p$, and $p$ is odd. Therefore every allowed even $k$ is not divisible by $p$, so its units digit in base $p$ is nonzero. The units digit of $2p$ is $0$. By Lucas' theorem,
$$
p\mid\binom{2p}{k}
\qquad(2\le k\le2p-2,\ k\text{ even}).
\tag{3}
$$
Thus $p\mid H_p$.

On the other hand,
$$
\binom{2p}{2}=p(2p-1)
$$
and $p\nmid2p-1$. Hence
$$
v_p(H_p)=1.
\tag{4}
$$
So the $p$-part of the gcd is exactly $p$.

Step 3: Decide when a prime divisor of $2p-1$ survives

Let $q$ be a prime divisor of $2p-1$, and write
$$
2p-1=q^a s,
\qquad a=v_q(2p-1),
\qquad q\nmid s.
\tag{5}
$$
Because $2p-1$ is odd, $q$ is odd. Then
$$
2p=q^a s+1.
\tag{6}
$$

First suppose $s>1$, so $2p-1$ is not a power of $q$. Choose
$$
k=q^a+1.
\tag{7}
$$
The number $k$ is even because $q$ is odd, and by $s>1$,
$$
2\le k<q^as+1=2p.
$$
Thus $k$ is one of the allowed indices.

In base $q$, equation (6) shows that the units digit of $2p$ is $1$, the next $a-1$ digits are $0$, and the digit in position $a$ is the nonzero residue of $s$ modulo $q$. The number $k=q^a+1$ has digit $1$ in positions $0$ and $a$ and zeros elsewhere. Therefore every digit of $k$ is at most the corresponding digit of $2p$. Lucas' theorem gives
$$
q\nmid\binom{2p}{q^a+1}.
\tag{8}
$$
Hence such a prime $q$ cannot divide $H_p$.

Consequently, a prime divisor $q$ of $2p-1$ can survive in the gcd only if
$$
2p-1=q^a
\tag{9}
$$
for some $a\ge1$.

Step 4: Prove the prime-power condition is sufficient and find the exact exponent

Assume now
$$
2p-1=q^a
$$
for a prime $q$ and $a\ge1$. Then
$$
2p=q^a+1.
\tag{10}
$$
In base $q$, the only nonzero digits of $2p$ are two $1$'s, in positions $0$ and $a$.

Suppose an allowed even integer $k$ satisfied the digit inequalities required for $q\nmid\binom{2p}{k}$. Then the base-$q$ digits of $k$ could only be chosen from those two $1$'s. Hence the only possibilities would be
$$
k\in\{0,1,q^a,q^a+1\}.
$$
The interior possibilities $1$ and $q^a$ are odd, while $0$ and $q^a+1=2p$ are not allowed. Therefore every allowed even $k$ violates at least one Lucas digit inequality, and so
$$
q\mid\binom{2p}{k}
\qquad(2\le k\le2p-2,\ k\text{ even}).
\tag{11}
$$
Thus $q\mid H_p$.

We now show that only one factor of $q$ occurs in the gcd. Take
$$
k=q^{a-1}+1,
$$
which is even and lies strictly between $0$ and $q^a+1$. Using
$$
\binom{q^a+1}{q^{a-1}+1}
=\frac{q^a+1}{q^{a-1}+1}\binom{q^a}{q^{a-1}},
\tag{12}
$$
the prefactor has $q$-adic valuation $0$. Also
$$
\binom{q^a}{q^{a-1}}
=q\binom{q^a-1}{q^{a-1}-1}.
\tag{13}
$$
The base-$q$ digits of $q^a-1$ are all $q-1$, while those of $q^{a-1}-1$ are $q-1$ in the lowest $a-1$ positions and $0$ in position $a-1$. Lucas' theorem gives
$$
\binom{q^a-1}{q^{a-1}-1}\equiv1\pmod q.
\tag{14}
$$
Therefore
$$
v_q\left(\binom{q^a+1}{q^{a-1}+1}\right)=1.
\tag{15}
$$
Hence
$$
v_q(H_p)=1.
\tag{16}
$$

Step 5: Combine the local conditions

By (1), no other primes can occur. Equation (4) gives one factor $p$. Steps 3-4 show that the factor $2p-1$ contributes a prime precisely when it is itself a prime power $q^a$, and then contributes exactly one factor $q$.

Thus
$$
H_p=
\begin{cases}
pq,&2p-1=q^a\text{ for some prime }q,\\
p,&\text{otherwise}.
\end{cases}
$$

## Solution Concepts

- Prime-by-prime analysis of a restricted binomial-coefficient gcd.
- Lucas' theorem and parity of base-$q$ digit selections.
- Prime-power characterization forced by the absence of an admissible digitwise subnumber.

Final Answer: $H_p=\begin{cases}pq,&2p-1=q^a\ (q\text{ prime}),\\p,&\text{otherwise}.\end{cases}$
