import numpy as np
import scipy.linalg as la
# Generate random matrices
np.random.seed(42)  # For reproducibility
A = np.random.rand(5, 2) @ np.random.rand(2, 5)  # A = (5x2) * (2x5)
# Compute rank
rank_A = np.linalg.matrix_rank(A)
# Compute null space (orthonormal basis for N(A))
null_space_A = la.null_space(A)
# Print results
print(f"Matrix A:\n{A}\n")
print(f"Rank of A: {rank_A}")
print(f"Nullity of A (expected 5 - rank): {A.shape[1] - rank_A}")
print(f"Orthonormal basis for N(A) (columns of Z):\n{null_space_A}")
