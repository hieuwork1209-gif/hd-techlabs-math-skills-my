# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge5$ be odd. Let $T_n$ be the triangular graph whose vertices are the $2$-element subsets of $\{1,\ldots,n\}$, with two vertices adjacent exactly when the corresponding $2$-subsets intersect in one element.

Let $L$ be the Laplacian matrix of $T_n$, and let $L'$ be any reduced Laplacian obtained by deleting one row and the corresponding column. The critical group of $T_n$ is
$$
K(T_n)=\mathbb Z^{\binom n2-1}/\operatorname{im}(L').
$$
Determine the invariant-factor decomposition of the finite abelian group $K(T_n)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Combinatorics |
| **Sub-domain** | Graph theory |
| **Problem Type** | Canonicalization or normalization |
| **Answer Type** | Canonical form |

---

## Domain Explanation

The problem asks for the critical (sandpile) group of the triangular graph, equivalently the Smith normal form of a reduced graph Laplacian. The proof uses the incidence matrix of $K_n$, the matrix-tree theorem, and local information on Smith invariants. The primary objects are graphs and their Laplacian invariants, so Combinatorics -> Graph theory is the appropriate classification.