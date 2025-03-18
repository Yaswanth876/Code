import numpy as np

# Define vectors
x = np.array([0.4, 4, -4, 1, 1])
y = np.ones(5)  # Adjusted to match the size of x (assuming a typo in problem)

# Compute norms
norm_x = np.linalg.norm(x)
norm_y = np.linalg.norm(y)
norm_x_plus_y = np.linalg.norm(x + y)

# Verify triangle inequality
triangle_inequality = norm_x_plus_y <= (norm_x + norm_y)

# Compute parallelogram law
lhs = np.linalg.norm(x + y)**2 + np.linalg.norm(x - y)**2
rhs = 2 * (norm_x**2 + norm_y**2)
parallelogram_law = np.isclose(lhs, rhs)

# Print results
print(f"||x|| = {norm_x:.4f}")
print(f"||y|| = {norm_y:.4f}")
print(f"||x + y|| = {norm_x_plus_y:.4f}")
print(f"Triangle inequality holds: {triangle_inequality}")

print(f"\nChecking parallelogram law:")
print(f"LHS: {lhs:.4f}, RHS: {rhs:.4f}")
print(f"Parallelogram law holds: {parallelogram_law}")
