## Steps

Step 1: Express the correlation through the two unknown higher moments
Set
$$
a=\mathbb E[X^{5}],\qquad b=\mathbb E[X^{6}].
$$
The prescribed moments give
$$
\operatorname{Var}(X^{2})=\frac15-\frac19=\frac4{45},
$$
$$
\operatorname{Cov}(X^{2},X^{3})=a-\frac13\cdot\frac14=a-\frac1{12},
$$
and
$$
\operatorname{Var}(X^{3})=b-\frac1{16}.
$$
Therefore
$$
\rho:=\operatorname{Corr}(X^{2},X^{3})
=\frac{a-\frac1{12}}{\sqrt{\frac4{45}\left(b-\frac1{16}\right)}}.
$$
Since $x\mapsto x^{3}$ is injective on $[0,1]$, $\operatorname{Var}(X^{3})=0$ would force $X$ to be constant, contradicting $\operatorname{Var}(X^{2})=4/45$. Thus the denominator is positive.

Step 2: Obtain the sharp lower bound on the fifth moment from a weighted square
For real $u,v$, the support condition $X\in[0,1]$ implies
$$
0\leq\mathbb E\left[X\left(X^{2}+uX+v\right)^{2}\right].
$$
Expanding with the known moments gives
$$
0\leq a+\frac{2u}{5}+\frac{u^{2}+2v}{4}+\frac{2uv}{3}+\frac{v^{2}}{2}.
$$
To make this inequality as strong as possible, minimize the known quadratic part in $u,v$. Its partial derivatives are
$$
\frac25+\frac{u}{2}+\frac{2v}{3}=0,
\qquad
\frac12+\frac{2u}{3}+v=0.
$$
Solving gives
$$
u=-\frac65,\qquad v=\frac3{10}.
$$
Substitution yields
$$
0\leq a-\frac{33}{200},
$$
so
$$
a\geq\frac{33}{200}>\frac1{12}.
$$
In particular the numerator of $\rho$ is positive.

Step 3: Obtain the sharp lower bound on the sixth moment for a fixed fifth moment
For a quadratic polynomial
$$
p(x)=A+Bx+Cx^{2},
$$
we have
$$
0\leq\mathbb E\left[(X^{3}-p(X))^{2}\right].
$$
For fixed $a$, the strongest lower bound on $b$ is obtained by choosing the least-squares quadratic approximation to $X^{3}$. The normal equations
$$
\mathbb E[X^{3}-p(X)]=0,
$$
$$
\mathbb E[X(X^{3}-p(X))]=0,
$$
$$
\mathbb E[X^{2}(X^{3}-p(X))]=0
$$
become
$$
A+\frac{B}{2}+\frac{C}{3}=\frac14,
$$
$$
\frac{A}{2}+\frac{B}{3}+\frac{C}{4}=\frac15,
$$
$$
\frac{A}{3}+\frac{B}{4}+\frac{C}{5}=a.
$$
Solving gives
$$
A=30a-\frac{99}{20},\qquad
B=\frac{147}{5}-180a,\qquad
C=180a-\frac{57}{2}.
$$
The normal equations imply $\mathbb E[p(X)^{2}]=\mathbb E[X^{3}p(X)]$, so
$$
\mathbb E[(X^{3}-p(X))^{2}]
=b-\mathbb E[X^{3}p(X)].
$$
Using $\mathbb E[X^{3}]=1/4$, $\mathbb E[X^{4}]=1/5$, and $\mathbb E[X^{5}]=a$,
$$
\mathbb E[X^{3}p(X)]
=\frac{A}{4}+\frac{B}{5}+Ca
=180a^{2}-57a+\frac{1857}{400}.
$$
Hence
$$
b\geq180a^{2}-57a+\frac{1857}{400}.
$$

Step 4: Optimize the coupled moment bounds
Because $a>1/12$, the bound from Step 3 gives
$$
\rho^{2}
\leq
\frac{\left(a-\frac1{12}\right)^{2}}
{\frac4{45}\left(180a^{2}-57a+\frac{1857}{400}-\frac1{16}\right)}
=:F(a).
$$
Simplifying,
$$
F(a)=\frac{125(12a-1)^{2}}{32(9000a^{2}-2850a+229)}.
$$
Differentiation gives
$$
F'(a)
=-\frac{3375(12a-1)(300a-49)}{16(9000a^{2}-2850a+229)^{2}}.
$$
For $a\geq33/200$, both $12a-1$ and $300a-49$ are positive, so $F$ is strictly decreasing on the entire feasible range. Therefore
$$
\rho^{2}\leq F\left(\frac{33}{200}\right)=\frac{2401}{2416}
=\left(\frac{49}{4\sqrt{151}}\right)^{2}.
$$
Thus
$$
\rho\leq\frac{49}{4\sqrt{151}}.
$$

Step 5: Construct a distribution attaining the bound
Let
$$
\alpha=\frac{6-\sqrt6}{10},\qquad
\beta=\frac{6+\sqrt6}{10},
$$
and define $X$ by
$$
\mathbb P(X=0)=\frac19,
$$
$$
\mathbb P(X=\alpha)=\frac49+\frac{\sqrt6}{36},
\qquad
\mathbb P(X=\beta)=\frac49-\frac{\sqrt6}{36}.
$$
The three probabilities are positive and sum to $1$. Substitution gives
$$
\mathbb E[X]=\frac12,
\qquad
\mathbb E[X^{2}]=\frac13.
$$
Also $\alpha$ and $\beta$ are the roots of
$$
10x^{2}-12x+3=0.
$$
After multiplying this relation by $x^{k-2}$, the atom at $0$ contributes zero for every $k\geq3$, so the moments satisfy
$$
\mathbb E[X^{k}]
=\frac65\mathbb E[X^{k-1}]-\frac3{10}\mathbb E[X^{k-2}]
\qquad(k\geq3).
$$
Starting from the displayed first two moments,
$$
\mathbb E[X^{3}]=\frac14,
\qquad
\mathbb E[X^{4}]=\frac15,
$$
so the distribution is admissible. The same recurrence gives
$$
a=\mathbb E[X^{5}]=\frac{33}{200},
\qquad
b=\mathbb E[X^{6}]=\frac{69}{500}.
$$
Therefore
$$
\operatorname{Cov}(X^{2},X^{3})=\frac{49}{600},
$$
$$
\operatorname{Var}(X^{2})=\frac4{45},
\qquad
\operatorname{Var}(X^{3})=\frac{151}{2000},
$$
and hence
$$
\operatorname{Corr}(X^{2},X^{3})
=\frac{49/600}{\sqrt{(4/45)(151/2000)}}
=\frac{49}{4\sqrt{151}}.
$$
Thus the upper bound is attained.

Final Answer: $\boxed{\frac{49}{4\sqrt{151}}}$

---

## Answer

$\frac{49}{4\sqrt{151}}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- truncated moment inequalities
- least squares projection
- correlation optimization
- extremal distributions
