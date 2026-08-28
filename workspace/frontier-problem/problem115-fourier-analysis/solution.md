## Steps

Step 1: Convert the nonlinear correlations into triangular coefficient identities

Put
$$
S_n=\sum_{a+b=n}c_{a}c_{b},
\qquad
T_n=\sum_{a+b+c=n}c_{a}c_{b}c_{c}.
$$
Expanding the definition of $D$, the integral in $x$ kills every term except those with $a+b=n$. The remaining $t$-frequency is $n$, so
$$
\widehat D(n)=\overline{c_n}S_n.
$$
Likewise, in $Q$ the $x$-integral forces $a+b+c=n$, and the remaining $t$-frequency is $2n$. Hence
$$
\widehat Q(2n)=\overline{c_n}T_n.
$$
Since $c_0=1$, write
$$
S_n=2c_n+A_n,
\qquad
A_n=\sum_{j=1}^{n-1}c_{j}c_{n-j},
$$
and
$$
T_n=3c_n+B_n,
$$
where $B_n$ is the sum over triples $a+b+c=n$ with all three indices strictly less than $n$. Because $|c_n|=1$,
$$
\widehat D(n)=2+\overline{c_n}A_n,
\qquad
\widehat Q(2n)=3+\overline{c_n}B_n.
$$
Thus both identities are triangular: once $c_0,\ldots,c_{n-1}$ are known, either one can determine $c_n$ provided its coefficient of $\overline{c_n}$ is nonzero.

Step 2: Compute the two convolution laws for the candidate sequence

Define
$$
u_k=i^{k(k-1)/2}.
$$
Then $u_0=u_1=1$ and $u_{k+4}=-u_k$. Therefore its ordinary generating function is
$$
U(z)=\sum_{k\geq0}u_kz^k
=\frac{1+z+iz^2-iz^3}{1+z^4}.
$$
Let $A(z)=1+z+iz^2-iz^3$. Since
$$
\frac{1}{(1+z^4)^2}=\sum_{j\geq0}(-1)^{j}(j+1)z^{4j},
$$
and
$$
A(z)^2=1+2z+(1+2i)z^2-(1+2i)z^4+2z^5-z^6,
$$
coefficient extraction from $U(z)^2$ gives
$$
\frac{[z^n]U(z)^2}{u_n}=
\begin{cases}
2m+1+2mi,&n=4m,\\
2,&n=4m+1,\\
2m+2-(2m+1)i,&n=4m+2,\\
0,&n=4m+3.
\end{cases}
$$
In particular, for $n=2m$ this is
$$
\frac{[z^{2m}]U(z)^2}{u_{2m}}=m+1+(-1)^{m}m i,
$$
and for $n=4m+3$ it is $0$.

For the cubic convolution we only need indices $n=4m+1$. Using
$$
\frac{1}{(1+z^4)^3}=\sum_{j\geq0}(-1)^{j}\binom{j+2}{2}z^{4j},
$$
the coefficients of $A(z)^3$ in degrees $1,5,9$ are respectively
$$
3,\qquad 3-3i,\qquad i.
$$
Hence, because $u_{4m+1}=(-1)^{m}$,
$$
\frac{[z^{4m+1}]U(z)^3}{u_{4m+1}}
=3\binom{m+2}{2}-(3-3i)\binom{m+1}{2}+i\binom{m}{2}.
$$
The right-hand side simplifies to
$$
3(m+1)+m(2m+1)i.
$$
Thus the sequence $(u_k)$ satisfies every correlation identity in the statement.

Step 3: Prove that the quadratic data force all indices except one residue class

We prove $c_n=u_n$ by induction on $n$. The cases $n=0,1$ are given. Assume $c_j=u_j$ for every $j<n$.

First suppose $n=2m$. By Step 2,
$$
A_n=\sum_{j=1}^{n-1}u_{j}u_{n-j}
=u_n\bigl(m-1+(-1)^{m}m i\bigr).
$$
The prescribed value of $\widehat D(2m)$ and Step 1 give
$$
m-1+(-1)^{m}m i
=\overline{c_n}u_n\bigl(m-1+(-1)^{m}m i\bigr).
$$
The factor on the left is nonzero because its imaginary part has absolute value $m$. Hence
$$
\overline{c_n}u_n=1,
$$
so $c_n=u_n$.

Now suppose $n=4m+3$. Step 2 gives
$$
A_n=-2u_n.
$$
Since $\widehat D(n)=0$, Step 1 yields
$$
-2=-2\overline{c_n}u_n,
$$
again forcing $c_n=u_n$.

Therefore the quadratic correlation determines every even index and every index congruent to $3$ modulo $4$. Its only degeneracy occurs at indices congruent to $1$ modulo $4$, where Step 2 gives $A_n=0$.

Step 4: Use the cubic data to repair the quadratic degeneracy

It remains to treat $n=4m+1$ with $m\geq1$. Under the induction hypothesis, Step 2 gives
$$
B_n=u_n\left(3m+m(2m+1)i\right).
$$
Indeed, the full cubic convolution equals
$$
T_n=u_n\left(3(m+1)+m(2m+1)i\right),
$$
and subtracting the three terms containing $c_n$ leaves the displayed $B_n$.

The prescribed value of $\widehat Q(2n)$ and Step 1 therefore imply
$$
3m+m(2m+1)i
=\overline{c_n}u_n\left(3m+m(2m+1)i\right).
$$
Because $m\geq1$, this factor is nonzero. Thus $\overline{c_n}u_n=1$, so $c_n=u_n$.

This closes the induction for every $0\leq n\leq N$. Existence was verified in Step 2, while Steps 3 and 4 prove uniqueness.
Final Answer: $\boxed{c_k=i^{k(k-1)/2}\quad(0\leq k\leq N)}$

---

## Answer

$c_k=i^{k(k-1)/2}\quad(0\leq k\leq N)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Sequence or series representation

---

## Solution Concepts

- nonlinear Fourier correlation identities
- triangular coefficient recovery
- periodic generating functions
- convolution coefficient extraction
- induction through a degenerate residue class

---

## Black-Box Audit — no issues found
