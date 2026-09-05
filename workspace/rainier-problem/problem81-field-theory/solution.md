## Steps

Step 1: Parameterize the lifts and expose the cyclic phase coupling.
Put
$$
Q=\ell^r,\qquad h=\ell^{r-1},\qquad g=\ell^{r-2},\qquad m=2q^2,
$$
$$
d=\frac{q(2q-1)}Q.
$$
Also set
$$
A=d+q+2\ell+2\ell^2-4,\quad B=d+2\ell+2\ell^2-4,
$$
$$
C=d+2\ell-4,\qquad E=d-4.
$$
The primes $q,q+2Q,q+4Q$ are all congruent to $2^{-1}$ modulo $\ell$. Since $2$ generates $\mathbb F_\ell^\times$, so does $2^{-1}$, hence all three primes are inert in $\mathbb Q(\zeta)$.

Write indices cyclically and define
$$
P(s_1,\ldots,s_r)=(s_2,\ldots,s_r,s_1).
$$
A lift of the fixed permutation $\pi$ has the form
$$
\sigma(\alpha_i^{(j)})=\zeta^{a_i^{(j)}}\alpha_{\pi(i)}^{(j)},\qquad
\sigma(\rho_j)=\zeta^{s_j}\rho_j,
$$
with every $s_j\ne0$. Applying $\sigma$ to
$$
\prod_i\alpha_i^{(j)}=\rho_{j+1}
$$
gives
$$
\sum_i a_i^{(j)}=s_{j+1}. \tag{1}
$$
For each transposition block $T$ of $\pi$, define
$$
Z_T=\left(\sum_{i\in T}a_i^{(1)},\ldots,\sum_{i\in T}a_i^{(r)}\right)\in G:=\mathbb F_\ell^r,
$$
and let $m_z$ be the number of blocks with label $z$. Then
$$
\sum_zm_z=m,\qquad \sum_zm_zz=Ps. \tag{2}
$$

Step 2: Convert the cycle data to a Fourier magnitude flag and transport the extra incidence.
Let $D_s=\operatorname{diag}(s_1,\ldots,s_r)$. For an index $(i,h,u)$ of $\Omega_k$, with $i$ in block $T$ and $h$ in block $R$, two applications of $\sigma$ translate the fiber by
$$
w+Z_T-Z_R,\qquad w=2D_sk.
$$
Because each $s_j\ne0$, $2D_s$ is an automorphism of $G$. Let
$$
\overline W=2D_sW,\qquad \overline U=2D_sU.
$$
Put
$$
N_w=\sum_{z\in G}m_zm_{z+w}.
$$
For distinct transposition blocks an ordered block-pair contributes two base orbits, while a diagonal block contributes one internal orbit when $w=0$. Hence the number of base orbits whose two-step translation vanishes is
$$
R_w=2N_w-m\delta_{w,0}. \tag{3}
$$
Each such base orbit gives $Q$ cycles of length $2$; every nonzero translation has order $\ell$ and gives cycles of length $2\ell$. Thus the prescribed gaps are equivalent to
$$
R_w=R_0+8\ell(q+3Q)1_{\overline U}(w)+8\ell^2(q+Q)1_{\overline W}(w) \tag{4}
$$
for a constant $R_0$.

For an additive character $\chi$ of $G$, write
$$
M(\chi)=\sum_zm_z\chi(z).
$$
The unnormalized Fourier transform gives $\widehat N(\chi)=|M(\chi)|^2$. For nontrivial $\chi$, (3)--(4) yield
$$
|M(\chi)|=
\begin{cases}
q+4Q,&\chi\in\overline U^\perp\setminus\{1\},\\
q+2Q,&\chi\in\overline W^\perp\setminus\overline U^\perp,\\
q,&\chi\notin\overline W^\perp.
\end{cases} \tag{5}
$$
The two incidence vectors in the statement satisfy
$$
D_s\mathbf1=s,\qquad D_sc_s=Ps.
$$
Thus
$$
s,Ps\in\overline U\setminus\overline W. \tag{6}
$$

Step 3: Recover the affine flag and its phase center.
Fix a nontrivial projective character direction $L$. Its $\ell-1$ nontrivial characters are Galois conjugate, and by (5) they have one common absolute value
$$
p_L\in\{q,q+2Q,q+4Q\}.
$$
Since $p_L$ is inert, $(M(\chi))=(p_L)$. Thus $M(\chi)/p_L$ is an algebraic integer all of whose conjugates have absolute value $1$, so it is a root of unity.

Let $\lambda=1-\zeta$. Every character value is $1$ modulo $\lambda$, hence
$$
M(\chi)\equiv m=2q^2\pmod\lambda.
$$
Also $p_L\equiv q\pmod\ell$, so
$$
\frac{M(\chi)}{p_L}\equiv2q\equiv1\pmod\lambda.
$$
The roots of unity in $\mathbb Q(\zeta)$ are $\pm\zeta^c$, and only $\zeta^c$ is congruent to $1$ modulo $\lambda$. Therefore every projective direction determines a distinguished affine hyperplane carrying the Fourier phase.

Let
$$
D=\frac{Q-1}{\ell-1},\qquad d_0=\frac{h-1}{\ell-1}.
$$
Let $e(z)$ count all $D$ distinguished affine hyperplanes through $z$, let $f(z)$ count those whose normals lie in $\mathbb P(\overline W^\perp)$, and let $I(z)$ indicate the distinguished hyperplane for $\overline U^\perp$. Fourier inversion gives
$$
Qm_z=m-qD-2Q(\ell+2)+\ell q\,e(z)+2\ell Q\,f(z)+2\ell Q\,I(z). \tag{7}
$$
Reducing modulo $Q$ gives $e(z)\equiv d_0\pmod h$. Since $0\le e(z)\le D=d_0+h$, every $e(z)$ is either $d_0$ or $D$. Counting incidences shows exactly one point has value $D$; call it $z_0$. Hence all distinguished affine hyperplanes meet at $z_0$, and
$$
f(z)=1+\ell 1_{z_0+\overline W}(z),\qquad I(z)=1_{z_0+\overline U}(z).
$$
Substitution into (7) gives
$$
m_z=d-4+2\ell^2 1_{z_0+\overline W}(z)+2\ell 1_{z_0+\overline U}(z)+q\delta_{z_0}(z). \tag{8}
$$
Taking the first moment and using (2) gives
$$
qz_0=Ps,\qquad z_0=q^{-1}Ps. \tag{9}
$$
The four multiplicity levels are $A,B,C,E$, so the profile recovers $z_0$ and the transformed flag. Conversely, every $s$ and transformed flag satisfying (6) gives exactly one profile of the form (8) with the required spectrum and first moment.

Step 4: Identify the conjugacy invariants.
Let $\tau\in\widetilde C_\pi$ have base permutation $c=\pi_\tau\in C_{S_n}(\pi)$. A direct conjugation calculation gives
$$
s_j'=s_j,\qquad Z_T'=Z_{c^{-1}T}. \tag{10}
$$
Hence $s$ and the multiplicity profile are invariants of a $\widetilde C_\pi$-conjugacy orbit.

Conversely, suppose two lifts have the same $s$ and the same profile. Since
$$
C_{S_n}(\pi)\cong C_2\wr S_m,
$$
the centralizer permutes the transposition blocks arbitrarily, so a base permutation can match equal labels. The remaining phase difference on each block is $(\delta,-\delta)$ in each Kummer family. A kernel element over $M$ removes these differences block by block. Thus two qualifying lifts are conjugate exactly when they have the same $s$ and the same multiplicity profile.

Step 5: Solve the affine recurrence and count the two flag regimes.
The new condition is
$$
\mathbf1\in\operatorname{span}\{s,Ps\}. \tag{11}
$$
If $s$ and $Ps$ are dependent, then (11) forces $s$ to be a scalar multiple of $\mathbf1$. Hence $Ps=s$, and there are exactly $\ell-1$ such phase vectors.

Now suppose $s,Ps$ are independent. Then (11) can be written uniquely in the form
$$
Ps=a\mathbf1+bs
$$
with $a\ne0$. Thus
$$
s_{j+1}=a+bs_j. \tag{12}
$$
If $b=0$, the sequence is constant. If $b=1$, periodicity gives $ra=0$; when $r\ne\ell$ this is impossible, while for $r=\ell$ the orbit $s_1,s_1+a,\ldots$ runs through all of $\mathbb F_\ell$ and contains $0$. Thus no nonconstant vector in $(\mathbb F_\ell^\times)^r$ arises from $b=0$ or $1$.

For $b\ne0,1$, put $c=a/(1-b)$. Then
$$
s_j=c+u b^{j-1},\qquad u=s_1-c\ne0. \tag{13}
$$
Periodicity forces $b^r=1$. Since $r$ is prime, every nontrivial such $b$ has order $r$. Therefore there are
$$
\gcd(r,\ell-1)-1
$$
possible values of $b$. For a fixed $b$, the $r$ values $b^{j-1}$ are distinct. Writing $x=-c/u$, condition $s_j\ne0$ for every $j$ is exactly
$$
x\notin\langle b\rangle.
$$
There are $\ell-r$ choices for $x$ and $\ell-1$ choices for $u$, so the number of independent phase vectors satisfying (11) is
$$
N_2=(\ell-1)(\gcd(r,\ell-1)-1)(\ell-r). \tag{14}
$$
The representation (13) determines $b$ uniquely for a nonconstant sequence because successive nonzero differences have constant ratio $b$, so there is no overcount.

For a constant phase vector, $H_s=\langle s,Ps\rangle$ is a line. The number of flags satisfying (6) is
$$
F_1=\ell^{r-2}\frac{\ell^{r-1}-1}{\ell-1}. \tag{15}
$$
For an independent phase vector, $H_s$ is a plane. The number of hyperplanes $\overline U$ containing it is $(\ell^{r-2}-1)/(\ell-1)$, and for each such $\overline U$ there are $(\ell-1)\ell^{r-3}$ hyperplanes $\overline W$ avoiding both $s$ and $Ps$. Hence
$$
F_2=\ell^{r-3}(\ell^{r-2}-1). \tag{16}
$$
Therefore the number of orbits is
$$
(\ell-1)F_1+N_2F_2
$$
$$
=\ell^{r-3}\left(\ell(\ell^{r-1}-1)+(\ell-1)(\gcd(r,\ell-1)-1)(\ell-r)(\ell^{r-2}-1)\right).
$$
Final Answer: $\boxed{\ell^{r-3}(\ell(\ell^{r-1}-1)+(\ell-1)(\gcd(r,\ell-1)-1)(\ell-r)(\ell^{r-2}-1))}$

---

## Answer

$\ell^{r-3}(\ell(\ell^{r-1}-1)+(\ell-1)(\gcd(r,\ell-1)-1)(\ell-r)(\ell^{r-2}-1))$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cyclic Kummer coupling of total phases
- three-level autocorrelation on a finite vector space
- affine-hyperplane phase recovery
- centralizer conjugation and orbit invariants
- periodic affine recurrences over finite fields
