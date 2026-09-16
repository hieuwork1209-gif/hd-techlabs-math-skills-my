## Steps

Step 1: Construct an admissible exchangeable law attaining a large central mass.
Let $U$ be the uniform probability measure on $\{-1,1\}^{12}$. For $x=(x_1,\ldots,x_{12})$, write
$$
S(x)=\sum_{i=1}^{12}x_i,
\qquad
R(x)=\prod_{i=1}^{12}x_i.
$$
Define a density with respect to $U$ by
$$
h(x)=1+\frac{R(x)(74-S(x)^2)}{70}.
$$
Since
$$
S^2=12+2\sum_{i<j}x_ix_j,
$$
we have
$$
h=1+\frac{31}{35}R-\frac1{35}\sum_{i<j}\prod_{k\ne i,j}x_k.
$$
Thus every nonconstant Fourier character in $h$ has degree $10$ or $12$. Hence for every nonempty $A\subseteq\{1,\ldots,12\}$ with $|A|\le9$,
$$
\mathbb E_U\left[h(X)\prod_{i\in A}X_i\right]=0,
$$
by orthogonality of distinct characters under $U$. Therefore, if $h\ge0$, the law $d\mu_*=h\,dU$ is $9$-wise independent and in particular admissible.

To check nonnegativity, note that when $R=1$, the possible values are $S\in\{0,\pm4,\pm8,\pm12\}$ and
$$
h=\frac{144-S^2}{70}\ge0.
$$
When $R=-1$, the possible values are $S\in\{\pm2,\pm6,\pm10\}$ and
$$
h=\frac{S^2-4}{70}\ge0.
$$
The density depends only on permutation-invariant quantities, so $\mu_*$ is exchangeable. At $S=0$ its value is $72/35$, while
$$
U(S=0)=\frac{\binom{12}{6}}{2^{12}}=\frac{231}{1024}.
$$
Hence
$$
\mu_*(S=0)=\frac{231}{1024}\cdot\frac{72}{35}=\frac{297}{640}.
$$
Moreover, $h=0$ exactly at $|S|=2$ and $|S|=12$.

Step 2: Derive a sharp degree-eight certificate from the support of the construction.
The positive support values of $\mu_*$ are $S=0$ and $|S|=4,6,8,10$. A sharp even polynomial majorant of degree $8$ should equal $1$ at $0$ and vanish at those four nonzero magnitudes. These conditions force
$$
Q(s)=\frac{(s^2-16)(s^2-36)(s^2-64)(s^2-100)}{3686400},
$$
because the numerator is the unique even degree-eight polynomial with those four pairs of roots, and the denominator makes $Q(0)=1$.

Every possible value of $S$ is an even integer between $-12$ and $12$. Direct substitution at the only two magnitudes not already covered gives
$$
Q(2)=\frac35,
\qquad
Q(12)=\frac{66}{5}.
$$
Thus
$$
Q(s)\ge \mathbf 1_{\{s=0\}}
$$
for every possible value of $S$.

For any admissible law $\mu$, every polynomial in $S$ of degree at most $8$ has the same expectation as under $U$: after expansion and using $X_i^2=1$, each monomial involves at most eight distinct coordinates. Therefore
$$
\mu(S=0)\le \mathbb E_\mu Q(S)=\mathbb E_UQ(S).
$$
The law $\mu_*$ is $9$-wise independent, so the same degree-eight expectation may be evaluated under $\mu_*$. On its support, $Q(S)$ is $1$ at $S=0$ and $0$ elsewhere. Hence
$$
\mathbb E_UQ(S)=\mathbb E_{\mu_*}Q(S)=\mu_*(S=0)=\frac{297}{640}.
$$
This proves that $297/640$ is the maximum.

Step 3: Reconstruct the symmetrized law of every maximizer.
Let $\mu$ attain the maximum. Since
$$
Q(S)-\mathbf 1_{\{S=0\}}\ge0
$$
and its expectation under $\mu$ is zero, it vanishes $\mu$-almost surely. The values $Q(2)=3/5$ and $Q(12)=66/5$ therefore imply
$$
\mu(|S|=2)=\mu(|S|=12)=0.
$$
Put
$$
K=\frac{S+12}{2}=\#\{i:X_i=1\}.
$$
Then under the permutation symmetrization $\bar\mu$, the variable $K$ is supported on
$$
A=\{1,2,3,4,6,8,9,10,11\}.
$$
Symmetrization preserves admissibility and the law of $S$. If $B\sim\operatorname{Bin}(12,1/2)$, then for every polynomial $f$ of degree at most $8$,
$$
\mathbb E_{\bar\mu}f(K)=\mathbb E f(B),
$$
because $K=\sum_i (X_i+1)/2$ and every expanded monomial of degree at most $8$ depends on at most eight coordinates. The same identities hold for the exchangeable law $\mu_*$ from Step 1.

Let $\nu$ and $\nu_*$ be the laws of $K$ under $\bar\mu$ and $\mu_*$. Both are supported on the nine-point set $A$ and have the same moments of orders $0,1,\ldots,8$. If $c_a=\nu(a)-\nu_*(a)$, then
$$
\sum_{a\in A}c_a a^j=0,
\qquad j=0,1,\ldots,8.
$$
The coefficient matrix is the Vandermonde matrix on the nine distinct points of $A$, whose determinant is
$$
\prod_{a<b}(b-a)\ne0.
$$
Hence every $c_a=0$, so $\nu=\nu_*$. An exchangeable law on the cube is determined by the law of $K$, because permutations act transitively on each level set of $K$. Therefore $\bar\mu=\mu_*$ for every maximizing $\mu$, and its density with respect to $U$ is the density $h$ from Step 1.

Final Answer: $\boxed{\left(\frac{297}{640},x\mapsto1+\frac{R(x)(74-S(x)^2)}{70}\right)}$

---

## Answer

$\left(\frac{297}{640},x\mapsto1+\frac{R(x)(74-S(x)^2)}{70}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- finite-wise independence
- fourier characters on the discrete cube
- polynomial majorant certificate
- exchangeable symmetrization
- vandermonde moment uniqueness
