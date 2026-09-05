## Steps

Step 1: Pass to the local cyclic-invariant quotient
Let
$$
R=\mathbb F_p[X,Y,Z]/(X^n-1,Y^n-1,Z^n-1),
$$
where multiplication by $X,Y,Z$ represents $T_1,T_2,T_3$. Sending $f$ to the functional
$$
\lambda_f(X^xY^yZ^z)=f(x,y,z)
$$
identifies the simultaneous kernel with the dual of the quotient by the operator polynomials. The cycle
$$
\rho:(X,Y,Z)\mapsto(Y,Z,X)
$$
preserves that quotient. Since $p\ne3$, Reynolds averaging makes taking $\langle\rho\rangle$-invariants exact, and the invariant subspace of the dual has the same dimension as the invariant subspace of the quotient.

Put
$$
a=X-1,\qquad b=Y-1,\qquad c=Z-1.
$$
Because $n$ is a power of $p$,
$$
X^n-1=a^n,\qquad Y^n-1=b^n,\qquad Z^n-1=c^n.
$$
The first operator equation becomes $a+b+c=0$. We temporarily omit the truncation $a^n=b^n=c^n=0$ and restore it in Step 5.

On the plane $a+b+c=0$, define
$$
s=ab+bc+ca,\qquad t=abc,\qquad \Delta=(a-b)(b-c)(c-a).
$$
Every polynomial fixed by the cycle splits uniquely into a symmetric part plus $\Delta$ times a symmetric part. Thus the cyclic invariant ring is
$$
E=\mathbb F_p[s,t,\Delta]_{(s,t,\Delta)}\Big/(\Delta^2+4s^3+27t^2).
$$

Step 2: Identify the mixed-scale generators
Define
$$
D=(T_1-I)(T_2-I)+(T_2-I)(T_3-I)+(T_3-I)(T_1-I).
$$
In the quotient by $a+b+c=0$, multiplication by $D$ is multiplication by $s$.

Let $q=n/p$. Since $q$ is a power of $p$,
$$
X^q=1+a^q,\qquad Y^q=1+b^q,\qquad Z^q=1+c^q,
$$
and $a^q+b^q+c^q=0$. Expanding the operators gives
$$
A=s^q,\qquad B=t^q,\qquad C=\Delta^q.
$$
Hence
$$
D^{q-1}A^2=s^{q-1}s^{2q}=s^{3q-1}.
$$
Therefore the untruncated cyclic-invariant quotient is
$$
Q=E/(s^{3q-1},t^q,\Delta^q).
$$
This is the load-bearing mixed-scale step: the first exponent is not a pure Frobenius multiple of $q$.

Step 3: Convert the surface singularity to $uv=w^3$
Extend scalars to a field $K/\mathbb F_p$ of degree at most $2$ containing an element $\alpha$ with
$$
\alpha^2=-27.
$$
Scalar extension does not change vector-space dimension. Set
$$
u=\Delta+\alpha t,\qquad
v=-\frac14(\Delta-\alpha t),\qquad
w=s.
$$
Then
$$
uv=-\frac14(\Delta^2+27t^2)=s^3=w^3.
$$
Because $q$ is a $p$-power, $u^q,v^q$ are invertible $K$-linear combinations of $\Delta^q,t^q$. Thus
$$
Q\otimes_{\mathbb F_p}K
\cong
\frac{K[u,v,w]}{(uv-w^3,u^q,v^q,w^{3q-1})}.
$$

Step 4: Count the surviving semigroup monomials
The ring
$$
K[u,v,w]/(uv-w^3)
$$
embeds into $K[\xi,\eta]$ by
$$
u=\xi^3,\qquad v=\eta^3,\qquad w=\xi\eta.
$$
Hence every monomial has a unique normal form of one of the types
$$
w^j,\qquad u^iw^j\ (i\ge1),\qquad v^iw^j\ (i\ge1).
$$

The pure $w$-monomials surviving modulo $w^{3q-1}$ are
$$
1,w,\dots,w^{3q-2},
$$
so there are $3q-1$ of them.

For $1\le i<q$, the relation
$$
u^qv^{q-i}=u^i(uv)^{q-i}=u^iw^{3(q-i)}
$$
shows that $u^iw^j$ is killed once $j\ge3(q-i)$. Since
$$
3(q-i)\le3q-3<3q-1,
$$
the generator $w^{3q-1}$ gives no earlier cutoff. Thus the number of surviving $u$-monomials is
$$
\sum_{i=1}^{q-1}3(q-i)=\frac{3q(q-1)}2.
$$
The same count holds for the $v$-monomials. Therefore
$$
\dim_{\mathbb F_p}Q
=(3q-1)+2\cdot\frac{3q(q-1)}2
=3q^2-1.
$$
This also covers $q=1$, when the two sums are empty and the quotient is $K[w]/(w^2)$.

Step 5: Restore the truncation and finish
Let
$$
M=\frac{\mathbb F_p[a,b,c]_{(a,b,c)}}{(a+b+c,s^{3q-1},t^q,\Delta^q)}.
$$
Then $M^{\langle\rho\rangle}=Q$. Give $u,v$ degree $3$ and $w$ degree $2$. The largest degree among the surviving monomials in Step 4 is at most
$$
6q-4.
$$
Hence
$$
(\mathfrak m^dM)^{\langle\rho\rangle}=0
\qquad(d>6q-4),
$$
where $\mathfrak m=(a,b,c)$.

Let
$$
K_0=(a^n,b^n,c^n)M.
$$
This ideal is $\rho$-stable and lies in $\mathfrak m^nM$. Since
$$
n=pq\ge29q>6q-4,
$$
we have $K_0^{\langle\rho\rangle}=0$. Exactness of cyclic invariants applied to
$$
0\to K_0\to M\to M/K_0\to0
$$
shows that restoring $a^n=b^n=c^n=0$ does not change the required invariant dimension.

Therefore
$$
\dim_{\mathbb F_p}V_n=3q^2-1=3\left(\frac np\right)^2-1.
$$

Final Answer: $\boxed{3\left(\frac np\right)^2-1}$

---

## Answer

$3\left(\frac np\right)^2-1$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- cyclic translation operators
- symmetric and alternating invariants
- mixed Frobenius exponents
- $A_2$ surface singularity
- semigroup monomial counting

## Black-Box Audit

The cyclic invariant ring, mixed-scale operator reduction, scalar extension, $uv=w^3$ model, monomial survival thresholds, and truncation argument are all derived explicitly.