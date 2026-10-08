# CERT-002 — Resource Bounding & Limits

## Objective

Declare hard bounds for execution depth, memory and numerical precision.

## Specification

\[
N\le N_{\max},
\qquad
\mathcal M_{\mathrm{alloc}}\le\mathcal M_{\mathrm{limit}}.
\]

Numerical precision must be stated together with a justified error model; a numerical value such as \(10^{-12}\) is a parameter requirement, not automatically a proved property.

## Status

**SPECIFICATION / OPEN VALIDATION**
