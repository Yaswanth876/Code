import numpy as np
import scipy.linalg as la
# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for row space of A (Y)
Y, _ = np.linalg.qr(A.T)  # QR decomposition gives orthonormal columns for R(A^T)
# Compute projection matrix U = Y Y^T
U = Y @ Y.T
# Generate random vector b in R^5
b = np.random.rand(5, 1)
# Compute projection y = U * b
y = U @ b
# Verify idempotency: Compute U * y and compare with y
Uy = U @ y
idempotency_check = np.allclose(Uy, y)
# Compute s = b - y
s = b - y
# Verify that s is in N(A) by computing A * s (should be approximately zero)
A_s = A @ s
zero_check = np.allclose(A_s, np.zeros_like(A_s))
# Print results
print(f"Random vector b:\n{b}\n")
print(f"Projection y = U b:\n{y}\n")
print(f"U y:\n{Uy}\n")
print(f"Is U y close to y? {idempotency_check}\n")
print(f"Residual vector s = b - y:\n{s}\n")
print(f"A s (should be approximately zero):\n{A_s}\n")
print(f"Is A s close to zero? {zero_check}")
