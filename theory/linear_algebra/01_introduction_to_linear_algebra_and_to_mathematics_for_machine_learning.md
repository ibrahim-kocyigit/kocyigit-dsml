# 1. Introduction to Linear Algebra and to Mathematics for Machine Learning

## 1.1. The Relationship Between Machine Learning, Linear Algebra, and Vectors and Matrices

### 1.1.1. Motivations for Linear Algebra

* Think of Linear Algebra as a toolbox of mathematical techniques that are incredibly useful in many fields.
* **Problem 1: Price Discovery (Apples and Bananas)**
    * Imagine you go to the store twice and buy different amounts of apples and bananas.  Each time, you get a total cost.  Linear Algebra helps you figure out the individual price of an apple and a banana.  This is done by setting up a system of equations (like the ones with "A" and "B" for the prices) and then solving them.  While you can do this by hand for a small number of items,  Linear Algebra provides tools (like matrices and vectors) that allow computers to solve these equations even when you have tons of items and shopping trips, making it much more efficient.

**Problem 2: Data Fitting**

Let's say you have a bunch of data points, like a histogram showing population data. You want to find an equation that best describes this data.  This is called "fitting" an equation to the data.  Linear Algebra helps find the best values for the parameters in that equation.  Why is this useful?  Because once you have the equation, you can easily describe the data without needing to store all the individual data points. This is especially important for things like privacy concerns.

**Key Concepts Introduced:**

*   **Simultaneous Equations:** These are equations with multiple unknowns (like the prices of apples and bananas) that you solve together.
*   **Linear Coefficients:**  These are the numbers you multiply your unknowns by (like the 2, 3, 10, and 1 in the apple and banana example).
*   **Vectors and Matrices:** These are mathematical objects that Linear Algebra uses to organize and manipulate data. Think of them as containers for numbers. Vectors are like lists of numbers, and matrices are like tables of numbers. They are fundamental in Linear Algebra and are used to represent and solve these kinds of problems.
*   **Optimization:**  Finding the best solution to a problem, like finding the equation that best fits the data.

The video explains that these two problems (price discovery and data fitting) will be used throughout the course to motivate the study of Linear Algebra and its close partner, multivariate calculus.  Basically, these problems give you a reason to learn the math!
