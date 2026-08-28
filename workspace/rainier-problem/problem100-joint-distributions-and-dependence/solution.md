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
This converts the problem into a Gaussian random walk plus one rank-one endpoint update.

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
R=\operatorname{diag}(1,q,q),
$$
where $A$ and $R$ are the scaled covariance matrices of $X_0$ and $D_n$. Writing $E=ee^T$, define
$$
H=A+\frac13R-\frac12(RE+ER)+ERE,
$$
$$
V=A+R,\qquad
N=A+\frac12R-RE,\qquad
L=\frac12R-RE.
$$
Then $H,V,N,L$ are respectively the scaled limits of
$\operatorname{Cov}(Y_n)$, $\operatorname{Cov}(X_n)$,
$\operatorname{Cov}(X_n,Y_n)$, and $\operatorname{Cov}(D_n,Y_n)$.
In particular,
$$
H=
\begin{pmatrix}
\frac{83q+1}{9}&\frac{\sqrt2(q-1)}{18}&0\\
\frac{\sqrt2(q-1)}{18}&\frac{q+11}{9}&0\\
0&0&\frac{q+3}{3}
\end{pmatrix}.
$$

Step 3: Compute the reference conditional determinant ratio by Schur complements

Let
$$
H_0=H-A,\qquad H_n=H-N^TV^{-1}N.
$$
The $h$-mode is already diagonal, while every effect of $E$ lies in
$\operatorname{span}\{u,w\}$. Hence all nontrivial algebra is only $2\times2$.
For
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
Substituting them into $H_n=H-N^TV^{-1}N$ gives the active block
$$
(H_n)_{uw}=\begin{pmatrix}
\dfrac{324q^2+263q+3}{36(q+1)(9q+1)}&
\dfrac{2\sqrt2q(27q+13)}{9(q+1)(9q+1)}\\[6pt]
\dfrac{2\sqrt2q(27q+13)}{9(q+1)(9q+1)}&
\dfrac{q(27q^2+543q+124)}{36(q+1)(9q+1)}
\end{pmatrix}.
$$
Its determinant is therefore
$$
\begin{aligned}
\det(H_n)_{uw}
&=\frac{q(324q^2+263q+3)(27q^2+543q+124)-128q^2(27q+13)^2}
{1296(q+1)^2(9q+1)^2}\\
&=\frac{q(324q^2+2963q+124)}{432(q+1)(9q+1)}.
\end{aligned}
$$
The remaining diagonal entry is
$$
(H_n)_{hh}
=\frac{q+3}{3}-\frac{(1+q/2)^2}{q+1}
=\frac{q(q+4)}{12(q+1)}.
$$
Applying the same two formulas to $H$ and $H_0$, and multiplying the active determinant above by $(H_n)_{hh}$, gives
$$
\det H=\frac{(q+3)(55q^2+610q+7)}{162},
\qquad
\det H_0=\frac{q(q^2+4q+1)}{162},
$$
$$
\det H_n=
\frac{q^2(q+4)(324q^2+2963q+124)}
{5184(q+1)^2(9q+1)}.
$$
No larger determinant is needed.

Let $\overline K_{00}$, $\overline K_{nn}$ and $\overline K$ be the scaled reference conditional covariance matrices of $X_0$, $X_n$, and $(X_0,X_n)$ given $Y_n$. Schur-complement determinant identities give
$$
\det\overline K_{00}
=\det A\,\frac{\det H_0}{\det H}
=\frac{9q^2(q^2+4q+1)}
{(q+3)(55q^2+610q+7)},
$$
and, since $\det V=(9q+1)(q+1)^2$,
$$
\begin{aligned}
\det\overline K_{nn}
&=\det V\,\frac{\det H_n}{\det H}\\
&=(9q+1)(q+1)^2
\frac{q^2(q+4)(324q^2+2963q+124)}{5184(q+1)^2(9q+1)}
\frac{162}{(q+3)(55q^2+610q+7)}\\
&=\frac{q^2(q+4)(324q^2+2963q+124)}
{32(q+3)(55q^2+610q+7)}.
\end{aligned}
$$

The shear $(X_0,X_n,T_n)\mapsto(X_0,X_n,Y_n)$ has determinant $1$.
For a scalar mode, the limiting covariance determinant of
$(X_0,X_n,T_n)$ is $cr^3/12$. Multiplying the three modes gives
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
\frac{(q+4)(q^2+4q+1)(324q^2+2963q+124)}
{3q(q+3)(55q^2+610q+7)}.
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
Gaussian conditioning gives them directly in matrix form:
$$
v=e^T(R-LH^{-1}L^T)e,
\qquad
v_0=e^T(R-LH_0^{-1}L^T)e.
$$
For the last one set
$$
R_n=R-RV^{-1}R,\qquad
L_n=L-RV^{-1}N;
$$
then
$$
v_n=e^T(R_n-L_nH_n^{-1}L_n^T)e.
$$
Again only the $(u,w)$ block contributes. First,
$$
e^TRe=\frac{2q+1}{3},
\qquad
y:=L^Te=
\begin{pmatrix}
\dfrac{\sqrt3(1-4q)}{18}\\[4pt]
-\dfrac{\sqrt6(q+2)}{18}
\end{pmatrix}.
$$
From the active block of $H$ in Step 2,
$$
H_{uw}^{-1}
=\frac1{55q^2+610q+7}
\begin{pmatrix}
6(q+11)&-3\sqrt2(q-1)\\
-3\sqrt2(q-1)&6(83q+1)
\end{pmatrix}.
$$
Thus
$$
y^TH_{uw}^{-1}y
=\frac{58q^3+276q^2+201q+5}{6(55q^2+610q+7)},
$$
and hence
$$
\begin{aligned}
v
&=\frac{2q+1}{3}
-\frac{58q^3+276q^2+201q+5}{6(55q^2+610q+7)}\\
&=\frac{54q^3+758q^2+349q+3}{2(55q^2+610q+7)}.
\end{aligned}
$$
For $v_0$ the active vector is the same $y$, while
$$
(H_0)_{uw}^{-1}
=\frac1{q^2+4q+1}
\begin{pmatrix}
6(q+2)&-3\sqrt2(q-1)\\
-3\sqrt2(q-1)&6(2q+1)
\end{pmatrix}.
$$
Therefore
$$
y^T(H_0)_{uw}^{-1}y
=\frac{(q+2)(2q+1)^2}{6(q^2+4q+1)},
$$
so
$$
\begin{aligned}
v_0
&=\frac{2q+1}{3}
-\frac{(q+2)(2q+1)^2}{6(q^2+4q+1)}\\
&=\frac{q(2q+1)}{2(q^2+4q+1)}.
\end{aligned}
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
Consequently
$$
e^T(R_n)_{uw}e
=\frac{q(27q+11)}{3(q+1)(9q+1)},
$$
and the active contraction vector is
$$
y_n:=(L_n)_{uw}^Te
=\begin{pmatrix}
-\dfrac{\sqrt3q(81q+49)}{18(q+1)(9q+1)}\\[6pt]
-\dfrac{\sqrt6q(81q+25)}{18(q+1)(9q+1)}
\end{pmatrix}.
$$
Writing $P_n=324q^2+2963q+124$, the inverse of the active block found in Step 3 is
$$
(H_n)_{uw}^{-1}
=\frac1{P_n}
\begin{pmatrix}
12(27q^2+543q+124)&-96\sqrt2(27q+13)\\[4pt]
-96\sqrt2(27q+13)&\dfrac{12(324q^2+263q+3)}q
\end{pmatrix}.
$$
The quadratic form now simplifies to
$$
y_n^T(H_n)_{uw}^{-1}y_n
=\frac{q(6561q^3+80109q^2+34558q+1250)}
{3(q+1)(9q+1)(324q^2+2963q+124)}.
$$
Subtracting it from $e^T(R_n)_{uw}e$ gives
$$
\begin{aligned}
v_n
&=\frac{q(27q+11)}{3(q+1)(9q+1)}
-\frac{q(6561q^3+80109q^2+34558q+1250)}
{3(q+1)(9q+1)(324q^2+2963q+124)}\\
&=\frac{q(81q+38)}{324q^2+2963q+124}.
\end{aligned}
$$

Conditioned on $Y_n$, the tilt in Step 1 adds
$\alpha aa^T$ to the endpoint precision, where
$$
\alpha=\frac1{nq},
\qquad
a=\begin{pmatrix}-e\\e\end{pmatrix}.
$$
The matrix determinant lemma therefore changes the joint conditional determinant by
$(1+\alpha\operatorname{Var}(d_n\mid Y_n))^{-1}$.
Applying the same lemma after also conditioning on $X_0$ or on $X_n$ gives the two marginal correction factors. Consequently the limiting determinant ratio is
$$
R
=R_0\frac{(1+v_0/q)(1+v_n/q)}{1+v/q}
=\frac{2(q+4)(2q^2+10q+3)(162q^2+1522q+81)}
{3(q+3)(164q^3+1978q^2+363q+3)}.
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
