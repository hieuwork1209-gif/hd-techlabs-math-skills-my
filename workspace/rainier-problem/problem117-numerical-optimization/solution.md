## Steps

Step 1: Reduce the two step constraints to a two-parameter minimax family
For four Richardson steps write
$$
p(\lambda)=\prod_{j=1}^4(1-\alpha_j\lambda).
$$
The two symmetric constraints
$$
\sum_{j=1}^4\alpha_j=2,
\qquad
\sum_{1\le i<j<k\le4}\alpha_i\alpha_j\alpha_k=\frac14
$$
are exactly the coefficient conditions
$$
p(\lambda)=1-2\lambda+A\lambda^2-\frac14\lambda^3+B\lambda^4. \tag{1}
$$
Thus only $A$ and $B$ are free. If $p$ and $q$ both satisfy (1), then
$$
q(\lambda)-p(\lambda)=\lambda^2(u+v\lambda^2),
$$
which has at most one positive zero unless $p=q$. Hence three increasing contacts with alternating values $-C,+C,-C$ are an exact optimality certificate: a strictly better feasible quartic would make $q-p$ alternate signs at those three contacts and therefore have at least two positive zeros, impossible. The weak-sign version gives uniqueness.

Every candidate below has four positive zeros. Therefore it factors as $\prod_{j=1}^4(1-\alpha_j\lambda)$ with all $\alpha_j>0$, and (1) then gives exactly the two required step constraints.

Step 2: Find the fixed first regime and the first transition
For the initial regime the three alternating contacts are stationary points
$$
m<s<r,
\qquad
p(m)=-C,\quad p(s)=C,\quad p(r)=-C.
$$
Since the two negative contacts are stationary,
$$
p(\lambda)+C=c(\lambda-m)^2(\lambda-r)^2
=c(\lambda^2-S\lambda+P)^2,
$$
where $S=m+r$ and $P=mr$. Comparing the $\lambda^3$ and $\lambda$ coefficients with (1) gives
$$
cS=\frac18,
\qquad
cSP=1,
$$
so
$$
P=8,
\qquad
c=\frac1{8S}.
$$
The constant term then gives
$$
C=\frac{8-S}{S}.
$$
The third stationary point is the midpoint
$$
s=\frac S2.
$$
At $s$ we have
$$
p(s)+C
=\frac{(S^2-32)^2}{128S}.
$$
Imposing $p(s)=C$ yields
$$
(S^2-32)^2=256(8-S).
$$
Writing $S=2\gamma_1$ gives
$$
\gamma_1^4-16\gamma_1^2+32\gamma_1-64=0. \tag{2}
$$
Let $\gamma_1$ be the unique root of (2) in $(3,7/2)$. Indeed the left side is negative at $3$, positive at $7/2$, and its derivative is positive throughout that interval.

Put
$$
S_0=2\gamma_1,
\qquad
m_0,r_0=\frac{S_0\mp\sqrt{S_0^2-32}}2.
$$
Then
$$
1<m_0<2<\gamma_1<r_0<6.
$$
Moreover $p+C=(\lambda^2-S_0\lambda+8)^2/(8S_0)$, and the only critical values on $[1,6]$ are $-C,+C,-C$ at $m_0,\gamma_1,r_0$; the endpoint values are strictly smaller in magnitude. Therefore
$$
\mathcal A_\gamma=\{m_0,\gamma_1,r_0\},
\qquad 3<\gamma<\gamma_1.
$$
At $\gamma=\gamma_1$, the positive stationary contact becomes the left endpoint of the right spectral interval, so the active set is still
$$
\mathcal A_{\gamma_1}=\{m_0,\gamma_1,r_0\},
$$
with $p'(\gamma_1)=0$.

Step 3: Track the moving square branch and find the second transition
For $\gamma>\gamma_1$, the alternating pattern is
$$
p(m)=-C,
\qquad
p(\gamma)=C,
\qquad
p(r)=-C,
$$
with $m,r$ stationary. The same coefficient comparison gives the one-parameter family
$$
p_S(\lambda)=\frac{(\lambda^2-S\lambda+8)^2}{8S}-\frac{8-S}{S}. \tag{3}
$$
The moving endpoint is active exactly when
$$
(\gamma^2-S\gamma+8)^2=16(8-S). \tag{4}
$$
On the branch continuing from Step 2 we have
$$
\gamma^2-S\gamma+8=-4\sqrt{8-S},
$$
which determines a unique $S=S_\gamma$ increasing from $S_0$.
The negative contacts are
$$
m_\gamma,r_\gamma
=\frac{S_\gamma\mp\sqrt{S_\gamma^2-32}}2.
$$
The remaining stationary point $S_\gamma/2$ lies in the gap $(2,\gamma)$, and neither $1$ nor $2$ reaches the positive level on the range considered. Hence
$$
\mathcal A_\gamma=\{m_\gamma,\gamma,r_\gamma\}
$$
until the right stationary minimum reaches the endpoint $6$.

Since $m_\gamma r_\gamma=8$, the collision $r_\gamma=6$ is equivalent to
$$
S_\gamma=\frac{22}{3}.
$$
Substituting this in (4), with the negative square-root branch, gives
$$
3\gamma^2-22\gamma+24+4\sqrt6=0.
$$
Thus
$$
\gamma_2=\frac{11+\sqrt{49-12\sqrt6}}3. \tag{5}
$$
At this value $m_{\gamma_2}=4/3$ and
$$
\mathcal A_{\gamma_2}=\left\{\frac43,\gamma_2,6\right\},
\qquad p'(6)=0.
$$

Step 4: Construct the final nonsquare branch and exclude another transition
Let
$$
\gamma_2<\gamma\le\frac{21}{4}.
$$
Now the negative contacts are an interior point $m\in(1,2)$ and the endpoint $6$, while the moving endpoint remains the positive contact. Write
$$
p(\lambda)+C=c(\lambda-m)^2(\lambda-6)(\lambda-\rho).
$$
Comparing the $\lambda^3$ and $\lambda$ coefficients with (1) gives, with
$$
D=m^2+12m-8,
$$
$$
c(m)=\frac{D}{8m(m+6)^2},
\qquad
\rho(m)=-\frac{2(3m^2-8m-24)}{D}. \tag{6}
$$
The constant term gives
$$
C(m)=6c(m)\rho(m)m^2-1
=-\frac{9m^3-22m^2-48m+72}{2(m+6)^2}. \tag{7}
$$
Finally $p(\gamma)=C$ is equivalent, after clearing the positive denominator, to
$$
F(\gamma,m)=0, \tag{8}
$$
where
$$
\begin{aligned}
F(\gamma,m)={}&(m^2+12m-8)\gamma^4
-2m(m+6)^2\gamma^3\\
&+(m^4+12m^3+132m^2+96m+288)\gamma^2\\
&-16m(m+6)^2\gamma
+4m(9m^3-20m^2-24m+144).
\end{aligned}
$$
For every $\gamma\in(\gamma_2,21/4]$ there is exactly one solution
$$
\frac{33}{25}<m_\gamma<\frac43.
$$
Here is a direct uniqueness check. On the rectangle
$$
\frac{257}{50}\le\gamma\le\frac{21}{4},
\qquad
\frac{33}{25}\le m\le\frac43,
$$
termwise bounding the expanded derivative gives
$$
F_m\le-\frac{67157971213}{1875000000}<0.
$$
Also $F(\gamma,33/25)$ is decreasing in $\gamma$ on this interval and
$$
F\left(\frac{21}{4},\frac{33}{25}\right)
=\frac{184934637}{100000000}>0,
$$
whereas
$$
F\left(\gamma,\frac43\right)
=\frac{88}{9}
\left(\gamma^2-\frac{22}{3}\gamma+8-\frac{4\sqrt6}{3}\right)
\left(\gamma^2-\frac{22}{3}\gamma+8+\frac{4\sqrt6}{3}\right)<0
$$
for $\gamma_2<\gamma\le21/4$. Thus (8) has one and only one root in the stated $m$-interval.

For this root, $D>0$, $c>0$, $C>0$, and
$$
\rho-6=-\frac{4(m+6)(3m-4)}D>0.
$$
Set
$$
p_\gamma(\lambda)
=c(m_\gamma)(\lambda-m_\gamma)^2(\lambda-6)
(\lambda-\rho(m_\gamma))-C(m_\gamma).
$$
Then
$$
p_\gamma(m_\gamma)=-C,
\qquad
p_\gamma(\gamma)=C,
\qquad
p_\gamma(6)=-C.
$$
The other stationary point below $6$ lies in the spectral gap. Indeed, for
$$
R(\lambda)=(\lambda-m)^2(\lambda-6)(\lambda-\rho),
$$
we have
$$
\frac{R'(\gamma)}{R(\gamma)}
=\frac2{\gamma-m}+\frac1{\gamma-6}+\frac1{\gamma-\rho}<0,
$$
because already
$$
\frac2{\gamma-m}+\frac1{\gamma-6}
\le\frac{300}{571}-\frac{50}{43}<0.
$$
Also $R'(2)>0$, so that stationary point lies in $(2,\gamma)$. Thus the right component decreases from $C$ to $-C$.

On the left component the only stationary point is $m$. Directly from (6)-(7),
$$
p(2)-C
=\frac{5m^4-10m^3-16m^2-72m+128}{m(m+6)^2}<0,
$$
and
$$
p(1)-C
=\frac{37m^4-86m^3-179m^2+36m+280}{8m(m+6)^2}<0
$$
for $33/25\le m\le4/3$; both numerators are already negative at $33/25$ and decrease on this interval. Hence $|p_\gamma|\le C$ on all of $E_\gamma$.

The three-point certificate from Step 1 now proves
$$
\mathcal A_\gamma=\{m_\gamma,\gamma,6\},
\qquad
\gamma_2<\gamma\le\frac{21}{4}.
$$
The strict endpoint inequalities above exclude any further transition before $21/4$.

Therefore the two interior transition values are exactly (2) and (5).

Final Answer: $\boxed{\left(\operatorname{root}_{(3,7/2)}(x^4-16x^2+32x-64),\frac{11+\sqrt{49-12\sqrt6}}3\right)}$

---

## Answer

$\left(\operatorname{root}_{(3,7/2)}(x^4-16x^2+32x-64),\frac{11+\sqrt{49-12\sqrt6}}3\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- constrained Richardson tuning
- elementary-symmetric step constraints
- three-point constrained alternation
- active-set phase transitions