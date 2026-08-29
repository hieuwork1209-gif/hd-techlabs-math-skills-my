## Steps

Step 1: Isolate the endpoint tilt

Let $D_n=X_n-X_0$. The precision quadratic form is
$$
x^T\Omega^{\mathrm{ref}}_{n,q}x
=\frac1n x_0^TA_qx_0+\sum_{k=1}^n(x_k-x_{k-1})^TB_q(x_k-x_{k-1}),
$$
plus
$$
\frac1{nq}(e^TD_n)^2.
$$
Thus the given law is the Gaussian random-walk reference law tilted by
$$
\exp\!\left(-\frac{(e^TD_n)^2}{2nq}\right).
$$
The tilt depends only on the endpoint increment $D_n$.

Step 2: Compute the weighted-increment innovation and the limiting channel

Use the orthonormal basis
$$
u=\frac1{\sqrt3}(1,1,1)^T,\qquad
w=\frac1{\sqrt6}(2,-1,-1)^T,\qquad
h=\frac1{\sqrt2}(0,1,-1)^T.
$$
In this basis
$$
A_q^{-1}=A=\operatorname{diag}(9q,1,1),\qquad
B_q^{-1}=R=\operatorname{diag}(1,q,q),
$$
and the original coordinate vector $e=(1,0,0)^T$ has coordinates
$$
e=\begin{pmatrix}1/\sqrt3\\ \sqrt{2/3}\\0\end{pmatrix},\qquad E=ee^T.
$$
Hence under the reference law
$$
X_0\sim N(0,nA),\qquad
\Delta_k:=X_k-X_{k-1}\stackrel{\mathrm{iid}}{\sim}N(0,R),
$$
with $X_0,\Delta_1,\ldots,\Delta_n$ independent. Therefore
$$
D_n=\sum_{k=1}^n\Delta_k\sim N(0,nR).
$$
The endpoint tilt adds $q^{-1}E$ to the scaled precision of $D_n$, so exactly
$$
\frac1n\operatorname{Cov}(D_n)=\widetilde R
=(R^{-1}+q^{-1}E)^{-1}
=R-\frac{Ree^TR}{q+e^TRe},
$$
that is
$$
\widetilde R=
\begin{pmatrix}
\dfrac{5q}{5q+1}&-\dfrac{\sqrt2q}{5q+1}&0\\[5pt]
-\dfrac{\sqrt2q}{5q+1}&\dfrac{q(3q+1)}{5q+1}&0\\[5pt]
0&0&q
\end{pmatrix},
\qquad
\det\widetilde R=\frac{3q^3}{5q+1}.
$$

Now
$$
T_n=\frac1n\sum_{k=1}^{n-1}X_k,\qquad G_n=T_n-X_0.
$$
Writing
$$
c_j=\frac{n-j}{n}\quad(1\le j\le n-1),\qquad c_n=0,
$$
gives
$$
G_n=-\frac1nX_0+\sum_{j=1}^n c_j\Delta_j.
$$
Put
$$
a_n=\frac1n\sum_{j=1}^n c_j=\frac{n-1}{2n},\qquad
Z_n=\sum_{j=1}^n(c_j-a_n)\Delta_j,
$$
and $\eta_n=G_n-a_nD_n=-X_0/n+Z_n$. Since
$$
\operatorname{Cov}(Z_n,D_n)
=R\sum_{j=1}^n(c_j-a_n)=0,
$$
$Z_n$ and $D_n$ are independent Gaussian vectors. Also
$$
\sum_{j=1}^n c_j^2=\frac{(n-1)(2n-1)}{6n},
$$
so
$$
\operatorname{Cov}(Z_n)
=R\left(\sum c_j^2-na_n^2\right)
=\frac{n^2-1}{12n}R.
$$
Consequently
$$
\frac1n\operatorname{Cov}(\eta_n)
=\frac{A}{n^2}+\frac{n^2-1}{12n^2}R
\longrightarrow \frac1{12}R,
$$
while
$$
\frac1n\operatorname{Cov}(X_0,\eta_n)
=-\frac{A}{n}\longrightarrow0.
$$
The tilt changes only the law of $D_n$, so the independence of $D_n$ from $(X_0,Z_n)$ is preserved.

Finally
$$
Y_n=X_0+C_nD_n+\eta_n,\qquad
C_n=a_nI-E\longrightarrow C:=\frac12I-E.
$$
Thus the scaled joint covariance converges to that of the limiting Gaussian channel
$$
X_0\sim N(0,A),\qquad D\sim N(0,\widetilde R),\qquad
\eta\sim N(0,R/12),
$$
with $X_0,D,\eta$ independent and
$$
Y=X_0+CD+\eta.
$$

Step 3: Display the covariance matrices and compute all four determinants

In the $(u,w,h)$ basis,
$$
C=
\begin{pmatrix}
1/6&-\sqrt2/3&0\\
-\sqrt2/3&-1/6&0\\
0&0&1/2
\end{pmatrix}.
$$
Let
$$
H_0=C\widetilde RC^T+\frac1{12}R,\qquad
H=A+H_0,\qquad
V=A+\widetilde R.
$$
Direct multiplication gives
$$
H_0=
\begin{pmatrix}
\dfrac{8q^2+12q+1}{12(5q+1)}&
\dfrac{\sqrt2q(2q-5)}{12(5q+1)}&0\\[5pt]
\dfrac{\sqrt2q(2q-5)}{12(5q+1)}&
\dfrac{q(q+2)}{2(5q+1)}&0\\[5pt]
0&0&q/3
\end{pmatrix},
$$
$$
H=
\begin{pmatrix}
\dfrac{548q^2+120q+1}{12(5q+1)}&
\dfrac{\sqrt2q(2q-5)}{12(5q+1)}&0\\[5pt]
\dfrac{\sqrt2q(2q-5)}{12(5q+1)}&
\dfrac{q^2+12q+2}{2(5q+1)}&0\\[5pt]
0&0&(q+3)/3
\end{pmatrix},
$$
and
$$
V=
\begin{pmatrix}
\dfrac{q(45q+14)}{5q+1}&-\dfrac{\sqrt2q}{5q+1}&0\\[5pt]
-\dfrac{\sqrt2q}{5q+1}&\dfrac{3q^2+6q+1}{5q+1}&0\\[5pt]
0&0&q+1
\end{pmatrix}.
$$
Set
$$
D_q=27q^2+57q+14,\qquad
M_q=164q^3+1978q^2+363q+3.
$$
Using $ac-b^2$ on each $(u,w)$ block,
$$
\det(H_0)_{uw}
=\frac{q\{3(q+2)(8q^2+12q+1)-q(2q-5)^2\}}
{72(5q+1)^2}
=\frac{q(2q^2+10q+3)}{36(5q+1)},
$$
$$
\det(H)_{uw}
=\frac{3(548q^2+120q+1)(q^2+12q+2)-q^2(2q-5)^2}
{72(5q+1)^2}
=\frac{M_q}{36(5q+1)},
$$
and
$$
\det(V)_{uw}
=\frac{q\{(45q+14)(3q^2+6q+1)-2q\}}{(5q+1)^2}
=\frac{qD_q}{5q+1}.
$$
Multiplying by the $h$-entries yields
$$
\det H_0=\frac{q^2(2q^2+10q+3)}{108(5q+1)},
$$
$$
\det H=\frac{(q+3)M_q}{108(5q+1)},\qquad
\det V=\frac{q(q+1)D_q}{5q+1}.
$$

Conditioning on $X_n=X_0+D$, the covariance of $D$ is
$$
Q=(A^{-1}+\widetilde R^{-1})^{-1}
=
\begin{pmatrix}
\dfrac{9q(3q+5)}{D_q}&-\dfrac{9\sqrt2q}{D_q}&0\\[5pt]
-\dfrac{9\sqrt2q}{D_q}&\dfrac{3q(9q+4)}{D_q}&0\\[5pt]
0&0&\dfrac{q}{q+1}
\end{pmatrix}.
$$
Therefore
$$
H_n:=\operatorname{Cov}(Y\mid X_n)
=(C-I)Q(C-I)^T+\frac1{12}R
$$
has
$$
(H_n)_{uw}=
\begin{pmatrix}
\dfrac{162q^2+172q+7}{6D_q}&
\dfrac{\sqrt2q(216q+77)}{12D_q}\\[6pt]
\dfrac{\sqrt2q(216q+77)}{12D_q}&
\dfrac{q(9q^2+190q+54)}{4D_q}
\end{pmatrix},
$$
and
$$
(H_n)_{hh}=\frac{q(q+4)}{12(q+1)}.
$$
Its active determinant is
$$
\det(H_n)_{uw}
=\frac{q\{3(162q^2+172q+7)(9q^2+190q+54)-q(216q+77)^2\}}
{72D_q^2}
=\frac{q(162q^2+1522q+81)}{72D_q}.
$$
Hence
$$
\det H_n
=\frac{q^2(q+4)(162q^2+1522q+81)}{864(q+1)D_q}.
$$

For a jointly Gaussian pair $(Z,Y)$, the two Schur-complement factorizations of the joint covariance determinant give
$$
\det\operatorname{Cov}(Z\mid Y)
=\det\operatorname{Cov}(Z)\,
\frac{\det\operatorname{Cov}(Y\mid Z)}{\det\operatorname{Cov}(Y)}.
$$
Thus, with $\overline K_{00}$ and $\overline K_{nn}$ denoting the limiting scaled conditional covariances of $X_0$ and $X_n$ given $Y$,
$$
\det\overline K_{00}
=\det A\,\frac{\det H_0}{\det H}
=\frac{9q^3(2q^2+10q+3)}{(q+3)M_q},
$$
$$
\det\overline K_{nn}
=\det V\,\frac{\det H_n}{\det H}
=\frac{q^3(q+4)(162q^2+1522q+81)}{8(q+3)M_q}.
$$

Step 4: Justify the limiting Gaussian formula and assemble the joint determinant

Let
$$
\Sigma^{(n)}=\frac1n\operatorname{Cov}(X_0,X_n,Y_n).
$$
Step 2 gives $\Sigma^{(n)}\to\Sigma$, where $\Sigma$ is the covariance of the limiting channel above. For $q>1$, $A\succ0$, $R\succ0$, and
$$
\widetilde R=(R^{-1}+q^{-1}E)^{-1}\succ0.
$$
Hence $A\oplus\widetilde R\oplus(R/12)\succ0$. The linear map
$$
(X_0,D,\eta)\longmapsto(X_0,X_n,Y)
$$
is invertible, so $\Sigma\succ0$. Therefore its $Y$-block and all corresponding conditional-covariance Schur complements are positive definite. Inversion, Schur complements, determinants, and $\log$ are continuous on this positive-definite neighborhood.

If $K^{(n)}$ is the conditional covariance of $(X_0,X_n)$ given $Y_n$, with diagonal blocks $K^{(n)}_{00},K^{(n)}_{nn}$, then
$$
\frac1nK^{(n)}\to\overline K,\qquad
\frac1nK^{(n)}_{00}\to\overline K_{00},\qquad
\frac1nK^{(n)}_{nn}\to\overline K_{nn}.
$$
For every $n$,
$$
I(X_0;X_n\mid Y_n)
=\frac12\log
\frac{\det K^{(n)}_{00}\det K^{(n)}_{nn}}{\det K^{(n)}}
=\frac12\log
\frac{\det(n^{-1}K^{(n)}_{00})\det(n^{-1}K^{(n)}_{nn})}
{\det(n^{-1}K^{(n)})},
$$
because the powers $n^3n^3/n^6$ cancel. Continuity now justifies passage to the limit.

The limiting linear map has determinant $1$, so independence of $X_0,D,\eta$ gives
$$
\det\overline{\operatorname{Cov}}(X_0,X_n,Y)
=\det A\,\det\widetilde R\,\det(R/12)
=\frac{q^6}{64(5q+1)}.
$$
Therefore
$$
\det\overline K
=\frac{\det\overline{\operatorname{Cov}}(X_0,X_n,Y)}{\det H}
=\frac{27q^6}{16(q+3)M_q}.
$$
Substitution gives
$$
\frac{\det\overline K_{00}\det\overline K_{nn}}{\det\overline K}
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
- Gaussian innovation factorization
- asymptotic covariance
- Schur complements for conditional covariance
