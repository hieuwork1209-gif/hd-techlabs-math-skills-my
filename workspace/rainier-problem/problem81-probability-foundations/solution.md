## Steps

Step 1: Find the critical Jordan coordinates
Let
$$
X_n=(R_n,G_n,B_n)
$$
be the urn composition after $n$ draws, with initial state
$$
X_0=(4,4,4).
$$
The deterministic replacement matrix is
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

The fluctuation directions are forced by the non-Perron part of $M$. Put
$$
u=
\begin{pmatrix}
1\\-1\\0
\end{pmatrix},
\qquad
v=
\begin{pmatrix}
1\\1\\-2
\end{pmatrix}.
$$
Direct multiplication gives
$$
Mu=6u,
\qquad
Mv=6v+6u.
$$
Thus $u,v$ form a Jordan chain at the critical eigenvalue $6=\frac{12}{2}$. Define the corresponding linear statistics
$$
U_n=X_nu=R_n-G_n,
$$
$$
V_n=X_nv=R_n+G_n-2B_n.
$$

If the drawn color is respectively red, green, or blue, the increments of $(U_n,V_n)$ are
$$
(6,12),
\qquad
(-6,0),
\qquad
(0,-12).
$$
Therefore, conditional on the current urn,
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
Since $U_0=V_0=0$, induction gives
$$
\mathbb E U_n=\mathbb E V_n=0.
$$

Step 2: Derive the coupled second-moment recurrences
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
36\frac{R_n+G_n}{S_n}
=
24+12\frac{V_n}{S_n},
$$
$$
\mathbb E[\Delta U_n\Delta V_n\mid\mathcal F_n]
=
72\frac{R_n}{S_n}
=
24+36\frac{U_n}{S_n}+12\frac{V_n}{S_n},
$$
and
$$
\mathbb E[(\Delta V_n)^2\mid\mathcal F_n]
=
144\frac{R_n+B_n}{S_n}
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
Using
$
U_{n+1}=U_n+\Delta U_n,
\qquad
V_{n+1}=V_n+\Delta V_n,
$
we obtain
$
\mathbb E[U_{n+1}^2\mid\mathcal F_n]
=
U_n^2
+
\frac{12}{S_n}U_n^2
+
24
+
12\frac{V_n}{S_n},
$
$
\mathbb E[U_{n+1}V_{n+1}\mid\mathcal F_n]
=
U_nV_n
+
\frac{6}{S_n}U_n^2
+
\frac{12}{S_n}U_nV_n
+
24
+
36\frac{U_n}{S_n}
+
12\frac{V_n}{S_n},
$
and
$
\mathbb E[V_{n+1}^2\mid\mathcal F_n]
=
V_n^2
+
\frac{12}{S_n}U_nV_n
+
\frac{12}{S_n}V_n^2
+
96
+
72\frac{U_n}{S_n}
-
24\frac{V_n}{S_n}.
$
Taking expectations and using $\mathbb E U_n=\mathbb E V_n=0$ gives
$
A_{n+1}
=
\left(1+\frac{12}{S_n}\right)A_n+24,
$$
$$
C_{n+1}
=
\left(1+\frac{12}{S_n}\right)C_n
+
\frac{6}{S_n}A_n
+
24,
$$
and
$$
D_{n+1}
=
\left(1+\frac{12}{S_n}\right)D_n
+
\frac{12}{S_n}C_n
+
96.
$$
Since $S_n=12(n+1)$, these become
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

Step 3: Solve the nested critical asymptotics
Normalize by the deterministic linear factor:
$$
a_n=\frac{A_n}{n+1},
\qquad
c_n=\frac{C_n}{n+1},
\qquad
d_n=\frac{D_n}{n+1}.
$$
The three recurrences become
$$
a_{n+1}=a_n+\frac{24}{n+2},
$$
$$
c_{n+1}
=
c_n
+
\frac{a_n/2+24}{n+2},
$$
and
$$
d_{n+1}
=
d_n
+
\frac{c_n+96}{n+2}.
$$
Since $a_0=c_0=d_0=0$,
$$
a_n
=
24\sum_{j=2}^{n+1}\frac{1}{j}
=
24\log n+O(1).
$$
Hence
$$
c_n
=
\sum_{k=0}^{n-1}
\frac{a_k/2+24}{k+2}
=
\sum_{k=2}^{n+1}
\frac{12\log k+O(1)}{k}
=
6(\log n)^2+O(\log n).
$$
The estimate
$$
\sum_{k\leq n}\frac{\log k}{k}
=
\frac{1}{2}(\log n)^2+O(1)
$$
follows from comparison with the integral of $(\log x)/x$.

Similarly,
$$
d_n
=
\sum_{k=0}^{n-1}
\frac{c_k+96}{k+2}
=
\sum_{k=2}^{n+1}
\frac{6(\log k)^2+O(\log k)}{k}
=
2(\log n)^3+O((\log n)^2),
$$
using
$$
\sum_{k\leq n}\frac{(\log k)^2}{k}
=
\frac{1}{3}(\log n)^3+O((\log n)^2).
$$
Therefore
$$
A_n
\sim
24n\log n,
$$
$$
C_n
\sim
6n(\log n)^2,
$$
and
$$
D_n
\sim
2n(\log n)^3.
$$

Step 4: Express the covariance matrix in an orthonormal fluctuation basis
The centered urn vector
$$
X_n-\mathbb E X_n
$$
always lies in the plane orthogonal to $(1,1,1)$ because the total $S_n$ is deterministic. The vectors
$$
e_1=\frac{u}{\sqrt{2}},
\qquad
e_2=\frac{v}{\sqrt{6}}
$$
form an orthonormal basis of that plane.

In this basis, the covariance operator is represented by
$$
K_n
=
\begin{pmatrix}
A_n/2&C_n/\sqrt{12}\\
C_n/\sqrt{12}&D_n/6
\end{pmatrix}.
$$
Let
$$
0<\lambda_n^-\leq\lambda_n^+
$$
be its two eigenvalues, which are exactly the two nonzero eigenvalues of the covariance matrix of $X_n$.

From Step 3,
$$
\frac{A_n}{2}
\sim
12n\log n,
$$
$$
\frac{C_n}{\sqrt{12}}
\sim
\sqrt{3}\,n(\log n)^2,
$$
and
$$
\frac{D_n}{6}
\sim
\frac{1}{3}n(\log n)^3.
$$
The lower-order entries are negligible relative to the bottom-right entry, so
$$
\lambda_n^+
\sim
\frac{1}{3}n(\log n)^3.
$$

Step 5: Recover the smaller covariance eigenvalue from the determinant
The determinant of $K_n$ is
$$
\det K_n
=
\frac{A_nD_n-C_n^2}{12}.
$$
Using the three asymptotics from Step 3,
$$
A_nD_n-C_n^2
\sim
(24\cdot2-6^2)n^2(\log n)^4
=
12n^2(\log n)^4.
$$
Thus
$$
\det K_n
\sim
n^2(\log n)^4.
$$
Since
$$
\lambda_n^-\lambda_n^+=\det K_n
$$
and
$$
\lambda_n^+
\sim
\frac{1}{3}n(\log n)^3,
$$
we obtain
$$
\lambda_n^-
\sim
3n\log n.
$$
Hence the requested two limits are
$$
\lim_{n\to\infty}
\frac{\lambda_n^-}{n\log n}
=
3,
\qquad
\lim_{n\to\infty}
\frac{\lambda_n^+}{n(\log n)^3}
=
\frac{1}{3}.
$$
Final Answer: $\boxed{\left(3,\frac{1}{3}\right)}$

---

## Answer

$\left(3,\frac{1}{3}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- generalized polya urns
- jordan chain decomposition
- conditional moment recursions
- critical logarithmic scaling
- covariance eigenvalue asymptotics
