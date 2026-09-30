## Steps

Step 1: Classify the typable parenthesizations made only from S
Define
$$
R_1=S,
\qquad
R_{j+1}=S R_j.
$$
For fresh type variables $a,b,c$, set
$$
A_0=a\to b,
\qquad
A_1=a\to b\to c,
\qquad
A_{j+1}=A_j\to A_{j-1}\quad(j\geq1).
$$
Then $R_j$ has principal type
$$
A_j\to A_{j-1}\to a\to c.
$$
The claim is immediate for $j=1$. If it holds for $R_j$, a fresh copy of
$$
S:(u\to v\to w)\to(u\to v)\to u\to w
$$
can take $R_j$ as its first argument with the most general unifier
$$
u=A_j,
\qquad
v=A_{j-1},
\qquad
w=a\to c.
$$
The resulting principal type is
$$
(A_j\to A_{j-1})\to A_j\to a\to c
=
A_{j+1}\to A_j\to a\to c.
$$

We also need that $R_kR_m$ is untypable whenever $k\geq2$ and $m\geq1$. Use independent variables $p,q,r$ and the analogous sequence
$$
B_0=p\to q,
\qquad
B_1=p\to q\to r,
\qquad
B_{j+1}=B_j\to B_{j-1}.
$$
For $j\geq1$, $B_j$ cannot unify with $p\to r$. For $j=1$, this would force $r=q\to r$. For $j\geq2$, it would force $p$ to unify with $B_{j-1}$, which contains $p$. Both violate the occurs check.

If $k\geq3$, typing $R_kR_m$ would require
$$
A_{k-1}=B_m,
\qquad
A_{k-2}=B_{m-1}\to p\to r.
$$
Since $A_{k-1}=A_{k-2}\to A_{k-3}$, for $m\geq2$ comparison with $B_m=B_{m-1}\to B_{m-2}$ forces
$$
B_{m-1}=B_{m-1}\to p\to r,
$$
and for $m=1$ it forces $p=(p\to q)\to p\to r$. Both fail the occurs check.

For $k=2$, the same application equations give
$$
A_1=B_m,
\qquad
A_0=B_{m-1}\to p\to r.
$$
Hence $a=B_{m-1}$ and $b=p\to r$, so
$$
B_m=B_{m-1}\to(p\to r)\to c.
$$
The case $m=1$ forces $p=p\to q$. If $m\geq2$, then
$$
B_{m-2}=(p\to r)\to c.
$$
For $m=2$ or $m=3$, comparison of first domains again forces $p=p\to r$. For $m\geq4$, it would force $B_{m-3}$ to unify with $p\to r$, excluded above. Thus $R_kR_m$ is never typable for $k\geq2$.

Now induct on the number of copies of $S$ in a pure-$S$ term. At a typable root $UV$, both subterms are typable, so by induction they are $R_k$ and $R_m$. The preceding obstruction forces $k=1$, and therefore the whole term is the right-associated $R_{k+m}$. Hence $R_j$ is the unique typable pure-$S$ parenthesization with $j$ copies of $S$.

Step 2: Reduce a typable term ending in I to blocks S and SS
Since $I:x\to x$, typing $SI$ forces $x=y\to z$. The resulting principal type is
$
((y\to z)\to y)\to(y\to z)\to z.
$
The second argument type $y\to z$ reappears as the first domain, so for the induction it is natural to record this shape as
$
H(Q,D,R)=(Q\to D)\to Q\to R.
$
Thus
$
SI:H(y\to z,y,z).
$

We now induct on the number of copies of $S$ in a typable term ending in $I$. The one-$S$ term $SI$ has the displayed interface. For a larger typable term, write its root as $UX$, where $U$ is a pure-$S$ term and $X$ is the suffix containing $I$. Step 1 forces $U=R_k$. If $X$ still contains an $S$, then the induction hypothesis gives $X$ a principal type of the form $H(Q,D,R)$.

If the right subterm is exactly $I$, then $R_1I$ is typable, while $R_kI$ is untypable for $k\geq2$. For $k=2$, unifying the domain
$$
A_2=A_1\to A_0
$$
with $x\to x$ would require $A_1=A_0$, hence $b\to c=b$. For $k\geq3$, it would require $A_{k-1}=A_{k-2}$, while $A_{k-1}=A_{k-2}\to A_{k-3}$. Each equation fails the occurs check. Thus the innermost block is necessarily $S$.

Suppose instead that the right subterm $X$ contains an $S$, so by induction it has principal type $H(Q,D,R)$. If $k\geq3$, the domain of $R_k$ is
$$
A_k=A_{k-1}\to A_{k-2},
\qquad
A_{k-1}=A_{k-2}\to A_{k-3}.
$$
Unifying $A_k$ with
$$
H(Q,D,R)=(Q\to D)\to Q\to R
$$
would first give
$$
A_{k-1}=Q\to D,
\qquad
A_{k-2}=Q\to R.
$$
The relation $A_{k-1}=A_{k-2}\to A_{k-3}$ would then force the first domain $Q$ to unify with $Q\to R$, impossible by the occurs check. Hence every later left block also has size at most $2$.

For the two possible blocks, the interface evolves canonically. If
$$
X:H(Q,D,R),
$$
then $SX$ is always typable and has principal type
$$
H(Q\to D,Q,R).
$$
Also, $(SS)X$ is typable exactly when $D$ unifies with $R\to E$ for a fresh $E$. In that case its principal type is
$$
H(Q,D,E).
$$
The two transformations preserve the interface form, completing the induction. Thus every typable parenthesization of $S^nI$ is obtained by iterating the two contexts
$$
L_1(X)=SX,
\qquad
L_2(X)=(SS)X,
$$
and their availability is controlled by the displayed interface equations.

Step 3: Solve the block-compatibility language
Start from the mandatory innermost block
$$
SI:H(D\to R,D,R),
$$
with $D,R$ fresh. Call this state A.

From state A, an outer $S$ gives
$$
H((D\to R)\to D,D\to R,R).
$$
An outer $SS$ requires $D=R\to E$ and gives, after renaming $R,E$ as fresh variables, the same principal-type pattern
$$
H((D\to R)\to D,D\to R,R).
$$
Call this state B. Therefore either a block $1$ or a block $2$ takes state A to state B.

Write state B as
$$
H((u\to v)\to u,u\to v,v).
$$
An outer $SS$ is still possible: its condition
$$
u\to v=v\to E
$$
forces $u=v$ and $E=v$. The resulting state is
$$
H((t\to t)\to t,t\to t,t),
$$
which we call state C. Applying another outer $SS$ to state C leaves state C unchanged, because $t\to t=t\to E$ forces $E=t$.

In contrast, once an outer $S$ is applied to state B or state C, no later outer $SS$ can occur. In both states the result variable $R$ occurs in the domain of the current $Q$. After one outer $S$, the new defect is the old $Q$, so an $SS$ step would require $Q$ to unify with $R\to E$. Comparing first domains then equates $R$ with a type containing $R$, which fails the occurs check. If another outer $S$ is taken instead, the new $Q$ has the preceding $Q$ as its first domain. Hence that first domain still contains $R$. Induction on the number of further outer $S$ blocks shows that every later defect has a first domain containing $R$, so every later $SS$ attempt fails by the same occurs-check equation.

Reading blocks from the outside inward, the typable block words are therefore exactly
$$
1^a2^b1^c,
\qquad
a,b\geq0,
\qquad
c\in\{1,2\}.
$$
The total number of copies of $S$ represented by such a block word is
$$
a+2b+c.
$$

Step 4: State the complete family of typable parenthesizations
For a block word $d_1\cdots d_r$, the prompt defines
$$
L_{d_1\cdots d_r}(I)
=
L_{d_1}\bigl(L_{d_2}(\cdots L_{d_r}(I)\cdots)\bigr).
$$
Step 2 shows that every typable parenthesization has such a block representation, and Step 3 gives exactly the block words for which all required unifications succeed. Hence for every $n\geq1$,
$$
\mathcal T_n=
\left\{
L_{1^a2^b1^c}(I):
a,b\geq0, c\in\{1,2\}, a+2b+c=n
\right\}.
$$
Final Answer: $\boxed{\{L_{1^a2^b1^c}(I):a,b\geq0,c\in\{1,2\},a+2b+c=n\}}$

---

## Answer

$\{L_{1^a2^b1^c}(I):a,b\geq0,c\in\{1,2\},a+2b+c=n\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- simply typed combinatory logic
- principal types
- type unification
- occurs check
- structural induction
