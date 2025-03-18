import numpy as np
# Set random seed for reproducibility
np.random.seed(42)
# Generate random integer vectors x (8x1) and y (6x1) in range [1, 10]
x = np.round(9 * np.random.rand(8, 1)) + 1
y = np.round(9 * np.random.rand(6, 1)) + 1
# Construct the matrix A = x * y^T (outer product)
A = x @ y.T  # Equivalent to np.outer(x, y).reshape(8,6)
# Compute and print the rank of A
rank_A = np.linalg.matrix_rank(A)
print(f"Rank of 8x6 matrix A: {rank_A} (Expected: 1)")
