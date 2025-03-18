import numpy as np
def generate_matrix(m, n, r):
    """Generate an m x n matrix of rank r"""
    U = np.random.rand(m, r)  # m x r matrix
    V = np.random.rand(r, n)  # r x n matrix
    return U @ V  # Matrix multiplication gives m x n matrix with rank r
# Set random seed for reproducibility
np.random.seed(42)
# Generate matrices
A = generate_matrix(8, 8, 3)  # 8x8 matrix with rank 3
B = generate_matrix(6, 9, 4)  # 6x9 matrix with rank 4
C = generate_matrix(10, 7, 5) # 10x7 matrix with rank 5
# Compute and print ranks
print(f"Rank of A (8x8): {np.linalg.matrix_rank(A)} (Expected: 3)")
print(f"Rank of B (6x9): {np.linalg.matrix_rank(B)} (Expected: 4)")
print(f"Rank of C (10x7): {np.linalg.matrix_rank(C)} (Expected: 5)")
