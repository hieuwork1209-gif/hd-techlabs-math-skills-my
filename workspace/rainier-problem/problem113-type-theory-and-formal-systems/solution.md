## Steps

Step 1: Charge every first-rule step to the swap that created its ancestor
Suppress the terminal $z$ and read a term as a word in the unary symbols. The rules are
$$
d_q a\longrightarrow a^2d_q,
\qquad
d_qd_p\longrightarrow a d_pd_q\quad(p<q).
$$
Deleting all $a$'s leaves a permutation of $d_2,\ldots,d_n$. The first rule does not change that permutation, while the second rule swaps one adjacent inversion. Hence every complete reduction swaps each inverted pair exactly once.

There are no $a$'s initially, so every occurrence of $a$ descends from the unique $a$ created by some swap. Suppose a swap is made at cut $k$, meaning that exactly $k$ $d$-symbols lie outside the swapped pair. Let $C_k$ be the number of future first-rule steps forced by the descendants of that one new $a$. Then
$$
C_0=0,
\qquad
C_k=1+2C_{k-1}.
$$
Indeed, the innermost of the $k$ outer $d$'s crosses the seed once and creates two descendants, each still lying inside the remaining $k-1$ outer $d$'s. Therefore
$$
C_k=2^k-1.
$$
Including the swap that created the seed, a swap performed at cut $k$ accounts for exactly
$$
1+C_k=2^k
$$
steps. Distinct seeds have disjoint genealogies, so the total reduction length is the sum of these weights over all $d$-$d$ swaps.

Step 2: Reduce the problem to a weighted adjacent-swap sort
Put $m=n-1$ and relabel the $d$-symbols by $m,m-1,\ldots,1$. A complete reduction induces a sequence of adjacent inversion swaps sorting
$$
m,m-1,\ldots,1
$$
into increasing order. A swap across cut $k$ (between positions $k$ and $k+1$, counted from $0$) has weight $2^k$ by Step 1.

Let $W_m$ be the minimum possible total weight of such a sorting sequence. Consider the largest label $m$. It starts in the leftmost position and ends in the rightmost position, so it must cross the other $m-1$ labels once each. Its successive swaps necessarily occur across cuts
$$
0,1,\ldots,m-2,
$$
and therefore have the fixed total weight
$$
1+2+\cdots+2^{m-2}=2^{m-1}-1.
$$

Now delete the label $m$ from an arbitrary sorting sequence and omit all swaps involving it. The remaining swaps still sort the reverse permutation on $m-1$ labels. If one of those swaps occurred at cut $k$ before deletion, then after deleting $m$ its cut is either $k$ or $k-1$. Hence its weight in the reduced $(m-1)$-label problem is at most its original weight. Consequently
$$
W_m\ge (2^{m-1}-1)+W_{m-1}.
$$

Step 3: Attain the recurrence and solve it
The lower bound is attainable: first move the largest label $m$ all the way to the right, using the cuts $0,1,\ldots,m-2$, and then use an optimal sequence for the remaining reverse permutation of size $m-1$. Thus
$$
W_1=0,
\qquad
W_m=W_{m-1}+2^{m-1}-1.
$$
Summing gives
$$
W_m=\sum_{j=1}^{m-1}(2^j-1)
=2^m-m-1.
$$
Since $m=n-1$, the minimum complete reduction length is
$$
L_n=W_{n-1}=2^{n-1}-n.
$$
Final Answer: $\boxed{2^{n-1}-n}$

---

## Answer

$2^{n-1}-n$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- term rewriting systems
- weighted adjacent swaps
- reduced decompositions
- recurrence optimization
