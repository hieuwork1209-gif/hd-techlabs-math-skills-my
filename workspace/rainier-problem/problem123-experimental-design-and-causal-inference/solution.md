## Steps

Step 1: Reduce the optimization to an exact log-determinant certificate
Let
$$
v(x)=\begin{pmatrix}1\\x\\x^2\\x^3\\x^4\end{pmatrix},\qquad M(\xi)=\int_0^1 v(x)v(x)^T\,d\xi(x).
$$
If $M(\xi)$ is singular, then $\det M(\xi)=0$, so only positive definite information matrices matter. For positive definite matrices, concavity of $\log\det$ gives
$$
\log\det M\leq \log\det M_*+\operatorname{tr}\!\left(M_*^{-1}(M-M_*)\right).
$$
Thus, for a feasible candidate $\xi_*$, define its sensitivity polynomial
$$
\phi(x)=v(x)^T M_*^{-1}v(x).
$$
Because $\operatorname{tr}(M_*^{-1}M_*)=5$, it is enough to prove an affine majorization
$$
\phi(x)\leq A+Bx\qquad(0\leq x\leq1)
$$
with $A+B/3=5$. Indeed, every feasible $\xi$ then satisfies
$$
\operatorname{tr}(M_*^{-1}M(\xi))=\int_0^1\phi(x)\,d\xi(x)
\leq A+B\int_0^1x\,d\xi(x)=5,
$$
so the concavity inequality gives $\det M(\xi)\leq\det M_*$.

Step 2: Obtain an exact five-point candidate from the stationarity equations
A positive definite polynomial-regression design needs at least five support points. For a five-atom design with distinct nodes $x_0,\ldots,x_4$ and positive weights $w_0,\ldots,w_4$, the Vandermonde factorization gives
$$
\det M=\left(\prod_{i=0}^4w_i\right)\prod_{0\leq i<j\leq4}(x_j-x_i)^2.
$$
The Lagrange multiplier equations for the two constraints $\sum w_i=1$ and $\sum w_ix_i=1/3$ therefore have the form
$$
\frac1{w_i}=A+Bx_i.
$$
Multiplying by $w_i$ and summing over the five atoms gives
$$
A+\frac{B}{3}=5.
$$
For an interior node $x_i$, differentiating the logarithm of the displayed determinant gives
$$
2\sum_{j\ne i}\frac1{x_i-x_j}=Bw_i=\frac{B}{A+Bx_i}.
$$
To construct a saturated candidate with both interval endpoints present, write
$$
p(x)=x(x-1)q(x),\qquad q(x)=x^3-Sx^2+Tx-U.
$$
At a root $r$ of $q$,
$$
\frac{p''(r)}{p'(r)}=2\sum_{x_j\ne r}\frac1{r-x_j},
$$
so the three interior stationarity equations are equivalent to
$$
q(x)\mid (A+Bx)p''(x)-Bp'(x).
$$
The three remainder coefficients are
$$
8AS-12A+7BS^2-5BS-12BT=0,
$$
$$
6AS-14AT-7BST+8BT+15BU=0,
$$
$$
-2AT+18AU+7BSU-9BU=0.
$$
The weight normalization is
$$
\frac1A+\frac1{A+B}-\frac{q'(-A/B)}{Bq(-A/B)}=1.
$$
Substitute $B=15-3A$ from $A+B/3=5$ and eliminate $T,U$ from these four equations. On the nondegenerate branch with three positive interior roots, the remaining equations reduce to
$$
S=\frac{9A^2-77A+120}{7(A^2-9A+15)},
$$
$$
A(A-3)(2A-15)^2(3A-5)=0.
$$
The value $A=0$ is impossible because $w_0=1/A$; $A=15/2$ gives $A+B=0$ and hence an impossible endpoint weight; and $A=5/3$ forces $T=0$, impossible for three positive roots because $T$ is their pairwise-product sum. Thus
$$
A=3,\qquad B=6.
$$
Substitution in the remainder equations gives
$$
(S,T,U)=\left(\frac{10}{7},\frac47,\frac{2}{35}\right).
$$
Hence set
$$
q(x)=x^3-\frac{10}{7}x^2+\frac47x-\frac{2}{35}.
$$
Equivalently, the three interior nodes are the roots in $(0,1)$ of
$$
Q(x)=35x^3-50x^2+20x-2.
$$
There are exactly three such roots because $Q$ changes sign on each of $(0,1/4)$, $(1/4,1/2)$, and $(3/4,1)$. Let them be $r_1<r_2<r_3$, and define
$$
x_0=0,\quad x_1=r_1,\quad x_2=r_2,\quad x_3=r_3,\quad x_4=1,
$$
with
$$
w_i=\frac1{3+6x_i}.
$$
The later global certificate does not assume that every optimum is saturated; this saturated calculation is only the forward construction of the candidate.

Step 3: Verify that the candidate is a feasible probability design
Since
$$
q\!\left(-\frac12\right)=-\frac{33}{40},\qquad q'\!\left(-\frac12\right)=\frac{11}{4},
$$
the logarithmic derivative identity gives
$$
\sum_{j=1}^3\frac1{r_j+1/2}=-\frac{q'(-1/2)}{q(-1/2)}=\frac{10}{3}.
$$
Therefore the total weight of the three interior nodes is
$$
\sum_{j=1}^3\frac1{3+6r_j}=\frac16\sum_{j=1}^3\frac1{r_j+1/2}=\frac59.
$$
The endpoint weights are $w_0=1/3$ and $w_4=1/9$, so all five weights sum to $1$. Also
$$
\sum_{j=1}^3\frac{r_j}{3+6r_j}
=\frac16\sum_{j=1}^3\left(1-\frac{1/2}{r_j+1/2}\right)
=\frac29.
$$
Adding the contribution $1\cdot w_4=1/9$ gives
$$
\sum_{i=0}^4w_ix_i=\frac13.
$$
Thus the discrete measure $\xi_*=\sum_{i=0}^4w_i\delta_{x_i}$ is feasible.

Step 4: Prove the global sensitivity inequality from contact multiplicities
Let $V$ be the $5\times5$ Vandermonde matrix whose $i$th column is $v(x_i)$, and let $W=\operatorname{diag}(w_0,\ldots,w_4)$. Then
$$
M_*=VWV^T.
$$
If $\ell_i(x)$ denotes the Lagrange cardinal polynomial for the five nodes, then
$$
V^{-1}v(x)=\begin{pmatrix}\ell_0(x)&\ell_1(x)&\ell_2(x)&\ell_3(x)&\ell_4(x)\end{pmatrix}^T,
$$
so
$$
\phi(x)=v(x)^TM_*^{-1}v(x)=\sum_{i=0}^4\frac{\ell_i(x)^2}{w_i}.
$$
At every support point $x_i$ this gives
$$
\phi(x_i)=\frac1{w_i}=3+6x_i.
$$
For an interior root $r_i$, only the $i$th Lagrange term contributes to the derivative at $r_i$, hence
$$
\phi'(r_i)=\frac{2\ell_i'(r_i)}{w_i}
=\frac{2}{w_i}\sum_{j\ne i}\frac1{r_i-x_j}.
$$
The stationarity equation in Step 2 makes this equal to $6$. Therefore
$$
h(x)=3+6x-\phi(x)
$$
has zeros at $0,1$ and double zeros at $r_1,r_2,r_3$. Since $\deg h\leq8$, there is a constant $C$ such that
$$
h(x)=C\,x(1-x)q(x)^2.
$$
The leading coefficient of $\phi$ is
$$
\sum_{i=0}^4\frac{1}{w_i p'(x_i)^2}>0.
$$
Thus the leading coefficient of $h$ is negative, while that of $x(1-x)q(x)^2$ is $-1$, so $C>0$. Consequently
$$
\phi(x)\leq3+6x\qquad(0\leq x\leq1).
$$
Step 1 now proves that $\xi_*$ is globally optimal among all feasible Borel probability measures.

Step 5: Evaluate the optimal determinant exactly
For the monic cubic $q$,
$$
\prod_{j=1}^3r_j=\frac{2}{35},\qquad \prod_{j=1}^3(1-r_j)=q(1)=\frac{3}{35},
$$
and
$$
\operatorname{disc}(q)=\prod_{1\leq i<j\leq3}(r_j-r_i)^2=\frac{44}{8575}.
$$
Also
$$
\prod_{j=1}^3(3+6r_j)=6^3\prod_{j=1}^3\left(r_j+\frac12\right)
=-216q\!\left(-\frac12\right)=\frac{891}{5}.
$$
Hence
$$
\prod_{i=0}^4w_i=\frac13\cdot\frac19\cdot\frac5{891}=\frac5{24057},
$$
and the squared Vandermonde product is
$$
\frac{44}{8575}\left(\frac{2}{35}\right)^2\left(\frac{3}{35}\right)^2.
$$
Therefore
$$
\det M(\xi_*)
=\frac5{24057}\cdot\frac{44}{8575}\left(\frac{2}{35}\right)^2\left(\frac{3}{35}\right)^2
=\frac{2^4}{3^5 5^5 7^7}.
$$

Final Answer: $\boxed{\frac{2^4}{3^5 5^5 7^7}}$

---

## Answer

$\frac{2^4}{3^5 5^5 7^7}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- D-optimal experimental design
- information matrices
- Vandermonde determinants
- Karush-Kuhn-Tucker conditions
- log-determinant concavity
