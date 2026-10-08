# Navier–Stokes Research

This directory contains the public Navier–Stokes research track.

## Public status

**Status: OPEN / WORK IN PROGRESS**

The released material records exact differential identities, derived local decompositions, and explicit unresolved regularity obligations. No completed global regularity proof or finite-time singularity construction is claimed.

## Mathematical core

- [Core Mathematical Identities](./CORE-MATHEMATICAL-IDENTITIES.md)
- [Regularity Boundary](./THEOREMS/REGULARITY-BOUNDARY.md)

### Released certificates

- [CERT-NS-001 — Vorticity Transport](./CERTIFICATES/CERT-NS-001-VORTICITY-TRANSPORT.md) — **PROVED**
- [CERT-NS-002 — Global Enstrophy](./CERTIFICATES/CERT-NS-002-ENSTROPHY.md) — **PROVED**
- [CERT-NS-003 — Magnitude/Direction Factorization](./CERTIFICATES/CERT-NS-003-MAGNITUDE-DIRECTION.md) — **PROVED** on \(\rho>0\)
- [CERT-NS-004 — Local Magnitude/Direction Balance](./CERTIFICATES/CERT-NS-004-LOCAL-BALANCE.md) — **DERIVED**

## Research boundary

The central nonlinear term is

\[
\int_\Omega \omega^T S\omega\,dx,
\qquad
S=\frac{\nabla u+\nabla u^T}{2}.
\]

Controlling this term sufficiently to close the global regularity problem remains **OPEN**.

A growth estimate is not automatically a finite-time blow-up proof, and a regularity criterion is not automatically a construction of a singular solution.

## Status discipline

- **PROVED** — exact identity/theorem established under stated assumptions.
- **DERIVED** — direct consequence of established identities.
- **COMPUTATIONALLY VERIFIED** — independently reproduced within stated scope.
- **OPEN** — unresolved obligation.

The previously empty certificate placeholders were removed. Their missing original source texts are not reconstructed or fabricated.
