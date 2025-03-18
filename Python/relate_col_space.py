import numpy as np
# Generate random integer matrices
np.random.seed(42)  # Set seed for reproducibility
B = np.round(10 * np.random.rand(8, 4))  # 8x4 matrix
X = np.round(10 * np.random.rand(4, 3))  # 4x3 matrix
C = B @ X  # Compute C as B * X
A = np.hstack((B, C))  # Concatenate B and C to form A
# Compute ranks
rank_B = np.linalg.matrix_rank(B)
rank_C = np.linalg.matrix_rank(C)
rank_A = np.linalg.matrix_rank(A)
# Print ranks
print(f"Rank of B (8x4): {rank_B}")
print(f"Rank of C (8x3): {rank_C}")
print(f"Rank of A (8x7): {rank_A} (Expected: same as rank_B)")

