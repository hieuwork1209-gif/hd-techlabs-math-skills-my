## Steps

Step 1: Write the relaxed Douglas-Rachford error operator
Let
$$
U=\frac{1}{\sqrt{2}}\begin{bmatrix}1&-1\\1&1\end{bmatrix},
\qquad
Q_{\mu}=\begin{bmatrix}\mu&0\\0&4/\mu\end{bmatrix},
\qquad
R_{\mu}=UQ_{\mu}U^T.
$$
For a quadratic with Hessian $H$, the proximal reflection is
$$
2P_{h,\rho}-I=(\rho I-H)(\rho I+H)^{-1}.
$$
Set
$$
s=\frac{\theta}{2}\in(0,1],
\qquad
a_{\mu}=\frac{\rho-\mu}{\rho+\mu},
\qquad
b_{\mu}=\frac{\rho-4/\mu}{\rho+4/\mu},
$$
and
$$
D_{\mu}=\operatorname{diag}(a_{\mu},b_{\mu}).
$$
Then the two reflected proximal maps are $D_{\mu}$ and $UD_{\mu}U^T$, so one relaxed Douglas-Rachford step is linear with
$$
z^+=T_{\mu,\rho,s}z,
\qquad
T_{\mu,\rho,s}=(1-s)I+sUD_{\mu}U^TD_{\mu}.
$$
Therefore
$$
\mathcal C(\rho,\theta)=\sup_{\mu\in[1,4]}\|T_{\mu,\rho,\theta/2}\|_2.
$$

Step 2: Obtain a global lower bound from one endpoint of the uncertainty set
The robust supremum contains $\mu=1$. At this endpoint write
$$
a=\frac{\rho-1}{\rho+1},
\qquad
b=\frac{\rho-4}{\rho+4},
\qquad
D=\operatorname{diag}(a,b),
\qquad
M=UDU^TD.
$$
Direct multiplication gives
$$
\operatorname{tr}M=\frac{(a+b)^2}{2},
\qquad
\|M\|_F^2=\frac{(a^2+b^2)^2}{2}.
$$
For $T=(1-s)I+sM$,
$$
\frac{\|T\|_F^2}{2}
=(1-s)^2+\frac{s(1-s)}{2}(a+b)^2+\frac{s^2}{4}(a^2+b^2)^2.
$$
Since a $2\times2$ matrix satisfies $\|T\|_2^2\geq\|T\|_F^2/2$, it remains to bound $a^2+b^2$. Here
$$
a^2+b^2-\frac{2}{9}
=\frac{4(\rho-2)^2(4\rho^2+11\rho+16)}{9(\rho+1)^2(\rho+4)^2}\geq0,
$$
with equality only at $\rho=2$. Consequently
$$
\mathcal C(\rho,2s)^2
\geq(1-s)^2+\frac{s^2}{81}.
$$
For every $s>0$, equality in this lower bound forces $\rho=2$.

Step 3: Optimize the relaxation parameter in the lower bound
Define
$$
L(s)=(1-s)^2+\frac{s^2}{81},
\qquad 0<s\leq1.
$$
Then
$$
L'(s)=-2(1-s)+\frac{2s}{81},
$$
so the unique critical point is
$$
s_*=\frac{81}{82}.
$$
Because $L$ is a strictly convex quadratic, this is its unique minimum on $(0,1]$, and
$$
L(s_*)=\frac{1}{82}.
$$
Thus every admissible pair satisfies
$$
\mathcal C(\rho,\theta)\geq\frac{1}{\sqrt{82}},
$$
and equality can occur only if
$$
\rho=2,
\qquad
\theta=2s_*=\frac{81}{41}.
$$

Step 4: Show that the forced pair attains the lower bound for every anisotropy
Set
$$
\rho=2,
\qquad
s=\frac{81}{82}.
$$
For arbitrary $\mu\in[1,4]$,
$$
a_{\mu}=\frac{2-\mu}{2+\mu},
\qquad
b_{\mu}=\frac{2-4/\mu}{2+4/\mu}
=\frac{\mu-2}{\mu+2}=-a_{\mu}.
$$
Let
$$
c_{\mu}=\frac{2-\mu}{2+\mu},
\qquad
Z=\begin{bmatrix}1&0\\0&-1\end{bmatrix}.
$$
Then $D_{\mu}=c_{\mu}Z$. The fixed matrix
$$
J=UZU^TZ=\begin{bmatrix}0&-1\\1&0\end{bmatrix}
$$
satisfies $J^T=-J$ and $J^TJ=I$, so
$$
UD_{\mu}U^TD_{\mu}=c_{\mu}^2J.
$$
Hence
$$
T_{\mu,2,81/82}
=\frac{1}{82}I+\frac{81}{82}c_{\mu}^2J
$$
and therefore
$$
T_{\mu,2,81/82}^TT_{\mu,2,81/82}
=\left(\frac{1}{82^2}+\frac{81^2}{82^2}c_{\mu}^4\right)I.
$$
On $\mu\in[1,4]$,
$$
|c_{\mu}|=\frac{|2-\mu|}{2+\mu}\leq\frac{1}{3},
$$
with equality at $\mu=1$ and $\mu=4$. Thus
$$
\|T_{\mu,2,81/82}\|_2^2
\leq\frac{1}{82^2}+\frac{81^2}{82^2}\frac{1}{81}
=\frac{1}{82},
$$
and equality is attained at the two endpoints. Hence
$$
\mathcal C\left(2,\frac{81}{41}\right)=\frac{1}{\sqrt{82}}.
$$

Step 5: State the unique robust optimum
The lower bound in Step 2 is strict unless $\rho=2$, and the strictly convex minimization in Step 3 then forces $s=81/82$, equivalently $\theta=81/41$. Step 4 proves that this pair controls every $\mu\in[1,4]$ and attains the lower bound. The minimizing pair is therefore unique.

Final Answer: $\boxed{\left(2,\frac{81}{41},\frac{1}{\sqrt{82}}\right)}$

---

## Answer

$\left(2,\frac{81}{41},\frac{1}{\sqrt{82}}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- robust parameter tuning
- relaxed Douglas-Rachford splitting
- proximal reflections
- Frobenius norm lower bounds
- fixed-determinant anisotropy
