import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
# Define the variable and parameter
x, alpha = sp.symbols('x alpha')
# Define the functions
f1 = sp.cos(x + alpha)
f2 = sp.sin(x)
# Compute the Wronskian determinant
wronskian = sp.Matrix([
    [f1, f2],
    [sp.diff(f1, x), sp.diff(f2, x)]
]).det().simplify()
# Solve for values of alpha where Wronskian is zero
alpha_values = sp.solveset(wronskian, alpha, domain=sp.S.Reals)
# Plot the functions for a few values of alpha
x_vals = np.linspace(-np.pi, np.pi, 400)
plt.figure(figsize=(10, 5))
for a in np.linspace(-np.pi, np.pi, 5):
    plt.plot(x_vals, np.cos(x_vals + a), label=f'cos(x + {a:.2f})')
plt.plot(x_vals, np.sin(x_vals), 'k--', label='sin(x)', linewidth=2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Graphical Interpretation of Linear Dependence")
plt.show()
# Print the values of alpha where the functions are dependent
print("Values of α for linear dependence:", alpha_values)
