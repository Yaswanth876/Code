import numpy as np
# Define vectors
x = np.array([0.4, 4, -4, 1, 1])
y = np.ones(5)  # Adjusted to match x's size
# Compute vector projection of x onto y
p = (np.dot(x, y) / np.dot(y, y)) * y
# Compute z = x - p
z = x - p
# Verify orthogonality by computing dot product ⟨z, p⟩
dot_zp = np.dot(z, p)
# Compute norms
norm_x_sq = np.linalg.norm(x) ** 2
norm_z_sq = np.linalg.norm(z) ** 2
norm_p_sq = np.linalg.norm(p) ** 2
# Verify Pythagorean theorem
pythagorean_check = np.isclose(norm_x_sq, norm_z_sq + norm_p_sq)
# Print results
print(f"Projection p of x onto y: {p}")
print(f"z = x - p: {z}")
print(f"Dot product ⟨z, p⟩ (should be 0 if orthogonal): {dot_zp:.4f}")
print(f"||x||² = {norm_x_sq:.4f}")
print(f"||z||² + ||p||² = {norm_z_sq + norm_p_sq:.4f}")
print(f"Pythagorean theorem holds: {pythagorean_check}")
