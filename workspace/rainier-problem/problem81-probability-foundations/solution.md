## Steps

Step 1: Construct a high-independence candidate by perturbing only high Fourier levels.
Let $U$ be the uniform probability measure on $\{-1,1\}^{12}$. For $x=(x_1,\ldots,x_{12})$, write
$$
S(x)=\sum_{i=1}^{12}x_i,
\qquad
P(x)=\prod_{i=1}^{12}x_i.
$$
Consider densities with respect to $U$ of the form
$$
h_{a,b}(x)=1+P(x)\bigl(a+bS(x)^2\bigr).
$$
Since
$$
S^2=12+2\sum_{i<j}x_ix_j,
$$
we have
$$
P S^2=12P+2\sum_{i<j}\prod_{k\ne i,j}x_k.
$$
Thus every nonconstant Fourier character occurring in $h_{a,b}$ has degree $10$ or $12$. Also $\mathbb E_U h_{a,b}=1$. Therefore, whenever $h_{a,b}\ge0$, the probability measure $d\mu=h_{a,b}\,dU$ has
$$
\mathbb E_\mu\prod_{i\in A}X_i=0
$$
for every nonempty $A$ with $|A|\le9$: multiplying by such a character cannot match the degree-$10$ or degree-$12$ characters in $h_{a,b}$. Hence for every $J$ with $|J|\le9$ and every $\varepsilon\in\{-1,1\}^{J}$,
$$
\mathbb P_\mu(X_j=\varepsilon_j\text{ for }j\in J)
=2^{-|J|}\mathbb E_\mu\prod_{j\in J}(1+\varepsilon_jX_j)
=2^{-|J|}.
$$
So any nonnegative density of this form is in fact $9$-wise independent.

At $S=0$ there are six $-1$ coordinates, so $P=1$ and the density is $1+a$. To maximize this within the two-parameter family, impose nonnegativity at the two extreme constraints that oppose increasing $a$. When $P=1$ and $|S|=12$,
$$
1+a+144b\ge0,
$$
while when $P=-1$ and $|S|=2$,
$$
1-a-4b\ge0.
$$
These inequalities imply
$$
\frac{-1-a}{144}\le b\le\frac{1-a}{4},
$$
so $a\le37/35$. Equality forces $b=-1/70$. Hence define
$$
h(x)=1+\frac{P(x)(74-S(x)^2)}{70}.
$$
If $P=1$, then $S\in\{0,\pm4,\pm8,\pm12\}$ and
$$
h=\frac{144-S^2}{70}\ge0.
$$
If $P=-1$, then $S\in\{\pm2,\pm6,\pm10\}$ and
$$
h=\frac{S^2-4}{70}\ge0.
$$
Thus $h$ defines a valid $9$-wise independent distribution $\mu_*$.

Step 2: Compute the central mass and identify the support of the candidate.
Under the uniform measure,
$$
U(S=0)=\frac{\binom{12}{6}}{2^{12}}=\frac{231}{1024}.
$$
On $S=0$ the density from Step 1 equals
$$
h=1+\frac{74}{70}=\frac{72}{35}.
$$
Therefore
$$
\mu_*(S=0)=\frac{231}{1024}\cdot\frac{72}{35}=\frac{297}{640}.
$$
The formulas for $h$ also show that $h=0$ exactly at $|S|=2$ and $|S|=12$. Hence the support of $\mu_*$ is contained in
$$
S\in\{0,\pm4,\pm6,\pm8,\pm10\}.
$$

Step 3: Derive a degree-eight polynomial certificate from the equality support.
For an arbitrary $8$-wise independent Rademacher family, expectations of every polynomial in $S$ of degree at most $8$ agree with those under the uniform product measure, because each expanded monomial involves at most eight distinct coordinates after using $X_i^2=1$.

The candidate from Step 2 suggests an equality certificate that vanishes at every nonzero magnitude in its support. The unique even degree-eight polynomial with value $1$ at $0$ and zeros at $|s|=4,6,8,10$ is
$$
Q(s)=\frac{(s^2-16)(s^2-36)(s^2-64)(s^2-100)}{3686400}.
$$
Every possible value of $S$ is an even integer between $-12$ and $12$. We have $Q(0)=1$. At $|s|=4,6,8,10$ the value is $0$; at $|s|=2$ all four factors are negative; and at $|s|=12$ all four are positive. Therefore
$$
Q(s)\ge \mathbf 1_{\{s=0\}}
$$
for every possible value of $S$.

Step 4: Apply the certificate to every eight-wise independent family.
Let $X_1,\ldots,X_{12}$ be any unbiased $8$-wise independent Rademacher variables and let $S=\sum_iX_i$. From Step 3,
$$
\mathbb P(S=0)\le\mathbb E Q(S).
$$
Because $Q$ has degree $8$, $8$-wise independence gives
$$
\mathbb E Q(S)=\mathbb E_U Q(S).
$$
The constructed measure $\mu_*$ is $9$-wise independent, so the same degree-eight expectation also equals $\mathbb E_{\mu_*}Q(S)$. By the support statement in Step 2, $Q(S)$ vanishes $\mu_*$-almost surely away from $S=0$, while $Q(0)=1$. Hence
$$
\mathbb E_UQ(S)=\mathbb E_{\mu_*}Q(S)=\mu_*(S=0)=\frac{297}{640}.
$$
Thus every admissible family satisfies $\mathbb P(S=0)\le297/640$, and Step 2 attains equality.

Final Answer: $\boxed{\frac{297}{640}}$

---

## Answer

$\frac{297}{640}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- finite-wise independence
- Fourier characters on the discrete cube
- probability density tilting
- polynomial majorant certificate
