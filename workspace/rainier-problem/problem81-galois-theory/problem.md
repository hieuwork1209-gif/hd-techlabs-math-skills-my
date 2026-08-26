# Normalized Math Problem

## LaTeX (Normalized)

Let $q$ be a rational prime with
$$
q\equiv5\pmod9,
$$
and put $n=4q^2$. Let $K/\mathbb Q$ be a Galois extension together with a fixed identification
$$
\operatorname{Gal}(K/\mathbb Q)\cong S_n,
$$
where $S_n$ acts naturally on $[n]=\{1,\ldots,n\}$. Let $\omega$ be a primitive cube root of unity, assume $\omega\notin K$, and put $M=K(\omega)$.

Choose elements
$$
g_1,\ldots,g_n,h_1,\ldots,h_n\in K^\times
$$
such that for every $\tau\in S_n$,
$$
\tau(g_i)=g_{\tau(i)},
\qquad
\tau(h_i)=h_{\tau(i)}.
$$
Choose $p_1,p_2\in\mathbb Q^\times$. Assume that the cubic relations among these elements are exactly the following: for
$$
a_i,b_i,s,t\in\mathbb F_3,
$$
the element
$$
p_1^s p_2^t\prod_{i=1}^n g_i^{a_i}h_i^{b_i}
$$
is a cube in $M$ if and only if
$$
s=t=0
$$
and there exist $\lambda,\mu\in\mathbb F_3$ such that
$$
a_1=\cdots=a_n=\lambda,
\qquad
b_1=\cdots=b_n=\mu.
$$

Choose cube roots
$$
\alpha_i^3=g_i,
\qquad
\beta_i^3=h_i,
\qquad
\rho_1^3=p_1,
\qquad
\rho_2^3=p_2,
$$
with $\prod_i\alpha_i,\prod_i\beta_i\in M$, and put
$$
L=M(\alpha_1,\ldots,\alpha_n,\beta_1,\ldots,\beta_n,\rho_1,\rho_2).
$$
For $\sigma\in\operatorname{Gal}(L/\mathbb Q(\omega))$, let $\pi_\sigma\in S_n$ be its restriction to $M$.

Fix a permutation $\pi\in S_n$ consisting of exactly $2q^2$ disjoint transpositions. For $(k,\ell)\in\mathbb F_3^2$, define the finite set
$$
\Omega_{k,\ell}
=
\left\{
\left(
\omega^u\rho_1^k\frac{\alpha_i}{\alpha_j},
\omega^v\rho_2^\ell\frac{\beta_i}{\beta_j}
\right)
:
i\neq j,\ u,v\in\mathbb F_3
\right\}.
$$
The assumed cubic-relation condition implies that the displayed elements are distinct, so each $\Omega_{k,\ell}$ has $9n(n-1)$ elements and is stable under $\operatorname{Gal}(L/\mathbb Q(\omega))$.

Determine the number of automorphisms $\sigma\in\operatorname{Gal}(L/\mathbb Q(\omega))$ such that
$$
\pi_\sigma=\pi,
\qquad
\sigma(\rho_1)\neq\rho_1,
\qquad
\sigma(\rho_2)\neq\rho_2,
$$
and the nine permutations induced by $\sigma$ on the sets
$$
\Omega_{k,\ell},
\qquad
(k,\ell)\in\mathbb F_3^2,
$$
all have the same cycle type.

Use the multinomial notation
$$
\binom{m}{m_1,\ldots,m_9}
=
\frac{m!}{m_1!\cdots m_9!},
$$
and set
$$
H_q=\frac{2q^2+8q}{9},
\qquad
L_q=\frac{2q^2-q}{9}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Abstract Algebra |
| **Sub-domain** | Galois theory |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is a Galois-theoretic counting problem for a two-dimensional cubic Kummer kernel. The cycle-type constraint becomes a correlation problem on the phase group $\mathbb F_3^2$, and its classification requires Fourier analysis on that group together with norms in the Eisenstein integers.