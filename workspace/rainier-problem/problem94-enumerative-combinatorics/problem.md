# Normalized Math Problem

## LaTeX (Normalized)

Fix an integer $r\geq3$ and put $n=2^r$. Label the vertices of a regular $n$-gon by $\mathbb Z/n\mathbb Z$.

Color every vertex either black or white. A coloring is admissible if the number of sides whose endpoints are both black plus the number of diameters joining opposite black vertices is odd.

The dihedral group $D_{2n}$ of order $2n$ acts on admissible colorings by the symmetries of the polygon. Determine the number of $D_{2n}$-orbits whose size is exactly $2n$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Discrete Mathematics and Combinatorics |
| **Sub-domain** | Enumerative Combinatorics |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This is an enumerative combinatorics problem centered on counting colorings up to a dihedral group action. The main task is to determine how many admissible colorings have trivial stabilizer, using fixed-point counts for rotations and reflections together with orbit-stabilizer reasoning. The parity condition is handled algebraically over two states, but that algebra serves the enumeration; the essential structure is exact counting of symmetry classes under a finite group action.
