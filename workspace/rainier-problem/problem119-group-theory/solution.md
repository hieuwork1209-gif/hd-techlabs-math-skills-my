## Steps

Step 1: Set up the quartic character and the basic Jacobi sum

Let
$$
p\equiv1\pmod4,
$$
let $g$ be a primitive root modulo $p$, and put
$$
r=g^{(p-1)/4}\in\mathbb F_p.
$$
Choose the quartic character
$$
\chi:\mathbb F_p^\times\to\{1,i,-1,-i\}
$$
by requiring
$$
\chi(g)=i,
$$
and extend it by $\chi(0)=0$. Put
$$
\eta=\chi^2,
$$
so $\eta$ is the quadratic character, and set
$$
s=\chi(-1)=(-1)^{(p-1)/4}.
$$
For multiplicative characters $A,B$, write
$$
J(A,B)=\sum_{x\in\mathbb F_p}A(x)B(1-x),
$$
and abbreviate
$$
J=J(\chi,\chi).
$$

A change of variables $x=t/(t-1)$ gives
$$
J(A,B)=A(-1)J(A,\overline{AB}).
$$
Taking $A=B=\chi$ therefore yields
$$
J(\chi,\eta)=sJ,
$$
and by conjugation
$$
J(\overline\chi,\eta)=s\overline J.
$$
Also
$$
J(A,A^{-1})=-A(-1).
$$

Step 2: Count the quartic twist in terms of $J$

Let
$$
C_g:\ X^4+Y^4=gZ^4.
$$
For $u\in\mathbb F_p$, the number of fourth roots of $u$ is
$$
1+\chi(u)+\eta(u)+\overline\chi(u).
$$
Hence the affine point count is
$$
p+\sum_{m,n=1}^3\chi^{m+n}(g)J(\chi^m,\chi^n).
$$
Since $\chi(g)=i$, the nine Jacobi-sum terms simplify, using Step 1, to
$$
p-(J+\overline J)+2is(\overline J-J)-2s-1.
$$

The points at infinity satisfy
$$
X^4+Y^4=0.
$$
Their number is $4$ when $-1$ is a fourth power and $0$ otherwise, namely
$$
2(1+s).
$$
Therefore
$$
\#C_g(\mathbb F_p)
=p+1-(J+\overline J)+2is(\overline J-J).
$$

Step 3: Determine both coordinates of the quartic Jacobi sum

Because $\chi$ takes values in $\mathbb Z[i]$, write
$$
J=A+iB,
\qquad A,B\in\mathbb Z.
$$
For a nontrivial multiplicative character $\theta$, let
$$
G(\theta)=\sum_{x\in\mathbb F_p}\theta(x)e^{2\pi ix/p}.
$$
Expanding products and grouping by the sum of the variables gives
$$
G(A_1)G(A_2)=J(A_1,A_2)G(A_1A_2)
$$
when $A_1,A_2,A_1A_2$ are nontrivial, while character orthogonality gives
$$
|G(\theta)|^2=p.
$$
Applying these identities to $A_1=A_2=\chi$ gives
$$
J\overline J=p,
$$
so
$$
A^2+B^2=p.
$$

We next determine the sign of $A$. Put
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
Therefore
$$
J\equiv\chi(1/4)+(p-3)\pmod{\lambda^3}.
$$
Now
$$
\chi(1/4)=\eta(2)=s,
$$
so
$$
J\equiv-s\pmod{\lambda^3}.
$$
Since $A^2+B^2=p$, $A$ is odd and $B$ is even; moreover $B\equiv0\pmod4$ for $p\equiv1\pmod8$ and $B\equiv2\pmod4$ for $p\equiv5\pmod8$. The divisibility
$$
\lambda^3\mid J+s
$$
is equivalent to
$$
A+s\equiv B\pmod4,
$$
which in both residue classes gives
$$
A\equiv-1\pmod4.
$$
Thus, for the integer $a$ in the problem,
$$
A=-a.
$$

It remains to fix the sign of $B$. Reduce $\mathbb Z[i]$ modulo $p$ by the embedding
$$
i\longmapsto r.
$$
Because $\chi(g)=i$, the value $\chi(x)$ maps to
$$
x^{(p-1)/4}.
$$
With $m=(p-1)/4$ we therefore have
$$
J\longmapsto\sum_{x\in\mathbb F_p}x^m(1-x)^m.
$$
Expanding $(1-x)^m$, every exponent lies between $m$ and $2m<(p-1)$, so each power sum over $\mathbb F_p$ is $0$. Hence the image of $J$ is $0$, and
$$
-a+Br\equiv0\pmod p.
$$
Thus
$$
Br\equiv a\pmod p.
$$
By the sign normalization in the problem, this means
$$
B=b.
$$
Consequently
$$
J=-a+ib.
$$

Step 4: Substitute the Gaussian coordinates

From Step 2 and
$$
J=-a+ib,
$$
we have
$$
-(J+\overline J)=2a
$$
and
$$
2is(\overline J-J)=4sb.
$$
Since
$$
s=(-1)^{(p-1)/4},
$$
it follows that
$$
\#C_g(\mathbb F_p)=p+1+2a+4(-1)^{(p-1)/4}b.
$$

Final Answer: $\boxed{p+1+2a+4(-1)^{(p-1)/4}b}$

---

## Answer

$p+1+2a+4(-1)^{(p-1)/4}b$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quartic twists of Fermat curves
- quartic Jacobi sums
- Gauss sums
- Gaussian prime normalization
- finite-field character sums

---

## Black-Box Audit - no issues found