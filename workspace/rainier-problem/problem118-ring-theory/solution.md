## Steps

Step 1: Reveal the hidden Lie basis and PBW structure
Let
$$
A=k[a,b,c,d].
$$
Define
$$
E=\frac{X+Y}{2},
\qquad
F=\frac{X-Y}{2},
\qquad
H=Z.
$$
The displayed commutator relations give
$$
[H,E]=2E,
\qquad
[H,F]=-2F,
\qquad
[E,F]=H.
$$
Their actions on $A$ are
$$
E(a)=0,
\quad E(b)=a,
\quad E(c)=2b,
\quad E(d)=3c,
$$
$$
F(a)=3b,
\quad F(b)=2c,
\quad F(c)=d,
\quad F(d)=0,
$$
and
$$
H(a)=3a,
\quad H(b)=b,
\quad H(c)=-c,
\quad H(d)=-3d.
$$
These derivations satisfy the same Lie brackets as $E,F,H$. Hence the presentation is the enveloping algebra of the semidirect product of the abelian span of $a,b,c,d$ by the three-dimensional Lie algebra spanned by $E,F,H$. PBW therefore gives a basis
$$
a^ib^jc^kd^\ell E^mH^nF^r,
$$
and the associated graded algebra for total $E,F,H$-degree is the polynomial domain
$$
\operatorname{gr}R=A[e,h,f].
$$

Step 2: Compute the invariant polynomials in the coefficient ring
Set
$$
p=ac-b^2,
$$
$$
q=a^2d-3abc+2b^3,
$$
and
$$
\Delta=a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2.
$$
Direct calculation gives
$$
E(p)=E(q)=E(\Delta)=0
$$
and
$$
a^2\Delta=q^2+4p^3.
$$
We first determine $\ker E$. Localize at $a$ and put
$$
t=\frac ba.
$$
Then $E(t)=1$, while
$$
c=\frac pa+at^2,
$$
$$
d=\frac q{a^2}+\frac{3tp}{a}+at^3.
$$
Thus
$$
A_a=k[a,a^{-1},t,p,q],
$$
and $E$ is differentiation with respect to $t$. Therefore
$$
(\ker E)_a=k[a,a^{-1},p,q].
$$

To intersect back with $A$, write an element as $a^{-N}G(a,p,q)$ with $N\geq0$. If $N>0$, polynomiality in $A$ gives
$$
G(0,-b^2,2b^3)=0.
$$
The kernel of
$$
k[p,q]\to k[b],
\qquad
p\mapsto-b^2,
\quad q\mapsto2b^3,
$$
is the principal ideal $(q^2+4p^3)$: after division by this polynomial, a remainder has the form $A(p)+qB(p)$, and substitution separates even and odd powers of $b$. Hence
$$
G(0,p,q)=(q^2+4p^3)G_0(p,q).
$$
Lift $G_0$ and write
$$
G=(q^2+4p^3)G_1+aG_2.
$$
Using $q^2+4p^3=a^2\Delta$ gives
$$
a^{-N}G=a^{-(N-2)}\Delta G_1+a^{-(N-1)}G_2.
$$
Induction on $N$ therefore yields
$$
A\cap k[a,a^{-1},p,q]=k[a,p,q,\Delta],
$$
so
$$
\ker E=k[a,p,q,\Delta].
$$

The $H$-weights of $a,p,q,\Delta$ are respectively
$$
3,
\qquad2,
\qquad3,
\qquad0.
$$
Therefore the weight-zero part of $\ker E$ is exactly $k[\Delta]$. Any polynomial fixed by $E,F,H$ is in particular fixed by $E$ and $H$, so it lies in $k[\Delta]$. A direct substitution also gives $F(\Delta)=0$. Hence
$$
A^{E,F,H}=k[\Delta].
$$

Step 3: Exclude every positive skew degree from the center
Let $z\in Z(R)$ and suppose its total $E,F,H$-degree is $N$. Let
$$
s\in A[e,h,f]
$$
be its leading symbol. For any $g\in A$, the degree-$(N-1)$ symbol of $[z,g]$ is
$$
E(g)\,\partial_e s+H(g)\,\partial_h s+F(g)\,\partial_f s.
$$
Since $z$ is central, this vanishes for every $g\in A$.

Over the fraction field of $A$, the derivations $E,H,F$ are linearly independent. Indeed, the coefficient matrix obtained from their values on $a,b,c$ has a $3\times3$ determinant which specializes to a nonzero value at
$$
a=1,
\qquad b=c=0,
\qquad d=1.
$$
Thus
$$
\partial_e s=\partial_h s=\partial_f s=0.
$$
Because the characteristic is zero, $s$ is independent of $e,h,f$. This is impossible when $N>0$. Therefore every central element has skew degree zero, so
$$
Z(R)\subseteq A.
$$

Step 4: Assemble the center
An element of $A$ commutes with $E,F,H$, equivalently with $X,Y,Z$, exactly when it belongs to
$$
A^{E,F,H}=k[\Delta].
$$
Conversely $\Delta$ commutes with $A$ and is killed by $E,F,H$, so it is central. Therefore
$$
Z(R)=k[\Delta]
=k[a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2].
$$
Final Answer: $\boxed{k[a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2]}$

---

## Answer

$k[a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- PBW filtrations
- semidirect enveloping algebras
- hidden Lie actions
- invariant subrings
- binary cubic discriminants

---

## Black-Box Audit — no issues found
