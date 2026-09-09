# Normalized Math Problem

## LaTeX (Normalized)

Let $p\equiv1\pmod4$ be a prime and let $g$ be a primitive root modulo $p$. Put
$$
r=g^{(p-1)/4}\in\mathbb F_p,
$$
so $r^2=-1$, and set
$$
s=(-1)^{(p-1)/4}.
$$
Choose integers $a,b$ uniquely by
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,\qquad br\equiv a\pmod p.
$$
Let
$$
S_g:\ X_0^4+X_1^4+X_2^4=gX_3^4
$$
be the smooth quartic surface over $\mathbb F_p$. Write its zeta function as
$$
Z(S_g/\mathbb F_p,T)
=\exp\left(\sum_{n\ge1}\#S_g(\mathbb F_{p^n})\frac{T^n}{n}\right)
=\frac{1}{(1-T)P_{2,S_g}(T)(1-p^2T)},
$$
where $P_{2,S_g}(T)\in\mathbb Z[T]$ has degree $22$.

Determine $P_{2,S_g}(T)$ exactly.

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

The problem asks for the exact middle Frobenius polynomial of a natural diagonal quartic K3 surface over a finite field. Its evaluation uses quartic characters, higher Jacobi sums, Davenport--Hasse lifting, and the Gaussian prime above $p$ normalized by the chosen primitive root. The central arithmetic content is finite-field character-sum computation, so Number Theory -> Modular arithmetic and congruences is the appropriate classification.