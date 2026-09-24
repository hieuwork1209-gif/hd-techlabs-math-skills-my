## Steps

Step 1: Turn commute times into an additive tree metric
Let the unknown tree have positive edge conductances $c_{xy}=c_{yx}$. For a vertex $x$, write
$$
c_x=\sum_{y\sim x}c_{xy},
$$
and let
$$
P(x,y)=\frac{c_{xy}}{c_x}
$$
for adjacent vertices. For an oriented edge $x-y$, remove that edge and let $A$ be the component containing $x$. If
$$
h(z)=\mathbb E_z T_y
$$
for $z\in A$, then the first-step equations are
$$
h(z)=1+\sum_{w\in A}P(z,w)h(w),
$$
where for $z=x$ the transition from $x$ to $y$ contributes zero because $h(y)=0$. Multiplying by $c_z$ and summing over $z\in A$ gives
$$
\sum_{z\in A}c_zh(z)
=
\sum_{z\in A}c_z
+
\sum_{z\in A}\sum_{w\in A}c_{zw}h(w).
$$
For every $w\neq x$, all conductance incident to $w$ stays inside $A$, while at $x$ the missing conductance is exactly $c_{xy}$. Hence
$$
\sum_{z\in A}\sum_{w\in A}c_{zw}h(w)
=
\sum_{w\in A}c_wh(w)-c_{xy}h(x).
$$
After cancellation,
$$
\mathbb E_xT_y
=
h(x)
=
\frac{\sum_{z\in A}c_z}{c_{xy}}.
$$

If $B$ is the other component, the reverse hitting time is
$$
\mathbb E_yT_x
=
\frac{\sum_{z\in B}c_z}{c_{xy}}.
$$
Therefore the commute time across one edge is
$$
C_{xy}
:=
\mathbb E_xT_y+\mathbb E_yT_x
=
\frac{\sum_z c_z}{c_{xy}}.
$$
For any two vertices $u,v$, a walk from $u$ to $v$ must cross the vertices of the unique tree path in order, so the strong Markov property makes the directed hitting time additive along that path. Consequently the commute time is also additive:
$$
C_{uv}
=
\sum_{e\in\operatorname{path}(u,v)}\ell_e,
$$
where
$$
\ell_e=\frac{\sum_zc_z}{c_e}>0.
$$

Step 2: Reconstruct the tree and its transition probabilities
The given commute times satisfy
$$
C_{13}=C_{12}+C_{23}=4+6=10.
$$
Because all edge lengths $\ell_e$ are positive, equality in the tree metric means vertex $2$ lies on the path from $1$ to $3$. Likewise,
$$
C_{24}=C_{23}+C_{34}=6+12=18,
$$
so vertex $3$ lies on the path from $2$ to $4$. With only four vertices, the tree is therefore the path
$$
1-2-3-4.
$$
Its edge commute lengths are
$$
\ell_{12}=4,
\qquad
\ell_{23}=6,
\qquad
\ell_{34}=12,
$$
so
$$
C_{14}=4+6+12=22.
$$

Since
$$
\ell_e=\frac{\sum_zc_z}{c_e},
$$
the edge conductances are proportional to the reciprocals of the commute lengths:
$$
c_{12}:c_{23}:c_{34}
=
\frac{1}{4}:\frac{1}{6}:\frac{1}{12}
=
3:2:1.
$$
Therefore the transition probabilities are forced:
$$
P(1,2)=1,
$$
$$
P(2,1)=\frac{3}{5},
\qquad
P(2,3)=\frac{2}{5},
$$
$$
P(3,2)=\frac{2}{3},
\qquad
P(3,4)=\frac{1}{3},
$$
and
$$
P(4,3)=1.
$$

Step 3: Analyze the first endpoint reached from vertex 2
Let
$$
\sigma=T_1\wedge T_4
$$
for a walk started from vertex $2$. For $i\in\{2,3\}$ define
$$
p_i=\mathbb P_i(T_1<T_4).
$$
First-step decomposition gives
$$
p_2=\frac{3}{5}+\frac{2}{5}p_3,
\qquad
p_3=\frac{2}{3}p_2.
$$
Thus
$$
p_2=\frac{9}{11},
\qquad
p_3=\frac{6}{11}.
$$

Let
$$
m_i=\mathbb E_i\sigma.
$$
Then
$$
m_2=1+\frac{2}{5}m_3,
\qquad
m_3=1+\frac{2}{3}m_2,
$$
so
$$
m_2=\frac{21}{11},
\qquad
m_3=\frac{25}{11}.
$$

For
$$
q_i=\mathbb E_i\sigma^2,
$$
conditioning on the first step gives
$$
q_2
=
1+\frac{4}{5}m_3+\frac{2}{5}q_3
=
\frac{31}{11}+\frac{2}{5}q_3
$$
and
$$
q_3
=
1+\frac{4}{3}m_2+\frac{2}{3}q_2
=
\frac{39}{11}+\frac{2}{3}q_2.
$$
Substituting the equation for $q_3$ into that for $q_2$ gives
$
q_2
=
\frac{31}{11}
+
\frac{2}{5}
\left(
\frac{39}{11}
+
\frac{2}{3}q_2
\right)
=
\frac{233}{55}
+
\frac{4}{15}q_2,
$
so
$
q_2=\frac{699}{121}.
$

The cover-time second moment also needs the correlation between $\sigma$ and which endpoint is reached first. Put
$$
a_i
=
\mathbb E_i\left[\sigma\mathbf 1_{\{T_1<T_4\}}\right].
$$
A first step from $2$ hits vertex $1$ immediately with probability $3/5$, while a first step to $3$ contributes one unit of time whenever vertex $1$ is eventually reached first. Hence
$$
a_2
=
\frac{3}{5}
+
\frac{2}{5}(p_3+a_3).
$$
Similarly,
$$
a_3
=
\frac{2}{3}(p_2+a_2).
$$
The second equation gives
$
a_3
=
\frac{6}{11}
+
\frac{2}{3}a_2.
$
Substituting this and $p_3=6/11$ into the first equation,
$
a_2
=
\frac{3}{5}
+
\frac{2}{5}
\left(
\frac{12}{11}
+
\frac{2}{3}a_2
\right)
=
\frac{57}{55}
+
\frac{4}{15}a_2,
$
so
$
a_2=\frac{171}{121}.
$
Therefore
$$
\mathbb E_2\left[\sigma\mathbf 1_{\{T_4<T_1\}}\right]
=
m_2-a_2
=
\frac{60}{121}.
$$

Step 4: Compute the traversal moments between the two endpoints
Let
$$
r_i=\mathbb E_iT_1
$$
for $i\in\{2,3,4\}$. The first-step equations are
$$
r_2=1+\frac{2}{5}r_3,
$$
$$
r_3=1+\frac{2}{3}r_2+\frac{1}{3}r_4,
$$
and
$$
r_4=1+r_3.
$$
From $r_4=1+r_3$, the middle equation becomes
$
r_3
=
1+\frac{2}{3}r_2+\frac{1}{3}(1+r_3),
$
so
$
r_3=2+r_2.
$
Then
$
r_2
=
1+\frac{2}{5}(2+r_2),
$
which gives
$
r_2=3,
\qquad
r_3=5,
\qquad
r_4=6.
$
Since $C_{14}=22$ from Step 2,
$$
\mathbb E_1T_4=22-r_4=16.
$$
Writing
$$
h_i=\mathbb E_iT_4,
$$
the relations $h_1=1+h_2$ and $h_3=1+\frac{2}{3}h_2$ therefore give
$$
h_1=16,
\qquad
h_2=15,
\qquad
h_3=11.
$$

For second moments to vertex $4$, set
$$
g_i=\mathbb E_iT_4^2.
$$
The identity
$$
g_i
=
2h_i-1+\sum_jP(i,j)g_j
$$
gives
$$
g_1=31+g_2,
$$
$$
g_2=29+\frac{3}{5}g_1+\frac{2}{5}g_3,
$$
and
$$
g_3=21+\frac{2}{3}g_2.
$$
Substituting the first and third equations into the second,
$
g_2
=
29
+
\frac{3}{5}(31+g_2)
+
\frac{2}{5}
\left(
21+\frac{2}{3}g_2
\right)
=
56+\frac{13}{15}g_2.
$
Thus
$
g_2=420,
\qquad
g_1=451.
$

For second moments to vertex $1$, put
$$
s_i=\mathbb E_iT_1^2.
$$
Using the means $r_2=3,r_3=5,r_4=6$ gives
$$
s_2=5+\frac{2}{5}s_3,
$$
$$
s_3=9+\frac{2}{3}s_2+\frac{1}{3}s_4,
$$
and
$$
s_4=11+s_3.
$$
Using $s_4=11+s_3$ in the middle equation gives
$
s_3=19+s_2.
$
Then
$
s_2
=
5+\frac{2}{5}(19+s_2),
$
so
$
s_2=21,
\qquad
s_3=40,
\qquad
s_4=51.
$

Step 5: Compute the cover-time mean and variance
Let
$$
\tau_{\rm cov}
=
\inf\{n\geq0:\{X_0,X_1,\ldots,X_n\}=\{1,2,3,4\}\}
$$
for a walk started from $2$. At time $\sigma=T_1\wedge T_4$, exactly one endpoint has just been reached. If it is vertex $1$, completing the cover requires a fresh passage from $1$ to $4$; if it is vertex $4$, completing the cover requires a fresh passage from $4$ to $1$. By the strong Markov property, conditional on the first endpoint, this post-$\sigma$ passage is independent of the pre-$\sigma$ path.

Therefore
$$
\mathbb E_2\tau_{\rm cov}
=
m_2
+
p_2\mathbb E_1T_4
+
(1-p_2)\mathbb E_4T_1.
$$
Substituting the values from Steps 3 and 4,
$$
\mathbb E_2\tau_{\rm cov}
=
\frac{21}{11}
+
\frac{9}{11}\cdot16
+
\frac{2}{11}\cdot6
=
\frac{177}{11}.
$$

For the second moment,
$$
\mathbb E_2\tau_{\rm cov}^2
=
q_2
+
2\left(
16a_2
+
6(m_2-a_2)
\right)
+
451p_2
+
51(1-p_2).
$$
Thus
$$
\mathbb E_2\tau_{\rm cov}^2
=
\frac{699}{121}
+
2\left(
16\cdot\frac{171}{121}
+
6\cdot\frac{60}{121}
\right)
+
451\cdot\frac{9}{11}
+
51\cdot\frac{2}{11}
=
\frac{52662}{121}.
$$
Hence
$$
\operatorname{Var}_2(\tau_{\rm cov})
=
\frac{52662}{121}
-
\left(\frac{177}{11}\right)^2
=
\frac{21333}{121}.
$$
Combining this with $C_{14}=22$ gives the requested tuple.
Final Answer: $\boxed{\left(22,\frac{177}{11},\frac{21333}{121}\right)}$
---

## Answer

$\left(22,\frac{177}{11},\frac{21333}{121}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- reversible markov chains
- weighted tree random walks
- commute time metrics
- hitting time recursions
- cover time decomposition
