## Steps

Step 1: Derive the integral block decomposition by explicit unimodular changes of basis

Let $A$ be the adjacency matrix of the Johnson graph on the $3$-subsets $X$, so
$$
L_n=3(n-3)I-A.
$$
Call $\beta=\{b_1<\cdots<b_s\}$ standard if $b_i\geq2i$, and let $\mathcal S_s$ be the standard $s$-subsets. Reflecting the $0$-$1$ word at the first prefix with more chosen than unchosen positions gives a bijection from nonstandard $s$-subsets to $(s-1)$-subsets, hence
$$
\mu_s:=|\mathcal S_s|=\binom ns-\binom n{s-1},\qquad \mu_{-1}=0.
$$
For $0\leq k\leq3$, let $P_k(n)$ have rows indexed by all $k$-subsets $T$ and columns indexed by all standard $\beta$ with $|\beta|\leq k$, with entry $1$ when $\beta\subseteq T$. It is square because $\sum_{s=0}^k\mu_s=\binom nk$, and it is unimodular. Indeed, for $n\geq2k$, order rows and columns according as they avoid or contain $n$; then
$$
P_k(n)=\begin{pmatrix}P_k(n-1)&0\\ *&P_{k-1}(n-1)\end{pmatrix}.
$$
At the boundary $n=2k-1$, no standard $k$-subset exists. Complementing a row $T$ to $B=T^c$ gives the matrix $Q(B,\beta)=1_{\beta\cap B=\varnothing}$, and inclusion-exclusion gives
$$
Q(B,\beta)=\sum_{\gamma\subseteq\beta}(-1)^{|\gamma|}1_{\gamma\subseteq B}.
$$
Thus $Q=P_{k-1}(2k-1)U$, where, after ordering columns by size, $U$ is triangular with diagonal entries $(-1)^{|\beta|}$. Induction on $k$ and $n$ proves $\det P_k(n)=\pm1$.

Therefore the vectors
$$
v_\beta=\sum_{S\in X,\ \beta\subseteq S}e_S\qquad(\beta\text{ standard},\ |\beta|\leq3)
$$
form an integral basis of $\mathbb Z^X$. If $|\beta|=s$ and $j=|T\cap\beta|$, the coefficient of $e_T$ in $Av_\beta$ is $(3-s)(n-3)$ when $j=s$, is $4-s$ when $j=s-1$, and is $0$ otherwise. Since
$$
\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha(T)=
\begin{cases}s,&j=s,\\1,&j=s-1,\\0,&j\leq s-2,
\end{cases}
$$
we obtain
$$
L_nv_\beta=s(n+1-s)v_\beta-(4-s)\sum_{\substack{\alpha\subset\beta\\|\alpha|=s-1}}v_\alpha.
$$
Thus, in the $v_\beta$ basis, the diagonal blocks for ranks $s=0,1,2,3$ are $0,n,2(n-1),3(n-2)$, and the adjacent block from rank $s$ to rank $s-1$ is $-(4-s)W_{s-1,s}$, where $W_{i,j}(\alpha,\beta)=1_{\alpha\subseteq\beta}$ for standard subsets.

We now diagonalize these three inclusion blocks by explicit unimodular matrices. Put
$$
\mathcal A_0=\{\varnothing\},\qquad
\mathcal A_1=\mathcal A_0\cup\{\{i\}:2\leq i\leq n-1\}.
$$
Let
$$
\mathcal C_2=\{\{i,n\}:2\leq i\leq n-1\}\cup\{\{n-2,n-1\}\},
$$
$$
\mathcal B_2=\mathcal S_2\setminus\mathcal C_2,\qquad
\mathcal A_2=\mathcal A_1\cup\mathcal B_2.
$$
For $s=0,1,2$, let $E_s$ be the incidence matrix with rows $\mathcal A_s$, columns $\mathcal S_s$, and entry $1_{\alpha\subseteq\beta}$. Clearly $E_0=[1]$. For $E_1$, the singleton rows give an identity matrix on the columns $\{2\},\ldots,\{n-1\}$, and the $\varnothing$ row has all entries $1$, so $\det E_1=\pm1$. For $E_2$, order rows as $\mathcal B_2,\mathcal A_1$ and columns as $\mathcal B_2,\mathcal C_2$. The upper-left block is $I$, the upper-right block is $0$, and the lower-right block is
$$
F=\begin{pmatrix}I_{n-2}&u\\ \mathbf1^T&1\end{pmatrix},
$$
where $u$ has exactly two $1$'s, corresponding to $n-2,n-1$. Hence $\det F=1-\mathbf1^Tu=-1$, so $E_2$ is unimodular.

To construct $E_3$, first put
$$
\mathcal P=\{\beta\cup\{n\}:\beta\in\mathcal B_2\}
$$
and let $\mathcal T$ consist of
$$
\{i,n-2,n-1\}\ (2\leq i\leq n-3),\quad
\{n-2,n-1,n\},\quad
\{2,4,n-2\},\quad\{2,4,n-1\}.
$$
All these triples are standard because $n\geq12$. Set
$$
\mathcal C_3=\mathcal P\cup\mathcal T,\qquad
\mathcal B_3=\mathcal S_3\setminus\mathcal C_3,\qquad
\mathcal A_3=\mathcal A_2\cup\mathcal B_3,
$$
and let $E_3(\alpha,\beta)=1_{\alpha\subseteq\beta}$. Order rows as $\mathcal B_3,\mathcal B_2,\mathcal A_1$ and columns as $\mathcal B_3,\mathcal P,\mathcal T$. The $\mathcal B_3$ and $\mathcal B_2$ pivot blocks are identities. For each $T\in\mathcal T$, subtract the pivot column $\beta\cup\{n\}$ for every $\beta\in\mathcal B_2$ with $\beta\subset T$; this clears the $\mathcal B_2$ rows. On the remaining $\mathcal A_1$ rows, write $e_0$ for the $\varnothing$ row and $e_i$ for the row $\{i\}$. After changing column signs, the resulting $\mathcal T$ columns are
$$
e_0+e_i\ (2\leq i\leq n-3),\qquad
 e_0+e_{n-2}+e_{n-1},
$$
$$
2e_0+e_2+e_4+e_{n-2},\qquad
2e_0+e_2+e_4+e_{n-1}.
$$
Subtracting the $i=2,4$ columns from the last two gives $e_{n-2}$ and $e_{n-1}$; subtracting these from $e_0+e_{n-2}+e_{n-1}$ gives $e_0$; then subtracting $e_0$ from every $e_0+e_i$ gives $e_i$. Hence $E_3$ reduces by unimodular column operations to the identity and is unimodular.

The sets $\mathcal A_0\subset\mathcal A_1\subset\mathcal A_2\subset\mathcal A_3$ are nested. If $\alpha\in\mathcal A_{s-1}$ has size $t$, then for a standard $s$-set $\beta$ the number of standard $(s-1)$-sets $\gamma$ with $\alpha\subseteq\gamma\subseteq\beta$ is $s-t$ when $\alpha\subseteq\beta$ and $0$ otherwise. Therefore
$$
E_{s-1}W_{s-1,s}E_s^{-1}=D_{s-1,s},
$$
where the diagonal entry belonging to $\alpha$ is $s-t$. A label first appearing in $\mathcal A_t\setminus\mathcal A_{t-1}$ therefore gives one chain through ranks $t,t+1,\ldots,3$, and on that chain the superdiagonal from rank $s-1$ to rank $s$ has absolute value $(4-s)(s-t)$. Conjugating by alternating signs makes these entries positive. Hence $L_n$ is integrally equivalent to
$$
M_0\oplus M_1^{\oplus(n-2)}\oplus M_2^{\oplus q}\oplus M_3^{\oplus r},
$$
with
$$
M_0=\begin{pmatrix}0&3&0&0\\0&n&4&0\\0&0&2(n-1)&3\\0&0&0&3(n-2)\end{pmatrix},
$$
$$
M_1=\begin{pmatrix}n&2&0\\0&2(n-1)&2\\0&0&3(n-2)\end{pmatrix},\qquad
M_2=\begin{pmatrix}2(n-1)&1\\0&3(n-2)\end{pmatrix},\qquad
M_3=[3(n-2)].
$$
Indeed the chain multiplicities are
$$
|\mathcal A_0|=1,\quad |\mathcal A_1|-|\mathcal A_0|=n-2,
$$
$$
|\mathcal A_2|-|\mathcal A_1|=\mu_2-\mu_1=q,\quad
|\mathcal A_3|-|\mathcal A_2|=\mu_3-\mu_2=r.
$$

Step 2: Compute the Smith form of the four small blocks

For $M_0$, $D_1=1$ because the entries include $3$ and $4$. Modulo $3$, $M_0$ has rank at most $1$ because $n\equiv0\pmod3$, so every $2\times2$ minor is divisible by $3$. The minors using rows $1,2$ and columns $2,3$, and rows $1,3$ and columns $2,4$, are respectively $12$ and $9$; hence their common gcd is exactly $3$, so $D_2=3$.

Because the first column is zero, every nonzero $3\times3$ minor uses columns $2,3,4$. The four row choices give
$$
36,\qquad36(n-2),\qquad18(n-1)(n-2),\qquad6n(n-1)(n-2).
$$
Since $12\mid n$, each is divisible by $36$, and the first is exactly $36$. Thus $D_3=36$, so
$$
\operatorname{SNF}(M_0)=\operatorname{diag}(1,3,12,0).
$$

For $M_1$, every entry is even, an entry equals $2$, and the minor from rows $1,2$ and columns $2,3$ equals $4$. Hence $D_1=2$, $D_2=4$, and with
$$
\det M_1=6n(n-1)(n-2)
$$
we get
$$
\operatorname{SNF}(M_1)=\operatorname{diag}(2,2,a).
$$
Since $M_2$ contains a unit entry and has determinant $b=6(n-1)(n-2)$,
$$
\operatorname{SNF}(M_2)=\operatorname{diag}(1,b),\qquad
\operatorname{SNF}(M_3)=[c].
$$

Step 3: Record the cyclic decomposition

The block Smith forms in Step 2 give
$$
\operatorname{coker}L_n\cong\mathbb Z\oplus\mathbb Z_3\oplus\mathbb Z_{12}\oplus
\mathbb Z_2^{\,2n-4}\oplus\mathbb Z_c^{\,r}\oplus\mathbb Z_b^{\,q}\oplus\mathbb Z_a^{\,n-2},
$$
up to the unit factors. This is not yet invariant-factor order because the primary parts must be aligned.

Step 4: Align the primary parts in divisibility order

Since $12\mid n$,
$$
v_2(c)=1,\qquad v_2(b)=2,\qquad v_2(a)=v_2(n)\geq2.
$$
Thus the positive $2$-primary factors are $r+2n-4$ copies of $2$, $q+1$ copies of $4$, and $n-2$ copies of $2^{v_2(a)}$. The odd-primary factors, in divisibility order, are two initial $3$-parts, then $r$ copies of the odd part of $c$, then $q$ copies of the odd part of $b$, then $n-2$ copies of the odd part of $a$. The $2$-primary rank exceeds the odd-primary rank by
$$
(r+2n-4)+(q+1)+(n-2)-(2+r+q+n-2)=2n-5.
$$
Hence the first $2n-5$ nontrivial invariant factors are $2$, and aligning the rest gives
$$
6,\ 6,\ c^{\,r-1},\ 2c,\ b^{\,q},\ a^{\,n-2}.
$$
This is a divisibility chain because $6\mid c\mid2c\mid b\mid a$.

Step 5: Insert the unit and zero factors

There is one zero Smith factor. The number of nontrivial finite invariant factors from Step 4 is
$$
(2n-5)+2+(r-1)+1+q+(n-2)=\binom n3-q-3,
$$
so among the remaining $\binom n3-1$ nonzero factors there are $q+2$ units. Therefore
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
