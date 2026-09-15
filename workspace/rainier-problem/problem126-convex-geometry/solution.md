## Steps

Step 1: Reduce the John ellipsoid to an $S_3$-invariant shape matrix
For $1\leq h\leq2$, write $H=h^2$ and let $B_4=\{v\in\mathbb{R}^4:\|v\|_2\leq1\}$. Because $K_h$ is centrally symmetric, any ellipsoid $c+TB_4\subset K_h$ yields the centered ellipsoid
$$
\frac12\bigl((c+TB_4)+(-c+TB_4)\bigr)=TB_4\subset K_h
$$
with the same volume. Thus the maximal-volume ellipsoid may be taken as
$$
E_A=\{A^{1/2}v:v\in B_4\},\qquad A=A^T>0.
$$
For a slab $|w^Tx|\leq b$, containment is equivalent to $w^TAw\leq b^2$. Also
$$
\left(\frac{\operatorname{vol}(E_A)}{\operatorname{vol}(B_4)}\right)^2=\det A.
$$
The feasible set of positive definite shape matrices is convex, and $\log\det$ is strictly concave. Hence the centered maximizer is unique. Averaging it over permutations of the first three coordinates preserves feasibility and cannot decrease $\det A$, so uniqueness forces $S_3$-invariance.

Let
$$
u=\frac1{\sqrt3}(1,1,1,0)^T
$$
and let $W=\{(w_1,w_2,w_3,0):w_1+w_2+w_3=0\}$. On $W$, $A$ acts by a scalar $r>0$. On $\operatorname{span}\{u,e_4\}$ write its matrix as
$$
\begin{pmatrix}q&\sqrt3c\\ \sqrt3c&d\end{pmatrix}.
$$
Then
$$
\det A=r^2(qd-3c^2).
$$
The first three coordinate constraints give
$$
\frac{2r+q}{3}\leq1,
$$
while $|x_4|\leq1$ gives $d\leq1$. The two oblique slabs give
$$
3q+6c+d\leq H,
$$
$$
\frac q3-2c+d\leq H.
$$
For fixed $q,c,d$, the determinant increases with $r$, so every maximizer has
$$
r=\frac{3-q}{2}.
$$
Thus the first three coordinate facet pairs are tangent for every $h$.

Step 2: Solve the inner active-set problem for fixed $q$
Put $\delta=H-1$. For fixed $q>0$, maximize
$$
G=qd-3c^2
$$
subject to
$$
d\leq1,\qquad d\leq H-3q-6c,\qquad d\leq H-\frac q3+2c.
$$
Since $q>0$, the optimal $d$ is the smallest of these three upper bounds.

First suppose $q\geq\delta$. The two slab bounds meet at
$$
c=-\frac q3,
$$
where their common value is $H-q\leq1$. For $c\geq-q/3$, the first slab is the smaller one and
$$
G=q(H-3q-6c)-3c^2,
$$
whose derivative in $c$ is $-6(q+c)<0$. For $c\leq-q/3$, the second slab is smaller and
$$
G=q\left(H-\frac q3+2c\right)-3c^2,
$$
whose derivative is $2q-6c>0$. Hence the optimum is exactly at the intersection:
$$
G=qH-\frac43q^2=\frac{q(3H-4q)}3.
$$

Now suppose $0<q\leq\delta$. The choice $d=1$ is feasible precisely when
$$
L:=\frac{1-H+q/3}{2}\leq c\leq U:=\frac{H-3q-1}{6}.
$$
If $q\leq\delta/3$, then $0\in[L,U]$, so $c=0$ gives the largest possible value $G=q$. If $\delta/3\leq q\leq\delta$, then $U\leq0$ and the point in $[L,U]$ closest to $0$ is $c=U$. Leaving the interval forces one slab bound below $1$; on the right the corresponding objective is decreasing, and on the left it is increasing, so no exterior point improves the value. Therefore
$$
G=q-3U^2=q-\frac{(\delta-3q)^2}{12}.
$$
Consequently the maximal determinant for a given $q$ is
$$
\Phi_H(q)=\frac{(3-q)^2}{4}\times
\begin{cases}
q,&0<q\leq\delta/3,\\
q-\dfrac{(\delta-3q)^2}{12},&\delta/3\leq q\leq\delta,\\
\dfrac{q(3H-4q)}3,&q\geq\delta.
\end{cases}
$$
with the obvious omission of empty ranges.

Step 3: Locate the two parameter values where the maximizing active set changes
On $0<q\leq\delta/3$, differentiation gives
$$
\Phi_H'(q)=\frac{3(q-3)(q-1)}4>0,
$$
because $q\leq\delta/3\leq1$.

On $\delta/3\leq q\leq\delta$,
$$
\Phi_H'(q)=-\frac{(q-3)(3q-\delta-6)(6q-\delta-3)}{24}.
$$
Here $q<3$ and $3q-\delta-6<0$, so this piece increases until
$$
q=\frac{\delta+3}{6}
$$
and decreases afterward. This critical point lies inside the interval exactly when
$$
\delta\geq\frac35.
$$
Thus for $\delta<3/5$ the middle piece is maximized at its right endpoint $q=\delta$, while for $\delta>3/5$ it is maximized at $q=(\delta+3)/6$.

On $q\geq\delta$,
$$
\Phi_H'(q)=-\frac{(q-3)\bigl(16q^2-(9H+24)q+9H\bigr)}{12}.
$$
The smaller root of the quadratic factor is
$$
q_-(H)=\frac{9H+24-3\sqrt{9H^2-16H+64}}{32}.
$$
This root lies in the region $q\geq\delta$ exactly until it meets the boundary $q=\delta$. Substituting $H=\delta+1$ and $q=\delta$ into the quadratic gives
$$
7\delta^2-24\delta+9=0,
$$
whose roots are $3/7$ and $3$. Inside $1<h<2$, the relevant transition is
$$
\delta=\frac37,
$$
that is
$$
H=\frac{10}{7}.
$$
Combining the three pieces, the unique maximizing $q$ is therefore
$$
q=q_-(H)\quad\text{for }1<H<\frac{10}{7},
$$
$$
q=H-1\quad\text{for }\frac{10}{7}<H<\frac85,
$$
$$
q=\frac{H+2}{6}\quad\text{for }\frac85<H<4.
$$
Hence the only possible contact-pattern transitions in $1<h<2$ occur at $H=10/7$ and $H=8/5$.

Step 4: Identify the facet families tangent in each regime
Let $C_{123}$ denote the three coordinate facet pairs $|x_i|=1$ for $1\leq i\leq3$, let $C_4$ denote $|x_4|=1$, and let $S_+$ and $S_-$ denote the two oblique slab facet pairs in the order they appear in the problem.

For $1<H<10/7$, the optimizer has
$$
c=-\frac q3,\qquad d=H-q<1.
$$
Both slab inequalities are equalities, while the fourth coordinate inequality is strict. Thus
$$
\mathcal T(h)=\{C_{123},S_+,S_-\}.
$$

For $10/7<H<8/5$, the optimizer has
$$
q=H-1,\qquad c=-\frac q3,\qquad d=1.
$$
Now both slabs and the fourth coordinate facets are tangent:
$$
\mathcal T(h)=\{C_{123},C_4,S_+,S_-\}.
$$

For $8/5<H<4$, the optimizer has
$$
q=\frac{H+2}{6},\qquad c=\frac{H-4}{12},\qquad d=1.
$$
The first oblique slab is tangent because $3q+6c+d=H$, whereas the second has
$$
\frac q3-2c+d=\frac{16-H}{9}<H
$$
for $H>8/5$. Hence
$$
\mathcal T(h)=\{C_{123},C_4,S_+\}.
$$
The collection of tangent facet families therefore fails to be locally constant exactly when $h^2=10/7$ or $h^2=8/5$.

Final Answer: $\boxed{\left\{\sqrt{\frac{10}{7}},\sqrt{\frac{8}{5}}\right\}}$

---

## Answer

$\left\{\sqrt{\frac{10}{7}},\sqrt{\frac{8}{5}}\right\}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- maximal-volume ellipsoids
- symmetry averaging
- support functions
- active-set transitions
- determinant optimization
