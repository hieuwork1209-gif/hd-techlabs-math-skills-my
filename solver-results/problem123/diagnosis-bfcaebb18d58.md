# Solver diagnosis — bfcaebb18d58

- **COMMON ENTRY:** View the two equations as cyclic Kummer covers of the x-line and use the branch valuations at 0, 1, lambda, and infinity.
- **COMMON REDUCTION:** Prove the compositum has degree mn, identify the Galois group as Z/m x Z/n, and reduce genus to the four inertia orders.
- **FIRST DECISIVE RECOGNITION:** At a branch point shared by both covers, local monodromy is the simultaneous valuation vector; hence e_0=lcm(m,n), while the vector (-2,-2) at infinity creates the parity transition.
- **RECOVERY PATH:** Compute e_0, e_1, e_lambda, e_infinity, substitute the Galois ramification contributions into Riemann-Hurwitz, and simplify by d=gcd(m,n).
- **EARLIEST ROBUST SHORTCUT:** Once the Kummer compositum and simultaneous inertia rule are recognized, the problem becomes a direct four-branch-point Riemann-Hurwitz calculation; no later obstruction prevents the solver from closing the genus formula.

Verdict: solver correct on the first clean Algebraic Geometry blob. A same-blueprint revision is permitted only if it adds a natural dependency after the Kummer/inertia gateway rather than more ramification bookkeeping.
