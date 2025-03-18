import numpy as np
def check_orthogonality(u, v):
    # Compute squared norms
    norm_u_sq = np.linalg.norm(u) ** 2
    norm_v_sq = np.linalg.norm(v) ** 2
    norm_u_v_sq = np.linalg.norm(u + v) ** 2
    # Compute inner product
    dot_product = np.dot(u, v)
    # Check if the Pythagorean theorem holds
    pythagorean_law_holds = np.isclose(norm_u_v_sq, norm_u_sq + norm_v_sq)
    # Check if vectors are orthogonal
    orthogonal = np.isclose(dot_product, 0)
    # Print results
    print(f"||u + v||^2 = {norm_u_v_sq}")
    print(f"||u||^2 + ||v||^2 = {norm_u_sq + norm_v_sq}")
    print(f"Dot Product u·v = {dot_product}")
    if pythagorean_law_holds:
        print("The Pythagorean law holds.")
        if orthogonal:
            print("Vectors u and v are orthogonal.")
        else:
            print("Vectors u and v are NOT orthogonal (contradiction).")
    else:
        print("The Pythagorean law does NOT hold.")
# Example vectors
u = np.array([3, 4])
v = np.array([4, -3])
# Check orthogonality
check_orthogonality(u, v)
