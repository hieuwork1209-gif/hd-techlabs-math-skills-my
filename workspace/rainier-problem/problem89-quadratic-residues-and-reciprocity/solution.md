## Steps

Step 1: Interpret the form as a norm and determine the class group
Let
$$
K=\mathbb Q(\sqrt{-5}),
\qquad
\mathcal O_K=\mathbb Z[\sqrt{-5}].
$$
Its discriminant is $-20$, its units are only $\pm1$, and
$$
N(x+y\sqrt{-5})=x^2+5y^2.
$$
Thus $r_m(p)$ counts elements of norm $p^m$ in $\mathcal O_K$.

We need the ideal class group of $\mathcal O_K$. For an imaginary quadratic field of discriminant $D$, every ideal class contains an integral ideal of norm at most
$$
\frac{2}{\pi}\sqrt{|D|}.
$$
For $D=-20$ this bound is less than $3$, so every class has a representative of norm $1$ or $2$.

The ideal
$$
\mathfrak q=(2,1+\sqrt{-5})
$$
has norm $2$. It is not principal, because a principal ideal of norm $2$ would give an integer solution of
$$
x^2+5y^2=2,
$$
which is impossible. Hence there are exactly two ideal classes. Write the nontrivial class as $c$; then
$$
c^2=1.
$$

Step 2: Use quadratic reciprocity to determine split and inert residue classes
For an odd prime $p\ne5$, splitting in $K$ is controlled by
$$
\left(\frac{-20}{p}\right)=\left(\frac{-5}{p}\right)
=\left(\frac{-1}{p}\right)\left(\frac5p\right).
$$
Since $5\equiv1\pmod4$, quadratic reciprocity gives
$$
\left(\frac5p\right)=\left(\frac p5\right).
$$
Checking the eight possible odd residue classes modulo $20$ gives
$$
\left(\frac{-5}{p}\right)=1
\quad\Longleftrightarrow\quad
p\equiv1,3,7,9\pmod{20},
$$
and
$$
\left(\frac{-5}{p}\right)=-1
\quad\Longleftrightarrow\quad
p\equiv11,13,17,19\pmod{20}.
$$
Thus the first four classes are split and the last four are inert.

Step 3: Distinguish the two ideal classes among split primes
Suppose first that a prime ideal $\mathfrak p\mid p$ is principal. Then
$$
p=x^2+5y^2
$$
for some integers $x,y$. Since $p$ is odd, exactly one of $x,y$ is odd, so
$$
p\equiv1\pmod4.
$$
Also $p\equiv x^2\pmod5$, and $p\ne5$, so
$$
p\equiv1,4\pmod5.
$$
Hence
$$
p\equiv1,9\pmod{20}.
$$

Now suppose $\mathfrak p$ is nonprincipal. Since the class group has order $2$, the ideal $\mathfrak p\mathfrak q$ is principal. Let
$$
\mathfrak p\mathfrak q=(\alpha).
$$
Its norm is $2p$, and because $\alpha\in\mathfrak q$ we may write
$$
\alpha=2u+(1+\sqrt{-5})v.
$$
Then
$$
2p=N(\alpha)
=(2u+v)^2+5v^2
=2\left(2u^2+2uv+3v^2\right),
$$
so
$$
p=2u^2+2uv+3v^2.
$$
For this value to be odd, $v$ must be odd, and then directly modulo $4$,
$$
p\equiv3\pmod4.
$$
Because $p$ is already known to split, this forces
$$
p\equiv3,7\pmod{20}.
$$
Therefore the split primes divide into the two ideal classes as follows:
$$
\begin{array}{c|c}
p\bmod20&[\mathfrak p]\\ \hline
1,9&1,\\
3,7&c.
\end{array}
$$

Step 4: Count representations of $p^m$ in the three cases
Every solution
$$
x^2+5y^2=p^m
$$
corresponds to a principal ideal $(x+y\sqrt{-5})$ of norm $p^m$. Conversely, each such principal ideal has exactly two generators, differing by the units $\pm1$. Thus it is enough to count principal ideals of norm $p^m$ and multiply by $2$.

If $p\equiv1,9\pmod{20}$, then
$$
(p)=\mathfrak p\overline{\mathfrak p}
$$
with both prime ideals principal. The ideals of norm $p^m$ are
$$
\mathfrak p^j\overline{\mathfrak p}^{\,m-j},
\qquad 0\le j\le m,
$$
and all $m+1$ are principal. Hence
$$
r_m(p)=2(m+1).
$$

If $p\equiv3,7\pmod{20}$, then both $\mathfrak p$ and $\overline{\mathfrak p}$ have class $c$. Therefore
$$
\left[\mathfrak p^j\overline{\mathfrak p}^{\,m-j}\right]
=c^m,
$$
independently of $j$. Hence all $m+1$ ideals are principal when $m$ is even and none are principal when $m$ is odd. Thus
$$
r_m(p)=
\begin{cases}
2(m+1),&m\text{ even},\\
0,&m\text{ odd}.
\end{cases}
$$

If $p\equiv11,13,17,19\pmod{20}$, then $p$ is inert, so $(p)$ itself is prime of norm $p^2$. A principal ideal of norm $p^m$ can therefore occur only when $m=2k$, in which case the only possibility is
$$
(p)^k=(p^k).
$$
Its two generators are $\pm p^k$, so
$$
r_m(p)=
\begin{cases}
2,&m\text{ even},\\
0,&m\text{ odd}.
\end{cases}
$$

Step 5: Sum the generating functions
For $p\equiv1,9\pmod{20}$,
$$
R_p(T)=2\sum_{m\ge0}(m+1)T^m
=\frac{2}{(1-T)^2}.
$$

For $p\equiv3,7\pmod{20}$,
$$
R_p(T)=2\sum_{k\ge0}(2k+1)T^{2k}
=\frac{2(1+T^2)}{(1-T^2)^2}.
$$

For $p\equiv11,13,17,19\pmod{20}$,
$$
R_p(T)=2\sum_{k\ge0}T^{2k}
=\frac{2}{1-T^2}.
$$

Step 6: Compress the three cases for the submission field
Set
$$
a=\left(\frac{-5}{p}\right),
\qquad
b=\left(\frac{-1}{p}\right).
$$
For $p\equiv1,9\pmod{20}$ we have $(a,b)=(1,1)$; for $p\equiv3,7\pmod{20}$ we have $(a,b)=(1,-1)$; and for $p\equiv11,13,17,19\pmod{20}$ we have $a=-1$. Therefore the three rational functions above combine to
$$
R_p(T)=\frac{2+(1+a)(1+b)T+2aT^2}{(1-T^2)^2}.
$$

Final Answer: $\boxed{R_p(T)=\frac{2+(1+a)(1+b)T+2aT^2}{(1-T^2)^2},\ a=(\frac{-5}{p}),b=(\frac{-1}{p})}$

---

## Answer

$R_p(T)=\frac{2+(1+a)(1+b)T+2aT^2}{(1-T^2)^2},\ a=(\frac{-5}{p}),b=(\frac{-1}{p})$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- quadratic reciprocity
- binary quadratic forms of discriminant $-20$
- ideal class group of $\mathbb Q(\sqrt{-5})$
- split and inert primes in quadratic fields
- prime-power representation counts
