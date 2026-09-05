## Steps

Step 1: Reveal the hidden triangular coordinates
Put
$$
q=b+a^2,
\qquad
r=c+ab.
$$
Since
$$
b=q-a^2,
\qquad
c=r-aq+a^3,
$$
we have
$$
k[a,b,c]=k[a,q,r].
$$
Now define
$$
P=X+aY,
\qquad
Q=Y+qZ,
\qquad
S=Z.
$$
The change is invertible because
$$
Z=S,
\qquad
Y=Q-qS,
\qquad
X=P-aQ+aqS.
$$
Using the defining relations,
$$
[P,u]=a,
\qquad
[Q,u]=q,
\qquad
[S,u]=r.
$$
Moreover $P,Q,S$ commute pairwise and commute with $a,q,r$. Thus $R$ has PBW normal form over $k[a,q,r,u]$ in the commuting skew variables $P,Q,S$.

Step 2: Reduce centrality to one nonfree invariant ring
Let $z\in Z(R)$. Since $P$ commutes with $q,r,P,Q,S$ and satisfies $[P,u]=a$, commutation with $P$ gives
$$
[P,z]=a\,\partial_u z=0.
$$
The algebra is a domain and has characteristic zero, so $z$ is independent of $u$. Hence
$$
z\in B:=k[a,q,r,P,Q,S].
$$
Commutation with $u$ is now equivalent to
$$
D(z)=0,
$$
where
$$
D=a\partial_P+q\partial_Q+r\partial_S.
$$
Conversely, every element of $\ker D\subseteq B$ commutes with $u,P,Q,S,a,q,r$. Therefore
$$
Z(R)=\ker D.
$$

Step 3: Compute the kernel and its saturation
Set
$$
U=qP-aQ,
\qquad
V=rP-aS,
\qquad
W=rQ-qS.
$$
Then
$$
D(U)=D(V)=D(W)=0,
$$
and
$$
aW=qV-rU.
$$
Thus
$$
C:=k[a,q,r,U,V,W]\subseteq\ker D.
$$

Localize at $a$. Since
$$
D\left(\frac Pa\right)=1,
$$
and
$$
Q=\frac{qP-U}{a},
\qquad
S=\frac{rP-V}{a},
$$
we get
$$
(\ker D)_a=k[a,a^{-1},q,r,U,V].
$$
It remains to intersect back with $B$. Let
$$
f=a^{-N}F(a,q,r,U,V)\in B
$$
with $N\ge0$ minimal. If $N>0$, reducing the numerator modulo $a$ gives
$$
F(0,q,r,qP,rP)=0.
$$
Consider
$$
\phi:k[q,r,U,V]\longrightarrow k[q,r,P],
\qquad
U\mapsto qP,
\quad
V\mapsto rP.
$$
We claim
$$
\ker\phi=(rU-qV).
$$
The polynomial $rU-qV$ is primitive and linear in $V$ over the UFD $k[q,r,U]$, hence irreducible and therefore prime in $k[q,r,U,V]$. After localizing at $q$, the equation $rU-qV=0$ gives
$$
V=\frac rqU,
$$
so the localized kernel is exactly $(rU-qV)_q$. Thus if $G\in\ker\phi$, some power $q^mG$ lies in $(rU-qV)$. Since this prime ideal does not contain $q$, it follows that $G\in(rU-qV)$, proving the claim.

Hence
$$
F(0,q,r,U,V)=(rU-qV)G_0.
$$
But
$$
rU-qV=-aW.
$$
Lifting $G_0$ therefore lowers the negative power of $a$, contradicting minimality. Thus $N=0$, so
$$
\ker D=C=k[a,q,r,U,V,W].
$$

Step 4: Return to the original generators
Substituting
$$
q=b+a^2,
\qquad
r=c+ab,
$$
and the definitions of $P,Q,S$ gives
$$
U=qX+a(q-1)Y-aqZ,
$$
$$
V=rX+arY-aZ,
$$
$$
W=rY+q(r-1)Z.
$$
Because $k[a,q,r]=k[a,b,c]$, we conclude
$$
Z(R)=k[a,b,c,U,V,W].
$$
Final Answer: $\boxed{k[a,b,c,qX+a(q-1)Y-aqZ,rX+arY-aZ,rY+q(r-1)Z]}$

---

## Answer

$k[a,b,c,qX+a(q-1)Y-aqZ,rX+arY-aZ,rY+q(r-1)Z]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- differential Ore extensions
- nonfree syzygy modules
- locally nilpotent derivations
- saturation of invariant rings
- PBW normal forms

---

## Black-Box Audit — no issues found
