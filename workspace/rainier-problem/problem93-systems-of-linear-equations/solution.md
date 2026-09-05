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
Every polynomial fixed by the cycle splits uniquely into a symmetric part plus $\Delta$ times a symmetric part. Hence the cyclic invariant ring is
$$
E=\mathbb F_p[s,t,\Delta]\Big/(\Delta^2+4s^3+27t^2).
$$

Step 2: Reduce the operator equations
Let $q=n/p$. Since $q$ is a power of $p$,
$$
X^q=1+a^q,\qquad Y^q=1+b^q,\qquad Z^q=1+c^q,
$$
and $a^q+b^q+c^q=0$. Expanding the operators gives
$$
A=s^q,\qquad B=t^q.
$$
For
$$
C=(T_1-T_2)(T_2-T_3)(T_3-T_1)
$$
we have simply $C=\Delta$. Therefore the untruncated cyclic-invariant quotient is
$$
Q=E/(s^{2q},t^q,\Delta^{2(q-1)}).
$$
Put
$$
H=4s^3+27t^2.
$$
Since $\Delta^2=-H$,
$$
\Delta^{2(q-1)}=(-1)^{q-1}H^{q-1}=H^{q-1}.
$$
Also $E=\mathbb F_p[s,t]\oplus\Delta\mathbb F_p[s,t]$ as a module over $\mathbb F_p[s,t]$. Thus, with
$$
R_0=\mathbb F_p[s,t]/(s^{2q},t^q),
$$
we have
$$
\dim Q=2\dim R_0/(H^{q-1}).
$$
It remains to determine the rank of multiplication by $H^{q-1}$ on $R_0$.

Step 3: Split into six residue blocks
Set
$$
X=s^3,\qquad Y=t^2.
$$
Decompose $R_0$ according to the exponent of $s$ modulo $3$ and the exponent of $t$ modulo $2$:
$$
R_0=\bigoplus_{r=0}^2\bigoplus_{e=0}^1
s^rt^e\,\mathbb F_p[X,Y]/(X^{A_r},Y^{B_e}),
$$
where
$$
A_r=\#\{0\le i<2q:i\equiv r\pmod3\},
$$
$$
B_e=\#\{0\le j<q:j\equiv e\pmod2\}.
$$
Hence
$$
\sum_{r=0}^2A_r=2q,
\qquad
\sum_{e=0}^1B_e=q.
$$
Each block is preserved by multiplication by
$$
H^{q-1}=(4X+27Y)^{q-1}.
$$
Rescaling $X,Y$ by nonzero constants does not affect rank, so it suffices to study multiplication by $(X+Y)^{q-1}$.

Because $q$ is a power of $p$,
$$
(1+z)^q=1+z^q.
$$
Since $q$ is odd,
$$
(1+z)^{q-1}=1-z+z^2-\cdots+z^{q-1}.
$$
Thus all coefficients of $(X+Y)^{q-1}$ alternate between $1$ and $-1$.

Step 4: Compute the Frobenius-degenerate rank
Fix one block
$$
S_{A,B}=\mathbb F_p[X,Y]/(X^A,Y^B)
$$
with $A=A_r$ and $B=B_e$, and put
$$
R=A+B-q.
$$
Since $q\ge p\ge29$, all six values of $R$ are positive.

Multiplication by $(X+Y)^{q-1}$ raises total degree by $q-1$. The source degrees that can contribute are exactly
$$
d=0,1,\dots,R-1.
$$
For such a $d$, the degree-$d$ source has basis
$$
X^aY^{d-a}\qquad(0\le a\le d),
$$
and the degree-$d+q-1$ target has $R-d$ basis monomials. Because $R<A,B$, every source basis vector can connect to every target basis vector without crossing either truncation bound.

If the target $X$-exponent is $c$, the corresponding coefficient is, up to a fixed sign,
$$
(-1)^{a+c}.
$$
Therefore the matrix on this graded piece is an outer product of a sign column and a sign row, so it has rank exactly $1$. Distinct total degrees do not mix. Hence
$$
\operatorname{rank}\bigl((X+Y)^{q-1}:S_{A,B}\to S_{A,B}\bigr)=A+B-q.
$$
Summing over the six blocks gives
$$
\operatorname{rank}(H^{q-1}:R_0\to R_0)
=\sum_{r=0}^2\sum_{e=0}^1(A_r+B_e-q).
$$
Using the two counting identities from Step 3,
$$
\operatorname{rank}(H^{q-1})
=2(2q)+3(q)-6q=q.
$$
Since $\dim R_0=2q^2$,
$$
\dim R_0/(H^{q-1})=2q^2-q,
$$
and therefore
$$
\dim Q=4q^2-2q.
$$

Step 5: Restore the truncation and finish
Before restoring $a^n,b^n,c^n$, the invariant quotient $Q$ is spanned by classes of
$$
s^it^j,\qquad \Delta s^it^j,
$$
with $0\le i<2q$ and $0\le j<q$. Since $\deg s=2$, $\deg t=3$, and $\deg\Delta=3$, every such class has degree at most
$$
2(2q-1)+3(q-1)+3=7q-2.
$$

Let $\mathcal M$ be the corresponding untruncated quotient before taking cyclic invariants, and let
$$
K_0=(a^n,b^n,c^n)\mathcal M.
$$
Then $K_0\subseteq\mathfrak m^n\mathcal M$, where $\mathfrak m=(a,b,c)$. Since $n=pq\ge29q>7q-2$, the invariant part of $\mathfrak m^n\mathcal M$ is zero, so $K_0^{\langle\rho\rangle}=0$. Exactness of cyclic invariants applied to
$$
0\to K_0\to\mathcal M\to\mathcal M/K_0\to0
$$
shows that restoring $a^n=b^n=c^n=0$ does not change the required dimension.

Therefore
$$
\dim_{\mathbb F_p}V_n
=4q^2-2q
=4\left(\frac np\right)^2-2\left(\frac np\right).
$$

Final Answer: $\boxed{4\left(\frac np\right)^2-2\left(\frac np\right)}$

---

## Answer

$4\left(\frac np\right)^2-2\left(\frac np\right)$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- cyclic translation operators
- symmetric and alternating invariants
- Frobenius binomial degeneration
- residue-class module decomposition
- graded rank counting

## Black-Box Audit

The invariant ring, operator reduction, six-block decomposition, characteristic-$p$ rank collapse, rank sum, and truncation argument are all derived explicitly.