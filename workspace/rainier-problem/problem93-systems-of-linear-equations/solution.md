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
preserves the quotient. Since $p\ne3$, Reynolds averaging makes taking $\langle\rho\rangle$-invariants exact, and the invariant subspace of the dual has the same dimension as the invariant subspace of the quotient.

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
A polynomial fixed by the cycle splits uniquely into a symmetric part plus $\Delta$ times a symmetric part. Hence the cyclic invariant ring is
$$
E=\mathbb F_p[s,t,\Delta]_{(s,t,\Delta)}\Big/(\Delta^2+4s^3+27t^2).
$$
The relation is the discriminant identity for
$$
(u-a)(u-b)(u-c)=u^3+su-t.
$$

Step 2: Identify the three Frobenius-power generators
Let $q=n/p$. Since $q$ is a power of $p$,
$$
X^q=1+a^q,\qquad Y^q=1+b^q,\qquad Z^q=1+c^q,
$$
and $a^q+b^q+c^q=0$. Expanding the three operators gives
$$
A=s^q,\qquad B=t^q,\qquad C=\Delta^q.
$$
Therefore the untruncated cyclic-invariant quotient to be counted is
$$
Q=E/(s^q,t^q,\Delta^q).
$$
Thus the problem is no longer a complete-intersection count: three Frobenius-power generators meet at the singular point of the surface
$$
\Delta^2+4s^3+27t^2=0.
$$

Step 3: Convert the singularity to $uv=w^3$
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
Because $q$ is a $p$-power, $u^q,v^q$ are invertible $K$-linear combinations of $\Delta^q,t^q$. Hence
$$
Q\otimes_{\mathbb F_p}K
\cong
\frac{K[u,v,w]}{(uv-w^3,u^q,v^q,w^q)}.
$$
It remains to compute the length of this monomial Frobenius quotient.

Step 4: Count the surviving semigroup monomials
The ring
$$
K[u,v,w]/(uv-w^3)
$$
embeds into $K[\xi,\eta]$ by
$$
u=\xi^3,\qquad v=\eta^3,\qquad w=\xi\eta.
$$
Thus monomials are linearly independent according to their exponent pairs, and every monomial has a unique form of one of the types
$$
w^j,\qquad u^iw^j\ (i\ge1),\qquad v^iw^j\ (i\ge1).
$$
In the quotient by $(u^q,v^q,w^q)$, the pure $w$-monomials surviving are
$$
1,w,\dots,w^{q-1}.
$$
For $1\le i<q$, the monomial $u^iw^j$ is killed by $w^q$ when $j\ge q$. It is also killed by $u^q$ exactly from the threshold
$$
u^qv^{q-i}=u^i(uv)^{q-i}=u^iw^{3(q-i)},
$$
so the surviving $u$-monomials are precisely
$$
u^iw^j,
\qquad
0\le j<\min\{q,3(q-i)\}.
$$
The same count holds for the $v$-monomials. Therefore
$$
\dim_{\mathbb F_p}Q
=q+2\sum_{i=1}^{q-1}\min\{q,3(q-i)\}.
$$
Put
$$
a_0=\left\lfloor\frac{q-1}{3}\right\rfloor.
$$
After replacing $q-i$ by $r$,
$$
\sum_{i=1}^{q-1}\min\{q,3(q-i)\}
=
\frac{3a_0(a_0+1)}2+q(q-1-a_0).
$$
Since $q$ is a power of the prime $p\ne3$, we have $q\equiv1$ or $2\pmod3$. Substituting $q=3m+1$ or $q=3m+2$ into the preceding expression gives in both cases
$$
\dim_{\mathbb F_p}Q=\frac{5q^2-2}{3}.
$$

Step 5: Restore the truncation
Let
$$
D=\frac{\mathbb F_p[a,b,c]_{(a,b,c)}}{(a+b+c,s^q,t^q,\Delta^q)}.
$$
Then $D^{\langle\rho\rangle}=Q$. In Step 4, after scalar extension, every spanning monomial has weighted degree at most
$$
3(q-1)+2(q-1)=5q-5,
$$
where $u,v$ have degree $3$ and $w$ has degree $2$. Hence
$$
(\mathfrak m^dD)^{\langle\rho\rangle}=0
\qquad(d>5q-5),
$$
with $\mathfrak m=(a,b,c)$.

Now let
$$
K_0=(a^n,b^n,c^n)D.
$$
This ideal is $\rho$-stable and lies in $\mathfrak m^nD$. Since
$$
n=pq\ge29q>5q-5,
$$
we get $K_0^{\langle\rho\rangle}=0$. Exactness of cyclic invariants applied to
$$
0\to K_0\to D\to D/K_0\to0
$$
shows that restoring $a^n=b^n=c^n=0$ does not change the cyclic-invariant dimension.

Therefore
$$
\dim_{\mathbb F_p}V_n
=\frac{5q^2-2}{3}
=\frac{5(n/p)^2-2}{3}.
$$

Final Answer: $\boxed{\frac{5(n/p)^2-2}{3}}$

---

## Answer

$\frac{5(n/p)^2-2}{3}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- cyclic translation operators
- symmetric and alternating invariants
- $A_2$ surface singularity
- Frobenius-power quotient length
- semigroup monomial counting

## Black-Box Audit

The cyclic invariant ring, discriminant relation, scalar extension, $uv=w^3$ reduction, monomial survival criterion, finite sum, and truncation argument are all derived explicitly.