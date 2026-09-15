## Steps

Step 1: Convert 6-wise independence into fixed moments
Let $\varepsilon_i=2X_i-1\in\{-1,1\}$ and
$$
Y=\frac12\sum_{i=1}^{12}\varepsilon_i=S-6,
$$
where $S=\sum_{i=1}^{12}X_i$. Since the variables are unbiased and 6-wise independent, every product of at most six distinct $\varepsilon_i$ has the same expectation as for independent Rademacher variables. Hence the moments of $Y$ through degree six are the corresponding moments for one half of a sum of twelve independent Rademacher variables.

Writing $R=2Y=\sum_{i=1}^{12}\varepsilon_i$, only index multiplicity patterns in which every multiplicity is even contribute. Therefore
$$
E(R^2)=12,
$$
$$
E(R^4)=12+6\binom{12}{2}=408,
$$
and, using the patterns $6$, $4+2$, and $2+2+2$,
$$
E(R^6)=12+15\cdot12\cdot11+90\binom{12}{3}=21792.
$$
Thus
$$
E(Y^2)=3,\qquad E(Y^4)=\frac{51}{2},\qquad E(Y^6)=\frac{681}{2}.
$$
The event that all twelve bits are equal is exactly $\{|Y|=6\}$.

Step 2: Derive a sharp polynomial certificate on the discrete support
Because $Y$ is an integer with $|Y|\leq6$, the variable $z=Y^2$ takes values
$$
0,1,4,9,16,25,36.
$$
The available information fixes $E(z)$, $E(z^2)$, and $E(z^3)$, so an upper certificate for the endpoint event should be a cubic polynomial in $z$. To be sharp, such a certificate should vanish at interior support values that can carry mass in an extremizer. A cubic with positive leading coefficient can be nonnegative on the discrete support while changing sign only across gaps containing no support point. Taking zeros at $0,4,9$ does exactly this: the only interval on which the sign is negative is $(4,9)$, which contains no allowed value of $z$. Normalizing the value at $z=36$ to be $1$ forces
$$
Q(z)=\frac{z(z-4)(z-9)}{36\cdot32\cdot27}=\frac{z(z-4)(z-9)}{31104}.
$$
Indeed, $Q(z)\geq0$ for every allowed $z<36$, and $Q(36)=1$. Hence on the entire support,
$$
\mathbf{1}_{\{z=36\}}\leq Q(z).
$$

Step 3: Evaluate the certificate to obtain the universal upper bound
Using the moments from Step 1,
$$
\begin{aligned}
P(|Y|=6)
&\leq E\bigl[Q(Y^2)\bigr]\\
&=\frac{E(Y^6)-13E(Y^4)+36E(Y^2)}{31104}\\
&=\frac{\frac{681}{2}-13\cdot\frac{51}{2}+108}{31104}\\
&=\frac{117}{31104}
=\frac{13}{3456}.
\end{aligned}
$$
So no admissible family can have probability larger than $13/3456$ that all twelve variables agree.

Step 4: Construct an admissible family attaining the bound
Define a symmetric integer-valued random variable $Y$ by
$$
P(Y=0)=\frac{77}{144},\qquad
P(Y=\pm2)=\frac{33}{256}\ \text{for each sign},
$$
$$
P(Y=\pm3)=\frac{11}{108}\ \text{for each sign},\qquad
P(Y=\pm6)=\frac{13}{6912}\ \text{for each sign}.
$$
These probabilities sum to $1$. Their even moments are
$$
E(Y^2)=4\cdot\frac{33}{128}+9\cdot\frac{11}{54}+36\cdot\frac{13}{3456}=3,
$$
$$
E(Y^4)=16\cdot\frac{33}{128}+81\cdot\frac{11}{54}+1296\cdot\frac{13}{3456}=\frac{51}{2},
$$
$$
E(Y^6)=64\cdot\frac{33}{128}+729\cdot\frac{11}{54}+46656\cdot\frac{13}{3456}=\frac{681}{2}.
$$
All odd moments through degree six vanish by symmetry. Set $S=6+Y$. Conditional on $S=s$, choose uniformly a subset of $\{1,\ldots,12\}$ of size $s$, and let $X_i$ be its membership indicators.

For $0\leq j\leq6$, every polynomial in $S$ of degree at most $j$ has the same expectation as under $\operatorname{Bin}(12,1/2)$ because $S-6=Y$ has matching moments through degree six. In particular,
$$
E\bigl[(S)_j\bigr]=\frac{(12)_j}{2^j}.
$$
For any distinct indices $i_1,\ldots,i_j$,
$$
P(X_{i_1}=\cdots=X_{i_j}=1)
=E\left[\frac{(S)_j}{(12)_j}\right]
=2^{-j}.
$$
Inclusion-exclusion then gives probability $2^{-j}$ for every prescribed $0$-$1$ pattern on any $j\leq6$ coordinates, so the constructed variables are unbiased and 6-wise independent. Finally,
$$
P(X_1=\cdots=X_{12})=P(|Y|=6)=2\cdot\frac{13}{6912}=\frac{13}{3456},
$$
which attains the upper bound.

Final Answer: $\boxed{\frac{13}{3456}}$

---

## Answer

$\frac{13}{3456}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- k-wise independence
- Rademacher moment method
- polynomial majorization certificate
- truncated moment problem
- exchangeable Bernoulli construction
