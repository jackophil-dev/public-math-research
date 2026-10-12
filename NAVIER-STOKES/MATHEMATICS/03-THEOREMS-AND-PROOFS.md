# Navier–Stokes — Theorems and Proofs

## Proposition — Enstrophy balance for smooth solutions
For a sufficiently smooth divergence-free solution on a periodic domain (or whole space with adequate decay),
\[
\frac12\frac{d}{dt}\|\omega\|_2^2+\nu\|\nabla\omega\|_2^2=\int\omega^TS\omega\,dx.
\]

**Proof sketch.** Take curl of momentum, multiply the vorticity equation by \(\omega\), and integrate. Under the stated boundary assumptions, transport integrates to zero and diffusion contributes \(-\nu\|\nabla\omega\|_2^2\). The contraction \(\omega_i\omega_j\partial_j u_i\) depends only on the symmetric part of \(\nabla u\), namely \(S\). Rearrangement gives the identity. \(\square\)

This a priori identity does not prove global smoothness in three dimensions. A separate estimate closing the nonlinear stretching term is required.