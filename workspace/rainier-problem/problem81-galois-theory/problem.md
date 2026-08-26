# Normalized Math Problem

## LaTeX (Normalized)

Let $q$ be a rational prime with $q\equiv2\pmod3$, and put $n=79q^2$. Let $f\in\mathbb Q[y]$ be monic of degree $n$, and suppose its splitting field $K$ satisfies
$$
\operatorname{Gal}(K/\mathbb Q)\cong S_n
$$
through its action on the roots $y_1,\ldots,y_n$ of $f$. Write $\Delta$ for the discriminant of $f$.

Let $a,c\in\mathbb Q^\times$ satisfy
$$
(-1)^n f(-a)=c^3,
$$
and suppose that $-3\Delta$ is not a square in $\mathbb Q$.

Assume there is a prime $p\equiv1\pmod3$ such that the coefficients of $f$ and the number $a$ are $p$-integral, meaning their denominators are not divisible by $p$, and
$$
p\nmid \Delta f(-a).
$$
Suppose further that
$$
f(y)\equiv(y-u)(y-v)h(y)\pmod p,
$$
where $u,v\in\mathbb F_p$ are distinct, $h\in\mathbb F_p[y]$ is irreducible of degree $n-2$, $a+u$ is not a cube in $\mathbb F_p^\times$, and $a+v$ is a cube in $\mathbb F_p^\times$.

For ordered pairs $i\neq j$, put
$$
B_{ij}=\frac{a+y_i}{a+y_j},
$$
and define
$$
R(z)=\prod_{i\neq j}(z-B_{ij})\in\mathbb Q[z],
\qquad
N=n(n-1).
$$
For $k\in\{0,1,2\}$, set
$$
P_k(x)=p^{kN}R\left(\frac{x^3}{p^k}\right),
$$
and let $L$ be the splitting field of
$$
f(y)P_0(x)P_1(x)P_2(x)
$$
over $\mathbb Q$. Let $\omega\in L$ be a primitive cube root of unity. For $\sigma\in\operatorname{Gal}(L/\mathbb Q)$, let $\pi_\sigma\in S_n$ be the permutation induced by restricting $\sigma$ to $K$.

Fix a permutation $\pi\in S_n$ having exactly $2q^2$ cycles of length $2$ and exactly $15q^2$ cycles of length $5$. Determine the number of automorphisms $\sigma\in\operatorname{Gal}(L/\mathbb Q)$ such that $\sigma$ fixes $\omega$, $\pi_\sigma=\pi$, and the three permutations induced by $\sigma$ on the roots of $P_0$, $P_1$, and $P_2$ have the same cycle type.

Use the multinomial notation
$$
\binom{m}{r,s,t}=\frac{m!}{r!s!t!},
$$
and set
$$
A_q=\frac{q(2q-1)}{3}.
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

This problem belongs to abstract algebra because it counts lifts of a prescribed permutation through a radical extension of a symmetric splitting field. Its primary sub-domain is Galois theory, since the main work is to determine the radical kernel and translate field automorphisms into orbit data. The number-theoretic norm argument is a supporting classification tool rather than the object being studied.
