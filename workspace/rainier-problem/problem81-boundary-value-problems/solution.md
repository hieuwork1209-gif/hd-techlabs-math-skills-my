## Steps

Step 1: Any positive solution has a unique maximum and is symmetric

Consider
\[
-u''=\lambda(1+u)^3,\qquad 0<x<1,
\]
with
\[
u(0)=u(1)=0,
\]
and suppose \(u>0\) on \((0,1)\).

Since \(\lambda>0\) and \(1+u>0\),
\[
u''<0,
\]
so \(u\) is strictly concave. Hence there is a unique point \(c\in(0,1)\) at which
\[
u'(c)=0,
\]
and this point is the unique maximum. Put
\[
A=u(c)>0.
\]

Multiplying the equation by \(u'\) gives the first integral
\[
\frac12(u')^2+\frac\lambda4(1+u)^4
=\frac\lambda4(1+A)^4.
\]
Therefore
\[
(u')^2
=\frac\lambda2\left((1+A)^4-(1+u)^4\right).
\tag{1}
\]
On the increasing branch from \(x=0\) to \(x=c\),
\[
c
=\sqrt{\frac2\lambda}
\int_0^A
\frac{du}{\sqrt{(1+A)^4-(1+u)^4}}.
\tag{2}
\]
The same quadrature on the decreasing branch from \(c\) to \(1\) gives
\[
1-c
=\sqrt{\frac2\lambda}
\int_0^A
\frac{du}{\sqrt{(1+A)^4-(1+u)^4}}.
\tag{3}
\]
Thus \(c=1/2\). In particular every positive solution is symmetric about \(x=1/2\).

Step 2: Parameterize every positive solution by its amplitude

From (2) with \(c=1/2\),
\[
\frac12
=\sqrt{\frac2\lambda}
\int_0^A
\frac{du}{\sqrt{(1+A)^4-(1+u)^4}}.
\]
Hence
\[
\lambda
=8\left(
\int_0^A
\frac{du}{\sqrt{(1+A)^4-(1+u)^4}}
\right)^2.
\tag{4}
\]

Set
\[
r=\frac1{1+A}\in(0,1),
\qquad
I(r)=\int_r^1\frac{dt}{\sqrt{1-t^4}}.
\tag{5}
\]
Using \(1+u=(1+A)t\), the integral in (4) becomes
\[
r I(r).
\]
Therefore every positive solution lies on the exact branch
\[
\boxed{\lambda(r)=8r^2I(r)^2,\qquad 0<r<1,}
\tag{6}
\]
with amplitude
\[
\boxed{A(r)=\frac1r-1.}
\tag{7}
\]
Conversely, for every \(r\in(0,1)\), equations (1)-(3) construct a unique positive symmetric solution with parameter \(\lambda(r)\) and maximum \(A(r)\). Thus counting positive solutions is exactly the same as counting points of the scalar curve (6).

Step 3: Prove that the branch has exactly one fold

Differentiate (6). Since
\[
I'(r)=-\frac1{\sqrt{1-r^4}},
\]
we get
\[
\lambda'(r)
=16rI(r)
\left(
I(r)-\frac r{\sqrt{1-r^4}}
\right).
\tag{8}
\]
Define
\[
F(r)=I(r)-\frac r{\sqrt{1-r^4}}.
\tag{9}
\]
A direct derivative calculation gives the especially simple formula
\[
F'(r)
=-\frac{2}{(1-r^4)^{3/2}}<0.
\tag{10}
\]
Also
\[
\lim_{r\downarrow0}F(r)
=\int_0^1\frac{dt}{\sqrt{1-t^4}}>0,
\]
whereas
\[
\lim_{r\uparrow1}F(r)=-\infty.
\]
Hence there is a unique
\[
r_*\in(0,1)
\]
satisfying
\[
\boxed{
\int_{r_*}^1\frac{dt}{\sqrt{1-t^4}}
=\frac{r_*}{\sqrt{1-r_*^4}}.
}
\tag{11}
\]
By (8), \(\lambda\) increases on \((0,r_*)\) and decreases on \((r_*,1)\).

Moreover,
\[
\lim_{r\downarrow0}\lambda(r)=0,
\qquad
\lim_{r\uparrow1}\lambda(r)=0.
\tag{12}
\]
Thus \(r_*\) gives the unique global maximum of \(\lambda(r)\).

Step 4: Evaluate the critical parameter and critical amplitude

At the critical point, (11) gives
\[
I(r_*)=\frac{r_*}{\sqrt{1-r_*^4}}.
\]
Substituting this into (6),
\[
\boxed{
\lambda_*
=\frac{8r_*^4}{1-r_*^4}.
}
\tag{13}
\]
The corresponding maximum value of the solution is
\[
\boxed{
A_*=\frac1{r_*}-1.
}
\tag{14}
\]
Numerically,
\[
r_*\approx0.6237834212282149,
\]
\[
\lambda_*\approx1.4273285578611884,
\qquad
A_*\approx0.6031205158210577.
\tag{15}
\]

Step 5: Count all positive solutions for every \(\lambda>0\)

Because \(\lambda(r)\) tends to \(0\) at both endpoints of \((0,1)\), is strictly increasing on \((0,r_*)\), and strictly decreasing on \((r_*,1)\), we obtain the complete bifurcation picture:

- if \(0<\lambda<\lambda_*\), there are exactly two positive solutions;
- if \(\lambda=\lambda_*\), there is exactly one positive solution;
- if \(\lambda>\lambda_*\), there is no positive solution.

The two solutions below the fold are distinguished by their amplitudes: one has \(A<A_*\), the other has \(A>A_*\).

---

## Answer

Let \(r_*\) be the unique root in \((0,1)\) of
\[
\int_{r_*}^1\frac{dt}{\sqrt{1-t^4}}
=\frac{r_*}{\sqrt{1-r_*^4}}.
\]
Then
\[
\boxed{
(\lambda_*,A_*)
=
\left(
\frac{8r_*^4}{1-r_*^4},
\frac1{r_*}-1
\right).
}
\]
Positive solutions exist exactly for \(0<\lambda\le\lambda_*\); there are two for \(0<\lambda<\lambda_*\), one at \(\lambda=\lambda_*\), and none for \(\lambda>\lambda_*\).

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonlinear Dirichlet boundary value problem
- phase-plane first integral
- symmetry from autonomous quadrature
- exact amplitude parameterization
- fold bifurcation and uniqueness of the critical parameter
