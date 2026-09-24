## Steps

Step 1: Find the critical Jordan coordinates
Let
$$
X_n=(R_n,G_n,B_n)
$$
be the urn composition after $n$ draws, with
$$
X_0=(4,4,4).
$$
The replacement matrix is
$$
M=
\begin{pmatrix}
9&3&0\\
1&7&4\\
2&2&8
\end{pmatrix}.
$$
Every row sum is $12$, so the total number of balls is deterministic:
$$
S_n=R_n+G_n+B_n=12(n+1).
$$

The non-Perron part of $M$ has a Jordan chain at the critical eigenvalue $6$. Indeed, for
$$
u=
\begin{pmatrix}
1\\-1\\0
\end{pmatrix},
\qquad
v=
\begin{pmatrix}
1\\1\\-2
\end{pmatrix},
$$
we have
$$
Mu=6u,
\qquad
Mv=6v+6u.
$$
Define
$$
U_n=X_nu=R_n-G_n,
\qquad
V_n=X_nv=R_n+G_n-2B_n.
$$
If the drawn color is red, green, or blue, the corresponding increments of $(U_n,V_n)$ are
$$
(6,12),
\qquad
(-6,0),
\qquad
(0,-12).
$$
Hence
$$
\mathbb E[\Delta U_n\mid\mathcal F_n]
=
\frac{6U_n}{S_n},
$$
and
$$
\mathbb E[\Delta V_n\mid\mathcal F_n]
=
\frac{6(U_n+V_n)}{S_n}.
$$
Since $U_0=V_0=0$,
$$
\mathbb E U_n=\mathbb E V_n=0.
$$

Step 2: Obtain the covariance scales needed for normalization
Because
$$
R_n
=
\frac{S_n}{3}
+
\frac{U_n}{2}
+
\frac{V_n}{6},
$$
$$
G_n
=
\frac{S_n}{3}
-
\frac{U_n}{2}
+
\frac{V_n}{6},
$$
and
$$
B_n
=
\frac{S_n}{3}
-
\frac{V_n}{3},
$$
the conditional quadratic increment moments are
$$
\mathbb E[(\Delta U_n)^2\mid\mathcal F_n]
=
24+12\frac{V_n}{S_n},
$$
$$
\mathbb E[\Delta U_n\Delta V_n\mid\mathcal F_n]
=
24+36\frac{U_n}{S_n}+12\frac{V_n}{S_n},
$$
and
$$
\mathbb E[(\Delta V_n)^2\mid\mathcal F_n]
=
96+72\frac{U_n}{S_n}-24\frac{V_n}{S_n}.
$$

Set
$$
A_n=\mathbb E[U_n^2],
\qquad
C_n=\mathbb E[U_nV_n],
\qquad
D_n=\mathbb E[V_n^2].
$$
Expanding
$$
U_{n+1}=U_n+\Delta U_n,
\qquad
V_{n+1}=V_n+\Delta V_n
$$
and taking expectations gives
$$
A_{n+1}
=
\frac{n+2}{n+1}A_n+24,
$$
$$
C_{n+1}
=
\frac{n+2}{n+1}C_n
+
\frac{A_n}{2(n+1)}
+
24,
$$
and
$$
D_{n+1}
=
\frac{n+2}{n+1}D_n
+
\frac{C_n}{n+1}
+
96.
$$
Put
$
a_n=\frac{A_n}{n+1},
\qquad
c_n=\frac{C_n}{n+1},
\qquad
d_n=\frac{D_n}{n+1}.
$
Then
$
a_{n+1}=a_n+\frac{24}{n+2},
$
$
c_{n+1}
=
c_n+\frac{a_n/2+24}{n+2},
$
and
$
d_{n+1}
=
d_n+\frac{c_n+96}{n+2}.
$
Since $a_0=c_0=d_0=0$,
$
a_n=24\log n+O(1).
$
Using
$
\sum_{k\leq n}\frac{\log k}{k}
=
\frac{1}{2}(\log n)^2+O(1)
$
and
$
\sum_{k\leq n}\frac{(\log k)^2}{k}
=
\frac{1}{3}(\log n)^3+O((\log n)^2),
$
the next two recurrences give
$
c_n=6(\log n)^2+O(\log n),
$
and
$
d_n=2(\log n)^3+O((\log n)^2).
$
Therefore
$
A_n
=
24n\log n+O(n),
$
$
C_n
=
6n(\log n)^2+O(n\log n),
$
and
$
D_n
=
2n(\log n)^3+O(n(\log n)^2).
$
Therefore, with
$$
L_n=\log n,
$$
the natural normalization is
$$
\left(
\frac{U_n}{\sqrt{nL_n}},
\frac{V_n}{\sqrt{nL_n^3}}
\right),
$$
whose limiting covariance matrix, if a joint limit exists, must be
$$
\Gamma=
\begin{pmatrix}
24&6\\
6&2
\end{pmatrix}.
$$

Step 3: Write the exact martingale array representation
Define centered innovations
$$
\eta_{n+1}^U
=
\Delta U_n
-
\mathbb E[\Delta U_n\mid\mathcal F_n],
$$
$$
\eta_{n+1}^V
=
\Delta V_n
-
\mathbb E[\Delta V_n\mid\mathcal F_n].
$$
Then
$$
\begin{pmatrix}
U_{n+1}\\
V_{n+1}
\end{pmatrix}
=
\begin{pmatrix}
a_n&0\\
b_n&a_n
\end{pmatrix}
\begin{pmatrix}
U_n\\
V_n
\end{pmatrix}
+
\begin{pmatrix}
\eta_{n+1}^U\\
\eta_{n+1}^V
\end{pmatrix},
$$
where
$$
a_n=1+\frac{1}{2(n+1)},
\qquad
b_n=\frac{1}{2(n+1)}.
$$
For $0\leq k<n$, put
$$
P_{k,n}
=
\prod_{j=k}^{n-1}a_j
$$
and
$$
H_{k,n}
=
\sum_{j=k}^{n-1}\frac{b_j}{a_j}.
$$
Because the nilpotent part of the transition matrices squares to zero,
$$
U_n
=
\sum_{k=0}^{n-1}
P_{k+1,n}\eta_{k+1}^U
$$
and
$$
V_n
=
\sum_{k=0}^{n-1}
P_{k+1,n}
\left(
\eta_{k+1}^V
+
H_{k+1,n}\eta_{k+1}^U
\right).
$$

The products satisfy
$$
P_{k+1,n}^2
=
\frac{n}{k+1}
\left(
1+O\left(\frac{1}{k+1}\right)
\right)
$$
uniformly once $k$ is large, because
$$
2\log P_{k+1,n}
=
\sum_{j=k+1}^{n-1}
2\log\left(1+\frac{1}{2(j+1)}\right)
=
\log\frac{n}{k+1}
+
O\left(\frac{1}{k+1}\right).
$$
Also
$$
H_{k+1,n}
=
\frac{1}{2}\log\frac{n}{k+1}
+
O\left(\frac{1}{k+1}\right).
$$

Step 4: Prove the joint Gaussian limit
For fixed $n$, the summands in Step 3 form a two-dimensional martingale-difference array after the deterministic normalization
$$
\xi_{n,k}
=
\begin{pmatrix}
\frac{P_{k+1,n}\eta_{k+1}^U}{\sqrt{nL_n}}\\
\frac{P_{k+1,n}(\eta_{k+1}^V+H_{k+1,n}\eta_{k+1}^U)}
{\sqrt{nL_n^3}}
\end{pmatrix}.
$$
The urn increments are bounded, and the estimates for $P_{k+1,n}$ and $H_{k+1,n}$ give
$$
\max_{0\leq k<n}\|\xi_{n,k}\|
=
O\left(\frac{1}{\sqrt{L_n}}\right)
\to0.
$$

The conditional variance of $\eta_{k+1}^U$ is
$$
24+12\frac{V_k}{S_k}
-
\left(\frac{U_k}{2(k+1)}\right)^2.
$$
The state-dependent correction is negligible in all three normalized quadratic-variation sums. For example,
$$
\mathbb E|V_k|
\leq
\sqrt{D_k}
=
O\left(\sqrt{k(\log k)^3}\right),
$$
so its contribution to the first coordinate is bounded in expectation by
$$
\frac{C}{nL_n}
\sum_{k=1}^{n}
\frac{n}{k}
\frac{\sqrt{k(\log k)^3}}{k}
=
O\left(\frac{1}{L_n}\right).
$$
The same estimate with one or two additional factors of $H_{k+1,n}$ shows that the corrections vanish for the cross and second-coordinate quadratic variations as well. Terms containing $\eta^V$ without the Jordan factor have one or two fewer powers of $\log n$ and are also negligible at these scales.

Therefore the conditional quadratic variation converges in probability to
$$
\Gamma
=
\begin{pmatrix}
24&6\\
6&2
\end{pmatrix}.
$$
Indeed, the three leading sums reduce to
$$
\frac{24}{L_n}
\sum_{k\leq n}\frac{1}{k}
\to24,
$$
$$
\frac{12}{L_n^2}
\sum_{k\leq n}
\frac{\log(n/k)}{k}
\to6,
$$
and
$$
\frac{6}{L_n^3}
\sum_{k\leq n}
\frac{\log^2(n/k)}{k}
\to2.
$$

For completeness, the needed martingale central limit step follows from conditional characteristic functions. For a fixed vector $t\in\mathbb R^2$,
$$
\mathbb E[
e^{i t^T\xi_{n,k}}
\mid\mathcal F_k]
=
1
-
\frac{1}{2}
t^T
\mathbb E[
\xi_{n,k}\xi_{n,k}^T
\mid\mathcal F_k]
t
+
r_{n,k},
$$
where bounded increments give
$$
\sum_k|r_{n,k}|
\leq
C\max_k\|\xi_{n,k}\|
\sum_k
\mathbb E[
\|\xi_{n,k}\|^2
\mid\mathcal F_k]
\to0
$$
in probability. Iterating conditional expectations therefore gives convergence of characteristic functions to
$$
\exp\left(-\frac{1}{2}t^T\Gamma t\right).
$$
Hence
$$
\left(
\frac{U_n}{\sqrt{n\log n}},
\frac{V_n}{\sqrt{n(\log n)^3}}
\right)
\Longrightarrow
N(0,\Gamma).
$$

Step 5: Evaluate the limiting quadrant probability
After standardizing the two coordinates of the limiting Gaussian, the correlation is
$$
\rho
=
\frac{6}{\sqrt{24\cdot2}}
=
\frac{\sqrt{3}}{2}.
$$
Let $X,Z$ be independent standard normal variables. A standard bivariate normal pair with correlation $\rho$ can be written as
$$
(X,\rho X+\sqrt{1-\rho^2}Z).
$$
Here
$$
\rho X+\sqrt{1-\rho^2}Z
=
\frac{\sqrt{3}}{2}X+\frac{1}{2}Z.
$$
Because $(X,Z)$ is rotationally symmetric in the plane, the event
$$
X>0,
\qquad
\frac{\sqrt{3}}{2}X+\frac{1}{2}Z>0
$$
is a wedge of angle
$$
\frac{5\pi}{6}.
$$
Its probability is therefore
$$
\frac{5\pi/6}{2\pi}
=
\frac{5}{12}.
$$
Since the limiting Gaussian assigns probability zero to the boundary lines, convergence in distribution gives
$$
\mathbb P(U_n>0,V_n>0)
\to
\frac{5}{12}.
$$
In the original urn variables this is exactly the event
$$
R_n>G_n,
\qquad
R_n+G_n>2B_n.
$$
Final Answer: $\boxed{\frac{5}{12}}$

---

## Answer

$\frac{5}{12}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- generalized polya urns
- jordan chain decomposition
- martingale difference arrays
- multivariate central limit theorem
- gaussian quadrant probabilities
