## Steps

Step 1: Symmetrize the three pair products
Let $\lambda$ denote Lebesgue measure and let $T:[0,1]\to[0,1]$ be measurable, measure-preserving, and satisfy
$$
T^3(x)=x
$$
for almost every $x$.
Set
$$
I=\int_0^1 x\,T(x)\,dx.
$$
Because $T$ preserves Lebesgue measure,
$$
\int_0^1 T(x)\,T^2(x)\,dx
=\int_0^1 y\,T(y)\,dy
=I.
$$
Applying the same change of variables with $T^2$ gives
$$
\int_0^1 T^2(x)\,x\,dx=I.
$$
Thus all three pairwise products along an orbit have the same integral.

Step 2: Convert the problem to a quadratic lower bound
Define
$$
S(x)=x+T(x)+T^2(x).
$$
Since $T$ and $T^2$ are measure-preserving,
$$
\int_0^1 S(x)\,dx
=3\int_0^1 x\,dx
=\frac32.
$$
Also
$$
\begin{aligned}
\int_0^1 S(x)^2\,dx
&=\int_0^1\bigl(x^2+T(x)^2+T^2(x)^2\bigr)\,dx\\
&\quad+2\int_0^1\bigl(xT(x)+T(x)T^2(x)+T^2(x)x\bigr)\,dx\\
&=3\int_0^1x^2\,dx+6I\\
&=1+6I.
\end{aligned}
$$
By Cauchy-Schwarz on the unit interval,
$$
\int_0^1 S(x)^2\,dx\ge\left(\int_0^1S(x)\,dx\right)^2=\frac94.
$$
Therefore
$$
1+6I\ge\frac94,
$$
so
$$
I\ge\frac5{24}.
$$
Equality can hold only when
$$
S(x)=\frac32
$$
for almost every $x$.

Step 3: Build a measure-preserving period-three map attaining equality
Ignore the countable set of points with two ternary expansions. On the remaining full-measure set, write
$$
x=\sum_{k=1}^{\infty}\frac{a_k}{3^k},
\qquad a_k\in\{0,1,2\}.
$$
Define $T$ by adding $1$ modulo $3$ to every ternary digit:
$$
T(x)=\sum_{k=1}^{\infty}\frac{a_k+1\pmod3}{3^k}.
$$
More formally, identify almost every point of $[0,1]$ with the product space $\{0,1,2\}^{\mathbb N}$ equipped with the uniform product measure. Coordinatewise addition by $1$ modulo $3$ is a measure-preserving bijection of that product space, so the induced map on $[0,1]$ is measure-preserving modulo a null set. Extend it arbitrarily on the exceptional null set.

Applying the digit shift three times restores every digit, hence
$$
T^3(x)=x
$$
for almost every $x$.
For every nonexceptional $x$, the three digits appearing in the same position of
$$
x,\qquad T(x),\qquad T^2(x)
$$
are a permutation of $0,1,2$. Their sum is therefore $3$ in every ternary place, so
$$
\begin{aligned}
x+T(x)+T^2(x)
&=\sum_{k=1}^{\infty}\frac{3}{3^k}\\
&=\frac32.
\end{aligned}
$$
Hence the equality condition from Step 2 is attained.

Step 4: Evaluate the minimum
For the transformation from Step 3,
$$
\int_0^1S(x)^2\,dx=\frac94.
$$
Using
$$
\int_0^1S(x)^2\,dx=1+6I,
$$
we obtain
$$
I=\frac5{24}.
$$
Together with the lower bound from Step 2, this proves that the minimum is exactly
$$
\frac5{24}.
$$

Final Answer: $\boxed{\frac5{24}}$

---

## Answer

$\frac5{24}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- measure-preserving transformations
- periodic dynamical systems
- orbit symmetrization
- Cauchy-Schwarz equality
- ternary digit construction
