## Steps

Step 1: Use five-point alternation as an exact optimality certificate
Write a four-step Richardson polynomial as
$$
p(\lambda)=(1-\alpha\lambda)(1-\beta\lambda)(1-\delta\lambda)(1-\eta\lambda),
\qquad p(0)=1.
$$
Suppose a quartic $p$ has five increasing points $x_1<\cdots<x_5$ in $E_\gamma$ with
$$
p(x_j)=(-1)^{j-1}C
$$
and $|p|\le C$ on $E_\gamma$. If another quartic $q$ with $q(0)=1$ had smaller sup norm, then $q-p$ would change sign in each of the four intervals $(x_j,x_{j+1})$, giving four positive zeros in addition to the zero at $0$. This is impossible for a nonzero quartic. The same argument with weak inequalities gives uniqueness at norm $C$.

Thus any feasible five-point alternating quartic is the unique minimizer among quartics with constant term $1$. In every regime below the five alternating values also force four positive zeros of $p$, so $p$ factors into four Richardson factors with positive step sizes.

Step 2: Construct the first regime and locate the first transition
Set
$$
s=\frac{25}{4},\qquad
u=\left(\gamma-\frac72\right)^2,
\qquad y=\lambda-\frac72,
$$
and define
$$
q_\gamma(y)=y^4-(s+\nu)y^2+\frac{s^2+6s\nu+\nu^2}{8}.
$$
As a quadratic in $z=y^2$, this satisfies
$$
q_\gamma\big|_{z=s}=q_\gamma\big|_{z=\nu}
=\frac{(s-\nu)^2}{8},
$$
while at its minimum
$$
z=\frac{s+\nu}{2}
$$
we have
$$
q_\gamma=-\frac{(s-\nu)^2}{8}.
$$
Let
$$
d_\gamma=\sqrt{\frac{s+\nu}{2}},\qquad
m_\gamma=\frac72-d_\gamma,\qquad
r_\gamma=\frac72+d_\gamma.
$$
For $\frac92<\gamma<5$, one has
$$
1<m_\gamma<2<\gamma<r_\gamma<6.
$$
Moreover $q_\gamma(-7/2)>0$, so
$$
p_\gamma(\lambda)=
\frac{q_\gamma(\lambda-7/2)}{q_\gamma(-7/2)}
$$
has $p_\gamma(0)=1$. If
$$
C_\gamma=
\frac{(s-\nu)^2}{8q_\gamma(-7/2)},
$$
then
$$
p_\gamma(1)=C_\gamma,\quad
p_\gamma(m_\gamma)=-C_\gamma,\quad
p_\gamma(\gamma)=C_\gamma,\quad
p_\gamma(r_\gamma)=-C_\gamma,\quad
p_\gamma(6)=C_\gamma.
$$
On the right interval, $z$ ranges over $[\nu,s]$. On the left interval, $z$ ranges over $[9/4,s]$, which is contained in $[\nu,s]$ because $\nu<9/4$ exactly when $\gamma<5$. Hence $|p_\gamma|\le C_\gamma$ on $E_\gamma$, and the alternation certificate gives
$$
\mathcal A_\gamma=
\{1,m_\gamma,\gamma,r_\gamma,6\}
\qquad\left(\frac92<\gamma<5\right).
$$

At $\gamma=5$, we have $\nu=9/4$, so the previously unused endpoint $2$ also reaches the positive level. Thus the first transition is
$$
\gamma_1=5.
$$
Writing
$$
m_0=\frac{7-\sqrt{17}}2,\qquad
r_0=\frac{7+\sqrt{17}}2,
$$
the transition active set is
$$
\mathcal A_5=\{1,m_0,2,5,r_0,6\}.
$$

Step 3: Identify the fixed middle minimizer and the second transition
At $\gamma=5$, the preceding polynomial simplifies to
$$
p_0(\lambda)
=1-\frac{56}{31}\lambda
+\frac{65}{62}\lambda^2
-\frac{7}{31}\lambda^3
+\frac{1}{62}\lambda^4,
$$
with
$$
C_0=\frac1{31}.
$$
Its derivative factors as
$$
p_0'(\lambda)
=\frac1{31}(2\lambda-7)(\lambda^2-7\lambda+8),
$$
so its stationary points are
$$
m_0=\frac{7-\sqrt{17}}2,\qquad
\frac72,\qquad
r_0=\frac{7+\sqrt{17}}2.
$$
Also
$$
p_0(1)=p_0(2)=p_0(5)=p_0(6)=C_0,
\qquad
p_0(m_0)=p_0(r_0)=-C_0.
$$
For
$$
5<\gamma<r_0,
$$
the point $5$ has left the spectrum, while $r_0$ remains in the right spectral interval. Therefore $|p_0|\le C_0$ on $E_\gamma$, with the five alternating active points
$$
\mathcal A_\gamma=\{1,m_0,2,r_0,6\}.
$$
This certifies $p_0$ as the unique minimizer throughout the whole middle regime.

The second change occurs when the moving left endpoint of the right interval reaches $r_0$. Hence
$$
\gamma_2=r_0=\frac{7+\sqrt{17}}2.
$$
At this transition,
$$
\mathcal A_{\gamma_2}=\{1,m_0,2,\gamma_2,6\},
\qquad p_0'(\gamma_2)=0.
$$

Step 4: Construct the final branch and rule out any further transition before $28/5$
For $\gamma>\gamma_2$, the right interior minimum has left the spectrum. The new alternating pattern must be
$$
p(1)=C,\quad p(m)=-C,\quad p(2)=C,\quad p(\gamma)=-C,\quad p(6)=C,
$$
with $1<m<2$ and $p'(m)=0$.

Introduce
$$
R(\lambda)=(\lambda-1)(\lambda-2)(\lambda-\rho)(\lambda-6).
$$
The condition $R'(m)=0$ gives
$$
\rho=\rho(m)=
\frac{4m^3-27m^2+40m-12}{3m^2-18m+20}.
$$
Put
$$
A(m)=3m^2-18m+20.
$$
A direct subtraction gives
$$
R(\gamma)-R(m)
=\frac{(\gamma-m)^2}{A(m)}F(\gamma,m),
$$
where
$$
\begin{aligned}
F(\gamma,m)={}&3\gamma^2m^2-18\gamma^2m+20\gamma^2
+2\gamma m^3-36\gamma m^2+162\gamma m-168\gamma\\
&+m^4-18m^3+121m^2-336m+292.
\end{aligned}
$$
At $m=m_0$ this factors as
$$
F(\gamma,m_0)
=\frac{13-3\sqrt{17}}2(\gamma-\gamma_2)^2.
$$
At $m=7/5$,
$$
F\left(\gamma,\frac75\right)
=\frac{425\gamma^2-3920\gamma+8256}{625}.
$$
On $[\gamma_2,28/5]$ this last quadratic is increasing and its value at $28/5$ is $-368/625$, so it is negative throughout that interval.

There is exactly one root $m=m_\gamma$ of $F(\gamma,m)=0$ in $(7/5,m_0)$ for every $\gamma_2<\gamma\le28/5$. Indeed, on the rectangle
$$
\gamma_2\le\gamma\le\frac{28}{5},\qquad
\frac75\le m\le m_0,
$$
we have $F_m>0$. One compact verification is that
$$
\partial_\gamma F_m=6(m-3)(2\gamma+m-9)<0,
$$
while
$$
\frac12\partial_mF_m
=3\gamma^2+6\gamma m-36\gamma+6m^2-54m+121<0;
$$
the latter expression has maximum $-83/25$ on the rectangle. Hence $F_m$ decreases in both variables, and its minimum is
$$
F_m\left(\frac{28}{5},m_0\right)
=\frac{2(1431-301\sqrt{17})}{25}>0.
$$

On this branch $A(m)>0$ and $\rho(m)$ is increasing; moreover
$$
\rho\left(\frac75\right)=\frac{257}{85}>2,
\qquad
\rho(m_0)=5.
$$
Thus
$$
2<\rho(m_\gamma)<5<\gamma<6.
$$
To locate the last stationary point, note that
$$
F_\gamma(\gamma_2,m)
=2(m-m_0)
\left(m^2+(\sqrt{17}-4)m-\frac{7\sqrt{17}+9}{2}\right)\ge0
$$
for $7/5\le m\le m_0$, with equality only at $m_0$. Since $F$ is quadratic in $\gamma$ with positive leading coefficient $A(m)$, we get $F_\gamma(\gamma,m_\gamma)>0$ for $\gamma>\gamma_2$. Differentiating the identity for $R(\gamma)-R(m)$ at a root of $F$ therefore gives
$$
R'(\gamma)
=\frac{(\gamma-m)^2}{A(m)}F_\gamma(\gamma,m)>0.
$$
The roots of $R$ are ordered
$$
1<2<\rho<\gamma<6.
$$
By interlacing, $R'$ has one root in each of $(1,2)$, $(2,\rho)$, and $(\rho,6)$. The first is $m$. Since $R'(\rho)<0<R'(\gamma)$, the third root lies in $(\rho,\gamma)$, so the other two stationary points are both in the spectral gap $(2,\gamma)$.

Let
$$
S_\gamma=R(m_\gamma)=R(\gamma)<0,
$$
and define
$$
C_\gamma=\frac{1}{1-2R(0)/S_\gamma},
\qquad
k_\gamma=-\frac{2C_\gamma}{S_\gamma}>0,
\qquad
p_\gamma(\lambda)=C_\gamma+k_\gamma R(\lambda).
$$
Then $p_\gamma(0)=1$ and
$$
p_\gamma(1)=C_\gamma,\quad
p_\gamma(m_\gamma)=-C_\gamma,\quad
p_\gamma(2)=C_\gamma,\quad
p_\gamma(\gamma)=-C_\gamma,\quad
p_\gamma(6)=C_\gamma.
$$
Because the remaining stationary points lie in the gap, $|p_\gamma|\le C_\gamma$ on $E_\gamma$. The five-point alternation certificate therefore proves
$$
\mathcal A_\gamma=\{1,m_\gamma,2,\gamma,6\}
\qquad\left(\gamma_2<\gamma<\frac{28}{5}\right).
$$
So no further transition occurs in the prescribed range.

The two interior transition values are
$$
\gamma_1=5,
\qquad
\gamma_2=\frac{7+\sqrt{17}}2.
$$

Final Answer: $\boxed{\left(5,\frac{7+\sqrt{17}}2\right)}$

---

## Answer

$\left(5,\frac{7+\sqrt{17}}2\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonstationary Richardson iteration
- quartic minimax equioscillation
- active-set phase transition
- Hermite interpolation and stationary-point migration
