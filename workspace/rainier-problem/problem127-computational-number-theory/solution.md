## Steps

Step 1: Separate the automatic high-valuation solutions
Let $N_n(p)$ be the number of pairs $(x,y)\in(\mathbb Z/p^n\mathbb Z)^2$ satisfying
$$
x^2\equiv y^3\pmod{p^n}.
$$
For a residue class $x$, write
$$
a=\min(v_p(x),n),
$$
and similarly
$$
b=\min(v_p(y),n).
$$
If
$$
2a\ge n
\qquad\text{and}\qquad
3b\ge n,
$$
then both $x^2$ and $y^3$ vanish modulo $p^n$, so the congruence is automatic.

There are
$$
p^{n-\lceil n/2\rceil}=p^{\lfloor n/2\rfloor}
$$
choices for $x$ divisible by $p^{\lceil n/2\rceil}$, and
$$
p^{n-\lceil n/3\rceil}=p^{\lfloor2n/3\rfloor}
$$
choices for $y$ divisible by $p^{\lceil n/3\rceil}$. Hence this high-valuation region contributes
$$
p^{\lfloor n/2\rfloor+\lfloor2n/3\rfloor}
$$
solutions.

Step 2: Classify every remaining solution by its exact valuations
Now suppose the solution is not in the region of Step 1. If one of $2a,3b$ were at least $n$ and the other were less than $n$, then $x^2-y^3$ would have valuation less than $n$, which is impossible. Therefore both are less than $n$.

For two nonzero residues modulo $p^n$ whose valuations are below $n$, congruence modulo $p^n$ forces the two valuations to agree. Thus
$$
2a=3b<n.
$$
Since $\gcd(2,3)=1$, there is a unique integer $t\ge0$ such that
$$
a=3t,
\qquad
b=2t,
$$
and necessarily
$$
6t<n.
$$
So the remaining solutions split disjointly into strata indexed by
$$
0\le t\le\left\lfloor\frac{n-1}{6}\right\rfloor.
$$

Step 3: Count one valuation stratum by reconstructing the unit parameter
Fix such a $t$ and put
$$
m=n-6t.
$$
Write
$$
x=p^{3t}u,
\qquad
y=p^{2t}v,
$$
where $u$ and $v$ are units. The congruence becomes
$$
u^2\equiv v^3\pmod{p^m}.
$$

The unit solutions modulo $p^m$ are in bijection with the units $z$ modulo $p^m$ via
$$
z\longmapsto(z^3,z^2).
$$
Indeed, this map always gives $u^2=v^3$. Conversely, if $u^2=v^3$, define
$$
z=v^2u^{-1}.
$$
Then
$$
z^2=v^4u^{-2}=v,
$$
and
$$
z^3=v^6u^{-3}=u.
$$
Hence there are exactly
$$
\varphi(p^m)=p^{m-1}(p-1)
$$
reduced unit pairs $(u,v)$ modulo $p^m$.

For each such pair, $u$ has
$$
p^{(n-3t)-m}=p^{3t}
$$
lifts to a unit modulo $p^{n-3t}$, while $v$ has
$$
p^{(n-2t)-m}=p^{4t}
$$
lifts to a unit modulo $p^{n-2t}$. Therefore the stratum indexed by $t$ contributes
$$
p^{7t}p^{m-1}(p-1)
=(p-1)p^{n+t-1}
$$
solutions.

Step 4: Sum the disjoint strata
Let
$$
q=\left\lfloor\frac{n-1}{6}\right\rfloor.
$$
The contribution from Step 3 is
$$
\sum_{t=0}^{q}(p-1)p^{n+t-1}
=p^{n-1}(p^{q+1}-1).
$$
Since
$$
q+1=\left\lceil\frac n6\right\rceil,
$$
adding the high-valuation solutions from Step 1 gives
$$
N_n(p)
=p^{\lfloor n/2\rfloor+\lfloor2n/3\rfloor}
+p^{n-1}\left(p^{\lceil n/6\rceil}-1\right).
$$
The valuation cases in Steps 1 and 2 are exhaustive and disjoint, so this counts every solution exactly once.

Final Answer: $\boxed{p^{\lfloor n/2\rfloor+\lfloor2n/3\rfloor}+p^{n-1}\left(p^{\lceil n/6\rceil}-1\right)}$

---

## Answer

$p^{\lfloor n/2\rfloor+\lfloor2n/3\rfloor}+p^{n-1}\left(p^{\lceil n/6\rceil}-1\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- p-adic valuations
- modular solution counting
- unit parametrization
- lifting residue classes
- geometric series
