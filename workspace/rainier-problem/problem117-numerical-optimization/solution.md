## Steps

Step 1: Reduce two heavy-ball steps to a quadratic residual
For a fixed curvature $\lambda\in[1,9]$, the scalar objective is
$$
f_\lambda(x)=\frac{\lambda}{2}x^2.
$$
With $x_{-1}=x_0$ and constant parameters $\alpha>0$, $\beta\ge0$, the first step is
$$
x_1=(1-\alpha\lambda)x_0.
$$
The second step is
$$
x_2=(1+\beta-\alpha\lambda)x_1-\beta x_0,
$$
so
$$
\frac{x_2}{x_0}=q_{\alpha,\beta}(\lambda)
=1-\alpha(2+\beta)\lambda+\alpha^2\lambda^2.
$$
Hence
$$
R(\alpha,\beta)=\max_{1\le\lambda\le9}|q_{\alpha,\beta}(\lambda)|.
$$

Step 2: Prove the sharp minimax lower bound
Consider any polynomial $p$ of degree at most $2$ with $p(0)=1$, and put
$$
r(y)=p(5-4y).
$$
Then $r(5/4)=1$ and
$$
\max_{1\le\lambda\le9}|p(\lambda)|
=\max_{-1\le y\le1}|r(y)|.
$$
Define
$$
r_*(y)=\frac8{17}(2y^2-1).
$$
Since
$$
r_*\left(\frac54\right)=1,
$$
and
$$
r_*(-1)=\frac8{17},\qquad
r_*(0)=-\frac8{17},\qquad
r_*(1)=\frac8{17},
$$
we have $\|r_*\|_{L^\infty[-1,1]}=8/17$.

Suppose some admissible $r$ satisfied $\|r\|_\infty<8/17$. For $h=r-r_*$,
$$
h(-1)<0,\qquad h(0)>0,\qquad h(1)<0,
$$
while $h(5/4)=0$. Thus $h$ has one zero in $(-1,0)$, another in $(0,1)$, and a third at $5/4$, impossible for a nonzero polynomial of degree at most $2$. Therefore every $p$ with $p(0)=1$ satisfies
$$
\max_{1\le\lambda\le9}|p(\lambda)|\ge\frac8{17}.
$$

The minimizer is unique. Indeed, if $\|r\|_\infty\le8/17$ and $h=r-r_*$ is nonzero, then either $h(0)>0$, which again forces three distinct zeros, or $h(0)=0$. In the latter case the roots at $0$ and $5/4$ force
$$
h(y)=c\,y\left(y-\frac54\right).
$$
The inequalities $h(-1)\le0$ and $h(1)\le0$ imply respectively $c\le0$ and $c\ge0$, so $c=0$, a contradiction. Hence $r=r_*$.

Step 3: Recover the heavy-ball parameters
Returning to $\lambda$,
$$
p_*(\lambda)
=r_*\left(\frac{5-\lambda}{4}\right)
=\frac{\lambda^2-10\lambda+17}{17}.
$$
To realize this as the heavy-ball residual from Step 1, compare coefficients:
$$
\alpha^2=\frac1{17},
\qquad
\alpha(2+\beta)=\frac{10}{17}.
$$
Because $\alpha>0$,
$$
\alpha_*=\frac1{\sqrt{17}},
\qquad
\beta_*=\frac{10}{\sqrt{17}}-2.
$$
The momentum is feasible because $10>2\sqrt{17}$. At $\lambda=1,5,9$ the residuals are respectively
$$
\frac8{17},\qquad-\frac8{17},\qquad\frac8{17},
$$
so the bound is attained. Uniqueness of the minimax polynomial gives uniqueness of $\alpha_*$ and $\beta_*$.

Final Answer: $\boxed{\left(\frac8{17},\left(\frac1{\sqrt{17}},\frac{10}{\sqrt{17}}-2\right)\right)}$

---

## Answer

$\left(\frac8{17},\left(\frac1{\sqrt{17}},\frac{10}{\sqrt{17}}-2\right)\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- heavy-ball residual polynomial
- minimax quadratic approximation
- equioscillation sign-change argument
