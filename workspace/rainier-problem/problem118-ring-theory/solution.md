## Steps

Step 1: Derive the oscillator shift and isolate the current algebra
Let $\mathfrak g$ be the Lie algebra defined by the displayed relations, so $R=U(\mathfrak g)$. PBW implies that $R$ is a domain. Since $z$ is central and regular, set
$$
S=R[z^{-1}],\qquad K=k[z^{\pm 1}].
$$
Because $[p,q]=z$ with $z$ invertible, $p,q$ form a Weyl pair over $K$. To separate this Weyl factor, seek corrected elements commuting with $p,q$.

For $e=E-\alpha$, the equations $[e,p]=[e,q]=0$ require
$$
[\alpha,p]=0,\qquad [\alpha,q]=p.
$$
Since $[p^2,q]=2zp$, take $\alpha=p^2/(2z)$. Then
$$
[e,p]=0,\qquad [e,q]=p-\frac{[p^2,q]}{2z}=0.
$$
For $f=F-\beta$, the equations become $[\beta,p]=q$, $[\beta,q]=0$. Since $[q^2,p]=-2zq$, take $\beta=-q^2/(2z)$, giving
$$
[f,p]=q+\frac{[q^2,p]}{2z}=0,\qquad [f,q]=0.
$$
For $H$, put $h_0=H+pq/z$. Using $[pq,p]=-zp$ and $[pq,q]=zq$,
$$
[h_0,p]=p- p=0,\qquad [h_0,q]=-q+q=0.
$$
The scalar correction is fixed by the bracket of $e$ and $f$. Since
$$
[e,f]
=H+\frac{pq+qp}{2z}
=H+\frac{pq}{z}-\frac{1}{2},
$$
where $qp=pq-z$, define
$$
h=[e,f]=H+\frac{pq}{z}-\frac{1}{2}.
$$
Thus $e,f,h$ commute with $p,q$. Moreover,
$$
\begin{aligned}
[h,e]
&=2E-\frac{[H,p^2]}{2z}+\frac{[pq,E]}{z}-\frac{[pq,p^2]}{2z^2}\\
&=2E-\frac{p^2}{z}-\frac{p^2}{z}+\frac{p^2}{z}=2e,
\end{aligned}
$$
and similarly
$$
\begin{aligned}
[h,f]
&=-2F+\frac{[H,q^2]}{2z}+\frac{[pq,F]}{z}+\frac{[pq,q^2]}{2z^2}\\
&=-2F-\frac{q^2}{z}-\frac{q^2}{z}+\frac{q^2}{z}=-2f.
\end{aligned}
$$
Hence $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$.

The correction terms involve only $p,q,z$, so they have zero brackets with $x,y,t,a,b,c$. The displayed relations therefore identify
$$
(e,f,h),\qquad (x,y,t)=\varepsilon(e,f,h),\qquad (a,b,c)=\varepsilon^2(e,f,h)
$$
with $\mathfrak l=\mathfrak{sl}_2[\varepsilon]/(\varepsilon^3)$ over $K$.

For the needed uniqueness, choose the PBW order $p,q,E,F,H,x,y,t,a,b,c$ after localization, with $z$ absorbed into $K$, and filter by the number of factors among $E,F,H,x,y,t,a,b,c$, assigning $p,q$ degree $0$. The inverse substitutions
$$
E=e+\frac{p^2}{2z},\qquad F=f-\frac{q^2}{2z},\qquad H=h-\frac{pq}{z}+\frac{1}{2}
$$
are triangular for this filtration: replacing $E,F,H$ by $e,f,h$ changes an ordered PBW monomial only by terms of strictly smaller filtered degree, while its leading term has coefficient $1$. Hence the transition from the ordinary PBW monomials to
$$
p^iq^je^rf^sh^m x^\alpha y^\beta t^\gamma a^\mu b^\nu c^\rho
$$
is unitriangular and therefore invertible. These shifted monomials are thus a $K$-basis of $S$.

Consequently every element of $S$ has a unique expansion
$$
s=\sum_{i,j\geq 0}p^iq^ju_{ij},\qquad u_{ij}\in U_K(\mathfrak l).
$$
If $s$ commutes with $p$, then $[p,q^j]=jzq^{j-1}$ and PBW independence force $u_{ij}=0$ for every $j>0$. Thus $s=\sum_i p^iu_i$. If $s$ also commutes with $q$, then $[q,p^i]=-izp^{i-1}$ forces $u_i=0$ for every $i>0$. Therefore a central element of $S$ lies in $U_K(\mathfrak l)$, and it is central there. The converse is immediate because $U_K(\mathfrak l)$ commutes with $p,q$. Hence
$$
Z(S)=Z\!\left(U_K(\mathfrak l)\right).
$$

Step 2: Compute the Poisson center of the third-order current algebra
Pass to the PBW associated graded Poisson algebra
$$
Q=K[e,f,h,x,y,t,a,b,c].
$$
Define
$$
A=c^2+4ab,\qquad B=tc+2xb+2ya,
$$
$$
C=ch+\frac{1}{2}t^2+2be+2af+2xy.
$$
The potentially nonzero Poisson brackets cancel explicitly. For $A$,
$$
\{e,A\}=-4ac+4ac=0,\qquad
\{f,A\}=4bc-4bc=0,\qquad
\{h,A\}=0.
$$
Its brackets with $x,y,t,a,b,c$ vanish because current-layer degrees add to at least $3$. For $B$,
$$
\begin{aligned}
\{e,B\}&=-2xc-2at+2xc+2at=0,\\
\{f,B\}&=2yc+2bt-2bt-2yc=0,\\
\{h,B\}&=0,\\
\{x,B\}&=-2ac+2ac=0,\\
\{y,B\}&=2bc-2bc=0,\\
\{t,B\}&=4ab-4ab=0.
\end{aligned}
$$
Its brackets with $a,b,c$ vanish by layer degree. For $C$,
$$
\begin{aligned}
\{e,C\}&=(-2ah-2ce)-2xt+2ce+2ah+2xt=0,\\
\{f,C\}&=(2bh+2cf)+2yt-2bh-2cf-2yt=0,\\
\{h,C\}&=0,\\
\{x,C\}&=-2cx-2at+2at+2cx=0,\\
\{y,C\}&=2cy+2bt-2bt-2cy=0,\\
\{t,C\}&=4bx-4ay+4ay-4bx=0,\\
\{a,C\}&=-2ac+2ac=0,\\
\{b,C\}&=2bc-2bc=0,\\
\{c,C\}&=4ab-4ab=0.
\end{aligned}
$$
Thus $A,B,C$ are Poisson central.

To prove exhaustion, localize at $a$. Let $D_r=\{r,-\}$. On $e,f,h$,
$$
D_a=c\partial_f-2a\partial_h,\qquad
D_c=2a\partial_e-2b\partial_f,
$$
and
$$
D_b=-\frac{b}{a}D_a-\frac{c}{2a}D_c.
$$
Set $L=ch+2af+2be$. Since $a$ is invertible,
$$
f=\frac{L-ch-2be}{2a},
$$
so $(e,h,L)$ are coordinates in place of $(e,f,h)$. In these coordinates $D_a(L)=D_c(L)=0$, $D_a=-2a\partial_h$, and $D_c=2a\partial_e$. Hence the common kernel of $D_a,D_b,D_c$ is
$$
K[a^{\pm 1},b,c,x,y,t,L].
$$
Replace $L$ by $C=L+t^2/2+2xy$. The derivations $D_x,D_t,D_y$ fix $C$, and
$$
D_x=c\partial_y-2a\partial_t,\qquad
D_t=2a\partial_x-2b\partial_y,\qquad
D_y=-\frac{b}{a}D_x-\frac{c}{2a}D_t.
$$
Since $B=tc+2xb+2ya$ and $a$ is invertible,
$$
y=\frac{B-tc-2xb}{2a}.
$$
Thus $(x,t,B)$ replace $(x,y,t)$, with $D_x=-2a\partial_t$ and $D_t=2a\partial_x$. Their common kernel is
$$
K[a^{\pm 1},b,c,B,C].
$$
Finally, $D_e(c)=-2a$, $D_e(a)=0$, and $D_e(A)=0$. Since $b=(A-c^2)/(4a)$, the kernel of $D_e$ is $K[a^{\pm 1},A,B,C]$. On this ring $D_h=2a\partial_a$, so imposing $h$-invariance leaves $K[A,B,C]$. These generators are already $f$-invariant, so
$$
Z_{\mathrm{Pois}}(Q[a^{-1}])=K[A,B,C].
$$
Because $A,B,C\in Q$, any Poisson-central element of $Q$ lies in this same polynomial ring. Therefore
$$
Z_{\mathrm{Pois}}(Q)=K[A,B,C].
$$

Step 3: Lift the Poisson generators to the enveloping center
For Lie generators $r,u,v$,
$$
\left[r,\frac{uv+vu}{2}\right]
=\frac{[r,u]v+u[r,v]+[r,v]u+v[r,u]}{2},
$$
which is the symmetrization of the Poisson derivation of $uv$. Hence the symmetrization of any quadratic Poisson invariant commutes with every generator.

The elements $A$ and $B$ need no ordering correction. For $C$,
$$
\operatorname{sym}(C)
=ch+\frac{1}{2}t^2+(be+eb)+(af+fa)+(xy+yx).
$$
Using $[e,b]=c$, $[f,a]=-c$, and $[x,y]=c$ gives
$$
\Gamma=ch+\frac{1}{2}t^2+2eb+2fa+2xy-c.
$$
Thus $A,B,\Gamma$ are central in $U_K(\mathfrak l)$ and have leading PBW symbols $A,B,C$.

Now let $u$ be central of PBW degree $n$. Its leading symbol $\sigma(u)$ is Poisson central, so by Step 2
$$
\sigma(u)=P(A,B,C)
$$
for a homogeneous polynomial $P$. The central element $P(A,B,\Gamma)$ has the same leading symbol, hence
$$
\deg\bigl(u-P(A,B,\Gamma)\bigr)<n.
$$
Induction on $n$, starting from degree $0$ where the center is $K$, expresses every central element as a polynomial in $A,B,\Gamma$. Therefore
$$
Z\!\left(U_K(\mathfrak l)\right)=K[A,B,\Gamma],
$$
and hence
$$
Z(S)=k[z^{\pm 1},A,B,\Gamma].
$$

Step 4: Clear the oscillator denominator
Substitute
$$
e=E-\frac{p^2}{2z},\qquad
f=F+\frac{q^2}{2z},\qquad
h=H+\frac{pq}{z}-\frac{1}{2}
$$
into $\Gamma$. Then $D=2z\Gamma$ is
$$
D=2zcH+zt^2+4zEb+4zFa+4zxy-3zc+2cpq-2bp^2+2aq^2.
$$
Hence $D\in R$ and is central. Therefore
$$
k[z,A,B,D]\subseteq Z(R),\qquad Z(S)=k[z^{\pm 1},A,B,D].
$$

Step 5: Intersect the localized center back with $R$
Let $u\in Z(R)$. Write
$$
u=z^{-m}P(z,A,B,D)
$$
with $m\geq 0$, $P\in k[z,A,B,D]$, and $P$ not divisible by $z$ if $m>0$. If $m>0$, then $P(z,A,B,D)\in zR$.

Modulo $z$, the leading PBW symbols of the three nontrivial generators are
$$
A_0=c^2+4ab,\qquad B_0=tc+2xb+2ya,\qquad D_0=2(cpq-bp^2+aq^2).
$$
At $(a,b,c,x,y,t,p,q)=(1,0,0,0,0,0,0,1)$,
$$
dA_0=4\,db,\qquad dB_0=2\,dy,\qquad d(D_0/2)=da+2\,dq,
$$
so $A_0,B_0,D_0$ are algebraically independent. Therefore $P(0,A_0,B_0,D_0)\neq 0$, contradicting divisibility by $z$. Hence $m=0$ and every central element lies in $k[z,A,B,D]$.

Thus
$$
Z(R)=k[z,A,B,D].
$$
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
