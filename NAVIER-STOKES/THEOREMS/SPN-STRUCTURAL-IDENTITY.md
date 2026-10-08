# Theorem NS-I.4 — Exact SPN Structural Identity

**Status:** DERIVED from the vorticity equation and Theorem NS-I.3  
**Track:** Navier–Stokes, Part I

## Hypotheses

Assume a sufficiently smooth solution of the unforced three-dimensional incompressible Navier–Stokes equations, with \(\nu>0\). On the regular set \(\mathcal R_t=\{x:|\omega(x,t)|>0\}\), write
\[
\rho=|\omega|,\qquad \xi=\omega/\rho,\qquad |\xi|=1,
\]
and define the strain tensor
\[
S=\frac{\nabla u+(\nabla u)^T}{2}.
\]

## Definitions

\[
M:=D_t\rho,\qquad D_t:=\partial_t+u\cdot\nabla,
\qquad P:=\rho\,\xi^TS\xi,\qquad N:=\nu\rho|\nabla\xi|^2.
\]

## Identity

\[
D_t\rho=\rho\,\xi^TS\xi+\nu\Delta\rho-\nu\rho|\nabla\xi|^2.
\]
Equivalently,
\[
\boxed{M=P+\nu\Delta\rho-N,\qquad N\ge0.}
\]
This is an exact structural identity, not an additional independent theorem or a closed estimate.

## Proof

The vorticity equation is
\[
D_t\omega=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]
On \(\rho>0\), dot with \(\xi=\omega/\rho\). The left-hand side satisfies \(\xi\cdot D_t\omega=D_t\rho\), because \(\xi\cdot D_t\xi=0\). The stretching contraction is
\[
\xi\cdot((\omega\cdot\nabla)u)=\rho\,\xi^T(\nabla u)\xi
=\rho\,\xi^TS\xi,
\]
since the antisymmetric part of \(\nabla u\) has zero quadratic contraction. By Theorem NS-I.3,
\[
\nu\,\xi\cdot\Delta\omega=\nu\Delta\rho-\nu\rho|\nabla\xi|^2.
\]
Combining these equalities gives the magnitude equation and then the SPN identity. Nonnegativity of \(N\) follows from \(\nu>0\), \(\rho>0\), and \(|\nabla\xi|^2\ge0\). \(\square\)

## Epistemic boundary

- The identity is local on the regular set and under the stated smoothness assumptions.
- \(P\) may be positive, zero, or negative; no sign is asserted for vortex stretching.
- \(N\ge0\) is exact, but no estimate controlling \(P\) by \(N\) is established here.
- Global nonlinear closure, global-in-time regularity, and finite-time singularity exclusion remain **OPEN**.
