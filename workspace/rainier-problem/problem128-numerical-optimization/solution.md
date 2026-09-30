## Steps

Step 1: Write the Douglas-Rachford iteration matrix
Let
$$
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
\frac{11}{2}&-\frac{7}{2}\\
-\frac{7}{2}&\frac{11}{2}
\end{pmatrix}.
$$
For the quadratic functions
$$
f(x)=\frac{1}{2}x^TAx,
\qquad
g(x)=\frac{1}{2}x^TBx,
$$
the proximal maps with parameter $\gamma>0$ are
$$
J_A=(I+\gamma A)^{-1},
\qquad
J_B=(I+\gamma B)^{-1}.
$$
Their reflected proximal maps are
$$
R_A=2J_A-I=(I-\gamma A)(I+\gamma A)^{-1},
$$
$$
R_B=2J_B-I=(I-\gamma B)(I+\gamma B)^{-1}.
$$
The standard Douglas-Rachford iteration is
$$
z_{k+1}=T_\gamma z_k,
\qquad
T_\gamma=\frac{1}{2}(I+R_BR_A).
$$

For $s=\gamma$,
$$
R_A=
\begin{pmatrix}
\frac{1-s}{1+s}&0\\
0&\frac{1-4s}{1+4s}
\end{pmatrix}.
$$
Since $B$ has eigenvalues $2$ and $9$ with eigenvectors at angle $\pi/4$, direct inversion gives
$$
R_B=
\frac{1}{18s^2+11s+1}
\begin{pmatrix}
1-18s^2&7s\\
7s&1-18s^2
\end{pmatrix}.
$$
Set
$$
C_s=R_BR_A.
$$
Its trace and determinant are
$$
t(s)=
\frac{2(2s-1)(18s^2-1)}
{(s+1)(4s+1)(9s+1)},
$$
and
$$
d(s)=
\frac{(s-1)(2s-1)(4s-1)(9s-1)}
{(s+1)(2s+1)(4s+1)(9s+1)}.
$$

Step 2: Use the determinant of the Douglas-Rachford map as a lower certificate
For any $2\times2$ matrix,
$$
r(T_\gamma)^2\geq|\det T_\gamma|.
$$
Because
$$
T_\gamma=\frac{1}{2}(I+C_s),
$$
the identity
$$
\det(I+C_s)=1+\operatorname{tr}(C_s)+\det(C_s)
$$
gives
$$
\det T_\gamma
=
\frac{1+t(s)+d(s)}{4}.
$$
Substitution and simplification yield
$$
J(s):=\det T_\gamma
=
\frac{144s^4+55s^2+2}
{2(s+1)(2s+1)(4s+1)(9s+1)}.
$$
Every factor in the denominator is positive for $s>0$, and the numerator is positive, so $J(s)>0$. Therefore
$$
r(T_\gamma)\geq\sqrt{J(s)}.
$$

This lower bound becomes exact whenever $C_s$ has nonreal conjugate eigenvalues. In that case $T_\gamma$ also has nonreal conjugate eigenvalues, and their common modulus is
$$
\sqrt{\det T_\gamma}=\sqrt{J(s)}.
$$
It remains to find the global minimizer of $J$ and verify that it lies in this nonreal-eigenvalue regime.

Step 3: Reduce the scalar minimization to one polynomial
Differentiating $J$ gives
$$
J'(s)=
\frac{P(s)}
{(s+1)^2(2s+1)^2(4s+1)^2(9s+1)^2},
$$
where
$$
P(s)=
9648s^6+7128s^5-229s^4+38s^2-99s-16.
$$
The denominator is positive for $s>0$, so the sign of $J'$ is the sign of $P$.

For $0<s\leq\frac{1}{4}$,
$$
s^6\leq\frac{s^2}{256},
\qquad
s^5\leq\frac{s^2}{64}.
$$
Dropping the negative term $-229s^4$ gives
$$
P(s)
\leq
\frac{2993}{16}s^2-99s-16.
$$
The quadratic on the right is convex, so its maximum on $[0,\frac{1}{4}]$ occurs at an endpoint. Its endpoint values are
$$
-16,
\qquad
-\frac{7439}{256}.
$$
Hence
$$
P(s)<0
\qquad
\left(0<s\leq\frac{1}{4}\right).
$$

Step 4: Prove that the stationary point is unique and globally minimizing
Differentiate $P$:
$$
P'(s)=
57888s^5+35640s^4-916s^3+76s-99.
$$
Write $s=\frac{1}{4}+u$ with $u\geq0$. Expanding gives
$$
P'\left(\frac{1}{4}+u\right)
=
57888u^5+108000u^4+70904u^3+21723u^2
+\frac{26099}{8}u+\frac{1623}{16},
$$
which is positive. Thus $P$ is strictly increasing on $[\frac{1}{4},\infty)$.

Also,
$$
P\left(\frac{1}{3}\right)=-\frac{136}{27}<0,
$$
while
$$
P\left(\frac{7}{20}\right)
=
\frac{1435437}{250000}>0.
$$
Therefore $P$ has exactly one positive zero
$$
s_*\in\left(\frac{1}{3},\frac{7}{20}\right).
$$
The sign information from Step 3 and strict increase above $\frac{1}{4}$ show
$$
J'(s)<0\quad(0<s<s_*),
\qquad
J'(s)>0\quad(s>s_*).
$$
Thus $s_*$ is the unique global minimizer of $J$ over $s>0$.

Step 5: Verify equality in the determinant certificate and identify the minimizing parameter
The discriminant of the characteristic polynomial of $C_s$ is
$$
\Delta(s)=t(s)^2-4d(s)
=
\frac{4s^2(2s-1)(925s^2-58)}
{(s+1)^2(2s+1)(4s+1)^2(9s+1)^2}.
$$
For
$$
\frac{1}{3}<s_*<\frac{7}{20},
$$
one has $2s_*-1<0$. Also
$$
925s_*^2-58
>
\frac{925}{9}-58
=
\frac{403}{9}>0.
$$
Hence
$$
\Delta(s_*)<0.
$$
The eigenvalues of $C_{s_*}$ are nonreal conjugates, so the lower certificate in Step 2 is attained:
$$
r(T_{s_*})=\sqrt{J(s_*)}.
$$
Since every $\gamma>0$ satisfies
$$
r(T_\gamma)\geq\sqrt{J(\gamma)}
\geq\sqrt{J(s_*)},
$$
the unique minimizing Douglas-Rachford parameter is $\gamma=s_*$.

By the root notation in the problem statement,
$$
s_*=
\operatorname{root}\left(
9648x^6+7128x^5-229x^4+38x^2-99x-16;
\frac{1}{3},\frac{7}{20}
\right).
$$
Final Answer: $\boxed{\operatorname{root}(9648x^6+7128x^5-229x^4+38x^2-99x-16;\frac{1}{3},\frac{7}{20})}$

---

## Answer

$\operatorname{root}(9648x^6+7128x^5-229x^4+38x^2-99x-16;\frac{1}{3},\frac{7}{20})$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- Douglas-Rachford splitting
- proximal reflections
- spectral radius
- determinant lower bounds
- polynomial root isolation
