import sympy as sp

# Define the variable x
x = sp.Symbol('x')

# Define the standard basis for P3 (ensure all elements are SymPy expressions)
basis = [sp.sympify(1), x, x**2, x**3]

# Define the given inner product function
def inner_product(p, q, points):
    p, q = sp.sympify(p), sp.sympify(q)  # Ensure they are SymPy expressions
    return sum(sp.sympify(p.subs(x, xi)) * sp.sympify(q.subs(x, xi)) for xi in points)

# Define the points
points = [-1, 0, 1]

# Construct the Gram-Schmidt process
def gram_schmidt(basis, inner_product, points):
    ortho_basis = []
    
    for i in range(len(basis)):
        vi = sp.sympify(basis[i])  # Ensure vi is a SymPy expression
        
        for j in range(i):
            num = inner_product(vi, ortho_basis[j], points)
            denom = inner_product(ortho_basis[j], ortho_basis[j], points)
            if denom == 0:
                continue  # Avoid division by zero
            
            vi -= (num / denom) * ortho_basis[j]
        
        if inner_product(vi, vi, points) == 0:
            continue  # Skip zero vectors
        
        ortho_basis.append(sp.simplify(vi))  # Store orthogonal vector
    
    # Normalize the basis
    ortho_normal_basis = [vi / sp.sqrt(inner_product(vi, vi, points)) for vi in ortho_basis]
    
    return [sp.simplify(poly) for poly in ortho_normal_basis]

# Compute the orthonormal basis
orthonormal_basis = gram_schmidt(basis, inner_product, points)

# Print the results
print("Orthonormal basis for P3:")
for i, poly in enumerate(orthonormal_basis):
    print(f"e{i}(x) =", poly)
