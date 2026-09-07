## Steps

Step 1: Localize and remove the Heisenberg action
Let \(\mathfrak g\) be the Lie algebra defined by the displayed relations, so \(R=U(\mathfrak g)\). PBW implies that \(R\) is a domain. Since \(z\) is central and regular, form
\[
S=R[z^{-1}].
\]
Put
\[
e=E-\frac{p^2}{2z},\qquad
f=F+\frac{q^2}{2z},\qquad
h=H+\frac{pq}{z}-\frac12.
\]
Using \([p,q]=z\) and the action of \(E,F,H\) on \(p,q\), one checks
\[
[e,p]=[e,q]=[f,p]=[f,q]=[h,p]=[h,q]=0
\]
and
\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h.
\]
The generators \(x,y,t,a,b,c\) commute with \(p,q,z\), so replacing \(E,F,H\) by \(e,f,h\) leaves all their other brackets unchanged. Hence, over
\[
K=k[z^{\pm1}],
\]
the generators
\[
e,f,h,x,y,t,a,b,c
\]
form the truncated current algebra
\[
\mathfrak l=\mathfrak{sl}_2[\varepsilon]/(\varepsilon^3),
\]
with \((x,y,t)=\varepsilon(e,f,h)\) and \((a,b,c)=\varepsilon^2(e,f,h)\). The localized Weyl pair \(p,q\) commutes with \(U_K(\mathfrak l)\). The usual Weyl-basis argument therefore gives
\[
Z(S)=Z\!\left(U_K(\mathfrak l)\right).
\]

Step 2: Compute the Poisson center of the third-order current algebra
Pass to the PBW associated graded Poisson algebra
\[
Q=K[e,f,h,x,y,t,a,b,c].
\]
Define
\[
A=c^2+4ab,
\]
\[
B=tc+2xb+2ya,
\]
\[
C=ch+\frac12t^2+2be+2af+2xy.
\]
Direct use of the current-algebra brackets gives zero Poisson bracket of each of \(A,B,C\) with all nine generators.

To prove that these exhaust the Poisson center, localize further at \(a\). The Hamiltonian derivations induced by \(a,c\) on the variables \(e,f,h\) are
\[
D_a=c\,\partial_f-2a\,\partial_h,
\qquad
D_c=2a\,\partial_e-2b\,\partial_f,
\]
and
\[
D_b=-\frac baD_a-\frac{c}{2a}D_c.
\]
Their common kernel is
\[
K[a^{\pm1},b,c,x,y,t,L],
\qquad
L=ch+2af+2be.
\]
Now replace \(L\) by
\[
C=L+\frac12t^2+2xy.
\]
The derivations induced by \(x,t,y\) fix \(C\), and on \(x,y,t\) they are
\[
c\,\partial_y-2a\,\partial_t,
\qquad
2a\,\partial_x-2b\,\partial_y,
\qquad
-c\,\partial_x+2b\,\partial_t.
\]
The third is again a linear combination of the first two, and their common kernel is
\[
K[a^{\pm1},b,c,B,C].
\]
Finally the derivation induced by \(e\) on \(a,b,c\) is
\[
c\,\partial_b-2a\,\partial_c.
\]
Since
\[
A=c^2+4ab,
\qquad
b=\frac{A-c^2}{4a},
\]
its kernel is \(K[a^{\pm1},A]\). The derivation of \(h\) is \(2a\partial_a-2b\partial_b\), so imposing it leaves exactly \(K[A]\). Thus
\[
Z_{\mathrm{Pois}}(Q[a^{-1}])=K[A,B,C].
\]
No denominator in \(a\) occurs for a polynomial invariant. Indeed, modulo \(a\), the images of \(A,B,C\) are algebraically independent: at
\[
(c,b,x,y,t,h,e)=(1,0,0,0,0,0,0)
\]
their differentials have independent \(dc,dt,dh\) components. Hence
\[
Z_{\mathrm{Pois}}(Q)=K[A,B,C].
\]

Step 3: Lift the three Poisson generators to the enveloping center
The PBW symmetrization map is adjoint-equivariant: for a quadratic monomial it sends \(uv\) to \((uv+vu)/2\), and commuting a generator through this symmetrized product gives the symmetrization of the corresponding Poisson derivation. Therefore the symmetrizations of the invariant quadratics \(A,B,C\) are central.

The first two require no correction:
\[
A=c^2+4ab,
\qquad
B=tc+2xb+2ya.
\]
For \(C\), using
\[
[e,b]=c,\qquad [f,a]=-c,\qquad [x,y]=c,
\]
its symmetrization is
\[
\Gamma=ch+\frac12t^2+2eb+2fa+2xy-c.
\]
Thus \(A,B,\Gamma\) are central in \(U_K(\mathfrak l)\). Their leading PBW symbols are \(A,B,C\), so Step 2 and PBW-degree induction give
\[
Z\!\left(U_K(\mathfrak l)\right)=K[A,B,\Gamma].
\]
Consequently
\[
Z(S)=k[z^{\pm1},A,B,\Gamma].
\]

Step 4: Clear the oscillator denominator
Substitute
\[
e=E-\frac{p^2}{2z},\qquad
f=F+\frac{q^2}{2z},\qquad
h=H+\frac{pq}{z}-\frac12
\]
into \(\Gamma\). Then
\[
D=2z\Gamma
\]
is the element
\[
D=2zcH+zt^2+4zEb+4zFa+4zxy-3zc+2cpq-2bp^2+2aq^2.
\]
Hence \(D\in R\), and since it is central in \(S\) while \(R\hookrightarrow S\), it is central in \(R\). Therefore
\[
k[z,A,B,D]\subseteq Z(R),
\]
and
\[
Z(S)=k[z^{\pm1},A,B,D].
\]

Step 5: Intersect the localized center back with \(R\)
Let \(u\in Z(R)\). Write
\[
u=z^{-m}P(z,A,B,D)
\]
with \(m\ge0\), \(P\in k[z,A,B,D]\), and \(P\) not divisible by \(z\) if \(m>0\). If \(m>0\), then
\[
P(z,A,B,D)=z^m u\in zR.
\]
Modulo \(z\), the three nontrivial generators have leading PBW symbols
\[
A_0=c^2+4ab,
\]
\[
B_0=tc+2xb+2ya,
\]
\[
D_0=2(cpq-bp^2+aq^2).
\]
They are algebraically independent: at
\[
(a,b,c,x,y,t,p,q)=(1,0,0,0,0,0,0,1)
\]
the differentials of \(A_0,B_0,D_0/2\) contain respectively the independent components
\[
4\,db,\qquad 2\,dy,\qquad da+2\,dq.
\]
Thus \(P(0,A_0,B_0,D_0)\neq0\), contradicting \(P(z,A,B,D)\in zR\). Hence \(m=0\), so every central element belongs to \(k[z,A,B,D]\).

Therefore
\[
Z(R)=k[z,A,B,D].
\]
Final Answer: $\boxed{k[z,c^2+4ab,tc+2xb+2ya,2zcH+zt^2+4zEb+4zFa+4zxy-3zc+2cpq-2bp^2+2aq^2]}$

---

## Answer

$k[z,c^2+4ab,tc+2xb+2ya,2zcH+zt^2+4zEb+4zFa+4zxy-3zc+2cpq-2bp^2+2aq^2]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- PBW localization
- oscillator shift
- truncated current algebras
- Poisson centers
- PBW symmetrization

---

## Black-Box Audit — no issues found
