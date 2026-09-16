## Steps

Step 1: Express the worst-case expected decrease as a spectral minimization
Let $A=A_n$ and $P=\operatorname{diag}(p_1,\ldots,p_n)$. The path matrix is positive definite because
$$
x^TAx=x_1^2+\sum_{i=1}^{n-1}(x_i-x_{i+1})^2+x_n^2>0
$$
for every $x\ne0$.

For a fixed coordinate $i$, write $g=Ax$. Since $A_{ii}=2$,
$$
f_n(x+te_i)=f_n(x)+t g_i+t^2.
$$
Thus exact minimization along coordinate $i$ uses $t=-g_i/2$ and gives
$$
f_n(x^+)=f_n(x)-\frac{g_i^2}{4}.
$$
Taking expectation with respect to $I\sim p$,
$$
\mathbb E[f_n(x^+)\mid x]
=f_n(x)-\frac14\sum_{i=1}^n p_i(Ax)_i^2
=f_n(x)-\frac14x^TAPA x.
$$
Therefore
$$
\Gamma_n(p)
=1-\frac12 m(p),
$$
where
$$
m(p):=\inf_{x\ne0}\frac{x^TAPA x}{x^TAx}.
$$
Hence minimizing $\Gamma_n$ is equivalent to maximizing $m(p)$.

Step 2: Construct a universal sharp upper bound for $m(p)$
Define
$$
r_i=i(n+1-i),\qquad i=1,\ldots,n,
$$
and set $r_0=r_{n+1}=0$. A direct second-difference calculation gives
$$
2r_i-r_{i-1}-r_{i+1}=2
$$
for every $i=1,\ldots,n$. Thus, with $\mathbf 1=(1,\ldots,1)^T$,
$$
Ar=2\mathbf 1.
$$
Let
$$
S:=\sum_{i=1}^n r_i.
$$
For every probability vector $p$,
$$
r^TAPA r=(Ar)^TP(Ar)=4\mathbf 1^TP\mathbf 1=4,
$$
while
$$
r^TAr=2\sum_{i=1}^n r_i=2S.
$$
Testing the Rayleigh quotient at $x=r$ therefore yields
$$
m(p)\leq\frac{2}{S}
$$
for every admissible $p$. Consequently
$$
\Gamma_n(p)\geq1-\frac1S.
$$

Step 3: Show that the Poisson-weighted sampling attains the bound
Take
$$
p_i^*=\frac{r_i}{S},
\qquad
P_*=\operatorname{diag}(p_1^*,\ldots,p_n^*).
$$
Because $P_*$ is positive definite, if
$$
C=A^{1/2}P_*^{1/2},
$$
then $A^{1/2}P_*A^{1/2}=CC^T$ and $P_*^{1/2}AP_*^{1/2}=C^TC$ have the same positive eigenvalues. Hence
$$
m(p^*)=\lambda_{\min}(P_*^{1/2}AP_*^{1/2}).
$$
Now
$$
P_*^{1/2}AP_*^{1/2}-\frac{2}{S}I
=P_*^{1/2}\left(A-\operatorname{diag}\left(\frac{2}{r_1},\ldots,\frac{2}{r_n}\right)\right)P_*^{1/2}.
$$
For any $u\in\mathbb R^n$, the identity $2r_i-r_{i-1}-r_{i+1}=2$ gives
$$
u^T\left(A-\operatorname{diag}\left(\frac{2}{r_1},\ldots,\frac{2}{r_n}\right)\right)u
=
\sum_{i=1}^{n-1}r_i r_{i+1}
\left(\frac{u_i}{r_i}-\frac{u_{i+1}}{r_{i+1}}\right)^2
\geq0.
$$
Thus
$$
P_*^{1/2}AP_*^{1/2}\succeq\frac{2}{S}I,
$$
so $m(p^*)\geq2/S$. Step 2 gives the reverse inequality, hence
$$
m(p^*)=\frac2S
$$
and therefore
$$
\Gamma_n(p^*)=1-\frac1S.
$$

Step 4: Prove uniqueness of the optimal sampling distribution
If some $p_i=0$, then $P$ is singular, so $APA$ is singular and $m(p)=0$. Such a distribution cannot be optimal because $m(p^*)=2/S>0$.

Now suppose $p_i>0$ for all $i$ and $p$ is optimal. Then Step 2 must be sharp, so $r$ attains the minimum in the generalized Rayleigh quotient defining $m(p)$. Therefore
$$
APA r=\frac{2}{S}Ar.
$$
Using $Ar=2\mathbf 1$ gives
$$
2Ap=\frac{4}{S}\mathbf 1,
$$
so
$$
Ap=\frac{2}{S}\mathbf 1=\frac1S Ar.
$$
Since $A$ is invertible,
$$
p=\frac{r}{S}.
$$
Thus $p^*$ is the unique minimizer of $\Gamma_n$.

Step 5: Evaluate the normalization and state the optimum
Using the standard sums of the first $n$ integers and their squares,
$$
S
=\sum_{i=1}^n i(n+1-i)
=(n+1)\frac{n(n+1)}{2}-\frac{n(n+1)(2n+1)}{6}
=\frac{n(n+1)(n+2)}{6}.
$$
Therefore
$$
p_i^*=\frac{6i(n+1-i)}{n(n+1)(n+2)}
$$
and
$$
\Gamma_n^*=1-\frac{6}{n(n+1)(n+2)}.
$$

Final Answer: $\boxed{\left(\left(\frac{6i(n+1-i)}{n(n+1)(n+2)}\right)_{i=1}^{n},1-\frac{6}{n(n+1)(n+2)}\right)}$

---

## Answer

$\left(\left(\frac{6i(n+1-i)}{n(n+1)(n+2)}\right)_{i=1}^{n},1-\frac{6}{n(n+1)(n+2)}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- randomized coordinate descent
- generalized Rayleigh quotient
- discrete Poisson equation
- ground-state factorization
- minimax sampling
