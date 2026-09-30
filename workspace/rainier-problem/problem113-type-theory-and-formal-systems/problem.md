# Normalized Math Problem

## LaTeX (Normalized)

Work in Curry-style simply typed combinatory logic with primitive combinators $S,I$ and binary application. Simple types are built from type variables using $\to$, which associates to the right. Every occurrence may receive a fresh instance of
$$
S:(\alpha\to\beta\to\gamma)\to(\alpha\to\beta)\to\alpha\to\gamma,
\qquad
I:\delta\to\delta.
$$
An application $UV$ is typable exactly when the types assigned to $U$ and $V$ can be unified so that $U$ has type $\sigma\to\tau$ and $V$ has type $\sigma$. Unification is finite simple-type unification with the occurs check.

For $n\geq1$, let $\mathcal P_n$ be the set of all full parenthesizations of the word consisting of $n$ copies of $S$ followed by one copy of $I$, and let $\mathcal T_n\subseteq\mathcal P_n$ be the typable terms.

Define
$$
L_1(X)=SX,
\qquad
L_2(X)=(SS)X.
$$
For a word $d_1\cdots d_r$ over $\{1,2\}$, define
$$
L_{d_1\cdots d_r}(I)
=
L_{d_1}\bigl(L_{d_2}(\cdots L_{d_r}(I)\cdots)\bigr).
$$
The notation $1^a2^b1^c$ means the concatenation of $a$ symbols $1$, then $b$ symbols $2$, then $c$ symbols $1$.

Determine $\mathcal T_n$ exactly for every $n\geq1$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Logic, Set Theory, and Foundations |
| **Sub-domain** | Type theory and formal systems |
| **Problem Type** | Exhaustive enumeration |
| **Answer Type** | Set or multiset of objects |

---

## Domain Explanation

This problem asks for the complete typability classification of a structured family of terms in Curry-style simply typed combinatory logic. Its main content is principal typing, simple-type unification, occurs-check obstructions, and the interaction of the standard $S$ and $I$ combinators, so Logic, Set Theory, and Foundations / Type theory and formal systems is the primary classification. The parenthesization count is only the syntax on which those typing constraints act.
