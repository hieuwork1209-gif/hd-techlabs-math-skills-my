## Steps

Step 1: Write the survival recursions and separate the two modes
Let
$$
a_n=mathbb P_A(Z_n>0),
\qquad
b_n=mathbb P_B(Z_n>0),
$$
where $Z_n$ is the total population in generation $n$, and the subscript records the initial type. Since survival through generation $0$ is certain,
$$
a_0=b_0=1.
$$

For a type $A$ parent, the offspring generating function is
$$
F_A(s,t)
=
\frac{1}{2}
+
\frac{3}{8}s^2
+
\frac{1}{8}t^2.
$$
For a type $B$ parent,
$$
F_B(s,t)
=
\frac{1}{2}
+
\frac{1}{4}s
+
\frac{1}{4}t^3.
$$
Thus
$$
a_{n+1}
=
1-F_A(1-a_n,1-b_n)
=
\frac{3}{4}a_n
+
\frac{1}{4}b_n
-
\frac{3}{8}a_n^2
-
\frac{1}{8}b_n^2
$$
and
$$
b_{n+1}
=
1-F_B(1-a_n,1-b_n)
=
\frac{1}{4}a_n
+
\frac{3}{4}b_n
-
\frac{3}{4}b_n^2
+
\frac{1}{4}b_n^3.
$$

The linearization at extinction is the mean offspring matrix
$
M=
\begin{pmatrix}
\frac{3}{4}&\frac{1}{4}\\
\frac{1}{4}&\frac{3}{4}
\end{pmatrix}.
$
Its eigenvectors $(1,1)$ and $(1,-1)$ have eigenvalues $1$ and $\frac{1}{2}$, respectively. This forces the Perron and stable coordinates
$
x_n=\frac{a_n+b_n}{2},
\qquad
y_n=\frac{a_n-b_n}{2}.
$
Then $a_n=x_n+y_n$ and $b_n=x_n-y_n$. Substitution gives
$$
x_{n+1}
=
x_n
-
\frac{5}{8}x_n^2
+
\frac{1}{2}x_ny_n
-
\frac{5}{8}y_n^2
+
\frac{1}{8}x_n^3
-
\frac{3}{8}x_n^2y_n
+
\frac{3}{8}x_ny_n^2
-
\frac{1}{8}y_n^3
$$
and
$$
y_{n+1}
=
\frac{1}{2}y_n
+
\frac{1}{8}x_n^2
-
x_ny_n
+
\frac{1}{8}y_n^2
-
\frac{1}{8}x_n^3
+
\frac{3}{8}x_n^2y_n
-
\frac{3}{8}x_ny_n^2
+
\frac{1}{8}y_n^3.
$$

Step 2: Establish extinction and the leading survival scale
Because $0\leq a_n,b_n\leq1$,
$$
x_n-x_{n+1}
=
\frac{3}{16}a_n^2
+
\frac{7}{16}b_n^2
-
\frac{1}{8}b_n^3.
$$
Since $b_n\leq1$,
$
x_n-x_{n+1}
\geq
\frac{3}{16}a_n^2
+
\frac{5}{16}b_n^2
\geq
\frac{3}{16}(a_n^2+b_n^2)
\geq
\frac{3}{8}x_n^2.
$
Hence $(x_n)$ decreases to some limit $L\geq0$. If $L>0$, then for all large $n$ the decrement is at least $\frac{3L^2}{16}$, contradicting convergence of $x_n$. Therefore
$$
x_n\to0.
$$
Since $|y_n|\leq x_n$, also $y_n\to0$.

From the recurrence for $y_n$ and $|y_n|\leq x_n$,
$$
y_{n+1}
=
\frac{1}{2}y_n
+
O(x_n^2).
$$
Also the recurrence for $x_n$ gives
$$
x_{n+1}=x_n+O(x_n^2),
$$
so $x_{n+1}/x_n\to1$. Therefore, with
$$
z_n=\frac{y_n}{x_n},
$$
we have
$$
z_{n+1}
=
\frac{1}{2}z_n+O(x_n).
$$
Since $|z_n|\leq1$, the recurrence implies
$
|z_{n+1}|
\leq
\left(\frac{1}{2}+o(1)\right)|z_n|+O(x_n).
$
Taking limit superior and using $x_n\to0$ gives
$
\limsup_{n\to\infty}|z_n|
\leq
\frac{1}{2}
\limsup_{n\to\infty}|z_n|,
$
so
$
z_n\to0.
$
Thus $y_n=o(x_n)$.

The $x_n$ recurrence now reduces to
$$
x_{n+1}
=
x_n
-
\frac{5}{8}x_n^2
+
o(x_n^2).
$$
Taking reciprocals,
$$
\frac{1}{x_{n+1}}
-
\frac{1}{x_n}
=
\frac{5}{8}+o(1).
$$
By Stolz-Cesaro,
$$
\frac{1/x_n}{n}\to\frac{5}{8},
$$
hence
$$
n x_n\to\frac{8}{5}.
$$

Step 3: Determine the stable-mode correction
We next sharpen $y_n=o(x_n)$ to its exact quadratic scale. The recurrence for $y_n$ can be written
$$
y_{n+1}
=
\frac{1}{2}y_n
+
\frac{1}{8}x_n^2
+
o(x_n^2),
$$
because every omitted term contains either an extra factor $x_n$ or $y_n=o(x_n)$.

Let
$$
t_n=\frac{y_n}{x_n^2}.
$$
Because $y_n=o(x_n)$ and $x_{n+1}/x_n\to1$, the exact recurrences give, for all sufficiently large $n$,
$
|t_{n+1}|
\leq
\frac{3}{4}|t_n|+C
$
for one fixed constant $C$. Iteration gives
$
|t_n|
\leq
\left(\frac{3}{4}\right)^{n-N}|t_N|+4C,
$
so $(t_n)$ is bounded. Since $x_{n+1}/x_n\to1$, division by $x_{n+1}^2$ gives
$$
t_{n+1}
=
\frac{1}{2}t_n
+
\frac{1}{8}
+
o(1).
$$
Subtracting $\frac{1}{4}$,
$$
t_{n+1}-\frac{1}{4}
=
\frac{1}{2}
\left(t_n-\frac{1}{4}\right)
+
o(1),
$$
and therefore
$$
t_n\to\frac{1}{4}.
$$
Thus
$$
y_n
\sim
\frac{1}{4}x_n^2.
$$

Since
$$
a_n-b_n=2y_n,
$$
we obtain
$$
n^2(a_n-b_n)
=
2\frac{y_n}{x_n^2}(n x_n)^2
\longrightarrow
2\cdot\frac{1}{4}\cdot\left(\frac{8}{5}\right)^2
=
\frac{32}{25}.
$$

Step 4: Extract the logarithmic correction in the Perron mode
Using $y_n=(1/4+o(1))x_n^2$ in the exact recurrence for $x_n$,
$$
\frac{1}{2}x_ny_n
=
\frac{1}{8}x_n^3+o(x_n^3),
$$
while every term containing $y_n^2$ or $x_n^2y_n$ is $O(x_n^4)$. Hence
$$
x_{n+1}
=
x_n
-
\frac{5}{8}x_n^2
+
\frac{1}{4}x_n^3
+
o(x_n^3).
$$
Put
$$
A=\frac{5}{8},
\qquad
B=\frac{1}{4}.
$$
Then
$$
x_{n+1}
=
x_n\left(1-Ax_n+Bx_n^2+o(x_n^2)\right),
$$
so
$$
\frac{1}{x_{n+1}}
-
\frac{1}{x_n}
=
A+(A^2-B)x_n+o(x_n).
$$
Here
$$
A^2-B
=
\frac{25}{64}-\frac{16}{64}
=
\frac{9}{64}.
$$

From Step 2,
$$
x_n\sim\frac{1}{An},
$$
and therefore
$$
\sum_{k=1}^{n}x_k
=
\frac{1}{A}\log n+o(\log n).
$$
Write the remainder in the reciprocal increment as $\varepsilon_nx_n$, where $\varepsilon_n\to0$. Since $x_n\sim1/(An)$,
$
\sum_{k=1}^{n}x_k
=
\frac{1}{A}\log n+o(\log n),
$
and for every fixed $N$,
$
\left|
\sum_{k=N}^{n}\varepsilon_kx_k
\right|
\leq
\sup_{k\geq N}|\varepsilon_k|
\sum_{k=N}^{n}x_k.
$
Letting first $n\to\infty$ and then $N\to\infty$ shows that the accumulated remainder is $o(\log n)$. Hence
$
\frac{1}{x_n}
=
An
+
\frac{A^2-B}{A}\log n
+
o(\log n).
$
Since
$$
\frac{A^2-B}{A}
=
\frac{9}{40},
$$
we get
$$
\frac{
\frac{1}{x_n}-\frac{5}{8}n
}{
\log n
}
\to
\frac{9}{40}.
$$

Step 5: Transfer the logarithmic correction back to survival from type A
Because
$$
a_n=x_n+y_n=x_n\left(1+t_nx_n\right)
$$
and $t_n\to1/4$,
$$
\frac{1}{a_n}
=
\frac{1}{x_n}
\frac{1}{1+t_nx_n}
=
\frac{1}{x_n}
-
t_n
+
o(1).
$$
Thus replacing $1/x_n$ by $1/a_n$ changes only a bounded term and does not affect the coefficient of $\log n$. Therefore
$$
\frac{
\frac{1}{a_n}-\frac{5}{8}n
}{
\log n
}
\to
\frac{9}{40}.
$$
Combining this with Step 3 gives the requested ordered pair.
Final Answer: $\boxed{\left(\frac{32}{25},\frac{9}{40}\right)}$

---

## Answer

$\left(\frac{32}{25},\frac{9}{40}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- multitype branching processes
- survival probability recursions
- perron and stable modes
- nonlinear asymptotic recurrences
- logarithmic correction terms
