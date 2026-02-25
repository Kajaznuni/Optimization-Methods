# 2.2 Half-Interval (Bisection) Method

This method is used to find the minimum of a unimodal function $f(x)$ on a closed interval $[a, b]$ with precision $\epsilon > 0$.

## Mathematical Background
Based on the textbook, the algorithm follows these steps:

* **Initialization**: Choose $\delta \in (0, 2\epsilon)$ and set $a_0 = a, b_0 = b$.
* **Iteration**: At each step $k$, calculate two points:
  $$x_1^{(k)} = \frac{a_k + b_k - \delta}{2}, \quad x_2^{(k)} = \frac{a_k + b_k + \delta}{2}$$
* **Logic**:
    * If $f(x_1^{(k)}) \le f(x_2^{(k)})$, the new interval becomes $[a_k, x_2^{(k)}]$.
    * If $f(x_1^{(k)}) > f(x_2^{(k)})$, the new interval becomes $[x_1^{(k)}, b_k]$.
* **Termination**: The process ends when $|b_n - a_n| \le \epsilon$.



## Numerical Example (Page 45)
For the function $f(x) = \frac{1}{4}x^4 + x^2 - 8x + 12$ on interval $[0, 2]$ with $\epsilon = 0.05$ and $\delta = 0.1$:

| $k$ | $x_m = 0.5(a_k + b_k)$ | $f(x^*)$ |
| :--- | :--- | :--- |
| 0 | 1 | 5.2562 |
| 1 | 1.4750 | 3.5695 |
| 2 | 1.7125 | 3.3962 |
