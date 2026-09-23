## Steps

Step 1: Reduce the two-grid cycle to a scalar cubic minimax problem

Put \(c=\cos\theta\) for \(0\leq\theta\leq\frac{\pi}{2}\), and use the harmonic basis
$
\{e^{ij\theta},e^{ij(\pi-\theta)}\}.
$
The fine-grid Poisson symbol is
$
\widehat A_h(\theta)=\operatorname{diag}(2(1-c),2(1+c)).
$
For linear interpolation the harmonic symbol is \(p=(1+c,1-c)^T\). Since full weighting is a scalar multiple of \(p^T\), the Galerkin coarse-grid correction is
$
C(c)=I-p(p^T\widehat A_hp)^{-1}p^T\widehat A_h
=\frac12
\begin{bmatrix}
1-c&-(1+c)\\
-(1-c)&1+c
\end{bmatrix}.
$
Weighted Jacobi has diagonal harmonic symbol
$
S_q(c)=\operatorname{diag}(1-q+qc,1-q-qc).
$
Hence the two-grid symbol is the rank-one matrix \(S_\nu(c)C(c)S_\omega(c)\). Its squared Euclidean norm is
$
F_{\omega,\nu}(t)
=\bigl((1-\nu)^2+\nu^2t\bigr)
\bigl((1-\omega)^2+(6\omega^2-6\omega+1)t+\omega^2t^2\bigr),
\qquad t=c^2\in[0,1].
$
Therefore
$
\rho(\omega,\nu)^2=\max_{0\leq t\leq1}F_{\omega,\nu}(t).
$

Step 2: Construct the two-contact candidate

Introduce the odds variables
$
a=\frac{1-\omega}{\omega},\qquad b=\frac{1-\nu}{\nu}.
$
Then
$
F_{\omega,\nu}(t)
=\frac{f_{a,b}(t)}{(1+a)^2(1+b)^2},
\qquad
f_{a,b}(t)=(t+b^2)\bigl(t^2+(a^2-4a+1)t+a^2\bigr).
$
At the candidate, the endpoint \(t=1\) and one interior point \(t=x\) have the same maximal value, while \(x\) is stationary. Since \(f_{a,b}\) is monic cubic, this is equivalent to
$
f_{a,b}(t)-m=(t-1)(t-x)^2.
$
Comparing the \(t^2\) and \(t\) coefficients gives
$
a^2-4a+1+b^2=-(2x+1),
$
$
a^2+(a^2-4a+1)b^2=x^2+2x.
$
Eliminating \(b^2\) yields two algebraic branches
$
x=-a^2+4a\pm\sqrt2(a-1)-2.
$
The branch relevant to \(0<x<1\), \(b^2>0\), and the small-contraction region is
$
x=-a^2+(4+\sqrt2)a-(2+\sqrt2),
$
$
b^2=a^2-(4+2\sqrt2)a+2+2\sqrt2.
$
It is feasible for
$
0.7286<a<0.8011.
$
The other sign can be feasible only for \(a>1.668\). On that branch
$
F_{\omega,\nu}(1)
=2(2\omega-1)^2(2\nu^2-2\nu+1)
\geq(2\omega-1)^2
=\left(\frac{a-1}{a+1}\right)^2>\frac1{16},
$
so it cannot compete with the candidate constructed below, whose squared factor is below \(0.019\).

Step 3: Determine the exact stationary point on the feasible branch

Write
$
H(a)=a^2-(4+2\sqrt2)a+2+2\sqrt2,\qquad b=\sqrt{H(a)}.
$
Along the equal-contact branch,
$
M(a)=F_{\omega,\nu}(1)
=\frac{2(1-a)^2(1+b^2)}{(1+a)^2(1+b)^2}.
$
Differentiating \(\log M(a)\), clearing the positive denominators, and using \(b^2=H(a)\) reduces the stationary equation to
$
u(a)b+2v(a)=0,
$
where
$
u(a)=a^2+(1-\sqrt2)a-8-5\sqrt2,
$
$
v(a)=a^3-\left(\frac{15}{2}+4\sqrt2\right)a^2
+\left(\frac{45}{2}+\frac{33}{2}\sqrt2\right)a
-13-\frac{19}{2}\sqrt2.
$
Thus
$
4v(a)^2-u(a)^2H(a)=R(a),
$
with \(R\) exactly the polynomial defined in the problem. On \(0.787<a<0.788\), one has \(u(a)<0<v(a)\), so \(R(a)=0\) is equivalent to the unsquared stationary equation.

Using \(1.4142<\sqrt2<1.4143\), direct interval bounds give
$
R''(a)>2500,\qquad R'(0.72)>1200
$
throughout \(0.72\leq a\leq0.81\). Hence \(R\) is strictly increasing there. Also
$
R(0.787)<-0.51,\qquad R(0.788)>1.06.
$
Therefore
$
a_*=\operatorname{root}_{(787/1000,197/250)}R
$
is the unique stationary point on the feasible plus branch. Define
$
b_*=\sqrt{H(a_*)},\quad
\omega_*=\frac1{1+a_*},\quad
\nu_*=\frac1{1+b_*},
$
and
$
x_*=-a_*^2+(4+\sqrt2)a_*-(2+\sqrt2).
$

Step 4: Certify global optimality and uniqueness

Let \(F(t)=F_{\omega,\nu}(t)\), and let \(M_*=F_{\omega_*,\nu_*}(1)=F_{\omega_*,\nu_*}(x_*)\). Choose
$
\lambda=
\frac{Q_1(2\nu_*-1)}
{Q_1(2\nu_*-1)-Q_x(\nu_*(1+x_*)-1)},
$
where
$
Q_x=(1-\omega_*)^2+(6\omega_*^2-6\omega_*+1)x_*+\omega_*^2x_*^2,
$
$
Q_1=(1-\omega_*)^2+(6\omega_*^2-6\omega_*+1)+\omega_*^2.
$
The isolating interval for \(a_*\) gives \(0.82<\lambda<0.88\). By construction,
$
\lambda\nabla F_{\omega,\nu}(x_*)\big|_{(\omega_*,\nu_*)}
+(1-\lambda)\nabla F_{\omega,\nu}(1)\big|_{(\omega_*,\nu_*)}=0;
$
the \(\nu\)-component is the displayed definition of \(\lambda\), and the \(\omega\)-component is the stationary equation from Step 3.

For arbitrary \(0<\omega,\nu<1\), set
$
G(\omega,\nu)=\lambda F_{\omega,\nu}(x_*)+(1-\lambda)F_{\omega,\nu}(1).
$
Since \(G\) is a convex combination of two sampled values,
$
\rho(\omega,\nu)^2\geq G(\omega,\nu).
$
As a quadratic in \(\nu\),
$
G=A(\omega)\nu^2-2C(\omega)\nu+C(\omega),
$
where, with
$
q_t(\omega)=(1-\omega)^2+(6\omega^2-6\omega+1)t+\omega^2t^2,
$
$
A(\omega)=\lambda(1+x_*)q_{x_*}(\omega)+2(1-\lambda)q_1(\omega),
$
$
C(\omega)=\lambda q_{x_*}(\omega)+(1-\lambda)q_1(\omega).
$
Both \(A\) and \(C\) are positive. Completing the square gives
$
G-M_*
=A\left(\nu-\frac{C}{A}\right)^2
+\frac{N(\omega)}{A},
\qquad
N=C(A-C)-AM_*.
$
The stationarity conditions imply that \(N\) has a double zero at \(\omega_*\). Expanding the displayed quadratic polynomials and dividing by this double factor gives
$
N(\omega)=(\omega-\omega_*)^2
\left(q_2\omega^2+q_1\omega+q_0\right).
$
Substitution of the exact quantities above, using only the isolating interval \(0.787<a_*<0.788\), gives the rigorous coefficient bounds
$
5.85<q_2<5.92,\qquad
-7.22<q_1<-7.15,\qquad
2.28<q_0<2.34.
$
Consequently
$
q_1^2-4q_2q_0<7.22^2-4(5.85)(2.28)<0,
$
so the quadratic factor is positive for every real \(\omega\). Thus \(G\geq M_*\), with equality only at \(\omega=\omega_*\) and \(\nu=C/A=\nu_*\). Therefore
$
\rho(\omega,\nu)^2\geq M_*
$
for every admissible pair, and equality is attained uniquely by \((\omega_*,\nu_*)\).

Step 5: Record the optimizer and convergence factor

The exact optimizer is
$
\omega_*=\frac1{1+a_*},
\qquad
\nu_*=
\frac1{1+\sqrt{a_*^2-(4+2\sqrt2)a_*+2+2\sqrt2}},
$
where
$
a_*=\operatorname{root}_{(787/1000,197/250)}R.
$
The exact optimal two-grid factor is
$
\rho_*=
\frac{|1-a_*|}{(1+a_*)(1+b_*)}
\sqrt{2(1+b_*^2)},
\qquad
b_*=\sqrt{a_*^2-(4+2\sqrt2)a_*+2+2\sqrt2}.
$
Numerically,
$
a_*\approx0.7873268113,\quad
\omega_*\approx0.5594947682,\quad
\nu_*\approx0.7883157487,\quad
\rho_*\approx0.1373545385.
$
Final Answer: $\boxed{\operatorname{root}_{(787/1000,197/250)}R}$

---

## Answer

$\operatorname{root}_{(787/1000,197/250)}R$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- local Fourier analysis
- Galerkin coarse-grid correction
- weighted Jacobi smoothing
- minimax equioscillation
- global lower-bound certificate
