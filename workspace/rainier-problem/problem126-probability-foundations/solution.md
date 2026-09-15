## Steps

Step 1: Convert 6-wise independence into fixed centered moments
Let
$$
\varepsilon_i=2X_i-1\in\{-1,1\},\qquad S=\sum_{i=1}^{12}X_i,\qquad Y=S-6=\frac12\sum_{i=1}^{12}\varepsilon_i.
$$
Because the variables are unbiased and every subfamily of at most six variables is independent, every product of at most six distinct $\varepsilon_i$ has the same expectation as for independent Rademacher variables. Thus the moments of $R=2Y=\sum_{i=1}^{12}\varepsilon_i$ through degree six are the independent Rademacher moments.

For the even moments, only index multiplicity patterns with all multiplicities even contribute. Hence
$$
E(R^2)=12,
$$
$$
E(R^4)=12+6\binom{12}{2}=408,
$$
and, from the patterns $6$, $4+2$, and $2+2+2$,
$$
E(R^6)=12+15\cdot12\cdot11+90\binom{12}{3}=21792.
$$
Therefore
$$
E(Y^2)=3,\qquad E(Y^4)=\frac{51}{2},\qquad E(Y^6)=\frac{681}{2}.
$$
The event that all twelve bits agree is $\{|Y|=6\}$, while the event that exactly one bit differs from the other eleven is $\{|Y|=5\}$.

Step 2: Derive a cubic dual certificate and identify the regime transition
Since $Y$ is an integer with $|Y|\leq6$, the variable $z=Y^2$ takes values
$$
0,1,4,9,16,25,36.
$$
The fixed moments from Step 1 determine the expectation of every cubic polynomial in $z$. Thus a natural dual bound for the two endpoint masses is a cubic majorant on this seven-point support. To make such a majorant sharp, it should have support contact points where it vanishes. A cubic with positive leading coefficient is negative only between its second and third real roots, so its negative interval must lie in a gap containing no allowed support value. Choosing the contact roots $0,4,9$ places that interval in the empty gap $(4,9)$ and gives the nonnegative support polynomial $z(z-4)(z-9)$. Normalizing its value at $z=36$ to be $1$ forces
$$
Q(z)=\frac{z(z-4)(z-9)}{36\cdot32\cdot27}=\frac{z(z-4)(z-9)}{31104}.
$$
Indeed, $Q(z)\geq0$ at every allowed support value, and
$$
Q(36)=1,\qquad Q(25)=\frac{25\cdot21\cdot16}{31104}=\frac{175}{648}.
$$
Put $\tau=175/648$. If $0\leq\lambda\leq\tau$, then on every allowed $z$,
$$
\mathbf{1}_{\{z=36\}}+\lambda\mathbf{1}_{\{z=25\}}\leq Q(z).
$$
If $\lambda\geq\tau$, then
$$
\mathbf{1}_{\{z=36\}}+\lambda\mathbf{1}_{\{z=25\}}\leq \frac{\lambda}{\tau}Q(z),
$$
because the right side equals $\lambda$ at $z=25$, is at least $1$ at $z=36$, and is nonnegative elsewhere.

Using the moments from Step 1,
$$
E[Q(Y^2)]
=\frac{E(Y^6)-13E(Y^4)+36E(Y^2)}{31104}
=\frac{\frac{681}{2}-13\cdot\frac{51}{2}+108}{31104}
=\frac{13}{3456}.
$$
Therefore every admissible family satisfies
$$
P(|Y|=6)+\lambda P(|Y|=5)
\leq
\max\left\{\frac{13}{3456},\frac{\lambda}{\tau}\frac{13}{3456}\right\}
=
\max\left\{\frac{13}{3456},\frac{39\lambda}{2800}\right\}.
$$

Step 3: Use the certificate contact sets to construct extremal centered laws
For $0\leq\lambda<\tau$, equality in the first pointwise majorization can occur only at $z\in\{0,4,9,36\}$. Hence a sharp centered law should be supported on $Y\in\{0,\pm2,\pm3,\pm6\}$. Solving the normalization and three even-moment equations on this contact set gives the symmetric law
$$
P(Y_A=0)=\frac{77}{144},\qquad
P(Y_A=\pm2)=\frac{33}{256}\ \text{for each sign},
$$
$$
P(Y_A=\pm3)=\frac{11}{108}\ \text{for each sign},\qquad
P(Y_A=\pm6)=\frac{13}{6912}\ \text{for each sign}.
$$
The total mass and the three required moments are verified by
$$
\frac{77}{144}+\frac{33}{128}+\frac{11}{54}+\frac{13}{3456}=1,
$$
$$
4\cdot\frac{33}{128}+9\cdot\frac{11}{54}+36\cdot\frac{13}{3456}=3,
$$
$$
16\cdot\frac{33}{128}+81\cdot\frac{11}{54}+1296\cdot\frac{13}{3456}=\frac{51}{2},
$$
$$
64\cdot\frac{33}{128}+729\cdot\frac{11}{54}+46656\cdot\frac{13}{3456}=\frac{681}{2}.
$$
Its odd moments vanish by symmetry, and
$$
P(|Y_A|=6)+\lambda P(|Y_A|=5)=\frac{13}{3456}.
$$

For $\lambda>\tau$, equality in the scaled majorization can occur only at $z\in\{0,4,9,25\}$. Solving the same four moment equations on this contact set gives
$$
P(Y_B=0)=\frac{99}{200},\qquad
P(Y_B=\pm2)=\frac{99}{560}\ \text{for each sign},
$$
$$
P(Y_B=\pm3)=\frac{11}{160}\ \text{for each sign},\qquad
P(Y_B=\pm5)=\frac{39}{5600}\ \text{for each sign}.
$$
Again the normalization and moments are explicit:
$$
\frac{99}{200}+\frac{99}{280}+\frac{11}{80}+\frac{39}{2800}=1,
$$
$$
4\cdot\frac{99}{280}+9\cdot\frac{11}{80}+25\cdot\frac{39}{2800}=3,
$$
$$
16\cdot\frac{99}{280}+81\cdot\frac{11}{80}+625\cdot\frac{39}{2800}=\frac{51}{2},
$$
$$
64\cdot\frac{99}{280}+729\cdot\frac{11}{80}+15625\cdot\frac{39}{2800}=\frac{681}{2}.
$$
Thus
$$
P(|Y_B|=6)+\lambda P(|Y_B|=5)=\frac{39\lambda}{2800}.
$$
At $\lambda=\tau$, both constructions attain the same value.

Step 4: Lift the centered laws to 6-wise independent Bernoulli families
For either $Y=Y_A$ or $Y=Y_B$, set $S=6+Y$. Conditional on $S=s$, choose uniformly a subset of $\{1,\ldots,12\}$ of size $s$, and let $X_i$ be its membership indicators.

The centered moments of $S-6$ through degree six agree with those of $\operatorname{Bin}(12,1/2)-6$, so every polynomial in $S$ of degree at most six has the same expectation as under $\operatorname{Bin}(12,1/2)$. In particular, for $0\leq j\leq6$,
$$
E[(S)_j]=\frac{(12)_j}{2^j}.
$$
For distinct indices $i_1,\ldots,i_j$,
$$
P(X_{i_1}=\cdots=X_{i_j}=1)
=E\left[\frac{(S)_j}{(12)_j}\right]
=2^{-j}.
$$
By inclusion-exclusion, every prescribed $0$-$1$ pattern on any $j\leq6$ coordinates has probability $2^{-j}$. Thus the constructed variables are unbiased and 6-wise independent.

The $Y_A$ construction attains $13/3456$, and the $Y_B$ construction attains $39\lambda/2800$. Together with Step 2, this proves the maximum for every $\lambda\geq0$.

Final Answer: $\boxed{\max\left\{\frac{13}{3456},\frac{39\lambda}{2800}\right\}}$

---

## Answer

$\max\left\{\frac{13}{3456},\frac{39\lambda}{2800}\right\}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- k-wise independence
- Rademacher moment method
- polynomial majorization certificate
- truncated moment problem
- exchangeable Bernoulli construction
