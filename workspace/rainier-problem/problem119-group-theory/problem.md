# Normalized Math Problem

## LaTeX (Normalized)

Let $p\equiv1\pmod4$ be a prime and let $g$ be a primitive root modulo $p$. Put
$$
r=g^{(p-1)/4}\in\mathbb F_p,
$$
so $r^2=-1$. Let
$$
C_g:\ X^4+Y^4=gZ^4
$$
be the corresponding quartic twist of the Fermat quartic over $\mathbb F_p$.

Choose integers $a,b$ uniquely by
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,\qquad br\equiv a\pmod p.
$$
Determine the exact value of
$$
\#C_g(\mathbb F_p).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Modular arithmetic and congruences |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for an exact point count on a natural quartic twist of the Fermat quartic over $\mathbb F_p$. Its evaluation requires quartic multiplicative characters, Jacobi sums, and the normalization of a Gaussian prime above $p$ relative to the chosen primitive root. The main content is finite-field congruence counting, so Number Theory -> Modular arithmetic and congruences is the appropriate classification.