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

Let $q=n/p$. Since $p$ is odd, $q$ is odd, so $(q-1)/2$ is an integer. Since $q$ is a power of $p$,
$$
X^q=1+a^q,\qquad Y^q=1+b^q,\qquad Z^q=1+c^q,
$$
and $a^q+b^q+c^q=0$. Expanding the operators gives
$$
A=s^q,\qquad B=t^q,\qquad C=\Delta^q.
$$
Hence
$$
D^{(q-1)/2}A=s^{(q-1)/2}s^q=s^{(3q-1)/2}.
$$
Put
$$
m=\frac{3q-1}{2}.
$$
Therefore the untruncated cyclic-invariant quotient is
$$
Q=E/(s^m,t^q,\Delta^q).
$$
The cutoff $m$ lies strictly inside the nilpotent range, so this is not a complete-intersection count with only a top socle correction.

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
\frac{K[u,v,w]}{(uv-w^3,u^q,v^q,w^m)}.
$$

Step 4: Count the two monomial regimes
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
There are $m$ surviving pure $w$-monomials.

For $1\le i<q$, the identity
$$
u^qv^{q-i}=u^i(uv)^{q-i}=u^iw^{3(q-i)}
$$
shows that $u^iw^j$ survives exactly for
$$
0\le j<\min\{m,3(q-i)\}.
$$
The same holds for the $v$-monomials. Therefore
$$
\dim Q=m+2\sum_{i=1}^{q-1}\min\{m,3(q-i)\}.
$$
Write $q=2k+1$, so $m=3k+1$. Replacing $q-i$ by $r$ splits the sum at $r=k$:
$$
\sum_{r=1}^{2k}\min\{3k+1,3r\}
=
3\sum_{r=1}^{k}r+k(3k+1)
=
\frac{9k^2+5k}{2}.
$$
Hence
$$
\dim Q
=3k+1+9k^2+5k
=9k^2+8k+1
=\frac{9q^2-2q-3}{4}.
$$

Step 5: Restore the truncation and finish
Let
$$
\mathcal M=\frac{\mathbb F_p[a,b,c]_{(a,b,c)}}{(a+b+c,s^m,t^q,\Delta^q)}.
$$
Then $\mathcal M^{\langle\rho\rangle}=Q$. Give $u,v$ degree $3$ and $w$ degree $2$. From the two regimes in Step 4, every surviving invariant monomial has degree less than $5q$. Hence
$$
(\mathfrak m^{5q}\mathcal M)^{\langle\rho\rangle}=0,
$$
where $\mathfrak m=(a,b,c)$.

Let
$$
K_0=(a^n,b^n,c^n)\mathcal M.
$$
This ideal is $\rho$-stable and lies in $\mathfrak m^n\mathcal M$. Since
$$
n=pq\ge29q>5q,
$$
we have $K_0^{\langle\rho\rangle}=0$. Exactness of cyclic invariants applied to
$$
0\to K_0\to\mathcal M\to\mathcal M/K_0\to0
$$
shows that restoring $a^n=b^n=c^n=0$ does not change the required invariant dimension.

Therefore
$$
\dim_{\mathbb F_p}V_n
=\frac{9q^2-2q-3}{4}
=\frac{9(n/p)^2-2(n/p)-3}{4}.
$$

Final Answer: $\boxed{\frac{9(n/p)^2-2(n/p)-3}{4}}$

---

## Answer

$\frac{9(n/p)^2-2(n/p)-3}{4}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- cyclic translation operators
- symmetric and alternating invariants
- mixed nilpotent cutoff
- $A_2$ surface singularity
- semigroup monomial counting

## Black-Box Audit

The invariant ring, mixed exponent reduction, scalar extension, $uv=w^3$ model, two-regime monomial count, and truncation argument are derived explicitly.