# Replicator — Core Equations and Derivations

## Invariant-set condition
If \(s_{t+1}=T(s_t,u_t)\) and \(T(s,u)\in K\) for all \(s\in K\) and admissible \(u\), then an initial state \(s_0\in K\) remains in \(K\) at all discrete times.

## Measurement and feedback
A generic observation model is \(m_t=\mathcal O(s_t)+\xi_t\). A controller may use \(u_t=C(s^*-\widehat s_t)\). This is only a template: stability depends on the plant, estimator, controller, delay, noise, and actuator constraints.

## Lyapunov candidate
For \(\dot e=f(e)\), a positive-definite \(V(e)\) with \(\dot V\le-c\|e\|^2\), \(c>0\), may imply stability/convergence under the appropriate regularity, domain, and invariance hypotheses. No implementation-specific conclusion follows until those hypotheses are established.

## Resource/conservation accounting
A model may require \(N_{steps}\le N_{max}\) and \(E_{used}\le E_{budget}\). Element inventories in a closed system should balance after accounting for feeds, outputs, and waste. Such inequalities are verified properties only after quantities, boundaries, and measurements are defined.