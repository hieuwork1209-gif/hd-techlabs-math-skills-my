## Steps

Step 1: Parameterize the lifts and attach a phase to each transposition.
By the cubic-relation hypothesis, every automorphism inducing the fixed $\pi$ is uniquely of the form
$$
\sigma(\alpha_i)=\omega^{a_i}\alpha_{\pi(i)},\qquad
\sigma(\beta_i)=\omega^{b_i}\beta_{\pi(i)},
$$
with $a_i,b_i\in\mathbb F_3$ and
$$
\sum_i a_i=\sum_i b_i=0,
$$
together with
$$
\sigma(\rho_1)=\omega^s\rho_1,\qquad
\sigma(\rho_2)=\omega^t\rho_2.
$$
We require $s,t\neq0$. For each transposition $C$ of $\pi$, put
$$
Z_C=(A_C,B_C)=\left(\sum_{i\in C}a_i,\sum_{i\in C}b_i\right)\in G:=\mathbb F_3^2.
$$
Let $m_z$ be the number of transpositions with label $z\in G$. Then
$$
\sum_zm_z=2q^2,
\qquad
\sum_zm_zz=(0,0).
$$

Step 2: Convert equal cycle types into an autocorrelation condition on $G$.
Every ordered pair $(i,j)$ with $i\neq j$ lies in a $\pi$-orbit of length $2$. Over such an orbit, the fiber $(u,v)\in G$ is translated after two steps by its intrinsic phase difference plus
$$
(2ks,2\ell t).
$$
If the resulting vector is $0$, the corresponding part of $\Omega_{k,\ell}$ gives nine $2$-cycles; otherwise it gives three $6$-cycles. Since $s,t\neq0$, as $(k,\ell)$ varies the twist vector runs through all of $G$.

Put $m=2q^2$ and
$$
N_w=\sum_{z\in G}m_zm_{z+w}.
$$
For twist $0$, the number of base pair-orbits with zero accumulated phase is
$$
2N_0-m,
$$
while for a nonzero twist $w$ it is $2N_w$. Hence all nine induced permutations have the same cycle type exactly when
$$
N_0-N_w=\frac m2=q^2
\qquad(w\neq0).
$$
For a character $\chi$ of $G$, define
$$
\widehat m(\chi)=\sum_zm_z\chi(z).
$$
The Fourier transform of $N_w$ is $|\widehat m(\chi)|^2$, so the preceding condition is equivalent, for every nontrivial $\chi$, to
$$
|\widehat m(\chi)|^2=q^2.
$$

Step 3: Classify the integral phase profiles.
For nontrivial $\chi$, $\widehat m(\chi)\in\mathbb Z[\omega]$ has norm $q^2$. Since $q\equiv2\pmod3$, the prime $q$ is inert in $\mathbb Z[\omega]$, so
$$
\widehat m(\chi)=q\varepsilon
$$
for a unit $\varepsilon$. Modulo $1-\omega$,
$$
\widehat m(\chi)\equiv\sum_zm_z=2q^2\equiv q,
$$
so only $\varepsilon\in\{1,\omega,\omega^2\}$ is possible. Thus, for each of the four character directions of $G$, one of its three parallel affine lines is distinguished: its total multiplicity exceeds each of the other two line totals by $q$.

Choose those four distinguished lines and let $d(z)$ be the number of them passing through $z$. Fourier inversion gives
$$
9m_z=2q^2+q(3d(z)-4).
$$
Because $q\equiv5\pmod9$, integrality forces
$$
d(z)\equiv1\pmod3.
$$
As $0\le d(z)\le4$, every $d(z)$ is $1$ or $4$. The four selected lines contain $12$ point-line incidences, so exactly one point $z_0$ has $d(z_0)=4$, and every other point has $d(z)=1$. Therefore
$$
m_{z_0}=H_q=\frac{2q^2+8q}{9},
\qquad
m_z=L_q=\frac{2q^2-q}{9}\quad(z\neq z_0).
$$
Finally,
$$
\sum_zm_zz=(H_q-L_q)z_0=qz_0.
$$
The global phase relation from Step 1 says this sum is $0$ in $G$, and $q\not\equiv0\pmod3$, hence $z_0=0$. Thus the zero phase occurs $H_q$ times and each of the other eight phases occurs $L_q$ times.

Step 4: Count the automorphisms.
The labels can be assigned to the $2q^2$ transpositions in
$$
\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}
$$
ways. Once a transposition label $(A_C,B_C)$ is fixed, its two $a_i$ values have $3$ choices with sum $A_C$, and independently its two $b_i$ values have $3$ choices with sum $B_C$. Thus all transpositions contribute
$$
9^{2q^2}=3^{4q^2}
$$
phase assignments. There are $2$ choices for each of the nonzero twists $s$ and $t$, hence $4$ twist choices. Therefore the required count is
$$
4\cdot3^{4q^2}\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}
=36\cdot3^{4q^2-2}\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}.
$$
Final Answer: $\boxed{36\cdot3^{4q^2-2}\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}}$

---

## Answer

$36\cdot3^{4q^2-2}\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- two-dimensional cubic Kummer extensions
- Fourier analysis on $\mathbb F_3^2$
- difference sets
- character sums
- multinomial counting
