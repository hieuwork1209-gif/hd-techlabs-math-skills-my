## Steps

Step 1: Reduce the gcd to two intrinsic prime families

Let $m\ge3$ be odd and put
$$
N=2m,
\qquad
H_m=\gcd\left\{\binom N{2j}:1\le j\le m-1\right\}.
$$
Since $j=1$ is allowed,
$$
H_m\mid\binom N2=m(N-1).
\tag{1}
$$
Also $\gcd(m,N-1)=\gcd(m,2m-1)=1$. Therefore every prime divisor of $H_m$ belongs to exactly one of the two families
$$
q\mid m
\qquad\text{or}\qquad
q\mid N-1.
\tag{2}
$$
All such primes are odd.

We use two standard facts in precise form.

**Lucas' theorem.** If $q$ is prime and
$$
A=\sum_{r\ge0}A_rq^r,
\qquad
B=\sum_{r\ge0}B_rq^r,
\qquad 0\le A_r,B_r<q,
$$
then
$$
\binom AB\equiv\prod_{r\ge0}\binom{A_r}{B_r}\pmod q.
\tag{3}
$$
Hence
$$
q\nmid\binom AB
$$
if and only if $B_r\le A_r$ for every $r$.

**Kummer's theorem.** For prime $q$,
$$
v_q\binom AB
$$
equals the number of carries when $B$ and $A-B$ are added in base $q$.

Step 2: Classify the primes $q\mid m$ that survive

Fix a prime $q\mid m$. Since $q\mid N$, the units digit of $N$ in base $q$ is $0$. Write
$$
N=\sum_{r\ge1}N_rq^r,
\qquad
S_q(N):=\sum_{r\ge1}N_r.
\tag{4}
$$
Because $q$ is odd,
$$
N\equiv S_q(N)\pmod2,
$$
so $S_q(N)$ is even.

By Lucas' theorem, $q$ fails to divide some allowed coefficient exactly when there is an even integer $K$ with
$$
0<K<N,
\qquad
K_r\le N_r\ \text{for every base-}q\text{ digit }r.
\tag{5}
$$
Because $q$ is odd, the parity of such a digitwise subnumber $K$ is the parity of the sum of its chosen digits.

If
$$
S_q(N)=2,
$$
then every nonzero proper digitwise subnumber has digit sum $1$, hence is odd. Thus no allowed even $K$ satisfies (5), and Lucas gives
$$
q\mid\binom N{2j}
\qquad(1\le j\le m-1).
\tag{6}
$$

Conversely, suppose $S_q(N)\ge4$. If some digit $N_r\ge2$, choose
$$
K=2q^r.
$$
If every nonzero digit equals $1$, choose two distinct nonzero digit positions $r\ne s$ and put
$$
K=q^r+q^s.
$$
In either case $K$ is even, digitwise bounded by $N$, positive, and proper because its digit sum is $2<S_q(N)$. Thus Lucas gives
$$
q\nmid\binom NK,
$$
so $q\nmid H_m$.

Therefore, for $q\mid m$,
$$
q\mid H_m
\quad\Longleftrightarrow\quad
S_q(2m)=2.
\tag{7}
$$
Because the units digit is $0$, condition (7) is equivalent to exactly one of the two forms
$$
2m=2q^a
\tag{8}
$$
or
$$
2m=q^a+q^b,
\qquad a>b\ge1.
\tag{9}
$$

Step 3: Show every surviving prime from $m$ occurs to exponent one

Assume first that
$$
N=2q^a.
$$
Take
$$
K=2q^{a-1}.
$$
This is an allowed even index. Moreover
$$
N-K=q^a+(q-2)q^{a-1}.
$$
When $K$ and $N-K$ are added in base $q$, the digit $2+(q-2)=q$ at position $a-1$ creates one carry, and after that carry the digit at position $a$ becomes $2$. There are no other carries. Kummer's theorem therefore gives
$$
v_q\binom NK=1.
\tag{10}
$$

Now assume
$$
N=q^a+q^b,
\qquad a>b\ge1.
$$
Take
$$
K=2q^{b-1}.
$$
Then
$$
N-K=q^a+(q-2)q^{b-1}.
$$
Again the addition of $K$ and $N-K$ has exactly one carry, from position $b-1$ to position $b$. Hence
$$
v_q\binom NK=1.
\tag{11}
$$

Thus every prime $q\mid m$ satisfying (7) appears in the gcd with exponent exactly one.

Step 4: Classify the primes dividing $2m-1$

Now fix a prime
$$
q\mid N-1.
$$
Write
$$
N-1=q^a s,
\qquad a=v_q(N-1),
\qquad q\nmid s.
\tag{12}
$$
Then
$$
N=q^a s+1.
\tag{13}
$$

Suppose first that $s>1$. The even integer
$$
K=q^a+1
\tag{14}
$$
satisfies $0<K<N$. In base $q$, equation (13) shows that the units digit of $N$ is $1$, the next $a-1$ digits are $0$, and the digit in position $a$ is the nonzero residue of $s$ modulo $q$. Thus the two nonzero digits of $K$ are digitwise bounded by those of $N$. Lucas' theorem gives
$$
q\nmid\binom N{q^a+1},
\tag{15}
$$
so $q\nmid H_m$.

Therefore a prime divisor of $N-1$ can survive only if
$$
N-1=q^a.
\tag{16}
$$
Conversely, if (16) holds, then
$$
N=q^a+1.
$$
Its only nonzero base-$q$ digits are two $1$'s, in positions $0$ and $a$. Hence the only digitwise subnumbers are
$$
0,\ 1,\ q^a,\ q^a+1.
$$
The two positive proper ones are odd. Thus every allowed even index violates a Lucas digit inequality, and
$$
q\mid H_m.
\tag{17}
$$

To determine the exponent, take
$$
K=q^{a-1}+1.
$$
Then
$$
N-K=q^a-q^{a-1}=(q-1)q^{a-1}.
$$
Adding $K$ and $N-K$ in base $q$ produces exactly one carry at position $a-1$ and no others. Kummer's theorem gives
$$
v_q\binom NK=1.
\tag{18}
$$
So a prime from $N-1$ survives exactly when $N-1$ is a power of that prime, and then only to the first power.

Step 5: Combine the local conditions

By (1)-(2), no other prime can divide $H_m$. Steps 2-4 show that every surviving prime occurs exactly once.

Therefore
$$
H_m=
\prod_{\substack{q\text{ prime}:\\
2m=2q^a\ \text{or}\ 2m=q^a+q^b\ (a>b\ge1)\\
\text{or}\ 2m-1=q^a}}q,
$$
where the exponents $a,b$ are positive integers whenever they appear.

## Solution Concepts

- Lucas digitwise criterion for divisibility of restricted binomial coefficients.
- Parity classification of proper base-$q$ subnumbers with digit sum two.
- Kummer carry counts giving the exact common prime exponents.

Final Answer: $H_m=\prod_{\substack{q\text{ prime}\\2m=2q^a\text{ or }q^a+q^b\ (a>b\ge1)\text{ or }2m-1=q^a}}q$.
