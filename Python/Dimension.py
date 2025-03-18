import numpy as np

# Define the matrices for part (a) and (b)
vectors_a = np.array([[1, 2, -3], [-2, -2, 3], [2, 4, 6]])
vectors_b = np.array([[1, 1, 2], [1, 2, 3], [1, 3, 1]])

# Compute the rank (dimension of the spanned subspace)
dimension_a = np.linalg.matrix_rank(vectors_a)
dimension_b = np.linalg.matrix_rank(vectors_b)

# Print the dimensions
print("Dimension of subspace spanned by vectors in (a):", dimension_a)
print("Dimension of subspace spanned by vectors in (b):", dimension_b)
