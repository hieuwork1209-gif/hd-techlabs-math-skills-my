## Steps

Step 1: Translate finite order into a recurrence
For $a>0$, write an orbit of
$$
F_a(x,y)=\left(y,\frac{a+y}{x}\right)
$$
as consecutive terms of the recurrence
$$
x_{n+2}=\frac{a+x_{n+1}}{x_n},
\qquad x_0=x>0,
\qquad x_1=y>0.
$$
Then
$$
F_a^N(x,y)=(x_N,x_{N+1}).
$$
Thus $F_a^N$ is the identity on $(0,\infty)^2$ exactly when every positive initial pair produces an $N$-periodic recurrence.

Step 2: Use growth exponents at infinity to force the period to be a multiple of five
Fix $y>0$ and set $x_0=X$, $x_1=y$, with $X\to\infty$. For each fixed $n$, write
$$
x_n=C_nX^{e_n}(1+o(1)),
$$
where $C_n>0$. Because every quantity is positive, no leading-term cancellation can occur. From
$$
x_{n+2}=\frac{a+x_{n+1}}{x_n}
$$
the exponents satisfy
$$
e_{n+2}=\max(0,e_{n+1})-e_n.
$$
Starting from
$$
e_0=1,
\qquad
e_1=0,
$$
we obtain the cycle of exponent pairs
$$
(1,0),
(0,-1),
(-1,0),
(0,1),
(1,1),
(1,0).
$$
Because the exponent recurrence is deterministic, this five-step cycle then repeats. Hence the pair $(1,0)$ occurs exactly when the index is a multiple of $5$.

If $F_a^N$ were the identity, then for every fixed $y>0$,
$$
x_N=X,
\qquad
x_{N+1}=y.
$$
Their exponents in $X$ are therefore $(1,0)$, so
$$
5\mid N.
$$
Write
$$
N=5k.
$$

Step 3: Compute the five-step drift and force the parameter
For fixed $y>0$ and $X\to\infty$, the first few terms are
$$
x_2=\frac{a+y}{X},
$$
$$
x_3=\frac{aX+a+y}{Xy}
=\frac{a}{y}+O(X^{-1}),
$$
$$
x_4
=\frac{a+x_3}{x_2}
=\frac{a(y+1)}{y(a+y)}X+O(1),
$$
$$
x_5
=\frac{a+x_4}{x_3}
=\frac{y+1}{a+y}X+O(1),
$$
and
$$
x_6
=\frac{a+x_5}{x_4}
=\frac{y}{a}+O(X^{-1}).
$$
Therefore
$$
F_a^5(X,y)
=\left(\frac{y+1}{a+y}X+O(1),\frac{y}{a}+O(X^{-1})\right).
$$
The displayed rational formulas show that these estimates are uniform when $y$ ranges over a compact subset of $(0,\infty)$. In particular, if the first coordinate tends to infinity and the second tends to a positive limit $Y$, then after five more iterates the first coordinate still tends to infinity and the second tends to $Y/a$.

Inducting over five-step blocks therefore gives, for every fixed positive integer $j$,
$$
\lim_{X\to\infty}\bigl(F_a^{5j}(X,y)\bigr)_2
=\frac{y}{a^j}.
$$

Now suppose $F_a^{5k}$ is the identity. Its second coordinate equals $y$ for every $X$, so taking $X\to\infty$ yields
$$
y=\frac{y}{a^k}.
$$
Since $y>0$ and $a>0$,
$$
a^k=1,
$$
which forces
$$
a=1.
$$
Thus no parameter other than $a=1$ can give a finite-order map.

Step 4: Verify the five-cycle at the remaining parameter
Set $a=1$. Starting from $x_0=x$ and $x_1=y$,
$$
x_2=\frac{1+y}{x},
$$
$$
x_3=\frac{1+x+y}{xy},
$$
$$
x_4
=\frac{1+x_3}{x_2}
=\frac{1+x}{y},
$$
$$
x_5
=\frac{1+x_4}{x_3}
=x,
$$
and
$$
x_6
=\frac{1+x_5}{x_4}
=y.
$$
Hence
$$
F_1^5(x,y)=(x,y)
$$
for every $x,y>0$.

The exponent-pair argument from Step 2 shows that an identity iterate must have exponent length divisible by $5$, so no positive iterate smaller than $5$ can be the identity. Therefore the order of $F_1$ is exactly $5$.

Final Answer: $\boxed{(1,5)}$

---

## Answer

$(1,5)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonlinear recurrence dynamics
- asymptotic growth exponents
- tropical exponent recurrence
- finite-order dynamical systems
- periodicity obstruction
