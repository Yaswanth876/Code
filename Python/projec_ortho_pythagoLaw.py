import numpy as np
# Define vectors x and y
x = np.array([4, 2, 2, 1]).reshape(-1, 1)
y = np.array([2, 0, 0, 2]).reshape(-1, 1)
# Compute projection p of x onto y
p = (np.dot(y.T, x) / np.dot(y.T, y)) * y
# Compute z = x - p
z = x - p
# Verify orthogonality (dot product should be 0)
orthogonality_check = np.allclose(np.dot(z.T, p), 0)
# Compute squared norms
norm_x2 = np.linalg.norm(x) ** 2
norm_z2 = np.linalg.norm(z) ** 2
norm_p2 = np.linalg.norm(p) ** 2
# Verify Pythagorean theorem
pythagorean_check = np.allclose(norm_x2, norm_z2 + norm_p2)
# Print results
print(f"Projection p:\n{p}\n")
print(f"Residual vector z:\n{z}\n")
print(f"Dot product of z and p (should be 0 for orthogonality): {np.dot(z.T, p)}")
print(f"Norm Squared ||x||^2: {norm_x2}")
print(f"Sum of Norms Squared ||z||^2 + ||p||^2: {norm_z2 + norm_p2}")
print(f"Does the Pythagorean law hold? {pythagorean_check}")
