## Steps

Step 1: Fix the signed Gaussian parameter and the basic CM trace

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

We shall use the classical CM character sum
$$
S_0:=\sum_{x\in\mathbb F_p}\chi(x^3-x).
$$
For completeness, choose a quartic character $\psi$ with $\psi^2=\chi$. Then
$$
S_0=J(\psi,\chi)+J(\overline\psi,\chi)
=2\operatorname{Re}J(\psi,\chi).
$$
If
$$
J(\psi,\chi)=A+iB\in\mathbb Z[i],
$$
the Gauss-sum norm identity gives
$$
A^2+B^2=p.
$$
For the curve
$$
E_0:\quad y^2=x^3-x,
$$
one has
$$
\#E_0(\mathbb F_p)=p+1+S_0.
$$
Because $p\equiv1\pmod8$, the argument using the full rational $2$-torsion together with a rational point of order $4$ shows
$$
8\mid \#E_0(\mathbb F_p).
$$
Hence
$$
S_0\equiv-(p+1)\pmod8,
$$
so
$$
A\equiv-1\pmod4.
$$
Comparing with the convention (1), we get $A=-u$, and therefore
$$
\boxed{S_0=-2u.}
\tag{2}
$$

Step 2: Evaluate the quartic character sum

Define
$$
Q_p
:=
\sum_{x\in\mathbb F_p}
\chi\bigl(x(x-1)(x-3)(x+3)\bigr).
\tag{3}
$$
Consider the genus-one curve
$$
C:\quad y^2=x(x-1)(x-3)(x+3).
$$
Since the quartic on the right is monic, the smooth projective model has two $\mathbb F_p$-rational points at infinity. Therefore
$$
\#C(\mathbb F_p)=p+Q_p+2.
\tag{4}
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
\tag{5}
$$
Because $p\equiv1\pmod8$, one has
$$
\chi(8)=1,
$$
and hence
$$
\chi(d)=\chi(3)=\delta.
$$
Using (2),
$$
\#E_d(\mathbb F_p)
=p+1+\delta S_0
=p+1-2\delta u.
\tag{6}
$$
Since $C$ and $E_d$ are birational smooth projective genus-one curves, their point counts agree. Comparing (4) and (6),
$$
\boxed{Q_p=-1-2\delta u.}
\tag{7}
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
\tag{8}
$$
For any distinct $a,b\in\mathbb F_p$,
$$
\sum_x\chi((x-a)(x-b))=-1.
$$
There are six pairs, so summing the right side of (8) over all $x\in\mathbb F_p$ gives the raw value
$$
\frac{p-6+Q_p}{8}.
\tag{9}
$$

We must remove the four exceptional roots, where one Legendre symbol is $0$. At such a point, the expression in (8) equals $1/2$ exactly when the remaining three nonzero signs are all equal, and is $0$ otherwise.

The remaining sign triples are
$$
\begin{array}{c|c}
x&\text{three nonzero signs}\\ \hline
0&(1,\delta,\delta)\\
1&(1,1,1)\\
3&(\delta,1,\delta)\\
-3&(\delta,1,\delta).
\end{array}
\tag{10}
$$
Hence all three remaining signs are equal at all four exceptional points when $\delta=1$, and only at $x=1$ when $\delta=-1$. The total exceptional contribution to subtract is therefore
$$
\frac{5+3\delta}{4}.
\tag{11}
$$

Let $A(p)$ denote the number of $x$ for which the four Legendre symbols are all $+1$ or all $-1$. Using (7), (9), and (11),
$$
\boxed{
A(p)
=
\frac{p-17-6\delta-2\delta u}{8}.
}
\tag{12}
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
\tag{13}
$$
These points split into the all-equal points counted by $A(p)$ and the points with exactly two residues and two nonresidues.

Let $B(p)$ denote the latter count. Subtracting (12) from (13),
$$
\boxed{
B(p)
=
\frac{3\bigl(p-1+2\delta-2\delta u\bigr)}8.
}
\tag{14}
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
