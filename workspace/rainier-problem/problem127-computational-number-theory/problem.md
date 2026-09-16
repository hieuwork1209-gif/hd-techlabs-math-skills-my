# Normalized Math Problem

## LaTeX (Normalized)

Let $p$ be an odd prime and let $n\ge1$. Define
$$
L_p=\left(\frac{-1}{p}\right).
$$
Determine the number $M_n(p)$ of ordered pairs
$$
(x,y)\in(\mathbb Z/p^n\mathbb Z)^2
$$
satisfying
$$
x^2\equiv y^3\pmod{p^n}
$$
and
$$
x+y\equiv2\pmod{p^n}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Computational number theory |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Number Theory and Computational number theory: it asks for an exact count of solutions to two simultaneous congruences modulo the prime powers $p^n$. The cusp equation admits a multiplicative unit parametrization, while the affine constraint converts the count into a prime-power root-lifting problem with a singular exceptional prime that must be analyzed separately.
