import numpy as np

def vector_projection(x, y):
    """Compute the projection of x onto y."""
    proj_coefficient = np.dot(x, y) / np.dot(y, y)
    p = proj_coefficient * y
    return p

def check_orthogonality(v1, v2):
    """Check if two vectors are orthogonal by computing their dot product."""
    return np.isclose(np.dot(v1, v2), 0)

# Define the given vectors
vectors = [
    (np.array([3, 4]), np.array([1, 0])),
    (np.array([3, 5]), np.array([1, 1])),
    (np.array([2, 4, 3]), np.array([1, 1, 1])),
    (np.array([2, -5, 4]), np.array([1, 2, -1]))
]

# Compute projections and check orthogonality
for i, (x, y) in enumerate(vectors, start=1):
    p = vector_projection(x, y)
    x_minus_p = x - p
    is_orthogonal = check_orthogonality(p, x_minus_p)
    
    print(f"\nCase ({chr(96 + i)}):")
    print(f"Projection p of x onto y: {p}")
    print(f"x - p: {x_minus_p}")
    print(f"Are p and x - p orthogonal? {'Yes' if is_orthogonal else 'No'}")
