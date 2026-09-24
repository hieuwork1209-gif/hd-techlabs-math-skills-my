## Steps

Step 1: Determine the directional transition from the logarithmic potential
Set
$$
\rho_x=\frac{1-\omega_x}{\omega_x}
=
\begin{cases}
\frac{1}{3},&S_x=R,\\
3,&S_x=L.
\end{cases}
$$
The stationary law is $\pi=(\theta,1-\theta)$. The environment transition matrix is
$$
P_{\alpha,\theta}
=
\alpha I+(1-\alpha)
\begin{pmatrix}
\theta&1-\theta\\
\theta&1-\theta
\end{pmatrix}.
$$
This form gives $\pi P_{\alpha,\theta}=\pi$. It is reversible because
$$
\theta(1-\alpha)(1-\theta)
=
(1-\theta)(1-\alpha)\theta.
$$
For $0<\alpha<1$ and $0<\theta<1$ the state chain is irreducible, hence stationary ergodic.

For a fixed environment, let $h(x)=P_\omega^x(T_b<T_a)$ for $a<x<b$. The harmonic equation
$$
h(x)=\omega_xh(x+1)+(1-\omega_x)h(x-1)
$$
implies, with $\Delta_x=h(x)-h(x-1)$,
$$
\Delta_{x+1}=\rho_x\Delta_x.
$$
Thus the scale increments are successive products of the local odds. By the ergodic theorem,
$$
\frac{1}{n}\sum_{j=1}^n\log\rho_j
\longrightarrow
\theta\log\frac{1}{3}+(1-\theta)\log3
=(1-2\theta)\log3.
$$
Hence the walk is transient to $+\infty$ for $\theta>\frac{1}{2}$ and to $-\infty$ for $\theta<\frac{1}{2}$.

At $\theta=\frac{1}{2}$, the state chain switches state with probability $(1-\alpha)/2$ at every step. Successive run lengths are therefore independent geometric random variables with the same law. Pairing an $R$-run with the following $L$-run makes the potential change by $\log3$ times the difference of two independent identically distributed geometric variables. These paired increments form a symmetric nondegenerate one-dimensional random walk, so their partial sums visit both signs infinitely often. Both scale tails diverge, and the walk is recurrent. Therefore
$$
\theta_{\rm dir}=\frac{1}{2}.
$$

Step 2: Derive the right second-moment criterion
Assume $\theta>\frac{1}{2}$, so $T_1<\infty$ almost surely. Let $\tau_x$ be the time needed to hit $x+1$ starting from $x$, and set
$$
u_x=E_\omega^x\tau_x,
\qquad
v_x=E_\omega^x\tau_x^2.
$$
A first-step decomposition gives
$$
u_x
=
1+(1-\omega_x)(u_{x-1}+u_x),
$$
hence
$$
u_x
=
1+\rho_x+\rho_xu_{x-1}.
$$
Iterating this nonnegative recursion to the left yields
$$
u_0
=
1+2\sum_{k=0}^{\infty}\rho_0\rho_{-1}\cdots\rho_{-k}.
$$

To control the second moment, condition on the first step. If the first step is left, the return time from $x-1$ to $x$ and the subsequent fresh crossing from $x$ to $x+1$ are independent under the quenched law by the strong Markov property. Thus
$$
v_x
=
1+(1-\omega_x)
\left(
v_{x-1}+v_x+2u_{x-1}+2u_x+2u_{x-1}u_x
\right).
$$
Using $\rho_x=(1-\omega_x)/\omega_x$ and the recursion for $u_x$ gives
$$
v_x
=
\rho_xv_{x-1}
+1+3\rho_x+2\rho_x^2
+4\rho_x(1+\rho_x)u_{x-1}
+2\rho_x^2u_{x-1}^2.
$$

Let
$$
D=\operatorname{diag}\left(\frac{1}{3},3\right).
$$
Because the environment is reversible, conditional on $S_x=i$ the previous state $S_{x-1}$ is distributed by the $i$th row of $P_{\alpha,\theta}$. Define the state-conditioned vectors
$
m_i=\mathbb E_\theta[u_x\mid S_x=i],
\qquad
s_i=\mathbb E_\theta[u_x^2\mid S_x=i],
\qquad
t_i=\mathbb E_\theta[v_x\mid S_x=i].
$
For a vector $z$, write $z^{\circ2}$ for its componentwise square.
From the recursion for $u_x$,
$$
m
=
\mathbf1+d+DP_{\alpha,\theta}m,
$$
where $d=(1/3,3)^T$. Squaring the same recursion gives
$$
s
=
(\mathbf1+d)^{\circ2}
+2D(I+D)P_{\alpha,\theta}m
+D^2P_{\alpha,\theta}s.
$$
The displayed recursion for $v_x$ gives
$$
t
=
\mathbf1+3d+2d^{\circ2}
+4D(I+D)P_{\alpha,\theta}m
+2D^2P_{\alpha,\theta}s
+DP_{\alpha,\theta}t.
$$

The decisive operator is therefore the squared-odds transfer matrix. If
$
r(P_{\alpha,\theta}D^2)<1,
$
then there are constants $C>0$ and $0<q<1$ such that
$
\mathbb E_\theta\left[
\left(\rho_0\rho_{-1}\cdots\rho_{-k}\right)^2
\right]
\leq Cq^k.
$
Cauchy-Schwarz gives
$
\mathbb E_\theta\left[
\rho_0\rho_{-1}\cdots\rho_{-k}
\right]
\leq C^{1/2}q^{k/2},
$
so the first-product series also converges. Hence $m$ is finite and, by Perron-Frobenius, $r(P_{\alpha,\theta}D)<1$. The displayed equation for $s$ then has a finite nonnegative solution because $r(D^2P_{\alpha,\theta})=r(P_{\alpha,\theta}D^2)<1$, and the equation for $t$ has a finite solution because $r(DP_{\alpha,\theta})=r(P_{\alpha,\theta}D)<1$. Therefore $\mathbb E_\theta T_1^2=\pi t<\infty$.

Conversely, Jensen gives $v_0\geq u_0^2$. Since all terms in the series for $u_0$ are nonnegative,
$$
u_0^2
\geq
4\sum_{k=0}^{\infty}
\left(\rho_0\rho_{-1}\cdots\rho_{-k}\right)^2.
$$
Averaging and using reversibility gives
$$
\mathbb E_\theta u_0^2
\geq
4\sum_{k=0}^{\infty}
\pi D^2(P_{\alpha,\theta}D^2)^k\mathbf1.
$$
If $r(P_{\alpha,\theta}D^2)\geq1$, this positive Perron series diverges, so $\mathbb E_\theta T_1^2=\infty$. Therefore
$$
\mathbb E_\theta T_1^2<\infty
\quad\Longleftrightarrow\quad
r(P_{\alpha,\theta}D^2)<1.
$$

Now $\det D^2=1$, while the eigenvalues of $P_{\alpha,\theta}$ are $1$ and $\alpha$, so
$$
\det(P_{\alpha,\theta}D^2)=\alpha.
$$
Also
$$
\operatorname{tr}(P_{\alpha,\theta}D^2)
=
9+\frac{\alpha}{9}
-\frac{80(1-\alpha)\theta}{9}.
$$
The characteristic polynomial is $\lambda^2-\operatorname{tr}(P_{\alpha,\theta}D^2)\lambda+\alpha$. With fixed determinant $\alpha$, its larger root is strictly increasing in the trace, so the Perron root decreases strictly with $\theta$ and equals $1$ exactly when
$$
0
=
\det(I-P_{\alpha,\theta}D^2)
=
\frac{8\left(10(1-\alpha)\theta+\alpha-9\right)}{9}.
$$
Hence
$$
\mathbb E_\theta T_1^2<\infty
\quad\Longleftrightarrow\quad
\theta>\frac{9-\alpha}{10(1-\alpha)},
$$
so
$$
\theta_+=\frac{9-\alpha}{10(1-\alpha)}.
$$

Step 3: Derive the left second-moment threshold
For left passage, reflection replaces $\rho_x$ by $\rho_x^{-1}$. The derivation in Step 2 applies with
$$
D^{-2}=\operatorname{diag}\left(9,\frac{1}{9}\right).
$$
Thus
$$
\mathbb E_\theta T_{-1}^2<\infty
\quad\Longleftrightarrow\quad
r(P_{\alpha,\theta}D^{-2})<1.
$$
Again
$$
\det(P_{\alpha,\theta}D^{-2})=\alpha,
$$
and
$$
\operatorname{tr}(P_{\alpha,\theta}D^{-2})
=
\frac{1+81\alpha+80(1-\alpha)\theta}{9}.
$$
With determinant fixed at $\alpha$, the larger root is strictly increasing in the trace, so this Perron root increases strictly with $\theta$. It equals $1$ exactly when
$$
0
=
\det(I-P_{\alpha,\theta}D^{-2})
=
\frac{8\left(1-9\alpha-10(1-\alpha)\theta\right)}{9}.
$$
Therefore
$$
\mathbb E_\theta T_{-1}^2<\infty
\quad\Longleftrightarrow\quad
\theta<\frac{1-9\alpha}{10(1-\alpha)},
$$
so
$$
\theta_- = \frac{1-9\alpha}{10(1-\alpha)}.
$$
The hypothesis $0<\alpha<\frac{1}{9}$ ensures
$$
0<\theta_-<\frac{1}{2}<\theta_+<1.
$$

Step 4: Assemble the second-moment phase transitions
The logarithmic potential gives $\theta_{\rm dir}=\frac{1}{2}$, while the squared-odds transfer operators give
$$
\theta_- = \frac{1-9\alpha}{10(1-\alpha)},
\qquad
\theta_+ = \frac{9-\alpha}{10(1-\alpha)}.
$$
Therefore
$$
(\theta_-,\theta_{\rm dir},\theta_+)
=
\left(
\frac{1-9\alpha}{10(1-\alpha)},
\frac{1}{2},
\frac{9-\alpha}{10(1-\alpha)}
\right).
$$
Final Answer: $\boxed{\left(\frac{1-9\alpha}{10(1-\alpha)},\frac{1}{2},\frac{9-\alpha}{10(1-\alpha)}\right)}$

---

## Answer

$\left(\frac{1-9\alpha}{10(1-\alpha)},\frac{1}{2},\frac{9-\alpha}{10(1-\alpha)}\right)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- stationary markov chains
- random walk in random environment
- quenched crossing-time recursion
- matrix geometric series
- perron spectral radius
