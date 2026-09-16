## Steps

Step 1: Use four-point alternation as an exact optimality certificate
Write a three-step Richardson polynomial as
$$
p(\lambda)=(1-\alpha\lambda)(1-\beta\lambda)(1-\delta\lambda)
=1+a\lambda+b\lambda^2+c\lambda^3,
$$
with $\alpha,\beta,\delta>0$. Suppose a cubic $p$ with constant term $1$ has four increasing points
$$
0<x_1<x_2<x_3<x_4
$$
in $E_\gamma$ such that
$$
p(x_1)=C,\qquad p(x_2)=-C,\qquad p(x_3)=C,\qquad p(x_4)=-C,
$$
and $|p|\le C$ on $E_\gamma$. If another cubic $q$ with $q(0)=1$ had smaller sup norm, then $q-p$ would have alternating signs at the four $x_j$, hence at least three positive zeros, in addition to its zero at $0$. That is impossible for a nonzero cubic. The same sign argument with weak inequalities gives uniqueness at norm $C$.

Thus every feasible four-point alternating candidate is the unique minimax cubic among all cubics with constant term $1$. In each candidate below the displayed alternating signs also force one root in each of three positive intervals between active points, so the cubic factors as three positive Richardson factors.

Step 2: Find the first regime and its exit point
Before the moving endpoint becomes active, the relevant pattern is
$$
p(1)=C,\qquad p(2)=-C,\qquad p(r)=C,\qquad p(6)=-C,
$$
where the third active point is an interior stationary point, so $p'(r)=0$. Eliminating $a,b,c,C$ from these five equations gives
$$
(r-1)(r^2-14r+44)=0.
$$
The only root in $(\frac92,6)$ is
$$
r=7-\sqrt5.
$$
For this choice,
$$
\begin{aligned}
p_L(\lambda)&=1-\frac{793+47\sqrt5}{739}\lambda
+\frac{845+147\sqrt5}{2956}\lambda^2
-\frac{69+19\sqrt5}{2956}\lambda^3,\\
C_L&=\frac{5(28-3\sqrt5)}{739}.
\end{aligned}
$$
Its derivative factors as
$$
p_L'(\lambda)
=-\frac{3(69+19\sqrt5)}{2956}
\left(\lambda-7+\sqrt5\right)
\left(\lambda-3+\frac{\sqrt5}{3}\right).
$$
The smaller stationary point $3-\sqrt5/3$ lies in $(2,\frac92)$, hence in the spectral gap throughout the parameter range. Therefore, for
$$
\frac92<\gamma<7-\sqrt5,
$$
we have $|p_L|\le C_L$ on both spectral intervals and
$$
\mathcal A_\gamma=\{1,2,7-\sqrt5,6\}.
$$
The first transition occurs when the moving endpoint reaches that stationary active point:
$$
\gamma_1=7-\sqrt5.
$$
At $\gamma=\gamma_1$, the active set is still $\{1,2,\gamma_1,6\}$, with $p'(\gamma_1)=0$.

Step 3: Track the four endpoint-active regime
For $\gamma>\gamma_1$, impose the alternating endpoint pattern
$$
p(1)=C,\qquad p(2)=-C,\qquad p(\gamma)=C,\qquad p(6)=-C.
$$
Solving the four linear equations gives, with
$$
D=19\gamma^2-128\gamma+60,
$$
$$
\begin{aligned}
a&=-\frac{8(2\gamma^2-11\gamma-11)}D,\\
b&=\frac{2(\gamma^2+\gamma-51)}D,\\
c&=-\frac{2(\gamma-7)}D,\\
C&=\frac{5(\gamma-6)(\gamma-2)}D.
\end{aligned}
$$
On our interval $D<0$. Two derivative values that detect the loss of feasibility are
$$
p'(\gamma)
=-\frac{2(\gamma-1)(\gamma^2-14\gamma+44)}D,
$$
and
$$
p'(2)
=-\frac{8(\gamma^2-9\gamma+19)}D.
$$
For $\gamma_1<\gamma<\frac{9+\sqrt5}{2}$, the two stationary points lie strictly in the gap $(2,\gamma)$, so $p$ decreases from $C$ to $-C$ on $[1,2]$ and from $C$ to $-C$ on $[\gamma,6]$. Hence
$$
\mathcal A_\gamma=\{1,2,\gamma,6\}.
$$
The first stationary point reaches $2$ exactly when
$$
\gamma^2-9\gamma+19=0.
$$
The root in the present parameter range is
$$
\gamma_2=\frac{9+\sqrt5}{2}.
$$
At $\gamma=\gamma_2$, the active set is $\{1,2,\gamma_2,6\}$ and $p'(2)=0$.

Step 4: Verify the final regime and exclude another transition before $17/3$
For $\gamma>\gamma_2$, the negative active point moves into the interior of $[1,2]$. Write it as $m$. The correct alternating system is
$$
p(1)=C,\qquad p(m)=-C,\qquad p(\gamma)=C,\qquad p(6)=-C,
\qquad p'(m)=0.
$$
Eliminating the coefficients gives
$$
\gamma^2-2\gamma m-5\gamma+m^2+10m-5=0.
$$
The branch entering $[1,2]$ at $\gamma_2$ is
$$
m_\gamma=\gamma-5+\sqrt{5(6-\gamma)}.
$$
The other stationary point is
$$
n_\gamma=\frac{\gamma+7+\sqrt{5(6-\gamma)}}3.
$$
For
$$
\gamma_2<\gamma\le\frac{17}{3},
$$
we have
$$
1<m_\gamma<2<n_\gamma<\gamma<6.
$$
Thus $m_\gamma$ is the only stationary point in $E_\gamma$, except that the right component is monotone decreasing. The only remaining possible obstruction is the unused endpoint $2$. Direct substitution shows that equality $p(2)=C$ can next occur only when
$$
(\gamma-6)(\gamma^2+6\gamma-71)=0,
$$
whose first root above $\gamma_2$ is
$$
-3+4\sqrt5>\frac{17}{3}.
$$
Hence no further change occurs in the prescribed range, and
$$
\mathcal A_\gamma=\{1,m_\gamma,\gamma,6\}
$$
for $\gamma_2<\gamma<17/3$.

The two and only two interior transition values are therefore
$$
\gamma_1=7-\sqrt5,
\qquad
\gamma_2=\frac{9+\sqrt5}{2}.
$$

Final Answer: $\boxed{\left(7-\sqrt5,\frac{9+\sqrt5}{2}\right)}$

---

## Answer

$\left(7-\sqrt5,\frac{9+\sqrt5}{2}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonstationary Richardson iteration
- cubic minimax equioscillation
- active-set phase transition
- stationary-point migration
