# THEOREM-002 — Lyapunov Convergence (Conditional)

## Statement

Suppose a positive-definite Lyapunov function \(V\) is defined on the relevant invariant domain and satisfies the regularity assumptions of the applicable Lyapunov theorem. If

\[
\dot V\le-\alpha\|e_t\|^2,
\qquad \alpha>0,
\]

then the corresponding stability or convergence conclusion follows under the remaining hypotheses of that theorem.

## Status

**DERIVED / CONDITIONAL**

The feedback inequality is a sufficient ingredient, not a complete proof of exponential convergence by itself.

## Limitation

The target manifold, class of dynamics, measurement error, actuator constraints and required Lyapunov hypotheses must be explicitly specified before a stronger convergence rate is claimed.
