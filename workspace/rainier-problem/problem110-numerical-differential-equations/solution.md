## Steps

Step 1: Convert boundedness to a uniform polynomial bound

For fixed $s$, the recurrence gives
$$
u_m=R_{a,b}(s)^m u_0.
$$
It is bounded for every real $u_0$ exactly when $|R_{a,b}(s)|\leq1$. Hence $\rho(a,b)$ is the largest initial interval on which
$$
|1-s+as^2+bs^3|\leq1.
$$

Step 2: Prove the sharp endpoint certificate for cubics

Let $q$ be any real polynomial of degree at most $3$. Differentiating its Lagrange interpolation formula at the four nodes
$$
1,\quad \frac12,\quad -\frac12,\quad -1
$$
gives the identity
$$
q'(1)=\frac{19}{6}q(1)-4q\left(\frac12\right)
+\frac43q\left(-\frac12\right)-\frac12q(-1).
$$
This identity can also be checked directly on the basis $1,x,x^2,x^3$, so no general extremal theorem is being assumed.

If $|q(x)|\leq1$ for $-1\leq x\leq1$, then each term on the right is at most its coefficient's absolute value. Therefore
$$
q'(1)\leq \frac{19}{6}+4+\frac43+\frac12=9.
$$
Moreover, equality can hold only if
$$
q(1)=1,
\qquad q\left(\frac12\right)=-1,
\qquad q\left(-\frac12\right)=1,
\qquad q(-1)=-1.
$$
The unique cubic with these four values is
$$
q(x)=4x^3-3x.
$$

Step 3: Obtain the universal upper bound

Fix $(a,b)$ and take any $L<\rho(a,b)$. Map $[0,L]$ onto $[-1,1]$ by setting
$$
q_L(x)=R_{a,b}\left(\frac{L}{2}(1-x)\right).
$$
Then $|q_L(x)|\leq1$ on $[-1,1]$, while
$$
q_L'(1)=-\frac{L}{2}R_{a,b}'(0)=\frac{L}{2},
$$
because $R_{a,b}'(0)=-1$. Step 2 yields $L/2\leq9$, so $L\leq18$. Letting $L$ increase to $\rho(a,b)$ gives
$$
\rho(a,b)\leq18
$$
for every pair $(a,b)$, and therefore $\rho_*\leq18$.

Step 4: Attain the bound and prove uniqueness

Take
$$
a_* = \frac{4}{27},
\qquad
b_*=-\frac{4}{729}.
$$
The corresponding amplification polynomial satisfies the exact factorizations
$$
R_{a_*,b_*}(s)-1=-\frac{s(2s-27)^2}{729},
\qquad
R_{a_*,b_*}(s)+1=\frac{(18-s)(2s-9)^2}{729}.
$$
Thus $-1\leq R_{a_*,b_*}(s)\leq1$ for $0\leq s\leq18$. For every $s>18$, the second factorization gives $R_{a_*,b_*}(s)<-1$. Hence
$$
\rho(a_*,b_*)=18.
$$

Now suppose another pair has stability radius $18$. Continuity gives $|R_{a,b}(s)|\leq1$ on the whole interval $[0,18]$. With
$$
q(x)=R_{a,b}(9(1-x)),
$$
we have $|q|\leq1$ on $[-1,1]$ and $q'(1)=9$. Equality must therefore hold in the certificate of Step 2, forcing
$$
q(x)=4x^3-3x.
$$
Consequently
$$
R_{a,b}(s)=4\left(1-\frac{s}{9}\right)^3-3\left(1-\frac{s}{9}\right)
=1-s+\frac{4}{27}s^2-\frac{4}{729}s^3.
$$
Thus $(a,b)=(a_*,b_*)$, proving uniqueness.

Final Answer: $\boxed{(18,\frac{4}{27},-\frac{4}{729})}$

## Answer

$(18,\frac{4}{27},-\frac{4}{729})$

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

## Solution Concepts

- absolute stability polynomial
- extremal cubic interpolation
- equioscillation certificate
- sharp stability radius

## Black-Box Audit

The sharp cubic derivative bound is proved directly from a four-node interpolation identity. No external theorem or computational black box is used.
