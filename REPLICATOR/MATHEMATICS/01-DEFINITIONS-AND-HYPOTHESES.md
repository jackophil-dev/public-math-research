# Replicator — Definitions and Hypotheses

Let \(S\subseteq\mathbb R^n\) be a state space, \(\mathcal U_{adm}\) admissible controls, and \(s_{t+1}=T(s_t,u_t)\) a discrete-time model. A concrete system must declare state variables, units, domains, controls, and transition map.

An observation model can be written
\[
m_t=\mathcal O(s_t)+\xi_t,
\]
where \(\mathcal O\) is an observation operator and \(\xi_t\) measurement error. Any bound on \(\xi_t\) is an assumption until supported by calibration.

For target \(s^*\) and estimate \(\widehat s_t\), define residual \(e_t=s^*-\widehat s_t\). Its norm, metric, uncertainty, and correction threshold must be specified.

A set \(K\subseteq S\) is positively invariant if every admissible transition from \(K\) remains in \(K\). Resource budgets require explicit units and accounting boundaries. No physical implementation or universal reconstruction capability is assumed by this architecture.