## Steps

Step 1: Compute the sign of a reversal

Let $v\in\{0,1\}^n$. In the fixed adjacent-exchange term $R_n$, every pair of tensor positions crosses exactly once. A crossing contributes $-1$ exactly when both crossed entries are $1$. Hence the total number of negative crossings is the number of unordered pairs of $1$ entries:
$$
R_n|v\rangle
=
(-1)^{\binom{|v|}{2}}|v^{\leftarrow}\rangle.
$$

Step 2: Follow the first scan and reversal

The first constructor applied to $|b\rangle$ is $P_n$, so
$$
P_n|b\rangle=|p\rangle.
$$
Applying the first reversal and then the second scan gives
$$
(P_n\circ R_n\circ P_n)|b\rangle
=
(-1)^{\binom{|p|}{2}}P_n|p^{\leftarrow}\rangle
=
(-1)^{\binom{|p|}{2}}|u\rangle,
$$
because $u$ was defined as the prefix-parity word of $p^{\leftarrow}$.

Step 3: Apply the cut and the second reversal

Each $Z_i$ is diagonal and leaves the bit word unchanged. Its exponent is $1$ precisely at a descent $u_i=1,u_{i+1}=0$. Therefore
$$
K_n|u\rangle=(-1)^{d(u)}|u\rangle.
$$
By Step 1, the following reversal contributes another factor
$$
R_n|u\rangle
=
(-1)^{\binom{|u|}{2}}|u^{\leftarrow}\rangle.
$$
Thus, immediately before $H_n$, the accumulated sign is
$$
(-1)^{\binom{|p|}{2}+d(u)+\binom{|u|}{2}},
$$
and the current word is $u^{\leftarrow}$.

Step 4: Compute the block-exchange sign and combine all factors

For any input word $v$, the term $H_n$ crosses every position in its first block with every position in its second block exactly once. Hence
$$
H_n|v\rangle
=
(-1)^{\left(\sum_{i=1}^{m}v_i\right)
\left(\sum_{i=m+1}^{n}v_i\right)}
|\text{the two blocks of }v\text{ exchanged}\rangle
=
(-1)^{\lambda(v)}
|\text{the two blocks of }v\text{ exchanged}\rangle.
$$
Here $v=u^{\leftarrow}$, so this last factor is $(-1)^{\lambda(u^{\leftarrow})}$. Multiplying the four independent sign contributions gives
$$
\omega_n(b)
=
(-1)^{\binom{|p|}{2}+d(u)+\binom{|u|}{2}+\lambda(u^{\leftarrow})}.
$$
The four terms are left in the specified-statistics form required by the problem, without canceling or simplifying them modulo $2$.

Final Answer: $\boxed{(-1)^{\binom{|p|}{2}+d(u)+\binom{|u|}{2}+\lambda(u^{\leftarrow})}}$

---

## Answer

$(-1)^{\binom{|p|}{2}+d(u)+\binom{|u|}{2}+\lambda(u^{\leftarrow})}$

---

## Classification

Problem Type: Symbolic derivation

Answer Type: Function or mapping

---

## Solution Concepts

- typed term reduction
- graded exchange signs
- prefix-parity scan
- descent counting
- block-crossing parity
- canonical answer normalization

---

## Black-Box Audit

No issues found. The final answer is constrained to the specified statistics, preventing rewrites in the original bits or modulo-$2$ cancellations while leaving the decomposition to the solver.
