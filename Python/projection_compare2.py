import numpy as np
import scipy.linalg as la
# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for null space of A^T (W)
W = la.null_space(A.T)  # Orthonormal basis for N(A^T)
# Generate random vector c in R^5
c = np.random.rand(5, 1)
# Compute projection w = WW^T c
w = W @ W.T @ c
# Compute r = c - Q Q^T c (previous result)
Q, _ = np.linalg.qr(A)  # Orthonormal basis for R(A)
r = c - Q @ Q.T @ c  # r is in N(A^T)
# Compare w with r
comparison_check = np.allclose(w, r)
# Print results
print(f"Projection w = WW^T c:\n{w}\n")
print(f"Residual vector r = c - Q Q^T c:\n{r}\n")
print(f"Are w and r approximately equal? {comparison_check}")
