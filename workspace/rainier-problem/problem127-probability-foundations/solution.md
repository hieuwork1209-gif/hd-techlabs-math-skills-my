## Steps

Step 1: Derive the contact nodes forced by a sharp degree-four moment certificate
For any polynomial $q$ of degree at most $4$, the hypotheses determine $\mathbb E[q(X)]$. Thus an upper bound for $\mathbb E[X^{7}]$ follows from any quartic $q$ with $q(x)\geq x^{7}$ on $[0,1]$. At equality, an extremizing measure must be supported where $q(x)-x^{7}=0$. Because an interior zero of a nonnegative polynomial has even multiplicity, the degree-seven difference naturally allows two double interior contacts together with one contact at the endpoint $1$.

Write the two interior contacts as the roots of a monic quadratic
$$
h(x)=x^{2}+Ax+B.
$$
If a three-point measure supported at those roots and at $1$ reproduces the moments through degree $4$, then every polynomial $(1-x)h(x)r(x)$ with $\deg r\leq1$ has zero expectation under that measure and hence must also have zero integral against the prescribed moment functional. Therefore $h$ is forced by
$$
\int_{0}^{1}(1-x)h(x)\,dx=0,
\qquad
\int_{0}^{1}x(1-x)h(x)\,dx=0.
$$
Expanding gives
$$
\frac{1}{12}+\frac{A}{6}+\frac{B}{2}=0,
\qquad
\frac{1}{20}+\frac{A}{12}+\frac{B}{6}=0.
$$
Solving yields $A=-\frac45$ and $B=\frac1{10}$, so
$$
h(x)=x^{2}-\frac45x+\frac1{10},
$$
with roots
$$
u=\frac{4-\sqrt6}{10},\qquad v=\frac{4+\sqrt6}{10}.
$$

Step 2: Construct the global quartic majorant
To obtain a degree-four majorant with exactly these contacts, set
$$
q(x)-x^{7}=(1-x)h(x)^{2}(x^{2}+\alpha x+\beta).
$$
Since $h$ is monic, the coefficient of $x^{7}$ on the right is $-1$, cancelling the $x^{7}$ term of $q$. Expanding only the next two coefficients gives
$$
[x^{6}]q=\frac{13}{5}-\alpha,
\qquad
[x^{5}]q=\frac{13}{5}\alpha-\beta-\frac{61}{25}.
$$
Thus the requirement $\deg q\leq4$ forces
$$
\alpha=\frac{13}{5},\qquad \beta=\frac{108}{25}.
$$
Hence
$$
q(x)-x^{7}
=\frac{(1-x)(10x^{2}-8x+1)^{2}(25x^{2}+65x+108)}{2500}.
$$
The quadratic $25x^{2}+65x+108$ has discriminant $65^{2}-4\cdot25\cdot108=-6575<0$ and positive leading coefficient. Therefore it is positive for all real $x$, so $q(x)\geq x^{7}$ on $[0,1]$. Expanding the quartic gives
$$
q(x)=\frac{736}{125}x^{4}-\frac{20277}{2500}x^{3}+\frac{486}{125}x^{2}-\frac{1771}{2500}x+\frac{27}{625}.
$$

Step 3: Evaluate the sharp upper bound from the prescribed moments
Using $\mathbb E[X]=\frac12$, $\mathbb E[X^{2}]=\frac13$, $\mathbb E[X^{3}]=\frac14$, and $\mathbb E[X^{4}]=\frac15$, the majorant gives
$$
\mathbb E[X^{7}]\leq\mathbb E[q(X)].
$$
Substituting the four moments,
$$
\mathbb E[q(X)]
=\frac{736}{125}\cdot\frac15
-\frac{20277}{2500}\cdot\frac14
+\frac{486}{125}\cdot\frac13
-\frac{1771}{2500}\cdot\frac12
+\frac{27}{625}
=\frac{1349}{10000}.
$$
Thus every admissible random variable satisfies
$$
\mathbb E[X^{7}]\leq\frac{1349}{10000}.
$$

Step 4: Construct an admissible distribution attaining the bound
Let $X$ take the three values
$$
u=\frac{4-\sqrt6}{10},\qquad v=\frac{4+\sqrt6}{10},\qquad 1
$$
with probabilities
$$
\frac49-\frac{\sqrt6}{36},\qquad
\frac49+\frac{\sqrt6}{36},\qquad
\frac19,
$$
respectively. These probabilities are positive and sum to $1$. Direct substitution gives the contributions of the two interior masses
$$
\left(\frac49-\frac{\sqrt6}{36}\right)u+
\left(\frac49+\frac{\sqrt6}{36}\right)v=\frac7{18},
$$
$$
\left(\frac49-\frac{\sqrt6}{36}\right)u^{2}+
\left(\frac49+\frac{\sqrt6}{36}\right)v^{2}=\frac29.
$$
Adding the mass $1/9$ at $1$ yields $\mathbb E[X]=\frac12$ and $\mathbb E[X^{2}]=\frac13$.

For the two interior nodes, $10x^{2}-8x+1=0$, so their contributions satisfy
$$
x^{k}=\frac45x^{k-1}-\frac1{10}x^{k-2}.
$$
The atom of mass $1/9$ at $1$ contributes the correction
$$
\frac19\left(1-\frac45+\frac1{10}\right)=\frac1{30}.
$$
Therefore, for $k\geq2$,
$$
\mathbb E[X^{k}]=\frac45\mathbb E[X^{k-1}]-\frac1{10}\mathbb E[X^{k-2}]+\frac1{30}.
$$
Using the already verified first two moments gives
$$
\mathbb E[X^{3}]=\frac45\cdot\frac13-\frac1{10}\cdot\frac12+\frac1{30}=\frac14,
$$
$$
\mathbb E[X^{4}]=\frac45\cdot\frac14-\frac1{10}\cdot\frac13+\frac1{30}=\frac15.
$$
Hence this distribution is admissible. Its support is contained in the zero set of $q(x)-x^{7}$, so $q(X)=X^{7}$ almost surely. Therefore
$$
\mathbb E[X^{7}]=\mathbb E[q(X)]=\frac{1349}{10000}.
$$
The upper bound is attained and is therefore the required maximum.

Final Answer: $\boxed{\frac{1349}{10000}}$

---

## Answer

$\frac{1349}{10000}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- truncated moment problems
- polynomial majorants
- extremal distributions
- quadrature exactness
