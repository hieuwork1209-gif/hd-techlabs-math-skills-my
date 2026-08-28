# Normalized Math Problem

## LaTeX (Normalized)

Work in the following typed term calculus over the field $\mathbb{Q}$. There is one type $B$, and the canonical closed values of the tensor context $B^{\otimes n}$ are denoted
$$
|b_1\cdots b_n\rangle,
\qquad b_i\in\{0,1\}.
$$
All sums in bit positions are taken modulo $2$. For $1\leq i<n$, the typed constructor $C_i:B^{\otimes n}\to B^{\otimes n}$ has the reduction rule
$$
C_i|b_1\cdots b_i b_{i+1}\cdots b_n\rangle
=|b_1\cdots b_i(b_i+b_{i+1})\cdots b_n\rangle.
$$
Define the left scan
$$
P_n=C_{n-1}\circ C_{n-2}\circ\cdots\circ C_1,
$$
where the rightmost constructor is reduced first. Thus, for a bit word $b=(b_1,\ldots,b_n)$, put
$$
p=(p_1,\ldots,p_n),
\qquad p_i=b_1+\cdots+b_i\pmod 2,
$$
so that $P_n|b\rangle=|p\rangle$. Write $|v|$ for the number of $1$ entries of a bit word $v$.

For $1\leq i<n$, graded exchange is the typed constructor
$$
S_i|b_1\cdots b_i b_{i+1}\cdots b_n\rangle
=(-1)^{b_i b_{i+1}}|b_1\cdots b_{i+1}b_i\cdots b_n\rangle.
$$
Let $R_n:B^{\otimes n}\to B^{\otimes n}$ be the fixed adjacent-exchange term that reverses the $n$ tensor positions, moving the rightmost position successively to the left and preserving that order at every stage. Every pair of tensor positions crosses exactly once.

For a bit word $v=(v_1,\ldots,v_n)$, write $v^{\leftarrow}=(v_n,\ldots,v_1)$. In addition to the prefix word $p$ above, define
$$
u=(u_1,\ldots,u_n),
\qquad
u_i=p_n+p_{n-1}+\cdots+p_{n+1-i}\pmod2.
$$
Thus $u$ is the prefix-parity word of $p^{\leftarrow}$.

For $1\leq i<n$, define a typed cut constructor by
$$
Z_i|v_1\cdots v_i v_{i+1}\cdots v_n\rangle
=(-1)^{v_i(1-v_{i+1})}|v_1\cdots v_i v_{i+1}\cdots v_n\rangle,
$$
and put $K_n=Z_{n-1}\circ\cdots\circ Z_1$. For any bit word $v$, let
$$
d(v)=\#\{i:1\leq i<n,\ v_i=1,\ v_{i+1}=0\}.
$$

Put $m=\lfloor n/2\rfloor$. Let $H_n$ be the fixed adjacent-exchange term that moves the first $m$ tensor positions past the last $n-m$ positions while preserving the internal order of both blocks. Every position from the first block crosses every position from the second block exactly once. For a bit word $v$, define the block-crossing statistic
$$
\lambda(v)=\left(\sum_{i=1}^{m}v_i\right)
\left(\sum_{i=m+1}^{n}v_i\right).
$$

Set
$$
\Theta_n=H_n\circ R_n\circ K_n\circ P_n\circ R_n\circ P_n.
$$
Because every reduction rule sends a canonical value to a signed canonical value, there are unique functions
$$
\psi_n:\{0,1\}^n\to\{0,1\}^n,
\qquad
\omega_n:\{0,1\}^n\to\{1,-1\}
$$
such that the fully reduced normal form is
$$
\Theta_n|b\rangle=\omega_n(b)|\psi_n(b)\rangle.
$$
Determine the function $\omega_n$ explicitly for every $n\geq2$ and every $b\in\{0,1\}^n$.

For verifiability, give the final result in the normalized form
$$
\omega_n(b)=(-1)^{E_1+E_2+E_3+E_4},
$$
where $(E_1,E_2,E_3,E_4)$ is the ordered list of the integer exponents contributed, respectively, by the first occurrence of $R_n$, by $K_n$, by the second occurrence of $R_n$, and by $H_n$ in the reduction of $\Theta_n|b\rangle$. Each $E_j$ must be written only in terms of the already specified statistics $|p|$, $d(u)$, $|u|$, and $\lambda(u^{\leftarrow})$; use binomial-coefficient notation for pair-count contributions. Do not reduce, cancel, combine, or otherwise simplify the four exponents modulo $2$, and do not rewrite them in terms of the original bits $b_i$. Report the ordered tuple $(E_1,E_2,E_3,E_4)$ together with $\omega_n(b)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Logic, Set Theory, and Foundations |
| **Sub-domain** | Type theory and formal systems |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Function or mapping |

---

## Domain Explanation

This problem asks for the scalar produced by fully normalizing a fixed typed term under explicitly stated reduction rules, so its central content is the operational behavior of a typed formal system. The tensor notation and graded exchanges encode the syntax and reduction semantics of that calculus. Type theory and formal systems is therefore a better fit than Linear Algebra, since the task is not to classify or analyze an arbitrary linear transformation but to derive the normal-form sign of a specified term.
