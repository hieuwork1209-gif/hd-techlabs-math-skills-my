## Steps

Step 1: Localize and split off the Heisenberg pair
Let \(\mathfrak g\) be the Lie algebra with the generators and brackets from the problem. Then \(R=U(\mathfrak g)\), and PBW implies that \(R\) is a domain. Since \(z\) is central and regular, form
\[
S=R[z^{-1}].
\]
Put
\[
e=E-\frac{p^2}{2z},\qquad
f=F+\frac{q^2}{2z},\qquad
h=H+\frac{pq}{z}-\frac12.
\]
Using \([p,q]=z\) and the displayed action on \(p,q\), one checks
\[
[e,p]=[e,q]=[f,p]=[f,q]=[h,p]=[h,q]=0
\]
and
\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h.
\]
The elements \(x,y,t\) commute with \(p,q,z\), so replacing \(E,F,H\) by \(e,f,h\) does not change their action on \(x,y,t\). Thus \(e,f,h,x,y,t\) generate over
\[
K=k[z^{\pm1}]
\]
the Takiff algebra \(\mathfrak l=\mathfrak{sl}_2\ltimes(\mathfrak{sl}_2)_{\mathrm{ab}}\), while \(p,q\) form a localized Weyl pair commuting with it.

Every element of \(S\) has a unique expansion
\[
\sum_{i,j\ge0}p^iq^j u_{ij},\qquad u_{ij}\in U_K(\mathfrak l).
\]
If it commutes with \(p\), then \([p,q^j]=jzq^{j-1}\) forces \(j=0\); commuting with \(q\) then forces \(i=0\). Hence
\[
Z(S)=Z\!\left(U_K(\mathfrak l)\right).
\]

Step 2: Compute the Takiff center
Inside \(U_K(\mathfrak l)\), define
\[
A=t^2+4xy,
\]
\[
B=th+2xf+2ye.
\]
A direct use of
\[
[h,x]=2x,\quad [h,y]=-2y,\quad [e,y]=t,\quad [e,t]=-2x,
\]
\[
[f,x]=-t,\quad [f,t]=2y
\]
shows that both \(A\) and \(B\) commute with \(e,f,h,x,y,t\). Thus \(K[A,B]\) lies in the center.

To prove exhaustion, pass to the PBW associated graded Poisson algebra
\[
Q=K[e,f,h,x,y,t].
\]
Localize further at \(x\). The Hamiltonian derivations of \(x\) and \(t\) on the variables \(e,f,h\) are
\[
D_x=t\,\partial_f-2x\,\partial_h,
\qquad
D_t=2x\,\partial_e-2y\,\partial_f.
\]
With
\[
C=2xf+th,
\]
the kernel of \(D_x\) is
\[
K[x^{\pm1},y,t,e,C].
\]
Since \(D_t(C)=-4xy\) and \(D_t(e)=2x\), the common kernel of \(D_x,D_t\) is
\[
K[x^{\pm1},y,t,B],
\qquad B=C+2ye.
\]
The derivation coming from \(y\) adds no condition because
\[
D_y=-\frac{y}{x}D_x-\frac{t}{2x}D_t.
\]
Now
\[
A=t^2+4xy,
\qquad
K[x^{\pm1},y,t,B]=K[x^{\pm1},t,A,B].
\]
On this ring, the Hamiltonian derivation of \(e\) is \(-2x\partial_t\), so its kernel is \(K[x^{\pm1},A,B]\). The derivation of \(h\) is then \(2x\partial_x\), whose kernel is exactly \(K[A,B]\). Since \(A,B\) are also \(f\)-invariant,
\[
Z_{\mathrm{Pois}}(Q)=K[A,B].
\]
Therefore the leading symbol of every central element of \(U_K(\mathfrak l)\) is a polynomial in the leading symbols of \(A,B\). Subtracting the corresponding polynomial in the central elements \(A,B\) lowers PBW degree, so induction gives
\[
Z\!\left(U_K(\mathfrak l)\right)=K[A,B].
\]
Consequently
\[
Z(S)=k[z^{\pm1},A,B].
\]

Step 3: Produce central generators already lying in \(R\)
Substituting the oscillator shift into \(B\) gives
\[
B=t\left(H+\frac{pq}{z}-\frac12\right)
+2x\left(F+\frac{q^2}{2z}\right)
+2y\left(E-\frac{p^2}{2z}\right).
\]
Hence
\[
D=2zB
=2ztH-zt+4zxF+4zyE+2tpq+2xq^2-2yp^2
\]
belongs to \(R\). Since \(A\) and \(D\) are central after localization and \(R\hookrightarrow S\), they are central in \(R\). Thus
\[
k[z,A,D]\subseteq Z(R),
\]
and, because \(B=D/(2z)\),
\[
Z(S)=k[z^{\pm1},A,D].
\]

Step 4: Intersect the localized center back with \(R\)
Let \(c\in Z(R)\). Write
\[
c=z^{-m}P(z,A,D)
\]
with \(m\ge0\), \(P\in k[z,A,D]\), and \(P\) not divisible by \(z\) if \(m>0\). If \(m>0\), then
\[
P(z,A,D)=z^m c\in zR.
\]
Modulo \(z\), the two generators become
\[
A_0=t^2+4xy,
\qquad
D_0=2(tpq+xq^2-yp^2),
\]
which lie in the polynomial subalgebra \(k[p,q,x,y,t]\subset R/(z)\). They are algebraically independent: at
\[
(x,y,t,p,q)=(1,0,0,0,1),
\]
the differentials satisfy
\[
dA_0=4\,dy,
\qquad
d(D_0/2)=dx+2\,dq,
\]
so they are linearly independent. Therefore
\[
P(0,A_0,D_0)\neq0,
\]
contradicting \(P(z,A,D)\in zR\). Hence \(m=0\), and every central element lies in \(k[z,A,D]\).

Thus
\[
Z(R)=k[z,A,D].
\]
Final Answer: $\boxed{k[z,t^2+4xy,2ztH-zt+4zxF+4zyE+2tpq+2xq^2-2yp^2]}$

---

## Answer

$k[z,t^2+4xy,2ztH-zt+4zxF+4zyE+2tpq+2xq^2-2yp^2]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- PBW localization
- oscillator shift
- Takiff algebras
- Poisson centers
- center intersection

---

## Black-Box Audit — no issues found
