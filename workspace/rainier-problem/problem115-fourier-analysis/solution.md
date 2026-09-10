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
=2^{-127}\sum_{x,y\in E}
(-1)^{x\cdot y+a\cdot x+b\cdot y+x\cdot v+y\cdot u}.
$$
For fixed $y$, the sum over $x$ vanishes unless $y=a+v$, when it equals $2^{127}$. Hence
$$
(\mathcal Ff_{a,b})(u,v)
=(-1)^{a\cdot b}f_{a,b}(u,v).
$$

Step 3: Reduce $Tf_{a,b}=f_{a,b}$ to a pairing between two kernels

The multiplicative group $P^\times$ has order $126$, so its subgroup of ninth powers has order $14$. The element $2$ has order $7$ modulo $127$, while $-1$ has order $2$, hence
$$
H=\{\pm2^i:0\le i<7\}.
$$
Thus both $H$ and $3H$ are stable under negation and under multiplication by $2$.

Consequently $A$ and $C$ are symmetric with zero diagonal. Writing $\tau_hx(t)=x(t+h)$, characteristic $2$ gives
$$
A^2=\left(\sum_{h\in H}\tau_h\right)^2
=\sum_{h\in H}\tau_{2h}=A,
$$
and similarly $C^2=C$. They commute because both are convolution operators.

The shears
$$
U_C(x,y)=(x+Cy,y),\qquad L_A(x,y)=(x,y+Ax)
$$
preserve $q_0$, and
$$
S=L_AU_C.
$$
Hence $q_0(Sz)=q_0(z)$. The linear part of $q_{a,b}(S(x,y))$ is
$$
(a+Ab)\cdot x+(Ca+b+CAb)\cdot y.
$$
Therefore $q_{a,b}\circ S=q_{a,b}$ exactly when
$$
Ab=0,\qquad Ca=0.
$$
Indeed, $Ab=0$ also gives $CAb=0$. By Step 2, evaluating $Tf_{a,b}=f_{a,b}$ at $0$ additionally forces
$$
a\cdot b=0.
$$
Thus we must count orthogonal pairs
$$
(a,b)\in\ker C\times\ker A.
$$

Step 4: Compute the joint spectrum of $A$ and $C$

Extend scalars to $\mathbb F_{128}$; this does not change any binary kernel dimension. Choose a primitive $127$th root $\zeta\in\mathbb F_{128}$. For $j\in\mathbb F_{127}$, the additive-character vector
$$
e_j(t)=\zeta^{jt}
$$
is a simultaneous eigenvector for $A$ and $C$. For $j\ne0$ their eigenvalues are
$$
\lambda_j=\sum_{h\in H}\zeta^{jh}
=\operatorname{Tr}_{\mathbb F_{128}/\mathbb F_2}(\zeta^j+\zeta^{-j}),
$$
$$
\mu_j=\sum_{h\in H}\zeta^{3jh}=\lambda_{3j}.
$$
For $j=0$, both eigenvalues are $14=0$ in $\mathbb F_2$.

Both eigenvalues are constant on multiplicative $H$-cosets. There are nine nonzero cosets. To determine their joint pattern exactly, take $\zeta$ to be a root of $X^7+X+1$. This polynomial has no linear root, and its remainders modulo the three irreducible polynomials of degrees $2$ and $3$ over $\mathbb F_2$ are respectively $1,X,X$, so it is irreducible. Since $|\mathbb F_{128}^\times|=127$ is prime, such a root has order $127$.

Using $\zeta^7=\zeta+1$ and
$$
\operatorname{Tr}(w)=w+w^2+w^4+w^8+w^{16}+w^{32}+w^{64},
$$
a direct reduction gives the following table. The representatives are written in cyclic order under multiplication by $3$ modulo $H$.

$$
\begin{array}{c|ccccccccc}
r&1&3&9&19&13&11&5&7&21\\ \hline
\lambda_r&1&1&0&0&1&0&1&1&0\\
\mu_r=\lambda_{3r}&1&0&0&1&0&1&1&0&1
\end{array}
$$

Each nonzero coset has $14$ elements. Hence the simultaneous eigenspaces
$$
E_{\varepsilon\delta}=\{x\in E:Ax=\varepsilon x,\ Cx=\delta x\}
$$
have dimensions
$$
\dim E_{00}=1+14=15,
$$
$$
\dim E_{01}=42,\qquad
\dim E_{10}=42,\qquad
\dim E_{11}=28.
$$
In particular
$$
\dim\ker A=\dim\ker C=57.
$$

Step 5: Count the orthogonal pairs

Because $C$ is self-adjoint,
$$
(\ker C)^\perp=\operatorname{im}C.
$$
Since $A$ and $C$ are commuting idempotents,
$$
\ker A\cap\operatorname{im}C=E_{01},
$$
which has dimension $42$. Thus the dot-product pairing
$$
\ker C\times\ker A\to\mathbb F_2
$$
has rank
$$
57-42=15.
$$

There are $2^{42}$ vectors $b\in\ker A$ that annihilate all of $\ker C$; for each of them all $2^{57}$ choices of $a\in\ker C$ work. For each of the remaining $2^{57}-2^{42}$ choices of $b$, exactly half of $\ker C$ is orthogonal to $b$. Therefore the number of functions is
$$
2^{42}2^{57}+(2^{57}-2^{42})2^{56}
=2^{113}+2^{98}
=10384910629719712314411366834241536.
$$

Final Answer: $\boxed{10384910629719712314411366834241536}$

---

## Answer

$10384910629719712314411366834241536$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier transform on binary vector spaces
- quadratic refinements of symplectic forms
- cyclotomic Cayley graph operators
- simultaneous Fourier spectra
- degenerate bilinear pair counting

---

## Black-Box Audit — no issues found
