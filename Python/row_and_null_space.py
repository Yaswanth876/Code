import numpy as np

# Define matrix A
A = np.array([[1, 2, -1, 1],
              [2, 4, -3, 0],
              [1, 2, 1, 5]], dtype=float)

# Compute SVD of A
U, S, Vt = np.linalg.svd(A)

# Compute the row space basis (first 'rank' columns of U)
rank_A = np.linalg.matrix_rank(A)
row_space_basis = U[:, :rank_A]

# Compute the null space basis (columns of V corresponding to zero singular values)
null_space_basis = Vt.T[:, rank_A:]

# Compute nullity using the rank-nullity theorem
n = A.shape[1]  # Number of columns
nullity_A = n - rank_A

# Function to print a matrix in a formatted way
def print_matrix(label, M):
    print(f"\n{label}:")
    print(np.array2string(np.round(M, 3), separator=", "))

# Print results rounded to 3 decimal places
print_matrix("Basis for the row space of A", row_space_basis)
print_matrix("Basis for the null space of A", null_space_basis)

# Print rank-nullity verification
print(f"\nVerification: dim N(A) = n - r\n"
      f"dim N(A) = {nullity_A}, n - r = {n - rank_A}")
