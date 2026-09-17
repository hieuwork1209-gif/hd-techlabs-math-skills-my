## Steps

Step 1: Fix the signed Gaussian parameter and prove the basic CM trace

Let $p\equiv1\pmod8$ be prime, let $\chi$ be the Legendre symbol modulo $p$, and put
$$
\delta=\chi(3)\in\{\pm1\}.
$$
Write
$$
p=u^2+v^2,
$$
where $u$ is odd, $v>0$ is even, and the sign of $u$ is fixed by
$$
\boxed{u\equiv1\pmod4.}
\tag{1}
$$

Set
$$
S_0:=\sum_{x\in\mathbb F_p}\chi(x^3-x).
$$
Choose a quartic multiplicative character $\psi$ on $\mathbb F_p^\times$ with $\psi^2=\chi$, extended by $\psi(0)=0$. Since $\chi(-1)=1$,
$$
S_0=\sum_x\chi(x)\chi(x^2-1).
$$
For $x\ne0$, put $z=x^2$. The two square roots $\pm x$ have the same quadratic character, and
$$
\psi(z)=\psi(x^2)=\chi(x).
$$
Therefore
$$
\begin{aligned}
S_0
&=2\sum_{\substack{z\ne0\\ \chi(z)=1}}\psi(z)\chi(z-1)\\
&=\sum_z(1+\chi(z))\psi(z)\chi(1-z)\\
&=J(\psi,\chi)+J(\overline\psi,\chi)\\
&=2\operatorname{Re}J(\psi,\chi),
\end{aligned}
\tag{2}
$$
where
$$
J(\alpha,\beta)=\sum_{z\in\mathbb F_p}\alpha(z)\beta(1-z).
$$
Write
$$
J(\psi,\chi)=A+iB\in\mathbb Z[i].
$$
The Gauss-sum identity
$$
G(\alpha)G(\beta)=J(\alpha,\beta)G(\alpha\beta)
$$
for nontrivial $\alpha,\beta,\alpha\beta$, together with $|G(\gamma)|^2=p$, gives
$$
A^2+B^2=p.
\tag{3}
$$

To fix the sign of $A$, consider
$$
E_0:\quad y^2=x^3-x.
$$
For each $x$, the number of $y$ is $1+\chi(x^3-x)$, so
$$
\#E_0(\mathbb F_p)=p+1+S_0.
\tag{4}
$$
The full rational $2$-torsion is
$$
E_0[2](\mathbb F_p)=\{O,(0,0),(1,0),(-1,0)\}.
$$
Choose $i\in\mathbb F_p$ with $i^2=-1$. Since $p\equiv1\pmod8$,
$$
\chi(i)=(-1)^{(p-1)/4}=1
$$
and $\chi(2)=1$, hence
$$
\chi(-2i)=1.
$$
Choose $y\in\mathbb F_p$ with $y^2=-2i$ and let $P=(i,y)$. The duplication formula yields
$$
x(2P)
=\left(\frac{3i^2-1}{2y}\right)^2-2i
=\frac4{y^2}-2i
=0.
$$
Thus
$$
2P=(0,0),
$$
so $P$ has order $4$. Together with, for example, $(1,0)$, this gives a subgroup of order $8$. Therefore
$$
8\mid\#E_0(\mathbb F_p).
\tag{5}
$$
From (4),
$$
S_0\equiv-(p+1)\equiv-2\pmod8.
$$
Using (2), $S_0=2A$, so
$$
A\equiv-1\pmod4.
$$
By (3), $A$ is the odd coordinate in a representation of $p$ as a sum of two squares. Comparing with (1),
$$
A=-u.
$$
Hence
$$
\boxed{S_0=-2u.}
\tag{6}
$$

Step 2: Evaluate the quartic character sum

Define
$$
Q_p
:=
\sum_{x\in\mathbb F_p}
\chi\bigl(x(x-1)(x-3)(x+3)\bigr).
\tag{7}
$$
Consider the genus-one curve
$$
C:\quad y^2=x(x-1)(x-3)(x+3).
$$
Since the quartic on the right is monic, the smooth projective model has two $\mathbb F_p$-rational points at infinity. Therefore
$$
\#C(\mathbb F_p)=p+Q_p+2.
\tag{8}
$$

We now transform $C$ to a quadratic twist of $E_0$. For $x\ne0$, put
$$
r=\frac1x,
\qquad
Y=\frac y{x^2}.
$$
Then
$$
Y^2=(1-r)(1-3r)(1+3r).
$$
Set
$$
T=\frac{3r-1}{2}.
$$
A direct calculation gives
$$
(1-r)(1-3r)(1+3r)
=\frac83(T^3-T).
$$
Thus $C$ is birational over $\mathbb F_p$ to
$$
E_d:\quad Y^2=d(T^3-T),
\qquad d=\frac83.
\tag{9}
$$
Because $p\equiv1\pmod8$,
$$
\chi(8)=1,
$$
and hence
$$
\chi(d)=\chi(3)=\delta.
$$
Using (6),
$$
\#E_d(\mathbb F_p)
=p+1+\delta S_0
=p+1-2\delta u.
\tag{10}
$$
Since $C$ and $E_d$ are birational smooth projective genus-one curves, their point counts agree. Comparing (8) and (10),
$$
\boxed{Q_p=-1-2\delta u.}
\tag{11}
$$

Step 3: Count points for which all four signs are equal

For $x\notin\{0,1,3,-3\}$, write
$$
s_1=\chi(x),
\quad
s_2=\chi(x-1),
\quad
s_3=\chi(x-3),
\quad
s_4=\chi(x+3).
$$
The indicator that all four signs are equal is
$$
\frac18\left(
1+\sum_{1\le i<j\le4}s_is_j+s_1s_2s_3s_4
\right).
\tag{12}
$$
For any distinct $a,b\in\mathbb F_p$,
$$
\sum_x\chi((x-a)(x-b))=-1.
$$
There are six pairs, so summing the right side of (12) over all $x\in\mathbb F_p$ gives the raw value
$$
\frac{p-6+Q_p}{8}.
\tag{13}
$$

We must remove the four exceptional roots, where one Legendre symbol is $0$. At such a point, the expression in (12) equals $1/2$ exactly when the remaining three nonzero signs are all equal, and is $0$ otherwise.

The remaining sign triples are
$$
\begin{array}{c|c}
x&\text{three nonzero signs}\\ \hline
0&(1,\delta,\delta)\\
1&(1,1,1)\\
3&(\delta,1,\delta)\\
-3&(\delta,1,\delta).
\end{array}
\tag{14}
$$
Hence all three remaining signs are equal at all four exceptional points when $\delta=1$, and only at $x=1$ when $\delta=-1$. The total exceptional contribution to subtract is therefore
$$
\frac{5+3\delta}{4}.
\tag{15}
$$

Let $A(p)$ denote the number of $x$ for which the four Legendre symbols are all $+1$ or all $-1$. Using (11), (13), and (15),
$$
\boxed{
A(p)
=
\frac{p-17-6\delta-2\delta u}{8}.
}
\tag{16}
$$

Step 4: Count the $2$-residue/$2$-nonresidue patterns

Among the $p-4$ nonexceptional values of $x$, the product
$$
s_1s_2s_3s_4
$$
is $+1$ exactly when the number of nonresidues is even. Therefore the number of nonexceptional $x$ with product $+1$ is
$$
\frac12\bigl((p-4)+Q_p\bigr)
=
\frac{p-5-2\delta u}{2}.
\tag{17}
$$
These points split into the all-equal points counted by $A(p)$ and the points with exactly two residues and two nonresidues.

Let $B(p)$ denote the latter count. Subtracting (16) from (17),
$$
\boxed{
B(p)
=
\frac{3\bigl(p-1+2\delta-2\delta u\bigr)}8.
}
\tag{18}
$$

Thus the exact pair is
$$
\boxed{
\left(
A(p),B(p)
\right)
=
\left(
\frac{p-17-6\delta-2\delta u}{8},
\frac{3(p-1+2\delta-2\delta u)}8
\right).
}
$$

---

## Answer

Let
$$
\delta=\left(\frac3p\right),
$$
and let $u$ be the unique odd integer for which
$$
p=u^2+v^2
$$
with $v>0$ even and
$$
u\equiv1\pmod4.
$$
Then
$$
\boxed{
\left(A(p),B(p)\right)
=
\left(
\frac{p-17-6\delta-2\delta u}{8},
\frac{3(p-1+2\delta-2\delta u)}8
\right).
}
$$
The decisive quartic sum is
$$
\boxed{
\sum_{x\in\mathbb F_p}
\left(\frac{x(x-1)(x-3)(x+3)}p\right)
=-1-2\delta u.
}
$$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- quadratic-character pattern counts
- harmonic cross-ratio and genus-one quartic curves
- quadratic twists of the CM curve $y^2=x^3-x$
- signed Gaussian two-square parameter
- boundary corrections at branch points
