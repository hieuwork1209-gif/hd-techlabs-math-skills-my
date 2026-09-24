# Normalized Math Problem

## LaTeX (Normalized)

Let $a>0$ and $b,c\geq0$. For delays $\tau,\sigma\geq0$, define
$$
\Delta_{\tau,\sigma}(\lambda)
=
\lambda^2+a\lambda+1
+b e^{-\lambda\tau}
+c\lambda e^{-\lambda\sigma},
$$
and let
$$
\mathcal R(a,b,c)
=
\bigcup_{\tau,\sigma\geq0}
\{\lambda\in\mathbb{C}:\Delta_{\tau,\sigma}(\lambda)=0\}.
$$
Determine all triples $(a,b,c)$ for which
$$
\mathcal R(a,b,c)
\cap
\{\lambda\in\mathbb{C}:\operatorname{Re}\lambda\geq0\}
=
\varnothing.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Dynamical systems |
| **Problem Type** | Exhaustive enumeration |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

The problem asks for the parameter region in which the full characteristic root locus of a two-delay dynamical family stays in the open left half-plane. The two independent delays create a phase-compatibility constraint in addition to the frequency-domain magnitude condition.
