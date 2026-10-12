# Navier–Stokes — Mathematical Overview

**Status:** research in progress. No proof of global regularity or finite-time blow-up is claimed.

For incompressible velocity \(u\), pressure \(p\), and viscosity \(\nu>0\):
\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\qquad \nabla\cdot u=0.
\]
Set \(\omega=\nabla\times u\) and \(S=(\nabla u+\nabla u^T)/2\).

For sufficiently smooth solutions on a periodic domain or with adequate decay,
\[
\frac12\frac{d}{dt}\|\omega\|_2^2+\nu\|\nabla\omega\|_2^2
=\int\omega^TS\omega\,dx.
\]
The stretching term is the central nonlinear contribution. A global estimate that closes this balance is a separate and unresolved task.

- [01 Definitions and hypotheses](01-DEFINITIONS-AND-HYPOTHESES.md)
- [02 Core equations and derivations](02-CORE-EQUATIONS-AND-DERIVATIONS.md)
- [03 Theorems and proofs](03-THEOREMS-AND-PROOFS.md)
- [04 Computational verification](04-COMPUTATIONAL-VERIFICATION.md)
- [05 Open problems](05-OPEN-PROBLEMS.md)
- [Existing core identities](../CORE-MATHEMATICAL-IDENTITIES.md), [theorems](../THEOREMS/), [certificates](../CERTIFICATES/)

Project-specific SPN identities are not extended here beyond what existing public sources establish.