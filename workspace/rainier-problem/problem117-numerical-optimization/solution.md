## Steps

Step 1: Express the block-coordinate contraction as a generalized Rayleigh quotient
Let $A=A_5$ and, for $i=1,\ldots,4$, let $E_i\in\mathbb R^{5\times2}$ insert a vector into coordinates $i,i+1$. Every adjacent principal block of $A$ equals
$$
H=\begin{bmatrix}2&-1\\-1&2\end{bmatrix},
\qquad
H^{-1}=\frac13\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$
Write $q=Ax$. If block $i$ is selected and its displacement is $d\in\mathbb R^2$, then
$$
f_5(x+E_i d)=f_5(x)+q_{\{i,i+1\}}^Td+\frac12d^THd.
$$
The exact block minimizer is therefore $d=-H^{-1}q_{\{i,i+1\}}$, and its decrease is
$$
f_5(x)-f_5(x^+)=\frac12q_{\{i,i+1\}}^TH^{-1}q_{\{i,i+1\}}.
$$
For $p=(p_1,\ldots,p_4)$ define
$$
B(p)=\sum_{i=1}^4p_iE_iH^{-1}E_i^T,
\qquad
K=A^{-1}.
$$
Since $f_5(x)=\frac12x^TAx=\frac12q^TKq$,
$$
\frac{\mathbb E[f_5(x^+)\mid x]}{f_5(x)}
=1-\frac{q^TB(p)q}{q^TKq}.
$$
Thus
$$
\Gamma(p)=1-m(p),
\qquad
m(p)=\inf_{q\ne0}\frac{q^TB(p)q}{q^TKq},
$$
and minimizing $\Gamma$ is equivalent to maximizing $m$.

Step 2: Derive a sampling-independent test direction and the sharp universal upper bound
To make the numerator independent of the unknown probabilities, require all four adjacent block energies to be equal. Because $H^{-1}$ is invariant under swapping its two coordinates, every alternating vector
$$
q=(u,v,u,v,u)^T
$$
has this property: each block contributes
$$
\begin{bmatrix}u&v\end{bmatrix}H^{-1}
\begin{bmatrix}u\\v\end{bmatrix}
=\frac23(u^2+uv+v^2).
$$
Hence $q^TB(p)q=\frac23(u^2+uv+v^2)$ for every probability vector $p$.

Solving $Az=q$ gives
$$
z=Kq=
\begin{bmatrix}
\frac32u+v\\
2u+2v\\
\frac52u+2v\\
2u+2v\\
\frac32u+v
\end{bmatrix},
$$
so
$$
q^TKq=\frac{11u^2+16uv+8v^2}{2}.
$$
For $u\ne0$ put $t=v/u$. The resulting test quotient is
$$
\frac{q^TB(p)q}{q^TKq}
=\frac{4(t^2+t+1)}{3(8t^2+16t+11)}
=\frac19+\frac{(2t-1)^2}{9(8t^2+16t+11)}.
$$
The denominator in the last term is $8(t+1)^2+3>0$, while the case $u=0$ gives quotient $1/6$. Therefore the smallest sampling-independent test value is $1/9$, attained uniquely in this family at $t=1/2$. With
$$
q_*=egin{bmatrix}1&\frac12&1&\frac12&1\end{bmatrix}^T,
$$
we obtain the universal bound
$$
m(p)\leq\frac19
$$
for every admissible $p$.

Step 3: Use equality in the upper bound to force the unique candidate sampling distribution
If a distribution attains the best possible value $m(p)=1/9$, then $q_*$ must minimize the generalized Rayleigh quotient. Differentiating
$$
R(q)=\frac{q^TB(p)q}{q^TKq}
$$
at $q_*$ in an arbitrary direction $h$ gives
$$
0=\frac{2h^T\left(B(p)q_*-\frac19Kq_*\right)}{q_*^TKq_*},
$$
so
$$
B(p)q_*=\frac19Kq_*.
$$
From Step 2,
$$
Kq_*=
\begin{bmatrix}2&3&\frac72&3&2\end{bmatrix}^T.
$$
Also
$$
H^{-1}\begin{bmatrix}1\\\frac12\end{bmatrix}
=\begin{bmatrix}\frac56\\\frac23\end{bmatrix},
\qquad
H^{-1}\begin{bmatrix}\frac12\\1\end{bmatrix}
=\begin{bmatrix}\frac23\\\frac56\end{bmatrix}.
$$
Therefore
$$
B(p)q_*
=\begin{bmatrix}
\frac56p_1\\
\frac23(p_1+p_2)\\
\frac56(p_2+p_3)\\
\frac23(p_3+p_4)\\
\frac56p_4
\end{bmatrix}.
$$
Equating coordinates with $\frac19Kq_*$ forces
$$
p_1=p_4=\frac4{15},
\qquad
p_2=p_3=\frac7{30}.
$$
These values are positive and sum to $1$, so any optimizer must equal
$$
p_*=\left(\frac4{15},\frac7{30},\frac7{30},\frac4{15}\right).
$$

Step 4: Prove the forced distribution attains the bound and identify every worst-case direction
For $p_*$, the matrix from Step 1 is
$$
B_*=
\begin{bmatrix}
\frac8{45}&\frac4{45}&0&0&0\\
\frac4{45}&\frac13&\frac7{90}&0&0\\
0&\frac7{90}&\frac{14}{45}&\frac7{90}&0\\
0&0&\frac7{90}&\frac13&\frac4{45}\\
0&0&0&\frac4{45}&\frac8{45}
\end{bmatrix}.
$$
Because $q=Ax$,
$$
\frac{q^TB_*q}{q^TKq}
=\frac{x^TAB_*Ax}{x^TAx}.
$$
Set
$$
C=AB_*A-\frac19A.
$$
Both $A$ and $B_*$ are invariant under reversing the five coordinates, so $C$ is also reversal-invariant. Decompose any $x$ into its reversal-symmetric and reversal-antisymmetric parts,
$$
x=x^++x^-,
\qquad
x^+=(a,b,c,b,a)^T,
\qquad
x^-=(u,v,0,-v,-u)^T.
$$
The two parts are $C$-orthogonal: if $J$ reverses the coordinates, then $JC=CJ$, $Jx^+=x^+$, and $Jx^-=-x^-$, so
$$
(x^+)^TCx^-=(x^+)^TJ^TCJx^-=-(x^+)^TCx^-=0.
$$
Substituting the displayed $A$ and $B_*$ gives
$$
(x^+)^TCx^+
=\frac{14}{135}(3a-2b)^2+\frac4{135}(7b-6c)^2,
$$
and
$$
(x^-)^TCx^-
=\frac{14}{15}\left((u-v)^2+v^2\right).
$$
Thus $C\succeq0$, so
$$
m(p_*)\geq\frac19.
$$
Together with Step 2, this gives $m(p_*)=1/9$.

The same sum-of-squares identities show that equality is possible only when $u=v=0$, $3a=2b$, and $7b=6c$. Hence the complete worst-case initial-vector subspace is
$$
\mathcal L_*=\operatorname{span}\{(4,6,7,6,4)^T\}.
$$

Step 5: State the unique optimum
Step 3 shows that any distribution reaching the universal upper bound must equal $p_*$, while Step 4 proves that $p_*$ reaches it. Therefore the minimizing distribution is unique. Since $\Gamma(p)=1-m(p)$,
$$
\Gamma_* = 1-\frac19=\frac89.
$$
The worst-case vectors at this optimum are exactly the nonzero vectors in $\mathcal L_*$.

Final Answer: $\boxed{\left(\left(\frac4{15},\frac7{30},\frac7{30},\frac4{15}\right),\frac89,\operatorname{span}\{(4,6,7,6,4)^T\}\right)}$

---

## Answer

$\left(\left(\frac4{15},\frac7{30},\frac7{30},\frac4{15}\right),\frac89,\operatorname{span}\{(4,6,7,6,4)^T\}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- randomized block coordinate descent
- generalized Rayleigh quotient
- equality conditions
- positive semidefinite factorization
- symmetry decomposition
