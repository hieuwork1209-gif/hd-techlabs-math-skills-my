## Steps

Step 1: Encode the presentation by an infinite-order automorphism
Let
$$
A=k[a,b,c,d]
$$
and let $D$ be the derivation
$$
D(a)=0,
\qquad D(b)=a,
\qquad D(c)=2b,
\qquad D(d)=3c.
$$
Let $\rho$ be the involution sending each of $a,b,c,d$ to its negative. Since $D$ preserves total degree, $D$ commutes with $\rho$. Hence
$$
\sigma=\rho\exp(D)
$$
is an automorphism of $A$, with
$$
\begin{aligned}
\sigma(a)&=-a,\\
\sigma(b)&=-(b+a),\\
\sigma(c)&=-(c+2b+a),\\
\sigma(d)&=-(d+3c+3b+a).
\end{aligned}
$$
Its inverse is $\rho\exp(-D)$, so
$$
\begin{aligned}
\sigma^{-1}(a)&=-a,\\
\sigma^{-1}(b)&=a-b,\\
\sigma^{-1}(c)&=-c+2b-a,\\
\sigma^{-1}(d)&=-d+3c-3b+a.
\end{aligned}
$$
The defining relations are therefore
$$
xf=\sigma(f)x,
\qquad
yf=\sigma^{-1}(f)y
\qquad(f\in A),
$$
together with $yx=xy$. Thus $R$ is an iterated skew polynomial ring and has a unique PBW normal form
$$
\sum \lambda_{i,j,r,s,t,u}a^ib^jc^rd^sx^ty^u.
$$
Moreover
$$
C=xy
$$
is central because $x$ and $y$ commute and act on $A$ by inverse automorphisms.

Step 2: Compute the kernel of the Jordan derivation
Define
$$
p=ac-b^2,
$$
$$
q=a^2d-3abc+2b^3,
$$
and
$$
r=a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2.
$$
Direct differentiation gives
$$
D(p)=D(q)=D(r)=0,
$$
and direct expansion gives the relation
$$
a^2r=q^2+4p^3.
$$
We claim
$$
\ker D=k[a,p,q,r].
$$
Localize at $a$ and put
$$
u=\frac ba.
$$
Then $D(u)=1$, and from the definitions of $p$ and $q$,
$$
c=\frac pa+au^2,
$$
$$
d=\frac q{a^2}+\frac{3up}{a}+au^3.
$$
Hence
$$
A_a=k[a,a^{-1},u,p,q],
$$
and on this ring $D$ is differentiation with respect to $u$. Therefore
$$
(\ker D)_a=k[a,a^{-1},p,q].
$$
It remains to intersect back with $A$. Let an element of this intersection be written as $a^{-N}F(a,p,q)$ with $N\geq0$. If $N>0$, then reducing the numerator modulo $a$ gives
$$
F(0,-b^2,2b^3)=0.
$$
The kernel of the substitution $k[p,q]\to k[b]$ given by $p\mapsto-b^2$, $q\mapsto2b^3$ is the principal ideal
$$
(q^2+4p^3).
$$
Indeed, after division by $q^2+4p^3$, a remainder has the form $A(p)+qB(p)$; substituting $p=-b^2$, $q=2b^3$ separates even and odd powers of $b$, forcing $A=B=0$. Thus
$$
F(0,p,q)=(q^2+4p^3)G_0(p,q).
$$
Lifting $G_0$ and using $q^2+4p^3=a^2r$ reduces the negative power of $a$. Induction on $N$ yields
$$
A\cap k[a,a^{-1},p,q]=k[a,p,q,r],
$$
proving the claim.

Step 3: Determine the fixed ring of the hidden automorphism
Because $\rho$ commutes with $D$ and $\rho^2=\operatorname{id}$,
$$
\sigma^2=\exp(2D).
$$
If $f\in A$ is fixed by $\sigma$, then it is fixed by $\sigma^2$. In the localization from Step 2, $\exp(2D)$ sends $u$ to $u+2$ and fixes $a,p,q$. A polynomial fixed by the nonzero translation $u\mapsto u+2$ is independent of $u$, so
$$
f\in\ker D=k[a,p,q,r].
$$
On $\ker D$, the exponential part acts trivially, so $\sigma$ restricts to $\rho$. The elements $a$ and $q$ have odd total degree, while $p$ and $r$ have even total degree. Using
$$
q^2=a^2r-4p^3,
$$
every element of $k[a,p,q,r]$ can be reduced to a sum of monomials containing at most one factor of $q$. Such a monomial is $\rho$-fixed exactly when the exponents of $a$ and $q$ have the same parity. Consequently
$$
A^\sigma=k[a^2,p,r,aq].
$$

Step 4: Eliminate nonzero skew degrees and assemble the center
Give $R$ the grading
$$
\deg x=1,
\qquad
\deg y=-1,
\qquad
\deg A=0.
$$
Since $C=xy$ is central, the degree-zero part is
$$
B=A[C],
$$
and every positive homogeneous element has the form $bx^n$ with $b\in B$, while every negative homogeneous element has the form $by^n$.

Suppose $bx^n$ is central with $n>0$. If $n$ is odd, then
$$
\sigma^n(a)=-a,
$$
so commutation with $a$ forces $b=0$. If $n$ is even, then
$$
\sigma^n=\exp(nD)
$$
and therefore
$$
\sigma^n(b)=b+na
$$
for the coefficient generator $b\in A$ from the presentation. Since $A[C]$ is a domain and the characteristic is zero, commutation with that generator again forces the homogeneous coefficient to vanish. The same argument with $\sigma^{-n}$ eliminates every negative degree.

Thus every central element lies in $B$. Because $\sigma(C)=C$, an element of $B$ commutes with $x$ and $y$ exactly when its $A$-coefficients lie in $A^\sigma$. Hence
$$
Z(R)=A^\sigma[C]
=k[xy,a^2,p,r,aq].
$$
Substituting the definitions of $p,q,r$ gives
$$
Z(R)=k[xy,a^2,ac-b^2,a(a^2d-3abc+2b^3),a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2].
$$
Final Answer: $\boxed{k[xy,a^2,ac-b^2,a(a^2d-3abc+2b^3),a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2]}$

---

## Answer

$k[xy,a^2,ac-b^2,a(a^2d-3abc+2b^3),a^2d^2-6abcd+4ac^3+4b^3d-3b^2c^2]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- iterated skew polynomial rings
- locally nilpotent derivations
- Weitzenbock invariants
- fixed subrings of polynomial automorphisms
- graded-center arguments

---

## Black-Box Audit — no issues found
