# Golden Section Search Method

## Overview
The **Golden Section Search** is a technique for finding the minimum of a unimodal function on a closed interval $[a, b]$.  
It is efficient and does not require derivatives.

---

## Key Idea
The method reduces the search interval using the **golden ratio**:

$$
\phi = \frac{\sqrt{5} - 1}{2} \approx 0.618
$$

Two interior points are selected:

$$
x_1 = a + (1 - \phi)(b - a)
$$

$$
x_2 = a + \phi (b - a)
$$

---

## Algorithm

1. **Initialize**
   - Choose interval $[a, b]$
   - Set tolerance $\varepsilon$

2. **Compute points**
   $$
   x_1 = a + 0.3819 (b - a)
   $$
   $$
   x_2 = a + 0.6180 (b - a)
   $$

3. **Evaluate function**
   - Compute $f(x_1)$ and $f(x_2)$

4. **Update interval**
   - If $f(x_1) > f(x_2)$:
     $$
     a = x_1
     $$
   - Else:
     $$
     b = x_2
     $$

5. **Stopping condition**
   $$
   |b - a| \leq \varepsilon
   $$

6. **Approximate solution**
   $$
   x^* = \frac{a + b}{2}
   $$

---

## Advantages
- No derivative required  
- Efficient interval reduction  
- Guaranteed convergence for unimodal functions  

---

## Disadvantages
- Slower than derivative-based methods  
- Requires unimodality assumption  

---
