## Steps

Step 1: Reduce the gcd to prime divisors of $n$

For $n\ge2$, define
$$
G_n:=\gcd\left\{\binom nk:1\le k<n,\ k\text{ odd}\right\}.
$$
Because $k=1$ is allowed,
$$
G_n\mid \binom n1=n.
\tag{1}
$$
Thus every prime divisor of $G_n$ must already divide $n$.

We will repeatedly use Lucas' theorem in the following precise form. Let $p$ be prime, and write
$$
N=N_0+N_1p+\cdots+N_rp^r,
\qquad
K=K_0+K_1p+\cdots+K_rp^r,
$$
with $0\le N_i,K_i<p$. Then
$$
\binom NK\equiv \prod_{i=0}^r\binom{N_i}{K_i}\pmod p.
\tag{2}
$$
In particular, if some digit $K_i>N_i$, then $p\mid\binom NK$; if every $K_i\le N_i$, then the product on the right is nonzero modulo $p$.

Step 2: Handle even $n$

Assume
$$
n=2^a m,
\qquad a\ge1,
\qquad m\text{ odd}.
$$
For every odd $k$,
$$
\binom nk=\frac nk\binom{n-1}{k-1}.
\tag{3}
$$
Since $k$ is odd,
$$
v_2\left(\binom nk\right)
=a+v_2\left(\binom{n-1}{k-1}\right)\ge a.
$$
Hence
$$
2^a\mid G_n.
\tag{4}
$$
On the other hand, $k=1$ gives $\binom n1=n$, whose $2$-adic valuation is exactly $a$. Therefore
$$
v_2(G_n)=a.
\tag{5}
$$

Now let $p$ be any odd prime divisor of $n$, and put
$$
b=v_p(n),
\qquad n=p^b s,
\qquad p\nmid s.
$$
Choose
$$
k=p^b.
$$
This $k$ is odd, and $k<n$ because $n$ is even. In base $p$, the lowest $b$ digits of $n$ are zero, while the digit in position $b$ is the nonzero residue of $s$ modulo $p$. The number $k=p^b$ has digit $1$ in position $b$ and zeros elsewhere. Thus every digit of $k$ is at most the corresponding digit of $n$, and by (2),
$$
p\nmid \binom n{p^b}.
\tag{6}
$$
So no odd prime divisor of $n$ can divide $G_n$. Combining (1), (5), and (6),
$$
G_n=2^{v_2(n)}
\qquad(n\text{ even}).
\tag{7}
$$

Step 3: Handle odd $n$ having at least two distinct prime divisors

Assume $n$ is odd and not a prime power. Let $p$ be any prime divisor of $n$, and again write
$$
b=v_p(n),
\qquad n=p^b s,
\qquad p\nmid s.
$$
Because $n$ is not a power of $p$, one has $s>1$. Set
$$
k=p^b.
$$
Then $k$ is odd and $1\le k<n$. Exactly the same base-$p$ digit comparison as in Step 2 shows, by Lucas' theorem,
$$
p\nmid\binom n{p^b}.
\tag{8}
$$
Thus each prime divisor $p$ of $n$ is absent from the gcd. Since $G_n\mid n$ by (1), it follows that
$$
G_n=1
\tag{9}
$$
whenever $n$ is odd and has at least two distinct prime divisors.

Step 4: Handle odd prime powers and determine the exact exponent

Now let
$$
n=p^a
$$
with $p$ an odd prime and $a\ge1$.

First we show that every interior binomial coefficient is divisible by $p$. In base $p$, the number $n=p^a$ has digits
$$
1,0,0,\dots,0.
$$
For every integer $k$ with $1\le k<n$, at least one of the lower $a$ base-$p$ digits of $k$ is nonzero. At that position the corresponding digit of $n$ is zero, so Lucas' theorem (2) gives
$$
p\mid\binom nk.
\tag{10}
$$
In particular $p\mid G_n$.

It remains to show that the gcd contains only one factor of $p$. Take the odd index
$$
k=p^{a-1}.
$$
Using
$$
\binom{p^a}{p^{a-1}}
=p\binom{p^a-1}{p^{a-1}-1},
\tag{11}
$$
we examine the second factor modulo $p$. The base-$p$ expansion of $p^a-1$ consists of $a$ digits all equal to $p-1$, while $p^{a-1}-1$ has its lowest $a-1$ digits equal to $p-1$ and its next digit equal to $0$. Applying (2),
$$
\binom{p^a-1}{p^{a-1}-1}\equiv1\pmod p.
\tag{12}
$$
Therefore
$$
v_p\left(\binom{p^a}{p^{a-1}}\right)=1.
\tag{13}
$$
Since $G_n\mid n=p^a$, equations (10) and (13) imply
$$
G_n=p.
\tag{14}
$$

Step 5: Combine the cases

Equations (7), (9), and (14) give the complete answer:
$$
G_n=
\begin{cases}
2^{v_2(n)},&2\mid n,\\
p,&n=p^a\text{ for an odd prime }p,\\
1,&\text{otherwise}.
\end{cases}
$$

## Solution Concepts

- Prime-by-prime reduction of a gcd of binomial coefficients.
- Lucas' theorem and base-$p$ digit compatibility.
- Interaction between parity-restricted indices and prime-power structure of $n$.

Final Answer: $G_n=\begin{cases}2^{v_2(n)},&2\mid n,\\p,&n=p^a\ (p\text{ odd prime}),\\1,&\text{otherwise}.\end{cases}$
