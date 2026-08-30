## Steps

Step 1: Reveal the positive moment determinant and monotonicity
For every integer $r\ge0$,
$$
\frac{r!}{(k+a)^{r+1}}
=\int_0^1 t^{k+a-1}(-\log t)^r\,dt.
$$
After summing against $(-1)^k\binom nk$,
$$
r!S_{r+1}(n,a)
=\int_0^1 t^{a-1}(1-t)^n(-\log t)^r\,dt.
$$
Thus $D_n(a)$ is the Gram determinant of $1,Y,Y^2$, where $Y=-\log t$, for the positive measure
$$
d\mu_{n,a}(t)=t^{a-1}(1-t)^n\,dt.
$$
In particular $D_n(a)>0$.

If $b>a$, then
$$
M_n(a)-M_n(b)
=\int_0^1 t^{a-1}(1-t)^n(1-t^{b-a})
\begin{pmatrix}1\\Y\\Y^2\end{pmatrix}
\begin{pmatrix}1&Y&Y^2\end{pmatrix}dt
$$
is positive definite, where $M_n(a)$ is the $3\times3$ moment matrix whose determinant is $D_n(a)$. Hence $D_n(a)$ is strictly decreasing in $a$. Also $D_n(a)\to0$ as $a\to\infty$; the divergence $D_n(a)\to\infty$ as $a\downarrow0$ follows from Step 2. Therefore the defining equation for $a_n$ has exactly one positive solution.

Step 2: Express the determinant through Beta cumulants
The total mass is
$$
S_1(n,a)=B(a,n+1)=\frac{\Gamma(a)\Gamma(n+1)}{\Gamma(n+a+1)}.
$$
Normalize $\mu_{n,a}$ to a probability measure and let $\kappa_r$ be the cumulants of $Y=-\log t$. Dividing the moment matrix by $S_1(n,a)$ gives
$$
D_n(a)=S_1(n,a)^3F_n(a),
$$
where translation $Y\mapsto Y-\mathbb EY$ is a determinant-one change of the basis $(1,Y,Y^2)$, so
$$
F_n(a)=2\kappa_2^3+\kappa_2\kappa_4-\kappa_3^2.
$$
Indeed the centered moment matrix is
$$
\begin{pmatrix}
1&0&\kappa_2\\
0&\kappa_2&\kappa_3\\
\kappa_2&\kappa_3&\kappa_4+3\kappa_2^2
\end{pmatrix}.
$$

The moment generating function is
$$
\mathbb E e^{sY}=\frac{B(a-s,n+1)}{B(a,n+1)},
$$
so, with $\psi_m$ denoting the order-$m$ polygamma function,
$$
\kappa_r=(-1)^r\bigl(\psi_{r-1}(a)-\psi_{r-1}(a+n+1)\bigr).
$$
Using
$$
\psi_1(a)=\frac1{a^2}+O(1),\qquad
\psi_2(a)=-\frac2{a^3}+O(1),\qquad
\psi_3(a)=\frac6{a^4}+O(1)
$$
as $a\downarrow0$, while the terms at $a+n+1$ stay bounded, gives
$$
\kappa_2\sim a^{-2},\qquad
\kappa_3\sim2a^{-3},\qquad
\kappa_4\sim6a^{-4}.
$$
Therefore
$$
F_n(a)\sim\frac4{a^6},\qquad
S_1(n,a)\sim\frac1a,
$$
for fixed $n$, and hence $D_n(a)\sim4a^{-9}\to\infty$ as $a\downarrow0$.

Step 3: Find the two-scale asymptotic profile
Put $L=\log n$ and let
$$
a=\frac{c}{L},
$$
where $c$ remains in a fixed compact subset of $(0,\infty)$. Stirling's formula, uniformly in this regime, gives
$$
\frac{\Gamma(n+1)}{\Gamma(n+a+1)}
=n^{-a}(1+o(1))=e^{-c}(1+o(1)),
$$
while $\Gamma(a)=a^{-1}(1+o(1))$. Thus
$$
S_1(n,a)=\frac{Le^{-c}}{c}(1+o(1)).
$$
For the cumulants, the series formulas for the polygamma functions give uniformly
$$
\kappa_2=a^{-2}(1+o(1)),\qquad
\kappa_3=2a^{-3}(1+o(1)),\qquad
\kappa_4=6a^{-4}(1+o(1)),
$$
because the corresponding terms at $n+a+1$ are $O(n^{-1})$, $O(n^{-2})$, and $O(n^{-3})$. Consequently
$$
F_n(a)=4a^{-6}(1+o(1)).
$$
Combining the two factors,
$$
\frac{D_n(c/L)}{L^9}
\longrightarrow
\Phi(c):=\frac{4e^{-3c}}{c^9},
$$
uniformly for $c$ in compact subsets of $(0,\infty)$.

Step 4: Pin down the implicit root
The function
$$
\Phi(c)=\frac{4e^{-3c}}{c^9}
$$
is continuous and strictly decreasing from $+\infty$ to $0$. Choose fixed $0<A<B$ with $\Phi(A)>1>\Phi(B)$. By the uniform limit in Step 3, for all sufficiently large $n$,
$$
D_n(A/L)>L^9>D_n(B/L).
$$
Since $D_n$ is strictly decreasing,
$$
A<a_nL<B.
$$
Thus every subsequential limit $c$ of $a_nL$ lies in $(0,\infty)$ and satisfies $\Phi(c)=1$. The solution is unique, so the whole sequence converges to the positive root of
$$
c^9e^{3c}=4.
$$
Taking ninth roots,
$$
\frac c3e^{c/3}=\frac{4^{1/9}}3.
$$
Therefore, with $W_0$ the principal Lambert $W$ function,

Final Answer: $\boxed{3W_0\!\left(\frac{4^{1/9}}3\right)}$

---

## Answer

$3W_0\!\left(\frac{4^{1/9}}3\right)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Beta-integral transform of alternating binomial sums
- positive Hankel moment determinants
- cumulants and polygamma asymptotics
- two-scale implicit asymptotics
- Lambert W inversion

---

## Black-Box Audit — no issues found

The key reductions are derived from the reciprocal-power integral and the moment generating function. The determinant is handled structurally through centering and cumulants, while existence and uniqueness of the implicit root follow from positive-definite measure ordering rather than numerical evidence.