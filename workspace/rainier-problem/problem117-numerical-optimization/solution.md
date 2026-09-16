## Steps

Step 1: Reduce the step budget to a constrained alternation problem
For four Richardson steps write
$$
p(\lambda)=\prod_{j=1}^4(1-\alpha_j\lambda).
$$
The budget constraint is exactly
$$
p(0)=1,\qquad p'(0)=-2.
$$
Hence the admissible quartics form a three-dimensional affine family. If a feasible quartic has four increasing active points with alternating values $\pm C$, then any strictly better feasible quartic would differ from it by a quartic with three positive sign-change zeros and also a double zero at $0$. That is impossible, so four-point alternation is an exact optimality certificate; the weak-sign version also gives uniqueness.

In the branches below the two negative contacts are interior stationary points $m<r$. Put
$$
S=m+r,\qquad P=mr,\qquad q(\lambda)=\lambda^2-S\lambda+P.
$$
Since $p(m)=p(r)=-C$ and $p'(m)=p'(r)=0$, we have
$$
p(\lambda)+C=kq(\lambda)^2.
$$
The conditions at $0$ give
$$
k=\frac1{PS},\qquad C=\frac{P-S}{S},
$$
so
$$
p(\lambda)=\frac{q(\lambda)^2}{PS}-\frac{P-S}{S}.
$$
Thus $p=C$ is equivalent to
$$
q(\lambda)^2=2P(P-S).
$$
Also $q(S-\lambda)=q(\lambda)$, so every positive-level crossing has a reflected crossing about $S/2$. The alternating signs used below force four positive zeros of $p$, hence four positive Richardson step sizes.

Step 2: First regime and the degree-six transition
Set
$$
u=\frac{15}{\gamma}.
$$
Initially the active pattern is
$$
p(m)=-C,\qquad p(\gamma)=C,\qquad p(r)=-C,\qquad p(u)=C.
$$
Here $q(\gamma)=-q(u)$, so
$$
P=\frac{S(\gamma+u)-\gamma^2-u^2}{2}.
$$
Since
$$
2q(\gamma)=(\gamma-u)(\gamma+u-S),
$$
the positive-level condition becomes the quadratic equation in $S$
$$
(\gamma-u)^2(\gamma+u-S)^2=8P(P-S). \tag{1}
$$
For $3\le\gamma\le17/5$, the smaller $S$-root of (1) has $P<0$, while the larger root has $P>S>0$ and gives
$$
1<m<2<\gamma<r<u.
$$
We always take this larger root.

The four positive-level crossings are
$$
\gamma,\quad u,\quad S-\gamma,\quad S-u.
$$
At $\gamma=3$, the two unused crossings satisfy $S-\gamma>2$ and $S-u<1$. The first possible collision with the spectrum is $S-\gamma=2$. Put $S=\gamma+2$ in (1), clear denominators using $u=15/\gamma$, and obtain
$$
H(\gamma)=0,
$$
where
$$
H(x)=4x^6-104x^5-345x^4+1140x^3+4050x^2+13500x-50625.
$$
Now $H(3)=6804$ and $H(7/2)=-15705/4$. Moreover, with $t=x-3\in[0,1/2]$,
$$
\frac{H'(x)}4
=6t^5-40t^4-1365t^3-7650t^2-13770t-1242<0.
$$
Hence $H$ has a unique root in $(3,7/2)$; call it $\gamma_1$.

The competing collision $S-u=1$ would give
$$
J(\gamma)=\gamma^6-2\gamma^5-25\gamma^4-4\gamma^3+195\gamma^2+390\gamma-675=0.
$$
Since $H(17/5)<0$, we have $\gamma_1<17/5$. On $[3,17/5]$, $J$ is strictly decreasing and
$$
J(17/5)=\frac{675624}{15625}>0,
$$
so this collision occurs later. Therefore
$$
\mathcal A_\gamma=\{m_\gamma,\gamma,r_\gamma,15/\gamma\},
\qquad 3<\gamma<\gamma_1.
$$
At $\gamma=\gamma_1$, the reflected positive crossing reaches $2$, so
$$
\mathcal A_{\gamma_1}
=\{m_1,2,\gamma_1,r_1,15/\gamma_1\}.
$$

Step 3: Second regime and the quadratic transition
After $2$ becomes active, the positive contacts are $2$ and $u=15/\gamma$. Thus
$$
q(2)=-q(u),
$$
which gives
$$
P=\frac{S(2+u)-4-u^2}{2}.
$$
The positive-level condition is now
$$
(2-u)^2(2+u-S)^2=8P(P-S). \tag{2}
$$
Again the relevant solution is the larger $S$-root, and the four positive-level crossings are
$$
2,\quad u,\quad S-2,\quad S-u.
$$
At $\gamma_1$, $S-2=\gamma_1$. Imposing $S-2=\gamma$ again in (2) reproduces $H(\gamma)=0$; since $H$ has no further zero before $18/5$, that crossing stays in the spectral gap.

The next collision is $S-u=1$. Substituting $S=u+1$ and $u=15/\gamma$ into (2) gives
$$
4\gamma^2-120\gamma+375=0.
$$
The root in our parameter interval is
$$
\gamma_2=\frac{5(6-\sqrt{21})}{2}.
$$
Thus
$$
\mathcal A_\gamma=\{m_\gamma,2,r_\gamma,15/\gamma\},
\qquad \gamma_1<\gamma<\gamma_2.
$$
At $\gamma=\gamma_2$, the reflected crossing has reached $1$.

Step 4: Final fixed branch and exclusion of a third transition
After the second transition, the two positive contacts on the left interval are $1$ and $2$. The relation $q(1)=-q(2)$ gives
$$
P=\frac{3S-5}{2},
$$
and the positive-level equation reduces to
$$
5S^2-34S+41=0.
$$
The feasible root is
$$
S_0=\frac{17+2\sqrt{21}}5,
\qquad
P_0=\frac{13+3\sqrt{21}}5.
$$
Let $m_0<r_0$ be the roots of $t^2-S_0t+P_0$. Numerically,
$$
m_0\approx1.39316,\qquad r_0\approx3.83987.
$$
The two other positive-level crossings are $S_0-2$ and $S_0-1$. At the transition,
$$
\frac{15}{\gamma_2}=\frac{12+2\sqrt{21}}5=S_0-1,
$$
so
$$
\mathcal A_{\gamma_2}=\{1,m_0,2,r_0,15/\gamma_2\}.
$$
For $\gamma_2<\gamma\le18/5$, the moving right interval lies strictly between the two reflected positive-level crossings, and it still contains $r_0$ because
$$
\gamma\le\frac{18}{5}<r_0<\frac{25}{6}\le\frac{15}{\gamma}.
$$
Hence the same quartic remains feasible and optimal, with
$$
\mathcal A_\gamma=\{1,m_0,2,r_0\}.
$$
There is therefore no third transition in the prescribed range.

The first transition is the unique zero of $H$ in $(3,7/2)$, and the second is $5(6-\sqrt{21})/2$.

Final Answer: $\boxed{\left(\operatorname{root}_{(3,7/2)}(4x^6-104x^5-345x^4+1140x^3+4050x^2+13500x-50625),\frac{5(6-\sqrt{21})}{2}\right)}$

---

## Answer

(root_(3,7/2)(4x^6-104x^5-345x^4+1140x^3+4050x^2+13500x-50625),5(6-sqrt(21))/2)

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- constrained Richardson tuning
- constrained equioscillation
- reciprocal moving spectral interval
- algebraic active-set transitions
