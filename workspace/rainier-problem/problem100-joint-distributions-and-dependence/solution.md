## Steps

Step 1: Separate the endpoint tilt

Let $D_n=X_n-X_0$. From the displayed blocks of $\Omega_{n,q}$,
$$
x^T\Omega_{n,q}x
=\frac1n x_0^TA_qx_0
+\sum_{k=1}^n(x_k-x_{k-1})^TB_q(x_k-x_{k-1})
+\frac1{nq}(e^TD_n)^2.
$$
Therefore, before the last term is inserted, the law is a Gaussian random walk with
$$
X_0\sim N(0,nA_q^{-1}),\qquad
\Delta_k:=X_k-X_{k-1}\stackrel{\mathrm{iid}}{\sim}N(0,B_q^{-1}),
$$
and $X_0,\Delta_1,\ldots,\Delta_n$ independent. The actual law is obtained by the single tilt
$$
\exp\!\left(-\frac{(e^TD_n)^2}{2nq}\right),
$$
which depends only on $D_n=\sum_{k=1}^n\Delta_k$.

Step 2: Extract the limiting three-variable Gaussian channel

Use the orthonormal basis
$$
u=\frac1{\sqrt3}(1,1,1)^T,\qquad
w=\frac1{\sqrt6}(2,-1,-1)^T,\qquad
h=\frac1{\sqrt2}(0,1,-1)^T.
$$
In this basis put
$$
A=A_q^{-1}=\operatorname{diag}(9q,1,1),\qquad
R=B_q^{-1}=\operatorname{diag}(1,q,q),
$$
and
$$
e=\begin{pmatrix}1/\sqrt3\\ \sqrt{2/3}\\0\end{pmatrix},\qquad E=ee^T.
$$
Under the reference walk, $D_n\sim N(0,nR)$. The endpoint tilt changes only this factor, so under the given law
$$
\frac1n\operatorname{Cov}(D_n)=S,
\qquad
S^{-1}=R^{-1}+q^{-1}E.
$$
The Sherman--Morrison formula gives
$$
S=R-\frac{Ree^TR}{q+e^TRe},
\qquad
\det S=\frac{3q^3}{5q+1}.
$$

Now set
$$
T_n=\frac1n\sum_{k=1}^{n-1}X_k,\qquad G_n=T_n-X_0.
$$
With
$$
c_j=\frac{n-j}{n}\ (1\le j\le n-1),\qquad c_n=0,
$$
we have
$$
G_n=-\frac1nX_0+\sum_{j=1}^n c_j\Delta_j.
$$
Let
$$
a_n=\frac1n\sum_{j=1}^n c_j=\frac{n-1}{2n},\qquad
Z_n=\sum_{j=1}^n(c_j-a_n)\Delta_j,
$$
and $\eta_n=G_n-a_nD_n=-X_0/n+Z_n$. Since
$$
\sum_{j=1}^n(c_j-a_n)=0,
$$
we get $\operatorname{Cov}(Z_n,D_n)=0$; hence $Z_n$ and $D_n$ are independent Gaussian vectors, and the endpoint tilt preserves this independence. Also
$$
\sum_{j=1}^n c_j^2=\frac{(n-1)(2n-1)}{6n},
$$
so
$$
\operatorname{Cov}(Z_n)
=R\left(\sum c_j^2-na_n^2\right)
=\frac{n^2-1}{12n}R.
$$
Thus
$$
\frac1n\operatorname{Cov}(\eta_n)
=\frac{A}{n^2}+\frac{n^2-1}{12n^2}R\longrightarrow\frac1{12}R,
$$
and
$$
\frac1n\operatorname{Cov}(X_0,\eta_n)=-\frac{A}{n}\longrightarrow0.
$$
Finally
$$
Y_n=X_0+C_nD_n+\eta_n,\qquad C_n=a_nI-E\longrightarrow C:=\frac12I-E.
$$
Hence the scaled joint covariance converges to the Gaussian channel
$$
X\sim N(0,A),\qquad D\sim N(0,S),\qquad \eta\sim N(0,N),\qquad N:=R/12,
$$
with $X,D,\eta$ independent, and
$$
Z=X+D,\qquad Y=X+CD+\eta.
$$
Here $Z$ is the limiting version of $X_n$.

Step 3: Use posterior precision instead of four separate covariance determinants

Let $J$ be the conditional precision of $(X,Z)$ given $Y$, partitioned as
$$
J=\begin{pmatrix}J_{XX}&J_{XZ}\\J_{ZX}&J_{ZZ}\end{pmatrix}.
$$
For any jointly Gaussian pair with covariance $K=J^{-1}$, Schur complements give
$$
\det K_{XX}=\frac{\det J_{ZZ}}{\det J},\qquad
\det K_{ZZ}=\frac{\det J_{XX}}{\det J}.
$$
Since $\det K=1/\det J$,
$$
I(X;Z\mid Y)
=\frac12\log\frac{\det J_{XX}\det J_{ZZ}}{\det J}.
$$
Thus only the two diagonal precision blocks and one total determinant are needed.

Given $Y$, the posterior precision in variables $(X,D)$ is
$$
J_{XD}
=\begin{pmatrix}
A^{-1}+N^{-1}&N^{-1}C\\
CN^{-1}&S^{-1}+CN^{-1}C
\end{pmatrix}.
$$
Replacing $D$ by $Z-X$ is a determinant-one linear change of variables. Therefore
$$
J_{XX}=A^{-1}+S^{-1}+(I-C)N^{-1}(I-C),
$$
$$
J_{ZZ}=S^{-1}+CN^{-1}C.
$$
Using $N^{-1}=12R^{-1}$ and $S^{-1}=R^{-1}+q^{-1}E$, these become
$$
J_{ZZ}=\frac1{3q}
\begin{pmatrix}
4q+9&\sqrt2(3-2q)&0\\
\sqrt2(3-2q)&8q+6&0\\
0&0&12
\end{pmatrix},
$$
$$
J_{XX}=\frac1{9q}
\begin{pmatrix}
28(3q+1)&15\sqrt2(2q+3)&0\\
15\sqrt2(2q+3)&3(11q+54)&0\\
0&0&9(q+4)
\end{pmatrix}.
$$
Each has one $2\times2$ active block. The two needed factorizations are
$$
(4q+9)(8q+6)-2(3-2q)^2
=12(2q^2+10q+3),
$$
$$
28(3q+1)\,3(11q+54)-450(2q+3)^2
=6(162q^2+1522q+81).
$$
Consequently
$$
\det J_{ZZ}=\frac{16(2q^2+10q+3)}{3q^3},
$$
$$
\det J_{XX}=\frac{2(q+4)(162q^2+1522q+81)}{27q^3}.
$$

It remains to find $\det J$ without expanding a $6\times6$ matrix. Write
$$
P=\operatorname{diag}(A^{-1},S^{-1}),\qquad L=(I\ \ C).
$$
Then
$$
J_{XD}=P+L^TN^{-1}L.
$$
The matrix determinant lemma and Sylvester's identity give
$$
\det J
=\det P\,\det N^{-1}\,
\det\bigl(N+LP^{-1}L^T\bigr).
$$
But
$$
H:=N+LP^{-1}L^T=A+CSC+N=\operatorname{Cov}(Y).
$$
In the same basis,
$$
H=\frac1{12(5q+1)}
\begin{pmatrix}
548q^2+120q+1&\sqrt2q(2q-5)&0\\
\sqrt2q(2q-5)&6(q^2+12q+2)&0\\
0&0&4(q+3)(5q+1)
\end{pmatrix}.
$$
Its single active determinant reduces by
$$
6(548q^2+120q+1)(q^2+12q+2)-2q^2(2q-5)^2
=4(5q+1)M_q,
$$
where
$$
M_q=164q^3+1978q^2+363q+3.
$$
Hence
$$
\det H=\frac{(q+3)M_q}{108(5q+1)}.
$$
Moreover
$$
\det A^{-1}=\frac1{9q},\qquad
\det S^{-1}=\frac{5q+1}{3q^3},\qquad
\det N^{-1}=\frac{1728}{q^2}.
$$
Therefore
$$
\det J
=\frac{16(q+3)M_q}{27q^6}.
$$

Step 4: Pass the finite-$n$ mutual information through the limit

Let
$$
\Sigma_n=\frac1n\operatorname{Cov}(X_0,X_n,Y_n).
$$
Step 2 shows $\Sigma_n\to\Sigma$, the covariance of $(X,Z,Y)$ above. For $q>1$, $A\succ0$, $R\succ0$, $S=(R^{-1}+q^{-1}E)^{-1}\succ0$, and $N=R/12\succ0$. Since
$$
(X,D,\eta)\mapsto(X,Z,Y)
$$
is invertible, $\Sigma\succ0$. Thus the relevant Schur complements are positive definite, and inversion, determinants, and logarithms are continuous near $\Sigma$.

If $K_n$ is the conditional covariance of $(X_0,X_n)$ given $Y_n$, then $n^{-1}K_n\to K$, the conditional covariance of $(X,Z)$ given $Y$. The powers of $n$ cancel in the Gaussian determinant formula, so
$$
I(X_0;X_n\mid Y_n)
\longrightarrow I(X;Z\mid Y).
$$
Using Step 3,
$$
\frac{\det J_{XX}\det J_{ZZ}}{\det J}
=\frac{2(q+4)(2q^2+10q+3)(162q^2+1522q+81)}{3(q+3)(164q^3+1978q^2+363q+3)}.
$$

Final Answer: $\boxed{\frac{1}{2}\log\frac{2(q+4)(2q^2+10q+3)(162q^2+1522q+81)}{3(q+3)(164q^3+1978q^2+363q+3)}}$

---

## Answer

$\frac{1}{2}\log\frac{2(q+4)(2q^2+10q+3)(162q^2+1522q+81)}{3(q+3)(164q^3+1978q^2+363q+3)}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- conditional mutual information for Gaussian vectors
- posterior precision of a Gaussian channel
- matrix determinant lemma
- asymptotic covariance
