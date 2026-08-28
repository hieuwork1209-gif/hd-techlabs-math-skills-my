## Steps

Step 1: Separate the random-walk reference law from the endpoint perturbation

Let $D_n=X_n-X_0$. The path part of the precision matrix is
$$
x^{T}\Omega^{\mathrm{ref}}_{n,q}x
=\frac1n x_0^{T}A_qx_0+\sum_{k=1}^{n}(x_k-x_{k-1})^{T}B_q(x_k-x_{k-1}),
$$
and the only remaining term is
$$
\frac{1}{nq}(e^{T}D_n)^2.
$$
Thus the given law is the reference Gaussian law tilted by
$$
\exp\!\left(-\frac{(e^{T}D_n)^2}{2nq}\right).
$$

Under the reference law the innovations $\varepsilon_k=X_k-X_{k-1}$ are independent of $X_0$, with
$$
\operatorname{Cov}(X_0)=nA_q^{-1},
\qquad
\operatorname{Cov}(\varepsilon_k)=B_q^{-1}.
$$
If
$$
P=\frac13\mathbf1\mathbf1^{T},\qquad P_\perp=I_3-P,
$$
then
$$
A_q^{-1}=9qP+P_\perp,\qquad B_q^{-1}=P+qP_\perp.
$$
This is the main structural reduction: a Gaussian random walk plus one rank-one endpoint update.

Step 2: Reduce the asymptotics to three scalar modes

Use the orthonormal basis
$$
u=\frac1{\sqrt3}(1,1,1)^T,\quad
w=\frac1{\sqrt6}(2,-1,-1)^T,\quad
h=\frac1{\sqrt2}(0,1,-1)^T.
$$
The three reference modes are independent scalar random walks. Their initial/increment variance parameters $(c,r)$ are $(9q,1)$ on $u$ and $(1/q,q)$ on $w,h$. Put
$$
T_n=\frac1n\sum_{k=1}^{n-1}X_k.
$$
For one scalar mode,
$$
\frac1n\operatorname{Cov}(X_0,X_n,T_n,D_n)
\longrightarrow
r\begin{pmatrix}
c&c&c&0\\
c&c+1&c+\frac12&1\\
c&c+\frac12&c+\frac13&\frac12\\
0&1&\frac12&1
\end{pmatrix}.
$$
In the $(u,w,h)$ basis,
$$
e=\begin{pmatrix}1/\sqrt3\\ \sqrt{2/3}\\0\end{pmatrix},
\qquad
A=\operatorname{diag}(9q,1,1),
\qquad
R=\operatorname{diag}(1,q,q).
$$
Writing $E=ee^T$, define
$$
H=A+\frac13R-\frac12(RE+ER)+ERE,
$$
$$
V=A+R,\qquad
N=A+\frac12R-RE,\qquad
L=\frac12R-RE.
$$
These are the scaled limits of $\operatorname{Cov}(Y_n)$, $\operatorname{Cov}(X_n)$, $\operatorname{Cov}(X_n,Y_n)$, and $\operatorname{Cov}(D_n,Y_n)$. In particular,
$$
H=
\begin{pmatrix}
\frac{83q+1}{9}&\frac{\sqrt2(q-1)}{18}&0\\
\frac{\sqrt2(q-1)}{18}&\frac{q+11}{9}&0\\
0&0&\frac{q+3}{3}
\end{pmatrix}.
$$
Because $e_h=0$, every nontrivial correction is confined to the $(u,w)$ plane.

Step 3: Compute the reference conditional determinant ratio by Schur complements

Let
$$
H_0=H-A,\qquad H_n=H-N^TV^{-1}N.
$$
For a symmetric $2\times2$ matrix
$$
M=\begin{pmatrix}a&b\\b&c\end{pmatrix},
$$
we use only
$$
\det M=ac-b^2,\qquad
x^TM^{-1}x=\frac{cx_1^2-2bx_1x_2+ax_2^2}{ac-b^2}.
$$
The active blocks needed for $H_n$ are
$$
N_{uw}=\begin{pmatrix}
9q+\frac16&-\frac{\sqrt2}{3}\\
-\frac{\sqrt2q}{3}&1-\frac q6
\end{pmatrix},
\qquad
V_{uw}=\operatorname{diag}(9q+1,q+1).
$$
Substitution in $H_n=H-N^TV^{-1}N$ gives
$$
(H_n)_{uw}=\begin{pmatrix}
\dfrac{324q^2+263q+3}{36(q+1)(9q+1)}&
\dfrac{2\sqrt2q(27q+13)}{9(q+1)(9q+1)}\\[6pt]
\dfrac{2\sqrt2q(27q+13)}{9(q+1)(9q+1)}&
\dfrac{q(27q^2+543q+124)}{36(q+1)(9q+1)}
\end{pmatrix}.
$$
Put $P_n=324q^2+2963q+124$. Applying $ac-b^2$ directly to this block gives
$$
\det(H_n)_{uw}=\frac{qP_n}{432(q+1)(9q+1)}.
$$
The $h$ entry is independent of that block and equals
$$
(H_n)_{hh}=\frac{q(q+4)}{12(q+1)}.
$$
Hence
$$
\det H_n=
\frac{q^2(q+4)P_n}{5184(q+1)^2(9q+1)}.
$$
The same $2\times2$ identity applied to $H$ and $H_0$ gives
$$
\det H=\frac{(q+3)(55q^2+610q+7)}{162},
\qquad
\det H_0=\frac{q(q^2+4q+1)}{162}.
$$

Let $\overline K_{00}$, $\overline K_{nn}$ and $\overline K$ be the scaled reference conditional covariance matrices of $X_0$, $X_n$, and $(X_0,X_n)$ given $Y_n$. Schur-complement determinant identities therefore give
$$
\det\overline K_{00}
=\det A\,\frac{\det H_0}{\det H}
=\frac{9q^2(q^2+4q+1)}{(q+3)(55q^2+610q+7)},
$$
and, since $\det V=(9q+1)(q+1)^2$,
$$
\det\overline K_{nn}
=\det V\,\frac{\det H_n}{\det H}
=\frac{q^2(q+4)P_n}{32(q+3)(55q^2+610q+7)}.
$$

The shear $(X_0,X_n,T_n)\mapsto(X_0,X_n,Y_n)$ has determinant $1$. For a scalar mode, the limiting covariance determinant of $(X_0,X_n,T_n)$ is $cr^3/12$, so multiplication over the three independent modes gives
$$
\det\overline{\operatorname{Cov}}(X_0,X_n,Y_n)=\frac{q^5}{192},
$$
and therefore
$$
\det\overline K
=\frac{27q^5}{32(q+3)(55q^2+610q+7)}.
$$
Thus the reference determinant ratio is
$$
R_0=
\frac{(q+4)(q^2+4q+1)P_n}{3q(q+3)(55q^2+610q+7)}.
$$

Step 4: Apply the rank-one endpoint update

Let $d_n=e^TD_n$. We need the scaled reference conditional variances
$$
v=\lim_{n\to\infty}\frac1n\operatorname{Var}(d_n\mid Y_n),
\quad
v_0=\lim_{n\to\infty}\frac1n\operatorname{Var}(d_n\mid Y_n,X_0),
\quad
v_n=\lim_{n\to\infty}\frac1n\operatorname{Var}(d_n\mid Y_n,X_n).
$$
Gaussian conditioning gives
$$
v=e^T(R-LH^{-1}L^T)e,
\qquad
v_0=e^T(R-LH_0^{-1}L^T)e.
$$
For the last one set
$$
R_n=R-RV^{-1}R,\qquad L_n=L-RV^{-1}N,
$$
so that
$$
v_n=e^T(R_n-L_nH_n^{-1}L_n^T)e.
$$
Only the $(u,w)$ plane contributes. To keep the calculation transparent without expanding large polynomials, we solve each active $2\times2$ system first and then take one dot product.

For $v$, put
$$
y=L^Te=
\begin{pmatrix}
\dfrac{\sqrt3(1-4q)}{18}\\[4pt]
-\dfrac{\sqrt6(q+2)}{18}
\end{pmatrix},
\qquad e^TRe=\frac{2q+1}{3}.
$$
The required active inverse is
$$
H_{uw}^{-1}
=\frac1{55q^2+610q+7}
\begin{pmatrix}
6(q+11)&-3\sqrt2(q-1)\\
-3\sqrt2(q-1)&6(83q+1)
\end{pmatrix},
$$
and its action on $y$ simplifies before the final contraction:
$$
H_{uw}^{-1}y=
\begin{pmatrix}
-\dfrac{\sqrt3(q^2+14q-3)}{55q^2+610q+7}\\[5pt]
-\dfrac{\sqrt6(54q^2+113q+1)}{2(55q^2+610q+7)}
\end{pmatrix}.
$$
Thus
$$
y^TH_{uw}^{-1}y
=\frac{58q^3+276q^2+201q+5}{6(55q^2+610q+7)},
$$
so
$$
v=\frac{54q^3+758q^2+349q+3}{2(55q^2+610q+7)}.
$$

For $v_0$ the vector $y$ is unchanged, while
$$
(H_0)_{uw}^{-1}
=\frac1{q^2+4q+1}
\begin{pmatrix}
6(q+2)&-3\sqrt2(q-1)\\
-3\sqrt2(q-1)&6(2q+1)
\end{pmatrix},
$$
$$
(H_0)_{uw}^{-1}y=
\begin{pmatrix}
-\dfrac{\sqrt3q(q+2)}{q^2+4q+1}\\[5pt]
-\dfrac{\sqrt6(5q+1)}{2(q^2+4q+1)}
\end{pmatrix}.
$$
Hence
$$
y^T(H_0)_{uw}^{-1}y
=\frac{(q+2)(2q+1)^2}{6(q^2+4q+1)},
\qquad
v_0=\frac{q(2q+1)}{2(q^2+4q+1)}.
$$

For $v_n$, the active blocks are
$$
(R_n)_{uw}=\begin{pmatrix}
\dfrac{9q}{9q+1}&0\\[4pt]
0&\dfrac{q}{q+1}
\end{pmatrix},
$$
$$
(L_n)_{uw}=\begin{pmatrix}
-\dfrac{15q}{2(9q+1)}&-\dfrac{3\sqrt2q}{9q+1}\\[6pt]
-\dfrac{\sqrt2q}{3(q+1)}&-\dfrac{7q}{6(q+1)}
\end{pmatrix}.
$$
Therefore
$$
e^T(R_n)_{uw}e=\frac{q(27q+11)}{3(q+1)(9q+1)},
$$
and
$$
y_n:=(L_n)_{uw}^Te=
\begin{pmatrix}
-\dfrac{\sqrt3q(81q+49)}{18(q+1)(9q+1)}\\[6pt]
-\dfrac{\sqrt6q(81q+25)}{18(q+1)(9q+1)}
\end{pmatrix}.
$$
The inverse of the active block from Step 3 is
$$
(H_n)_{uw}^{-1}
=\frac1{P_n}
\begin{pmatrix}
12(27q^2+543q+124)&-96\sqrt2(27q+13)\\[4pt]
-96\sqrt2(27q+13)&\dfrac{12(324q^2+263q+3)}q
\end{pmatrix}.
$$
Again its action is much simpler than a full expansion:
$$
(H_n)_{uw}^{-1}y_n=
\begin{pmatrix}
-\dfrac{2\sqrt3q(81q+292)}{P_n}\\[5pt]
-\dfrac{2\sqrt6(324q+25)}{P_n}
\end{pmatrix}.
$$
Consequently
$$
y_n^T(H_n)_{uw}^{-1}y_n
=\frac{q\bigl(q(81q+49)(81q+292)+2(81q+25)(324q+25)\bigr)}{3(q+1)(9q+1)P_n},
$$
and subtraction gives
$$
v_n=\frac{q(81q+38)}{P_n}.
$$

Conditioned on $Y_n$, the tilt from Step 1 adds $\alpha aa^T$ to the endpoint precision, where
$$
\alpha=\frac1{nq},
\qquad
a=\begin{pmatrix}-e\\e\end{pmatrix}.
$$
The matrix determinant lemma changes the joint conditional determinant by $(1+\alpha\operatorname{Var}(d_n\mid Y_n))^{-1}$, and the analogous marginal factors are obtained after also conditioning on $X_0$ or $X_n$. Hence
$$
R
=R_0\frac{(1+v_0/q)(1+v_n/q)}{1+v/q}
=\frac{2(q+4)(2q^2+10q+3)(162q^2+1522q+81)}{3(q+3)(164q^3+1978q^2+363q+3)}.
$$
For jointly Gaussian vectors,
$$
I(X_0;X_n\mid Y_n)=\frac12\log R.
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
