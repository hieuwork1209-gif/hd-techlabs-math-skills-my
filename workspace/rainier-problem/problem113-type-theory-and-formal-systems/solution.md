## Steps

Step 1: Encode the unsigned update as a cyclic change of basepoint

Put $N=n+1$ and form the auxiliary cyclic bit word
$$
(z_0,z_1,\ldots,z_n)=(0,b_1,\ldots,b_n).
$$
For $0\leq k<N$, define a length-$n$ word by
$$
x_i^{(k)}=z_k+z_{k+i},
\qquad 1\leq i\leq n,
$$
where the subscripts of $z$ are read modulo $N$. At $k=0$ this gives $x^{(0)}=b$. If the current word is $x^{(k)}$, then for $1\leq i<n$,
$$
x_1^{(k)}+x_{i+1}^{(k)}
=
(z_k+z_{k+1})+(z_k+z_{k+i+1})
=
z_{k+1}+z_{k+i+1}
=
x_i^{(k+1)},
$$
while
$$
x_1^{(k)}
=
z_k+z_{k+1}
=
z_{k+1}+z_k
=
x_n^{(k+1)}.
$$
Thus the unsigned part of one $T_n$ reduction sends $x^{(k)}$ to $x^{(k+1)}$. Therefore the $n+1=N$ successive reductions run once around the cyclic choices of basepoint.

Step 2: Count the two possible Hamming weights along the cycle

Let $W=|b|$. Since $z_0=0$, the cyclic word $z$ has exactly $W$ entries equal to $1$ and $N-W$ entries equal to $0$. For a basepoint with $z_k=0$, the word $x^{(k)}$ records which of the other entries differ from $0$, so
$$
|x^{(k)}|=W.
$$
For a basepoint with $z_k=1$, it records which entries differ from $1$, namely the zero entries, so
$$
|x^{(k)}|=N-W.
$$
Among the $N$ basepoints, the first case occurs $N-W$ times and the second occurs $W$ times. Hence the exact accumulated exponent is
$$
E_n(b)
=
(N-W)\binom{W}{2}
+
W\binom{N-W}{2}.
$$

Step 3: Simplify the accumulated exponent

Using the two pair counts from Step 2,
$$
\begin{aligned}
E_n(b)
&=
\frac{(N-W)W(W-1)+W(N-W)(N-W-1)}{2}\\
&=
\frac{W(N-W)(N-2)}{2}.
\end{aligned}
$$
Substituting $N=n+1$ and $W=|b|$ yields
$$
E_n(b)=\frac{(n-1)|b|(n+1-|b|)}{2}.
$$
This is an integer because it was obtained as a sum of binomial coefficients; equivalently, if $n-1$ is odd then $n+1$ is odd, so $|b|(n+1-|b|)$ is even.

Final Answer: $\boxed{\frac{(n-1)|b|(n+1-|b|)}{2}}$

---

## Answer

$\frac{(n-1)|b|(n+1-|b|)}{2}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- signed term reduction
- cyclic orbit encoding
- Hamming weight
- binary linear transformations
- combinatorial pair counting
