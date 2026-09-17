## Steps

Step 1: Convert stability on the negative real axis to an affine-envelope problem

Write
$$
P_{a,b}(y)=R_{a,b}(-y)
=1-y+\frac{y^2}{2}-\frac{y^3}{6}+ay^4-by^5,
\qquad y\ge0.
$$
For $y>0$, the condition
$$
-1\le P_{a,b}(y)\le1
$$
is equivalent to
$$
A_-(y)\le q(y)\le A_+(y),
\qquad
q(y)=a-by,
\tag{1}
$$
where
$$
A_+(y)=\frac1{y^3}-\frac1{2y^2}+\frac1{6y},
$$
$$
A_-(y)=A_+(y)-\frac2{y^4}.
\tag{2}
$$
Thus the problem is to find an affine function $q(y)=a-by$ which stays in the strip between $A_-$ and $A_+$ for as long as possible.

Step 2: Construct the unique common supporting line

We have
$$
A_+'(y)=-\frac{y^2-6y+18}{6y^4},
$$
$$
A_+''(y)=\frac{y^2-9y+36}{3y^5}>0
\qquad(y>0),
\tag{3}
$$
so $A_+$ is strictly convex.

Also
$$
A_-'(y)
=-\frac{y^3-6y^2+18y-48}{6y^5},
$$
$$
A_-''(y)
=\frac{y^3-9y^2+36y-120}{3y^6}.
\tag{4}
$$
On $5\le y\le 11/2$, the numerator in (4) is negative, so $A_-'$ is strictly decreasing there.

For a slope $s<0$, let $m$ be a point on the lower curve and $n$ a point on the upper curve with the same tangent slope:
$$
A_-'(m)=A_+'(n)=s.
\tag{5}
$$
Since $A_-'(m)=A_+'(m)+8/m^5>A_+'(m)$ and $A_+'$ is strictly increasing, every such pair has
$$
n>m.
$$
The two tangents coincide exactly when their intercepts coincide:
$$
A_-(m)-mA_-'(m)
=
A_+(n)-nA_+'(n).
\tag{6}
$$
Equations (5)--(6) are equivalent to the polynomial system
$$
m^5(n^2-6n+18)
-n^4(m^3-6m^2+18m-48)=0,
\tag{7}
$$
$$
n^3(2m^3-9m^2+24m-60)
-m^4(2n^2-9n+24)=0.
\tag{8}
$$

There is a unique solution of (7)--(8) with
$$
5<m<\frac{11}{2},
\qquad n>m.
\tag{9}
$$
To see uniqueness, regard $n=n(m)$ as determined by (5). Put
$$
J(m)
=
A_-(m)-mA_-'(m)
-
\bigl(A_+(n(m))-n(m)A_+'(n(m))\bigr).
$$
Differentiating through (5) gives
$$
J'(m)=(n(m)-m)A_-''(m)<0
$$
on $(5,11/2)$. At $m=5$, the slope equality gives $n(5)>10$, and
$$
A_-(5)-5A_-'(5)
-
\bigl(A_+(10)-10A_+'(10)\bigr)
=\frac1{3000}>0.
$$
At $m=11/2$, the slope equality gives $n(11/2)<44/5$, and
$$
A_-\!\left(\frac{11}{2}\right)
-\frac{11}{2}A_-'\!\left(\frac{11}{2}\right)
-
\left(
A_+\!\left(\frac{44}{5}\right)
-\frac{44}{5}A_+'\!\left(\frac{44}{5}\right)
\right)
=-\frac{115}{468512}<0.
$$
Hence $J$ has exactly one zero in $(5,11/2)$.

Denote the unique solution by $(m_*,n_*)$. Numerically,
$$
m_*\approx5.313101567870497,
\qquad
n_*\approx9.157447340251675.
$$
The common tangent line is
$$
q_*(y)=a_*-b_*y,
$$
with
$$
\boxed{
 b_*=-A_+'(n_*)
 =\frac{n_*^2-6n_*+18}{6n_*^4},
}
\tag{10}
$$
$$
\boxed{
 a_*=A_+(n_*)-n_*A_+'(n_*)
 =\frac{2n_*^2-9n_*+24}{6n_*^3}.
}
\tag{11}
$$
Numerically,
$$
a_*\approx0.02372183246172764,
\qquad
b_*\approx0.001111872409731495.
$$

Step 3: Determine the last lower-envelope intersection

Define
$$
D(y)=q_*(y)-A_-(y).
$$
At $y=m_*$,
$$
D(m_*)=D'(m_*)=0.
$$
The cubic numerator of $A_-''$,
$$
g(y)=y^3-9y^2+36y-120,
$$
has exactly one positive root $c$ because
$$
g'(y)=3\bigl((y-3)^2+3\bigr)>0,
$$
and $6<c<7$. Hence $A_-'$ decreases on $(0,c)$ and increases on $(c,\infty)$.

Since $m_*<c$ and $q_*'=A_-'(m_*)<0$, the equation
$$
D'(y)=0
$$
has exactly two positive solutions: $m_*$ and one point $d_*>c$. The first is a strict local minimum of $D$, the second a strict local maximum. Moreover
$$
D(y)\to+\infty\quad(y\downarrow0),
$$
while
$$
D(y)\to-\infty\quad(y\to\infty)
$$
because $b_*>0$. Therefore there is a unique root
$$
L_*>d_*
$$
of $D$, and
$$
D(y)\ge0
\qquad(0<y\le L_*).
\tag{12}
$$
Equivalently, $L_*$ is the unique root $>n_*$ of
$$
6(a_*-b_*L)L^4-L^3+3L^2-6L+12=0.
\tag{13}
$$
Numerically,
$$
L_*\approx10.535518013528512.
$$

Step 4: Verify feasibility of the constructed polynomial

Because $A_+$ is strictly convex and $q_*$ is tangent to $A_+$ at $n_*$,
$$
q_*(y)\le A_+(y)
\qquad(y>0).
\tag{14}
$$
By (12),
$$
q_*(y)\ge A_-(y)
\qquad(0<y\le L_*).
\tag{15}
$$
Thus (1) holds on $(0,L_*]$, so
$$
|P_{a_*,b_*}(y)|\le1
\qquad(0\le y\le L_*).
$$
The active contacts are
$$
P_{a_*,b_*}(m_*)=-1,
\qquad
P_{a_*,b_*}'(m_*)=0,
$$
$$
P_{a_*,b_*}(n_*)=1,
\qquad
P_{a_*,b_*}'(n_*)=0,
$$
$$
P_{a_*,b_*}(L_*)=-1.
\tag{16}
$$

Step 5: Prove global optimality and uniqueness

Let
$$
\widetilde q(y)=\widetilde a-\widetilde b\,y
$$
be any affine function feasible on $[0,L]$ with $L\ge L_*$. Put
$$
h(y)=\widetilde q(y)-q_*(y).
$$
At the lower contact $m_*$, feasibility gives
$$
h(m_*)\ge0.
$$
At the upper contact $n_*$, feasibility gives
$$
h(n_*)\le0.
$$
Since $h$ is affine and $m_*<n_*$, its slope is nonpositive, so for every $y\ge n_*$,
$$
h(y)\le h(n_*)\le0.
$$
At $L_*$, lower feasibility gives
$$
h(L_*)
=\widetilde q(L_*)-q_*(L_*)
\ge0.
$$
Hence
$$
h(L_*)=h(n_*)=0.
$$
An affine function with two distinct zeros is identically zero, so
$$
\widetilde q=q_*.
$$
But for every $y>L_*$ sufficiently close to $L_*$, and in fact for all $y>L_*$ until no further real crossing occurs,
$$
q_*(y)<A_-(y),
$$
so $q_*$ is not feasible beyond $L_*$. Therefore no coefficient pair can have a larger stability radius.

Thus $(a_*,b_*)$ is the unique optimizer and $L_*$ is the exact maximal radius.

Final Answer:
$$
\boxed{
(a_*,b_*,L_*,m_*,n_*)
}
$$
where $(m_*,n_*)$ is the unique solution of (7)--(9), $a_*,b_*$ are given by (10)--(11), and $L_*$ is the unique root $>n_*$ of (13).

Numerically,
$$
\boxed{
(a_*,b_*,L_*,m_*,n_*)
\approx
(0.02372183246172764,
0.001111872409731495,
10.535518013528512,
5.313101567870497,
9.157447340251675).
}
$$

---

## Answer

$\left(a_*,b_*,L_*,m_*,n_*\right)$, where $(m_*,n_*)$ is the unique solution with $5<m_*<11/2$ and $n_*>m_*$ of
$$
m_*^5(n_*^2-6n_*+18)-n_*^4(m_*^3-6m_*^2+18m_*-48)=0,
$$
$$
n_*^3(2m_*^3-9m_*^2+24m_*-60)-m_*^4(2n_*^2-9n_*+24)=0,
$$
$$
a_*=\frac{2n_*^2-9n_*+24}{6n_*^3},
\qquad
b_*=\frac{n_*^2-6n_*+18}{6n_*^4},
$$
and $L_*>n_*$ is the unique root of
$$
6(a_*-b_*L)L^4-L^3+3L^2-6L+12=0.
$$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- absolute-stability polynomial optimization
- affine envelope feasibility
- common supporting tangents
- equioscillation contacts
- global optimality from active constraints
