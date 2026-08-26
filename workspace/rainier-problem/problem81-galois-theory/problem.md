# Normalized Math Problem

## LaTeX (Normalized)

Let $q$ be a prime with $q\equiv5\pmod9$ and put $n=4q^2$. Let $K/\mathbb Q$ be Galois with $\operatorname{Gal}(K/\mathbb Q)\cong S_n$ acting on $[n]$, let $\omega\notin K$ be a primitive cube root of unity, and put $M=K(\omega)$.

Choose $g_i,h_i\in K^\times$ $(1\le i\le n)$ with $\tau(g_i)=g_{\tau(i)}$ and $\tau(h_i)=h_{\tau(i)}$ for every $\tau\in S_n$, and choose $p_1,p_2\in\mathbb Q^\times$. Assume
$$
p_1^sp_2^t\prod_i g_i^{a_i}h_i^{b_i}\in(M^\times)^3
$$
for $a_i,b_i,s,t\in\mathbb F_3$ iff $s=t=0$ and there are $\lambda,\mu\in\mathbb F_3$ with $a_i=\lambda,\ b_i=\mu$ for all $i$.

Choose $\alpha_i^3=g_i,\ \beta_i^3=h_i,\ \rho_1^3=p_1,\ \rho_2^3=p_2$, with $\prod_i\alpha_i,\prod_i\beta_i\in M$, and set
$$
L=M(\alpha_1,\ldots,\alpha_n,\beta_1,\ldots,\beta_n,\rho_1,\rho_2).
$$
For $\sigma\in\operatorname{Gal}(L/\mathbb Q(\omega))$, let $\pi_\sigma\in S_n$ be its restriction to $M$.

Fix $\pi\in S_n$ consisting of $2q^2$ transpositions. For $(k,\ell)\in\mathbb F_3^2$, let
$$
\Omega_{k,\ell}=\left\{\left(\omega^u\rho_1^k\frac{\alpha_i}{\alpha_j},\omega^v\rho_2^\ell\frac{\beta_i}{\beta_j}\right):i\ne j,\ u,v\in\mathbb F_3\right\}.
$$
The relation hypothesis implies these elements are distinct.

Determine the number of $\sigma\in\operatorname{Gal}(L/\mathbb Q(\omega))$ such that $\pi_\sigma=\pi$, $\sigma(\rho_1)\ne\rho_1$, $\sigma(\rho_2)\ne\rho_2$, and the nine induced permutations on $\Omega_{k,\ell}$ have the same cycle type.

Use $\binom{m}{m_1,\ldots,m_9}=m!/(m_1!\cdots m_9!)$ and set
$$
H_q=\frac{2q^2+8q}{9},\qquad L_q=\frac{2q^2-q}{9}.
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