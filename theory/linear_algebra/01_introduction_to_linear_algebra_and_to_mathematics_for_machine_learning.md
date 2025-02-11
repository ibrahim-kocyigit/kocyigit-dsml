# 1. Introduction to Linear Algebra and to Mathematics for Machine Learning

## 1.1. The Relationship Between Machine Learning, Linear Algebra, and Vectors and Matrices

### 1.1.1. Introduction to Linear Algebra: Motivations

Linear Algebra is a powerful set of mathematical tools used to solve a wide range of problems, especially those involving data.  Let's look at two motivating examples:

#### 1. Price Discovery (The Apple and Banana Mystery)

Imagine you go to the store twice and buy different amounts of apples and bananas. Each time, you get a total cost. Your challenge? Figure out the individual price of an apple and a banana.  We can represent this using a system of equations. Let 'a' be the price of an apple and 'b' be the price of a banana. Your shopping trips might look like this:

*   Trip 1: 2a + 3b = 8 (2 apples and 3 bananas cost 8 Euros)
*   Trip 2: 10a + 1b = 13 (10 apples and 1 banana cost 13 Euros)

Linear Algebra provides the tools to solve these equations quickly and efficiently, even if you have hundreds of items and shopping trips. It uses special mathematical objects called *vectors* (think of them as ordered lists of numbers, like [a, b] representing the prices) and *matrices* (think of them as grids of numbers). These tools help organize the information and make the calculations much easier, especially for computers.

**2. Data Fitting (Finding the Hidden Pattern)**

Let's say you have a bunch of data points, like a histogram showing population data. It looks messy, but you suspect there's a pattern. You want to find an equation that best describes this data. This is called "fitting" an equation to the data. Linear Algebra helps you find the best values for the *parameters* in that equation. Think of parameters as knobs you can tweak to make the equation fit the data better.

Why is this useful? Because once you have the equation, you can easily describe the data without needing to store all the individual data points. It's like finding a simple formula that captures the essence of the data. This is especially important for things like privacy concerns or when dealing with huge datasets. Instead of sharing all the individual data points, you can just share the equation.

**Key Concepts:**

*   **Simultaneous Equations:** A set of equations with multiple unknowns that you solve together (like our apple and banana example).
*   **Linear Coefficients:** The numbers you multiply your unknowns by (like the 2, 3, 10, and 1 in the apple and banana example). They determine how much each unknown contributes to the final result.
*   **Vectors and Matrices:** Think of these as organized ways to store and manipulate numbers. Vectors are like lists, and matrices are like tables. They are fundamental tools in Linear Algebra.
*   **Parameters:** Values that control the shape or behavior of an equation. We adjust these to make the equation fit our data.
*   **Optimization:** Finding the best solution, like the equation that best fits the data.

These two problems (price discovery and data fitting) serve as excellent examples of why we study Linear Algebra. They demonstrate how these mathematical tools can be used to solve real-world problems.

