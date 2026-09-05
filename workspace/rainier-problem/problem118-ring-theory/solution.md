## Steps

Step 1: Put the presentation into a normal form
Let
$$
A=k[x]/(x^{n+1})
$$
and define a $k$-derivation $\delta:A\to A$ by
$$
\delta(f)=x^r f'(x).
$$
This is well defined because $\delta(x^{n+1})=(n+1)x^{n+r}=0$ in $A$. The defining relation is therefore
$$
ya=ay+\delta(a)\qquad(a\in A).
$$
In particular,
$$
yx^q=x^q y+q x^{q+r-1}\qquad(0\leq q\leq n).
$$
The relation moves every $y$ to the right of every coefficient from $A$. For uniqueness, take the free left $A$-module with basis $1,y,y^2,\ldots$ and define multiplication by $ya=ay+\delta(a)$; associativity follows from $\delta(ab)=\delta(a)b+a\delta(b)$. Its generators satisfy the stated relations, while rewriting every word in the presented algebra gives the same normal monomials, so the two constructions are inverse. Hence every element of $R_{n,r}$ has a unique form
$$
z=\sum_{j=0}^{m}a_j(x)y^j,\qquad a_j(x)\in A.
$$

Step 2: Determine which coefficients can commute with $y$
Set
$$
s=n-r+2.
$$
For $1\leq q\leq n$,
$$
\delta(x^q)=q x^{q+r-1}.
$$
Since the characteristic is zero, this vanishes in $A$ exactly when $q+r-1\geq n+1$, equivalently $q\geq s$. Thus
$$
\ker\delta=k\oplus x^sA.
$$
If $z=\sum a_jy^j$ is central, then
$$
0=[y,z]=\sum_{j=0}^{m}\delta(a_j)y^j,
$$
so uniqueness of the normal form gives $a_j\in k\oplus x^sA$ for every $j$.

Step 3: Eliminate scalar coefficients of positive powers of $y$
Write
$$
a_j=c_j+b_j,\qquad c_j\in k,\quad b_j\in x^sA.
$$
Induction from $yx=xy+x^r$ gives, for $j\geq1$,
$$
y^j x=xy^j+jx^r y^{j-1}+\text{terms of $y$-degree at most $j-2$},
$$
and every coefficient in $[y^j,x]$ is divisible by $x^r$. Since $s+r=n+2$, every $b_j\in x^sA$ annihilates those coefficients.

Assume some $c_j$ with $j\geq1$ is nonzero, and choose the largest such index $m$. In $[z,x]$, the coefficient of $y^{m-1}$ contributed by scalar parts is
$$
m c_m x^r.
$$
No lower scalar term reaches $y^{m-1}$, and all $b_j$ contributions vanish as noted above. Because $r\leq n$, the class of $x^r$ in $A$ is nonzero; because the characteristic is zero, $m c_m\neq0$. This contradicts $[z,x]=0$. Hence $c_j=0$ for all $j\geq1$, so every central element lies in
$$
k+x^sR_{n,r}.
$$

Step 4: Verify that the candidate subalgebra is central and that the threshold is sharp
A normal monomial in $x^sR_{n,r}$ has the form $x^{s+q}y^j$ with $q,j\geq0$ and $s+q\leq n$. Its commutator with $y$ is
$$
[y,x^{s+q}y^j]=(s+q)x^{s+q+r-1}y^j=0,
$$
because $s+r-1=n+1$. Its commutator with $x$ also vanishes: every coefficient of $[y^j,x]$ is divisible by $x^r$, while
$$
x^{s+q}x^r=0
$$
in $A$. Therefore $x^sR_{n,r}\subseteq Z(R_{n,r})$.

The exponent cannot be lowered, since
$$
[y,x^{s-1}]=(s-1)x^n\neq0.
$$
Combining this with Step 3 yields
$$
Z(R_{n,r})=k+x^{n-r+2}R_{n,r}.
$$
Final Answer: $\boxed{k+x^{n-r+2}R_{n,r}}$

---

## Answer

$k+x^{n-r+2}R_{n,r}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- noncommutative ring center
- derivations of truncated polynomial rings
- normal forms in skew polynomial rings
- leading-degree commutator analysis
- annihilator ideals

---

## Black-Box Audit — no issues found
