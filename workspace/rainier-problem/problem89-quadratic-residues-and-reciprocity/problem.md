# Normalized Math Problem

## LaTeX (Normalized)

Let $p$ be an odd prime with $p\ne 5$. For each integer $m\ge 0$, define
$$
r_m(p)=\#\left\{(x,y)\in\mathbb Z^2:x^2+5y^2=p^m\right\}.
$$
Form the ordinary generating function
$$
R_p(T)=\sum_{m=0}^{\infty}r_m(p)T^m.
$$
Determine $R_p(T)$ explicitly as a rational function of $T$ for every possible residue class of $p$ modulo $20$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Quadratic residues and reciprocity |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Polynomial or rational function |

---

## Domain Explanation

The problem asks for prime-power representation counts by the binary quadratic form $x^2+5y^2$, whose discriminant is $-20$. The decisive arithmetic is the quadratic-residue behavior of $-5$ and $5$ modulo $p$: quadratic reciprocity determines whether $p$ is inert or split in $\mathbb Q(\sqrt{-5})$, and among split primes the residue class modulo $20$ distinguishes the principal form $x^2+5y^2$ from the other class of discriminant $-20$. The generating function only packages these residue-controlled local representation counts, so Quadratic residues and reciprocity is more precise than the broader Multiplicative functions alternative.
