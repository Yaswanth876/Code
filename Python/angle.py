import numpy as np
# Define vectors
x = np.array([0.4, 4, -4, 1, 1])
y = np.ones(5)  # Adjusted to match x's size
# Compute dot product
dot_xy = np.dot(x, y)
# Compute norms
norm_x = np.linalg.norm(x)
norm_y = np.linalg.norm(y)
# Compute t
t = dot_xy / (norm_x * norm_y)
# Compute angle in radians
theta_rad = np.arccos(t)
# Convert to degrees
theta_deg = np.degrees(theta_rad)
# Print results
print(f"t = {t:.4f}")
print(f"Angle (radians) = {theta_rad:.4f}")
print(f"Angle (degrees) = {theta_deg:.4f}")
# Verify |t| <= 1
print(f"|t| <= 1: {abs(t) <= 1}")
