## Steps

Step 1: Reduce the upper bound to four moments of the Rademacher sum
Let
$$
n=m^2,
$$
and write
$$
S=X_1+\cdots+X_n.
$$
Because the variables are fair Rademacher variables and are $4$-wise independent, expanding powers of $S$ gives the same first four moments as for a sum of independent fair Rademacher variables:
$$
\mathbb E S=0,
\qquad
\mathbb E S^2=n,
\qquad
\mathbb E S^3=0,
$$
and
$$
\mathbb E S^4=3n^2-2n.
$$
For the fourth moment, the only nonzero terms are those in which every index occurs an even number of times. There are $n$ terms with one index repeated four times and $6\binom n2$ terms with two indices each repeated twice, so
$$
\mathbb E S^4=n+6\binom n2=3n^2-2n.
$$
The event that all variables equal $1$ is exactly the event $S=n$.

Step 2: Build a quartic lattice certificate
Since $n=m^2$, the integers $n$ and $m$ have the same parity. Every value of $S$ therefore has the same parity as $m$. Define
$$
Q(s)=(s+m+2)(s+m)(s-m+2)(s-m).
$$
For an integer $s$ with the same parity as $m$, both numbers $s+m$ and $s-m$ are even. Hence
$$
(s+m)(s+m+2)\ge0,
\qquad
(s-m)(s-m+2)\ge0,
$$
so
$$
Q(s)\ge0
$$
for every possible value of $S$.

Also $Q(n)>0$. Therefore
$$
\mathbf 1_{\{S=n\}}\le\frac{Q(S)}{Q(n)},
$$
and consequently
$$
\mathbb P(S=n)\le\frac{\mathbb E Q(S)}{Q(n)}.
$$

It is useful to rewrite
$$
Q(s)=\bigl((s+1)^2-(m+1)^2\bigr)\bigl((s+1)^2-(m-1)^2\bigr).
$$
Since $m^2=n$, this is
$$
Q(s)=(s^2+2s-n)^2-4n.
$$
Using the moments from Step 1,
$$
\begin{aligned}
\mathbb E Q(S)
&=\mathbb E S^4+4\mathbb E S^3+(4-2n)\mathbb E S^2
-4n\mathbb E S+n^2-4n\\
&=(3n^2-2n)+(4-2n)n+n^2-4n\\
&=2n(n-1).
\end{aligned}
$$
On the other hand,
$$
\begin{aligned}
Q(n)
&=(n+m+2)(n+m)(n-m+2)(n-m)\\
&=m^2(m^2-1)(m^4+3m^2+4)\\
&=n(n-1)(m^4+3m^2+4).
\end{aligned}
$$
Thus every admissible law satisfies
$$
\mathbb P(X_1=\cdots=X_n=1)
\le
\frac{2}{m^4+3m^2+4}.
$$

Step 3: Construct a moment distribution attaining the bound
Let $G$ be a sum of $n=m^2$ independent fair Rademacher variables. Consider the five lattice points
$$
T=\{-m-2,-m,m-2,m,n\}.
$$
They all lie between $-n$ and $n$ and have the same parity as $n$.

For each $t\in T$, let $\ell_t$ be the degree-$4$ Lagrange polynomial for the node set $T$:
$$
\ell_t(x)=\prod_{u\in T\setminus\{t\}}\frac{x-u}{t-u},
$$
and define
$$
p_t=\mathbb E\ell_t(G).
$$
For every polynomial $h$ of degree at most $4$, Lagrange interpolation gives
$$
h(x)=\sum_{t\in T}h(t)\ell_t(x).
$$
Taking expectation at $x=G$ yields
$$
\mathbb E h(G)=\sum_{t\in T}p_t h(t).
$$
In particular, the numbers $p_t$ reproduce all moments of $G$ through degree $4$.

Using
$$
\mathbb E G=0,
\quad
\mathbb E G^2=n,
\quad
\mathbb E G^3=0,
\quad
\mathbb E G^4=3n^2-2n
$$
in the explicit Lagrange polynomials gives
$$
p_{-m-2}=\frac{m(m-1)}{4(m^2+m+2)},
\qquad
p_{-m}=\frac14,
$$
$$
p_{m-2}=\frac{m(m+1)}{4(m^2-m+2)},
\qquad
p_m=\frac14,
$$
and
$$
p_n=\frac{2}{m^4+3m^2+4}.
$$
All five numbers are nonnegative for $m\ge2$. Since the interpolation identity applied to $h\equiv1$ gives
$$
\sum_{t\in T}p_t=1,
$$
they define a probability distribution on $T$. Notice also that
$$
\ell_n(x)=\frac{Q(x)}{Q(n)},
$$
so the formula for $p_n$ agrees with the upper-bound calculation in Step 2.

Step 4: Lift the moment distribution to an exchangeable $4$-wise independent law
Choose a random variable $S$ taking values in $T$ with probabilities $p_t$ from Step 3, and put
$$
K=\frac{n+S}{2}.
$$
Because every element of $T$ has the same parity as $n$, $K$ is integer-valued in $\{0,1,\dots,n\}$.

Conditional on $K=k$, choose uniformly among all sign vectors in $\{-1,1\}^n$ having exactly $k$ coordinates equal to $1$. This produces an exchangeable law for $(X_1,\dots,X_n)$.

The distribution of $S=2K-n$ has the same moments through degree $4$ as the independent Rademacher sum $G$. Therefore $K$ has the same moments, and hence the same falling-factorial moments through degree $4$, as a $\operatorname{Bin}(n,1/2)$ random variable:
$$
\mathbb E(K)_j=\frac{(n)_j}{2^j}
\qquad(0\le j\le4).
$$
For distinct indices $i_1,\dots,i_j$ with $j\le4$, exchangeability and the conditional uniform construction give
$$
\mathbb P(X_{i_1}=\cdots=X_{i_j}=1)
=\frac{\mathbb E(K)_j}{(n)_j}
=2^{-j}.
$$
Mixed sign patterns follow by inclusion-exclusion. If among $j$ specified coordinates exactly $r$ are required to be $1$ and the other $j-r$ are required to be $-1$, then
$$
\sum_{q=0}^{j-r}(-1)^q\binom{j-r}{q}2^{-(r+q)}
=2^{-j}.
$$
Thus every set of at most four coordinates is mutually independent and each coordinate is fair.

Finally, all coordinates equal $1$ exactly when $S=n$, so the constructed law has
$$
\mathbb P(X_1=\cdots=X_n=1)=p_n
=\frac{2}{m^4+3m^2+4}.
$$
This attains the upper bound from Step 2.

Final Answer: $\boxed{\frac{2}{m^4+3m^2+4}}$

---

## Answer

$\frac{2}{m^4+3m^2+4}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- exchangeable Rademacher variables
- four-wise independence
- moment extremal polynomial
- Lagrange interpolation
- factorial moments
