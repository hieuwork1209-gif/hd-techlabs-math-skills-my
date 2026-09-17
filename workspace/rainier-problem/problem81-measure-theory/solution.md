## Steps

Step 1: Define the two product measures and apply Kakutani's criterion

Let
\[
\Omega=\{0,1\}^{\mathbb N}.
\]
For every integer \(k\ge3\), put
\[
a_k=\frac1{k^2(\log k)^2},\qquad b_k=\frac1{k^3},\qquad c_k=\frac1{k^2}.
\]
Define Bernoulli product measures \(\mu\) and \(\nu\) as follows:

- at coordinate \(3k\),
\[
\mu(X_{3k}=1)=a_k,\qquad \nu(X_{3k}=1)=b_k;
\]
- at coordinate \(3k+1\),
\[
\mu(X_{3k+1}=1)=b_k,\qquad \nu(X_{3k+1}=1)=c_k;
\]
- at every other coordinate, both measures give probability \(1/2\) to \(1\).

For Bernoulli parameters \(p,q\in(0,1)\), the Hellinger affinity is
\[
\rho(p,q)=\sqrt{pq}+\sqrt{(1-p)(1-q)}.
\]
Kakutani's theorem says that the two product measures are equivalent iff
\[
\sum_n\bigl(1-\rho(p_n,q_n)\bigr)<\infty.
\tag{1}
\]
Now
\[
2(1-\rho(p,q))
=(\sqrt p-\sqrt q)^2+(\sqrt{1-p}-\sqrt{1-q})^2
\le 2|p-q|.
\]
Hence
\[
\sum_{k\ge3}\bigl(1-\rho(a_k,b_k)\bigr)
+\sum_{k\ge3}\bigl(1-\rho(b_k,c_k)\bigr)
<\infty,
\]
because
\[
\sum_{k\ge3}(a_k+b_k+c_k)<\infty.
\]
Therefore
\[
\boxed{\mu\sim\nu.}
\tag{2}
\]
Both measures are nonatomic because infinitely many coordinates are common fair Bernoulli coordinates.

Let
\[
Z=\frac{d\mu}{d\nu}.
\]

Step 2: Write the Mellin product for the likelihood ratio

At coordinate \(3k\), the likelihood ratio is
\[
L_k^{(A)}=
\begin{cases}
 a_k/b_k,&X_{3k}=1,\\[1mm]
 (1-a_k)/(1-b_k),&X_{3k}=0,
\end{cases}
\]
while at coordinate \(3k+1\),
\[
L_k^{(B)}=
\begin{cases}
 b_k/c_k,&X_{3k+1}=1,\\[1mm]
 (1-b_k)/(1-c_k),&X_{3k+1}=0.
\end{cases}
\]
The fair coordinates contribute factor \(1\).

Since
\[
\sum_k \mathbb E_\nu\bigl|\log L_k^{(A)}\bigr|
+\sum_k \mathbb E_\nu\bigl|\log L_k^{(B)}\bigr|<\infty,
\]
the logarithmic likelihood series converges absolutely \(\nu\)-a.s., and
\[
Z=\prod_{k\ge3}L_k^{(A)}L_k^{(B)}.
\tag{3}
\]

For real \(t\), define
\[
M(t)=\int_\Omega Z^t\,d\nu.
\]
The finite-coordinate moments factor as
\[
M_N(t)=\prod_{3\le k\le N}A_k(t)B_k(t),
\tag{4}
\]
where
\[
A_k(t)
=b_k\left(\frac{a_k}{b_k}\right)^t
+(1-b_k)\left(\frac{1-a_k}{1-b_k}\right)^t,
\tag{5}
\]
\[
B_k(t)
=c_k\left(\frac{b_k}{c_k}\right)^t
+(1-c_k)\left(\frac{1-b_k}{1-c_k}\right)^t.
\tag{6}
\]

Step 3: Analyze the upper critical exponent

At the \(A\)-coordinates,
\[
\frac{a_k}{b_k}=\frac{k}{(\log k)^2}\to\infty.
\]
For fixed real \(t\), expansion of the zero-coordinate factor gives
\[
A_k(t)-1
=b_k\left(\frac{a_k}{b_k}\right)^t
-t a_k+(t-1)b_k+O_t(a_k^2+b_k^2).
\tag{7}
\]
Thus, for \(t\ge0\), convergence of
\[
\sum_k |A_k(t)-1|
\]
is controlled by
\[
\sum_k b_k\left(\frac{a_k}{b_k}\right)^t
=
\sum_k \frac{k^{t-3}}{(\log k)^{2t}}.
\tag{8}
\]
This converges for \(t<2\), and at the endpoint \(t=2\) it becomes
\[
\sum_k\frac1{k(\log k)^4}<\infty.
\]
For every \(t>2\), the series in (8) diverges.

Moreover, for \(t>2\), the positive first term in (7) dominates the summable correction terms, so
\[
\sum_k\log A_k(t)=+\infty.
\tag{9}
\]
Hence the \(A\)-coordinates force the upper critical exponent
\[
\boxed{t\le2,\ \text{with }t=2\text{ included}.}
\tag{10}
\]

Step 4: Analyze the lower critical exponent

At the \(B\)-coordinates,
\[
\frac{b_k}{c_k}=\frac1k.
\]
For fixed real \(t\), similarly
\[
B_k(t)-1
=c_k\left(\frac{b_k}{c_k}\right)^t
-t b_k+(t-1)c_k+O_t(b_k^2+c_k^2).
\tag{11}
\]
For negative \(t\), the decisive series is
\[
\sum_k c_k\left(\frac{b_k}{c_k}\right)^t
=
\sum_k k^{-2-t}.
\tag{12}
\]
This converges exactly when
\[
t>-1.
\]
At \(t=-1\) it is the harmonic series, so the lower endpoint is excluded.

The \(A\)-coordinates cause no further restriction for \(t<0\), and the \(B\)-coordinates cause no further restriction for \(t\ge0\).

Therefore the only possible finite-moment interval is
\[
(-1,2].
\tag{13}
\]

Step 5: Prove finiteness on the whole interval and divergence outside it

For every compact interval
\[
I\subset(-1,2),
\]
the estimates above are uniform in \(t\in I\), so
\[
\sum_k\sup_{t\in I}igl(|A_k(t)-1|+|B_k(t)-1|\bigr)<\infty.
\tag{14}
\]
Hence the product in (4) converges locally uniformly there.

For \(1<t\le2\), the likelihood-ratio martingale \(Z_N\) is bounded in \(L^t(\nu)\), so \(Z_N\to Z\) in \(L^t\), giving
\[
M(t)=\prod_{k\ge3}A_k(t)B_k(t)<\infty.
\tag{15}
\]
For \(0<t\le1\), use \(x^t\le1+x\) and the \(L^1\)-convergence of \(Z_N\). For \(-1<t<0\), choose \(\varepsilon>0\) so that
\[
(1+\varepsilon)t>-1.
\]
Then the already established product bound at \((1+\varepsilon)t\) gives uniform integrability of \(Z_N^t\), hence again (15).

At \(t=2\), (8) is still summable, so \(Z_N\) is bounded in \(L^2\) and (15) remains valid.

For \(t>2\) or \(t\le-1\), the partial moments in (4) diverge to \(+\infty\). Since \(x\mapsto x^t\) is convex for \(t>1\) and for \(t<0\), and
\[
Z_N=\mathbb E_\nu[Z\mid\mathcal F_N],
\]
Jensen's inequality yields
\[
\mathbb E_\nu Z^t\ge \mathbb E_\nu Z_N^t.
\]
Thus
\[
M(t)=+\infty
\]
outside the interval in (13).

Therefore
\[
\boxed{
\mathcal I:=\{t\in\mathbb R:M(t)<\infty\}=(-1,2].
}
\tag{16}
\]

Step 6: Holomorphic strip and the two asymmetric \(L^p\) thresholds

For complex \(z\), the factors \(A_k(z),B_k(z)\) are entire in \(z\). The same estimates with \(t\) replaced by \(\Re z\) show locally uniform absolute convergence on
\[
\boxed{-1<\Re z<2.}
\tag{17}
\]
Hence
\[
M(z)=\prod_{k\ge3}A_k(z)B_k(z)
\]
is holomorphic on that open vertical strip. The line \(\Re z=2\) is still pointwise absolutely convergent, but no larger open vertical strip is possible because every real \(t>2\) gives infinite moment. The lower boundary \(t=-1\) already diverges.

From (16),
\[
Z\in L^p(\nu)
\iff 0<p\le2.
\tag{18}
\]
Also, if
\[
W=\frac{d\nu}{d\mu}=Z^{-1},
\]
then
\[
\int W^p\,d\mu
=\int Z^{1-p}\,d\nu
=M(1-p).
\]
Therefore
\[
W\in L^p(\mu)
\iff -1<1-p\le2
\iff 0<p<2.
\tag{19}
\]
In particular,
\[
Z\in L^2(\nu),
\qquad
W\notin L^2(\mu),
\]
even though \(\mu\sim\nu\).

Finally,
\[
Z^{-1}\in L^p(\nu)
\iff M(-p)<\infty
\iff 0<p<1.
\tag{20}
\]

---

## Answer

\[
\boxed{
\left(
(-1,2],\ (0,2],\ (0,2)
\right)
}
\]
where the three entries are respectively
\[
\{t\in\mathbb R:\int Z^t\,d\nu<\infty\},
\qquad
\{p>0:Z\in L^p(\nu)\},
\qquad
\left\{p>0:\frac{d\nu}{d\mu}\in L^p(\mu)\right\}.
\]
Moreover \(\mu\sim\nu\), the Mellin transform is holomorphic on the maximal open vertical strip \(-1<\Re z<2\), and \(Z^{-1}\in L^p(\nu)\) exactly for \(0<p<1\).

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- Kakutani equivalence criterion for product measures
- Radon-Nikodym likelihood-ratio martingales
- Mellin transforms of infinite products
- endpoint \(L^p\) integrability
- local uniform convergence of analytic Euler-type products
