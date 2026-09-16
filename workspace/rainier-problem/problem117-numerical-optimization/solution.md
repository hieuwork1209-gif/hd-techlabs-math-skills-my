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
\Gamma_n(p)=1-\frac12 m(p),
$$
where
$$
m(p):=\inf_{x\ne0}\frac{x^TAPA x}{x^TAx}.
$$
Hence minimizing $\Gamma_n$ is equivalent to maximizing $m(p)$.

Step 2: Derive a universal test vector and the sharp upper bound
To make the numerator
$$
x^TAPA x=(Ax)^TP(Ax)
$$
independent of the unknown probability vector, seek a positive vector $r$ for which $Ar$ is constant. Fix the scale by requiring
$$
Ar=2\mathbf{1},
$$
where $\mathbf{1}=(1,\ldots,1)^T$. With the boundary convention $r_0=r_{n+1}=0$, this is the recurrence
$$
2r_i-r_{i-1}-r_{i+1}=2.
$$
If $d_i=r_i-r_{i-1}$, then
$$
d_i-d_{i+1}=2.
$$
Thus $d_i=d_1-2(i-1)$. Since
$$
0=r_{n+1}=\sum_{i=1}^{n+1}d_i,
$$
we get $d_1=n$, and summing the differences gives the uniquely determined positive solution
$$
r_i=i(n+1-i),\qquad i=1,\ldots,n.
$$
Let
$$
S:=\sum_{i=1}^n r_i.
$$
For every probability vector $p$,
$$
r^TAPA r=(Ar)^TP(Ar)=4\mathbf{1}^TP\mathbf{1}=4,
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

Step 3: Derive the only possible sharp sampling and prove attainment
For the bound in Step 2 to be sharp at a positive probability vector, $r$ must minimize the generalized Rayleigh quotient at value $2/S$. If
$$
q(x)=\frac{x^TAPA x}{x^TAx},
$$
then differentiating $q(r+th)$ at $t=0$ in every direction $h$ gives the necessary stationarity equation
$$
APA r=\frac{2}{S}Ar.
$$
Using $Ar=2\mathbf{1}$, this becomes
$$
Ap=\frac{2}{S}\mathbf{1}=\frac1S Ar.
$$
Since $A$ is invertible, sharpness forces
$$
p_i^*=\frac{r_i}{S},
\qquad
P_*=\operatorname{diag}(p_1^*,\ldots,p_n^*).
$$
It remains to prove that this candidate actually attains the bound.

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
For any $u\in\mathbb R^n$, consider
$$
\sum_{i=1}^{n-1}r_i r_{i+1}
\left(\frac{u_i}{r_i}-\frac{u_{i+1}}{r_{i+1}}\right)^2.
$$
Expanding gives the cross-term $-2\sum_{i=1}^{n-1}u_i u_{i+1}$, while the coefficient of $u_i^2$ is
$$
\frac{r_{i-1}+r_{i+1}}{r_i}
=2-\frac{2}{r_i},
$$
where $r_0=r_{n+1}=0$ and the last equality is the recurrence from Step 2. Therefore
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
and
$$
\Gamma_n(p^*)=1-\frac1S.
$$

Step 4: Close the uniqueness argument including boundary distributions
If some $p_i=0$, then $P$ is singular, so $APA$ is singular and $m(p)=0$. Such a distribution cannot be optimal because Step 3 gives $m(p^*)=2/S>0$.

If instead every $p_i>0$ and $p$ is optimal, then the universal bound from Step 2 must be sharp. The sharpness calculation in Step 3 forces $p_i=r_i/S$ for every $i$. Therefore $p^*$ is the unique minimizing probability vector.

Step 5: Evaluate the normalization and state the optimum
Using
$$
\sum_{i=1}^n i=\frac{n(n+1)}{2},
\qquad
\sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}{6},
$$
we obtain
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
