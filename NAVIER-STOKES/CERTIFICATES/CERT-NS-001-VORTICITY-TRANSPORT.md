# CERT-NS-001 — Vorticity Transport

## Objective

Record the exact vorticity transport identity for incompressible Navier–Stokes in the unforced case.

## Definition

\[
\omega=\nabla\times u,
\qquad
\nabla\cdot u=0.
\]

## Result

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

## Status

**PROVED** as the standard curl reduction under the stated smoothness assumptions.

## Boundary

This certificate records the identity only. It does not establish global regularity or finite-time singularity.
