## Steps

Step 1: Encode the prescribed moments as a linear functional

Let $L$ be the linear functional on polynomials of degree at most $9$ defined by
$$
L(x^k)=\frac1{k+1}
\qquad(0\le k\le 8),
$$
and
$$
L(x^9)=\frac{35281}{352800}.
$$
Every admissible probability law $\mu$ on $[0,1]$ satisfies
$$
\int p(x)\,d\mu(x)=L(p)
$$
for every polynomial $p$ of degree at most $9$.

We must maximize
$$
\int_0^1\frac{d\mu(x)}{2-x}.
$$

Step 2: Find the quartic controlling the extremal support

Set
$$
Q(x)=420x^4-798x^3+497x^2-113x+7.
$$
A direct substitution of the prescribed moments gives
$$
L\bigl(x^{j+1}(1-x)Q(x)\bigr)=0
\qquad(j=0,1,2,3).
\tag{1}
$$
Indeed, each expression is a linear combination of $L(x^k)$ with $k\le9$, and all four simplify to zero.

The polynomial $Q$ has four simple roots in $(0,1)$. It is enough to note the sign changes
$$
Q(0)=7,
\qquad
Q\!\left(\frac1{10}\right)=-\frac{43}{500},
$$
$$
Q\!\left(\frac3{10}\right)=-\frac{157}{500},
\qquad
Q\!\left(\frac13\right)=\frac5{27},
$$
$$
Q\!\left(\frac35\right)=\frac{23}{125},
\qquad
Q\!\left(\frac58\right)=-\frac{227}{1024},
$$
$$
Q\!\left(\frac45\right)=-\frac{233}{125},
\qquad
Q\!\left(\frac78\right)=\frac{245}{1024}.
$$
Thus there is one root in each of the four disjoint intervals
$$
\left(0,\frac1{10}\right),
\quad
\left(\frac3{10},\frac13\right),
\quad
\left(\frac35,\frac58\right),
\quad
\left(\frac45,\frac78\right).
$$
Since $Q$ has degree $4$, these are exactly its four roots; denote them by
$$
r_1<r_2<r_3<r_4.
$$

Step 3: Build a sharp degree-$9$ majorant

One has
$$
Q(2)=2105.
$$
Define
$$
P(x)
=\frac{1+\dfrac{x(1-x)Q(x)^2}{2\cdot2105^2}}{2-x}.
\tag{2}
$$
At $x=2$, the numerator in (2) is
$$
1+\frac{2(1-2)Q(2)^2}{2Q(2)^2}=0,
$$
so $P$ is a polynomial, of degree $9$. Moreover, for $0\le x\le1$,
$$
P(x)-\frac1{2-x}
=\frac{x(1-x)Q(x)^2}{2\cdot2105^2(2-x)}\ge0.
\tag{3}
$$

For an explicit moment evaluation, polynomial division gives
$$
P(x)=\frac1{8862050}\Bigl(
176400x^9-493920x^8+736764x^7-468888x^6
+383593x^5+210455x^4
$$
$$
\hspace{35mm}
+564131x^3+1106953x^2+2215537x+4431025
\Bigr).
\tag{4}
$$
Therefore the prescribed moments imply
$$
L(P)=\frac{58363}{84200}.
\tag{5}
$$
Combining (3) and (5), every admissible law satisfies
$$
\mathbb E\!\left[\frac1{2-X}\right]
\le \frac{58363}{84200}.
\tag{6}
$$

Step 4: Construct a probability law attaining the bound

Use the six nodes
$$
0,r_1,r_2,r_3,r_4,1.
$$
Let $\ell_i$ be their Lagrange basis polynomials, and define weights
$$
w_i=L(\ell_i).
$$
We claim the resulting quadrature rule
$$
L(f)=\sum_{i=0}^5w_i f(r_i)
\tag{7}
$$
is exact for every polynomial $f$ of degree at most $9$, where $r_0=0$ and $r_5=1$.

Indeed, let $R$ be the degree-at-most-$5$ interpolant of $f$ at the six nodes. Since
$$
x(1-x)Q(x)
$$
vanishes at all six nodes, one has
$$
f(x)-R(x)=x(1-x)Q(x)s(x)
$$
for some polynomial $s$ of degree at most $3$. Equation (1) gives
$$
L(f-R)=0,
$$
which proves (7).

It remains to show the weights are positive. For an interior node $r_i$, define
$$
g_i(x)=x(1-x)\left(\frac{Q(x)}{x-r_i}\right)^2.
$$
This has degree $8$ and is nonnegative on $[0,1]$. Since $L$ agrees with the uniform integral through degree $8$,
$$
L(g_i)=\int_0^1g_i(x)\,dx>0.
$$
In the quadrature rule (7), $g_i$ vanishes at every node except $r_i$, so
$$
w_i g_i(r_i)=L(g_i)>0.
$$
Hence every interior weight is positive.

For the two endpoints, use
$$
g_0(x)=(1-x)Q(x)^2,
\qquad
g_1(x)=xQ(x)^2.
$$
Directly from the prescribed moments,
$$
L(g_0)=\frac{77}{60}>0,
\qquad
L(g_1)=\frac{377}{60}>0.
$$
Since
$$
g_0(0)=Q(0)^2=49,
\qquad
g_1(1)=Q(1)^2=169,
$$
the endpoint weights are also positive. Finally, exactness for the constant polynomial gives
$$
\sum_iw_i=1.
$$
Thus
$$
\mu_*=\sum_{i=0}^5w_i\delta_{r_i}
$$
is a probability law on $[0,1]$ having exactly the prescribed moments through degree $9$.

At every support point of $\mu_*$, the error term in (3) vanishes, because either $x=0$, $x=1$, or $Q(x)=0$. Hence equality holds in (6):
$$
\max\mathbb E\!\left[\frac1{2-X}\right]
=\frac{58363}{84200}.
$$

Step 5: Prove uniqueness

If an admissible law $\mu$ attains equality in (6), then the nonnegative function in (3) must vanish $\mu$-almost surely. Therefore $\mu$ is supported on
$$
\{0,r_1,r_2,r_3,r_4,1\}.
$$
The six masses at these six distinct points are uniquely determined by the moment equations for degrees $0,1,\ldots,5$, because the corresponding $6\times6$ Vandermonde matrix is invertible. Hence
$$
\mu=\mu_*.
$$
The maximizing law is unique.

Final Answer: $\boxed{\frac{58363}{84200}}$

---

## Answer

$\frac{58363}{84200}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- truncated Hausdorff moment problems
- polynomial dual majorants
- quasi-orthogonal support polynomials
- interpolatory quadrature
- equality and uniqueness from support zeros
