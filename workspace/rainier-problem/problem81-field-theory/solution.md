## Steps

Step 1: Parameterize the lifts.
Let $\ell$ be the prime in the statement, let $\zeta=\zeta_\ell$, and put
$$
Q=\ell^r,\qquad m=2q^2,\qquad D=\frac{Q-1}{\ell-1}.
$$
For $1\le j\le r$, the relation hypothesis in $M^\times/(M^\times)^\ell$ shows by Kummer theory that a lift $\sigma$ of the fixed $\pi$ is uniquely described by
$$
\sigma(\alpha_i^{(j)})=\zeta^{a_i^{(j)}}\alpha_{\pi(i)}^{(j)},
\qquad
\sigma(\rho_j)=\zeta^{s_j}\rho_j,
$$
with $a_i^{(j)},s_j\in\mathbb F_\ell$ and
$$
\sum_{i=1}^n a_i^{(j)}=0\qquad(1\le j\le r).
$$
Here is the constraint explicitly. Put $A_j=\prod_i\alpha_i^{(j)}\in M$. Its $\ell$th power $\prod_i g_i^{(j)}$ is fixed by $S_n$, hence lies in $\mathbb Q^\times$. For $\tau\in\operatorname{Gal}(M/\mathbb Q(\zeta))\cong S_n$, the quotient $\tau(A_j)/A_j\in\mu_\ell$ defines a homomorphism $S_n\to\mu_\ell$. Since $S_n^{\rm ab}\cong C_2$ and $\ell$ is odd, this homomorphism is trivial. Thus $A_j$ is fixed and the displayed sum is $0$. Conversely, the class span is $\pi$-stable, so the lifts form a torsor under the Kummer kernel and these are the only constraints. The condition $\sigma(\rho_j)\ne\rho_j$ is exactly $s_j\ne0$.

For each transposition $C$ of $\pi$, define its label
$$
Z_C=\left(\sum_{i\in C}a_i^{(1)},\ldots,\sum_{i\in C}a_i^{(r)}\right)\in G:=\mathbb F_\ell^r.
$$
If $m_z$ is the number of transpositions carrying label $z$, then
$$
\sum_{z\in G}m_z=m,
\qquad
\sum_{z\in G}m_zz=0.
$$

Step 2: Convert equal cycle types to flat Fourier magnitude.
For $k\in G$, the action on the fiber coordinate $u\in G$ above an ordered pair $(i,h)$ is
$$
(i,h,u)\longmapsto
\left(\pi(i),\pi(h),u+(k_js_j+a_i^{(j)}-a_h^{(j)})_{j=1}^r\right).
$$
If $i$ lies in transposition $C$ and $h$ in transposition $E$, then after two steps the fiber is translated by
$$
2(k_1s_1,\ldots,k_rs_r)+Z_C-Z_E.
$$
A zero translation gives $Q$ cycles of length $2$ over that base orbit, whereas a nonzero translation has additive order $\ell$ and gives $Q/\ell$ cycles of length $2\ell$. Since $2s_j\ne0$, the twist vector runs through all of $G$ as $k$ varies.

Set
$$
N_w=\sum_{z\in G}m_zm_{z+w}.
$$
For twist $0$, the number of base pair-orbits with zero accumulated phase is $2N_0-m$; for $w\ne0$ it is $2N_w$. Hence all $Q$ induced permutations have the same cycle type exactly when
$$
N_0-N_w=q^2\qquad(w\ne0).
$$
For a character $\chi$ of $G$, define
$$
\widehat m(\chi)=\sum_zm_z\chi(z).
$$
Taking the Fourier transform of the autocorrelation gives, for every nontrivial $\chi$,
$$
|\widehat m(\chi)|^2=q^2.
$$

Step 3: Recover the phase profile through the cyclotomic field.
Fix a nontrivial character $\chi(z)=\zeta^{\lambda(z)}$ with nonzero linear form $\lambda:G\to\mathbb F_\ell$, and put
$$
z_\chi=\widehat m(\chi)\in\mathbb Z[\zeta].
$$
For $a\in\mathbb F_\ell^\times$, the Galois automorphism $\zeta\mapsto\zeta^a$ sends $z_\chi$ to $\widehat m(\chi^a)$, whose complex absolute value is again $q$. Thus every one of the $\ell-1$ conjugates of $z_\chi$ has absolute value $q$, so
$$
N_{\mathbb Q(\zeta)/\mathbb Q}(z_\chi)=q^{\ell-1}.
$$

We next show that $q$ is inert in $\mathbb Z[\zeta]$. The congruence $2q\equiv1\pmod\ell$ gives $q\equiv2^{-1}\pmod\ell$. Since $2$ generates $\mathbb F_\ell^\times$, so does $q$, hence $q$ has order $\ell-1$ modulo $\ell$. A primitive $\ell$th root of unity lies in $\mathbb F_{q^d}$ exactly when $\ell\mid q^d-1$; the least such $d$ is therefore $\ell-1$. Thus the degree-$\ell+1-2=\ell-1$ polynomial $\Phi_\ell$ is irreducible modulo $q$, and
$$
\mathbb Z[\zeta]/(q)\cong\mathbb F_{q^{\ell-1}}.
$$
In particular $(q)$ is prime. Reducing multiplication by $z_\chi$ modulo $q$, its determinant is the algebraic norm modulo $q$, hence is $0$. Multiplication by a nonzero element of a field is invertible, so $z_\chi\equiv0\pmod q$. Therefore
$$
z_\chi=q\varepsilon_\chi
$$
with $\varepsilon_\chi\in\mathbb Z[\zeta]$ an algebraic integer all of whose conjugates have absolute value $1$.

We use the following elementary form of Kronecker's lemma. If an algebraic integer $\varepsilon$ has all conjugates of absolute value $1$, then $\varepsilon$ is a root of unity: for every $n\ge1$, the monic polynomial whose roots are the conjugates of $\varepsilon^n$ has integral coefficients, and each coefficient is bounded in absolute value by a binomial coefficient depending only on the degree. Only finitely many such polynomials occur, hence only finitely many values $\varepsilon^n$ occur, so two powers coincide.

Let $\mathfrak l=(1-\zeta)$. Since $\mathbb Z[\zeta]/\mathfrak l\cong\mathbb F_\ell$, every character value is $1$ modulo $\mathfrak l$. Hence
$$
z_\chi\equiv\sum_zm_z=2q^2\pmod{\mathfrak l}.
$$
Because $2q\equiv1\pmod\ell$ and $q\not\equiv0\pmod\ell$, division by $q$ gives
$$
\varepsilon_\chi\equiv1\pmod{\mathfrak l}.
$$
A root of unity in $\mathbb Q(\zeta)$ with this congruence must be an $\ell$th root of unity. Indeed, if its order is $\ell^a s$ with $(s,\ell)=1$, its $s$-primary part $\eta$ is also $1$ modulo $\mathfrak l$. If $s>1$, then $1+\eta+\cdots+\eta^{s-1}=0$, while reduction modulo $\mathfrak l$ gives $s\ne0$, a contradiction. Thus the order is an $\ell$-power. It cannot be divisible by $\ell^2$, since a primitive $\ell^2$th root has degree $\ell(\ell-1)>[\mathbb Q(\zeta):\mathbb Q]$. Therefore
$$
\widehat m(\chi)=q\zeta^{c_\chi}
$$
for some $c_\chi\in\mathbb F_\ell$.

Now group the nonzero characters into the $D$ one-dimensional directions of the dual space. For a representative $\lambda$ of one direction, write
$$
S_t=\sum_{\lambda(z)=t}m_z\qquad(t\in\mathbb F_\ell).
$$
If $\widehat m(\lambda)=q\zeta^c$, then its powers give $q\zeta^{ac}$ for $a\ne0$. The $\ell$-term inverse Fourier transform shows that exactly one affine hyperplane $\lambda(z)=c$ has total
$$
\frac{2q^2+(\ell-1)q}{\ell},
$$
and each of the other $\ell-1$ parallel hyperplanes has total $(2q^2-q)/\ell$. Call the first one distinguished.

Let $d(z)$ be the number of distinguished hyperplanes, one from each of the $D$ directions, that contain $z$. Fourier inversion grouped by directions gives
$$
Qm_z=2q^2+q(\ell d(z)-D).
$$
Because $m_z$ is integral and $q$ is prime to $Q$,
$$
2q+\ell d(z)-D\equiv0\pmod Q.
$$
Using $2q\equiv1\pmod Q$ and
$$
D-1=\ell d_0,\qquad d_0:=\frac{\ell^{r-1}-1}{\ell-1},
$$
we get
$$
d(z)\equiv d_0\pmod{\ell^{r-1}}.
$$
Since $0\le d(z)\le D=d_0+\ell^{r-1}$, every point has $d(z)=d_0$ or $d(z)=D$. The $D$ distinguished hyperplanes contain $D\ell^{r-1}$ incidences. If $x$ points have value $D$, then
$$
xD+(Q-x)d_0=D\ell^{r-1}.
$$
Using $D-d_0=\ell^{r-1}$ and $D-\ell d_0=1$ gives $x=1$. Thus there is a unique point $z_0$ lying on every distinguished hyperplane.

Define
$$
H=\frac{2q^2+(Q-1)q}{Q},\qquad
L_0=\frac{2q^2-q}{Q}.
$$
Then
$$
m_{z_0}=H,\qquad m_z=L_0\quad(z\ne z_0).
$$
These are integers because $Q\mid2q-1$, and $H-L_0=q$. Also $\sum_{z\in G}z=0$, so the global phase constraint becomes
$$
0=\sum_zm_zz=qz_0.
$$
As $q\not\equiv0\pmod\ell$, we get $z_0=0$. Conversely, this heavy-at-zero profile has every nontrivial Fourier coefficient equal to $q$, so it satisfies the required cycle condition.

Step 4: Count the lifts.
The transposition labels can be assigned in
$$
\frac{(2q^2)!}{H!(L_0!)^{Q-1}}
$$
ways. Once a label is fixed, for each transposition and each of the $r$ Kummer families there are exactly $\ell$ ordered phase pairs with the prescribed sum. Hence the internal phase choices contribute
$$
\ell^{rm}=\ell^{2rq^2}.
$$
Finally, each $s_j$ has $\ell-1$ nonzero choices, contributing $(\ell-1)^r$. Therefore
$$
\boxed{(\ell-1)^r\ell^{2rq^2}\frac{(2q^2)!}{H!(L_0!)^{Q-1}}}.
$$
Final Answer: $\boxed{(\ell-1)^r\ell^{2rq^2}\frac{(2q^2)!}{H!(L_0!)^{Q-1}}}$

---

## Answer

$(\ell-1)^r\ell^{2rq^2}(2q^2)!/[H!(L_0!)^{Q-1}]$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Kummer extensions of prime degree
- cyclotomic inertness, algebraic norms, and Kronecker's lemma
- finite Fourier analysis on $\mathbb F_\ell^r$
- affine-hyperplane incidence
- multinomial counting
