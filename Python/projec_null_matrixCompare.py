import numpy as np
import scipy.linalg as la
# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for null space of A (Z)
Z = la.null_space(A)  # Orthonormal basis for N(A)
# Compute projection matrix V = ZZ^T
V = Z @ Z.T
# Generate random vector b in R^5
b = np.random.rand(5, 1)
# Compute projection V * b
Vb = V @ b
# Compute s = b - U b (from previous task, where U projects onto R(A^T))
Y, _ = np.linalg.qr(A.T)  # Orthonormal basis for R(A^T)
U = Y @ Y.T  # Projection matrix for R(A^T)
s = b - U @ b  # s should be in N(A)
# Compare Vb with s
comparison_check = np.allclose(Vb, s)
# Print results
print(f"Projection V * b:\n{Vb}\n")
print(f"Residual vector s = b - U b:\n{s}\n")
print(f"Are V * b and s approximately equal? {comparison_check}")
