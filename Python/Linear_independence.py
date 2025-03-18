import numpy as np
def check_linear_independence(vectors):
    matrix = np.column_stack(vectors)
    rank = np.linalg.matrix_rank(matrix)
    num_vectors = matrix.shape[1]
    return rank == num_vectors  # True if independent, False if dependent
# Define the vectors
vectors_a = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
vectors_b = [np.array([1, 0, 0]), np.array([0, 1, 1]), np.array([1, 0, 1]), np.array([1, 2, 3])]
# Check for linear independence
independent_a = check_linear_independence(vectors_a)
independent_b = check_linear_independence(vectors_b)
# Print results
print("Vectors in (a) are linearly independent:", independent_a)
print("Vectors in (b) are linearly independent:", independent_b)

