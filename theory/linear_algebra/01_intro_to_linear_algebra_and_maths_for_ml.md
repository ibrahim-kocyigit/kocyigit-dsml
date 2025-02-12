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
* **Optimization:** The process of finding the "best" equation involves adjusting the parameters of the function (e.g., the mean, `μ`, and standard deviation, `σ`, of a Gaussian curve) to minimize the difference between the curve's predictions and the actual data points. This is an optimization problem. Linear algebra provides tools to find the optimal values of these parameters efficiently.
* **Benefits:** Having a compact equation that represents the data offers several advantages:
    * **Concise Representation:** The equation is a much smaller and more manageable representation of the data.
    * **Predictive Power:** The equation can be used to make predictions.
    * **Privacy:** You can share parameters without revealing the raw data.

#### Connection to Data Science

These two examples, solving systems of equations and optimization, are cornerstones of many data science techniques:
* **Linear Regression:** A machine learning algorithm that relies on linear algebra to find the best-fitting line (or hyperplane) through data points.
* **Principal Component Analysis (PCA):** A dimensionality reduction technique using linear algebra to find directions of greatest variance.
* **Support Vector Machines (SVMs):** A classification algorithm using linear algebra to find the optimal hyperplane to separate data.
* **Neural Networks:** Operations within neural networks involve matrix multiplications and linear transformations.

### 1.1.2. Getting a Handle on Vectors

In this section, we'll introduce vectors in the context of data science, building upon the familiar concept of vectors from physics, but expanding their application to broader parameter spaces. The primary motivation is to prepare for optimization problems, particularly fitting functions to data.


#### Revisiting Curve Fitting
Let's visit the example from the previous section: fitting a curve to a histogram representing the distribution of heights in a population.
* **Data:** A histogram showing the frequency of different heights. It's observed that few people are above 2 meters or below 1.5 meters.
* **Goal:** Find a mathematical function that closely matches the shape of the histogram. 
* **Gaussian (Normal) Distribution:** A common choice for modeling such distribution is the Gaussian (or normal) distribution. This function has a bell-curve shape. The specific equation, while provided, isn't the primary focus here:
```
f(x) = (1 / (σ * sqrt(2π))) * exp(- (x - μ)^2 / (2σ^2))
```
Where:
* `x` represents the height (the independent variable).
* `f(x)` represents the frequency or probability density of a given height (the dependent variable).
* `μ` (mu) represents the mean or average height, the center of the distribution.
* `σ` (sigma) represents the standard deviation, a measure of the spread or width of the distribution.
* `exp()` is the exponential function

The important point is that this function is defined by two parameters: `μ` and `σ`.

#### Goodness of Fit and Parameter Space
* **Fitting Process:** To fit the Gaussian curve to the histogram, we need to find the values of `μ` and `σ` that make the curve best match the data.
* **Incorrect Guesses:** If we guess a `σ` that's too wide, the curve will be too flat and wide; it will overestimate the frequencies at the extremes and underestimate them in the middle.
* **Quantifying 'Goodness':** We need a way to measure how well the curve fits the data. A common approach is to calculate the _sum of squared differences_. For each data point in the histogram, we find the difference between the actual frequency and the frequency predicted by the curve, square that difference, and then add up all those squared differences. A smaller sum of squares indicates a better fit.
* **Contour Plot of Goodness:** Imagine a plot where:
    * The x-axis represents different values of `μ`.
    * The y-axis represents different values of `σ`.
    * The z-axis (coming out of the screen/page) represents the "goodness of fit" (or, conversely, the "badness of fit", like the sum of squared differences). Lower values on the z-axis are better.  
    This creates a 3D surface. We can visualize this surface using _contour lines_, similar to a topographical map. Each contour line connects points with the same "goodness fit" value. The goal is to find the lowers point on this surface, representing the best combination of `μ` and `σ`.

#### Vectors in Parameter Space
* **Incremental Changes:** Instead of calculating the goodness of fit for every possible combination of `μ` and `σ`, we can take a more iterative approach. We start with an initial guess for `μ` and `σ`, and then make small adjustments.
* **Vector as Changes:** A vector can represent these adjustments. A vector in this context is simply a list of changes to the parameters. For example, the vector `[Δμ, Δσ]` represents i change of `Δμ` in the mean and `Δσ` in the standard deviation.
* **Example:**
    * Start with initial guess: `[μ, σ]`
    * Create a change vector: `[Δμ, Δσ]`
    * New guess: `[μ + Δμ, σ + Δσ] = [μ', σ']`  
    We then evaluate the goodness of fit at this new point `[μ', σ']`.
* **Finding the Steepest Descent:** Ideally, we want to find the direction in the parameters space `(μ, σ)` that leads to the _steepest decrease_ in the badness of fit (or the _steepest increase_ in the goodness of fit). This analogous to finding the steepest way down a hill on a topographical map. Calculus provides tools (gradients) to determine this direction. 

#### Beyond Geometric Vectors
* **Generalized Definition:** This example demonstrates that vectors are not limited to representing physical displacements in space (as often taught in introductory physics). A vector can represent a list of _any_ quantities.
* **Examples:**
    * **Car Attributes:** A vector could represent characteristics of a car: `[cost, emissions, safety_rating, top_speed]`.
    * **Alloy Composition:** In metallurgy, a vector could represent the proportions of different elements in an alloy.
    * **Spacetime:** In relativity, a vector can represent a point in spacetime: `[x, y, z, t]` (three spatial coordinates and one time coordinate).
* **Data Science Perspective:** From a data science (and computer science) perspective, a vector is essentially an ordered list of numbers. The key is that these numbers represent _quantities_ that are related in some way, and we can perform mathematical operations on them. 
