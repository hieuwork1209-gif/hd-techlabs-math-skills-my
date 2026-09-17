## Steps

Step 1: Define the three product measures and prove pairwise equivalence

Let
\[
\Omega=\{0,1\}^{\mathbb N}.
\]
For every integer \(k\ge3\), put
\[
a_k=\frac1{k^2(\log k)^2},\qquad
b_k=\frac1{k^4},\qquad
c_k=\frac1{k^5},\qquad
d_k=\frac1{k^2},\qquad
e_k=\frac1{k^4}.
\]
Define Bernoulli product measures \(\mu,\nu,\lambda\) by

\[
\begin{array}{c|ccc}
\text{coordinate}&\mu(1)&\nu(1)&\lambda(1)\\ \hline
4k&a_k&b_k&b_k\\
4k+1&c_k&c_k&d_k\\
4k+2&e_k&d_k&e_k
\end{array}
\tag{1}
\]

for every \(k\ge3\), and let all three measures be fair Bernoulli at every remaining coordinate.

For Bernoulli parameters \(p,q\), the Hellinger affinity is
\[
\rho(p,q)=\sqrt{pq}+\sqrt{(1-p)(1-q)}.
\]
Since
\[
2(1-\rho(p,q))
=(\sqrt p-\sqrt q)^2+(\sqrt{1-p}-\sqrt{1-q})^2
\le 2|p-q|,
\]
and all five sequences in (1) are summable, the Kakutani sums for every pair among \(\mu,\nu,\lambda\) converge. Hence
\[
\boxed{\mu\sim\nu\sim\lambda.}
\tag{2}
\]
The common fair coordinates also make all three measures nonatomic.

Set
\[
Z=\frac{d\mu}{d\nu},
\qquad
W=\frac{d\lambda}{d\nu}.
\]

Step 2: Write the joint Mellin product

For a single Bernoulli coordinate with
\[
\mu(1)=p,\qquad \nu(1)=q,\qquad \lambda(1)=r,
\]
the joint coordinate moment is
\[
\Phi_{p,q,r}(s,t)
=q\left(\frac pq\right)^s\left(\frac rq\right)^t
+(1-q)\left(\frac{1-p}{1-q}\right)^s
\left(\frac{1-r}{1-q}\right)^t.
\tag{3}
\]
Thus the finite-coordinate joint Mellin transforms factor. For the three sparse coordinate families define
\[
A_k(s)=\Phi_{a_k,b_k,b_k}(s,t),
\]
which is independent of \(t\),
\[
B_k(t)=\Phi_{c_k,c_k,d_k}(s,t),
\]
which is independent of \(s\), and
\[
C_k(s+t)=\Phi_{e_k,d_k,e_k}(s,t),
\]
which depends only on \(u=s+t\).
Hence formally
\[
M(s,t):=\int Z^sW^t\,d\nu
=\prod_{k\ge3}A_k(s)B_k(t)C_k(s+t).
\tag{4}
\]
We now determine exactly when this product represents a finite moment.

Step 3: The first critical face, \(s=3/2\)

At the \(A\)-coordinates,
\[
\frac{a_k}{b_k}=\frac{k^2}{(\log k)^2}.
\]
For fixed real \(s\), expansion of the zero-coordinate term gives
\[
A_k(s)-1
=b_k\left(\frac{a_k}{b_k}\right)^s
-s a_k+(s-1)b_k+O_s(a_k^2+b_k^2).
\tag{5}
\]
The decisive series is therefore
\[
\sum_k b_k\left(\frac{a_k}{b_k}\right)^s
=
\sum_k\frac{k^{2s-4}}{(\log k)^{2s}}.
\tag{6}
\]
It converges for \(s<3/2\), and at the endpoint
\[
s=\frac32
\]
it becomes
\[
\sum_k\frac1{k(\log k)^3}<\infty.
\]
For every \(s>3/2\), the positive rare-event term in (5) dominates the summable corrections and forces divergence of the partial moments. Thus the exact first constraint is
\[
\boxed{s\le\frac32,}
\tag{7}
\]
with equality allowed.

Step 4: The second critical face, \(t=4/3\)

At the \(B\)-coordinates,
\[
\frac{d_k}{c_k}=k^3.
\]
The corresponding expansion is
\[
B_k(t)-1
=c_k\left(\frac{d_k}{c_k}\right)^t
-t d_k+(t-1)c_k+O_t(c_k^2+d_k^2).
\tag{8}
\]
Hence the decisive series is
\[
\sum_k c_k\left(\frac{d_k}{c_k}\right)^t
=
\sum_k k^{3t-5}.
\tag{9}
\]
This converges exactly when
\[
t<\frac43.
\]
At \(t=4/3\) it is the harmonic series. Hence
\[
\boxed{t<\frac43,}
\tag{10}
\]
and this face is excluded.

Step 5: The diagonal critical face, \(s+t=-1/2\)

At the \(C\)-coordinates, both \(\mu\) and \(\lambda\) have parameter \(e_k=k^{-4}\), while \(\nu\) has parameter \(d_k=k^{-2}\). Put
\[
u=s+t.
\]
Then
\[
\frac{e_k}{d_k}=k^{-2},
\]
and
\[
C_k(u)-1
=d_k\left(\frac{e_k}{d_k}\right)^u
-u e_k+(u-1)d_k+O_u(e_k^2+d_k^2).
\tag{11}
\]
The decisive series is
\[
\sum_k d_k\left(\frac{e_k}{d_k}\right)^u
=
\sum_k k^{-2-2u}.
\tag{12}
\]
This converges exactly when
\[
u>-\frac12.
\]
At \(u=-1/2\) it is again harmonic. Hence the exact diagonal constraint is
\[
\boxed{s+t>-\frac12,}
\tag{13}
\]
with equality excluded.

Step 6: Exact real joint-moment domain

Combining (7), (10), and (13), define
\[
\mathcal D
=
\left\{(s,t)\in\mathbb R^2:
 s\le\frac32,
\ t<\frac43,
\ s+t>-\frac12
\right\}.
\tag{14}
\]

For every \((s,t)\in\mathcal D\), the coordinate estimates above give
\[
\sum_k\mathbb E_\nu|Y_k(s,t)-1|<\infty,
\]
where \(Y_k(s,t)\) is the corresponding coordinate factor in \(Z^sW^t\). At the allowed face \(s=3/2\), the logarithmic gain in (6) still gives summability. The standard independent-product criterion therefore gives convergence in \(L^1(\nu)\), and
\[
M(s,t)=\prod_{k\ge3}A_k(s)B_k(t)C_k(s+t)<\infty.
\tag{15}
\]

For the converse, split the densities according to the three independent sparse coordinate families:
\[
Z=Z_AZ_C,
\qquad
W=W_BW_C,
\qquad
Z_C=W_C.
\tag{16}
\]
If \(s>3/2\), then \(s>1\). The finite-coordinate likelihood ratios \(Z_{A,N}\) form a martingale converging to \(Z_A\), so convexity of \(x\mapsto x^s\) gives
\[
\mathbb E_\nu Z_A^s
\ge \mathbb E_\nu Z_{A,N}^s.
\]
By (6) the right-hand side tends to \(+\infty\), hence \(\mathbb E Z_A^s=\infty\).

If \(t\ge4/3\), the same argument with \(W_B\) and the convex function \(x^t\) gives
\[
\mathbb E_\nu W_B^t=\infty.
\]

Finally, if \(u=s+t\le-1/2\), then \(u<0\) and \(x\mapsto x^u\) is convex. Applying Jensen to the finite-coordinate likelihood martingale \(Z_{C,N}=W_{C,N}\) and using (12) gives
\[
\mathbb E_\nu Z_C^u=\infty.
\]

The three family factors are independent and strictly positive, so Tonelli factors the extended expectation of
\[
Z_A^sW_B^tZ_C^{s+t}.
\]
If any one of the three inequalities in (14) fails, one factor has infinite expectation and the full joint moment is infinite. Consequently
\[
\boxed{
\{(s,t):M(s,t)<\infty\}=\mathcal D.
}
\tag{17}
\]

Step 7: Maximal holomorphic tube domain

For complex \((z,w)\), every factor
\[
A_k(z),\qquad B_k(w),\qquad C_k(z+w)
\]
is entire. On every compact subset of
\[
\mathcal T
=
\left\{(z,w)\in\mathbb C^2:
\Re z<\frac32,
\ \Re w<\frac43,
\ \Re(z+w)>-\frac12
\right\},
\tag{18}
\]
the estimates above are locally uniform and absolutely summable. Hence
\[
M(z,w)=\prod_{k\ge3}A_k(z)B_k(w)C_k(z+w)
\]
is holomorphic on \(\mathcal T\).

No strictly larger open tube domain is possible: any open enlargement across one of the three real supporting faces contains a real point outside \(\mathcal D\), where the corresponding moment is infinite. Therefore
\[
\boxed{\mathcal T\text{ is the maximal open holomorphic tube.}}
\tag{19}
\]

Step 8: Marginal and reverse \(L^p\) thresholds

From (14),
\[
Z\in L^p(\nu)
\iff (p,0)\in\mathcal D
\iff 0<p\le\frac32,
\]
so
\[
\boxed{\mathcal P_Z=(0,3/2].}
\tag{20}
\]
Similarly,
\[
W\in L^p(\nu)
\iff (0,p)\in\mathcal D
\iff 0<p<\frac43,
\]
so
\[
\boxed{\mathcal P_W=(0,4/3).}
\tag{21}
\]

For the reverse densities,
\[
\int\left(\frac{d\nu}{d\mu}\right)^p d\mu
=\int Z^{1-p}\,d\nu
=M(1-p,0),
\]
which is finite exactly for
\[
0<p<\frac32.
\]
Likewise,
\[
\int\left(\frac{d\nu}{d\lambda}\right)^p d\lambda
=M(0,1-p)<\infty
\iff 0<p<\frac32.
\]
Thus
\[
\boxed{
\mathcal R_\mu=\mathcal R_\lambda=(0,3/2).
}
\tag{22}
\]
As one further check,
\[
Z^{-1}W^{-1}\in L^p(\nu)
\iff (-p,-p)\in\mathcal D
\iff 0<p<\frac14.
\tag{23}
\]

---

## Answer

\[
\boxed{
\left(
\mathcal D,
(0,3/2],
(0,4/3),
(0,3/2),
(0,3/2)
\right)
}
\]
where
\[
\mathcal D=
\left\{(s,t)\in\mathbb R^2:
 s\le\frac32,
\ t<\frac43,
\ s+t>-\frac12
\right\}.
\]
The maximal holomorphic tube is
\[
\left\{(z,w)\in\mathbb C^2:
\Re z<\frac32,
\ \Re w<\frac43,
\ \Re(z+w)>-\frac12
\right\}.
\]
Moreover \(\mu\sim\nu\sim\lambda\), and \(Z^{-1}W^{-1}\in L^p(\nu)\) exactly for \(0<p<1/4\).

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- Kakutani equivalence of product measures
- joint Radon-Nikodym Mellin transforms
- coordinatewise likelihood products
- asymmetric critical faces and endpoint inclusion
- holomorphic tube domains
- marginal and reverse density integrability
