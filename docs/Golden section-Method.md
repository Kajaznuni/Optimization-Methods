# Golden Section Search Method

This implementation is based on optimization principles for unimodal functions and improves efficiency compared to uniform search by reducing the number of function evaluations.

## Theoretical Breakdown
The **Golden Section Search Method** is used to find the minimum of a unimodal function $f(x)$ on a closed interval $[a, b]$ without using derivatives.

* **Objective**: Find the minimum of a unimodal function $f(x)$ on the interval $[a, b]$ with precision $\epsilon > 0$.

* **Key Idea**: The method reduces the interval using the golden ratio:
    $$
    \phi = \frac{\sqrt{5} - 1}{2} \approx 0.618
    $$

* **Interior Points**: Two points inside the interval are selected:
    $$
    x_1 = a + (1 - \phi)(b - a)
    $$
    $$
    x_2 = a + \phi (b - a)
    $$

* **Function Evaluation**: Compute $f(x_1)$ and $f(x_2)$.

* **Interval Reduction Rule**:
    - If $f(x_1) > f(x_2)$, then the minimum lies in $[x_1, b]$, so set $a = x_1$
    - Otherwise, the minimum lies in $[a, x_2]$, so set $b = x_2$

* **Reuse Property**: One of the interior points is reused in the next iteration, reducing computations.

* **Stopping Condition**:
    $$
    |b - a| \le \epsilon
    $$

* **Approximate Solution**:
    $$
    x^* = \frac{a + b}{2}
    $$

* **Error Bound**:
    $$
    \epsilon_n = |b - a|
    $$

---

## Python Implementation

```python
def golden_section_search(f, a, b, tol=1e-5):
    phi = (5**0.5 - 1) / 2

    x1 = a + (1 - phi) * (b - a)
    x2 = a + phi * (b - a)

    f1 = f(x1)
    f2 = f(x2)

    while abs(b - a) > tol:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + phi * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (1 - phi) * (b - a)
            f1 = f(x1)

    return (a + b) / 2
