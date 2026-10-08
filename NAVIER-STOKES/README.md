# Navier–Stokes Research

This directory contains the public Navier–Stokes research track.

## Public status

**Status: OPEN / WORK IN PROGRESS**

The released material records exact differential identities, derived local decompositions, and explicit unresolved regularity obligations. No completed global regularity proof or finite-time singularity construction is claimed.

## Part I release index

- [Part I Release Index](./PART-I-RELEASE.md) — local vorticity structure, geometric dissipation, SPN identity, and certificate audit.

## Mathematical core

- [Core Mathematical Identities](./CORE-MATHEMATICAL-IDENTITIES.md)
- [Geometric Dissipation Lemma](./THEOREMS/GEOMETRIC-DISSIPATION-LEMMA.md)
- [Exact SPN Structural Identity](./THEOREMS/SPN-STRUCTURAL-IDENTITY.md)
- [Regularity Boundary](./THEOREMS/REGULARITY-BOUNDARY.md)

### Released certificates

- [CERT-NS-001 — Vorticity Transport](./CERTIFICATES/CERT-NS-001-VORTICITY-TRANSPORT.md) — **PROVED**
- [CERT-NS-002 — Global Enstrophy](./CERTIFICATES/CERT-NS-002-ENSTROPHY.md) — **PROVED** under stated boundary/decay assumptions
- [CERT-NS-003 — Magnitude/Direction Factorization](./CERTIFICATES/CERT-NS-003-MAGNITUDE-DIRECTION.md) — **PROVED** on \(\rho>0\)
- [CERT-NS-004 — Local Magnitude/Direction Balance](./CERTIFICATES/CERT-NS-004-LOCAL-BALANCE.md) — **DERIVED**
- [CERT-NS-005 — Geometric Dissipation](./CERTIFICATES/CERT-NS-005-GEOMETRIC-DISSIPATION.md) — **VERIFIED — ANALYTICAL**
- [CERT-NS-006 — Exact SPN Structural Identity](./CERTIFICATES/CERT-NS-006-SPN-STRUCTURAL-IDENTITY.md) — **VERIFIED — ANALYTICAL**
- [Part I Verification Audit](./CERTIFICATES/PART-I-VERIFICATION-AUDIT.md)

## Research boundary

The central nonlinear term is
\[
\int_\Omega \omega^T S\omega\,dx,
\qquad
S=\frac{\nabla u+(\nabla u)^T}{2}.
\]
Controlling this term sufficiently to close the global regularity problem remains **OPEN**.

A growth estimate is not automatically a finite-time blow-up proof, and a regularity criterion is not automatically a construction of a singular solution.

## Status discipline

- **PROVED** — exact identity/theorem established under stated assumptions.
- **DERIVED** — direct consequence of established identities.
- **VERIFIED — ANALYTICAL** — written derivation checked under stated assumptions; not a software test.
- **COMPUTATIONALLY VERIFIED** — independently reproduced within stated scope.
- **OPEN** — unresolved obligation.

No global stretching estimate or global regularity proof is claimed in Part I.
