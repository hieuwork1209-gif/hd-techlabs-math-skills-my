## Steps

Step 1: Reduce the scale uncertainty to one effective penalty parameter
Let
$$
Q=\begin{bmatrix}1&0\\0&4\end{bmatrix},
\qquad
R=\begin{bmatrix}\frac{5}{2}&-\frac{3}{2}\\-\frac{3}{2}&\frac{5}{2}\end{bmatrix}.
$$
For a scale $\mu\in[1,4]$, the Hessians of $f_{\mu}$ and $g_{\mu}$ are $\mu Q$ and $\mu R$. If
$$
t=\frac{\rho}{\mu},
$$
then solving the proximal first-order conditions gives
$$
J_Q(t)=t(tI+Q)^{-1},
\qquad
J_R(t)=t(tI+R)^{-1}.
$$
Define the reflected proximal maps
$$
H_Q(t)=2J_Q(t)-I,
\qquad
H_R(t)=2J_R(t)-I.
$$
With $s=\theta/2$, one relaxed Douglas-Rachford step has error operator
$$
T_{t,s}=(1-s)I+sH_R(t)H_Q(t),
\qquad 0<s\leq1.
$$
Therefore
$$
\mathcal C(\rho,\theta)
=\sup_{\mu\in[1,4]}\|T_{\rho/\mu,\theta/2}\|_2,
$$
so for fixed $\rho$ the effective parameter $t$ ranges over $[\rho/4,\rho]$.

Step 2: Derive the reciprocal symmetry of the one-scale contraction
Let
$$
U=\frac{1}{\sqrt{2}}\begin{bmatrix}1&-1\\1&1\end{bmatrix},
\qquad
R=UQU^T,
$$
and set
$$
a=\frac{t-1}{t+1},
\qquad
b=\frac{t-4}{t+4},
\qquad
D=\operatorname{diag}(a,b).
$$
Then
$$
H_Q(t)=D,
\qquad
H_R(t)=UDU^T,
$$
and
$$
UDU^T=\frac{1}{2}
\begin{bmatrix}
a+b&a-b\\
a-b&a+b
\end{bmatrix}.
$$
Writing
$$
M(t)=H_R(t)H_Q(t)=UDU^TD,
$$
this multiplication gives
$$
\operatorname{tr}M(t)=\frac{(a+b)^2}{2},
\qquad
\|M(t)\|_F^2=\frac{(a^2+b^2)^2}{2},
\qquad
\det M(t)=a^2b^2.
$$
For the reciprocal parameter $t^{\vee}=4/t$,
$$
a(t^{\vee})=-b(t),
\qquad
b(t^{\vee})=-a(t),
$$
so the three displayed invariants are unchanged. Since
$$
T_{t,s}=(1-s)I+sM(t),
$$
we have
$$
\|T_{t,s}\|_F^2
=2(1-s)^2+2s(1-s)\operatorname{tr}M(t)+s^2\|M(t)\|_F^2
$$
and
$$
\det T_{t,s}
=(1-s)^2+s(1-s)\operatorname{tr}M(t)+s^2\det M(t).
$$
The squared singular values of a $2\times2$ matrix have sum $\|T\|_F^2$ and product $(\det T)^2$. Hence they are unchanged by $t\mapsto4/t$, and therefore
$$
\|T_{t,s}\|_2=\|T_{4/t,s}\|_2.
$$

Step 3: Prove a sharp lower bound outside the balanced interval
Assume first that $0<t\leq1$. From the matrix in Step 2,
$$
M(t)e_2
=\frac{b}{2}
\begin{bmatrix}
a-b\\
a+b
\end{bmatrix}
=:m.
$$
Thus
$$
\|m\|_2^2=\frac{b^2(a^2+b^2)}{2},
\qquad
m_2=\frac{b(a+b)}{2}.
$$
For
$$
v(s)=T_{t,s}e_2=(1-s)e_2+sm,
$$
the function $\|v(s)\|_2^2$ is convex in $s$. At $s=1$ its derivative divided by $2$ is
$$
\begin{aligned}
\|m\|_2^2-m_2
&=\frac{b}{2}\left(b(a^2+b^2)-(a+b)\right)\\
&=-\frac{t(t-4)(13t^3+19t^2-16t-112)}{(t+1)^2(t+4)^4}.
\end{aligned}
$$
For $0<t\leq1$,
$$
13t^3+19t^2-16t-112
\leq13+19-112<0,
$$
so the displayed derivative is negative. Because the derivative of a convex quadratic is increasing, $\|v(s)\|_2$ decreases throughout $0<s\leq1$. Hence
$$
\|T_{t,s}\|_2\geq\|T_{t,s}e_2\|_2\geq\|M(t)e_2\|_2.
$$
On $(0,1]$ the quantities
$$
|a|=\frac{1-t}{1+t},
\qquad
|b|=\frac{4-t}{4+t}
$$
are both decreasing in $t$. Therefore
$$
\|M(t)e_2\|_2^2
=\frac{b^2(a^2+b^2)}{2}
\geq\frac{81}{1250},
$$
with equality only at $t=1$. Thus
$$
\|T_{t,s}\|_2\geq\frac{9}{25\sqrt{2}}
$$
for $0<t\leq1$, with equality only at $(t,s)=(1,1)$. By the reciprocal symmetry from Step 2, the same bound holds for $t\geq4$, with equality only at $(t,s)=(4,1)$.

For any $\rho>0$, the uncertainty interval for $t$ is $[\rho/4,\rho]$. If $\rho\leq4$, then $\rho/4\leq1$; if $\rho\geq4$, then $\rho\geq4$. Consequently
$$
\mathcal C(\rho,\theta)\geq\frac{9}{25\sqrt{2}}.
$$
Equality in this robust lower bound can occur only when
$$
\rho=4,
\qquad
s=1,
$$
that is, only when $\rho=4$ and $\theta=2$.

Step 4: Show that the balanced parameters control every uncertain scale
Set
$$
\rho=4,
\qquad
\theta=2.
$$
Then $s=1$ and, as $\mu$ ranges over $[1,4]$,
$$
t=\frac{4}{\mu}\in[1,4].
$$
Now $T_{t,1}=M(t)$, so
$$
\|T_{t,1}\|_2\leq\|M(t)\|_F
=\frac{a^2+b^2}{\sqrt{2}}.
$$
Substituting the displayed $a$ and $b$ gives
$$
a^2+b^2
=\frac{(t-1)^2(t+4)^2+(t-4)^2(t+1)^2}{(t+1)^2(t+4)^2}
=\frac{2(t^4+t^2+16)}{(t+1)^2(t+4)^2}.
$$
Subtracting from $9/25$ and factoring yields
$$
\frac{9}{25}-(a^2+b^2)
=-\frac{(t-1)(t-4)(41t^2+115t+164)}{25(t+1)^2(t+4)^2}.
$$
For $1\leq t\leq4$, the right-hand side is nonnegative. Therefore
$$
\|T_{t,1}\|_2\leq\frac{9}{25\sqrt{2}}
$$
for every uncertain scale. Combined with Step 3,
$$
\mathcal C(4,2)=\frac{9}{25\sqrt{2}}.
$$

Step 5: State the unique robustly optimal parameters
Step 3 gives the global lower bound and shows that equality forces $\rho=4$ and $\theta=2$. Step 4 proves that this pair attains the bound for the whole uncertainty interval. Hence the minimizing pair is unique.

Final Answer: $\boxed{\left(4,2,\frac{9}{25\sqrt{2}}\right)}$

---

## Answer

$\left(4,2,\frac{9}{25\sqrt{2}}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- robust parameter tuning
- relaxed Douglas-Rachford splitting
- reciprocal parameter symmetry
- singular values and matrix norms
- equality-case uniqueness
