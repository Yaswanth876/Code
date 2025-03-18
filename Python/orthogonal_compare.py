import numpy as np
import scipy.linalg as la
# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for column space of A (Q)
Q, _ = np.linalg.qr(A)  # QR decomposition gives orthonormal columns for R(A)
# Compute null space of A^T (W)
W = la.null_space(A.T)  # Orthonormal basis for N(A^T)
# Construct S matrix
S = np.hstack((Q, W))
# Verify orthogonality: Compute S * S^T
S_ST = S @ S.T
I = np.eye(5)  # Identity matrix
# Compute A^T W and W^T A (should be zero matrices)
AT_W = A.T @ W
WT_A = W.T @ A
# Print results
print(f"S * S^T:\n{S_ST}\n")
print(f"Comparison with identity matrix I:\n{I}\n")
print(f"A^T * W:\n{AT_W}\n")
print(f"W^T * A:\n{WT_A}\n")
