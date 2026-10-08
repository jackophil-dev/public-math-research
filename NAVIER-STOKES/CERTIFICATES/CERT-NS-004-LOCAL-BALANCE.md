# CERT-NS-004 — Local Magnitude/Direction Balance

## Objective

Record the derived scalar balance obtained from the vorticity magnitude/direction factorization.

## Definitions

\[
D_t=\partial_t+u\cdot\nabla,
\]

\[
M=D_t\rho,
\qquad
P=\rho\,\xi^TS\xi,
\qquad
N=\nu\rho|\nabla\xi|^2.
\]

## Result

\[
D_t\rho
=
\rho\,\xi^TS\xi
+\nu\Delta\rho
-\nu\rho|\nabla\xi|^2,
\]

hence

\[
M=P+\nu\Delta\rho-N.
\]

Moreover,

\[
N\ge0.
\]

## Status

**DERIVED**.

## Limitation

This local decomposition does not by itself provide the missing global regularity closure.
