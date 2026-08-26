## Steps

### Step 1: Kummer parameterization

By the assumed cubic-relation condition, the automorphisms fixing $\omega$ and inducing the fixed permutation $\pi$ are uniquely described by
$$
\sigma(\alpha_i)=\omega^{a_i}\alpha_{\pi(i)},
\qquad
\sigma(\beta_i)=\omega^{b_i}\beta_{\pi(i)},
$$
with
$$
\sum_i a_i=\sum_i b_i=0
$$
and
$$
\sigma(\rho_1)=\omega^s\rho_1,
\qquad
\sigma(\rho_2)=\omega^t\rho_2,
$$
where $(s,t)\in\mathbb F_3^2$.

The condition in the problem requires $s\neq0$ and $t\neq0$.

### Step 2: Fourier reduction

For each transposition $C$ of $\pi$, define
$$
A_C=\sum_{i\in C}a_i,
\qquad
B_C=\sum_{i\in C}b_i.
$$
The phase of a pair of transposition cycles depends only on the difference of the two-dimensional cycle labels
$$
Z_C=(A_C,B_C)\in\mathbb F_3^2.
$$

Let $m_z$ be the number of transpositions with label $z\in\mathbb F_3^2$. Since there are $2q^2$ transpositions,
$$
\sum_{z\in\mathbb F_3^2}m_z=2q^2.
$$

The equal-cycle-type condition for the nine sets $\Omega_{k,\ell}$ is equivalent to the vanishing of every nontrivial Fourier coefficient of the difference distribution:
$$
\sum_{z\in\mathbb F_3^2}m_z\chi(z)=0
$$
for every nontrivial character $\chi$ of $\mathbb F_3^2$.

Equivalently, the correlation counts
$$
\sum_z m_zm_{z+w}
$$
are independent of nonzero $w$.

### Step 3: Classify the transposition labels

Write the Fourier transform of $m$ as
$$
\widehat m(\chi)=\sum_zm_z\chi(z).
$$
The difference-set condition gives
$$
|\widehat m(\chi)|^2=\frac{(2q^2)^2}{8}
$$
for every nontrivial character. Since $q\equiv5\pmod9$, the integral solution in $\mathbb Z[\omega]$ is unique up to affine translation in $\mathbb F_3^2$:

- one phase class has size
$$
H_q=\frac{2q^2+8q}{9},
$$
- each of the remaining eight classes has size
$$
L_q=\frac{2q^2-q}{9}.
$$

Thus the transposition labels are exactly a translate of the profile
$$
(H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q).
$$

### Step 4: Count realizations

There are nine possible choices for the distinguished phase class. For each profile, the number of ways to assign the labels to the $2q^2$ transpositions is
$$
\binom{2q^2}{H_q,\underbrace{L_q,\ldots,L_q}_{8\text{ times}}}.
$$

For prescribed cycle labels, a transposition contributes one free phase coordinate. Hence the internal choices of $(a_i,b_i)$ contribute
$$
3^{2\cdot(2q^2)-2}=3^{4q^2-2},
$$
where the two subtracted dimensions are the global sum constraints.

The two nonzero twist parameters $s,t$ have four choices. Therefore the total contribution is
$$
36\cdot3^{4q^2-2}
\binom{2q^2}{H_q,\underbrace{L_q,\ldots,L_q}_{8\text{ times}}}.
$$

### Final Answer

$$
\boxed{
36\cdot3^{4q^2-2}
\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}
}
$$

---

## Answer

$$
36\cdot3^{4q^2-2}
\binom{2q^2}{H_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q,L_q}
$$

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
