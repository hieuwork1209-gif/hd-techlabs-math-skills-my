## Steps

Step 1: Identify the two Kan-norm maps
Let $k=\mathbb F_p$, let $G=C_{p^2}=\langle g\rangle$, and let $H=\langle g^p\rangle\cong C_p$. For a finite group $Q$ and a functor $M:BQ\to\operatorname{Vect}_k$, left and right Kan extension along $BQ\to *$ are
$$
M_Q=M/\langle qm-m:q\in Q,m\in M\rangle,
\qquad
M^Q=\{m:qm=m\text{ for all }q\in Q\}.
$$
The norm comparison is
$$
\mathsf N_Q:M_Q\to M^Q,
\qquad
[m]\longmapsto\sum_{q\in Q}qm.
$$

Fix a functor $F:BG\to\operatorname{Vect}_k$ with $F(*)=V$, $\dim V=N$, and write the action of $g$ as $A$. Since
$$
A^{p^2}=I
$$
and over $k$
$$
x^{p^2}-1=(x-1)^{p^2},
$$
we may write
$$
A=I+T,
\qquad
T^{p^2}=0.
$$
Thus $T$ has a Jordan type $\lambda$ whose parts are at most $p^2$, and conversely every such nilpotent $T$ gives a functor.

For $G$, the norm operator on $V$ is
$$
I+A+\cdots+A^{p^2-1}=T^{p^2-1}.
$$
Indeed
$$
(A-I)(I+A+\cdots+A^{p^2-1})=A^{p^2}-I=T^{p^2},
$$
and the polynomial identity in characteristic $p$ gives the displayed equality. On a Jordan block of size $s\le p^2$, the rank of $T^{p^2-1}$ is $1$ if $s=p^2$ and $0$ otherwise. Hence
$$
\alpha(F)=\operatorname{rank}\mathsf N_G
$$
is exactly the number of parts of $\lambda$ equal to $p^2$.

Step 2: Optimize the $G$-norm rank
Put
$$
R=p(p-1)+r,
\qquad
N=ap^2+R,
$$
where $1\le r\le p-1$. Then
$$
0<R<p^2.
$$
Therefore a partition of $N$ with all parts at most $p^2$ contains at most $a$ parts equal to $p^2$. Thus
$$
\alpha(F)\le a.
$$
Equality holds exactly when
$$
\lambda=(p^2,\ldots,p^2)\sqcup\mu,
$$
with $a$ copies of $p^2$ and with $\mu$ a partition of $R$.

Hence the first lexicographic maximum is
$$
A=a.
$$

Step 3: Compute and optimize the $H$-norm rank
On restriction to $H$, the generator $g^p$ acts as
$$
A^p=(I+T)^p=I+T^p.
$$
Therefore the $H$-norm operator is
$$
I+A^p+A^{2p}+\cdots+A^{(p-1)p}
=(T^p)^{p-1}=T^{p(p-1)}.
$$
Set
$$
Q=p(p-1).
$$
On a Jordan block of size $s$, this operator has rank
$$
(s-Q)_+=\max\{s-Q,0\}.
$$
In particular a block of size $p^2$ contributes $p$.

Inside the equality class $\alpha(F)=a$, write the residual partition as
$$
\mu=(s_1,\ldots,s_t),
\qquad
\sum_i s_i=R=Q+r.
$$
Then
$$
\beta(F)=ap+\sum_i(s_i-Q)_+.
$$
Because $R<2Q$ for odd $p$, at most one part can exceed $Q$. If no part exceeds $Q$, the residual contribution is $0$. If exactly one part $s_j$ exceeds $Q$, then
$$
\sum_i(s_i-Q)_+=s_j-Q\le R-Q=r.
$$
Equality requires $s_j=R$, so there are no other residual parts. Thus the second lexicographic maximum is
$$
B=ap+r,
$$
and it is attained for one and only one Jordan type,
$$
\lambda_*=(p^2)^a\sqcup(R).
$$

Step 4: Reduce the count to one unipotent conjugacy class
Two functors with the fixed object value $V$ are distinct here whenever the corresponding matrices $A$ are distinct, even if they are naturally isomorphic. Since every maximizing functor has Jordan type $\lambda_*$, all maximizing generator actions form one conjugacy class in $GL_N(k)$.

Let
$$
\Gamma_j(p)=|GL_j(\mathbb F_p)|.
$$
Then
$$
K=\frac{\Gamma_N(p)}{|C_{GL_N(k)}(A)|}.
$$
It remains to compute the centralizer.

Step 5: Compute the centralizer self-containedly
View $V$ as a $k[t]$-module with $t$ acting by $T$. For the maximizing type,
$$
V\cong U_{p^2}^{\oplus a}\oplus U_R,
\qquad
U_s=k[t]/(t^s).
$$
Since
$$
\dim_k\operatorname{Hom}_{k[t]}(U_s,U_t)=\min\{s,t\},
$$
the endomorphism algebra
$$
E=\operatorname{End}_{k[t]}(V)
$$
has dimension
$$
S=a^2p^2+(2a+1)R.
$$

The two indecomposable summand types $U_{p^2}$ and $U_R$ are nonisomorphic. Modulo the Jacobson radical, endomorphisms retain only the induced scalar maps on their simple tops, so
$$
E/\operatorname{rad}E\cong M_a(k)\times k.
$$
Hence
$$
\dim_k\operatorname{rad}E=S-a^2-1.
$$
An endomorphism is invertible exactly when its image in the semisimple quotient is invertible. Therefore
$$
|E^\times|
=p^{S-a^2-1}\,\Gamma_a(p)\,(p-1).
$$
But $E^\times$ is exactly the centralizer of $A=I+T$ in $GL_N(k)$. Consequently
$$
K=
\frac{\Gamma_N(p)}
{p^{a^2p^2+(2a+1)R-a^2-1}\Gamma_a(p)(p-1)}.
$$

Final Answer: $\boxed{\left(a,ap+r,\frac{\Gamma_N(p)}{p^{a^2p^2+(2a+1)R-a^2-1}\Gamma_a(p)(p-1)}\right)}$

---

## Answer

$\left(a,ap+r,\frac{\Gamma_N(p)}{p^{a^2p^2+(2a+1)R-a^2-1}\Gamma_a(p)(p-1)}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- left and right Kan extensions
- norm maps from coinvariants to invariants
- restriction along subgroup inclusions
- unipotent Jordan types
- centralizers of finite-length modules
