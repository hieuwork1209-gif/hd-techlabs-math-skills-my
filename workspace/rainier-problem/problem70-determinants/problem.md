# Normalized Math Problem

## LaTeX (Normalized)

For a permutation $\pi\in S_5$, let
$$
\operatorname{inv}(\pi)=\#\{(i,j):1\le i<j\le5,\ \pi(i)>\pi(j)\}
$$
be its inversion number. Index the rows and columns of a $120\times120$ matrix $A$ by the elements of $S_5$, and define
$$
A_{\sigma,\tau}=\delta_{\sigma,\tau}+2^{\operatorname{inv}(\sigma^{-1}\tau)}
\qquad(\sigma,\tau\in S_5),
$$
where $\delta_{\sigma,\tau}$ is the Kronecker delta. Determine $\det A$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Determinants |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The matrix is the identity-regularized exponential kernel for Kendall-tau distance on permutations. The unregularized kernel has a closed Varchenko determinant, but the identity shift forces one to determine the noncentral irreducible block spectra rather than only their determinants. The target remains the exact determinant of a concrete finite matrix, so Linear Algebra -> Determinants is the primary classification.
