## Steps

Step 1: Reduce the subset-intersection matrix to four integral block types

Write $V=\mathbb Z^X$. A standard $s$-subset is a set $\beta=\{b_1<\cdots<b_s\}$ with $b_i\geq2i$. For such $\beta$ with $s\leq3$, put
$$
v_\beta=\sum_{S\in X,\ \beta\subseteq S}e_S.
$$
The vectors $v_\beta$ over all standard subsets of size at most $3$ form an integral basis of $V$. One convenient proof is the usual parenthesis matching on characteristic words: each $3$-subset lies in a unique symmetric chain whose lower member is standard, and replacing the level-$3$ basis vector of each chain by the successive containment sums is unitriangular when the chains are ordered by their lower members. Hence the change-of-basis matrix has determinant $\pm1$.

Group these chains by the size $s$ of their lower member. A direct count of neighbors of a $3$-subset shows that, on a chain starting in rank $s$, the matrix of $L_n$ has diagonal entries
$$
0,\ n,\ 2(n-1),\ 3(n-2)
$$
from ranks $0,1,2,3$, and superdiagonal entries $3,4,3$ with the initial entries omitted according to $s$. Row sign changes do not affect Smith form, so $L_n$ is integrally equivalent to
$$
M_0\oplus M_1^{\oplus(n-2)}\oplus M_2^{\oplus q}\oplus M_3^{\oplus r},
$$
where
$$
M_0=\begin{pmatrix}
0&3&0&0\\
0&n&4&0\\
0&0&2(n-1)&3\\
0&0&0&3(n-2)
\end{pmatrix},
$$
$$
M_1=\begin{pmatrix}
n&2&0\\
0&2(n-1)&2\\
0&0&3(n-2)
\end{pmatrix},\qquad
M_2=\begin{pmatrix}2(n-1)&1\\0&3(n-2)\end{pmatrix},
$$
$$
M_3=[3(n-2)].
$$
The multiplicities are the successive differences
$$
\binom ns-2\binom n{s-1}+\binom n{s-2},
$$
which give $1,n-2,q,r$ for $s=0,1,2,3$.

Step 2: Compute the Smith form of each small block

Because $n\equiv0\pmod{12}$, the determinantal divisors of $M_0$ are
$$
D_1=1,\qquad D_2=3,\qquad D_3=36.
$$
Indeed $D_1=1$ from the entries $3$ and $4$; the $2\times2$ minors have gcd
$$
\gcd(3,2n(n-1))=3,
$$
and the nonzero $3\times3$ minors have gcd
$$
\gcd\bigl(36,18(n-1)(n-2),6n(n-1)(n-2)\bigr)=36.
$$
Thus
$$
\operatorname{SNF}(M_0)=\operatorname{diag}(1,3,12,0).
$$

For $M_1$, every entry is even and the displayed superdiagonal entries force $D_1=2$ and $D_2=4$. Its determinant is
$$
6n(n-1)(n-2),
$$
so
$$
\operatorname{SNF}(M_1)=\operatorname{diag}(2,2,a),
\qquad a=\frac32n(n-1)(n-2)=\frac n4b.
$$
Since $M_2$ contains a unit entry,
$$
\operatorname{SNF}(M_2)=\operatorname{diag}(1,b),
\qquad b=6(n-1)(n-2),
$$
and
$$
\operatorname{SNF}(M_3)=[c],\qquad c=3(n-2).
$$

Step 3: Record the resulting cyclic decomposition

Ignoring unit factors and retaining the single free factor, Step 2 gives
$$
\operatorname{coker}L_n\cong\mathbb Z\oplus
\mathbb Z_3\oplus\mathbb Z_{12}\oplus
\mathbb Z_2^{\,2n-4}\oplus
\mathbb Z_c^{\,r}\oplus
\mathbb Z_b^{\,q}\oplus
\mathbb Z_a^{\,n-2}.
$$
This is a diagonal decomposition, but it is not yet in invariant-factor order because the $2$-primary and odd-primary factors have not been aligned.

Step 4: Recombine the primary parts in divisibility order

Since $n\equiv0\pmod{12}$,
$$
v_2(c)=1,\qquad v_2(b)=2,\qquad v_2(a)=v_2(n)\geq2.
$$
The positive $2$-primary factors therefore consist of
$$
2^{\,2n-4+r},\qquad 4^{\,q+1},\qquad
(2^{v_2(a)})^{\,n-2},
$$
where, when $v_2(a)=2$, the last family simply merges with the $4$'s.

For odd primes the factors are already nested: there are two initial $3$-parts, then $r$ copies of the odd part of $c$, then $q$ copies of the odd part of $b$, and finally $n-2$ copies of the odd part of $a$. The $2$-rank exceeds the odd-primary rank by
$$
(2n-4+r+q+1+n-2)-(2+r+q+n-2)=2n-5.
$$
Hence the first $2n-5$ nontrivial invariant factors are $2$. Aligning the remaining primary factors from smallest to largest gives
$$
6,\ 6,\ c^{\,r-1},\ 2c,\ b^{\,q},\ a^{\,n-2}.
$$
This is already a divisibility chain because
$$
2\mid6\mid c\mid2c\mid b\mid a;
$$
here $6\mid c$ since $n-2$ is even, $2c\mid b$ with quotient $n-1$, and $b\mid a$ with quotient $n/4$.

Step 5: Insert the unit and zero factors

The matrix size is $\binom n3$, and it has one zero Smith factor. The number of nontrivial finite invariant factors from Step 4 is
$$
(2n-5)+2+(r-1)+1+q+(n-2)=\binom n3-q-3.
$$
Therefore the number of unit invariant factors is $q+2$. The complete Smith normal form is
$$
I_{q+2}\oplus2I_{2n-5}\oplus6I_2\oplus cI_{r-1}\oplus[2c]\oplus bI_q\oplus aI_{n-2}\oplus[0].
$$
Final Answer: $\boxed{I_{q+2}\oplus2I_{2n-5}\oplus6I_2\oplus cI_{r-1}\oplus[2c]\oplus bI_q\oplus aI_{n-2}\oplus[0]}$

---

## Answer

$I_{q+2}\oplus2I_{2n-5}\oplus6I_2\oplus cI_{r-1}\oplus[2c]\oplus bI_q\oplus aI_{n-2}\oplus[0]$

---

## Classification

**Problem Type:** Canonicalization or normalization

**Answer Type:** Canonical form

---

## Solution Concepts

- Smith normal form
- subset-incidence bases
- determinantal divisors
- primary decomposition
- Johnson-scheme matrices

---

## Black-Box Audit — no issues found
