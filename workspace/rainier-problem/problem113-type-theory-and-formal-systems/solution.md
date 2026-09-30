## Steps

Step 1: Derive the principal types of the right-associated terms
For fresh type variables $a,b,c$, define
$$
A_0=a\to b,
\qquad
A_1=a\to b\to c,
\qquad
A_{j+1}=A_j\to A_{j-1}\quad(j\geq1).
$$
We claim that the right-associated term $R_n$ has principal type
$$
A_n\to A_{n-1}\to a\to c.
$$
For $n=1$, this is
$$
(a\to b\to c)\to(a\to b)\to a\to c,
$$
which is exactly the type scheme of $S$.

Assume the claim for $R_n$. Take a fresh instance of the type of $S$,
$$
(u\to v\to w)\to(u\to v)\to u\to w.
$$
To type $S R_n$, its first argument type $u\to v\to w$ must unify with the principal type
$$
A_n\to A_{n-1}\to a\to c
$$
of $R_n$. The most general unifier is
$$
u=A_n,
\qquad
v=A_{n-1},
\qquad
w=a\to c.
$$
The resulting type is
$$
(A_n\to A_{n-1})\to A_n\to a\to c
=
A_{n+1}\to A_n\to a\to c.
$$
These equations are the most general unifier of the function domain with the principal type of $R_n$; every other typing of the application factors through a further substitution. Hence the displayed result is principal, and every $R_n$ is typable.

Step 2: Prove that a nontrivial right-associated term cannot be used as a function
Let $B_0=p\to q$, $B_1=p\to q\to r$, and
$$
B_{j+1}=B_j\to B_{j-1}.
$$
These are the corresponding type expressions for an independent copy of a right-associated term.

For every $j\geq1$, $B_j$ cannot unify with $p\to r$. For $j=1$, unifying
$$
p\to q\to r
$$
with $p\to r$ would force $r=q\to r$, which fails the occurs check. For $j\geq2$,
$$
B_j=B_{j-1}\to B_{j-2}
$$
would have to unify with $p\to r$, so $p$ would have to unify with $B_{j-1}$. Since $p$ occurs inside every $B_{j-1}$, this also fails the occurs check.

We now show that $R_kR_m$ is untypable whenever $k\geq2$ and $m\geq1$. Use independent variables $a,b,c$ for the principal type of $R_k$ and $p,q,r$ for that of $R_m$.

Suppose first that $k\geq3$. The domain of the principal type of $R_k$ is
$$
A_k=A_{k-1}\to A_{k-2},
$$
while the full principal type of $R_m$ is
$$
B_m\to B_{m-1}\to p\to r.
$$
For the application to type, these two types must unify, giving
$$
A_{k-1}=B_m,
\qquad
A_{k-2}=B_{m-1}\to p\to r.
$$
Since $A_{k-1}=A_{k-2}\to A_{k-3}$, the first equation becomes
$$
B_m=(B_{m-1}\to p\to r)\to A_{k-3}.
$$
If $m\geq2$, then $B_m=B_{m-1}\to B_{m-2}$, so the first domains would require
$$
B_{m-1}=B_{m-1}\to p\to r.
$$
No substitution on finite simple types can satisfy an equation $T=T\to U$: after applying any substitution, the right side is a proper arrow extension of the left side and has strictly more type-tree nodes. Hence this case is impossible. If $m=1$, comparing first domains instead forces
$$
p=(p\to q)\to p\to r,
$$
which fails the occurs check. Thus $R_kR_m$ is untypable for $k\geq3$.

It remains to handle $k=2$. Here
$$
A_2=A_1\to A_0.
$$
Unifying $A_2$ with the principal type of $R_m$ gives
$$
A_1=B_m,
\qquad
A_0=B_{m-1}\to p\to r.
$$
Since $A_0=a\to b$, this forces
$$
a=B_{m-1},
\qquad
b=p\to r.
$$
Using $A_1=a\to b\to c$, the first equation becomes
$$
B_m=B_{m-1}\to(p\to r)\to c.
$$
For $m=1$, comparing first domains forces $p=p\to q$, impossible by occurs check. For $m\geq2$, comparison with
$$
B_m=B_{m-1}\to B_{m-2}
$$
requires
$$
B_{m-2}=(p\to r)\to c.
$$
If $m=2$ or $m=3$, the left side begins with domain $p$, so this forces $p=p\to r$. If $m\geq4$, the first domain of $B_{m-2}$ is $B_{m-3}$, so $B_{m-3}$ would have to unify with $p\to r$, contradicting the first paragraph of this step. Therefore $R_2R_m$ is also untypable.

Step 3: Classify all typable parenthesizations
We prove by induction on $n$ that the only typable full parenthesization of $n$ copies of $S$ is $R_n$.

For $n=1$, the only term is $S=R_1$, which is typable.

Let $n\geq2$, and suppose a full parenthesization $T$ of $n$ copies of $S$ is typable. Its root has the form
$$
T=UV,
$$
where $U$ contains $k$ copies of $S$ and $V$ contains $m$ copies, with $k,m\geq1$ and $k+m=n$. Any typing derivation for an application includes typings of both subterms, so $U$ and $V$ are typable. By the induction hypothesis,
$$
U=R_k,
\qquad
V=R_m.
$$
If $k\geq2$, Step 2 shows that $R_kR_m$ is untypable, a contradiction. Hence $k=1$, so
$$
U=S
$$
and therefore
$$
T=SR_m=R_{m+1}=R_n.
$$
Conversely, Step 1 shows that every $R_n$ is typable. Thus there is exactly one typable parenthesization for each $n$, namely the fully right-associated one.

Step 4: State the exhaustive family
Let $\mathcal T_n$ be the set of all typable full parenthesizations of $n$ copies of $S$. The induction in Step 3 proves that no other parenthesization can occur, while Step 1 proves that $R_n$ always occurs. Hence
$$
\mathcal T_n=\{R_n\}.
$$
Final Answer: $\boxed{\{R_n\}}$

---

## Answer

$\{R_n\}$

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
