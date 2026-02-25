import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.25 * (x**4) + (x**2) - (8*x) + 12

# Parameters from textbook
a, b = 0, 2
epsilon = 0.5
n = int(np.ceil((b - a) / epsilon))

# Generate smooth curve for the function
x_curve = np.linspace(a, b, 100)
y_curve = f(x_curve)

# Generate search nodes (x_k)
x_nodes = np.linspace(a, b, n + 1)
y_nodes = f(x_nodes)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_curve, y_curve, label='f(x)', color='blue', linewidth=2)
plt.scatter(x_nodes, y_nodes, color='red', zorder=5, label='Search Nodes (x_k)')

# Add labels for the nodes matching the textbook table
for x, y in zip(x_nodes, y_nodes):
    plt.text(x, y + 0.5, f'{y:.4f}', ha='center', fontsize=9)

# Formatting to match textbook style
plt.title('Method of Alternatives: Uniform Search Grid')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xlim(a - 0.2, b + 0.2)
plt.ylim(min(y_curve) - 1, max(y_curve) + 1)

# Save the plot as an image to display in README
plt.savefig('optimization_plot.png')
plt.show()
