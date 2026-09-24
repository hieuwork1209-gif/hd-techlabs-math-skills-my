## Steps

Step 1: Write the critical group presentation
Let $W_n$ have rim vertices $v_0,\ldots,v_{n-1}$ and hub $h$, with indices taken modulo $n$. Deleting the hub row and column from the Laplacian gives the reduced Laplacian
$$
Q_n=
\begin{pmatrix}
3&-1&0&\cdots&0&-1\\
-1&3&-1&\ddots&&0\\
0&-1&3&\ddots&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&-1&0\\
0&&\ddots&-1&3&-1\\
-1&0&\cdots&0&-1&3
\end{pmatrix}.
$$
The critical group is presented by generators $x_0,\ldots,x_{n-1}$ and relations
$$
3x_i-x_{i-1}-x_{i+1}=0
\qquad(i\bmod n).
$$

Each relation can be rewritten as
$$
x_{i+1}=3x_i-x_{i-1}.
$$
Introduce
$$
M=
\begin{pmatrix}
3&-1\\
1&0
\end{pmatrix}.
$$
Then
$$
\begin{pmatrix}
x_{i+1}\\
x_i
\end{pmatrix}
=
M
\begin{pmatrix}
x_i\\
x_{i-1}
\end{pmatrix}.
$$

Step 2: Reduce the presentation to two generators
Starting from $x_0,x_1$, the recurrence determines every $x_i$. After one full turn around the rim,
$$
\begin{pmatrix}
x_{n+1}\\
x_n
\end{pmatrix}
=
M^n
\begin{pmatrix}
x_1\\
x_0
\end{pmatrix}.
$$
The cyclic identifications are $x_n=x_0$ and $x_{n+1}=x_1$, so the remaining two relations are
$$
(M^n-I)
\begin{pmatrix}
x_1\\
x_0
\end{pmatrix}
=0.
$$
For $i=1,\ldots,n-2$, the relation $x_{i+1}-3x_i+x_{i-1}=0$ has coefficient $1$ on the new generator $x_{i+1}$. It can therefore be used to eliminate that generator and that relation by unimodular presentation operations. Repeating this leaves only $x_0,x_1$ and the two cyclic closure relations. This gives
$
K(W_n)\cong\operatorname{coker}(M^n-I).
$
The Smith form of $Q_n$ is therefore obtained by adjoining $n-2$ unit factors to the Smith form of $M^n-I$.

Step 3: Express the transfer matrix through Fibonacci numbers
Let $F_0=0$, $F_1=1$, and $F_{j+1}=F_j+F_{j-1}$. Two applications of the Fibonacci recurrence give
$
F_{m+2}=2F_m+F_{m-1}=3F_m-F_{m-2},
$
so in particular
$
F_{2j+2}=3F_{2j}-F_{2j-2}.
$
Using this recurrence and the case $n=1$ gives, by induction,
$$
M^n=
\begin{pmatrix}
F_{2n+2}&-F_{2n}\\
F_{2n}&-F_{2n-2}
\end{pmatrix}.
$$
Therefore
$$
M^n-I=
\begin{pmatrix}
F_{2n+2}-1&-F_{2n}\\
F_{2n}&-F_{2n-2}-1
\end{pmatrix}.
$$

Step 4: Determine the first invariant factor
The first determinantal divisor of an integer matrix is the gcd of all $1\times1$ minors, hence the gcd of its entries. Set
$$
g=\gcd(F_{2n},F_{2n-2}+1).
$$
The even-index recurrence gives
$$
F_{2n+2}-1
=
3F_{2n}-(F_{2n-2}+1).
$$
Every entry of $M^n-I$ is divisible by $g$, and every common divisor of all four entries divides both $F_{2n}$ and $F_{2n-2}+1$. The first nontrivial invariant factor is
$$
d_1=g
=
\gcd(F_{2n},F_{2n-2}+1).
$$

Step 5: Determine the determinant and the second invariant factor
Since $\det M=1$,
$$
\det(M^n-I)
=
2-\operatorname{tr}(M^n).
$$
From the formula in Step 3,
$$
\operatorname{tr}(M^n)
=
F_{2n+2}-F_{2n-2}.
$$
The sequence $F_{m+1}+F_{m-1}$ has initial values $2,1$ at $m=0,1$ and satisfies the same recurrence as the Lucas sequence. It follows that
$
L_m=F_{m+1}+F_{m-1}.
$
Also
$$
F_{m+2}-F_{m-2}
=
F_{m+1}+F_{m-1}
=
L_m.
$$
Taking $m=2n$ gives
$$
\operatorname{tr}(M^n)=L_{2n}.
$$
For $n\geq3$, $L_{2n}>2$, so
$$
|\det(M^n-I)|=L_{2n}-2.
$$

The gcd of the $2\times2$ minors is the absolute determinant, so the second determinantal divisor is $d_1d_2=|\det(M^n-I)|$. Therefore
$$
d_2
=
\frac{L_{2n}-2}{d_1}
=
\frac{L_{2n}-2}{\gcd(F_{2n},F_{2n-2}+1)}.
$$
Final Answer: $\boxed{\left(\gcd(F_{2n},F_{2n-2}+1),\frac{L_{2n}-2}{\gcd(F_{2n},F_{2n-2}+1)}\right)}$

---

## Answer

$\left(\gcd(F_{2n},F_{2n-2}+1),\frac{L_{2n}-2}{\gcd(F_{2n},F_{2n-2}+1)}\right)$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- graph critical groups
- smith normal form
- integer presentations
- transfer matrices
- fibonacci and lucas recurrences
