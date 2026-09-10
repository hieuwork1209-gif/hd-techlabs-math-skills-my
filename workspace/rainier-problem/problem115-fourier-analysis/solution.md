## Steps

Step 1: Classify the sign functions satisfying the four-point identity

Put
$$
q_0(x,y)=x\cdot y.
$$
Its polar form is $\omega$. Since $f(0)=1$, write uniquely $f(z)=(-1)^{q(z)}$ with $q(0)=0$. Setting $z=0$ in the four-point identity gives
$$
q(r+s)=q(r)+q(s)+\omega(r,s).
$$
Hence $q+q_0$ is linear. Therefore every admissible function is uniquely
$$
f_{a,b}(x,y)=(-1)^{x\cdot y+a\cdot x+b\cdot y},
\qquad a,b\in E.
$$
Conversely every $f_{a,b}$ satisfies the four-point identity.

Step 2: Compute the Walsh--Fourier transform

For $(u,v)\in V$,
$$
(\mathcal Ff_{a,b})(u,v)
=2^{-8191}\sum_{x,y\in E}
(-1)^{x\cdot y+a\cdot x+b\cdot y+x\cdot v+y\cdot u}.
$$
For fixed $y$, the sum over $x$ vanishes unless $y=a+v$, when it equals $2^{8191}$. Thus
$$
(\mathcal Ff_{a,b})(u,v)
=(-1)^{a\cdot b}f_{a,b}(u,v).
$$

Step 3: Reduce $Tf_{a,b}=f_{a,b}$ to a pairing between two kernels

Since $2^{13}=8192\equiv1\pmod{8191}$ and $13$ is prime, $2$ has order $13$ in $P^\times$. Thus $H=\langle2,-1\rangle$ has $26$ elements. Both $H$ and $3H$ are stable under negation and multiplication by $2$.

Consequently $A$ and $C$ are symmetric with zero diagonal. If $\tau_hx(t)=x(t+h)$, then in characteristic $2$,
$$
A^2=\left(\sum_{h\in H}\tau_h\right)^2
=\sum_{h\in H}\tau_{2h}=A,
$$
and similarly $C^2=C$. They commute because both are convolution operators.

The shears
$$
U_C(x,y)=(x+Cy,y),\qquad L_A(x,y)=(x,y+Ax)
$$
preserve $q_0$, so $S=L_AU_C$ preserves $q_0$. The linear part of $q_{a,b}(S(x,y))$ is
$$
(a+Ab)\cdot x+(Ca+b+CAb)\cdot y.
$$
Hence $q_{a,b}\circ S=q_{a,b}$ exactly when
$$
Ab=0,\qquad Ca=0.
$$
By Step 2, evaluating $Tf_{a,b}=f_{a,b}$ at $0$ also forces $a\cdot b=0$. Thus we must count orthogonal pairs
$$
(a,b)\in\ker C\times\ker A.
$$

Step 4: Express the joint spectrum by two exponential sums

Because $8191=2^{13}-1$, a primitive $8191$st root $\zeta$ lies in $\mathbb F_{8192}$. For $j\in\mathbb F_{8191}$, put $\xi=\zeta^j$. Then $j\mapsto\xi$ is a bijection from $\mathbb F_{8191}$ to $\mathbb F_{8192}^\times$. The additive-character vector
$$
e_j(t)=\zeta^{jt}
$$
is a simultaneous eigenvector for $A$ and $C$. Its eigenvalues are
$$
\lambda_j=\sum_{h\in H}\zeta^{jh}
=\operatorname{Tr}_{\mathbb F_{8192}/\mathbb F_2}(\xi+\xi^{-1}),
$$
$$
\mu_j=\sum_{h\in H}\zeta^{3jh}
=\operatorname{Tr}_{\mathbb F_{8192}/\mathbb F_2}(\xi^3+\xi^{-3}).
$$
Let
$$
K_n=\sum_{x\in\mathbb F_{2^n}^\times}(-1)^{\operatorname{Tr}(x+x^{-1})}.
$$
The curve
$$
\mathcal E:\quad Y^2+XY=X^3+1
$$
has
$$
\#\mathcal E(\mathbb F_{2^n})=2^n+1+K_n.
$$
Indeed, for $x\ne0$, writing $Y=xz$ gives $z^2+z=x+x^{-2}$, and $\operatorname{Tr}(x^{-2})=\operatorname{Tr}(x^{-1})$; the points over $x=0$ and infinity contribute one each. Over $\mathbb F_2$ the curve has $4$ points, so its Frobenius trace is $-1$. Therefore, if $t_0=2,t_1=-1$ and
$$
t_n=-t_{n-1}-2t_{n-2},
$$
then $K_n=-t_n$. Successively,
$$
t_2,t_3,\ldots,t_{13}
=-3,5,1,-11,9,13,-31,5,57,-67,-47,181,
$$
so
$$
K_{13}=-181.
$$
Thus
$$
\sum_j(-1)^{\lambda_j}
=\sum_j(-1)^{\mu_j}=-181,
$$
because $x\mapsto x^3$ is a permutation of $\mathbb F_{8192}^\times$.

For the joint correlation, in characteristic $2$,
$$
x^3+x^{-3}=(x+x^{-1})^3+(x+x^{-1}),
$$
so
$$
\lambda_j+\mu_j
=\operatorname{Tr}\bigl((\xi+\xi^{-1})^3\bigr).
$$
For $s\ne0$, the equation $x+x^{-1}=s$ has $1+(-1)^{\operatorname{Tr}(s^{-1})}$ solutions, while $s=0$ has the single solution $x=1$. Hence, writing $\psi(u)=(-1)^{\operatorname{Tr}(u)}$,
$$
\sum_j(-1)^{\lambda_j+\mu_j}
=1+\sum_{s\ne0}\bigl(1+\psi(s^{-1})\bigr)\psi(s^3).
$$
Since cubing permutes $\mathbb F_{8192}$,
$$
\sum_{s\in\mathbb F_{8192}}\psi(s^3)=0,
$$
and therefore
$$
\sum_j(-1)^{\lambda_j+\mu_j}
=\sum_{s\ne0}\psi(s^3+s^{-1})=:J_{13}.
$$

Step 5: Evaluate the genus-two correlation

For general $n$, put
$$
J_n=\sum_{x\in\mathbb F_{2^n}^\times}
(-1)^{\operatorname{Tr}(x^3+x^{-1})}.
$$
Consider the Artin--Schreier curve
$$
\mathcal C:\quad Y^2+Y=X^3+X^{-1}.
$$
The right side has poles of odd orders $3$ and $1$. For an Artin--Schreier curve $Y^2+Y=f(X)$ with odd pole orders $d_i$, Riemann--Hurwitz gives
$$
g=\frac{\sum_i(d_i+1)-2}{2},
$$
so $\mathcal C$ has genus $2$. Each pole has one point above it, and therefore
$$
\#\mathcal C(\mathbb F_{2^n})=2^n+1+J_n.
$$

Directly, $\#\mathcal C(\mathbb F_2)=4$. Over $\mathbb F_4=\{0,1,\rho,\rho^2\}$ with $\rho^2+\rho+1=0$, only $x=1$ contributes two affine points, while $x=\rho,\rho^2$ contribute none; together with the two pole-points this gives $\#\mathcal C(\mathbb F_4)=4$.

Let $T_n$ be the sum of the $n$th powers of the four Frobenius eigenvalues of $\mathcal C$. Then
$$
T_1=2+1-4=-1,
\qquad
T_2=4+1-4=1.
$$
For a genus-$2$ curve over $\mathbb F_2$, the reciprocal Frobenius polynomial has the form
$$
L(T)=1-T_1T+e_2T^2-2T_1T^3+4T^4,
$$
where $e_2=(T_1^2-T_2)/2$. Here $e_2=0$, so
$$
L(T)=1+T+2T^3+4T^4.
$$
Newton's identities give $T_0=4$, $T_3=-7$, and for $n\ge4$,
$$
T_n=-T_{n-1}-2T_{n-3}-4T_{n-4}.
$$
Iterating,
$$
T_3,T_4,\ldots,T_{13}
=-7,-7,9,1,41,-31,-7,-79,-23,161,25.
$$
Hence
$$
J_{13}=-T_{13}=-25.
$$

Step 6: Recover the four simultaneous eigenspace dimensions

Let $N_{\varepsilon\delta}$ be the number of $j$ for which $(\lambda_j,\mu_j)=(\varepsilon,\delta)$. Since there are $8191$ values of $j$,
$$
N_{00}=\frac{8191-181-181-25}{4}=1951,
$$
$$
N_{01}=N_{10}=\frac{8191-181+181+25}{4}=2054,
$$
$$
N_{11}=\frac{8191+181+181-25}{4}=2132.
$$
Therefore
$$
\dim\ker A=\dim\ker C=N_{00}+N_{01}=4005.
$$
Because $C$ is self-adjoint,
$$
(\ker C)^\perp=\operatorname{im}C.
$$
Since $A$ and $C$ are commuting idempotents,
$$
\ker A\cap\operatorname{im}C
$$
is exactly the simultaneous eigenspace $(\lambda,\mu)=(0,1)$, of dimension $2054$. Thus the dot-product pairing
$$
\ker C\times\ker A\to\mathbb F_2
$$
has rank
$$
4005-2054=1951.
$$

Step 7: Count the orthogonal pairs

For a bilinear pairing of rank $r$ between spaces of dimensions $m$ and $n$, the number of zero pairs is
$$
2^{m+n-1}+2^{m+n-r-1}.
$$
Here $m=n=4005$ and $r=1951$, so the number of admissible functions is
$$
2^{8009}+2^{6058}.
$$

Final Answer: $\boxed{2^{8009}+2^{6058}}$

---

## Answer

$2^{8009}+2^{6058}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier transform on binary vector spaces
- quadratic refinements of symplectic forms
- cyclotomic Cayley convolution operators
- binary Kloosterman sums
- genus-two Artin--Schreier curves

---

## Black-Box Audit — no issues found
