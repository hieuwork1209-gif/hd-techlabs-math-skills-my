## Steps

Step 1: Reduce the wheel relations and track the marked divisor
Let the rim generators be $x_0,\ldots,x_{n-1}$, with indices modulo $n$. Deleting the hub from the Laplacian gives the relations
$$
3x_i-x_{i-1}-x_{i+1}=0.
$$
Thus
$$
x_{i+1}=3x_i-x_{i-1}.
$$
With
$$
M=
\begin{pmatrix}
3&-1\\
1&0
\end{pmatrix},
$$
the recurrence becomes
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

Since the reduced Laplacian is symmetric, its column quotient may be read from the same integer row relations. Starting from $x_0,x_1$, the relations with indices $1,\ldots,n-2$ eliminate $x_2,\ldots,x_{n-1}$ by unimodular presentation operations. The two cyclic closure relations are
$$
(M^n-I)
\begin{pmatrix}
x_1\\
x_0
\end{pmatrix}
=0.
$$
Therefore the row lattice of $R_n=M^n-I$ presents the critical group in the basis $x_1,x_0$.

Let $F_0=0$, $F_1=1$, and $F_{j+1}=F_j+F_{j-1}$. The even-indexed Fibonacci numbers satisfy
$$
F_{2j+2}=3F_{2j}-F_{2j-2},
$$
so induction gives
$$
M^m=
\begin{pmatrix}
F_{2m+2}&-F_{2m}\\
F_{2m}&-F_{2m-2}
\end{pmatrix}.
$$
The same recurrence gives
$$
x_k=F_{2k}x_1-F_{2k-2}x_0.
$$
Hence the class $\delta_k=[e_k-e_0]$ is represented in the basis $x_1,x_0$ by
$$
v_k=
\begin{pmatrix}
F_{2k}\\
-(F_{2k-2}+1)
\end{pmatrix}.
$$

Step 2: Identify the row lattice when $n$ is odd
For $m\geq2$, set
$$
c_m=\gcd(F_{2m},F_{2m-2}+1).
$$
Since
$$
R_m=
\begin{pmatrix}
F_{2m+2}-1&-F_{2m}\\
F_{2m}&-(F_{2m-2}+1)
\end{pmatrix}
$$
and
$$
F_{2m+2}-1=3F_{2m}-(F_{2m-2}+1),
$$
the gcd of all entries of $R_m$ is exactly $c_m$.

The Fibonacci addition identity
$
F_{a+b}=F_{a-1}F_b+F_aF_{b+1}
$
follows by fixing $a$ and observing that both sides satisfy the same recurrence in $b$ with the same values at $b=0,1$. Also the sequence
$
D_r=F_{r+1}F_{r-2}-F_rF_{r-1}
$
satisfies $D_{r+1}=-D_r$ and $D_3=1$, so
$
D_r=(-1)^{r+1}.
$
Since $L_m=F_{m-1}+F_{m+1}$ by the Lucas recurrence and its initial values, the addition identity gives
$
F_{2m}=F_mL_m,
\qquad
F_{2m-2}=F_{m-1}L_{m-1}.
$
For odd $m$,
$
F_{m-2}L_m-F_{2m-2}
=
F_{m+1}F_{m-2}-F_mF_{m-1}
=
1,
$
while for even $m$,
$
F_mL_{m-2}-F_{2m-2}
=
F_mF_{m-3}-F_{m-1}F_{m-2}
=
1.
$
Therefore
$
F_{2m-2}+1=
\begin{cases}
F_{m-2}L_m,&m\text{ odd},\\
F_mL_{m-2},&m\text{ even}.
\end{cases}
$
Also $\gcd(F_m,F_{m-2})=1$ by the Fibonacci recurrence, while the Lucas recurrence gives
$$
\gcd(L_m,L_{m-2})=\gcd(L_{m-1},L_{m-2})=1.
$$
It follows that
$$
c_m=
\begin{cases}
L_m,&m\text{ odd},\\
F_m,&m\text{ even}.
\end{cases}
$$

Now assume $n$ is odd. Every entry of $R_n$ is divisible by $L_n$. Since $\det M=1$,
$$
\det(R_n)=2-\operatorname{tr}(M^n).
$$
From the matrix formula,
$
\operatorname{tr}(M^n)
=
F_{2n+2}-F_{2n-2}
=
F_{2n+1}+F_{2n-1}
=
L_{2n}.
$
The Lucas addition identity
$
L_{a+b}=L_aL_b-(-1)^bL_{a-b}
$
is proved by the same recurrence argument as the Fibonacci addition identity. Taking $a=b=n$ gives
$
L_{2n}=L_n^2-2(-1)^n.
$
Therefore
$$
|\det(R_n)|=L_n^2.
$$
Thus $R_n=L_nU_n$ for an integer matrix $U_n$ with $|\det U_n|=1$. Its row lattice is
$$
L_n\mathbb Z^2.
$$
Hence, in the basis $x_1,x_0$,
$$
K(W_n)\cong(\mathbb Z/L_n\mathbb Z)^2.
$$

Step 3: Convert the element order to a gcd
In $(\mathbb Z/L_n\mathbb Z)^2$, the order of a vector $(a,b)$ is
$$
\frac{L_n}{\gcd(L_n,a,b)}.
$$
Applying this to $v_k$ from Step 1 gives
$$
\operatorname{ord}(\delta_k)
=
\frac{L_n}
{\gcd(L_n,F_{2k},F_{2k-2}+1)}
=
\frac{L_n}{\gcd(c_n,c_k)}.
$$
The last equality uses $c_n=L_n$ because $n$ is odd and the definition of $c_k$.

Step 4: Prove the gcd compatibility for the transfer matrices
Let
$$
d=\gcd(n,k).
$$
The monic polynomials $t^n-1$ and $t^k-1$ have monic gcd $t^d-1$. Euclidean division by monic polynomials stays inside $\mathbb Z[t]$, so the extended Euclidean algorithm gives $A(t),B(t)\in\mathbb Z[t]$ such that
$$
t^d-1=A(t)(t^n-1)+B(t)(t^k-1).
$$
Evaluating at $M$ gives
$$
R_d=A(M)R_n+B(M)R_k.
$$
Therefore every common divisor of the entries of $R_n$ and $R_k$ divides every entry of $R_d$, so
$$
\gcd(c_n,c_k)\mid c_d.
$$

Conversely, since $d\mid n$ and $d\mid k$,
$$
R_n
=
R_d\left(I+M^d+\cdots+M^{n-d}\right),
$$
and the analogous identity holds for $R_k$. Hence every entry of $R_n$ and $R_k$ is an integer linear combination of entries of $R_d$, giving
$$
c_d\mid\gcd(c_n,c_k).
$$
Thus
$$
\gcd(c_n,c_k)=c_d.
$$

Step 5: Use the oddness of $n$
Because $n$ is odd, every divisor $d$ of $n$ is odd. Step 2 therefore gives
$$
c_n=L_n,
\qquad
c_d=L_d.
$$
Substituting the equality from Step 4 into Step 3 yields
$$
\operatorname{ord}(\delta_k)
=
\frac{L_n}{L_d}
=
\frac{L_n}{L_{\gcd(n,k)}}.
$$
Final Answer: $\boxed{\frac{L_n}{L_{\gcd(n,k)}}}$

---

## Answer

$\frac{L_n}{L_{\gcd(n,k)}}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- graph critical groups
- integer presentations
- transfer matrices
- fibonacci and lucas recurrences
- polynomial bezout identity
