# Linear Algebra Applied - II 

In the previous section, we established that a linear regression model with $n$ features and $m$ data records can be represented as a system of linear equations:

* **Record 1**: $w_1x_1^{(1)} + w_2x_2^{(1)} + \dots + w_nx_n^{(1)} + b = y^{(1)}$
* **Record 2**: $w_1x_1^{(2)} + w_2x_2^{(2)} + \dots + w_nx_n^{(2)} + b = y^{(2)}$
* ...
* **Record m**: $w_1x_1^{(m)} + w_2x_2^{(m)} + \dots + w_nx_n^{(m)} + b = y^{(m)}$

An important thing to remember is that the **weights ($w$)** and the **bias ($b$)** are the **same for all equations**. We are looking for a single set of these values that works for every record in our dataset. The features ($x$) and targets ($y$) are unique to each row.

---

## A More Compact Notation: Vectors and Matrices

Writing out the full system of equations can be cumbersome. Linear algebra gives us a much more efficient way to represent this using **vectors** and **matrices**.

For now, you can think of them simply as:
* **Vector**: A list of numbers.
* **Matrix**: A grid of numbers (a collection of vectors).

Using this, we can simplify our entire system of equations into a single, elegant line:

$$ y = WX + b $$

* $W$ is now a **vector** containing all the weights ($w_1, w_2, \dots, w_n$).
* $X$ is a **matrix** where each row contains the features for a single data record.
* $b$ is the bias term.
* $y$ is a **vector** of all the target outputs ($y^{(1)}, y^{(2)}, \dots, y^{(m)}$).

This compact form is the backbone of how we perform calculations in machine learning.

*(Note: If you're already familiar with linear algebra, you might notice we're being a bit imprecise here. Depending on how we define our vectors and matrices, we might need to use a transpose ($`W^T`$) to make the math work. We'll ignore that detail for now to focus on the core concept.)*

--- 

## Analytical vs. Empirical Solutions

When you have a system of linear equations, there are two general ways to "solve" it.

* **Analytical Solution**: This is what you do with a pencil and paper. Using algebraic methods like substitution or elimination, you can find the *exact* values for your unknowns. This is possible if you have a "perfect" system, often where the number of unique equations matches the number of unknown variables.

* **Empirical Solution**: This is the machine learning approach. In reality, data is noisy and a perfect solution rarely exists. Linear regression finds the best *approximate* solution by iteratively adjusting the weights and bias to minimize the error. It's an empirical, or data-driven, way of finding the best-fit line or plane.

---

## A New Problem: What Are Your Scores? 🤔

Let's frame a new problem to explore these concepts. Imagine you took three courses: **Linear Algebra**, **Calculus**, and **Probability & Statistics**. I know your scores, but I won't tell you directly. Instead, I'll give you these three facts:

1.  Your Linear Algebra score plus your Calculus score minus your Probability & Statistics score is **6**.
2.  Your Linear Algebra score minus your Calculus score plus double your Probability & Statistics score is **4**.
3.  Four times your Linear Algebra score minus double your Calculus score plus your Probability & Statistics score is **10**.

Can we use this information to figure out your exact scores? Let's turn these sentences into a system of linear equations.

--- 

## Formulating the System of Equations

Let's assign variables to our unknown scores:
* $a$ = Linear Algebra score
* $c$ = Calculus score
* $p$ = Probability & Statistics score

Now we can translate the sentences into equations:

1.  $a + c - p = 6$
2.  $a - c + 2p = 4$
3.  $4a - 2c + p = 10$

This is a classic system of linear equations. Since we have 3 distinct equations and 3 unknowns, we might be able to solve this analytically (We will cover how to solve systems of linear equations later).

---

## Relating This Back to Machine Learning

Our course-score problem is a perfect analogy for the components of a machine learning model. In linear algebra, we represent these components efficiently using **vectors** (a column of numbers) and **matrices** (a grid of numbers). This allows us to write a complex system of equations in a very simple form.

### Weights (The Unknowns) - Vector $w$

The **weights** are the unknown values we are trying to solve for. In machine learning, these are the parameters the model "learns."

* In our problem, the unknowns are the scores: $a, c, p$.
* We collect these into a single column **vector**:  

$`
w = \begin{bmatrix} a \\ c \\ p \end{bmatrix} 
`$

### Features (The Known Coefficients) - Matrix $X$

The **features** are the known coefficients that multiply each of our unknown weights. In a real dataset, these would be your input data points.

* We collect all the features from our system of equations into a **matrix**, which we can call $X$. Each row in the matrix corresponds to one of our equations: 

$`
X = \begin{bmatrix}
1 & 1 & -1 \\
1 & -1 & 2 \\
4 & -2 & 1
\end{bmatrix}
`$

### Targets (The Known Outcomes) - Vector $y$

The **targets** are the known results on the other side of the equal sign. In a dataset, this would be the "correct answer" for each row of features.

* In our problem, the targets are the equation outcomes: 6, 4, 10.
* We collect these into a column **vector**, which we can call:  
 
$`
y = \begin{bmatrix} 6 \\ 4 \\ 10 \end{bmatrix}
`$

### The Full Picture: $Xw = y$

When we put it all together, our entire system of three separate equations can be written in a single, compact matrix-vector equation: **$Xw = y$**.  

Visually, that looks like this:  

$`
\begin{bmatrix}
1 & 1 & -1 \\
1 & -1 & 2 \\
4 & -2 & 1
\end{bmatrix}
\begin{bmatrix} a \\ c \\ p \end{bmatrix}
`$=
`$
\begin{bmatrix} 6 \\ 4 \\ 10 \end{bmatrix}
`$ 

This elegant notation is fundamental to linear algebra and is used everywhere in machine learning to represent data and solve complex problems.

