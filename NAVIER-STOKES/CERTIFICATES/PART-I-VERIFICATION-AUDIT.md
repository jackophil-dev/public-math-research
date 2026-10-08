# Navier–Stokes Part I — Verification Audit

**Release scope:** Local vorticity structure and exact scalar identities  
**Audit status:** ANALYTICAL DERIVATIONS RECORDED; GLOBAL CLOSURE OPEN

## Certificate register

| Item | Result | Status | Scope boundary |
|---|---|---|---|
| CERT-NS-001 | Incompressible vorticity transport | PROVED | Smooth unforced solution |
| CERT-NS-002 | Global enstrophy identity | PROVED | Required boundary/decay conditions |
| CERT-NS-003 | Magnitude/direction factorization | PROVED | Only where \(\rho=|\omega|>0\) |
| CERT-NS-004 | Local magnitude/direction balance | DERIVED | Local regular set; smoothness assumptions |
| CERT-NS-005 | Geometric dissipation identity | VERIFIED — ANALYTICAL | Local regular set |
| CERT-NS-006 | Exact SPN structural identity | VERIFIED — ANALYTICAL | Follows from vorticity equation and CERT-NS-005 |

## Core mathematical checks

- The factorization \(\omega=\rho\xi\) is used only where \(\rho>0\).
- The unit-vector identity \(\xi\cdot\Delta\xi=-|\nabla\xi|^2\) follows by applying the Laplacian to \(\xi\cdot\xi=1\).
- The cross term in \(\xi\cdot\Delta(\rho\xi)\) vanishes because \(\xi\cdot\partial_j\xi=0\).
- \(N=\nu\rho|\nabla\xi|^2\ge0\); strict positivity is not claimed.
- \(P=\rho\,\xi^TS\xi\) has no asserted sign.
- \(\nu\Delta\rho\) remains the ordinary scalar Laplacian contribution; \(N\) is not an extra physical viscosity.
- No universal inequality bounding stretching by geometric dissipation is claimed.
- No numerical execution or computer-assisted proof is claimed by these analytical certificates.

## Explicitly open obligations

1. Quantitative control of the nonlinear vortex-stretching term sufficient for global closure.
2. A global-in-time continuation argument derived from such control.
3. Any proof excluding finite-time singularities in three dimensions.

These are outside Part I and remain open. The exact local identities do not by themselves solve the global regularity problem.
