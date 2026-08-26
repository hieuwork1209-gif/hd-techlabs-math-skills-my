## Steps

Step 1: Encode the conic as a norm-one set
Let
$$
A=\mathbb F_p[\omega]/(\omega^2-5),
$$
with conjugation determined by $\overline\omega=-\omega$. For $z=x+y\omega$,
$$
N(z)=z\overline z=x^2-5y^2.
$$
Hence the map
$$
(x,y)\longmapsto z=x+y\omega
$$
is a bijection from $S_p$ onto
$$
G=\{z\in A^\times:N(z)=1\}.
$$
For $z\in G$, we have $\overline z=z^{-1}$, so the corresponding first coordinate is
$$
x=\frac{z+z^{-1}}2.
$$

Step 2: Determine the size of the norm-one group
Write
$$
\varepsilon=\left(\frac5p\right)\in\{1,-1\}.
$$
If $\varepsilon=1$, then $5$ is a square in $\mathbb F_p$ and
$$
A\cong\mathbb F_p\times\mathbb F_p.
$$
The norm-one elements are then of the form $(t,t^{-1})$ with $t\in\mathbb F_p^\times$, so
$$
|G|=p-1.
$$
If $\varepsilon=-1$, then
$$
A\cong\mathbb F_{p^2},
$$
and $G$ is the kernel of the field norm
$$
\mathbb F_{p^2}^\times\to\mathbb F_p^\times.
$$
Therefore
$$
|G|=\frac{p^2-1}{p-1}=p+1.
$$
Thus, in both cases,
$$
n:=|G|=p-\varepsilon.
$$
The group $G$ is cyclic: in the split case it is isomorphic to $\mathbb F_p^\times$, and in the nonsplit case it is a subgroup of the cyclic group $\mathbb F_{p^2}^\times$.

Step 3: Rewrite each factor $x-1$ in terms of $z$
The point $(1,0)$ corresponds to $z=1$. For $z\ne1$,
$$
x-1
=\frac{z+z^{-1}}2-1
=\frac{(z-1)^2}{2z}.
$$
Hence
$$
P_p
=\prod_{\substack{z\in G\\z\ne1}}\frac{(z-1)^2}{2z}
=\frac{\left(\prod_{z\ne1}(z-1)\right)^2}
{2^{n-1}\prod_{z\ne1}z}.
$$

Step 4: Evaluate the two group products
First consider
$$
Q:=\prod_{\substack{z\in G\\z\ne1}}(1-z).
$$
If $\varepsilon=-1$, then $A\cong\mathbb F_{p^2}$ and $G$ is exactly the set of roots of $T^n-1$ in the field. Differentiating at $T=1$ gives
$$
Q=n.
$$
If $\varepsilon=1$, identify
$$
G=\{(t,t^{-1}):t\in\mathbb F_p^\times\}.
$$
Then
$$
Q=
\left(
\prod_{t\ne1}(1-t),
\prod_{t\ne1}(1-t^{-1})
\right).
$$
The first component equals $p-1=n$ by differentiating $T^{p-1}-1$ at $T=1$, and inversion permutes $\mathbb F_p^\times\setminus\{1\}$, so the second component is the same. Thus again
$$
Q=n.
$$
Therefore in both cases
$$
\left(\prod_{z\ne1}(z-1)\right)^2=n^2.
$$

Also $n=p-\varepsilon$ is even. In a cyclic group of even order, all elements pair with their inverses except $1$ and the unique element of order $2$, which is $-1$. Hence
$$
\prod_{z\ne1}z=-1.
$$
Substituting these identities gives
$$
P_p=-\frac{n^2}{2^{n-1}}.
$$
Since $n=p-\varepsilon$,
$$
n\equiv-\varepsilon\pmod p,
$$
so $n^2\equiv1\pmod p$. Hence
$$
P_p=-2^{-(n-1)}.
$$

Step 5: Separate the two quadratic-residue cases
If $\varepsilon=1$, then $n=p-1$, so by Fermat's theorem
$$
2^{n-1}=2^{p-2}=2^{-1}
$$
in $\mathbb F_p$. Therefore
$$
P_p=-2.
$$
If $\varepsilon=-1$, then $n=p+1$, so
$$
2^{n-1}=2^p=2
$$
in $\mathbb F_p$. Therefore
$$
P_p=-2^{-1}.
$$
Equivalently,
$$
P_p=-2^{\left(\frac5p\right)}.
$$

Step 6: Use quadratic reciprocity to express the answer by $p\bmod 5$
Because $5\equiv1\pmod4$, quadratic reciprocity gives
$$
\left(\frac5p\right)=\left(\frac p5\right).
$$
The nonzero quadratic residues modulo $5$ are $1$ and $4$. Hence
$$
\left(\frac5p\right)=1
\quad\Longleftrightarrow\quad
p\equiv1,4\pmod5,
$$
and
$$
\left(\frac5p\right)=-1
\quad\Longleftrightarrow\quad
p\equiv2,3\pmod5.
$$
Therefore
$$
P_p=
\begin{cases}
-2, & p\equiv1,4\pmod5,\\[4pt]
-2^{-1}, & p\equiv2,3\pmod5,
\end{cases}
$$
where $2^{-1}$ denotes the inverse of $2$ in $\mathbb F_p$.

Final Answer: $\boxed{P_p=\begin{cases}-2,&p\equiv1,4\pmod5,\\-2^{-1},&p\equiv2,3\pmod5.\end{cases}}$

---

## Answer

$P_p=\begin{cases}-2,&p\equiv1,4\pmod5,\\-2^{-1},&p\equiv2,3\pmod5.\end{cases}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quadratic reciprocity
- Legendre symbols
- norm-one conics over finite fields
- cyclic multiplicative groups
- roots-of-unity product identities
