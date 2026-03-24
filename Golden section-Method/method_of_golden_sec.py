import numpy as np

# Function from textbook
def f(x):
    return 0.25 * (x**4) + (x**2) - (8*x) + 12

def golden_section_search(a, b, tol=0.01):
    phi = (1 + np.sqrt(5)) / 2  # golden ratio
    resphi = 2 - phi  # 1/phi^2
    
    # Initial interior points
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    
    f1 = f(x1)
    f2 = f(x2)
    
    n = 0  # count iterations
    
    while abs(b - a) > tol:
        n += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = f(x2)
    
    # Minimum is at the midpoint of final interval
    x_min = (a + b) / 2
    f_min = f(x_min)
    
    return x_min, f_min, n

# Using the golden section method
a, b = 0, 2
tol = 0.01

x_opt, f_opt, n_steps = golden_section_search(a, b, tol)

print(f"Results for Golden Section Method:")
print(f"Number of steps: {n_steps}")
print(f"Minimum found at x = {x_opt}")
print(f"f(x) = {f_opt}")
