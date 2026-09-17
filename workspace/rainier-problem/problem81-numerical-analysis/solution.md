## Steps

Step 1: Rewrite the real-axis stability condition

Consider
$$
R_a(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+az^4.
$$
For $y\ge0$, put
$$
P_a(y)=R_a(-y)=1-y+\frac{y^2}{2}-\frac{y^3}{6}+ay^4.
$$
If $L>0$, then the interval $[-L,0]$ lies in the absolute-stability region exactly when
$$
|P_a(y)|\le1
\qquad(0\le y\le L).
$$
For $y>0$, the two inequalities $-1\le P_a(y)\le1$ are equivalent to
$$
A_-(y)\le a\le A_+(y),
\tag{1}
$$
where
$$
A_+(y)=\frac1{y^3}-\frac1{2y^2}+\frac1{6y},
$$
$$
A_-(y)=A_+(y)-\frac2{y^4}.
$$
Hence there exists a coefficient $a$ stabilizing the whole interval $[-L,0]$ iff
$$
\sup_{0<y\le L}A_-(y)
\le
\inf_{0<y\le L}A_+(y).
\tag{2}
$$

Step 2: Analyze the two envelope functions

Differentiate:
$$
A_+'(y)
=-\frac{y^2-6y+18}{6y^4}.
$$
Since
$$
y^2-6y+18=(y-3)^2+9>0,
$$
we have
$$
A_+'(y)<0
\qquad(y>0).
$$
Therefore
$$
\inf_{0<y\le L}A_+(y)=A_+(L).
\tag{3}
$$

Also
$$
A_-'(y)
=-\frac{f(y)}{6y^5},
$$
where
$$
f(y)=y^3-6y^2+18y-48.
$$
Now
$$
f'(y)=3\bigl((y-2)^2+2\bigr)>0,
$$
so $f$ has a unique real zero. Denote it by $m_*$. Since
$$
f(4)=-8,
\qquad
f(5)=17,
$$
one has
$$
4<m_*<5.
$$
Thus $A_-$ increases on $(0,m_*)$ and decreases on $(m_*,\infty)$, so its global maximum occurs uniquely at $m_*$.

Therefore, for every $L\ge m_*$,
$$
\sup_{0<y\le L}A_-(y)=A_-(m_*).
\tag{4}
$$

Step 3: Identify the unique optimal crossing

Define
$$
a_*=A_-(m_*).
$$
Using $f(m_*)=0$, a short simplification gives
$$
\boxed{
a_*=\frac{m_*^2-2m_*+2}{8m_*^3}.
}
\tag{5}
$$
This is positive.

At $L=m_*$,
$$
A_+(m_*)-A_-(m_*)=\frac2{m_*^4}>0.
$$
On the other hand,
$$
A_+(L)\to0
\qquad(L\to\infty),
$$
while $a_*>0$. Since $A_+$ is strictly decreasing, there is a unique number $L_*>m_*$ such that
$$
A_+(L_*)=a_*.
\tag{6}
$$

For $L\le L_*$, condition (2) is satisfied. For $L>L_*$, (2) fails because
$$
\sup A_-=a_*>A_+(L)=\inf A_+.
$$
Hence $L_*$ is the maximal possible real-axis stability radius.

At $L=L_*$, the admissible interval for $a$ in (1) collapses to the single value $a_*$, so the optimizing coefficient is unique.

The two active contacts are
$$
P_{a_*}(m_*)=-1,
\qquad
P_{a_*}(L_*)=1.
$$
Moreover $m_*$ is the unique interior minimum contact, since $A_-'(m_*)=0$ is equivalent to
$$
P_{a_*}'(m_*)=0.
$$

Step 4: Give exact algebraic characterizations

The interior contact is the unique real root of
$$
\boxed{
m^3-6m^2+18m-48=0.
}
\tag{7}
$$
Equivalently, if $m_*$ denotes that root, then $a_*$ is given by (5).

Eliminating $m_*$ from (5) and (7) gives
$$
\boxed{
884736a^3-60048a^2+1728a-17=0.
}
\tag{8}
$$
The derivative of the cubic in (8) is
$$
864(3072a^2-139a+2),
$$
whose quadratic factor has negative discriminant, so (8) has exactly one real root. Thus (8) alone also characterizes $a_*$ uniquely.

From (6), $L_*$ satisfies
$$
\boxed{
6a_*L^3-L^2+3L-6=0,
\qquad L>m_*.
}
\tag{9}
$$
Because $A_+$ is strictly decreasing, (9) has exactly one solution with $L>m_*$.

Eliminating $a_*$ and $m_*$ yields the integer polynomial
$$
17L^9-288L^8+2532L^7-15832L^6+71892L^5-244368L^4
$$
$$
\hspace{15mm}
+613008L^3-1105920L^2+1327104L-884736=0,
\tag{10}
$$
and $L_*$ is its unique real root in $(6,7)$.

Numerically,
$$
m_*\approx4.39034924017418,
$$
$$
a_*\approx0.0184557022688728,
$$
$$
L_*\approx6.02725972343821.
$$

Therefore the unique optimal parameter and maximal real-axis stability radius are
$$
\boxed{
(a_*,L_*)
}
$$
with $a_*$ and $L_*$ characterized exactly by (8)--(9), or equivalently by (7)--(9).

---

## Answer

$\left(a_*,L_*\right)$, where $a_*$ is the unique real root of $884736a^3-60048a^2+1728a-17=0$, and $L_*$ is the unique root $>m_*$ of $6a_*L^3-L^2+3L-6=0$, with $m_*$ the unique real root of $m^3-6m^2+18m-48=0$.

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- absolute-stability polynomials
- envelope characterization of uniform constraints
- equioscillation at active contacts
- algebraic elimination
- uniqueness from monotone envelopes
