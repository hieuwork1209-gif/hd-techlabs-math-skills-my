## Steps

Step 1: Reduce infinite exchangeability to a moment problem
By the Bernoulli de Finetti theorem, there is a random variable $\Theta\in[0,1]$ such that, conditional on $\Theta$, the variables $X_1,X_2,\ldots$ are independent Bernoulli variables with success probability $\Theta$.

Therefore
$$
\mathbb{E}[\Theta]=\mathbb{P}(X_1=1)=p.
$$
Write
$$
q=\mathbb{E}[\Theta^2]=\mathbb{P}(X_1=X_2=1).
$$
Since each $X_i$ has variance $p(1-p)$,
$$
\rho
=\operatorname{Corr}(X_1,X_2)
=\frac{q-p^2}{p(1-p)},
$$
so
$$
q=p^2+\rho p(1-p).
$$
For every integer $n\geq3$,
$$
\mathbb{P}(X_1=\cdots=X_n=1)=\mathbb{E}[\Theta^n].
$$
Thus it remains to maximize the $n$th moment of a random variable in $[0,1]$ whose first two moments are $p$ and $q$.

Step 2: Construct the only two-point candidate compatible with the moments
Set
$$
a=\frac{p-q}{1-p}=p(1-\rho).
$$
Because $0<p<1$ and $0<\rho<1$,
$$
0<a<p<1.
$$
Let
$$
w=\frac{p-a}{1-a}=\frac{\rho p}{1-p+\rho p},
$$
and define $\Theta_*$ by
$$
\mathbb{P}(\Theta_*=1)=w,
\qquad
\mathbb{P}(\Theta_*=a)=1-w.
$$
Then $\mathbb{E}[\Theta_*]=p$. On the two-point set $\{a,1\}$ one has
$$
x^2=(1+a)x-a,
$$
so
$$
\mathbb{E}[\Theta_*^2]=(1+a)p-a.
$$
The definition of $a$ is equivalent to
$$
q=p-a(1-p)=(1+a)p-a,
$$
hence $\Theta_*$ has the required first two moments.

Its $n$th moment is
$$
\mathbb{E}[\Theta_*^n]
=w+(1-w)a^n
=\frac{\rho p+(1-p)[p(1-\rho)]^n}{1-p+\rho p}.
$$

Step 3: Build a quadratic majorant that proves global optimality
Let $H$ be the unique quadratic polynomial satisfying
$$
H(a)=a^n,
\qquad
H'(a)=na^{n-1},
\qquad
H(1)=1.
$$
The elementary identity
$$
\frac{u^r-v^r}{u-v}=\sum_{j=0}^{r-1}u^{r-1-j}v^j
$$
applied successively to the repeated interpolation nodes $a,a,1,x$ gives the exact factorization
$$
H(x)-x^n
=(1-x)(x-a)^2
\sum_{\substack{i,j,k,\ell\geq0\\i+j+k+\ell=n-3}}
a^{i+j}x^\ell.
$$
Every term on the right is nonnegative for $0\leq x\leq1$, so
$$
H(x)\geq x^n
$$
throughout $[0,1]$.

Now let $\Theta$ be any mixing variable with the required first two moments. Since $H$ is quadratic and $\Theta$ and $\Theta_*$ have the same moments of degrees $0,1,2$,
$$
\mathbb{E}[H(\Theta)]=\mathbb{E}[H(\Theta_*)].
$$
Because $H$ agrees with $x^n$ at both points in the support of $\Theta_*$,
$$
\mathbb{E}[H(\Theta_*)]=\mathbb{E}[\Theta_*^n].
$$
Consequently
$$
\mathbb{E}[\Theta^n]
\leq\mathbb{E}[H(\Theta)]
=\mathbb{E}[\Theta_*^n].
$$
Thus the value found in Step 2 is a sharp upper bound.

Step 4: Verify equality, uniqueness, and realization by an exchangeable sequence
For $n\geq3$, the sum in the factorization from Step 3 is strictly positive on $[0,1]$: the term with $k=n-3$ and $i=j=\ell=0$ already equals $1$. Hence
$$
H(x)=x^n
$$
for $x\in[0,1]$ only when $x=a$ or $x=1$.

Therefore equality in the moment bound forces
$$
\Theta\in\{a,1\}
$$
almost surely. The condition $\mathbb{E}[\Theta]=p$ then forces the weight at $1$ to be $w$, so the extremal mixing law is unique.

Conversely, take $\Theta=\Theta_*$ and, conditional on $\Theta$, let $X_1,X_2,\ldots$ be independent Bernoulli variables with success probability $\Theta$. This produces an infinite exchangeable Bernoulli sequence with
$$
\mathbb{P}(X_1=1)=p
$$
and
$$
\operatorname{Corr}(X_1,X_2)
=\frac{\mathbb{E}[\Theta_*^2]-p^2}{p(1-p)}
=\rho.
$$
Hence the sharp bound is attained.

Final Answer: $\boxed{\frac{\rho p+(1-p)[p(1-\rho)]^n}{1-p+\rho p}}$

---

## Answer

$\frac{\rho p+(1-p)[p(1-\rho)]^n}{1-p+\rho p}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- de Finetti theorem
- exchangeable Bernoulli mixtures
- moment extremization
- Hermite interpolation
- equality-case analysis
