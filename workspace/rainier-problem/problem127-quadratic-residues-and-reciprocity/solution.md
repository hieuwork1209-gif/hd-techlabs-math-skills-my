## Steps

Step 1: Expand the three residue conditions into one cubic character sum
Let $\chi$ be the quadratic character modulo $p$, extended by $\chi(0)=0$, and put
$$
T=\sum_{x\in\mathbb F_p}\chi(x^3-x).
$$
For $x\notin\{-1,0,1\}$, the indicator that $x-1,x,x+1$ are all nonzero quadratic residues is
$$
\frac{1}{8}(1+\chi(x-1))(1+\chi(x))(1+\chi(x+1)).
$$
The three single-character sums vanish. For distinct $a,b\in\mathbb F_p$,
$$
\sum_x\chi((x-a)(x-b))=-1.
$$
Indeed, after an affine change of variable this is $\sum_y\chi(y^2-d)$ with $d\ne0$. If $N_d$ is the number of pairs $(y,z)$ satisfying $z^2=y^2-d$, then
$$
N_d=p+\sum_y\chi(y^2-d).
$$
But $(y-z)(y+z)=d$ has exactly $p-1$ solutions, so the sum is $-1$.

Therefore the sum of the expanded product over all $x\in\mathbb F_p$ is
$$
p-3+T.
$$
Because $p\equiv1\pmod4$, one has $\chi(-1)=1$ and $\chi(-2)=\chi(2)=\varepsilon$. The values of the expanded product at $x=0,1,-1$ are respectively
$$
4,\qquad 2(1+\varepsilon),\qquad 2(1+\varepsilon).
$$
Hence, if $N_p$ denotes the required count,
$$
8N_p=p-11-4\varepsilon+T.
$$

Step 2: Convert the cubic character sum to a quartic Jacobi sum
Choose a multiplicative character $\psi$ of order $4$ on $\mathbb F_p^\times$, extended by $\psi(0)=0$. Then $\psi^2=\chi$. Define
$$
J(\psi,\chi)=\sum_{t\in\mathbb F_p}\psi(t)\chi(1-t).
$$
For $x\ne-1$, set
$$
t=\frac{x-1}{x+1}.
$$
Since the omitted term $x=-1$ contributes $0$, and the missing value $t=1$ also contributes $0$, this change of variable gives
$$
T=\sum_{t\in\mathbb F_p}\chi\bigl(t(1-t^2)\bigr).
$$
Now set
$$
S=\sum_{u\in\mathbb F_p}\chi(1-u^4).
$$
Each $t\in\mathbb F_p$ has $1+\chi(t)$ square roots, so
$$
S=\sum_t(1+\chi(t))\chi(1-t^2).
$$
The first part is
$$
\sum_t\chi(1-t^2)=-1,
$$
by the quadratic-sum identity from Step 1. Thus
$$
S=-1+T.
$$

On the other hand, for $t\ne0$ the number of fourth roots of $t$ is
$$
1+\psi(t)+\chi(t)+\overline{\psi(t)}.
$$
Therefore
$$
S
=1+\sum_{t\ne0}(1+\psi(t)+\chi(t)+\overline{\psi(t)})\chi(1-t).
$$
Here
$$
\sum_{t\ne0}\chi(1-t)=-1,
\qquad
J(\chi,\chi)=\sum_t\chi(t)\chi(1-t)=-1,
$$
and $J(\overline\psi,\chi)=\overline{J(\psi,\chi)}$. Hence
$$
S=-1+2\operatorname{Re}J(\psi,\chi).
$$
Comparing the two formulas for $S$ yields
$$
T=2\operatorname{Re}J(\psi,\chi).
$$

Step 3: Evaluate the quartic Jacobi sum with the prescribed sign convention
The classical quartic Jacobi-sum evaluation states the following exact form. If $p\equiv1\pmod4$, $\chi$ is the quadratic character, and $\psi$ is either quartic character, then
$$
J(\psi,\chi)=A\pm Bi,
$$
where
$$
A^2+B^2=p,
\qquad
B\text{ is even},
\qquad
A\equiv-\chi(2)\pmod4.
$$
Changing $\psi$ to $\overline\psi$ changes only the sign of $B$, so the real part is uniquely determined.

In the notation of the problem, $\chi(2)=\varepsilon$ and the uniquely signed odd coordinate in the representation of $p$ as a sum of two squares is precisely $a$. Therefore
$$
\operatorname{Re}J(\psi,\chi)=a,
$$
and Step 2 gives
$$
T=2a.
$$

Step 4: Substitute the cubic sum into the counting identity
Step 1 gives
$$
8N_p=p-11-4\varepsilon+T.
$$
Using $T=2a$ from Step 3,
$$
N_p=\frac{p-11-4\varepsilon+2a}{8}.
$$
This counts exactly the residues $x$ for which all three of $x-1,x,x+1$ are nonzero quadratic residues.

Final Answer: $\boxed{\frac{p-11-4\varepsilon+2a}{8}}$

---

## Answer

$\frac{p-11-4\varepsilon+2a}{8}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quadratic characters
- quadratic character sums
- quartic characters
- Jacobi sums
- sums of two squares
