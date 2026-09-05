## Steps

Step 1: Reveal common coordinates for the two hidden automorphisms
Let
$$
A=k[u,v,w],
\qquad
\Delta=v^2+uw,
$$
and set
$$
p=u-2v\Delta-w\Delta^2,
\qquad
q=v+w\Delta,
\qquad
r=w.
$$
Since
$$
q^2+pr=\Delta,
$$
this is an invertible polynomial change of coordinates: if
$$
\delta=q^2+pr,
$$
then
$$
u=p+2q\delta-r\delta^2,
\qquad
v=q-r\delta,
\qquad
w=r.
$$
Thus $A=k[p,q,r]$. Now put
$$
a=p+q,
\qquad
b=q+r,
\qquad
c=r.
$$
Then $A=k[a,b,c]$.

For the first automorphism, the triple used in the problem is
$$
P=-8p+19q-98r,
\qquad
Q=-27q+98r,
\qquad
R=-125r.
$$
Applying the inverse Nagata change to $(P,Q,R)$ is exactly the displayed formula for $\sigma(u),\sigma(v),\sigma(w)$. Therefore
$$
\sigma(p)=P,
\qquad
\sigma(q)=Q,
\qquad
\sigma(r)=R,
$$
and hence
$$
\sigma(a)=-8a,
\qquad
\sigma(b)=-27b,
\qquad
\sigma(c)=-125c.
$$
Similarly the second triple is
$$
\widetilde P=-\frac14p-\frac5{36}q+\frac{16}{225}r,
$$
$$
\widetilde Q=-\frac19q-\frac{16}{225}r,
\qquad
\widetilde R=-\frac1{25}r,
$$
so
$$
\tau(a)=-\frac14a,
\qquad
\tau(b)=-\frac19b,
\qquad
\tau(c)=-\frac1{25}c.
$$
In particular $\sigma$ and $\tau$ commute.

Step 2: Compute the common fixed ring and the relation lattice
The product $\sigma\tau$ acts by
$$
a\mapsto2a,
\qquad
b\mapsto3b,
\qquad
c\mapsto5c.
$$
If a polynomial in $A$ is fixed by both $\sigma$ and $\tau$, then it is fixed by $\sigma\tau$. For a monomial $a^ib^jc^\ell$, this multiplies it by
$$
2^i3^j5^\ell.
$$
Because the characteristic is zero, this equals $1$ only for $i=j=\ell=0$. Hence
$$
A^{\langle\sigma,\tau\rangle}=k.
$$

For integers $m,n$, the automorphism $\sigma^m\tau^n$ acts on $a$ by
$$
(-1)^{m+n}2^{3m-2n}.
$$
Thus $\sigma^m\tau^n=\operatorname{id}$ forces
$$
3m-2n=0
$$
and $m+n$ even. Writing $m=2r$, $n=3r$, the parity condition becomes $5r$ even, so $r$ is even. Therefore
$$
\sigma^m\tau^n=\operatorname{id}
\quad\Longleftrightarrow\quad
(m,n)=(4s,6s)
$$
for some $s\in\mathbb Z$.

Step 3: Translate the automorphism lattice into central skew degrees
Let the four skew generators be $x,y,z,t$, where $x,y$ use $\sigma,\sigma^{-1}$ and $z,t$ use $\tau,\tau^{-1}$. Since $\sigma$ and $\tau$ commute and the four skew generators commute pairwise, $R$ has PBW basis
$$
f_{i,j,k,\ell}x^iy^jz^kt^\ell,
\qquad
f_{i,j,k,\ell}\in A.
$$
For $g\in A$,
$$
x^iy^jz^kt^\ell g
=
\sigma^{i-j}\tau^{k-\ell}(g)x^iy^jz^kt^\ell.
$$
Hence a nonzero term in a central element must satisfy
$$
(i-j,k-\ell)=(4s,6s)
$$
for some integer $s$.

Also, commuting a coefficient with $x$ and $z$ forces it to be fixed by both $\sigma$ and $\tau$, so by Step 2 every central coefficient lies in $k$.

Step 4: Generate the full central semigroup
Set
$$
C=xy,
\qquad
D=zt,
\qquad
M=x^4z^6,
\qquad
N=y^4t^6.
$$
The relation lattice from Step 2 shows that all four are central.

Conversely, let $x^iy^jz^kt^\ell$ be central. If $s\geq0$, then
$$
i=j+4s,
\qquad
k=\ell+6s,
$$
so
$$
x^iy^jz^kt^\ell=C^jD^\ell M^s.
$$
If $s<0$, the same argument gives a product of powers of $C,D,N$. Therefore every central monomial lies in
$$
k[C,D,M,N].
$$
Thus
$$
Z(R)=k[xy,zt,x^4z^6,y^4t^6].
$$
Final Answer: $\boxed{k[xy,zt,x^4z^6,y^4t^6]}$

---

## Answer

$k[xy,zt,x^4z^6,y^4t^6]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- iterated skew polynomial rings
- simultaneous polynomial conjugacy
- automorphism relation lattices
- invariant subrings
- affine semigroup generators

---

## Black-Box Audit — no issues found
