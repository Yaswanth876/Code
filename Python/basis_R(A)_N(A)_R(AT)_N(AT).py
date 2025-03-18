import sympy as sp

# Define the given matrices
A1 = sp.Matrix([[3, 4], [6, 8]])
A2 = sp.Matrix([[1, 3, 1], [2, 4, 0]])

def compute_subspaces(A):
    AT = A.T  # Transpose of A

    # Column space of A (basis for R(A))
    col_space_A = A.columnspace()

    # Null space of A (basis for N(A))
    null_space_A = A.nullspace()

    # Column space of A^T (basis for R(A^T))
    col_space_AT = AT.columnspace()

    # Null space of A^T (basis for N(A^T))
    null_space_AT = AT.nullspace()

    return col_space_A, null_space_A, col_space_AT, null_space_AT

# Compute for both matrices
results_A1 = compute_subspaces(A1)
results_A2 = compute_subspaces(A2)

# Print results
def print_results(matrix_label, results):
    col_space_A, null_space_A, col_space_AT, null_space_AT = results
    print(f"\nResults for {matrix_label}:")
    print("Basis for R(A):", col_space_A)
    print("Basis for N(A):", null_space_A)
    print("Basis for R(A^T):", col_space_AT)
    print("Basis for N(A^T):", null_space_AT)

print_results("A1", results_A1)
print_results("A2", results_A2)
