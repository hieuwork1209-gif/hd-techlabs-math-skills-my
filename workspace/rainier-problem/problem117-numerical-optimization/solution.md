## Steps

Step 1: Reduce three gradient steps to a cubic residual
For a symmetric positive-definite matrix $A$, the iteration
$$
x_{k+1}=(I-\alpha_kA)x_k,
\qquad k=0,1,2,
$$
gives
$$
x_3=p(A)x_0,
\qquad
p(\lambda)=\prod_{k=0}^2(1-\alpha_k\lambda).
$$
Thus $p$ has degree at most $3$ and satisfies $p(0)=1$. By the spectral theorem,
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\max_{\lambda\in[1,4]\cup[6,9]}|p(\lambda)|.
$$
Therefore any lower bound for all degree-$3$ polynomials with value $1$ at $0$ also applies to every admissible step-size triple.

Step 2: Prove the sharp minimax lower bound
Let $p$ be any polynomial of degree at most $3$ with $p(0)=1$, and put
$$
M=\max_{\lambda\in[1,4]\cup[6,9]}|p(\lambda)|.
$$
Lagrange interpolation at the four spectral points $1,3,7,9$, evaluated at $0$, gives
$$
p(0)=\frac{63}{32}p(1)-\frac{21}{16}p(3)
+\frac9{16}p(7)-\frac7{32}p(9).
$$
Hence
$$
1\le
\left(\frac{63}{32}+\frac{21}{16}+\frac9{16}+\frac7{32}\right)M
=\frac{65}{16}M,
$$
so
$$
M\ge\frac{16}{65}.
$$
Consequently
$$
R_*\ge\frac{16}{65}.
$$

Step 3: Construct the extremal cubic and recover the ordered step sizes
Consider
$$
p_*(\lambda)
=-\frac{(\lambda-5)^3-12(\lambda-5)}{65}.
$$
At the four interpolation points,
$$
p_*(1)=\frac{16}{65},\qquad
p_*(3)=-\frac{16}{65},\qquad
p_*(7)=\frac{16}{65},\qquad
p_*(9)=-\frac{16}{65}.
$$
Also
$$
p_*'(\lambda)
=-\frac{3\bigl((\lambda-5)^2-4\bigr)}{65},
$$
so the only critical points in the two spectral bands are $3$ and $7$. Since
$$
p_*(4)=-\frac{11}{65},
\qquad
p_*(6)=\frac{11}{65},
$$
we obtain
$$
\max_{\lambda\in[1,4]\cup[6,9]}|p_*(\lambda)|
=\frac{16}{65}.
$$
Thus the lower bound is attained.

Equality in the interpolation estimate of Step 2 forces the signs
$$
p(1)=\frac{16}{65},\quad
p(3)=-\frac{16}{65},\quad
p(7)=\frac{16}{65},\quad
p(9)=-\frac{16}{65}.
$$
These four values determine a unique cubic, so $p_*$ is the unique minimax residual polynomial.

Its roots are
$$
5-2\sqrt3,\qquad 5,\qquad 5+2\sqrt3.
$$
Since
$$
p_*(\lambda)=\prod_{k=0}^2(1-\alpha_k\lambda),
$$
the step sizes are the reciprocals of these roots. Imposing
$$
0<\alpha_0\le\alpha_1\le\alpha_2
$$
gives
$$
\alpha_0=\frac{1}{5+2\sqrt3}=\frac{5-2\sqrt3}{13},
\qquad
\alpha_1=\frac15,
\qquad
\alpha_2=\frac{1}{5-2\sqrt3}=\frac{5+2\sqrt3}{13}.
$$

Final Answer: $\boxed{\left(\frac{16}{65},\left(\frac{5-2\sqrt3}{13},\frac15,\frac{5+2\sqrt3}{13}\right)\right)}$

---

## Answer

$\left(\frac{16}{65},\left(\frac{5-2\sqrt3}{13},\frac15,\frac{5+2\sqrt3}{13}\right)\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- polynomial acceleration for gradient descent
- minimax interpolation certificate
- clustered spectrum with a spectral gap
