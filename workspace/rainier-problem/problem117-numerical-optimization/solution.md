## Steps

Step 1: Reduce two Richardson steps to a quadratic minimax polynomial
For a symmetric positive-definite matrix with eigenvalue $\lambda$, two Richardson steps with positive step sizes $\alpha,\beta$ multiply that eigendirection by
$$
p(\lambda)=(1-\alpha\lambda)(1-\beta\lambda)
=1-s\lambda+t\lambda^2,
$$
where
$$
s=\alpha+\beta>0,
\qquad
t=\alpha\beta>0.
$$
Hence for
$$
E_\gamma=[1,2]\cup[\gamma,6]
$$
the worst-case two-step factor is
$$
\mathcal C_\gamma(\alpha,\beta)=\max_{\lambda\in E_\gamma}|p(\lambda)|.
$$
We will compare feasible quadratic polynomials with $p(0)=1$. The following elementary alternation observation gives global optimality whenever a candidate is found. Suppose a candidate $p$ has
$$
p(x_1)=C,\qquad p(x_2)=-C,\qquad p(x_3)=C
$$
for three points $0<x_1<x_2<x_3$ in $E_\gamma$, and $|p|\leq C$ on $E_\gamma$. If another quadratic $q$ with $q(0)=1$ satisfied $|q|<C$ on $E_\gamma$, then $q-p$ would be negative at $x_1$, positive at $x_2$, and negative at $x_3$. It would therefore have a zero in each of $(x_1,x_2)$ and $(x_2,x_3)$, in addition to the zero at $0$. A nonzero polynomial of degree at most $2$ cannot have three distinct zeros. Thus such a candidate is the unique minimax polynomial among all quadratics with constant term $1$.

Step 2: Solve the regime before the spectral gap removes the interior extremum
First ignore the gap and optimize on the full interval $[1,6]$. For a convex quadratic minimax candidate, the two endpoint values must agree, so
$$
p(1)=p(6).
$$
Since $p(\lambda)=1-s\lambda+t\lambda^2$ with $t>0$, this equality forces the axis to be the midpoint
$$
\lambda_0=\frac{s}{2t}=\frac72.
$$
Write
$$
p(\lambda)=t\left(\lambda-\frac72\right)^2-C.
$$
Equal magnitude at the endpoints and at the vertex gives
$$
t\left(\frac52\right)^2-C=C,
$$
while $p(0)=1$ gives
$$
t\left(\frac72\right)^2-C=1.
$$
Solving yields
$$
C=\frac{25}{73},
\qquad
t=\frac8{73},
\qquad
s=\frac{56}{73}.
$$
Thus
$$
p_L(\lambda)=1-\frac{56}{73}\lambda+\frac8{73}\lambda^2.
$$
Its step sizes are
$$
\alpha_L=\frac{28-10\sqrt2}{73},
\qquad
\beta_L=\frac{28+10\sqrt2}{73},
$$
so the candidate is feasible. Because $p_L$ is convex, takes value $25/73$ at $1$ and $6$, and value $-25/73$ at $7/2$, it satisfies $|p_L|\leq25/73$ on all of $[1,6]$. Therefore whenever
$$
\gamma\leq\frac72,
$$
the three active points $1,7/2,6$ all lie in $E_\gamma$, and the alternation argument from Step 1 proves that $p_L$ remains the unique minimax polynomial. The first qualitative change can occur only when the moving endpoint $\gamma$ passes the stationary point $7/2$.

Step 3: Solve the gap-active regime and locate its right endpoint
Now assume $\gamma>7/2$. The vertex $7/2$ lies in the spectral gap, so the first point of the right spectral interval becomes the natural negative active point. Impose
$$
p(1)=C,
\qquad
p(\gamma)=-C,
\qquad
p(6)=C.
$$
The equality $p(1)=p(6)$ again forces the axis to be $7/2$. Solving the three displayed conditions together with $p(0)=1$ gives, with
$$
D_\gamma=6+7\gamma-\gamma^2,
$$
$$
p_M(\lambda)
=1-\frac{14}{D_\gamma}\lambda+\frac2{D_\gamma}\lambda^2,
$$
and
$$
C_M(\gamma)=\frac{7\gamma-\gamma^2-6}{6+7\gamma-\gamma^2}.
$$
For $7/2<\gamma<6$, $D_\gamma>0$, and the discriminant of the step-size equation is
$$
\left(\frac{14}{D_\gamma}\right)^2-rac8{D_\gamma}
=\frac{4(2\gamma^2-14\gamma+37)}{D_\gamma^2}>0,
$$
so $p_M$ factors with two positive Richardson step sizes.

On $[\gamma,6]$, the polynomial is increasing because its axis is $7/2<\gamma$, hence its values stay between $-C_M$ and $C_M$. On $[1,2]$ it is decreasing, so the only additional condition needed is
$$
p_M(2)\geq-C_M(\gamma).
$$
A direct simplification gives
$$
p_M(2)+C_M(\gamma)
=\frac{2(5-\gamma)(\gamma-2)}{6+7\gamma-\gamma^2}.
$$
Thus the candidate is valid exactly through
$$
\gamma\leq5.
$$
For $7/2<\gamma<5$, its alternating active points are exactly
$$
\{1,\gamma,6\},
$$
so Step 1 proves global optimality and uniqueness. At $\gamma=5$, the point $\lambda=2$ also reaches the negative level.

Step 4: Solve the final regime after the left endpoint becomes active
For $\gamma\geq5$, use the three fixed active points $1,2,6$ and impose
$$
p(1)=C,
\qquad
p(2)=-C,
\qquad
p(6)=C.
$$
Solving gives
$$
p_R(\lambda)=1-\frac78\lambda+\frac18\lambda^2,
\qquad
C_R=\frac14.
$$
The corresponding positive ordered step sizes are
$$
\alpha_R=\frac{7-\sqrt{17}}{16},
\qquad
\beta_R=\frac{7+\sqrt{17}}{16}.
$$
The axis is again $7/2$. On $[1,2]$, $p_R$ decreases from $1/4$ to $-1/4$. On the right interval it increases, and
$$
p_R(5)=-\frac14,
\qquad
p_R(6)=\frac14.
$$
Hence for every $\gamma\geq5$, the restriction to $[\gamma,6]$ also satisfies $|p_R|\leq1/4$. The active points on the open regime $5<\gamma\leq6$ are
$$
\{1,2,6\},
$$
and the alternation argument proves that $p_R$ is uniquely minimax. At $\gamma=5$, both $2$ and $5$ are active at the negative level, so the middle and final formulas meet continuously.

Step 5: Identify the two phase transitions and the active-set patterns
Step 2 shows that the interior stationary maximizer at $7/2$ remains active precisely until the moving right interval starts at that point. Step 3 shows that the moving endpoint $\gamma$ then remains active until $\gamma=5$, where the fixed point $2$ reaches the same negative extremal value. Step 4 shows that beyond this point the active triple is fixed.

Therefore the two transition values are
$$
\gamma_1=\frac72,
\qquad
\gamma_2=5,
$$
and on the three open regimes the active sets are respectively
$$
\left\{1,\frac72,6\right\},
\qquad
\{1,\gamma,6\},
\qquad
\{1,2,6\}.
$$

Final Answer: $\boxed{\left(\frac{7}{2},5,\left\{1,\frac{7}{2},6\right\},\{1,\gamma,6\},\{1,2,6\}\right)}$

---

## Answer

$\left(\frac{7}{2},5,\left\{1,\frac{7}{2},6\right\},\{1,\gamma,6\},\{1,2,6\}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonstationary Richardson iteration
- minimax polynomial tuning
- spectral gap phase transition
- equioscillation certificate
- worst-case contraction
