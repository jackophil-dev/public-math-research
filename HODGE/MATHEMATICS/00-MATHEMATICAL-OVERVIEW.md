# Hodge — Mathematical Overview

**Scope:** Explicit lattice arithmetic and Weil-type abelian fourfolds. This folder does **not** claim a proof of the general Hodge Conjecture.

## Mathematical route
1. Fix the variety, coefficient field, cohomological degree, basis, and pairing.
2. Define candidate Weil/Hodge classes and their coordinates.
3. Compute Gram matrices, determinants, Smith normal forms (SNF), and discriminant groups.
4. Separately establish saturation and geometric identification with algebraic-cycle classes.

For the recorded matrix
\[
G=\begin{pmatrix}36&12\\12&0\end{pmatrix},
\quad \det G=-144,
\quad \operatorname{SNF}(G)=\operatorname{diag}(12,12),
\]
the corresponding non-degenerate lattice has discriminant group \((\mathbb Z/12\mathbb Z)^2\), provided the recorded SNF is correct. Matrix arithmetic alone does not identify the full geometric cycle lattice.

## Navigation
- [01 Definitions and hypotheses](01-DEFINITIONS-AND-HYPOTHESES.md)
- [02 Core equations and derivations](02-CORE-EQUATIONS-AND-DERIVATIONS.md)
- [03 Theorems and proofs](03-THEOREMS-AND-PROOFS.md)
- [04 Computational verification](04-COMPUTATIONAL-VERIFICATION.md)
- [05 Open problems](05-OPEN-PROBLEMS.md)
- [Core theorem record](../CORE-THEOREMS-01-04.md) and H01–H12 certificates.

**Evidence boundary:** geometric identification, polarization compatibility, and saturation remain open wherever the project certificates say so.