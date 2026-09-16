## Steps

Step 1: Separate the case in which a factor vanishes
Let
$$
m=\frac{p-1}{2}
$$
and write $\chi(\cdot)=\left(\frac{\cdot}{p}\right)$ for the Legendre symbol. We must evaluate
$$
P_p=\prod_{k=1}^{m}\chi(k^2+k+1).
$$

If $p\equiv1\pmod3$, then $\mathbb F_p^\times$ contains two nontrivial cube roots of unity. These are precisely the two roots of
$$
x^2+x+1=0.
$$
If their representatives in $\{1,\dots,p-1\}$ are $r$ and $s$, then
$$
r+s\equiv-1\pmod p.
$$
Since $2\le r+s\le2p-2$, we must have
$$
r+s=p-1=2m.
$$
The two roots are distinct, so exactly one of them lies in $\{1,\dots,m\}$. Hence one factor in $P_p$ is zero, and therefore
$$
P_p=0
\qquad(p\equiv1\pmod3).
$$

From now on assume
$$
p\equiv2\pmod3.
$$
Then $x^2+x+1$ has no root in $\mathbb F_p$, so every factor in $P_p$ is nonzero.

Step 2: Convert the half-range product into a product over odd residues
For every $k$,
$$
4(k^2+k+1)=(2k+1)^2+3.
$$
Since $4$ is a square modulo $p$,
$$
P_p
=\chi\left(\prod_{k=1}^{m}\bigl((2k+1)^2+3\bigr)\right).
$$

Let
$$
O=\{1,3,5,\dots,p-2\}\subset\mathbb F_p
$$
and define
$$
B=\prod_{u\in O}(u^2+3).
$$
As $k$ runs from $1$ to $m-1$, the numbers $2k+1$ run through $O\setminus\{1\}$, while for $k=m$ we have $2m+1=p\equiv0\pmod p$. Hence
$$
\prod_{k=1}^{m}\bigl((2k+1)^2+3\bigr)
=3\prod_{u\in O\setminus\{1\}}(u^2+3).
$$
The omitted factor at $u=1$ is $4$, so
$$
4\prod_{k=1}^{m}\bigl((2k+1)^2+3\bigr)=3B.
$$
Again $4$ is a square, and therefore
$$
P_p=\chi(3B).
$$

Step 3: Evaluate the odd-residue product in a quadratic extension
Quadratic reciprocity gives
$$
\left(\frac{-3}{p}\right)
=\left(\frac{-1}{p}\right)\left(\frac3p\right)
=(-1)^m\cdot(-1)^m\left(\frac p3\right)
=\left(\frac p3\right).
$$
Because $p\equiv2\pmod3$,
$$
\left(\frac{-3}{p}\right)=-1.
$$
Thus $-3$ is not a square in $\mathbb F_p$. Choose
$$
\alpha\in\mathbb F_{p^2}
$$
with
$$
\alpha^2=-3.
$$
The Frobenius automorphism must exchange the two roots $\alpha$ and $-\alpha$, so
$$
\alpha^p=-\alpha.
$$
Consequently
$$
\alpha^{p-1}=-1.
$$

Define
$$
F(t)=\prod_{u\in O}(t-u).
$$
The nonzero elements of $\mathbb F_p$ split as the disjoint union of $O$ and $-O$: if $u$ is represented by an odd integer, then $p-u$ is even. Therefore
$$
t^{p-1}-1
=\prod_{x\in\mathbb F_p^\times}(t-x)
=F(t)\prod_{u\in O}(t+u).
$$
Since
$$
F(-t)=(-1)^m\prod_{u\in O}(t+u),
$$
we obtain
$$
t^{p-1}-1=(-1)^mF(t)F(-t).
$$
Evaluating at $t=\alpha$ gives
$$
-2=(-1)^mF(\alpha)F(-\alpha).
$$
But
$$
F(\alpha)F(-\alpha)
=\prod_{u\in O}(\alpha-u)(-\alpha-u)
=\prod_{u\in O}(u^2-\alpha^2)
=\prod_{u\in O}(u^2+3)
=B.
$$
Hence
$$
B=-2(-1)^m.
$$

Step 4: Return to the Legendre symbol
Using Step 2,
$$
P_p=\chi(3B)=\chi\bigl(-6(-1)^m\bigr).
$$
Now
$$
\chi(-1)=(-1)^m,
$$
so
$$
\chi\bigl(-(-1)^m\bigr)=1.
$$
Therefore
$$
P_p=\chi(6)=\left(\frac6p\right)
\qquad(p\equiv2\pmod3).
$$
Combining the two congruence classes modulo $3$ gives
$$
P_p=
\begin{cases}
0,&p\equiv1\pmod3,\\
\left(\dfrac6p\right),&p\equiv2\pmod3.
\end{cases}
$$

Final Answer: $\boxed{\begin{cases}0,&p\equiv1\pmod3,\\\left(\dfrac6p\right),&p\equiv2\pmod3.\end{cases}}$

---

## Answer

$\begin{cases}0,&p\equiv1\pmod3,\\\left(\dfrac6p\right),&p\equiv2\pmod3.\end{cases}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- legendre symbol
- quadratic reciprocity
- quadratic finite-field extensions
- frobenius conjugation
- finite-field product factorization
