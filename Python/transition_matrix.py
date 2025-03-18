import numpy as np
# Generate random matrix U (assumed to be a basis for R^4)
np.random.seed(42)  # For reproducibility
U = np.round(20 * np.random.rand(4, 4)) - 10
# Define the vector b
b = np.ones((4, 1))
# Compute the coordinate vector c (solution to Uc = b)
c = np.linalg.solve(U, b)
# Verify that Uc = b
verification = np.allclose(U @ c, b)
# Print results
print(f"Matrix U (Basis for R^4):\n{U}\n")
print(f"Vector b:\n{b}\n")
print(f"Coordinate vector c:\n{c}\n")
print(f"Verification (Is Uc ≈ b?): {verification}")