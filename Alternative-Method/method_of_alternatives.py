import numpy as np

# Function from your Armenian textbook
def f(x):
    return 0.25 * (x**4) + (x**2) - (8*x) + 12

def uniform_search(a, b, epsilon):
    n = int(np.ceil((b - a) / epsilon))
    x_points = np.linspace(a, b, n + 1)
    y_values = [f(x) for x in x_points]
    
    min_val = min(y_values)
    min_x = x_points[y_values.index(min_val)]
    
    return min_x, min_val, n

# Data from page 42 of your textbook
a, b = 0, 2
epsilon = 0.5

x_opt, f_opt, n = uniform_search(a, b, epsilon)

print(f"Results for Method of Alternatives:")
print(f"Number of steps: {n}")
print(f"Minimum found at x = {x_opt}")
print(f"f(x) = {f_opt}")
