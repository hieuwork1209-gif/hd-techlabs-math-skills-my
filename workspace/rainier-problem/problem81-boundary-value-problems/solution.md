## Steps

Step 1: Every positive solution is symmetric and has a unique maximum

Consider
\[
-u''=\lambda(1+u)^3,\qquad 0<x<1,
\]
with
\[
u(0)=u(1)=0,
\qquad u>0\text{ on }(0,1).
\]
Since \(u''<0\), every positive solution is strictly concave. Hence it has a unique maximum at some \(c\in(0,1)\). Put
\[
A=u(c)>0.
\]
Multiplying the equation by \(u'\) gives
\[
\frac12(u')^2+\frac\lambda4(1+u)^4
=\frac\lambda4(1+A)^4,
\]
so
\[
(u')^2
=\frac\lambda2\Bigl((1+A)^4-(1+u)^4\Bigr).
\tag{1}
\]
The travel time from either boundary value \(u=0\) to the maximum value \(u=A\) is therefore
\[
\sqrt{\frac2\lambda}
\int_0^A
\frac{du}{\sqrt{(1+A)^4-(1+u)^4}}.
\]
Thus both sides have the same length, so
\[
c=\frac12.
\]
Uniqueness for the autonomous IVP with data \(u(1/2)=A\), \(u'(1/2)=0\) then gives
\[
u(x)=u(1-x).
\]

Step 2: Exact one-parameter solution branch

From (1) on the half interval,
\[
\frac12
=\sqrt{\frac2\lambda}
\int_0^A
\frac{du}{\sqrt{(1+A)^4-(1+u)^4}}.
\]
Set
\[
r=\frac1{1+A}\in(0,1),
\qquad
I(r)=\int_r^1\frac{dt}{\sqrt{1-t^4}}.
\tag{2}
\]
Then
\[
\boxed{\lambda(r)=8r^2I(r)^2,\qquad A(r)=\frac1r-1.}
\tag{3}
\]
Conversely, for each \(r\in(0,1)\), the quadrature reconstructs a unique positive symmetric solution \(u_r\). Thus all positive solutions are exactly the branch \(\{u_r:0<r<1\}\).

Step 3: The branch has exactly one fold

Since
\[
I'(r)=-\frac1{\sqrt{1-r^4}},
\]
we have
\[
\lambda'(r)
=16rI(r)
\left(
I(r)-\frac r{\sqrt{1-r^4}}
\right).
\tag{4}
\]
Define
\[
F(r)=I(r)-\frac r{\sqrt{1-r^4}}.
\]
A direct derivative gives
\[
\boxed{F'(r)=-\frac{2}{(1-r^4)^{3/2}}<0.}
\tag{5}
\]
Also
\[
F(0+)>0,
\qquad
F(1-)=-\infty.
\]
Hence there is a unique \(r_*\in(0,1)\) such that
\[
\boxed{
I(r_*)=rac{r_*}{\sqrt{1-r_*^4}}.
}
\tag{6}
\]
The branch is strictly increasing in \(\lambda\) on \((0,r_*)\), strictly decreasing on \((r_*,1)\), and
\[
\lambda(r)\to0
\quad(r\downarrow0\text{ or }r\uparrow1).
\]
Therefore
\[
\boxed{
\lambda_*=\frac{8r_*^4}{1-r_*^4},
\qquad
A_*\equiv A(r_*)=\frac1{r_*}-1.
}
\tag{7}
\]
Numerically,
\[
r_*\approx0.6237834212282149,
\]
\[
\lambda_*\approx1.4273285578611884,
\qquad
A_*\approx0.6031205158210577.
\tag{8}
\]
Hence there are exactly two positive solutions for \(0<\lambda<\lambda_*\), exactly one at \(\lambda=\lambda_*\), and none for \(\lambda>\lambda_*\).

Step 4: Linearization and the kernel at the fold

For each branch point define the Dirichlet linearized operator
\[
\mathcal L_r\phi
=-\phi''-3\lambda(r)(1+u_r)^2\phi,
\qquad
\phi(0)=\phi(1)=0.
\tag{9}
\]
Let its eigenvalues be
\[
\mu_1(r)<\mu_2(r)<\cdots.
\]
Differentiate the nonlinear boundary value problem with respect to \(r\). Since the boundary values are fixed,
\[
\dot u_r(0)=\dot u_r(1)=0,
\]
and
\[
\boxed{
\mathcal L_r\dot u_r
=\lambda'(r)(1+u_r)^3.
}
\tag{10}
\]
At the fold \(r=r_*\), \(\lambda'(r_*)=0\), so \(\dot u_{r_*}\) is a nonzero Dirichlet kernel element.

We now show it is the principal eigenfunction. On the right half interval put
\[
z=u_{r_*}'.
\]
Differentiating the ODE in \(x\) gives
\[
\mathcal L_{r_*}z=0.
\tag{11}
\]
Moreover
\[
z(1/2)=0,\qquad z(x)<0\quad(1/2<x\le1).
\]
The function \(\dot u_{r_*}\) is symmetric, satisfies
\[
\dot u_{r_*}'(1/2)=0,
\qquad
\dot u_{r_*}(1/2)=A'(r_*)=-\frac1{r_*^2}<0,
\]
and vanishes at \(x=1\). The Wronskian
\[
W=\dot u_{r_*}z'-\dot u_{r_*}'z
\]
is constant. At \(x=1/2\), both \(\dot u_{r_*}(1/2)\) and \(z'(1/2)=u_{r_*}''(1/2)\) are negative, so \(W>0\). Hence on \((1/2,1]\),
\[
\left(\frac{\dot u_{r_*}}{z}\right)'
=-\frac{W}{z^2}<0.
\tag{12}
\]
The ratio decreases from \(+\infty\) at the center to \(0\) at \(x=1\). Therefore
\[
\dot u_{r_*}(x)<0
\qquad(0<x<1).
\]
Thus \(-\dot u_{r_*}>0\) is the principal eigenfunction, and
\[
\boxed{
\mu_1(r_*)=0,
\qquad
\ker\mathcal L_{r_*}
=\operatorname{span}\{\dot u_{r_*}\}.
}
\tag{13}
\]
In particular the nullity at the fold is exactly \(1\).

Step 5: There is never more than one negative eigenvalue

The potential in \(\mathcal L_r\) is symmetric about \(x=1/2\). Again, the translation mode
\[
z_r=-u_r'
\]
on \([1/2,1]\) satisfies
\[
\mathcal L_r z_r=0,
\qquad
z_r(1/2)=0,
\qquad
z_r(x)>0\quad(1/2<x\le1).
\tag{14}
\]
Thus the zero-energy Dirichlet shooting solution on the half interval has no zero before the endpoint and does not vanish at \(x=1\). By Sturm oscillation, the first Dirichlet-Dirichlet eigenvalue on \([1/2,1]\) is strictly positive.

Because the full potential is symmetric, the second full-interval eigenfunction is odd about \(x=1/2\), and its eigenvalue is exactly that first half-interval Dirichlet eigenvalue. Hence
\[
\boxed{\mu_2(r)>0\quad\text{for every }r\in(0,1).}
\tag{15}
\]
Therefore the Morse index of \(u_r\) is always either \(0\) or \(1\).

Step 6: Exact Morse index on the two branches

First, if \(\mu_1(r)=0\), let \(\phi_1>0\) span the kernel. Taking the inner product of (10) with \(\phi_1\) gives
\[
0
=\lambda'(r)
\int_0^1(1+u_r)^3\phi_1\,dx.
\]
The integral is strictly positive, so
\[
\mu_1(r)=0\Longrightarrow\lambda'(r)=0.
\]
By Step 3, this occurs only at \(r=r_*\).

As \(r\uparrow1\), we have \(u_r\to0\) and \(\lambda(r)\to0\), so
\[
\mathcal L_r\to-\frac{d^2}{dx^2}
\]
in the usual form sense and
\[
\mu_1(r)\to\pi^2>0.
\]
Since \(\mu_1\) cannot vanish again, we obtain
\[
\mu_1(r)>0
\qquad(r_*<r<1).
\tag{16}
\]
Thus the small-amplitude branch \(A<A_*\) has Morse index \(0\).

For the large-amplitude branch, parameterize by the amplitude \(A\). Since
\[
A'(r)=-\frac1{r^2}<0,
\]
we have, on \(0<r<r_*\),
\[
\frac{d\lambda}{dA}<0.
\]
Let
\[
w=\frac{\partial u}{\partial A}
\]
along the branch, normalized so that
\[
w(1/2)=1,\qquad w(0)=w(1)=0.
\]
Differentiating with respect to \(A\) gives
\[
\mathcal L_r w
=\frac{d\lambda}{dA}(1+u_r)^3<0.
\tag{17}
\]
If \(\mu_1(r)>0\), the maximum principle for \(\mathcal L_r\) with Dirichlet boundary data would force \(w<0\) in \((0,1)\), contradicting \(w(1/2)=1\). Hence
\[
\mu_1(r)<0
\qquad(0<r<r_*).
\tag{18}
\]
Together with (15), the large-amplitude branch has Morse index exactly \(1\).

Therefore the complete spectral classification is:

- for \(0<\lambda<\lambda_*\), the smaller-amplitude positive solution has Morse index \(0\), while the larger-amplitude positive solution has Morse index \(1\);
- at \(\lambda=\lambda_*\), the unique positive solution has Morse index \(0\) and nullity \(1\);
- for \(\lambda>\lambda_*\), there is no positive solution.

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
(\lambda_*,A_*,m_{\rm small},m_{\rm large},\nu_*)
=
\left(
\frac{8r_*^4}{1-r_*^4},
\frac1{r_*}-1,
0,
1,
1
\right),
}
\]
where \(m_{\rm small}\) and \(m_{\rm large}\) are the Morse indices of the two positive solutions for \(0<\lambda<\lambda_*\), and \(\nu_*\) is the nullity of the fold solution. At the fold the Morse index itself is \(0\).

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonlinear Dirichlet boundary value problem
- phase-plane first integral and symmetry
- exact fold parameterization
- Dirichlet Sturm-Liouville linearization
- Morse index and nullity
- Sturm oscillation and maximum-principle stability classification
