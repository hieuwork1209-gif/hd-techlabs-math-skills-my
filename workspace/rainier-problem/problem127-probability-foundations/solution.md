## Steps

Step 1: Reduce finite exchangeability to the distribution of the total number of successes
Let
$$
K=X_1+\cdots+X_N.
$$
Because $(X_1,\ldots,X_N)$ is exchangeable, conditional on $K=k$ every binary vector with exactly $k$ ones has the same probability. Hence the law is determined by the distribution of $K$ on $\{0,1,\ldots,N\}$.

Set
$$
q=\mathbb{P}(X_1=X_2=1).
$$
Since
$$
\rho
=\frac{q-p^2}{p(1-p)},
$$
we have
$$
q=p^2+\rho p(1-p).
$$
Moreover,
$$
\mathbb{E}[K]=Np
$$
and
$$
\mathbb{E}[K(K-1)]=N(N-1)q.
$$
The quantity to maximize is exactly
$$
\mathbb{P}(K=N).
$$

Step 2: Build a sharp quadratic certificate on the integer lattice
Define
$$
a=(N-1)p(1-\rho),
\qquad
r=\lfloor a\rfloor.
$$
Because $0<p<1$ and $0<\rho<1$,
$$
0<a<N-1,
$$
so $0\leq r\leq N-2$.

For integers $k\in\{0,1,\ldots,N\}$, put
$$
Q(k)=\frac{(k-r)(k-r-1)}{(N-r)(N-r-1)}.
$$
For every integer $k<N$, the product $(k-r)(k-r-1)$ is nonnegative, while
$$
Q(N)=1.
$$
Therefore
$$
\mathbf{1}_{\{K=N\}}\leq Q(K).
$$
Taking expectations and using the two moment identities from Step 1 gives
$$
\mathbb{P}(K=N)
\leq
\frac{N(N-1)q-2rNp+r(r+1)}{(N-r)(N-r-1)}.
$$
Substituting $q=p^2+\rho p(1-p)$ gives the proposed upper bound.

Step 3: Construct a distribution of K that attains the certificate
Write
$$
\delta=a-r,
$$
so $0\leq\delta<1$. Define
$$
x=\frac{(1-\delta)N(1-p)}{N-r},
\qquad
y=\frac{\delta N(1-p)}{N-r-1},
\qquad
w=1-x-y.
$$
The first two weights are nonnegative. Also,
$$
(N-r)(N-r-1)w
=(N-r)(N-r-1)-N(1-p)(N-r-1+\delta).
$$
Using $r+\delta=a=(N-1)p(1-\rho)$, this simplifies to
$$
(N-r)(N-r-1)w
=N(N-1)\bigl(p^2+\rho p(1-p)\bigr)-2rNp+r(r+1).
$$
Thus $w$ is exactly the upper bound from Step 2. To see that it is nonnegative, let $B$ be a binomial random variable with parameters $N$ and $p$. The numerator above equals
$$
\mathbb{E}[(B-r)(B-r-1)]
+N(N-1)\rho p(1-p),
$$
which is nonnegative because $(B-r)(B-r-1)\geq0$ for integer $B$. Hence $x,y,w$ are valid probabilities.

Now define $K$ by
$$
\mathbb{P}(K=r)=x,
\qquad
\mathbb{P}(K=r+1)=y,
\qquad
\mathbb{P}(K=N)=w.
$$
Since
$$
(N-r)x+(N-r-1)y=N(1-p),
$$
we get
$$
\mathbb{E}[K]=Np.
$$
Also,
$$
(N-1)\mathbb{E}[K]-\mathbb{E}[K(K-1)]
=\mathbb{E}[K(N-K)].
$$
For the three-point distribution above,
$$
\mathbb{E}[K(N-K)]
=r(N-r)x+(r+1)(N-r-1)y
=(r+\delta)N(1-p).
$$
Because $r+\delta=a=(N-1)p(1-\rho)$, this equals
$$
(N-1)Np(1-p)(1-\rho).
$$
Combining this with $\mathbb{E}[K]=Np$ yields
$$
\mathbb{E}[K(K-1)]
=N(N-1)\bigl(p^2+\rho p(1-p)\bigr),
$$
so the required first two exchangeable moments are satisfied.

Step 4: Realize the extremal K-law by an exchangeable Bernoulli vector and close the equality case
Conditional on $K=k$, choose uniformly among all binary vectors in $\{0,1\}^N$ having exactly $k$ ones. The resulting Bernoulli vector is exchangeable. Its marginal and pair probabilities satisfy
$$
\mathbb{P}(X_1=1)=\frac{\mathbb{E}[K]}{N}=p
$$
and
$$
\mathbb{P}(X_1=X_2=1)
=\frac{\mathbb{E}[K(K-1)]}{N(N-1)}
=p^2+\rho p(1-p),
$$
so its pairwise correlation is $\rho$.

For this construction,
$$
\mathbb{P}(X_1=\cdots=X_N=1)=\mathbb{P}(K=N)=w,
$$
which equals the upper bound from Step 2. Thus the bound is sharp.

Moreover, $Q(k)>0$ for every $k<N$ except $k=r,r+1$. Hence equality in the certificate forces every extremal law of $K$ to be supported on $\{r,r+1,N\}$. The two moment constraints then determine the three weights uniquely, so the extremal success-count law is unique.

Final Answer: $\boxed{\frac{N(N-1)(p^2+\rho p(1-p))-2rNp+r(r+1)}{(N-r)(N-r-1)}}$

---

## Answer

$\frac{N(N-1)(p^2+\rho p(1-p))-2rNp+r(r+1)}{(N-r)(N-r-1)}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- finite exchangeability
- success-count representation
- moment constraints
- quadratic lattice certificate
- extremal discrete distribution
