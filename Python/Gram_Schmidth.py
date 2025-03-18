import numpy as np

def gram_schmidt(X):
    """Efficient Gram-Schmidt process to compute an orthonormal basis."""
    m, n = X.shape
    Q = np.zeros((m, n), dtype=np.float64)

    for i in range(n):
        q = X[:, i].copy()
        for j in range(i):
            proj = np.dot(Q[:, j], q) * Q[:, j]
            q -= proj
        q /= np.linalg.norm(q)
        Q[:, i] = q

    return Q

# Define the matrix with given vectors as columns
X = np.array([[4, 2, 1],
              [2, 0, 1],
              [2, 0, -1],
              [1, 2, 1]], dtype=float)

# Compute the orthonormal basis using the optimized Gram-Schmidt process
orthonormal_basis = gram_schmidt(X)

# Print the orthonormal basis rounded to 3 decimal places
print("Orthonormal basis for the subspace:")
print(np.round(orthonormal_basis, 3))  # Rounds the matrix to 3 decimal places
