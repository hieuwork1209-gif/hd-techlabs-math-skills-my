# Normalized Math Problem

## LaTeX (Normalized)

For $\tau>0$, consider the delayed-damping oscillator
$$
\ddot x(t)+x(t)+\frac12\dot x(t-\tau)=0.
$$
Its characteristic roots are the zeros of
$$
\lambda^2+1+\frac\lambda2e^{-\lambda\tau}=0.
$$
Determine all $\tau>0$ for which every characteristic root has negative real part.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Solve for unknowns |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

This is a spectral-stability problem for a delayed oscillator with damping applied after a time lag. The delay changes the location of the infinitely many characteristic roots, and the problem asks for the exact set of delays for which the full spectrum remains in the open left half-plane.
