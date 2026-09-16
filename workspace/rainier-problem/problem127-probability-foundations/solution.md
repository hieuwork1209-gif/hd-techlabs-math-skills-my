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
Since $h$ is monic, the right side has degree $7$. Requiring the coefficients of $x^{6}$ and $x^{5}$ in $q$ to vanish determines the remaining two parameters. Direct expansion of
$$
(1-x)\left(x^{2}-\frac45x+\frac1{10}\right)^{2}(x^{2}+\alpha x+\beta)
$$
shows that those two coefficients vanish precisely for
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
respectively. These probabilities are positive and sum to $1$. Since $u$ and $v$ satisfy $10x^{2}-8x+1=0$, every power $x^{k}$ at these two points reduces recursively by
$$
x^{k}=\frac45x^{k-1}-\frac1{10}x^{k-2}.
$$
A direct substitution for $k=1,2$ gives $\mathbb E[X]=\frac12$ and $\mathbb E[X^{2}]=\frac13$; applying the displayed recurrence then gives $\mathbb E[X^{3}]=\frac14$ and $\mathbb E[X^{4}]=\frac15$. Hence this distribution is admissible. Its support is contained in the zero set of $q(x)-x^{7}$, so $q(X)=X^{7}$ almost surely. Therefore
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
