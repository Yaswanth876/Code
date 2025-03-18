import sympy as sp

# Define the given vectors as rows of a matrix
A = sp.Matrix([[1, 0, -2, 1], [0, 1, 3, -2]])

# Find the null space of A (which gives the orthogonal complement S⊥)
null_space_basis = A.nullspace()

# Print the basis for S⊥
print("Basis for S⊥:")
for vec in null_space_basis:
    print(vec)
