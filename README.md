Optimization Methods: Finding the Minimum of a Function
This repository demonstrates three classical numerical optimization methods for finding the minimum of a single-variable function:
Uniform Search (Method of Alternatives)
Bisection Method
Golden Section Search
The example function used in this project is:
f
(
x
)
=
0.25
x
4
+
x
2
−
8
x
+
12
f(x)=0.25x 
4
 +x 
2
 −8x+12
These methods are widely used in engineering, mathematics, and data science for function minimization and optimization problems.
Methods Overview
1. Uniform Search (Method of Alternatives)
Concept: Divide the search interval into equally spaced points and evaluate the function at each point. The minimum is approximated from these points.
Pros: Simple and easy to implement.
Cons: Can be inefficient if high accuracy is needed.
2. Bisection Method
Concept: Uses the derivative of the function to find the minimum by iteratively halving the interval and checking where the derivative changes sign.
Pros: Efficient for unimodal functions; linear convergence.
Cons: Requires the derivative of the function.
3. Golden Section Search
Concept: A derivative-free method that narrows the search interval using the golden ratio. Efficient for unimodal functions.
Pros: Fast, derivative-free, and converges reliably.
Cons: Slightly more complex than uniform search.
