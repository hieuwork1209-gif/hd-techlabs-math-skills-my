## Steps

Step 1: Handle the case $p\equiv3\pmod4$

Let
$$
C:\ X^4+Y^4=Z^4
$$
be the projective Fermat quartic. If $p\equiv3\pmod4$, then
$$
\gcd(4,p-1)=2.
$$
Hence the map $x\mapsto x^4$ on $\mathbb F_p$ has exactly the same fibers as the map $x\mapsto x^2$: zero has one preimage and every nonzero square has two. Therefore the number of projective solutions of
$$
X^4+Y^4=Z^4
$$
equals the number of projective solutions of
$$
X^2+Y^2=Z^2.
$$
The latter is a nonsingular conic with the rational point $(1:0:1)$, hence it is isomorphic to $\mathbb P^1$ over $\mathbb F_p$ and has
$$
p+1
$$
points.

Step 2: Express the count for $p\equiv1\pmod4$ by Jacobi sums

Assume now $p\equiv1\pmod4$. Choose a quartic character
$$
\chi:\mathbb F_p^\times\to\{1,i,-1,-i\},
$$
extended by $\chi(0)=0$, and put
$$
\eta=\chi^2,
$$
so $\eta$ is the quadratic character. For multiplicative characters $A,B$, write
$$
J(A,B)=\sum_{t\in\mathbb F_p}A(t)B(1-t).
$$

Let $r(u)$ be the number of fourth roots of $u$. Then
$$
r(0)=1,
$$
and for $u\ne0$,
$$
r(u)=1+\chi(u)+\eta(u)+\overline\chi(u).
$$
Expanding
$$
\sum_{u\in\mathbb F_p}r(u)r(1-u)
$$
therefore gives the affine point count
$$
p+\sum_{r,s=1}^3J(\chi^r,\chi^s).
$$
The three terms with $r+s\equiv0\pmod4$ are
$$
J(\chi,\overline\chi),\qquad J(\eta,\eta),\qquad J(\overline\chi,\chi),
$$
and the identity
$$
J(A,A^{-1})=-A(-1)
$$
gives their sum as
$$
-2\chi(-1)-1.
$$
The number of points at infinity is the number of fourth roots of $-1$, namely
$$
2(1+\chi(-1)).
$$
These two contributions add to $1$. Hence
$$
\#C(\mathbb F_p)
=p+1+J(\chi,\chi)+J(\overline\chi,\overline\chi)
+2J(\chi,\eta)+2J(\overline\chi,\eta).
$$

A change of variables $x=t/(t-1)$ in a Jacobi sum gives
$$
J(A,B)=A(-1)J(A,\overline{AB}).
$$
Taking $A=B=\chi$ yields
$$
J(\chi,\eta)=\chi(-1)J(\chi,\chi).
$$
By conjugation,
$$
J(\overline\chi,\eta)=\chi(-1)\overline{J(\chi,\chi)}.
$$
Thus, if
$$
J=J(\chi,\chi),\qquad s=\chi(-1),
$$
then
$$
\#C(\mathbb F_p)=p+1+(1+2s)(J+\overline J).
$$
Here
$$
s=1\quad\text{for }p\equiv1\pmod8,
$$
and
$$
s=-1\quad\text{for }p\equiv5\pmod8.
$$

Step 3: Evaluate the real part of the quartic Jacobi sum

Since $\chi$ takes values in $\mathbb Z[i]$, write
$$
J=A+iB,\qquad A,B\in\mathbb Z.
$$
For a nontrivial multiplicative character $\theta$, let
$$
G(\theta)=\sum_{x\in\mathbb F_p}\theta(x)e^{2\pi ix/p}.
$$
Expanding $G(A_1)G(A_2)$ and grouping by the sum of the two variables gives
$$
G(A_1)G(A_2)=J(A_1,A_2)G(A_1A_2)
$$
when $A_1,A_2,A_1A_2$ are nontrivial. Also direct character orthogonality gives
$$
|G(\theta)|^2=p.
$$
Taking $A_1=A_2=\chi$ therefore yields
$$
J\overline J=p,
$$
so
$$
A^2+B^2=p.
$$

It remains to determine the sign of the odd coordinate $A$. Put
$$
\lambda=1+i.
$$
Pair $x$ with $1-x$ in
$$
J=\sum_x\chi(x(1-x)).
$$
The fixed point is $x=1/2$, and every fourth root of unity $\zeta$ satisfies
$$
2\zeta\equiv2\pmod{\lambda^3}.
$$
Hence
$$
J\equiv \chi(1/4)+(p-3)\pmod{\lambda^3}.
$$
Now
$$
\chi(1/4)=\chi(4)=\eta(2)=s,
$$
so, using $p\equiv1\pmod8$ when $s=1$ and $p\equiv5\pmod8$ when $s=-1$,
$$
J\equiv-s\pmod{\lambda^3}.
$$
Thus $A$ is odd and $B$ is even. From $A^2+B^2=p$, one has
$$
B\equiv0\pmod4\quad\text{if }p\equiv1\pmod8,
$$
and
$$
B\equiv2\pmod4\quad\text{if }p\equiv5\pmod8.
$$
The divisibility $\lambda^3\mid J+s$ is equivalent to
$$
A+s\equiv B\pmod4.
$$
In both residue classes this gives
$$
A\equiv-1\pmod4.
$$
Therefore, if
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,
$$
then necessarily
$$
A=-a,\qquad J+\overline J=-2a.
$$

Step 4: Combine the cases

For $p\equiv1\pmod8$, we have $s=1$, so
$$
\#C(\mathbb F_p)=p+1+3(-2a)=p+1-6a.
$$
For $p\equiv5\pmod8$, we have $s=-1$, so
$$
\#C(\mathbb F_p)=p+1-(-2a)=p+1+2a.
$$
Together with Step 1,
$$
\#C(\mathbb F_p)=
\begin{cases}
p+1,&p\equiv3\pmod4,\\
p+1-6a,&p\equiv1\pmod8,\\
p+1+2a,&p\equiv5\pmod8.
\end{cases}
$$

Final Answer: $\boxed{p+1\text{ if }p\equiv3\pmod4;\ p+1-6a\text{ if }p\equiv1\pmod8;\ p+1+2a\text{ if }p\equiv5\pmod8}$

---

## Answer

$p+1$ if $p\equiv3\pmod4$; $p+1-6a$ if $p\equiv1\pmod8$; $p+1+2a$ if $p\equiv5\pmod8$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quartic multiplicative characters
- Jacobi sums
- Gauss sums
- Gaussian integer norm
- Fermat quartic over finite fields

---

## Black-Box Audit - no issues found