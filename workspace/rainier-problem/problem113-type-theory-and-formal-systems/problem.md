# Normalized Math Problem

## LaTeX (Normalized)

Work in Curry-style simply typed combinatory logic with one primitive combinator $S$ and binary application. Simple types are built from type variables using $\to$, which associates to the right. Every occurrence of $S$ may be assigned a fresh instance of
$$
(\alpha\to\beta\to\gamma)\to(\alpha\to\beta)\to\alpha\to\gamma.
$$
An application $UV$ is typable exactly when the types assigned to $U$ and $V$ can be unified so that $U$ has type $\sigma\to\tau$ and $V$ has type $\sigma$ for some simple types $\sigma,\tau$. Unification is the usual finite simple-type unification with the occurs check.

For $n\geq1$, let $\mathcal P_n$ be the set of all full parenthesizations of a word consisting of $n$ copies of $S$. Let $\mathcal T_n\subseteq\mathcal P_n$ be the subset of typable terms. Define
$$
R_1=S,
\qquad
R_{n+1}=S R_n.
$$

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

This problem asks for a complete classification of typable terms in Curry-style simply typed combinatory logic, so its primary content is type assignment, principal typing, and unification in Logic, Set Theory, and Foundations / Type theory and formal systems. The binary-tree structure of parenthesizations is only the syntax on which the typing constraints act, so combinatorics is secondary.
