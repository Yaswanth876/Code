import numpy as np
# Generate two random basis matrices E and F (assumed to be full-rank)
np.random.seed(42)  # For reproducibility
E = np.round(20 * np.random.rand(4, 4)) - 10  # Basis E
F = np.round(20 * np.random.rand(4, 4)) - 10  # Basis F
# Compute transition matrix S (from E to F)
S = np.linalg.solve(F, E)
# Compute transition matrix T (from F to E)
T = np.linalg.solve(E, F)
# Verify S and T are inverses of each other (S * T should be the identity matrix)
identity_check = np.allclose(S @ T, np.eye(4))
# Define coordinate vector c in basis E
c = np.random.rand(4, 1)
# Compute coordinate vector d in basis F
d = S @ c
# Verify S c = d and T d = c
verify_Sc_d = np.allclose(S @ c, d)
verify_Td_c = np.allclose(T @ d, c)
# Print results
print(f"Basis E:\n{E}\n")
print(f"Basis F:\n{F}\n")
print(f"Transition matrix S (E to F):\n{S}\n")
print(f"Transition matrix T (F to E):\n{T}\n")
print(f"Are S and T inverses? {identity_check}\n")
print(f"Coordinate vector c:\n{c}\n")
print(f"Coordinate vector d (S @ c):\n{d}\n")
print(f"Verification S c = d: {verify_Sc_d}")
print(f"Verification T d = c: {verify_Td_c}")
