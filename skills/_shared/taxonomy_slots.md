# Shared Taxonomy Slot Snapshot

This file is the source of truth for currently usable taxonomy slots. Update it whenever the portal capacity changes. Skills must read this file before choosing or changing a Domain/Sub-domain, Problem Type, or Answer Type.

Last updated from user-provided portal snapshot: **2026-09-05**. Reviewer taxonomy classification feedback retained from **2026-08-28**; any older capacity/availability statements are superseded by the newer portal snapshot. The current portal snapshot contains **110 Domain/Sub-domain rows across 12 Domains**, and **all 110 currently listed rows have positive remaining capacity**. The table below is derived directly from the latest user-provided snapshot; any Domain/Sub-domain pair absent from that list must be treated as unavailable for the current snapshot rather than carried forward from older snapshots.

## Selection Rules

- Determine the Domain/Sub-domain by what the problem fundamentally asks, rather than by the solution methods or tools used.
- If a problem involves multiple domains, classify it by the highest-level concepts fundamental to the problem.
- Use only Domain/Sub-domain pairs present in the current `available_segments` table below with a positive remaining-slot count.
- Treat a row with `0` remaining slots, or a row absent from the current portal snapshot, as unavailable.
- Never force a taxonomy label merely because it has more or fewer remaining slots. Primary mathematical content decides the label.
- If the mathematically correct Sub-domain is unavailable, do not relabel the same prompt into a nearby open Sub-domain. Materially redesign the prompt so that its fundamental content genuinely fits an open slot.
- Treat explicit reviewer classification feedback as a taxonomy guardrail for future choices until superseded by newer portal or reviewer evidence.
- For the Domain Explanation, state why the selected Domain/Sub-domain is the best fit and why it is more appropriate than the next-best alternative.
- If the user provides a newer portal snapshot in chat, that newer snapshot supersedes this file for the current run.

## Domain/Sub-domain Slots

| Domain | Sub-domain | Remaining slots | Status | Notes |
|---|---|---:|---|---|
| Abstract Algebra | Group theory | 2 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Ring theory | 2 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Galois theory | 3 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Universal algebra and algebraic structures | 3 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Metric spaces | 3 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Computational geometry | 3 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Bayesian statistics | 3 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Field theory | 4 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Module theory | 4 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Representation theory | 4 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Asymptotic analysis | 4 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Fourier analysis | 4 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Commutative algebra | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Homological Algebra | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Calculus of variations | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Functional analysis | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Measure theory | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Real analysis | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Applications of integration | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Eigenvalues and eigenvectors | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Matrix decompositions and canonical forms | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Numerical analysis | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Numerical optimization | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Limit theorems | 5 | open | 2026-09-05 user-provided portal snapshot. |
| Abstract Algebra | Computational algebra | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Equations and inequalities | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Complex analysis | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Analysis | Harmonic analysis | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Bifurcation theory | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Determinants | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Vectors and vector spaces | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Complexity theory | 6 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | First-order ordinary differential equations | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Inner product spaces | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Linear transformations | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Matrices and matrix operations | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Systems of linear equations | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Tensor and multilinear algebra | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Mathematical logic | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Experimental design and causal inference | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Probability foundations | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Regression and statistical modeling | 7 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Integration | 8 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Higher-order ordinary differential equations | 8 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Systems of differential equations | 8 | open | 2026-09-05 user-provided portal snapshot. |
| Linear Algebra | Numerical linear algebra | 8 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Algebraic topology | 8 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Applications of derivatives | 9 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Partial differential equations | 9 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Algebraic number theory | 9 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Elementary number theory | 9 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Statistical computing and simulation | 9 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Algebraic geometry | 9 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Sequences and elementary recurrence relations | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Systems of equations | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Infinite sequences and series | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Numerical differential equations | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Analytic number theory | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Computational number theory | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Diophantine equations | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Modular arithmetic and congruences | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Quadratic residues and reciprocity | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Scientific computing | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Joint distributions and dependence | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Convex geometry | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Differential geometry | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Point-set topology | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Riemannian geometry | 10 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Functions and graphs | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Trigonometry | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Single-variable calculus | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Initial value problems | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Proof theory | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Type theory and formal systems | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Number Theory | Multiplicative functions | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Differential topology | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Geometric topology | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Topology and Geometry | Symplectic and contact geometry | 11 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Algebraic expressions and manipulation | 12 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Exponential and logarithmic functions | 12 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Vector calculus | 12 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Stability theory | 12 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Elementary mathematical modeling | 13 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Differentiation | 13 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Limits and continuity | 13 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Boundary value problems | 13 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Stochastic processes | 13 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Expectation and variance | 14 | open | 2026-09-05 user-provided portal snapshot. |
| Calculus | Multivariable calculus | 15 | open | 2026-09-05 user-provided portal snapshot. |
| Differential Equations and Dynamical Systems | Dynamical systems | 15 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Model theory | 15 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Euclidean geometry | 16 | open | 2026-09-05 user-provided portal snapshot. |
| Algebra, Functions, and Trigonometry | Polynomial and rational functions | 19 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Analytic geometry | 20 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Computability theory | 20 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Set theory | 20 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Coordinate and analytic geometry | 21 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Solid geometry | 21 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Discrete and integer optimization | 21 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Random variables and distributions | 21 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Approximation theory | 22 | open | 2026-09-05 user-provided portal snapshot. |
| Logic, Set Theory, and Foundations | Category theory | 23 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Convex optimization | 23 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Error analysis and stability | 23 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Linear programming | 23 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Nonlinear optimization | 23 | open | 2026-09-05 user-provided portal snapshot. |
| Optimization and Numerical Mathematics | Dynamic programming and optimal control | 24 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Transformational geometry | 26 | open | 2026-09-05 user-provided portal snapshot. |
| Probability and Statistics | Statistical inference | 27 | open | 2026-09-05 user-provided portal snapshot. |
| Euclidean, Coordinate, and Transformational Geometry | Trigonometric geometry | 30 | open | 2026-09-05 user-provided portal snapshot. |

## Reviewer-Confirmed Taxonomy Guardrails

- The 2026-09-05 portal snapshot supersedes older capacity statements: **Linear Algebra → Linear transformations** is currently open with **7** remaining slots, and **Linear Algebra → Vectors and vector spaces** is currently open with **6** remaining slots.
- Reviewer feedback dated 2026-08-26 still governs classification: prompts whose core task is classification or counting of subspaces invariant under specified linear operators, or whose defining structure is eigenspace/spectral decomposition and operator action, belong to **Linear transformations**, not **Vectors and vector spaces**.
- Do not relabel such prompts to **Vectors and vector spaces** merely because of slot counts. Primary mathematical content decides the label.
- Reviewer feedback dated 2026-08-28 confirms that problems whose central objects are commutative rings/modules and whose target is a Poincare series encoding Betti numbers through `Tor`, minimal resolutions, fiber products, socle quotients, annihilators, and Yoneda/Ext structure belong to **Abstract Algebra → Commutative algebra**, not **Discrete Mathematics and Combinatorics → Generating functions**.
- A rational function in the series variable does not by itself make such a problem a Generating functions problem; the series is only packaging homological dimensions after the algebraic structure is understood.
- The 2026-09-05 portal snapshot now lists **Abstract Algebra → Commutative algebra** as open with **5** remaining slots. The reviewer classification rule above remains in force; capacity no longer blocks that taxonomy choice.

## Problem Type Slots

Select **exactly one**. These names and definitions mirror the current portal form.

| Problem Type | Definition | Remaining slots | Status | Notes |
|---|---|---:|---|---|
| Exact computation | A problem asking for an exact numerical value or exact mathematical object derived from the given information | unknown | open | Use when the requested output is exact. |
| Symbolic derivation | A problem asking for a closed-form expression, identity, recurrence, transform, or asymptotic form obtained through symbolic reasoning | unknown | open | Use when the requested output is a symbolic derivation. |
| Numerical approximation | A problem asking for a numerical answer computed to a specified tolerance, precision, or error bound | unknown | open | Use only when the problem specifies the required tolerance, precision, or error bound. |
| Solve for unknowns | A problem asking for one or more values or objects that satisfy a given equation, system, or mathematical condition | unknown | open | Bonus Pay Category. |
| Construction under constraints | A problem asking for the unique mathematical object that satisfies a stated set of structural or quantitative constraints | unknown | open | Bonus Pay Category. |
| Optimization | A problem asking for an optimal value, an optimizer, or both under a given objective and constraint set | unknown | open | Bonus Pay Category. |
| Exhaustive enumeration | A problem asking for the complete set of all valid solutions, cases, or objects satisfying the given criteria | unknown | open | Bonus Pay Category. |
| Canonicalization or normalization | A problem asking for an object to be rewritten in a specified standard, reduced, or canonical form | unknown | open | Bonus Pay Category. |
| Transformation between representations | A problem asking for conversion of an object from one mathematically equivalent representation to another | unknown | open | Bonus Pay Category. |
| Parameter identification | A problem asking for unknown parameters, coefficients, or latent quantities to be inferred from equations, conditions, or observed structure | unknown | open | Bonus Pay Category. |
| Other | A task that does not honestly fit any listed problem type | unknown | open | Use only when no listed type honestly fits. |

## Answer Type Slots

Select **exactly one**. These names and definitions mirror the current portal form.

| Answer Type | Definition | Remaining slots | Status | Notes |
|---|---|---:|---|---|
| Exact scalar | A single exact numerical quantity, such as an integer, rational number, algebraic number, or closed-form constant | unknown | open |  |
| Numerical scalar approximation | A single numerical quantity expected up to a specified tolerance or precision | unknown | open | Any tolerances must be specified in the problem. |
| Exact symbolic expression | A closed-form symbolic expression representing the correct final answer up to mathematical equivalence | unknown | open |  |
| Polynomial or rational function | A polynomial, rational function, or closely related algebraic expression returned in symbolic form | unknown | open | Bonus Pay Category. |
| Equation or inequality | An equation, inequality, system, recurrence, congruence, or constraint written explicitly as the answer | unknown | open | Bonus Pay Category. |
| Interval or region description | An interval, union of intervals, domain, range, feasible region, solution region, or set described by inequalities or symbolic conditions | unknown | open | Bonus Pay Category. |
| Vector | A finite-dimensional vector returned as coordinates, components, or an equivalent explicit representation | unknown | open | Bonus Pay Category. |
| Matrix | A matrix returned explicitly, typically with entries in exact or numerical form as specified | unknown | open | Bonus Pay Category. |
| Tuple or ordered list | A finite ordered collection of values, objects, labels, or coordinates where order matters | unknown | open | Bonus Pay Category. |
| Set or multiset of objects | A complete finite collection of valid outputs, where order is irrelevant and multiplicity may or may not matter | unknown | open | Bonus Pay Category. |
| Sequence or series representation | A sequence, recurrence, finite truncation rule, or series-form representation of the target object | unknown | open | Bonus Pay Category. |
| Function or mapping | A function, transformation, homomorphism, permutation, operator, rule, or mapping specified explicitly by formula, table, images of elements, or action on a basis | unknown | open | Bonus Pay Category. |
| Canonical form | A mathematical object expressed in a specified standard or normalized form, such as diagonal form, Jordan form, or reduced row echelon form | unknown | open | Bonus Pay Category. |
| Other | A final answer object that does not honestly fit the listed types | unknown | open | Use only when no listed type honestly fits. |

## Solution Concepts

List **1 to 5** concepts, techniques, or pieces of knowledge required to solve the problem.

- Each concept must be concise: under 100 characters.
- Each concept must be on a single line.
- If more than five apply, list the five most important.
