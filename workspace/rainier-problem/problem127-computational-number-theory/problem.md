# Normalized Math Problem

## LaTeX (Normalized)

Let $p$ be a prime and let $n\ge1$. Determine the number $N_n(p)$ of ordered pairs
$$
(x,y)\in(\mathbb Z/p^n\mathbb Z)^2
$$
satisfying
$$
x^2\equiv y^3\pmod{p^n}.
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

This problem is primarily Number Theory and Computational number theory: it asks for an exact count of solutions to a singular polynomial congruence modulo the prime powers $p^n$. The count is controlled by the possible $p$-adic valuations of the coordinates, the unit solutions that remain after dividing out those valuations, and the number of lifts back to the original modulus.
