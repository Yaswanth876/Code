import numpy as np
# Set random seed for reproducibility
np.random.seed(42)
# Generate random matrices X (8x2) and Y (6x2)
X = np.random.rand(8, 2)
Y = np.random.rand(6, 2)
# Construct the matrix A = X * Y^T
A = X @ Y.T  # Matrix multiplication
# Compute and print the rank of A
rank_A = np.linalg.matrix_rank(A)
expected_rank = min(np.linalg.matrix_rank(X), np.linalg.matrix_rank(Y))
print(f"Rank of 8x6 matrix A: {rank_A}")
print(f"Expected rank (min(rank(X), rank(Y))): {expected_rank}")
print(f"Does rank(A) match the expected value? {rank_A == expected_rank}")
