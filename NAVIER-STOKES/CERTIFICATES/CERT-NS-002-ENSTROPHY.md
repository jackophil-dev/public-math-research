# CERT-NS-002 — Global Enstrophy Identity

## Objective

Record the global enstrophy balance under boundary/decay assumptions that eliminate the required boundary terms.

## Definition

\[
\mathcal E(t)=\frac12\int_\Omega|\omega|^2\,dx.
\]

## Result

\[
\frac12\frac{d}{dt}\|\omega\|_{L^2}^2
+\nu\|\nabla\omega\|_{L^2}^2
=
\int_\Omega\omega^TS\omega\,dx,
\]

where

\[
S=\frac{\nabla u+\nabla u^T}{2}.
\]

## Status

**PROVED** under the stated boundary/decay assumptions.

## Limitation

The identity isolates the nonlinear stretching term; it does not itself close the global regularity problem.
