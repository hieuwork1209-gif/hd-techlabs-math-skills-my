## Steps

Step 1: Reduce one cycle of gradient descent to a convergence polynomial
The Hessian is
$$
A=\operatorname{diag}(1,3,5,7),
$$
so $\nabla f(x)=Ax$. For
$$
p(t)=\prod_{j=0}^2(1-\alpha_j t),
$$
three successive steps give
$$
x_3=p(A)x_0.
$$
Since $A$ is diagonal,
$$
\rho(\alpha_0,\alpha_1,\alpha_2)
=\max\{|p(1)|,|p(3)|,|p(5)|,|p(7)|\}.
$$
Also $p(0)=1$. The step-size restriction is not a per-step contraction condition; what it gives directly is
$$
p(2)=\prod_{j=0}^2(1-2\alpha_j)\geq0,
$$
because every factor is nonnegative.

Step 2: Obtain a sharp lower bound from the step-size cap
Every such $p$ has degree at most $3$. Evaluating its Lagrange interpolation formula through the nodes $0,1,5,7$ at $t=2$ gives
$$
p(2)=-\frac37p(0)+\frac54p(1)+\frac14p(5)-\frac1{14}p(7).
$$
Using $p(0)=1$ and $p(2)\geq0$,
$$
\frac37
\leq
\frac54p(1)+\frac14p(5)-\frac1{14}p(7).
$$
If $\rho=\rho(\alpha_0,\alpha_1,\alpha_2)$, then
$$
\frac54p(1)+\frac14p(5)-\frac1{14}p(7)
\leq
\left(\frac54+\frac14+\frac1{14}\right)\rho
=\frac{11}{7}\rho.
$$
Hence every admissible three-step schedule satisfies
$$
\rho\geq\frac3{11}.
$$

Step 3: Determine the equality polynomial and its step sizes
Equality $\rho=3/11$ forces equality in both estimates above. Therefore
$$
p(2)=0,\qquad
p(1)=p(5)=\frac3{11},\qquad
p(7)=-\frac3{11}.
$$
Since $p(0)=1$ and $p(2)=0$, write
$$
p(t)=\left(1-\frac t2\right)(1-st+rt^2).
$$
The conditions at $t=1$ and $t=5$ become
$$
1-s+r=\frac6{11},
\qquad
1-5s+25r=-\frac2{11},
$$
so
$$
s=\frac{28}{55},\qquad r=\frac3{55}.
$$
Thus
$$
p(t)=\left(1-\frac t2\right)
\left(1-\frac{28}{55}t+\frac3{55}t^2\right)
$$
and the quadratic factor splits as
$$
\left(1-\frac{14-\sqrt{31}}{55}t\right)
\left(1-\frac{14+\sqrt{31}}{55}t\right).
$$
The three resulting step sizes are positive and admissible: $\sqrt{31}<6$ gives $(14+\sqrt{31})/55<20/55<1/2$.

Step 4: Verify the remaining eigenvalue and close the optimization
For this polynomial,
$$
p(1)=\frac3{11},\qquad
p(3)=\frac1{55},\qquad
p(5)=\frac3{11},\qquad
p(7)=-\frac3{11}.
$$
Hence its worst-case three-step contraction is exactly $3/11$, so the lower bound is attained. Moreover, equality in Step 2 fixes the convergence polynomial, hence fixes the unordered multiset of its reciprocal roots; only the order of the three steps can vary.
Final Answer: $\boxed{\left(\frac3{11},\{\frac12,\frac{14-\sqrt{31}}{55},\frac{14+\sqrt{31}}{55}\}\right)}$

---

## Answer

$\left(\frac3{11},\{\frac12,\frac{14-\sqrt{31}}{55},\frac{14+\sqrt{31}}{55}\}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- periodic gradient descent
- convergence polynomials
- worst-case spectral contraction
- Lagrange interpolation certificate
- constrained step-size optimization

---

## Black-Box Audit — no issues found
