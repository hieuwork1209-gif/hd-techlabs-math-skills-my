## Steps

Step 1: Parameterize the lifts and expose the cyclic phase coupling.
Put
$$
Q=\ell^r,\qquad h=\ell^{r-1},\qquad m=2q^2,\qquad d=\frac{q(2q-1)}Q.
$$
Also set
$$
A=d+q+2\ell+2\ell^2-4,\quad B=d+2\ell+2\ell^2-4,
$$
$$
C=d+2\ell-4,\qquad E=d-4.
$$
The primes $q,q+2Q,q+4Q$ are all congruent to $2^{-1}$ modulo $\ell$, hence are inert in $\mathbb Q(\zeta)$ because $2$ generates $\mathbb F_\ell^\times$.

Write indices cyclically and let $P(s_1,\ldots,s_r)=(s_2,\ldots,s_r,s_1)$. A lift of $\pi$ has the form
$$
\sigma(\alpha_i^{(j)})=\zeta^{a_i^{(j)}}\alpha_{\pi(i)}^{(j)},\qquad
\sigma(\rho_j)=\zeta^{s_j}\rho_j,
$$
with every $s_j\ne0$. Applying $\sigma$ to $\prod_i\alpha_i^{(j)}=\rho_{j+1}$ gives
$$
\sum_i a_i^{(j)}=s_{j+1}. \tag{1}
$$
For each transposition block $T$ of $\pi$, define
$$
Z_T=\left(\sum_{i\in T}a_i^{(1)},\ldots,\sum_{i\in T}a_i^{(r)}\right)\in G:=\mathbb F_\ell^r,
$$
and let $m_z$ count the blocks with label $z$. Then
$$
\sum_zm_z=m,\qquad \sum_zm_zz=Ps. \tag{2}
$$

Step 2: Convert the cycle data into a Fourier-magnitude flag.
Let $D_s=\operatorname{diag}(s_1,\ldots,s_r)$. For $i$ in block $T$ and $h$ in block $R$, two applications of $\sigma$ on $\Omega_k$ translate the fiber by
$$
w+Z_T-Z_R,\qquad w=2D_sk.
$$
Since $D_s$ is invertible, put $\overline W=2D_sW$ and $\overline U=2D_sU$. If
$$
N_w=\sum_zm_zm_{z+w},
$$
then the number of base orbits with zero two-step translation is
$$
R_w=2N_w-m\delta_{w,0}. \tag{3}
$$
Each such base orbit yields $Q$ cycles of length $2$, while every nonzero translation has order $\ell$. Hence the two prescribed gaps are equivalent to
$$
R_w=R_0+8\ell(q+3Q)1_{\overline U}(w)+8\ell^2(q+Q)1_{\overline W}(w). \tag{4}
$$
For $M(\chi)=\sum_zm_z\chi(z)$, Fourier transforming gives
$$
|M(\chi)|=
\begin{cases}
q+4Q,&\chi\in\overline U^\perp\setminus\{1\},\\
q+2Q,&\chi\in\overline W^\perp\setminus\overline U^\perp,\\
q,&\chi\notin\overline W^\perp.
\end{cases} \tag{5}
$$
For $0\le t<r$, define
$$
c_s^{(t)}=\left(\frac{s_{1+t}}{s_1},\ldots,\frac{s_{r+t}}{s_r}\right)
$$
with cyclic indices. Then $D_sc_s^{(t)}=P^ts$, so the extra incidence condition becomes
$$
P^ts\in\overline U\setminus\overline W\qquad(0\le t<r). \tag{6}
$$

Step 3: Recover the affine flag and its phase center.
Fix a nontrivial projective character direction $L$. By (5), its nontrivial Fourier coefficients have one absolute value $p_L\in\{q,q+2Q,q+4Q\}$. Since $p_L$ is inert, $(M(\chi))=(p_L)$, so $M(\chi)/p_L$ is an algebraic integer all of whose conjugates have absolute value $1$ and therefore is a root of unity.

Let $\lambda=1-\zeta$. Since every character value is $1$ modulo $\lambda$,
$$
M(\chi)\equiv2q^2\pmod\lambda,
$$
and $p_L\equiv q\pmod\ell$, hence $M(\chi)/p_L\equiv1\pmod\lambda$. Thus every projective direction determines a distinguished affine hyperplane carrying the Fourier phase.

Put
$$
D=\frac{Q-1}{\ell-1},\qquad d_0=\frac{h-1}{\ell-1}.
$$
Let $e(z)$ count all distinguished hyperplanes through $z$, let $f(z)$ count those with normals in $\mathbb P(\overline W^\perp)$, and let $I(z)$ indicate the distinguished hyperplane for $\overline U^\perp$. Fourier inversion gives
$$
Qm_z=m-qD-2Q(\ell+2)+\ell q\,e(z)+2\ell Q\,f(z)+2\ell Q\,I(z). \tag{7}
$$
Reducing modulo $Q$ gives $e(z)\equiv d_0\pmod h$. Since $0\le e(z)\le D=d_0+h$, every $e(z)$ is either $d_0$ or $D$. Counting incidences shows exactly one point has value $D$; call it $z_0$. Therefore
$$
f(z)=1+\ell 1_{z_0+\overline W}(z),\qquad I(z)=1_{z_0+\overline U}(z),
$$
and
$$
m_z=d-4+2\ell^2 1_{z_0+\overline W}(z)+2\ell 1_{z_0+\overline U}(z)+q\delta_{z_0}(z). \tag{8}
$$
Taking the first moment and using (2) gives
$$
qz_0=Ps. \tag{9}
$$
The four multiplicity levels are $A,B,C,E$, so the profile recovers $z_0$ and the transformed flag. Conversely, every admissible $s$ and transformed flag satisfying (6) gives exactly one profile of the form (8).

Step 4: Identify the conjugacy invariants.
For $\tau\in\widetilde C_\pi$ with base permutation in $C_{S_n}(\pi)$, direct conjugation gives
$$
s_j'=s_j,\qquad Z_T'=Z_{c^{-1}T}. \tag{10}
$$
Thus $s$ and the multiplicity profile are orbit invariants. Conversely, the wreath product $C_{S_n}(\pi)\cong C_2\wr S_m$ permutes the transposition blocks arbitrarily, and an element over $M$ removes the remaining opposite endpoint phases. Hence two qualifying lifts are conjugate exactly when they have the same $s$ and the same multiplicity profile.

Step 5: Solve the periodic affine recurrence and count the flags.
The statement imposes
$$
\mathbf1\in\operatorname{span}\{s,Ps\},\qquad \sum_js_j=r,\qquad \prod_js_j=2. \tag{11}
$$
If $s$ and $Ps$ were dependent, (11) would force $s$ to be constant. The sum condition would then give $s=\mathbf1$, contradicting the product condition. Thus $s,Ps$ are independent, and uniquely
$$
Ps=a\mathbf1+bs
$$
with $a\ne0$. Summing coordinates and using $\sum_js_j=r$ gives $a=1-b$. Therefore
$$
s_{j+1}=1-b+bs_j. \tag{12}
$$
The cases $b=0$ or $1$ are constant, so $b\ne0,1$. Writing $u=s_1-1\ne0$ gives
$$
s_j=1+ub^{j-1}. \tag{13}
$$
Cyclic periodicity forces $b^r=1$. Since $r$ is prime and $r\mid\ell-1$, $b$ has order $r$, and there are $r-1$ choices for $b$. As $r$ is odd,
$$
\prod_{j=0}^{r-1}(1+ub^j)=1+u^r.
$$
The product condition in (11) is therefore $u^r=1$, giving exactly $r$ choices for $u$. Because the subgroup of order $r$ has odd order, it does not contain $-1$, so every coordinate in (13) is nonzero. Thus there are exactly
$$
r(r-1) \tag{14}
$$
admissible phase vectors $s$.

Let $H=\operatorname{span}\{s,Ps\}$. From (12),
$$
P^ts=(1-b^t)\mathbf1+b^ts,
$$
so all $P^ts$ lie in $H$, and their $r$ projective lines are distinct. The number of hyperplanes $\overline U$ containing $H$ is
$$
\frac{\ell^{r-2}-1}{\ell-1}. \tag{15}
$$
For fixed $\overline U$, a hyperplane $\overline W\subset\overline U$ avoids all $r$ vectors $P^ts$ exactly when the kernel line of its restriction to $H$ avoids those $r$ projective points. There are $\ell+1-r$ possible kernel lines, and each has $\ell^{r-3}$ extensions to $\overline U$. Hence
$$
F=(\ell+1-r)\ell^{r-3}\frac{\ell^{r-2}-1}{\ell-1}. \tag{16}
$$
Multiplying (14) and (16) gives the number of conjugacy orbits.
Final Answer: $\boxed{r(r-1)(\ell+1-r)\ell^{r-3}\frac{\ell^{r-2}-1}{\ell-1}}$

---

## Answer

$r(r-1)(\ell+1-r)\ell^{r-3}\frac{\ell^{r-2}-1}{\ell-1}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cyclic Kummer coupling of total phases
- three-level autocorrelation on a finite vector space
- affine-hyperplane phase recovery
- periodic affine recurrences over finite fields
- projective incidence for a cyclic orbit
