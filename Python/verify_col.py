import numpy as np
import sympy as sp
# Generate random integer matrices
np.random.seed(42)  # Set seed for reproducibility
B = np.round(10 * np.random.rand(8, 4))  # 8x4 matrix
X = np.round(10 * np.random.rand(4, 3))  # 4x3 matrix
C = B @ X  # Compute C as B * X
A = np.hstack((B, C))  # Concatenate B and C to form A
# Convert A to a sympy Matrix and compute its Reduced Row Echelon Form (RREF)
A_sym = sp.Matrix(A)
U, pivots = A_sym.rref()
# Display results
print("Reduced Row Echelon Form of A (U):")
sp.pprint(U)
print("\nPivot Columns:", pivots)

