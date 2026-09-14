## Steps

Step 1: Construct the two elliptic quotients and a two-primary isogeny
Let
$$
f(x)=x^6-x^4+x^3-x^2+1.
$$
Since $x^6f(x^{-1})=f(x)$, the curve has the involution
$$
\sigma:(x,y)\longmapsto\left(x^{-1},\frac{y}{x^3}\right).
$$
Let $\iota(x,y)=(x,-y)$ and $\tau=\iota\sigma$. Put
$$
u=x+x^{-1},\qquad v=\frac{y(x+1)}{x^2},\qquad w=\frac{y(x-1)}{x^2}.
$$
Then $u,v$ are $\sigma$-invariant and $u,w$ are $\tau$-invariant. In $\mathbb F_5$,
$$
\frac{f(x)}{x^3}=x^3+x^{-3}-(x+x^{-1})+1=u^3+u+1,
$$
while
$$
\frac{(x+1)^2}{x}=u+2,\qquad \frac{(x-1)^2}{x}=u-2.
$$
Hence the quotient curves are
$$
E_+:v^2=(u+2)(u^3+u+1),\qquad
E_-:w^2=(u-2)(u^3+u+1).
$$
Let $\pi_+:C\to E_+$ and $\pi_-:C\to E_-$ be the quotient maps. Their pullbacks define
$$
\Phi:E_+\times E_-\longrightarrow J,
\qquad
(P,Q)\longmapsto \pi_+^*P+\pi_-^*Q,
$$
and the norm maps define
$$
\Psi:J\longrightarrow E_+\times E_-,
\qquad
D\longmapsto(\pi_{+*}D,\pi_{-*}D).
$$
For a degree-two quotient, $\pi_{\pm *}\pi_\pm^*=[2]$. The cross maps vanish. For example, since $\pi_+\sigma=\pi_+$, while $\tau=\iota\sigma$ fixes the $E_-$ pullback and $\iota$ acts as $[-1]$ on $J$, one has $\sigma\pi_-^*=-\pi_-^*$. Thus
$$
\pi_{+*}\pi_-^*=\pi_{+*}\sigma\pi_-^*=-\pi_{+*}\pi_-^*.
$$
Its image is both connected and contained in the finite group $E_+[2]$, so the cross map is zero; similarly $\pi_{-*}\pi_+^*=0$. Therefore
$$
\Psi\Phi=([2],[2]).
$$
Consequently $\Phi$ is an isogeny and $\deg\Phi$ is a power of $2$ dividing $16$.

Step 2: Find the Frobenius traces of the two quotient curves
Both quartics have leading coefficient $1$, so their smooth projective models have two $\mathbb F_5$-rational points at infinity. For $E_+$, the right-hand side at $u=0,1,2,3,4$ is
$$
2,4,4,0,4.
$$
The corresponding affine fiber sizes are $0,2,2,1,2$, so
$$
\#E_+(\mathbb F_5)=9,
\qquad t_+=5+1-9=-3.
$$
For $E_-$, the right-hand side values are
$$
3,2,0,1,3,
$$
with affine fiber sizes $0,0,1,2,0$. Hence
$$
\#E_-(\mathbb F_5)=5,
\qquad t_-=5+1-5=1.
$$
Thus the Frobenius eigenvalue pairs on $E_+$ and $E_-$ have sums $-3$ and $1$, respectively, and product $5$ in each case.

Step 3: Compute the two group orders over the seventeenth extension
For a Frobenius pair $\alpha,\beta$ with $\alpha+\beta=t$ and $\alpha\beta=5$, write
$$
S_n(t)=\alpha^n+\beta^n.
$$
Besides $S_1=t$ and $S_2=t^2-10$, multiplication of the two power sums gives
$$
S_{2m}=S_m^2-2\cdot5^m,
\qquad
S_{2m+1}=S_mS_{m+1}-5^m t.
$$
For $t=-3$,
$$
S_2=-1,\quad S_3=18,\quad S_4=-49,\quad S_5=57,
$$
so successive doubling gives
$$
S_8=1151,\quad S_9=-918,\quad S_{16}=543551,
$$
and
$$
S_{17}=1151(-918)-5^8(-3)=115257.
$$
For $t=1$,
$$
S_2=-9,\quad S_3=-14,\quad S_4=31,\quad S_5=101,
$$
then
$$
S_8=-289,\quad S_9=2506,\quad S_{16}=-697729,
$$
and
$$
S_{17}=(-289)(2506)-5^8=-1114859.
$$
Set $Q=5^{17}=762939453125$. Therefore
$$
N_+:=\#E_+(\mathbb F_Q)=Q+1-115257=762939337869,
$$
$$
N_-:=\#E_-(\mathbb F_Q)=Q+1+1114859=762940567985.
$$

Step 4: Prove that both elliptic rational-point groups are cyclic
For an elliptic curve over $\mathbb F_Q$, write its finite rational-point group as
$$
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z,
\qquad m\mid n.
$$
Then $m^2$ divides the group order. Here $5\nmid N_+$ and $25\nmid N_-$, so $5\nmid m$ in either case. The full $m$-torsion is rational, and the Weil pairing therefore gives $m\mid Q-1$.

It remains to show that $N_+$ and $N_-$ are each coprime to $Q-1$. Since
$$
N_+-(Q-1)=-115255,
\qquad
N_--(Q-1)=1114861,
$$
the following Bezout identities certify the two gcds:
$$
37104(Q-1)-245612819129(115255)=1,
$$
$$
151927(Q-1)-103969106727(1114861)=1.
$$
Hence $m=1$ for both curves, so
$$
E_+(\mathbb F_Q)\cong\mathbb Z/N_+\mathbb Z,
\qquad
E_-(\mathbb F_Q)\cong\mathbb Z/N_-\mathbb Z.
$$

Step 5: Transfer the group structure through the isogeny and put it in invariant-factor form
The two integers $N_+$ and $N_-$ are odd. Since the kernel of $\Phi$ has two-power order, the induced map
$$
\Phi:E_+(\mathbb F_Q)\times E_-(\mathbb F_Q)\longrightarrow J(\mathbb F_Q)
$$
has trivial kernel. Isogenous abelian varieties over a finite field have the same Frobenius polynomial and therefore the same number of rational points over every finite extension. Thus the source and target above have the same finite cardinality, so $\Phi$ is an isomorphism on $\mathbb F_Q$-points.

Finally,
$$
-208985688411N_+ + 208985351456N_-=1,
$$
so $\gcd(N_+,N_-)=1$. The direct product of the two cyclic groups is therefore cyclic, of order
$$
N_+N_-=762939337869\cdot762940567985
=582077371771874679523965.
$$
Hence the invariant-factor decomposition has a single factor.

Final Answer: $\boxed{\mathbb{Z}/582077371771874679523965\mathbb{Z}}$

---

## Answer

$\mathbb{Z}/582077371771874679523965\mathbb{Z}$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- elliptic quotients of genus-two curves
- Jacobian isogenies
- Frobenius trace recurrences
- elliptic curve group structure
- Weil pairing
