# CERT-NS-006 — Exact SPN Structural Identity

**Status:** VERIFIED — ANALYTICAL  
**Scope:** Derivation from the smooth incompressible vorticity equation on \(\rho>0\)

## Definitions

\[
D_t=\partial_t+u\cdot\nabla,\quad
\rho=|\omega|,\quad \xi=\omega/\rho,\quad
S=\frac{\nabla u+(\nabla u)^T}{2},
\]
\[
M=D_t\rho,\qquad P=\rho\,\xi^TS\xi,\qquad N=\nu\rho|\nabla\xi|^2.
\]

## Claim

\[
M=P+\nu\Delta\rho-N,\qquad N\ge0.
\]

## Verification

The vorticity equation gives \(D_t\omega=(\omega\cdot\nabla)u+\nu\Delta\omega\). Contracting with \(\xi\) gives \(D_t\rho\) on the left. On the right, the stretching term becomes \(\rho\,\xi^TS\xi\), because the antisymmetric part of \(\nabla u\) has zero quadratic contraction. CERT-NS-005 supplies \(\xi\cdot\Delta\omega=\Delta\rho-\rho|\nabla\xi|^2\). Substitution yields the claimed identity.

## Status interpretation

“VERIFIED — ANALYTICAL” means the displayed identity is checked by the written derivation under the stated hypotheses. It does not mean a software test, numerical experiment, peer review, or proof of global regularity.

## Limitations

The production term \(P\) has no fixed sign. The nonnegative term \(N\) is not shown to dominate \(P\). Global closure and regularity remain **OPEN**.
