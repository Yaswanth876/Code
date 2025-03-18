import numpy as np
# Set random seed for reproducibility
np.random.seed(42)
# Generate random matrices
A1 = np.random.rand(6, 6)  # 6x6 matrix
A2 = np.random.rand(8, 6)  # 8x6 matrix
A3 = np.random.rand(5, 8)  # 5x8 matrix
# Compute ranks
rank_A1 = np.linalg.matrix_rank(A1)
rank_A2 = np.linalg.matrix_rank(A2)
rank_A3 = np.linalg.matrix_rank(A3)
# Print results
print(f"Rank of 6x6 matrix A1: {rank_A1} (Expected: min(6,6) = 6)")
print(f"Rank of 8x6 matrix A2: {rank_A2} (Expected: min(8,6) = 6)")
print(f"Rank of 5x8 matrix A3: {rank_A3} (Expected: min(5,8) = 5)")
 