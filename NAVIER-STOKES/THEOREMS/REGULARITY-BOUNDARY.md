# Navier–Stokes — Regularity Boundary

**Research track:** Navier–Stokes  
**Status:** OPEN

## Purpose

This file records the exact boundary between the released differential identities and the unresolved global regularity question.

The established identities include the vorticity equation, the strain decomposition, the global enstrophy balance, and the local magnitude/direction factorization.

## Central nonlinear term

The global enstrophy identity contains

\[
\int_\Omega \omega^T S\omega\,dx,
\qquad
S=\frac{\nabla u+\nabla u^T}{2}.
\]

Controlling this term strongly enough to close a global regularity argument remains the central unresolved obligation in the public track.

## Critical distinction

A growth estimate for vortex stretching is not, by itself, a finite-time blow-up theorem.

Likewise, a regularity criterion of the form

\[
\int_0^T\|\omega(s)\|_{L^\infty}\,ds<\infty
\]

cannot be reversed without an additional argument establishing actual divergence.

Therefore:

- local differential identities — **PROVED / DERIVED**;
- norm estimates — **subject to stated hypotheses**;
- finite-time singularity construction — **OPEN**;
- global regularity closure — **OPEN**.

No unresolved private mechanism is reconstructed here.
