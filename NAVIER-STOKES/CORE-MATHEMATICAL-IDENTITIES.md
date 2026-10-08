# Navier–Stokes Research

This directory contains the public Navier–Stokes research track.

## Public mathematical core

The currently released core records the exact incompressible vorticity identities and the local magnitude/direction decomposition. It does **not** claim a completed global regularity proof.

### 1. Incompressible Navier–Stokes

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0.
\]

### 2. Vorticity equation

\[
\omega=\nabla\times u,
\]

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

### 3. Strain tensor

\[
S=\frac{\nabla u+\nabla u^T}{2}.
\]

### 4. Global enstrophy identity

\[
\frac12\frac{d}{dt}\|\omega\|_2^2
+\nu\|\nabla\omega\|_2^2
=
\int \omega^T S\omega\,dx.
\]

The nonlinear stretching term
\[
\int \omega^T S\omega\,dx
\]
is the central global obstruction.

### 5. Magnitude/direction factorization

Where \(\rho=|\omega|>0\),
\[
\omega=\rho\xi,
\qquad |\xi|=1.
\]

The local balance is
\[
D_t\rho
=
\rho\,\xi^TS\xi
+\nu\Delta\rho
-\nu\rho|\nabla\xi|^2,
\qquad
D_t=\partial_t+u\cdot\nabla.
\]

Equivalently, with
\[
M=D_t\rho,\qquad
P=\rho\,\xi^TS\xi,\qquad
N=\nu\rho|\nabla\xi|^2,
\]
one has
\[
M=P+\nu\Delta\rho-N.
\]

Here \(N\ge0\); it is not asserted to be strictly positive everywhere.

## Status

- Vorticity transport equation — **PROVED**
- Global enstrophy identity — **PROVED**
- Kinematic factorization \(\omega=\rho\xi\) — **PROVED** where \(\rho>0\)
- Local magnitude/direction balance — **DERIVED**
- Global nonlinear regularity closure — **OPEN**

No private derivation or unreleased calculation is represented here as a completed theorem.

## Certificates

The public certificate sequence will use the same discipline as the HODGE track:

- **PROVED**
- **COMPUTATIONALLY VERIFIED**
- **DERIVED**
- **OPEN**

The previously empty Navier–Stokes \`CERT-001\` through \`CERT-004\` placeholders were removed. Their original complete source texts are not present in the current private repository, so they are **not reconstructed or fabricated here**.
