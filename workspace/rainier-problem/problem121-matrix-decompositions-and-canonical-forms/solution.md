## Steps

Step 1: Construct an integral basis and reduce the incidence maps

Let $A$ be the adjacency matrix of the Johnson graph on $3$-subsets, so $L_n=3(n-3)I-A$. Call $\beta=\{b_1<\cdots<b_s\}$ standard if $b_i\geq2i$, and let $\mathcal S_s$ be the standard $s$-subsets. The usual first-bad-prefix reflection bijects nonstandard $s$-subsets with $(s-1)$-subsets, hence
$$
\mu_s:=|\mathcal S_s|=\binom ns-\binom n{s-1}.
$$
For $0\leq k\leq3$, let $P_k(n)$ have rows all $k$-subsets $T$, columns all standard $\beta$ with $|\beta|\leq k$, and entry $1_{\beta\subseteq T}$. Since $\sum_{s=0}^k\mu_s=\binom nk$, it is square. For $n\geq2k$, ordering rows and columns by whether they contain $n$ gives
$$
P_k(n)=\begin{pmatrix}P_k(n-1)&0\\ *&P_{k-1}(n-1)\end{pmatrix}.
$$
At $n=2k-1$, complementing a row $T$ to $B=T^c$ gives $Q(B,\beta)=1_{\beta\cap B=\varnothing}=\sum_{\gamma\subseteq\beta}(-1)^{|\gamma|}1_{\gamma\subseteq B}$, so $Q=P_{k-1}(2k-1)U$ with $U$ triangular and diagonal $(-1)^{|\beta|}$. Induction gives $\det P_k(n)=\pm1$.

Thus
$$
v_\beta=\sum_{S\supseteq\beta}e_S\qquad(\beta\text{ standard},\ |\beta|\leq3)
$$
forms an integral basis of $\mathbb Z^X$. If $|\beta|=s$ and $j=|T\cap\beta|$, then the coefficient of $e_T$ in $Av_\beta$ is $(3-s)(n-3)$ for $j=s$, $4-s$ for $j=s-1$, and $0$ otherwise. Since
$$
\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha(T)=s,1,0
$$
for $j=s,s-1,\leq s-2$, respectively,
$$
L_nv_\beta=s(n+1-s)v_\beta-(4-s)\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha.
$$
Hence the diagonal rank blocks are $0,n,2(n-1),3(n-2)$ and the adjacent block is $-(4-s)W_{s-1,s}$, where $W_{i,j}(\alpha,\beta)=1_{\alpha\subseteq\beta}$.

Put
$$
\mathcal A_0=\{\varnothing\},\qquad \mathcal A_1=\mathcal A_0\cup\{\{i\}:2\leq i\leq n-1\},
$$
$$
\mathcal C_2=\{\{i,n\}:2\leq i\leq n-1\}\cup\{\{n-2,n-1\}\},\quad
\mathcal B_2=\mathcal S_2\setminus\mathcal C_2,\quad \mathcal A_2=\mathcal A_1\cup\mathcal B_2.
$$
Let $E_s(\alpha,\beta)=1_{\alpha\subseteq\beta}$ for rows $\mathcal A_s$ and columns $\mathcal S_s$. Clearly $E_0$ is unimodular. For $E_1$, the singleton rows form an identity block and the $\varnothing$ row is all $1$'s. For $E_2$, ordering rows as $\mathcal B_2,\mathcal A_1$ and columns as $\mathcal B_2,\mathcal C_2$ leaves the lower-right block
$$
F=\begin{pmatrix}I_{n-2}&u\\ \mathbf1^T&1\end{pmatrix},
$$
where $u$ has two $1$'s, so $\det F=1-\mathbf1^Tu=-1$.

For $E_3$, let
$$
\mathcal P=\{\beta\cup\{n\}:\beta\in\mathcal B_2\}
$$
and let $\mathcal T$ consist of $\{i,n-2,n-1\}$ for $2\leq i\leq n-3$, together with $\{n-2,n-1,n\}$, $\{2,4,n-2\}$, and $\{2,4,n-1\}$. Put $\mathcal C_3=\mathcal P\cup\mathcal T$, $\mathcal B_3=\mathcal S_3\setminus\mathcal C_3$, and $\mathcal A_3=\mathcal A_2\cup\mathcal B_3$. Since $|\mathcal P|=|\mathcal B_2|$, $\mathcal P\cap\mathcal T=\varnothing$, and $|\mathcal T|=|\mathcal A_1|=n-1$, the matrix $E_3$ is square.

Order rows as $\mathcal B_3,\mathcal B_2,\mathcal A_1$ and columns as $\mathcal B_3,\mathcal P,\mathcal T$. The first two pivot blocks are identities. For $T\in\mathcal T$, subtract the pivot column $\beta\cup\{n\}$ for every $\beta\in\mathcal B_2$ with $\beta\subset T$. Write $e_0$ for the $\varnothing$ row and $e_j$ for the $\{j\}$ row, and set
$$
N(T)=|\{\beta\in\mathcal B_2:\beta\subset T\}|,\qquad
N_j(T)=|\{\beta\in\mathcal B_2:\beta\subset T,\ j\in\beta\}|.
$$
The reduced $T$-column on $\mathcal A_1$ is
$$
(1-N(T))e_0+\sum_{j=2}^{n-1}(1_{j\in T}-N_j(T))e_j.
$$
For $T=\{i,n-2,n-1\}$, the relevant $\mathcal B_2$ pairs are $\{i,n-2\},\{i,n-1\}$, giving $-e_0-e_i$. For $T=\{n-2,n-1,n\}$ there are none, giving $e_0+e_{n-2}+e_{n-1}$. For $T=\{2,4,n-2\}$ all three internal pairs lie in $\mathcal B_2$, giving $-2e_0-e_2-e_4-e_{n-2}$; similarly $\{2,4,n-1\}$ gives $-2e_0-e_2-e_4-e_{n-1}$. After changing the three negative column signs, subtracting the $i=2,4$ columns from the last two gives $e_{n-2},e_{n-1}$; these give $e_0$ from $e_0+e_{n-2}+e_{n-1}$, and then all $e_i$. The identity columns just obtained then clear the entries below the $\mathcal B_3$ pivots, so $E_3$ reduces to the identity and is unimodular.

For $\alpha\in\mathcal A_{s-1}$ of size $t$, the number of standard $(s-1)$-sets $\gamma$ with $\alpha\subseteq\gamma\subseteq\beta$ is $s-t$ if $\alpha\subseteq\beta$ and $0$ otherwise. Therefore $E_{s-1}W_{s-1,s}E_s^{-1}$ is diagonal with entry $s-t$ at label $\alpha$. A label first appearing in $\mathcal A_t\setminus\mathcal A_{t-1}$ gives one chain through ranks $t,\ldots,3$, with superdiagonal magnitude $(4-s)(s-t)$. Hence $L_n$ is integrally equivalent to
$$
M_0\oplus M_1^{\oplus(n-2)}\oplus M_2^{\oplus q}\oplus M_3^{\oplus r},
$$
where
$$
M_0=\begin{pmatrix}0&3&0&0\\0&n&4&0\\0&0&2(n-1)&3\\0&0&0&3(n-2)\end{pmatrix},
$$
$$
M_1=\begin{pmatrix}n&2&0\\0&2(n-1)&2\\0&0&3(n-2)\end{pmatrix},\quad
M_2=\begin{pmatrix}2(n-1)&1\\0&3(n-2)\end{pmatrix},\quad M_3=[3(n-2)].
$$
The multiplicities are $1,n-2,\mu_2-\mu_1=q,\mu_3-\mu_2=r$.

Step 2: Compute the Smith forms of the four blocks

For an integer matrix $M$ of rank $\rho$, let $D_0(M)=1$ and let $D_j(M)$ be the positive gcd of all $j\times j$ minors. Unimodular row and column operations preserve the ideal generated by these minors, hence preserve $D_j$. If the nonzero Smith factors are $d_1\mid\cdots\mid d_\rho$, then every $j\times j$ minor of the Smith diagonal is divisible by $d_1\cdots d_j$, while the minor on the first $j$ diagonal positions equals that product. Thus
$$
D_j(M)=d_1\cdots d_j,\qquad d_j=\frac{D_j(M)}{D_{j-1}(M)}.
$$

For $M_0$, $D_1=1$ because the entries include $3$ and $4$. Modulo $3$, $M_0$ has rank at most $1$ since $3\mid n$, so every $2\times2$ minor is divisible by $3$. The minors on rows $1,2$/columns $2,3$ and rows $1,3$/columns $2,4$ are $12$ and $9$, so $D_2=3$. Since the first column is zero, the nonzero $3\times3$ minors use columns $2,3,4$; the four row choices give
$$
36,\quad36(n-2),\quad18(n-1)(n-2),\quad6n(n-1)(n-2).
$$
Because $12\mid n$, all are divisible by $36$, and the first equals $36$. Hence $D_3=36$ and
$$
\operatorname{SNF}(M_0)=\operatorname{diag}(1,3,12,0).
$$
For $M_1$, every entry is even, so every $2\times2$ minor is divisible by $4$; an entry equals $2$, and the rows $1,2$/columns $2,3$ minor equals $4$. Hence $D_1=2,D_2=4$. Also $D_3=6n(n-1)(n-2)$, so
$$
\operatorname{SNF}(M_1)=\operatorname{diag}(2,2,a).
$$
Finally $M_2$ contains a unit and has determinant $b$, while $M_3=[c]$, hence
$$
\operatorname{SNF}(M_2)=\operatorname{diag}(1,b),\qquad \operatorname{SNF}(M_3)=[c].
$$

Step 3: Record the cyclic decomposition

The block Smith forms give
$$
\operatorname{coker}L_n\cong\mathbb Z\oplus\mathbb Z_3\oplus\mathbb Z_{12}\oplus\mathbb Z_2^{\,2n-4}\oplus\mathbb Z_c^{\,r}\oplus\mathbb Z_b^{\,q}\oplus\mathbb Z_a^{\,n-2},
$$
up to unit factors. These cyclic factors are not yet in invariant-factor order because their primary parts must be aligned.

Step 4: Align the primary parts

Since $12\mid n$,
$$
v_2(c)=1,\qquad v_2(b)=2,\qquad v_2(a)=v_2(n)\geq2.
$$
Thus the positive $2$-primary factors are $r+2n-4$ copies of $2$, $q+1$ copies of $4$, and $n-2$ copies of $2^{v_2(a)}$. The odd-primary factors, in divisibility order, are two initial $3$-parts, then $r$ copies of the odd part of $c$, then $q$ copies of the odd part of $b$, then $n-2$ copies of the odd part of $a$. The $2$-primary rank exceeds the odd-primary rank by
$$
(r+2n-4)+(q+1)+(n-2)-(2+r+q+n-2)=2n-5.
$$
Therefore the first $2n-5$ nontrivial invariant factors are $2$, and the rest align as
$$
6,\ 6,\ c^{\,r-1},\ 2c,\ b^{\,q},\ a^{\,n-2}.
$$
This is a divisibility chain because $6\mid c\mid2c\mid b\mid a$.

Step 5: Insert the unit and zero factors

There is one zero Smith factor. The number of nontrivial finite invariant factors from Step 4 is
$$
(2n-5)+2+(r-1)+1+q+(n-2)=\binom n3-q-3.
$$
Hence among the remaining $\binom n3-1$ nonzero factors there are $q+2$ units, giving
$$
\operatorname{SNF}(L_n)=I_{q+2}\oplus2I_{2n-5}\oplus6I_2\oplus cI_{r-1}\oplus[2c]\oplus bI_q\oplus aI_{n-2}\oplus[0].
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
- unimodular subset-incidence bases
- determinantal divisors
- primary decomposition
- Johnson graph Laplacian
