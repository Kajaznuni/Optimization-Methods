# Golden Section Search Method

## Overview
The Golden Section Search is a technique for finding the minimum of a unimodal function on a closed interval [a, b].  
It is efficient and does not require derivatives.

---

## Key Idea
The method reduces the search interval using the golden ratio:

phi = (sqrt(5) - 1) / 2 ≈ 0.618

Two interior points are selected:

x1 = a + (1 - phi)(b - a)  
x2 = a + phi (b - a)

---

## Algorithm

1. Initialize
   - Choose interval [a, b]
   - Set tolerance epsilon

2. Compute points
   x1 = a + 0.3819 (b - a)  
   x2 = a + 0.6180 (b - a)

3. Evaluate function
   - Compute f(x1) and f(x2)

4. Update interval
   - If f(x1) > f(x2):
       a = x1
   - Else:
       b = x2

5. Stopping condition
   |b - a| ≤ epsilon

6. Approximate solution
   x* = (a + b) / 2

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
