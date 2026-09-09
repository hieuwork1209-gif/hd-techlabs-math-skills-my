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
be the quartic twist of the Fermat quartic over $\mathbb F_p$.

Choose integers $a,b$ uniquely by
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,\qquad br\equiv a\pmod p.
$$
Write the zeta function of $C_g$ as
$$
Z(C_g/\mathbb F_p,T)
=\exp\left(\sum_{n\ge1}\#C_g(\mathbb F_{p^n})\frac{T^n}{n}\right)
=\frac{L_{C_g}(T)}{(1-T)(1-pT)}.
$$
Determine the numerator polynomial $L_{C_g}(T)\in\mathbb Z[T]$ exactly.

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

The problem asks for the exact Frobenius zeta numerator of a natural quartic twist of the Fermat quartic over a finite field. Its evaluation uses quartic characters, Jacobi sums, Davenport--Hasse lifting across finite-field extensions, and the Gaussian prime above $p$ normalized by the chosen primitive root. The central arithmetic content is finite-field character-sum computation, so Number Theory -> Modular arithmetic and congruences is the appropriate classification.