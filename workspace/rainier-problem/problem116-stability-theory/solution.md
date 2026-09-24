## Steps

Step 1: Compute the two possible period maps
Write
$$
A_i=-\alpha I+N_i,
$$
where $E_{ij}$ denotes the matrix unit with a single $1$ in position $(i,j)$, and $N_1=E_{12}$, $N_2=E_{23}$, $N_3=E_{31}$. Since $N_i^2=0$,
$$
e^{tA_i}=e^{-\alpha t}(I+tN_i).
$$
Fix a period $T>0$ and dwell times $x,y,z\geq0$ with $x+y+z=T$. For the order $A_1,A_2,A_3$, the period map is
$$
\Phi_+=e^{-\alpha T}M_+,
\qquad
M_+=(I+zE_{31})(I+yE_{23})(I+xE_{12}),
$$
so
$$
M_+=
\begin{pmatrix}
1&x&0\\
0&1&y\\
z&xz&1
\end{pmatrix}.
$$
For the reverse order $A_3,A_2,A_1$,
$$
\Phi_-=e^{-\alpha T}M_-,
\qquad
M_-=(I+xE_{12})(I+yE_{23})(I+zE_{31}),
$$
and
$$
M_-=
\begin{pmatrix}
1+xyz&x&xy\\
yz&1&y\\
z&0&1
\end{pmatrix}.
$$
For any fixed choice, the solution at times $nT$ is obtained by powers of the corresponding period map. In finite dimension, Jordan form gives exponential decay of these powers exactly when the spectral radius is less than $1$. The transition on the compact interval $[0,T]$ is bounded, so the periodic system is exponentially stable exactly under the same condition.

Step 2: Compare the two orderings at fixed dwell product
Set $q=xyz$ and $L=\lambda-1$. Expanding along the first row gives
$
\det(\lambda I-M_+)
=L(L^2-q)-q
=L^3-q(L+1)
=(\lambda-1)^3-q\lambda,
$
while
$
\det(\lambda I-M_-)
=(L-q)L^2-q(L+1)-qL
=L^3-q(L+1)^2
=(\lambda-1)^3-q\lambda^2.
$
If $q=0$, both matrices have spectral radius $1$. Assume $q>0$. Then $x,y,z>0$, both matrices are nonnegative, and their positive entries coming from $x,y,z$ contain the directed three-cycle, so both are irreducible. The Perron-Frobenius theorem gives a positive eigenvalue equal to the spectral radius.

For $\lambda>1$, define
$$
f_+(\lambda)=\frac{(\lambda-1)^3}{\lambda},
\qquad
f_-(\lambda)=\frac{(\lambda-1)^3}{\lambda^2}.
$$
Their logarithmic derivatives are
$$
\frac{f_+'(\lambda)}{f_+(\lambda)}
=\frac{2\lambda+1}{\lambda(\lambda-1)}>0,
$$
$$
\frac{f_-'(\lambda)}{f_-(\lambda)}
=\frac{\lambda+2}{\lambda(\lambda-1)}>0.
$$
Both Perron roots therefore increase with $q$. Also $f_-(\lambda)<f_+(\lambda)$ for every $\lambda>1$, so for the same $q>0$ the reverse-order Perron root is larger. The reverse order is always the worse of the two.

Step 3: Optimize the dwell times for a fixed period
For fixed $T$,
$$
xyz\leq\left(\frac{x+y+z}{3}\right)^3
=\frac{T^3}{27},
$$
with equality exactly at
$$
x=y=z=\frac{T}{3}.
$$
By Step 2, the largest period-map spectral radius for this $T$ is therefore attained by the reverse order with equal dwell times. Let its unscaled Perron root be $\lambda_T>1$. It satisfies
$$
(\lambda_T-1)^3
=\frac{T^3}{27}\lambda_T^2.
$$
The largest logarithmic growth rate per unit time at period $T$ is
$$
-\alpha+\frac{\log\lambda_T}{T}.
$$

Step 4: Optimize over the period length
The relation in Step 3 is equivalent to
$$
T=\frac{3(\lambda_T-1)}{\lambda_T^{2/3}}.
$$
Its derivative with respect to $\lambda_T$ is
$
\frac{\lambda_T+2}{\lambda_T^{5/3}}>0.
$
The right side therefore increases from $0$ to $\infty$ for $\lambda_T>1$, so every $T>0$ corresponds to exactly one $\lambda_T>1$. Put
$$
s=\log\lambda_T.
$$
Then
$$
\frac{\log\lambda_T}{T}
=
h(s):=
\frac{s e^{2s/3}}{3(e^s-1)},
\qquad s>0.
$$
This function satisfies
$$
\lim_{s\to0^+}h(s)=\frac{1}{3},
\qquad
\lim_{s\to\infty}h(s)=0.
$$
Moreover the sign of $h'(s)$ is the sign of
$$
F(s)=(3-s)e^s-(3+2s).
$$
Differentiating $\log h$ gives
$
\frac{h'(s)}{h(s)}
=
\frac{1}{s}+\frac{2}{3}-\frac{e^s}{e^s-1}
=
\frac{F(s)}{3s(e^s-1)}.
$
Now
$$
F'(s)=(2-s)e^s-2,
\qquad
F''(s)=(1-s)e^s.
$$
The sign of $F''$ shows that $F'$ increases on $(0,1)$ and then decreases strictly. Since $F'(0)=0$, $F'(1)=e-2>0$, and $F'(2)=-2<0$, the function $F$ first increases and then decreases. Also $F(0)=0$ and $F(3)=-9$, so $F$ has exactly one positive zero. Therefore $h$ has a unique maximizer on $(0,\infty)$, and
$$
\max_{T>0}\frac{\log\lambda_T}{T}
=
\max_{s>0}\frac{s e^{2s/3}}{3(e^s-1)}.
$$

Step 5: State the exact stability condition
Let
$$
\beta_*=
\max_{s>0}\frac{s e^{2s/3}}{3(e^s-1)}.
$$
If $\alpha>\beta_*$, then for every period, every dwell split, and either allowed order, Steps 2 through 4 give
$$
\frac{1}{T}\log\rho(\Phi)<0.
$$
This gives $\rho(\Phi)<1$, so each corresponding periodic system is exponentially stable.

If $\alpha\leq\beta_*$, take the reverse order, the equal dwell split, and the period corresponding in Step 4 to the unique maximizer of $h$. The period map then has spectral radius at least $1$, so that periodic system is not exponentially stable. This proves both necessity and sufficiency.
Final Answer: $\boxed{\alpha>\max_{s>0}\frac{s e^{2s/3}}{3(e^s-1)}}$

---

## Answer

$\alpha>\max_{s>0}\frac{s e^{2s/3}}{3(e^s-1)}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- periodic linear systems
- monodromy matrices
- Perron-Frobenius theorem
- spectral-radius optimization
- exponential stability

---

## Black-Box Audit — no issues found
