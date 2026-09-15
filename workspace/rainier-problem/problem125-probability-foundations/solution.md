## Steps

Step 1: Convert six-wise independence into exact moments of the centered Hamming weight
Let $Y_i=2X_i-1\in\{-1,1\}$, let $T=\sum_{i=1}^{8}Y_i$, and set
$$
Z=\frac{T}{2}=\sum_{i=1}^{8}X_i-4.
$$
Thus $Z$ is an integer in $\{-4,-3,\ldots,4\}$, and the event $X_1=\cdots=X_8$ is exactly $|Z|=4$.

For every power at most $6$, expand $T^m$. After using $Y_i^2=1$, each monomial becomes either $1$ or a product of at most $m\leq6$ distinct $Y_i$'s. Every nonempty such product has expectation $0$ by six-wise independence and $\mathbb E Y_i=0$. Hence the moments through degree $6$ are the same as for eight independent Rademacher variables. In particular, all odd moments through degree $5$ vanish, and
$$
\mathbb E T^2=8.
$$
For the fourth moment, only multiplicity patterns $4$ and $2+2$ survive, so
$$
\mathbb E T^4=8+6\binom82=176.
$$
For the sixth moment, the surviving patterns are $6$, $4+2$, and $2+2+2$. Their multiplicities give
$$
\mathbb E T^6
=8+15\cdot8\cdot7+90\binom83
=5888.
$$
Therefore
$$
\mathbb E Z^2=2,\qquad \mathbb E Z^4=11,\qquad \mathbb E Z^6=92,
$$
and
$$
\mathbb E Z=\mathbb E Z^3=\mathbb E Z^5=0.
$$

Step 2: Build a sharp lattice polynomial certificate for the all-equal event
Because $Z$ is an integer with $|Z|\leq4$, the square $Z^2$ lies in $\{0,1,4,9,16\}$. Consider the degree-six polynomial
$$
g(z)=z^2(z^2-1)(z^2-4).
$$
On the allowed integer values, $g(z)=0$ for $|z|\in\{0,1,2\}$, $g(\pm3)=360$, and $g(\pm4)=2880$. Hence the pointwise inequality
$$
g(Z)\geq2880\,\mathbf 1_{\{|Z|=4\}}
$$
holds. Using the moments from Step 1,
$$
\mathbb E g(Z)=\mathbb E Z^6-5\mathbb E Z^4+4\mathbb E Z^2
=92-55+8=45.
$$
Consequently
$$
\mathbb P(X_1=\cdots=X_8)=\mathbb P(|Z|=4)\leq\frac{45}{2880}=\frac1{64}.
$$

Step 3: Determine the Hamming-weight law forced by equality
Assume equality holds in the bound from Step 2. The pointwise gap is positive only at $|Z|=3$, so equality of expectations forces $\mathbb P(|Z|=3)=0$. For $r\in\{0,1,2,4\}$ write $A_r=\mathbb P(|Z|=r)$. The even moments give
$$
A_0+A_1+A_2+A_4=1,
$$
$$
A_1+4A_2+16A_4=2,
$$
$$
A_1+16A_2+256A_4=11,
$$
$$
A_1+64A_2+4096A_4=92.
$$
Subtracting the second moment equation from the fourth, and the fourth from the sixth, gives
$$
12A_2+240A_4=9,
$$
$$
48A_2+3840A_4=81.
$$
Subtracting four times the first of these equations from the second yields $2880A_4=45$, so
$$
A_4=\frac1{64},\qquad A_2=\frac7{16},\qquad A_1=0,\qquad A_0=\frac{35}{64}.
$$
To split the masses between opposite signs, let
$$
d_r=\mathbb P(Z=r)-\mathbb P(Z=-r),\qquad r\in\{2,4\}.
$$
The identities $\mathbb E Z=\mathbb E Z^3=0$ give
$$
2d_2+4d_4=0,\qquad 8d_2+64d_4=0,
$$
so $d_2=d_4=0$. Thus, with $S=\sum_iX_i$,
$$
\mathbb P(S=0)=\mathbb P(S=8)=\frac1{128},
$$
$$
\mathbb P(S=2)=\mathbb P(S=6)=\frac7{32},\qquad \mathbb P(S=4)=\frac{35}{64},
$$
and all odd Hamming weights have probability $0$.

Step 4: Recover the entire joint distribution from the six-wise cylinder probabilities
For each subset $A\subseteq[8]$, let
$$
w_A=\mathbb P\bigl(\{i:X_i=1\}=A\bigr).
$$
Step 3 shows $w_A=0$ whenever $|A|$ is odd. Six-wise independence implies that for every $T\subseteq[8]$ with $|T|\leq6$,
$$
\sum_{A\supseteq T}w_A
=\mathbb P(X_i=1\text{ for all }i\in T)
=2^{-|T|}.
$$
The Hamming-weight law from Step 3 gives $w_{[8]}=1/128$. If $|T|=6$, the only even supersets of $T$ are $T$ and $[8]$, hence
$$
w_T=\frac1{64}-\frac1{128}=\frac1{128}.
$$
If $|T|=4$, there are $\binom42=6$ six-element supersets of $T$, so
$$
w_T=\frac1{16}-6\cdot\frac1{128}-\frac1{128}=\frac1{128}.
$$
If $|T|=2$, there are $\binom62=15$ four-element supersets and $\binom64=15$ six-element supersets, so
$$
w_T=\frac14-15\cdot\frac1{128}-15\cdot\frac1{128}-\frac1{128}=\frac1{128}.
$$
Finally Step 3 already gives $w_{\varnothing}=1/128$. Therefore every even-cardinality subset of $[8]$ has probability $1/128$ and every odd-cardinality subset has probability $0$. Thus any maximizer is uniquely the uniform distribution on the even-parity vectors in $\{0,1\}^8$.

Step 5: Verify attainment and finish the optimization
Take the uniform distribution on the $2^7=128$ vectors in $\{0,1\}^8$ having even parity. Fix any $k\leq7$ coordinates and any assignment of their values. Among the $2^{8-k}$ completions, exactly half, namely $2^{7-k}$, have even parity. Hence that assignment has probability
$$
\frac{2^{7-k}}{2^7}=2^{-k}.
$$
So this law is actually seven-wise independent, in particular six-wise independent with fair marginals. Both constant vectors $(0,\ldots,0)$ and $(1,\ldots,1)$ have even parity and each has probability $1/128$, so the all-equal event has probability $1/64$. Together with Step 4, this also proves that the maximizer is unique.

Final Answer: $\boxed{\frac{1}{64}}$

---

## Answer

$\frac{1}{64}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- k-wise independence
- Rademacher moment counting
- polynomial extremal certificate
- subset incidence inversion
- parity distribution
