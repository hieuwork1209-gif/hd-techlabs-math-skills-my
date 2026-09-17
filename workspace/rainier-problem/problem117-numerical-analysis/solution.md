## Steps

Step 1: Determine the three-point Gaussian nodes

Let
$$
d\mu_\tau(x)=dx+\tau(\delta_{-1}+\delta_1),\qquad \tau>0,
$$
and write
$$
m_k=\int_{-1}^1 x^k\,d\mu_\tau(x).
$$
The measure is even, so $m_{2j+1}=0$, while
$$
m_0=2+2\tau,
\qquad
m_{2j}=\frac{2}{2j+1}+2\tau\quad(j\ge1). \tag{1}
$$

The monic cubic orthogonal polynomial is odd, hence has the form
$$
g_3(x)=x(x^2-a^2).
$$
Orthogonality to $x$ gives
$$
0=\int xg_3(x)\,d\mu_\tau(x)=m_4-a^2m_2,
$$
so the nonzero nodes of the three-point Gaussian rule satisfy
$$
a^2=\frac{m_4}{m_2}
=\frac{\tau+1/5}{\tau+1/3}
=\frac{3(5\tau+1)}{5(3\tau+1)}. \tag{2}
$$
For $\tau>0$, this lies strictly between $0$ and $1$.

Step 2: Use the nested-node polynomial to force the parameter

Assume there is a symmetric seven-node rule
$$
Q(p)=A[p(-1)+p(1)]
+B[p(-b)+p(b)]
+C[p(-a)+p(a)]
+Dp(0), \tag{3}
$$
with
$$
0<b<a<1,\qquad A,B,C,D>0,
$$
which is exact for every polynomial of degree at most $11$. Put
$$
r=a^2,\qquad q=b^2.
$$
Its node polynomial is
$$
\Pi(x)=x(x^2-r)(x^2-q)(x^2-1).
$$
Since $\Pi$ vanishes at all seven nodes, $Q(\Pi x)=Q(\Pi x^3)=0$. Exactness therefore forces
$$
\int \Pi(x)x\,d\mu_\tau(x)=0,
\qquad
\int \Pi(x)x^3\,d\mu_\tau(x)=0. \tag{4}
$$
Expanding the first integral gives
$$
m_8-(1+r+q)m_6+(r+q+rq)m_4-rqm_2=0, \tag{5}
$$
and the second gives
$$
m_{10}-(1+r+q)m_8+(r+q+rq)m_6-rqm_4=0. \tag{6}
$$
Substitute the moments from (1) and $r$ from (2). After clearing the positive denominators, (5) and (6) reduce respectively to
$$
(90\tau+9)q=30\tau+1, \tag{7}
$$
$$
(330\tau+11)q=150\tau-5. \tag{8}
$$
Eliminating $q$ yields
$$
(30\tau+1)(330\tau+11)
=(150\tau-5)(90\tau+9),
$$
that is,
$$
450\tau^2+30\tau-7=0. \tag{9}
$$
The two roots are
$$
\frac{-1\pm\sqrt{15}}{30},
$$
so there is exactly one positive candidate,
$$
\tau_* = \frac{\sqrt{15}-1}{30}. \tag{10}
$$

At this value, (2) and (7) give
$$
r=\frac{15+2\sqrt{15}}{33},
\qquad
q=\frac{15-2\sqrt{15}}{33}. \tag{11}
$$
Hence
$$
0<q<r<1,
$$
so the extra node $b=\sqrt q$ really lies strictly between $0$ and the Gaussian node $a=\sqrt r$.

Step 3: Construct the positive degree-11 rule

At $\tau=\tau_*$, match the even moments of degrees $2,4,6$ in (3):
$$
A+Bq+Cr=\frac{m_2}{2},
$$
$$
A+Bq^2+Cr^2=\frac{m_4}{2},
$$
$$
A+Bq^3+Cr^3=\frac{m_6}{2}. \tag{12}
$$
Because $1,q,r$ are distinct, this Vandermonde system has a unique solution. Substitution of (10)-(11) gives
$$
A=\frac1{70}+\frac{\sqrt{15}}{30},
$$
$$
B=\frac{62}{175}+\frac{\sqrt{15}}{50},
$$
$$
C=\frac{62}{175}-\frac{\sqrt{15}}{50}. \tag{13}
$$
The degree-$0$ moment then gives
$$
D=m_0-2A-2B-2C=\frac{256}{525}. \tag{14}
$$
All four weights in (13)-(14) are positive.

The rule now matches degrees $0,2,4,6$. Equation (5) says its degree-$8$ error equals the error on $\Pi x$, hence vanishes. Once degree $8$ also matches, (6) says the degree-$10$ error equals the error on $\Pi x^3$, hence vanishes. Every odd polynomial is integrated exactly by symmetry. Therefore the rule is exact for every polynomial of degree at most $11$.

Step 4: Prove uniqueness

Conversely, any positive symmetric seven-node rule of the required nested form must satisfy (4), hence (7)-(9). Thus $\tau$ must equal the unique positive root (10), and then (7) fixes $q$. Equation (2) fixes the Gaussian node $r$, and the distinct-node system (12) fixes $A,B,C$, after which the mass equation fixes $D$. Therefore the compatible parameter and the entire positive nested rule are unique.

Final Answer: $\boxed{(\sqrt{15}-1)/30}$

---

## Answer

$(\sqrt{15}-1)/30$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Gaussian quadrature nodes
- nested quadrature compatibility
- orthogonal-polynomial moments
- node-polynomial annihilation
- positive quadrature weights
