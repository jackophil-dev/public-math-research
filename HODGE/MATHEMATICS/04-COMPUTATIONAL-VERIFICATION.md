# Hodge — Computational Verification

Input: \(G=\begin{pmatrix}36&12\\12&0\end{pmatrix}\).

Exact hand checks:
- \(G^T=G\).
- \(\det G=-144\).
- The recorded SNF diagonal product is \(12\cdot12=144=|\det G|\).
- The recorded group \((\mathbb Z/12)^2\) has order 144.

For reproducibility, retain the full input matrix, basis ordering, source of entries, exact-integer SNF output, and preferably the unimodular transformation matrices. A determinant check alone does not establish the SNF.

These are direct arithmetic consistency checks on recorded values. This repository update does not claim a new independent software run. No numerical or symbolic computation can establish the missing geometric identification without the corresponding geometric data.