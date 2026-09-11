## Steps

Step 1: Derive the three quadratic invariants from the current-algebra action
Let
$$
\mathfrak g=\mathfrak{sl}_2(k)\otimes_k k[\varepsilon]/(\varepsilon^3),
$$
and write
$$
e_i=e\otimes\varepsilon^i,\qquad f_i=f\otimes\varepsilon^i,\qquad h_i=h\otimes\varepsilon^i\qquad (i=0,1,2).
$$
Let $R=U(\mathfrak g)$ and let
$$
P=\operatorname{gr}R
 =k[e_0,f_0,h_0,e_1,f_1,h_1,e_2,f_2,h_2]
$$
with its PBW Poisson bracket.

The quadratic polynomial
$$
q(e,f,h)=h^2+4ef
$$
is $\mathfrak{sl}_2$-invariant. Indeed, for the three adjoint derivations one has
$$
D_e(q)=2h(-2e)+4e(h)=0,
$$
$$
D_f(q)=2h(2f)+4(-h)f=0,
$$
$$
D_h(q)=4(2e)f+4e(-2f)=0.
$$

The truncation forces a reversal of the current layers. Put, modulo $s^3$,
$$
E(s)=e_2+s e_1+s^2e_0,\qquad
F(s)=f_2+s f_1+s^2f_0,\qquad
H(s)=h_2+s h_1+s^2h_0.
$$
This is not an ad hoc choice: if $r\in\mathfrak{sl}_2$ and $D_{r_i}=\{r_i,-\}$, then the relation
$$
[r_i,u_j]=[r,u]_{i+j}
$$
(with the bracket zero for $i+j\ge 3$) gives
$$
D_{r_i}(E(s),F(s),H(s))
\equiv s^i D_r(E(s),F(s),H(s))\pmod{s^3}.
$$
Therefore the coefficients modulo $s^3$ of
$$
q(E(s),F(s),H(s))=H(s)^2+4E(s)F(s)
$$
are killed by every $D_{r_i}$.

Writing those coefficients with harmless factors removed gives
$$
A=h_2^2+4e_2f_2,
$$
$$
B=h_2h_1+2e_2f_1+2e_1f_2,
$$
$$
C=h_2h_0+\frac12 h_1^2+2e_2f_0+2e_1f_1+2e_0f_2.
$$
Hence $A,B,C\in Z_{\mathrm{Pois}}(P)$.

Step 2: Prove that the Poisson center is exactly $k[A,B,C]$
Localize at $e_2$ and write $P_*=P[e_2^{-1}]$. We compute the common kernel of the Hamiltonian derivations explicitly.

First consider the top layer. Since brackets of total current degree at least $3$ vanish, $D_{e_2},D_{h_2},D_{f_2}$ act nontrivially only on $e_0,f_0,h_0$, and
$$
D_{e_2}=h_2\partial_{f_0}-2e_2\partial_{h_0},
$$
$$
D_{h_2}=2e_2\partial_{e_0}-2f_2\partial_{f_0},
$$
$$
D_{f_2}=-\frac{f_2}{e_2}D_{e_2}-\frac{h_2}{2e_2}D_{h_2}.
$$
Set
$$
L=h_2h_0+2e_2f_0+2f_2e_0.
$$
Both $D_{e_2}$ and $D_{h_2}$ kill $L$. Since
$$
f_0=\frac{L-h_2h_0-2f_2e_0}{2e_2},
$$
replacing $f_0$ by $L$ is an invertible coordinate change in $P_*$. In the coordinates $(e_0,h_0,L)$,
$$
D_{e_2}=-2e_2\partial_{h_0},\qquad
D_{h_2}=2e_2\partial_{e_0}.
$$
Thus the common kernel of the three top-layer derivations is
$$
k[e_2^{\pm1},f_2,h_2,e_1,f_1,h_1,L].
$$
Because
$$
C=L+\frac12 h_1^2+2e_1f_1,
$$
we may use $C$ instead of $L$.

Now restrict $D_{e_1},D_{h_1},D_{f_1}$ to
$$
k[e_2^{\pm1},f_2,h_2,e_1,f_1,h_1,C].
$$
They fix $C$, and
$$
D_{e_1}=h_2\partial_{f_1}-2e_2\partial_{h_1},
$$
$$
D_{h_1}=2e_2\partial_{e_1}-2f_2\partial_{f_1},
$$
$$
D_{f_1}=-\frac{f_2}{e_2}D_{e_1}-\frac{h_2}{2e_2}D_{h_1}.
$$
Since
$$
f_1=\frac{B-h_2h_1-2f_2e_1}{2e_2},
$$
replacing $f_1$ by $B$ is again an invertible coordinate change. In coordinates $(e_1,h_1,B)$,
$$
D_{e_1}=-2e_2\partial_{h_1},\qquad
D_{h_1}=2e_2\partial_{e_1}.
$$
Hence the common kernel through current degree $1$ is
$$
k[e_2^{\pm1},f_2,h_2,B,C].
$$

Next apply $D_{e_0}$. On the remaining top-layer variables,
$$
D_{e_0}(e_2)=0,\qquad D_{e_0}(h_2)=-2e_2,\qquad D_{e_0}(f_2)=h_2,
$$
and $D_{e_0}$ fixes $B,C$. Since
$$
f_2=\frac{A-h_2^2}{4e_2},
$$
we can replace $f_2$ by $A$, after which
$$
D_{e_0}=-2e_2\partial_{h_2}.
$$
Its kernel is therefore
$$
k[e_2^{\pm1},A,B,C].
$$
Finally, $D_{h_0}$ fixes $A,B,C$ and satisfies $D_{h_0}(e_2)=2e_2$. Thus, on the Laurent polynomial ring above,
$$
D_{h_0}=2e_2\partial_{e_2},
$$
whose kernel is $k[A,B,C]$ because $\operatorname{char}k=0$. The remaining derivation $D_{f_0}$ also kills $A,B,C$. Hence
$$
Z_{\mathrm{Pois}}(P_*)=k[A,B,C].
$$
Every Poisson-central element of $P$ remains Poisson central after localization, while $A,B,C\in P$, so
$$
Z_{\mathrm{Pois}}(P)=k[A,B,C].
$$
The successive coordinate changes above also show that $A,B,C$ are algebraically independent.

Step 3: Lift the Poisson generators canonically to $Z(R)$
For a Lie algebra $\mathfrak g$, PBW symmetrization
$$
\operatorname{sym}:S(\mathfrak g)\longrightarrow U(\mathfrak g)
$$
is $\mathfrak g$-equivariant: for $r\in\mathfrak g$ and $F\in S(\mathfrak g)$,
$$
[r,\operatorname{sym}(F)]=\operatorname{sym}(D_rF).
$$
Indeed this identity follows on a monomial by expanding the commutator with each factor and averaging over all orders. Since $A,B,C$ are annihilated by every $D_r$, their symmetrizations are central.

For $A$ and $B$ no ordering correction occurs, because all products appearing in them involve current layers whose brackets vanish. Thus set
$$
Z_0=h_2^2+4e_2f_2,
$$
$$
Z_1=h_2h_1+2e_2f_1+2e_1f_2.
$$
For $C$, symmetrization gives
$$
Z_2=h_2h_0+\frac12 h_1^2
 +(e_2f_0+f_0e_2)
 +(e_1f_1+f_1e_1)
 +(e_0f_2+f_2e_0).
$$
Therefore
$$
k[Z_0,Z_1,Z_2]\subseteq Z(R).
$$
Their leading PBW symbols are respectively $A,B,C$.

Step 4: Prove that no further central elements exist
Let $u\in Z(R)$ have PBW degree $n$. Its leading symbol $\sigma(u)\in P$ is Poisson central, because for every $r\in\mathfrak g$ the equality $[r,u]=0$ implies $\{r,\sigma(u)\}=0$. By Step 2,
$$
\sigma(u)=F(A,B,C)
$$
for some polynomial $F\in k[X,Y,Z]$. Taking the homogeneous part of $F$ of the PBW degree of $\sigma(u)$, we may assume $F(A,B,C)$ is homogeneous of degree $n$.

The central element $F(Z_0,Z_1,Z_2)$ has the same leading symbol as $u$. Hence
$$
\deg_{\mathrm{PBW}}\bigl(u-F(Z_0,Z_1,Z_2)\bigr)<n.
$$
Induction on PBW degree, starting from degree $0$ where the center is $k$, shows that every central element belongs to $k[Z_0,Z_1,Z_2]$. Since the leading symbols $A,B,C$ are algebraically independent, so are $Z_0,Z_1,Z_2$.

Consequently
$$
Z(R)=k[Z_0,Z_1,Z_2].
$$

Final Answer: $\boxed{k[Z_0,Z_1,Z_2]}$, where
$$
Z_0=h_2^2+4e_2f_2,
$$
$$
Z_1=h_2h_1+2e_2f_1+2e_1f_2,
$$
$$
Z_2=h_2h_0+\frac12 h_1^2+(e_2f_0+f_0e_2)+(e_1f_1+f_1e_1)+(e_0f_2+f_2e_0).
$$

---

## Answer

$k[Z_0,Z_1,Z_2]$, with
$Z_0=h_2^2+4e_2f_2$,
$Z_1=h_2h_1+2e_2f_1+2e_1f_2$, and
$Z_2=h_2h_0+\frac12 h_1^2+(e_2f_0+f_0e_2)+(e_1f_1+f_1e_1)+(e_0f_2+f_2e_0)$.

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- PBW filtration and Poisson center
- invariant quadratic form of $\mathfrak{sl}_2$
- truncated current algebra
- localization and slice derivations
- PBW symmetrization

---

## Black-Box Audit — no issues found
