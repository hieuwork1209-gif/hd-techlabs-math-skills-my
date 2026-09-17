## Steps

Step 1: Translate finite order into a recurrence and its growth exponents
For $a>0$ and an integer $p\ge0$, write an orbit of
$$
F_{a,p}(x,y)=\left(y,\frac{a+y^p}{x}\right)
$$
as consecutive terms of
$$
x_{n+2}=\frac{a+x_{n+1}^p}{x_n},
\qquad x_0=x>0,
\qquad x_1=y>0.
$$
Then
$$
F_{a,p}^N(x,y)=(x_N,x_{N+1}).
$$
Fix $y>0$, put $x_0=X$, and let $X\to\infty$. For each fixed $n$, write
$$
x_n=C_nX^{e_n}(1+o(1)),
$$
with $C_n>0$. Positivity prevents leading-term cancellation, so
$$
e_{n+2}=\max(0,pe_{n+1})-e_n,
\qquad e_0=1,
\qquad e_1=0.
$$
If $F_{a,p}^N$ is the identity, then $(x_N,x_{N+1})=(X,y)$ for every $X$, so necessarily
$$
(e_N,e_{N+1})=(1,0).
$$
Thus finite order requires the exponent-pair dynamics itself to return to $(1,0)$.

Step 2: Classify the exponent regimes
If $p=0$, then
$$
e_{n+2}=-e_n,
$$
so the exponent pairs cycle as
$$
(1,0),
(0,-1),
(-1,0),
(0,1),
(1,0).
$$
Hence any identity iterate must have length divisible by $4$.

If $p=1$, then
$$
e_{n+2}=\max(0,e_{n+1})-e_n,
$$
and the exponent pairs cycle as
$$
(1,0),
(0,-1),
(-1,0),
(0,1),
(1,1),
(1,0).
$$
Hence any identity iterate must have length divisible by $5$.

Now let $p\ge2$. The first exponents are
$$
e_0=1,
\qquad e_1=0,
\qquad e_2=-1,
\qquad e_3=0,
\qquad e_4=1,
\qquad e_5=p.
$$
Since $p>1$, we have $e_5>e_4>0$. Whenever $e_{n+1}>e_n>0$,
$$
e_{n+2}=pe_{n+1}-e_n
\ge 2e_{n+1}-e_n
>e_{n+1}.
$$
Therefore the exponents are strictly increasing from $e_4$ onward. The pair $(1,0)$ never returns, so $F_{a,p}$ cannot have finite order for any $p\ge2$.

Step 3: Resolve the constant-exponent regime $p=0$
For $p=0$ the recurrence becomes
$$
x_{n+2}=\frac{a+1}{x_n}.
$$
Writing $c=a+1>0$,
$$
F_{a,0}(x,y)=\left(y,\frac{c}{x}\right),
$$
so
$$
F_{a,0}^2(x,y)=\left(\frac{c}{x},\frac{c}{y}\right),
$$
$$
F_{a,0}^3(x,y)=\left(\frac{c}{y},x\right),
$$
and
$$
F_{a,0}^4(x,y)=(x,y).
$$
The exponent-pair argument in Step 2 shows that no positive iterate of length less than $4$ can be the identity. Thus for every $a>0$,
$$
\operatorname{ord}(F_{a,0})=4.
$$

Step 4: Resolve the Lyness regime $p=1$
Suppose $p=1$ and $F_{a,1}$ has finite order. Step 2 gives
$$
N=5k
$$
for some positive integer $k$.

Fix $y>0$ and let $X\to\infty$. Directly from
$$
x_{n+2}=\frac{a+x_{n+1}}{x_n}
$$
we obtain
$$
x_2=\frac{a+y}{X},
$$
$$
x_3=\frac{a}{y}+O(X^{-1}),
$$
$$
x_4=\frac{a(y+1)}{y(a+y)}X+O(1),
$$
$$
x_5=\frac{y+1}{a+y}X+O(1),
$$
and
$$
x_6=\frac{y}{a}+O(X^{-1}).
$$
Hence one block of five iterates sends a state whose first coordinate tends to infinity and whose second coordinate tends to a positive limit $Y$ to another such state with second-coordinate limit $Y/a$. The displayed rational formulas make this asymptotic uniform when $Y$ stays in a compact subset of $(0,\infty)$, so induction gives
$$
\lim_{X\to\infty}\bigl(F_{a,1}^{5j}(X,y)\bigr)_2
=\frac{y}{a^j}
$$
for every fixed positive integer $j$.

If $F_{a,1}^{5k}$ is the identity, its second coordinate equals $y$ for every $X$. Taking $X\to\infty$ yields
$$
y=\frac{y}{a^k},
$$
so $a^k=1$. Since $a>0$,
$$
a=1.
$$

For $a=1$,
$$
x_2=\frac{1+y}{x},
$$
$$
x_3=\frac{1+x+y}{xy},
$$
$$
x_4=\frac{1+x}{y},
$$
$$
x_5=x,
\qquad
x_6=y.
$$
Thus
$$
F_{1,1}^5=\operatorname{id}.
$$
Again Step 2 rules out any smaller positive identity iterate, so
$$
\operatorname{ord}(F_{1,1})=5.
$$

Combining all regimes gives exactly the triples $(a,p,N)$ listed below, where $N$ is the least order.

Final Answer: $\boxed{\{(a,0,4):a>0\}\cup\{(1,1,5)\}}$

---

## Answer

$\{(a,0,4):a>0\}\cup\{(1,1,5)\}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- nonlinear recurrence dynamics
- tropical exponent recurrence
- asymptotic growth regimes
- finite-order dynamical systems
- periodicity obstruction
