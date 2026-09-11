## Steps

Step 1: Obtain a universal upper bound from the path geometry

For edge weights
$$
w_1,\dots,w_{n-1}\ge0,
\qquad
\sum_{i=1}^{n-1}w_i=1,
$$
let $L_w$ be the weighted path Laplacian, so for $x=(x_1,\dots,x_n)^T$,
$$
x^T L_w x
=\sum_{i=1}^{n-1}w_i(x_{i+1}-x_i)^2.
\tag{1}
$$
Since $L_w\mathbf 1=0$, its second-smallest eigenvalue has the Rayleigh characterization
$$
\lambda_2(L_w)
=\min_{\substack{x\ne0\\\sum_i x_i=0}}
\frac{\sum_{i=1}^{n-1}w_i(x_{i+1}-x_i)^2}
{\sum_{i=1}^n x_i^2}.
\tag{2}
$$

The path has a canonical affine coordinate. Put
$$
v_i=i-\frac{n+1}{2},
\qquad 1\le i\le n.
\tag{3}
$$
Then $\sum_i v_i=0$ and $v_{i+1}-v_i=1$ for every edge. Therefore, by (2),
$$
\lambda_2(L_w)
\le
\frac{\sum_{i=1}^{n-1}w_i}{\sum_{i=1}^n v_i^2}.
\tag{4}
$$
Now
$$
\sum_{i=1}^n\left(i-\frac{n+1}{2}\right)^2
=\frac{n(n^2-1)}{12},
\tag{5}
$$
so every admissible weighting satisfies
$$
\lambda_2(L_w)
\le \frac{12}{n(n^2-1)}.
\tag{6}
$$

Step 2: Let equality force the only possible optimizer

Write
$$
M:=\frac{12}{n(n^2-1)}.
\tag{7}
$$
Suppose some weighting attains the upper bound (6). Then the vector $v$ in (3) attains the minimum in the Rayleigh quotient (2). Hence $v$ must be an eigenvector:
$$
L_wv=Mv.
\tag{8}
$$

At the first vertex, (8) gives
$$
w_1(v_1-v_2)=Mv_1,
$$
so
$$
w_1=\frac{M(n-1)}2.
\tag{9}
$$
For $2\le i\le n-1$, since $v_i-v_{i-1}=1$ and $v_i-v_{i+1}=-1$,
$$
(L_wv)_i=w_{i-1}-w_i=M\left(i-\frac{n+1}{2}\right).
\tag{10}
$$
The recurrence (9)-(10) yields
$$
w_i=\frac M2\,i(n-i),
\qquad 1\le i\le n-1.
\tag{11}
$$
Substituting (7), the only possible maximizing weights are therefore
$$
w_i^*
=\frac{6i(n-i)}{n(n^2-1)}.
\tag{12}
$$
They are positive, and indeed
$$
\sum_{i=1}^{n-1}i(n-i)=\frac{n(n^2-1)}6,
$$
so the weights in (12) sum to $1$.

It remains to prove that these forced weights actually attain the bound. This is the nontrivial closure step.

Step 3: Derive the exact spectrum for the forced weighting

Let $L_0$ denote the path Laplacian with unnormalized weights
$$
a_i=i(n-i),
\qquad 1\le i\le n-1.
\tag{13}
$$
Then
$$
L_{w^*}=\frac{6}{n(n^2-1)}L_0.
\tag{14}
$$

The coefficients in (13) are quadratic in the vertex coordinate, while each first difference in the Laplacian lowers polynomial degree by one. This visibly suggests the polynomial-degree filtration as the canonical structure to test, rather than introducing an auxiliary basis by guesswork.

For $0\le k\le n-1$, let $\mathcal P_k$ be the vectors obtained by evaluating real polynomials of degree at most $k$ at the points $1,\dots,n$. These spaces form a strictly increasing flag
$$
\mathcal P_0\subset\mathcal P_1\subset\cdots\subset\mathcal P_{n-1}=\mathbb R^n.
\tag{15}
$$
For a polynomial $p$,
$$
(L_0p)(i)
=(i-1)(n-i+1)\bigl(p(i)-p(i-1)\bigr)
+i(n-i)\bigl(p(i)-p(i+1)\bigr),
\tag{16}
$$
where the first coefficient vanishes at $i=1$ and the second at $i=n$.
Thus $L_0$ preserves each $\mathcal P_k$. Moreover, if $p(i)=i^k+$ lower-degree terms, binomial expansion in (16) shows that the degree-$k$ coefficient of $L_0p$ is
$$
k(k+1).
\tag{17}
$$
Indeed, the degree-$(k+1)$ terms from the two finite differences cancel, while the surviving degree-$k$ coefficient is
$$
\frac{k(k-1)}2+k(n+2)
+\frac{k(k-1)}2-kn
=k(k+1).
$$

Equip $\mathbb R^n$ with the usual inner product. The matrix $L_0$ is symmetric. For each $k$, let $p_k$ be the monic degree-$k$ polynomial whose value vector is orthogonal to $\mathcal P_{k-1}$; this is obtained uniquely by Gram-Schmidt from $1,i,i^2,\dots$. Since $L_0\mathcal P_{k-1}\subseteq\mathcal P_{k-1}$, for every $q\in\mathcal P_{k-1}$,
$$
\langle L_0p_k,q\rangle
=\langle p_k,L_0q\rangle=0.
\tag{18}
$$
By (17), $L_0p_k$ has degree $k$ and leading coefficient $k(k+1)$. The one-dimensional orthogonal complement of $\mathcal P_{k-1}$ in $\mathcal P_k$ is spanned by $p_k$, hence
$$
L_0p_k=k(k+1)p_k.
\tag{19}
$$
Because $p_0,\dots,p_{n-1}$ form an orthogonal basis of $\mathbb R^n$, (19) gives the complete spectrum
$$
0,\ 2,\ 6,\ 12,\dots,\ n(n-1).
\tag{20}
$$
Therefore, by (14),
$$
\lambda_2(L_{w^*})
=\frac{6}{n(n^2-1)}\cdot2
=\frac{12}{n(n^2-1)}=M.
\tag{21}
$$
So the universal upper bound is attained.

Step 4: Close uniqueness and the exact optimum

Equation (21) proves existence of an optimizer. Conversely, any optimizer must make the affine test vector (3) attain equality in the Rayleigh bound (4), and hence must satisfy the eigenvector equation (8). Step 2 showed that this forces every edge weight uniquely to be (12).

Thus the maximizing weighting is unique and the optimal algebraic connectivity is exactly
$$
\max_{\substack{w_i\ge0\\\sum_{i=1}^{n-1}w_i=1}}\lambda_2(L_w)
=\frac{12}{n(n^2-1)}.
$$

## Solution Concepts

- Rayleigh-quotient upper certificate from the affine coordinate on a path.
- Equality forcing of the quadratic edge-weight profile $i(n-i)$.
- Invariant polynomial flag and exact discrete orthogonal-polynomial spectrum.

Final Answer: $\displaystyle M_n=\frac{12}{n(n^2-1)},\quad w_i^*=\frac{6i(n-i)}{n(n^2-1)}$.
