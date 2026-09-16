## Steps

Step 1: Reduce the budget constraint to a constrained alternation problem
For four Richardson steps write
$$
p(\lambda)=\prod_{j=1}^4(1-\alpha_j\lambda).
$$
The condition $\sum_j\alpha_j=2$ is exactly
$$
p(0)=1,\qquad p'(0)=-2.
$$
Thus the admissible quartics form a three-dimensional affine space. If a feasible quartic has four increasing active points with alternating values $\pm C$, then any strictly better feasible quartic would differ from it by a quartic having three positive sign-change zeros and also a double zero at $0$. That is impossible. Hence four-point alternation is an exact optimality certificate; the weak-sign argument gives uniqueness.

All three regimes below have two negative interior contacts $m<r$. Put
$$
S=m+r,\qquad P=mr,\qquad q(\lambda)=\lambda^2-S\lambda+P.
$$
Since $p(m)=p(r)=-C$ and $p'(m)=p'(r)=0$,
$$
p(\lambda)+C=kq(\lambda)^2.
$$
Using $p(0)=1$ and $p'(0)=-2$ gives
$$
k=\frac1{PS},\qquad C=\frac{P-S}{S},
$$
so
$$
p(\lambda)=\frac{q(\lambda)^2}{PS}-\frac{P-S}{S}.
$$
The positive level $p=C$ is characterized by
$$
q(\lambda)^2=2P(P-S).
$$
Consequently, if two positive contacts $a,b$ satisfy $q(a)=-q(b)$, then the other two positive-level crossings are $S-a$ and $S-b$.

Step 2: First regime and the cubic transition
Write
$$
u=8-\gamma.
$$
Initially the active pattern is
$$
p(m)=-C,\qquad p(\gamma)=C,\qquad p(r)=-C,\qquad p(u)=C.
$$
Because $q(\gamma)=-q(u)$ and $\gamma+u=8$,
$$
P=4S-\gamma^2+8\gamma-32.
$$
Substituting $p(\gamma)=C$ gives the quadratic equation
$$
F_1(S,\gamma)=0,
$$
where
$$
\begin{aligned}
F_1(S,\gamma)={}&(\gamma^2-8\gamma-8)S^2
+(-2\gamma^2+16\gamma+192)S\\
&-2(\gamma^4-16\gamma^3+96\gamma^2-256\gamma+512).
\end{aligned}
$$
For $3\le\gamma\le7/2$, the relevant solution is the larger $S$-root: it lies in $(4,6)$ and is the only one for which $P>S>0$. Hence the third stationary point $S/2$ lies in the spectral gap $(2,\gamma)$.

The four positive-level crossings are
$$
\gamma,\quad u,\quad S-\gamma,\quad S-u.
$$
At $\gamma=3$ one has $S-\gamma>2$ and $S-u<1$. The first possible collision with the spectrum is therefore $S-\gamma=2$. Substituting $S=\gamma+2$ into $F_1=0$ yields
$$
-(\gamma-2)(\gamma^3-24\gamma^2+168\gamma-336)=0.
$$
Let $\gamma_1$ be the unique root in $(3,7/2)$ of
$$
f(x)=x^3-24x^2+168x-336.
$$
Indeed, $f(3)<0<f(7/2)$ and
$$
f'(x)=3x^2-48x+168>0
$$
on that interval. The competing collision $S-u=1$ would require
$$
\gamma^4-8\gamma^3+9\gamma^2+40\gamma-56=0,
$$
whose left side stays positive on $[3,7/2]$; hence it occurs later.

Therefore, for
$$
3<\gamma<\gamma_1,
$$
the extra positive-level crossings stay outside $E_\gamma$, so
$$
\mathcal A_\gamma=\{m_\gamma,\gamma,r_\gamma,8-\gamma\}.
$$
At $\gamma=\gamma_1$ we have $S=\gamma_1+2$. If $m_1<r_1$ are the roots of
$$
t^2-(\gamma_1+2)t+P_1=0,
\qquad
P_1=4(\gamma_1+2)-\gamma_1^2+8\gamma_1-32,
$$
then
$$
\mathcal A_{\gamma_1}
=\{m_1,2,\gamma_1,r_1,8-\gamma_1\}.
$$

Step 3: Second regime and the quadratic transition
After $2$ becomes active, the positive contacts are $2$ and $u=8-\gamma$, while $m,r$ remain the negative contacts. The condition $q(2)=-q(u)$ gives
$$
P=\frac{(10-\gamma)S-\gamma^2+16\gamma-68}{2}.
$$
Substitution into $p(2)=C$ gives
$$
F_2(S,\gamma)=0,
$$
where
$$
\begin{aligned}
F_2(S,\gamma)={}&(\gamma^2-24\gamma+124)S^2\\
&+(2\gamma^3-56\gamma^2+536\gamma-1728)S\\
&+\gamma^4-32\gamma^3+408\gamma^2-2432\gamma+5648.
\end{aligned}
$$
Again the relevant $S$ is the larger root in $(4,6)$, so $S/2$ remains in the gap. The four positive-level crossings are now
$$
2,\quad u,\quad S-2,\quad S-u.
$$
At $\gamma_1$ we have $S-2=\gamma_1$. For $\gamma>\gamma_1$ this crossing moves into the gap; equality $S-2=\gamma$ can occur again only at another root of the same cubic $f$, and there is none before $19/5$.

The next collision is $S-u=1$. Since $u=8-\gamma$, this means $S=9-\gamma$. Substitution into $F_2=0$ gives
$$
5\gamma^2-56\gamma+140=0.
$$
Thus
$$
\gamma_2=\frac{28-2\sqrt{21}}5.
$$
For
$$
\gamma_1<\gamma<\gamma_2,
$$
we therefore have
$$
\mathcal A_\gamma=\{m_\gamma,2,r_\gamma,8-\gamma\}.
$$

Step 4: Final fixed branch and exclusion of a third transition
Once the crossing $S-u$ reaches $1$, the positive contacts become $1$ and $2$. The relation $q(1)=-q(2)$ gives
$$
P=\frac{3S-5}{2},
$$
and $p(1)=C$ reduces to
$$
5S^2-34S+41=0.
$$
The relevant root is
$$
S_0=\frac{17+2\sqrt{21}}5,
\qquad
P_0=\frac{13+3\sqrt{21}}5.
$$
Let $m_0<r_0$ be the roots of
$$
t^2-S_0t+P_0=0.
$$
Then
$$
1<m_0<2<\frac{S_0}{2}<\gamma_2<r_0<8-\gamma_2,
$$
and the two additional positive-level crossings are
$$
S_0-2,\qquad S_0-1.
$$
Since
$$
8-\gamma_2=S_0-1,
$$
at the second transition
$$
\mathcal A_{\gamma_2}=\{1,m_0,2,r_0,8-\gamma_2\}.
$$
For $\gamma>\gamma_2$, both moving endpoints lie strictly between the two positive-level crossings. Moreover
$$
r_0\approx3.83987>\frac{19}{5},
$$
so throughout
$$
\gamma_2<\gamma\le\frac{19}{5}
$$
the right spectral interval still contains $r_0$. Hence the same fixed quartic remains feasible and optimal, with
$$
\mathcal A_\gamma=\{1,m_0,2,r_0\}.
$$
Thus there is no third transition in the prescribed range.

The first transition is the unique root in $(3,7/2)$ of the irreducible cubic $x^3-24x^2+168x-336$, while the second is $(28-2\sqrt{21})/5$.

Final Answer: $\boxed{\left(\operatorname{root}_{(3,7/2)}(x^3-24x^2+168x-336),\frac{28-2\sqrt{21}}5\right)}$

---

## Answer

$\left(\operatorname{root}_{(3,7/2)}(x^3-24x^2+168x-336),\frac{28-2\sqrt{21}}5\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- constrained Richardson tuning
- constrained equioscillation
- moving spectral interval
- active-set phase transitions