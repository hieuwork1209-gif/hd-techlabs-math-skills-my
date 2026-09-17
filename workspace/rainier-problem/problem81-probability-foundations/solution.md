## Steps

Step 1: Reformulate the constraints as a truncated Hausdorff moment problem

Let \(\mu\) be the law of \(X\) on \([0,1]\). The assumptions are
\[
\int_0^1 x^k\,d\mu(x)=\frac1{k+1}
\qquad(k=0,1,\ldots,8),
\]
where the case \(k=0\) is the total mass condition. Thus \(\mu\) agrees with the uniform probability measure on all polynomials of degree at most \(8\).

We must maximize
\[
\int_0^1 \frac{d\mu(x)}{2-x}.
\]

Step 2: Construct the dual polynomial

Set
\[
q(x)=126x^4-224x^3+126x^2-24x+1.
\]
A direct beta-integral calculation gives
\[
\int_0^1 x^j(1-x)q(x)\,dx=0
\qquad(j=0,1,2,3).
\tag{1}
\]
Indeed, after expanding \(q\), each integral is a linear combination of
\[
\int_0^1 x^m(1-x)\,dx=\frac1{(m+1)(m+2)},
\]
and the four resulting combinations vanish.

Also
\[
q(2)=681.
\]
Define
\[
P(x)=\frac{1+\dfrac{(1-x)q(x)^2}{681^2}}{2-x}.
\tag{2}
\]
The numerator in (2) vanishes at \(x=2\), because
\[
1+\frac{(1-2)q(2)^2}{681^2}=0.
\]
Hence \(P\) is actually a polynomial, of degree \(8\). Moreover, for \(0\le x\le1\),
\[
P(x)-\frac1{2-x}
=\frac{(1-x)q(x)^2}{681^2(2-x)}\ge0.
\tag{3}
\]
Thus \(P\) is a degree-\(8\) polynomial majorant of the objective function.

Expanding (2) gives
\[
P(x)=\frac{1}{463761}\Bigl(
15876x^8-40572x^7+57232x^6-29960x^5+29456x^4
+25536x^3+58396x^2+115916x+231881
\Bigr).
\tag{4}
\]

Step 3: Obtain the sharp upper bound from the moment constraints

Since \(\mu\) and the uniform measure have the same moments through degree \(8\), (4) implies
\[
\int_0^1 P(x)\,d\mu(x)=\int_0^1P(x)\,dx.
\]
Using (4),
\[
\int_0^1P(x)\,dx
=\frac{14161}{20430}.
\tag{5}
\]
Combining (3) and (5), every admissible law satisfies
\[
\mathbb E\frac1{2-X}\le\frac{14161}{20430}.
\tag{6}
\]

Step 4: Construct an admissible law attaining equality

The polynomial \(q\) is orthogonal to \(1,x,x^2,x^3\) for the positive weight \((1-x)\,dx\) on \([0,1]\). Therefore its four roots
\[
r_1<r_2<r_3<r_4
\]
are simple and lie in \((0,1)\).

Take the five nodes
\[
r_1,r_2,r_3,r_4,1.
\]
Let \(L_i\) be their Lagrange basis polynomials, and define
\[
w_i=\int_0^1L_i(x)\,dx.
\]
We claim the quadrature rule
\[
\int_0^1 f(x)\,dx=\sum_{i=1}^5w_i f(r_i)
\tag{7}
\]
is exact for every polynomial \(f\) of degree at most \(8\), where \(r_5=1\).

Indeed, let \(R\) be the degree-at-most-\(4\) interpolant of \(f\) at the five nodes. Then
\[
f(x)-R(x)=(1-x)q(x)s(x)
\]
for some polynomial \(s\) of degree at most \(3\). By (1),
\[
\int_0^1(f-R)=0,
\]
which proves (7).

The weights are positive. In fact, applying (7) to \(L_i^2\), whose degree is \(8\), gives
\[
w_i=\int_0^1L_i(x)^2\,dx>0.
\]
Also \(\sum_iw_i=1\). Hence
\[
\mu_*=\sum_{i=1}^5w_i\,\delta_{r_i}
\]
is a probability measure, and (7) shows that it has moments
\[
\int x^k\,d\mu_*(x)=\frac1{k+1}
\qquad(k=0,1,\ldots,8).
\]

By construction, every support point of \(\mu_*\) is a zero of the nonnegative error in (3): the first four satisfy \(q(r_i)=0\), and the fifth is \(1\). Therefore equality holds in (6), so
\[
\max\mathbb E\frac1{2-X}=\frac{14161}{20430}.
\]

Step 5: Uniqueness of the maximizing law

If an admissible law \(\mu\) attains equality in (6), then the nonnegative function in (3) must vanish \(\mu\)-almost surely. Hence \(\mu\) is supported on
\[
\{r_1,r_2,r_3,r_4,1\}.
\]
The masses at these five distinct points are uniquely determined by the first five moment equations \(k=0,1,2,3,4\), because the corresponding Vandermonde matrix is invertible. Thus \(\mu=\mu_*\). The maximizing law is unique.

As a useful check, the mass at the endpoint is
\[
\mu_*(\{1\})=\int_0^1\frac{q(x)}{q(1)}\,dx
=\frac1{25},
\]
since \(q(1)=5\) and \(\int_0^1q(x)\,dx=1/5\).

Final Answer: $\boxed{\frac{14161}{20430}}$

---

## Answer

$\frac{14161}{20430}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- truncated Hausdorff moment problem
- polynomial dual majorants
- orthogonal-polynomial quadrature
- moment matching
- equality and uniqueness from support zeros
