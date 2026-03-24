                                                         Optimization Methods
            
Finding the Minimum of a Function

This repository demonstrates three popular numerical optimization techniques for locating the minimum of a single-variable function:
Uniform Search (Method of Alternatives)
Bisection Method
Golden Section Search
We use the following example function throughout:


f(x)=0.25x^4+x^2−8x+12

These methods are fundamental in mathematics, engineering, and data science when solving optimization problems or minimizing functions efficiently.
-
Overview of Methods
-
1. Alternative Method
-   
How it works: The interval is divided into evenly spaced points. Each point is evaluated, and the smallest function value is selected.
Pros: Simple and straightforward.
Cons: Requires many evaluations for higher accuracy.

2. Bisection Method
-
How it works: Uses the derivative of the function to iteratively shrink the interval containing the minimum. The derivative’s sign indicates which subinterval contains the minimum.
Pros: Fast for unimodal functions; reliable convergence.
Cons: Needs the derivative of the function.

3. Golden Section Search
-
How it works: A derivative-free method that progressively narrows the search interval using the golden ratio, honing in on the minimum.
Pros: Efficient and does not require derivatives; fewer function evaluations needed.
Cons: Slightly more complex than uniform search.
