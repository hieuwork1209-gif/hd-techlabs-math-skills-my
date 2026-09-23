## Steps

Step 1: Derive the BDF4 difference-transfer matrix

At step \(n\), let
$$
H_j=t_n-t_{n-j},\qquad j=1,2,3,4.
$$
After translating \(t_n\) to \(0\), the interpolation nodes are \(0,-H_1,-H_2,-H_3,-H_4\). If
$$
p_n'(t_n)=\sum_{j=0}^4 w_jy_{n-j},
$$
the Lagrange basis gives
$$
w_0=\sum_{m=1}^4\frac1{H_m},
$$
and, for \(1\leq j\leq4\),
$$
w_j=
-\frac{\prod_{\substack{1\leq m\leq4\\m\ne j}}H_m}
{H_j\prod_{\substack{1\leq m\leq4\\m\ne j}}(H_m-H_j)}.
$$
For the test equation \(y'=0\),
$$
\sum_{j=0}^4w_jy_{n-j}=0.
$$
Because the derivative formula annihilates constants, \(\sum_{j=0}^4w_j=0\). Set \(d_n=y_n-y_{n-1}\). Substituting
$$
y_{n-j}=y_{n-1}-\sum_{k=1}^{j-1}d_{n-k}
$$
into the recurrence gives
$$
\begin{bmatrix}
d_n\\ d_{n-1}\\ d_{n-2}
\end{bmatrix}
=
T(H_1,H_2,H_3,H_4)
\begin{bmatrix}
d_{n-1}\\ d_{n-2}\\ d_{n-3}
\end{bmatrix},
$$
where
$$
T=
\begin{bmatrix}
\beta_1&\beta_2&\beta_3\\
1&0&0\\
0&1&0
\end{bmatrix},
\qquad
\beta_k=\frac{\sum_{j=k+1}^4w_j}{w_0}.
$$
Thus zero-stability reduces to the three parasitic Floquet multipliers of a \(3\times3\) periodic transfer product.

Step 2: Build the three-phase monodromy

Scale the repeating steps by the common factor \(h\). For the cycle
$$
1,\quad r,\quad r^2,
$$
the four cumulative backward distances in the three phases are
$$
H^{(0)}=(1,\ 1+r^2,\ 1+r+r^2,\ 2+r+r^2),
$$
$$
H^{(1)}=(r,\ 1+r,\ 1+r+r^2,\ (1+r)^2),
$$
$$
H^{(2)}=(r^2,\ r+r^2,\ 1+r+r^2,\ 1+r+2r^2).
$$
Let \(T_k=T(H^{(k)})\). Over one full period,
$$
M(r)=T_2T_1T_0.
$$
Let
$$
\chi_r(z)=\det(zI-M(r)).
$$
Substituting the weights from Step 1 and putting the entries over the positive common denominator
$$
\begin{aligned}
D(r)={}&(2r^4+7r^3+9r^2+6r+1)\\
&\cdot(7r^5+13r^4+15r^3+10r^2+4r+1)\\
&\cdot(r^6+2r^5+8r^4+9r^3+15r^2+8r+7)
\end{aligned}
$$
gives a cubic with denominator \(D(r)\). No sign information is lost because \(D(r)>0\) for \(r>0\).

Step 3: Convert the unit-disk condition to a Hurwitz condition

Use the Cayley map
$$
z=\frac{1+x}{1-x}.
$$
It maps \(\operatorname{Re}x<0\) to \(|z|<1\). Define
$$
G_r(x)=D(r)(1-x)^3\chi_r\left(\frac{1+x}{1-x}\right)
=g_3x^3+g_2x^2+g_1x+g_0.
$$
Put \(S=r^2+r+1\). Collecting the coefficients from the three matrices in Step 2 gives
$$
g_0=12S^5(r^5+5r^4+8r^3+9r^2+3r+2),
$$
$$
g_3=4(r+1)Q(r),
$$
where \(Q\) is the polynomial defined in the problem. The two differences needed for the stability test are
$$
\begin{aligned}
g_1-g_0
=4S^3(&7r^9+30r^8+89r^7+186r^6+251r^5\\
&+270r^4+193r^3+91r^2+28r+3),
\end{aligned}
$$
and
$$
\begin{aligned}
g_2-g_3
=4S^3(&7r^9+30r^8+89r^7+184r^6+249r^5\\
&+268r^4+191r^3+91r^2+28r+3).
\end{aligned}
$$
All coefficients displayed here are positive except the constant term of \(Q\).

For a cubic
$$
g_3x^3+g_2x^2+g_1x+g_0,
$$
the Routh table has first column
$$
g_3,\qquad
g_2,\qquad
\frac{g_2g_1-g_3g_0}{g_2},\qquad
g_0.
$$
Hence all roots have negative real part exactly when these four quantities are positive. If \(Q(r)>0\), then
$$
g_3>0,\qquad g_2>g_3>0,\qquad g_1>g_0>0,
$$
so
$$
g_2g_1>g_3g_0.
$$
Therefore every parasitic Floquet multiplier lies strictly inside the unit disk whenever \(Q(r)>0\).

Step 4: Find the sharp threshold and handle the boundary case

The polynomial
$$
\begin{aligned}
Q(r)={}&4r^{14}+18r^{13}+63r^{12}+172r^{11}+371r^{10}
+656r^9+926r^8\\
&+1074r^7+986r^6+728r^5+399r^4+164r^3+37r^2+4r-2
\end{aligned}
$$
has
$$
Q'(r)>0\qquad(r>0),
$$
because every coefficient of its derivative is positive. Also
$$
Q\left(\frac18\right)
=-\frac{525126457835}{1099511627776}<0,
$$
while
$$
Q\left(\frac17\right)
=\frac{16293658784}{678223072849}>0.
$$
Thus
$$
r_*=\operatorname{root}_{(1/8,1/7)}Q
$$
is the unique positive zero of \(Q\).

At \(r=r_*\), one has \(g_3=0\), while \(g_0,g_1,g_2>0\). The finite part of the transformed polynomial is
$$
g_2x^2+g_1x+g_0.
$$
Its roots have negative real part because their sum is \(-g_1/g_2<0\) and their product is \(g_0/g_2>0\). Since \(g_2\ne0\), exactly one root of \(\chi_{r_*}\) is sent to infinity by the Cayley map, so that multiplier is
$$
z=-1
$$
and it is simple. The other two parasitic multipliers remain strictly inside the unit disk.

If \(0<r<r_*\), then \(g_3<0\), whereas \(G_r(0)=g_0>0\). Since \(G_r(x)\to-\infty\) as \(x\to+\infty\), \(G_r\) has a positive real zero. Under the inverse Cayley map this gives a real multiplier with \(|z|>1\). Hence zero-stability fails below \(r_*\).

Step 5: Translate the parasitic criterion back to the BDF4 recurrence

The original four-dimensional recurrence has the constant solution as its consistency mode, with period multiplier \(1\). The difference transformation in Step 1 removes only that mode, so the eigenvalues of \(M(r)\) are exactly the three parasitic period multipliers.

For \(r_*<r\leq1\), all three have modulus less than \(1\). At \(r=r_*\), the only unit-modulus parasitic multiplier is the simple multiplier \(-1\), distinct from the consistency multiplier \(1\). Therefore all solutions of the homogeneous BDF4 recurrence remain bounded precisely for
$$
r_*\leq r\leq1.
$$
Numerically, \(r_*\approx0.1420837844\).

Final Answer: $\boxed{\operatorname{root}_{(1/8,1/7)}Q}$

---

## Answer

$\operatorname{root}_{(1/8,1/7)}Q$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- variable-step backward differentiation formulas
- Lagrange differentiation weights
- Floquet monodromy
- Cayley transform
- Routh-Hurwitz stability criterion
