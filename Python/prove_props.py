import numpy as np
import scipy.linalg as la
# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for column space of A (Q)
Q, _ = np.linalg.qr(A)  # QR decomposition gives orthonormal columns for R(A)
# Compute null space of A^T (W)
W = la.null_space(A.T)  # Orthonormal basis for N(A^T)
# Compute identity matrix
I = np.eye(5)
# Verify the first identity: I - WW^T = QQ^T
lhs1 = I - W @ W.T
rhs1 = Q @ Q.T
identity1_check = np.allclose(lhs1, rhs1)
# Verify the second identity: QQ^T A = A
lhs2 = Q @ Q.T @ A
rhs2 = A
identity2_check = np.allclose(lhs2, rhs2)
# Print results
print(f"I - W W^T:\n{lhs1}\n")
print(f"Q Q^T:\n{rhs1}\n")
print(f"Identity 1 holds: {identity1_check}\n")
print(f"Q Q^T A:\n{lhs2}\n")
print(f"A:\n{rhs2}\n")
print(f"Identity 2 holds: {identity2_check}")
