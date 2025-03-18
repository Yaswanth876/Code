import sympy as sp
# Define the variable
x = sp.Symbol('x')
# Define the inner product function
def inner_product(f, g):
    return sp.integrate(f * g, (x, 0, 1))
# Define the functions
f1 = 1
f2 = x
# Compute the inner products
inner_11 = inner_product(f1, f1)
inner_12 = inner_product(f1, f2)
inner_22 = inner_product(f2, f2)
# Compute the angle theta
theta = sp.acos(inner_12 / sp.sqrt(inner_11 * inner_22))
# Compute the projection of 1 onto x
p = (inner_12 / inner_22) * f2
# Compute norms
norm_1_p = sp.sqrt(inner_product(f1 - p, f1 - p))
norm_p = sp.sqrt(inner_product(p, p))
norm_1 = sp.sqrt(inner_11)
# Verify Pythagorean theorem
pythagorean_check = sp.simplify(norm_1**2 - (norm_p**2 + norm_1_p**2))
# Print results
print("Angle θ between 1 and x:", theta.evalf())
print("\nProjection p of 1 onto x:", p)
print("\nInner product ⟨1 - p, p⟩:", inner_product(f1 - p, p))
print("\nNorms:")
print("‖1 - p‖ =", norm_1_p.evalf())
print("‖p‖ =", norm_p.evalf())
print("‖1‖ =", norm_1.evalf())
print("\nPythagorean theorem verification (should be 0):", pythagorean_check)
