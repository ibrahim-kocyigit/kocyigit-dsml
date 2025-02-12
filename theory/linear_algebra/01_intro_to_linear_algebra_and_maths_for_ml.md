# 1. Introduction to Linear Algebra and to Mathematics for Machine Learning

## 1.1. The Relationship Between Machine Learning, Linear Algebra, and Vectors and Matrices

### 1.1.1. Motivations for Linear Algebra

Linear Algebra is a fundamental branch of mathematics that is extremely useful in data science. It provides the tools and concepts needed to work with large datasets, solve systems of equations, and perform optimization, which are all crucial tasks in many data science applications.

#### Price Discovery: Solving Simultaneous Equations
A common problem in data science involves finding unknown values that satisfy multiple linear relationships. Consider a simplified example of price discovery:
* **Scenario:** You go shopping on two separate occasions.
    * **Trip 1:** You buy 2 apples and 3 bananas, and the total cost is 8 euros.
    * **Trip 2:** You buy 10 apples and 1 banana, and the total cost is 13 euros.
* **Goal:** Determine the price of a single apple (`a`) and (`b`).
* **Mathematical Representation:** We can represent this situation with a system of linear equations:
```
2a + 3b = 8
10a + b = 13
```
* **Generalization:** In a real-world scenario, you might have many items (products) and many shopping trips (observations). Manually solving such a large system of equation is impractical. Linear algebra provides methods for efficiently solving these systems, even with a very large number of variables and equations, using computer algorithms.
* **Matrix Representation:** The system of equations can be written in a compact matrix form:
```
[2  3] [a] = [8 ]
[10 1] [b] = [13]
```
Where:
* The matrix `[2, 3 ; 10 1]` represents the coefficients of the variables (quantities of apples and bananas). We can call this matrix `M`.
* The vector `[a ; b]` represents the unknown variables (prices of apples and bananas). We can call this vector `v`.
* The vector `[8 ; 13]` represents the constants (total costs). We can call this vector `c`.
This can be written more abstractly as:
```
M v = c
```
Where `M` is the matrix of coefficients, `v` is the vector of unknowns, and `c` is the vector of constants. One of the core goals of linear algebra is to develop techniques to solve for `v` in equations of this form.

#### Curve Fitting and optimization

Another crucial application of linear algebra is in fitting equations to data, a fundamental task in machine learning and statistical modeling.
* **Scenario:** Imagine you have a dataset represented as a histogram. The data points appear to follow a certain pattern (e.g., a bell-shaped curve or Gaussian distribution).
* **Goal:** Find an equation (a mathematical function) that best describes the relationship between the variables in the data. For instance, you might want to fit a Gaussian curve to the histogram. This Gaussian will have parameters that needs to be fitted.
* **Example:** The equation is going to look like a function, and the parameters of the function might describe, for instance, the average and standard deviation of a gaussian curve.
* **Optimization:** The process of finding the "best" equation involves adjusting the parameters of the function (e.g., the mean, `μ`, and standard deviation, `σ`, of a Gaussian curve)