import numpy as np

# Generate random matrix A
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)
# Compute orthonormal basis for column space of A (Q)
Q, _ = np.linalg.qr(A)  # QR decomposition gives orthonormal columns for R(A)
# Generate random vector b in the column space of A
b = A @ np.random.rand(5, 1)
# Compute Q Q^T b
QQT_b = Q @ Q.T @ b
# Verify if Q Q^T b ≈ b
identity_check = np.allclose(QQT_b, b)
# Print results
print(f"b:\n{b}\n")
print(f"Q Q^T b:\n{QQT_b}\n")
print(f"Identity Q Q^T b = b holds: {identity_check}")