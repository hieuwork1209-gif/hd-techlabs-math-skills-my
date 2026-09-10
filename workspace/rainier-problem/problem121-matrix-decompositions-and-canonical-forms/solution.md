## Steps

Step 1: Derive the integral block decomposition explicitly

Write $V=\mathbb Z^X$, let $A$ be the adjacency matrix of the Johnson graph on $X$, and note that
$$
L_n=3(n-3)I-A.
$$
For an $s$-subset $\beta=\{b_1<\cdots<b_s\}$ with $s\leq3$, call $\beta$ standard if $b_i\geq2i$ for every $i$, and put
$$
v_\beta=\sum_{S\in X,\ \beta\subseteq S}e_S.
$$
We first compute $L_nv_\beta$ directly. Fix $T\in X$ and put $j=|T\cap\beta|$. The coefficient of $e_T$ in $Av_\beta$ is the number of $3$-sets $S$ such that $\beta\subseteq S$ and $|S\cap T|=2$.

If $j=s$, then $\beta\subseteq T$. To obtain such an $S$, delete one of the $3-s$ elements of $T\setminus\beta$ and insert one of the $n-3$ elements outside $T$. Thus there are
$$
(3-s)(n-3)
$$
choices.

If $j=s-1$, then exactly one element of $\beta$ is missing from $T$. That missing element must be inserted, and the deleted element may be any of the
$$
3-(s-1)=4-s
$$
elements of $T\setminus\beta$. Hence there are $4-s$ choices. If $j\leq s-2$, one swap cannot make a set contain all of $\beta$, so there are no choices.

Now
$$
\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha(T)
=
\begin{cases}
s,&j=s,\\
1,&j=s-1,\\
0,&j\leq s-2.
\end{cases}
$$
Therefore
$$
Av_\beta=(4-s)\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha+
\bigl((3-s)(n-3)-s(4-s)\bigr)v_\beta,
$$
and hence
$$
L_nv_\beta=s(n+1-s)v_\beta-(4-s)\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha.\tag{1}
$$
Thus the diagonal coefficients for $s=0,1,2,3$ are exactly
$$
0,\qquad n,\qquad2(n-1),\qquad3(n-2),
$$
while the three adjacent-level coefficients before diagonalizing the inclusion maps are $3,2,1$.

We next make the integral basis reduction explicit. Let $\mu_s$ be the number of standard $s$-subsets, with $\mu_{-1}=0$. A subset is standard exactly when, in every initial segment $\{1,\ldots,t\}$, it contains at most as many chosen positions as unchosen positions. Reflecting the characteristic word up to the first initial segment where this inequality fails gives a bijection from nonstandard $s$-subsets to $(s-1)$-subsets. Hence
$$
\mu_s=\binom ns-\binom n{s-1}.\tag{2}
$$
In particular,
$$
\sum_{s=0}^3\mu_s=\binom n3.
$$
The usual parenthesis matching gives an integral containment basis: scan a characteristic word from left to right and pair each chosen position with the nearest unpaired earlier unchosen position. The paired chosen positions form a standard lower member, and changing the unpaired positions from unchosen to chosen gives a symmetric chain. Ordering by these lower members makes the containment-change matrices unitriangular, so all basis changes have determinant $\pm1$.

For $0\leq i<j\leq3$, let $W_{i,j}$ be the $0$-$1$ matrix whose rows and columns are indexed by standard $i$- and $j$-subsets, with entry $1$ when the row subset is contained in the column subset. In the same chain bases these inclusion matrices are simultaneously diagonal: on a chain whose second-stage lower rank is $t$, the coefficient is
$$
\binom{j-t}{i-t},
$$
because the $t$ fixed elements are already present and one chooses the remaining $i-t$ elements from the $j-t$ free positions. The number of such chains is $\mu_t-\mu_{t-1}$. Therefore the three adjacent inclusion maps have diagonal forms
$$
W_{0,1}\sim[1],
$$
$$
W_{1,2}\sim\operatorname{diag}\bigl(2,1^{\,\mu_1-\mu_0}\bigr),
$$
$$
W_{2,3}\sim\operatorname{diag}\bigl(3,2^{\,\mu_1-\mu_0},1^{\,\mu_2-\mu_1}\bigr),
$$
with zero columns appended where necessary. Because the same chain bases are used at every level, these three diagonalizations are compatible with one another in (1).

Now group coordinates by $t$. For $t=0$, the adjacent coefficients in (1) are
$$
3\cdot1=3,\qquad2\cdot2=4,\qquad1\cdot3=3,
$$
which gives the $4\times4$ block $M_0$. For $t=1$ they are
$$
2\cdot1=2,\qquad1\cdot2=2,
$$
which gives $M_1$. For $t=2$ the only adjacent coefficient is $1\cdot1=1$, giving $M_2$, and for $t=3$ there is only the scalar diagonal block $M_3$. Changing signs of rows removes the minus signs in (1), so $L_n$ is integrally equivalent to
$$
M_0\oplus M_1^{\oplus(\mu_1-\mu_0)}\oplus M_2^{\oplus(\mu_2-\mu_1)}\oplus M_3^{\oplus(\mu_3-\mu_2)},
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
Finally, using (2),
$$
\mu_0-\mu_{-1}=1,
$$
$$
\mu_1-\mu_0=(n-1)-1=n-2,
$$
$$
\mu_2-\mu_1=\binom n2-2n+1=q,
$$
$$
\mu_3-\mu_2=\binom n3-2\binom n2+n=r.
$$
This proves both the four block types and their multiplicities.

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
