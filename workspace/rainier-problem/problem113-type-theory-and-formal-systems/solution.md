## Steps

Step 1: Separate each interchange into a swap and a family of translation seeds
Read a term as a word in the unary symbols, suppressing the terminal $z$. The rules are
$$
d_q a\longrightarrow a^2d_q,
\qquad
d_qd_p\longrightarrow a^{q-p}d_pd_q\quad(p<q).
$$
Deleting all $a$'s leaves a permutation of the labels $2,3,\ldots,n$. The first rule does not change this permutation, while the second rule swaps one adjacent inversion. Hence every complete reduction uses exactly
$$
\binom{n-1}{2}
$$
interchange steps.

Consider one of the $q-p$ copies of $a$ created when $d_qd_p$ is interchanged. Suppose that, in the $d$-subword at that moment, the swapped pair occupies positions $k,k+1$, counted from $0$. Thus exactly $k$ constructors $d_r$ lie outside this new copy of $a$. Track only the descendants of this one copy. Passing the innermost remaining $d_r$ across it costs one first-rule step and replaces it by two descendants. Therefore, if $C_k$ is the number of first-rule steps forced by one such seed with $k$ outer $d$'s, then
$$
C_0=0,\qquad C_k=1+2C_{k-1}.
$$
Thus
$$
C_k=2^k-1.
$$
The genealogy of different seeds is disjoint, so an interchange $d_qd_p\to a^{q-p}d_pd_q$ made at cut $k$ contributes exactly
$$
(q-p)(2^k-1)
$$
future first-rule steps, independent of how those steps are interleaved with the rest of the reduction.

Step 2: Determine the total label difference that can cross each cut
Let the current $d$-subword be
$$
\pi_0,\pi_1,\ldots,\pi_{n-2},
$$
and for $0\leq k\leq n-3$ define the prefix sum
$$
P_k=\pi_0+\pi_1+\cdots+\pi_k.
$$
A swap at any cut other than $k$ leaves $P_k$ unchanged. If a swap at cut $k$ changes adjacent labels $q,p$ with $q>p$, then $P_k$ decreases by exactly $q-p$. Consequently the sum of all quantities $q-p$ over swaps occurring at cut $k$ is forced by the initial and final $d$-orders.

Initially the order is $n,n-1,\ldots,2$, whereas every normal form has order $2,3,\ldots,n$. Hence
$$
\sum_{\substack{\text{swaps at}\\\text{cut }k}}(q-p)
=P_k^{\mathrm{initial}}-P_k^{\mathrm{final}}.
$$
The two prefix sums are
$$
P_k^{\mathrm{initial}}=\frac{(k+1)(2n-k)}2,
\qquad
P_k^{\mathrm{final}}=\frac{(k+1)(k+4)}2,
$$
so
$$
\sum_{\substack{\text{swaps at}\\\text{cut }k}}(q-p)
=(k+1)(n-k-2).
$$
This is the load-bearing point: the amount of translation created at a cut is not chosen by the reduction order; it is encoded by the change of that prefix sum.

Step 3: Count all first-rule steps
By Step 1, every unit of translation created at cut $k$ generates exactly $2^k-1$ first-rule steps. By Step 2, the total translation created there is $(k+1)(n-k-2)$. Therefore every complete reduction uses exactly
$$
E_n=\sum_{k=0}^{n-3}(2^k-1)(k+1)(n-k-2)
$$
applications of the first rule.

To evaluate the sum, expand
$$
(k+1)(n-k-2)=-k^2+(n-3)k+(n-2)
$$
and use, for $N=n-3$,
$$
\sum_{k=0}^{N}2^k=2^{N+1}-1,
$$
$$
\sum_{k=0}^{N}k2^k=(N-1)2^{N+1}+2,
$$
$$
\sum_{k=0}^{N}k^22^k=(N^2-2N+3)2^{N+1}-6,
$$
together with the standard polynomial sums for $1,k,k^2$. Simplification gives
$$
E_n=2^{n-1}(n-4)-\frac{n^3}{6}+\frac{n^2}{2}+\frac{2n}{3}+2.
$$

Step 4: Add the interchange steps
Every complete reduction has the same number of steps: the $E_n$ first-rule steps from Step 3 plus the $\binom{n-1}{2}$ interchange steps from Step 1. In particular this common value is the minimum $L_n$. Thus
$$
L_n
=E_n+\binom{n-1}{2}
=2^{n-1}(n-4)-\frac{n^3}{6}+n^2-\frac{5n}{6}+3.
$$
Final Answer: $\boxed{2^{n-1}(n-4)-\frac{n^3-6n^2+5n-18}{6}}$

---

## Answer

$2^{n-1}(n-4)-\frac{n^3-6n^2+5n-18}{6}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- term rewriting systems
- affine rewrite semantics
- reduction genealogy
- prefix-sum invariants
- inversion counting
