# problem123 regeneration audit v2

Selected taxonomy: Probability and Statistics -> Joint distributions and dependence. The 2026-09-11 taxonomy snapshot lists this row as open with 6 remaining slots. The requested object is mutual information between two random blocks; Bayesian conjugacy is auxiliary.

Natural object: two conditionally independent exchangeable Bernoulli samples sharing a symmetric latent parameter through the success probability 4 theta(1-theta).

Hidden dependency chain:
1. Discover that theta is not identifiable and pass to the quotient latent P=4 theta(1-theta).
2. Reconstruct the induced law P ~ Beta(a,1/2), including the two-to-one Jacobian.
3. Use conditional independence to reduce block mutual information to 2 J_n - J_{2n}, where J_m is parameter-sample information.
4. Derive the exact Beta-Bernoulli posterior-entropy asymptotic, including boundary control for the singular Beta(a,1/2) density at p=1.
5. Evaluate the Beta entropy/log-moments and simplify the n versus 2n cancellation.

Closure: the posterior-entropy estimate proves existence of the stated limit for every fixed a>0; no unproved uniqueness or branch choice remains.

Structural false trails:
- Working directly in theta produces a non-conjugate posterior and hides the two-to-one identifiability quotient.
- Treating theta as a regular one-dimensional parameter leads to a degenerate Fisher-information picture at theta=1/2; the correct regular parameter is P.

## Triviality probes

P1 PASS: no finite state enumeration. The problem is an n->infinity asymptotic with a free real parameter a>0.

P2 PASS: every structural component is load-bearing. Beta(a,a) prior: Yes. The map 4 theta(1-theta): Yes. Two conditionally independent Bernoulli blocks: Yes. The subtraction (1/2) log n: Yes. Free parameter a: Yes.

P3 PASS: the answer is a non-degenerate symbolic function of a, not 0, an identity object, an empty set, or a gotcha.

P4 PASS with mild named-asymptotic warning: the decisive skeleton is hidden identifiable quotient -> induced Beta law -> shared-latent information identity -> posterior-entropy asymptotic. No single named theorem supplies the whole route, and the singular endpoint must be checked rather than assumed regular. Workspace mechanism-registry reuse = 0 for this skeleton; repository search found no Beta-Bernoulli mutual-information analogue.

P5 PASS: the requested answer is a symbolic function for arbitrary a, so one fixed numerical simulation/PSLQ computation cannot recover it. Direct finite-n computation only approximates individual parameter values and does not identify the digamma dependence.

P6 PASS: the statement does not introduce P, state its induced Beta law, give the mutual-information decomposition, or construct the posterior route.

P7 PASS: serial graph with 5 load-bearing nodes; the longest unlock chain is 5 nodes and at most 2 mathematical states must be tracked simultaneously. Difficulty is depth, not parallel bookkeeping.

P8 PASS: bespoke term count N=1 (L(a)); maximum simultaneous bespoke definitions = 1. Beta, Bernoulli, mutual information, B, Gamma, and digamma are standard terms/functions, not renamed concepts.

Answer-length check: stripped final expression `\log B(a,\frac12)+(a-\frac12)(\psi(a+\frac12)-\psi(a))-\frac12\log(4\pi e)` has 72 characters, below the 100-character gate.
