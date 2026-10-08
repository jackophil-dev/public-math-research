# Navier–Stokes — Part I Release Index

**Part I scope:** Local vorticity factorization, exact magnitude evolution, geometric dissipation, and the SPN structural identity.

Part I records the analytical identities and their assumptions without claiming a solution of the global three-dimensional Navier–Stokes regularity problem.

## Theorems

- [Core mathematical identities](./CORE-MATHEMATICAL-IDENTITIES.md)
- [Geometric Dissipation Lemma](./THEOREMS/GEOMETRIC-DISSIPATION-LEMMA.md)
- [Exact SPN Structural Identity](./THEOREMS/SPN-STRUCTURAL-IDENTITY.md)
- [Regularity boundary and open obligations](./THEOREMS/REGULARITY-BOUNDARY.md)

## Certificates and audit

- [CERT-NS-001 — Vorticity Transport](./CERTIFICATES/CERT-NS-001-VORTICITY-TRANSPORT.md)
- [CERT-NS-002 — Global Enstrophy Identity](./CERTIFICATES/CERT-NS-002-ENSTROPHY.md)
- [CERT-NS-003 — Magnitude/Direction Factorization](./CERTIFICATES/CERT-NS-003-MAGNITUDE-DIRECTION.md)
- [CERT-NS-004 — Local Magnitude/Direction Balance](./CERTIFICATES/CERT-NS-004-LOCAL-BALANCE.md)
- [CERT-NS-005 — Geometric Dissipation Lemma](./CERTIFICATES/CERT-NS-005-GEOMETRIC-DISSIPATION.md)
- [CERT-NS-006 — Exact SPN Structural Identity](./CERTIFICATES/CERT-NS-006-SPN-STRUCTURAL-IDENTITY.md)
- [Part I Verification Audit](./CERTIFICATES/PART-I-VERIFICATION-AUDIT.md)

## Status discipline

“VERIFIED — ANALYTICAL” denotes a checked written derivation, not a software test, numerical validation, or peer review. The statements are local on \(\rho>0\) unless otherwise specified. No global stretching estimate or global regularity proof is claimed.

Part II is reserved for the unresolved quantitative nonlinear closure and continuation/regularity obligations.
