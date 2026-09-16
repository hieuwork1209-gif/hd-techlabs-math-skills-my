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
Since $T^2$ is also measure-preserving and $T^3(x)=x$ almost everywhere,
$$
\int_0^1 T^2(x)\,x\,dx
=\int_0^1 y\,T(y)\,dy
=I.
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
Let
$$
\Omega=\{0,1,2\}^{\mathbb N}
$$
with the uniform product probability measure, and let
$$
\pi((a_k))=\sum_{k=1}^{\infty}\frac{a_k}{3^k}.
$$
The coding map $\pi$ pushes product measure forward to Lebesgue measure on $[0,1]$ and is one-to-one except on the countable set of ternary rationals.

Define
$$
\tau((a_k))=(a_k+1\pmod3)_{k\ge1}.
$$
Then $\tau$ is a measure-preserving bijection of $\Omega$ and $\tau^3$ is the identity. Remove from $\Omega$ the countable union consisting of the exceptional coding sequences and their inverse images under $\tau$ and $\tau^2$. On the remaining full-measure, $\tau$-invariant set, $\pi$ is injective throughout every three-point orbit. Hence
$$
T(\pi(\omega))=\pi(\tau\omega)
$$
defines a measurable measure-preserving map on a full-measure subset of $[0,1]$. Extend $T$ arbitrarily on the null complement; this does not change measure preservation or any almost-everywhere statement.

For every point in the full-measure set, applying the digit shift three times restores every digit, so
$$
T^3(x)=x.
$$
Moreover, in each ternary place, the three digits belonging to
$$
x,\qquad T(x),\qquad T^2(x)
$$
are a permutation of $0,1,2$. Their sum is $3$, hence
$$
\begin{aligned}
x+T(x)+T^2(x)
&=\sum_{k=1}^{\infty}\frac{3}{3^k}\\
&=\frac32.
\end{aligned}
$$
Thus the equality condition from Step 2 is attained.

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
