## Steps

Step 1: Reduce the transient objective to scalar mode constraints
The Hessian is
$$
A=\operatorname{diag}(1,3,5,7),
$$
so every eigencoordinate with eigenvalue $\lambda\in\{1,3,5,7\}$ is multiplied successively by
$$
1-\alpha_0\lambda,\qquad
(1-\alpha_0\lambda)(1-\alpha_1\lambda),\qquad
\prod_{j=0}^2(1-\alpha_j\lambda).
$$
Therefore $R\leq r$ is equivalent to the three families of inequalities
$$
|1-\alpha_0\lambda|\leq \frac{14}{5}r,
$$
$$
|(1-\alpha_0\lambda)(1-\alpha_1\lambda)|\leq \frac75r,
$$
$$
\left|\prod_{j=0}^2(1-\alpha_j\lambda)\right|\leq r
$$
for all $\lambda\in\{1,3,5,7\}$.

Step 2: Prove the sharp lower bound from the two-step prefix
Assume $R\leq 3/10$ and set
$$
g(t)=(1-\alpha_0 t)(1-\alpha_1 t).
$$
Then
$$
|g(1)|,|g(3)|,|g(5)|,|g(7)|\leq \frac{21}{50}.
$$
Because $0<\alpha_0,\alpha_1\leq1/2$,
$$
g(2)=(1-2\alpha_0)(1-2\alpha_1)\geq0,
$$
and $g(1)>0$. For every quadratic $g$ with $g(0)=1$, interpolation at $1,2,7$ gives
$$
1=\frac73g(1)-\frac75g(2)+\frac1{15}g(7).
$$
Hence
$$
1\leq \frac73g(1)+\frac1{15}|g(7)|
\leq \frac73\cdot\frac{21}{50}+\frac1{15}\cdot\frac{21}{50}=1.
$$
Thus equality holds throughout, so necessarily
$$
g(1)=\frac{21}{50},\qquad g(2)=0,\qquad g(7)=\frac3{10}.
$$
Since $g(2)=0$, one of the first two step sizes is $1/2$. Writing the other as $a$ and using $g(1)=21/50$ gives
$$
\frac12(1-a)=\frac{21}{50},
$$
so
$$
a=\frac4{25}.
$$
Therefore any schedule with $R\leq3/10$ must have
$$
\{\alpha_0,\alpha_1\}=\left\{\frac4{25},\frac12\right\}.
$$

Step 3: Use the one-step transient bound to fix the order
If $\alpha_0=1/2$, then at $\lambda=7$ the one-step multiplier has magnitude
$$
|1-7\alpha_0|=\frac52,
$$
so the weighted one-step contribution is
$$
\frac5{14}\cdot\frac52=\frac{25}{28}>\frac3{10}.
$$
Hence an optimizer with $R\leq3/10$ cannot start with $1/2$. Consequently
$$
\alpha_0=\frac4{25},\qquad \alpha_1=\frac12.
$$
For this ordered pair,
$$
g(1)=\frac{21}{50},\quad g(3)=\frac{13}{50},\quad g(5)=-\frac3{10},\quad g(7)=\frac3{10},
$$
so the weighted two-step contribution is exactly
$$
\frac57\max_{\lambda}|g(\lambda)|
=\frac57\cdot\frac{21}{50}=\frac3{10}.
$$
Also the weighted one-step contribution is at most $3/10$ because
$$
\max_{\lambda\in\{1,3,5,7\}}|1-\tfrac4{25}\lambda|
=\frac{21}{25},
$$
so
$$
\frac5{14}\cdot\frac{21}{25}=\frac3{10}.
$$

Step 4: Determine the third step and attain the bound
Now let $c=\alpha_2$. The three-step multipliers at $\lambda=1$ and $\lambda=7$ are
$$
\frac{21}{50}(1-c),
\qquad
\frac3{10}(1-7c).
$$
To keep both magnitudes at most $3/10$, the first inequality gives
$$
\frac{21}{50}(1-c)\leq\frac3{10}
\quad\Longrightarrow\quad
c\geq\frac27,
$$
while the second gives
$$
\frac3{10}|1-7c|\leq\frac3{10}
\quad\Longrightarrow\quad
0\leq c\leq\frac27.
$$
Hence necessarily
$$
\alpha_2=\frac27.
$$
For
$$
\alpha_*=\left(\frac4{25},\frac12,\frac27\right),
$$
the three-step multipliers are
$$
\frac3{10},\quad -\frac{13}{350},\quad \frac9{70},\quad -\frac3{10},
$$
so the three-step contribution is $3/10$. Steps 2 and 3 already showed that the weighted one- and two-step contributions are also at most $3/10$. Therefore the lower bound is attained, and the equality argument proves uniqueness of the ordered optimizer.
Final Answer: $\boxed{\left(\frac3{10},\left(\frac4{25},\frac12,\frac27\right)\right)}$

---

## Answer

$\left(\frac3{10},\left(\frac4{25},\frac12,\frac27\right)\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- periodic gradient descent
- transient growth control
- prefix convergence polynomials
- interpolation certificates
- minimax step-size optimization

---

## Black-Box Audit — no issues found
