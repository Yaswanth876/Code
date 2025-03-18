import sympy as sp

def check_functional_independence(functions, variable):
    wronskian = sp.Matrix(len(functions), len(functions), lambda i, j: sp.diff(functions[i], variable, j)).det()
    return wronskian.simplify()

# Define the variable
x = sp.Symbol('x')

# Define the functions
functions_a = [sp.cos(sp.pi * x), sp.sin(sp.pi * x)]
functions_b = [x**(3/2), x**(5/2)]

# Compute the Wronskian determinant
wronskian_a = check_functional_independence(functions_a, x)
wronskian_b = check_functional_independence(functions_b, x)

# Print results
print("Wronskian for (a):", wronskian_a)
print("Wronskian for (b):", wronskian_b)
