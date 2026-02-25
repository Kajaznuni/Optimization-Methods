import numpy as np

def f(x):
    # Textbook function: f(x) = 1/4x^4 + x^2 - 8x + 12
    return 0.25 * (x**4) + (x**2) - (8*x) + 12

def bisection_method(a, b, eps, delta):
    step = 0
    while (b - a) > eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        
        step += 1
        print(f"Step {step}: Interval = [{a:.4f}, {b:.4f}]")
    
    x_opt = (a + b) / 2
    return x_opt, f(x_opt)

# Input data from textbook page 45
a_val, b_val = 0, 2
epsilon = 0.5
delta_val = 0.1

result_x, result_f = bisection_method(a_val, b_val, epsilon, delta_val)
print(f"\nResult: x ≈ {result_x:.4f}, f(x) ≈ {result_f:.4f}")
