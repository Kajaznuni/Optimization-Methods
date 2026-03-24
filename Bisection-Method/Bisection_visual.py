import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.25 * (x**4) + (x**2) - (8*x) + 12

def bisection_with_plot(a, b, eps, delta):
    x_range = np.linspace(a - 0.5, b + 0.5, 500)
    y_range = f(x_range)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, 'b-', label='f(x)')
    plt.axhline(0, color='black', lw=1)
    
    colors = ['red', 'green', 'orange', 'purple']
    step = 0
    
    while (b - a) > eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        
        # Գծում ենք ընթացիկ հատվածը և կետերը
        plt.scatter([x1, x2], [f(x1), f(x2)], color=colors[step % len(colors)], 
                    label=f'Step {step}: [a={a:.2f}, b={b:.2f}]')
        plt.vlines([a, b], 0, f(a), linestyles='dashed', alpha=0.3)

        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        step += 1

    plt.title('Bisection Method Optimization Steps')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('bisection_plot.png')
    plt.show()

# Հաշվարկ գրքի տվյալներով
bisection_with_plot(0, 2, 0.5, 0.1)
