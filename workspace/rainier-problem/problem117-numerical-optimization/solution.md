## Steps

Step 1: Use constrained alternation
For four Richardson steps write
$$
p(\lambda)=\prod_{j=1}^4(1-\alpha_j\lambda).
$$
The budget constraint $\sum_j\alpha_j=2$ is exactly
$$
p(0)=1,\qquad p'(0)=-2.
$$
Conversely, once a feasible quartic with these two conditions has four positive zeros, it factors into four positive Richardson factors whose step sizes sum to $2$.

The fixed derivative changes the alternation count. Suppose a feasible quartic $p$ has four increasing active points $x_1<\cdots<x_4$ in $E_\gamma$ with alternating values $\pm C$. If another feasible quartic $q$ had strictly smaller norm, then $q-p$ would change sign in each of the three gaps $(x_j,x_{j+1})$, giving three positive zeros. But $q-p$ also has a double zero at $0$ because both its value and derivative vanish there. Hence a nonzero quartic would have at least five zeros, impossible. The weak-sign version gives uniqueness. Thus four-point alternation is the exact optimality certificate for this constrained problem.

Step 2: Construct the first regime and evaluate the left-end contraction
For $\frac92<\gamma<\frac{24}{5}$, the active pattern is
$$
p(m)=-C,\qquad p(\gamma)=C,\qquad p(r)=-C,\qquad p(6)=C,
$$
with $1<m<2<\gamma<r<6$ and $p'(m)=p'(r)=0$.

Set $S=m+r$ and $P=mr$. Since the two negative active points are double roots of $p+C$, write
$$
p(\lambda)=\frac{(\lambda^2-S\lambda+P)^2}{PS}-\frac{P-S}{S}.
$$
Then automatically
$$
p(0)=1,\qquad p'(0)=-2,
$$
and
$$
C=\frac{P-S}{S}>0.
$$
The conditions $p(\gamma)=p(6)=C$ are equivalent to
$$
P=\frac{S(\gamma+6)-\gamma^2-36}{2}
$$
and
$$
(\gamma^2+32\gamma+12)S^2
-(2\gamma^3+32\gamma^2+216\gamma+288)S
+\gamma^4+216\gamma^2+1296=0.
$$
Take the larger root $S=S_\gamma$ and then define
$$
P_\gamma=\frac{S_\gamma(\gamma+6)-\gamma^2-36}{2},
$$
$$
m_\gamma=\frac{S_\gamma-\sqrt{S_\gamma^2-4P_\gamma}}2,
\qquad
r_\gamma=\frac{S_\gamma+\sqrt{S_\gamma^2-4P_\gamma}}2.
$$
On $\frac92\le\gamma\le\frac{24}{5}$, the explicit larger-root formula gives
$$
\frac{67}{10}<S_\gamma\le\frac{34}{5},
\qquad
\frac{36}{5}\le P_\gamma<\frac{73}{10}.
$$
Hence
$$
1<m_\gamma<2<\frac{S_\gamma}{2}<\gamma<r_\gamma<6.
$$
The other two points at which $p=C$ are $S_\gamma-6$ and $S_\gamma-\gamma$. Here $S_\gamma-6<1$. The equality $S_\gamma-\gamma=2$ means $S_\gamma=\gamma+2$; substitution into the quadratic for $S_\gamma$ gives
$$
-4(\gamma-2)(5\gamma-24)=0.
$$
Thus, throughout $\frac92<\gamma<\frac{24}{5}$,
$$
S_\gamma-\gamma>2.
$$
Therefore neither extra positive-level crossing lies in $[1,2]$. Since the vertex $S_\gamma/2$ lies in the gap and the right component runs between equal positive levels with the stationary minimum $r_\gamma$, we have $|p|\le C$ on $E_\gamma$. The constrained alternation certificate gives
$$
\mathcal A_\gamma=\{m_\gamma,\gamma,r_\gamma,6\}.
$$
The first transition is therefore
$$
\gamma_1=\frac{24}{5}.
$$

At $\gamma=\frac92$, the larger root and associated product are
$$
S_{9/2}=\frac{2787+12\sqrt{1021}}{470},
\qquad
P_{9/2}=\frac{1413+63\sqrt{1021}}{470}.
$$
Therefore
$$
\mathcal C_{9/2}^*
=\frac{P_{9/2}-S_{9/2}}{S_{9/2}}
=\frac{25\sqrt{1021}-702}{1201}.
$$

Step 3: Identify the fixed middle minimizer and the second transition
At $\gamma=\frac{24}{5}$ the first-regime polynomial becomes
$$
p_0(\lambda)=
\frac{25\lambda^4-340\lambda^3+1516\lambda^2-2448\lambda+1224}{1224},
$$
with
$$
C_0=\frac1{17}.
$$
Two useful factorizations are
$$
p_0(\lambda)-C_0
=\frac{(\lambda-6)(\lambda-2)(5\lambda-24)(5\lambda-4)}{1224},
$$
$$
p_0(\lambda)+C_0
=\frac{(5\lambda^2-34\lambda+36)^2}{1224}.
$$
Thus, with
$$
m_0=\frac{17-\sqrt{109}}5,
\qquad
r_0=\frac{17+\sqrt{109}}5,
$$
we have
$$
p_0(m_0)=p_0(r_0)=-C_0,
\qquad
p_0(2)=p_0(6)=C_0.
$$
Also
$$
p_0'(\lambda)=\frac{(5\lambda-17)(5\lambda^2-34\lambda+36)}{306},
$$
so the third stationary point is $17/5$, which lies in the spectral gap.

At the first transition the moving endpoint $\gamma_1=24/5$ is also active, so
$$
\mathcal A_{\gamma_1}=\{m_0,2,\gamma_1,r_0,6\}.
$$
For
$$
\frac{24}{5}<\gamma<r_0,
$$
the point $24/5$ has left the right spectral interval while $r_0$ remains in it. Hence the same fixed quartic remains feasible and has the four alternating active points
$$
\mathcal A_\gamma=\{m_0,2,r_0,6\}.
$$
The second transition occurs exactly when the moving endpoint reaches $r_0$:
$$
\gamma_2=r_0=\frac{17+\sqrt{109}}5.
$$
At this transition
$$
\mathcal A_{\gamma_2}=\{m_0,2,\gamma_2,6\},
\qquad p_0'(\gamma_2)=0.
$$

Step 4: Construct the final constrained branch and extract its endpoint algebraic invariant
Let
$$
\gamma_2<\gamma\le\frac{11}{2}.
$$
The new alternating pattern is
$$
p(m)=-C,\qquad p(2)=C,\qquad p(\gamma)=-C,\qquad p(6)=C,
$$
with $1<m<2$.

Define
$$
\begin{aligned}
G(\gamma,m)={}&\gamma^2m^4-16\gamma^2m^3+40\gamma^2m^2+88\gamma^2m-144\gamma^2\\
&-8\gamma m^4+96\gamma m^3-144\gamma m^2-896\gamma m+1152\gamma\\
&-4m^4+88m^3-736m^2+2304m-1728.
\end{aligned}
$$
For every $\gamma\in(\gamma_2,11/2]$ there is a unique root
$$
m_\gamma\in(m_0,4/3)
$$
of $G(\gamma,m)=0$. Indeed,
$$
G(\gamma,m_0)
=\frac{16(376\sqrt{109}-3647)}{625}(\gamma-\gamma_2)^2>0,
$$
whereas
$$
G\left(\gamma,\frac43\right)
=\frac{16(49\gamma^2-488\gamma+1172)}{81}<0
$$
on this interval. Moreover, on the rectangle
$$
\gamma_2\le\gamma\le\frac{11}{2},
\qquad
m_0\le m\le\frac43,
$$
direct differentiation gives $G_{mm}>0$ and $G_{m\gamma}>0$, hence
$$
G_m(\gamma,m)
\le G_m\left(\frac{11}{2},\frac43\right)
=-\frac{7406}{27}<0.
$$
So the root is unique.

Put $m=m_\gamma$ and
$$
D=2\gamma m-8\gamma+m^2-16m+52,
$$
$$
\rho=\frac{-\gamma m^2+16\gamma m-52\gamma+8m^2-104m+320}{D}.
$$
On the rectangle above, $D\ge28/9>0$. The choice of $\rho$ is exactly the solution of
$$
R(2)=R(6),
\qquad
R(\lambda)=(\lambda-m)^2(\lambda-\gamma)(\lambda-\rho).
$$
After this substitution, the second condition
$$
R(2)-2R(0)=R'(0)
$$
is precisely $G(\gamma,m)=0$.

We also have
$$
\rho-2=-\frac{(\gamma-6)(m-6)^2}{D}>0.
$$
In fact $\rho>5$. To prove $\rho<\gamma$, set
$$
t_\gamma=4-\frac4{\gamma-4}.
$$
Then
$$
G(\gamma,t_\gamma)
=\frac{16(\gamma-6)(\gamma-2)(\gamma^2-4\gamma-4)(5\gamma^2-34\gamma+36)}{(\gamma-4)^4}<0.
$$
Since $G(\gamma,m_0)>0$ and $G$ is strictly decreasing in $m$, we get $m_\gamma<t_\gamma$. Using
$$
\rho-\gamma
=-\frac{2(\gamma+m-8)(\gamma m-4\gamma-4m+20)}{D}
$$
then gives
$$
1<m<2<5<\rho<\gamma<6.
$$

Now let
$$
k=-\frac2{R'(0)}>0,
\qquad
C=kR(0)-1,
\qquad
p(\lambda)=kR(\lambda)-C.
$$
Then $p(0)=1$ and $p'(0)=-2$, while
$$
p(m)=-C,\quad p(2)=C,\quad p(\gamma)=-C,\quad p(6)=C.
$$
The remaining stationary points lie in the spectral gap, and on the left component the only stationary point is $m$; consequently $|p|\le C$ on $E_\gamma$. The four-point constrained alternation certificate proves
$$
\mathcal A_\gamma=\{m_\gamma,2,\gamma,6\}
\qquad\left(\gamma_2<\gamma\le\frac{11}{2}\right).
$$
Thus there are no further transitions in the prescribed interval.

Now let $m_*=m_{11/2}$, the unique active point in $(1,2)$ at the right endpoint. Substituting $\gamma=11/2$ into $G$ gives
$$
G\left(\frac{11}{2},m\right)
=-\frac14\left(71m^4-528m^3+1272m^2-152m-1008\right).
$$
Hence $m_*$ is the unique root in $(m_0,4/3)$ of
$$
Q(t)=71t^4-528t^3+1272t^2-152t-1008.
$$
This primitive quartic is irreducible over $\mathbb Q$: modulo $11$, multiplying by the inverse of its leading coefficient gives
$$
f(t)=t^4-3t^2-4t+3,
$$
and a Euclidean calculation gives
$$
\gcd\bigl(f(t),t^{121}-t\bigr)=1.
$$
Any reducible quartic over $\mathbb F_{11}$ has a factor of degree $1$ or $2$, hence would have a nontrivial gcd with $t^{121}-t$. Therefore $Q$ is irreducible and is exactly the primitive minimal polynomial of $m_*$.

The requested data are
$$
\gamma_1=\frac{24}{5},\qquad
\gamma_2=\frac{17+\sqrt{109}}5,\qquad
\mathcal C_{9/2}^*=\frac{25\sqrt{1021}-702}{1201},
$$
with minimal-polynomial coefficient tuple
$$
(q_4,q_3,q_2,q_1,q_0)=(71,-528,1272,-152,-1008).
$$

Final Answer: $\boxed{(24/5,(17+\sqrt{109})/5,(25\sqrt{1021}-702)/1201;71,-528,1272,-152,-1008)}$

---

## Answer

$(24/5,(17+\sqrt{109})/5,(25\sqrt{1021}-702)/1201;71,-528,1272,-152,-1008)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- constrained Richardson tuning
- coefficient-constrained minimax approximation
- active-set phase transitions
- algebraic endpoint invariant