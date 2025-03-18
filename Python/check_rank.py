import numpy as np
# Set random seed for reproducibility
np.random.seed(42)
# Function to generate random integer matrices in range [a, b]
def random_int_matrix(m, n, a=1, b=10):
    return np.round((b - a) * np.random.rand(m, n)) + a
# Generate random integer matrices
A1 = random_int_matrix(10, 7)   # 10x7 matrix
A2 = random_int_matrix(8, 12)   # 8x12 matrix
A3 = random_int_matrix(10, 15)  # 10x15 matrix
# Compute ranks
rank_A1 = np.linalg.matrix_rank(A1)
rank_A2 = np.linalg.matrix_rank(A2)
rank_A3 = np.linalg.matrix_rank(A3)
# Print results
print(f"Rank of 10x7 matrix A1: {rank_A1} (Expected max: min(10,7) = 7)")
print(f"Rank of 8x12 matrix A2: {rank_A2} (Expected max: min(8,12) = 8)")
print(f"Rank of 10x15 matrix A3: {rank_A3} (Expected max: min(10,15) = 10)")
# Check if matrices have full rank
print(f"A1 has full rank: {rank_A1 == min(10, 7)}")
print(f"A2 has full rank: {rank_A2 == min(8, 12)}")
print(f"A3 has full rank: {rank_A3 == min(10, 15)}")
