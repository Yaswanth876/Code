import numpy as np
import scipy.linalg as la
# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for column space of A (Q)
Q, _ = np.linalg.qr(A)  # QR decomposition gives orthonormal columns for R(A)
# Generate random vector c in R^5
c = np.random.rand(5, 1)
# Compute projection q = QQ^T c
q = Q @ Q.T @ c
# Compute r = c - q
r = c - q
# Verify that r is in N(A^T) by computing A^T r (should be approximately zero)
AT_r = A.T @ r
zero_check = np.allclose(AT_r, np.zeros_like(AT_r))
# Print results
print(f"Random vector c:\n{c}\n")
print(f"Projection q = QQ^T c:\n{q}\n")
print(f"Residual vector r = c - q:\n{r}\n")
print(f"A^T r (should be approximately zero):\n{AT_r}\n")
print(f"Is A^T r close to zero? {zero_check}")
