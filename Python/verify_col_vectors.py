import numpy as np
# Generate random integer matrices U and V
np.random.seed(42)  # For reproducibility
U = np.round(20 * np.random.rand(4, 4)) - 10
V = np.round(10 * np.random.rand(4, 4))
# Compute the rank of U and V
rank_U = np.linalg.matrix_rank(U)
rank_V = np.linalg.matrix_rank(V)
# Verify if they form a basis for R^4
is_U_basis = rank_U == 4
is_V_basis = rank_V == 4
# Print results
print(f"Matrix U:\n{U}\n")
print(f"Rank of U: {rank_U}")
print(f"Do the columns of U form a basis for R^4? {is_U_basis}\n")
print(f"Matrix V:\n{V}\n")
print(f"Rank of V: {rank_V}")
print(f"Do the columns of V form a basis for R^4? {is_V_basis}")
