## Steps

Step 1: Determine the unperturbed weighted minimax polynomial

Write $w(x)=\sqrt{1+120x^2}$. At $\varepsilon=0$, both prescribed odd coefficients vanish. Replacing $P(x)$ by $(P(x)+P(-x))/2$ preserves monicity and cannot increase the weighted norm, so an optimizer has the form $P(x)=Q(x^2)$ with $Q$ monic cubic. For every monic cubic $Q$,
$$
-91Q(0)+128Q\left(\frac18\right)-63Q\left(\frac23\right)+26Q(1)=\frac{91}{12},
$$
because the left functional annihilates $1,t,t^2$ and takes the value $91/12$ on $t^3$. If $M=\max_{0\leq t\leq1}|Q(t)|/\sqrt{1+120t}$, then
$$
\frac{91}{12}\leq\left(91+128\cdot4+63\cdot9+26\cdot11\right)M=1456M,
$$
so $M\geq1/192$. Equality in the four contact equations gives
$$
Q_0(t)=t^3-\frac{31}{24}t^2+\frac{17}{48}t-\frac1{192}.
$$
The identity
$$
Q_0(t)^2-\frac{1+120t}{192^2}=t(t-1)\left(t-\frac18\right)^2\left(t-\frac23\right)^2
$$
shows that the bound is attained. Therefore
$$
\Lambda_c(0)=\frac1{192},\qquad
P_0(x)=x^6-\frac{31}{24}x^4+\frac{17}{48}x^2-\frac1{192}.
$$
Put $a=1/\sqrt8$ and $b=\sqrt{2/3}$. The contact points are $-1,-b,-a,0,a,b,1$, with signs $+,-,+,-,+,-,+$.

Step 2: Find the degenerate first-order tangent

The parameter $c$ enters the prescribed $x$-coefficient only at order $\varepsilon^2$. A first-order tangent has odd part
$$
O(x)=ux^5+x^3-\frac19x
$$
and an even part $E$ of degree at most $4$. For every such $E$,
$$
-\frac{E(0)}{16}+\frac{8E(a)}{91}-\frac{9E(b)}{208}+\frac{E(1)}{56}=0.
$$
Applying this identity to the four paired contact inequalities gives the sharp linearized value
$$
F(u)=\left(\frac1{1456\sqrt2}+\frac1{56}\right)\left|u+\frac89\right|
+\frac{\sqrt6}{624}|4u+5|.
$$
Since
$$
\frac1{1456\sqrt2}+\frac1{56}>\frac{\sqrt6}{156},
$$
the unique weighted median is $u=-8/9$. Hence, for every $c$,
$$
\Lambda_c'(0+)=d_0:=\frac{13\sqrt6}{5616}.
$$
The equality conditions determine
$$
E_0(x)=d_0(-32x^4+44x^2-1),
$$
$$
O_0(x)=-\frac89x^5+x^3-\frac19x,
\qquad H_0=E_0+O_0.
$$
The first-order equalities occur at
$$
-1,-b,-a,0,a,1,
$$
while $b$ has strict first-order slack. In particular, both $-a$ and $a$ remain active at first order. This is the degeneracy that controls the requested second-order function.

Step 3: Describe the complete dual segment at the degenerate contact set

Use the node order
$$
S=(-1,-b,-a,0,a,1)
$$
and the corresponding sign vector
$$
\sigma=(1,-1,1,-1,1,1).
$$
A signed dual vector $\beta=(\beta_z)_{z\in S}$ must satisfy
$$
\sum_{z\in S}\beta_zz^k=0\quad(k=0,2,4,5),
\qquad
\sum_{z\in S}\beta_z\sigma_zw(z)=1,
$$
with $\beta_z\sigma_z\geq0$. The five linear equations leave one degree of freedom, and positivity cuts the solution line to a segment. Its endpoints are
$$
\beta^+=\left(
\frac1{112}+\frac{\sqrt6}{312}+\frac{\sqrt2}{5824},
-\frac9{208},0,-\frac1{16},\frac8{91},
\frac1{112}-\frac{\sqrt6}{312}-\frac{\sqrt2}{5824}
\right),
$$
$$
\beta^-=\left(
\frac1{112}+\frac{\sqrt6}{312}-\frac{\sqrt2}{5824},
-\frac9{208},\frac8{91},-\frac1{16},0,
\frac1{112}-\frac{\sqrt6}{312}+\frac{\sqrt2}{5824}
\right).
$$
Substitution verifies the five moment equations, and every nonzero entry has the required sign. Thus every feasible dual vector is a convex combination of $\beta^+$ and $\beta^-$. The first endpoint omits $-a$, while the second omits $a$.

Step 4: Compute the two competing second-order branches

Write
$$
P_\varepsilon=P_0+\varepsilon H_0+\varepsilon^2J+o(\varepsilon^2),
\qquad
\Lambda_c(\varepsilon)=\frac1{192}+d_0\varepsilon+g\varepsilon^2+o(\varepsilon^2).
$$
The coefficient constraints give
$$
J(x)=cx+K(x),\qquad K\in\operatorname{span}\{x^5,x^4,x^2,1\}.
$$
For an interior first-order contact $z$ with sign $\sigma_z$, set
$$
C_z=P_0''(z)-\sigma_z\frac1{192}w''(z),
\qquad v_z=z'(0+).
$$
Differentiating the stationarity equation gives
$$
C_zv_z=\sigma_zd_0w'(z)-H_0'(z).
$$
At the four interior nodes this yields
$$
C_{-b}=\frac{2704}{729},\quad v_{-b}=\frac9{208},
\qquad C_0=\frac43,\quad v_0=\frac1{12},
$$
$$
C_{-a}=-\frac{1183}{1536},\quad v_{-a}=\frac{32(4-\sqrt3)}{507},
$$
$$
C_a=-\frac{1183}{1536},\quad v_a=\frac{32(4+\sqrt3)}{507}.
$$
Let $r_z=C_zv_z^2$, with $r_{-1}=r_1=0$. Then
$$
r_{-b}=\frac1{144},\qquad r_0=\frac1{108},
$$
$$
r_{-a}=\frac{-266+112\sqrt3}{4563},
\qquad r_a=\frac{-266-112\sqrt3}{4563}.
$$
Differentiating the contact-value equation twice and using stationarity cancels the second derivative of the moving node. The resulting second-order contact inequality is
$$
g\geq\frac{\sigma_zJ(z)}{w(z)}-\frac{\sigma_zr_z}{2w(z)}.
$$
Multiplying the inequality at $z$ by the nonnegative mass $\beta_z\sigma_z$ and summing eliminates $K$. Define
$$
A(\beta)=\sum_{z\in S}\beta_zz,
\qquad
B(\beta)=\sum_{z\in S}\beta_zr_z.
$$
Then
$$
g\geq cA(\beta)-\frac12B(\beta).
$$
At the two endpoints this becomes
$$
g_+(c)=\frac{91175+32768\sqrt3}{30371328}
+\left(\frac{5\sqrt6}{624}+\frac{9\sqrt2}{416}\right)c,
$$
$$
g_-(c)=\frac{91175-32768\sqrt3}{30371328}
+\left(\frac{5\sqrt6}{624}-\frac{9\sqrt2}{416}\right)c.
$$

To certify that these bounds come from actual local branches, write
$$
p_{\varepsilon,c}(x)=x^6+Ax^5+Bx^4+\varepsilon x^3+Cx^2+
\left(-\frac{\varepsilon}{9}+c\varepsilon^2\right)x+D.
$$
For the plus branch take moving nodes $(s_1,s_2,s_3)$ with base point $(-b,0,a)$ and signs $(1,-1,-1,1,1)$ at $(-1,s_1,s_2,s_3,1)$. For the minus branch use base point $(-b,-a,0)$ and signs $(1,-1,1,-1,1)$. With
$$
y=(A,B,C,D,L,s_1,s_2,s_3),
$$
define $\Phi_\pm(\varepsilon,y)$ by the five equations
$$
p_{\varepsilon,c}(x_j)-\sigma_jLw(x_j)=0
$$
at those five nodes and the three stationarity equations
$$
p_{\varepsilon,c}'(s_i)-\sigma_iLw'(s_i)=0\qquad(i=1,2,3).
$$
We use the following local solvability criterion: if a continuously differentiable system $\Phi(\varepsilon,y)=0$ satisfies $\Phi(0,y_0)=0$ and $\det D_y\Phi(0,y_0)\neq0$, then there is a unique continuously differentiable solution $y(\varepsilon)$ near $\varepsilon=0$ with $y(0)=y_0$.

At $\varepsilon=0$, the Jacobian is block triangular. Its value-equation blocks are
$$
M_+=\begin{pmatrix}
-1&1&1&1&-11\\
-b^5&b^4&b^2&1&9\\
0&0&0&1&1\\
a^5&a^4&a^2&1&-4\\
1&1&1&1&-11
\end{pmatrix},
\qquad
M_-=\begin{pmatrix}
-1&1&1&1&-11\\
-b^5&b^4&b^2&1&9\\
-a^5&a^4&a^2&1&-4\\
0&0&0&1&1\\
1&1&1&1&-11
\end{pmatrix},
$$
where the columns are $(A,B,C,D,L)$. Direct elimination gives
$$
\det M_+=-\frac{91}{18},\qquad \det M_-=\frac{91}{18}.
$$
The moving-node blocks are diagonal because each base contact is stationary:
$$
\operatorname{diag}(C_{-b},C_0,C_a)
\quad\text{and}\quad
\operatorname{diag}(C_{-b},C_{-a},C_0).
$$
Hence
$$
\det D_y\Phi_+(0,y_0)=\frac{18193357}{944784},
\qquad
\det D_y\Phi_-(0,y_0)=-\frac{18193357}{944784},
$$
so both five-contact branches exist uniquely. Differentiating their five value equalities twice gives the second-order coefficient $g$. Because $\beta^+$ and $\beta^-$ are supported exactly on the corresponding five contacts, summing those equalities with the dual masses gives equality in the two formulas above, so the branch coefficients are precisely $g_+(c)$ and $g_-(c)$.

Let $\ell_{-a}^+(c)$ be the second-order value required by the omitted contact $-a$ on the plus branch, and define $\ell_a^-(c)$ analogously. Substitution in the omitted inequalities gives
$$
g_+(c)-\ell_{-a}^+(c)=\frac{91}{32}\left(g_+(c)-g_-(c)\right),
$$
$$
g_-(c)-\ell_a^-(c)=\frac{91}{32}\left(g_-(c)-g_+(c)\right).
$$
Thus the plus branch is feasible exactly when $g_+(c)\geq g_-(c)$, and the minus branch is feasible exactly when the reverse inequality holds. The dual bound, the fixed gap away from the original contacts, and the first-order slack at $b$ therefore give
$$
G(c)=\max\{g_+(c),g_-(c)\}.
$$

Step 5: Combine the two branches into the requested function

Using $\max\{p,q\}=(p+q+|p-q|)/2$ in the two affine formulas from Step 4 gives
$$
G(c)=\frac{91175}{30371328}+\frac{5\sqrt6}{624}c
+\left|\frac{64\sqrt3}{59319}+\frac{9\sqrt2}{416}c\right|.
$$
Putting the three terms over the common denominator $30371328$ gives the compact form
$$
G(c)=\frac{91175+243360\sqrt6c+|32768\sqrt3+657072\sqrt2c|}{30371328}.
$$

Final Answer: $\boxed{G(c)=\frac{91175+243360\sqrt6c+|32768\sqrt3+657072\sqrt2c|}{30371328}}$

---

## Answer

$G(c)=\frac{91175+243360\sqrt6c+|32768\sqrt3+657072\sqrt2c|}{30371328}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Function or mapping

---

## Solution Concepts

- weighted minimax approximation
- dual moment certificates
- degenerate active sets
- moving contact perturbation
- second-order sensitivity envelopes
